"""Private parent boundary; the parent owns cancellation, limits, and reaping."""

from __future__ import annotations

import json
import os
import resource
import selectors
import subprocess
import sys
import time
from collections.abc import Callable, Mapping
from dataclasses import fields, is_dataclass
from pathlib import Path

from .identity import verify_decoder
from .ipc import REQUEST, RESULT, encode_frame, read_frame
from .model import (
    HARD_LIMITS,
    REGRESSION_LIMITS,
    DecodeRequest,
    DecodeResult,
    HostFailure,
    WorkerFailure,
    decode_result_from_dict,
)


class CancellationToken:
    """Parent-owned one-way cancellation state for this private boundary."""

    def __init__(self) -> None:
        self._cancelled = False

    def cancel(self) -> None:
        self._cancelled = True

    @property
    def cancelled(self) -> bool:
        return self._cancelled


def decode_private(
    request: DecodeRequest, cancellation: CancellationToken | None = None
) -> DecodeResult:
    """Run one fresh fixed worker only after identity and request preflight succeed."""
    return _decode_with_factory(request, subprocess.Popen, cancellation)


def _decode_with_factory(
    request: DecodeRequest,
    process_factory: Callable[..., subprocess.Popen[bytes]],
    cancellation: CancellationToken | None = None,
    measure_rss: Callable[[], int] | None = None,
    monotonic_ns: Callable[[], int] = time.monotonic_ns,
    measure_decoded: Callable[[object], int] | None = None,
    measure_retained: Callable[[object], int] | None = None,
) -> DecodeResult:
    """Injection seam for inert preflight-order tests; never exposed by the package."""
    run_started = monotonic_ns()
    rss = measure_rss or _parent_rss
    parent_before = rss()
    if cancellation is not None and cancellation.cancelled:
        raise HostFailure("cancelled")
    identity = verify_decoder(request.decoder)
    payload = encode_frame(
        REQUEST,
        {
            "decoder": identity.decoder,
            "file_set_sha256": identity.file_set_sha256,
            "samplerate_hz": request.samplerate,
            "channel_ids": list(request.channel_ids),
            "mapping": dict(request.mapping),
            "samples": list(request.samples),
            "trigger_index": request.trigger_index,
            "options": dict(request.options),
        },
        HARD_LIMITS["request_bytes"],
    )
    launch_started = monotonic_ns()
    process, response_fd = _spawn_fixed_worker(process_factory, payload)
    response: Mapping[str, object] | None = None
    stdout = b""
    stderr = b""
    try:
        _validate_elapsed(monotonic_ns() - launch_started, REGRESSION_LIMITS["launch_ns"])
        response, stdout, stderr = _collect_response(process, response_fd, cancellation)
        try:
            reap_started = monotonic_ns()
            process.wait(timeout=HARD_LIMITS["terminate_grace_ms"] / 1000)
            if monotonic_ns() - reap_started > REGRESSION_LIMITS["reap_ns"]:
                raise HostFailure("process-exit")
        except subprocess.TimeoutExpired:
            raise HostFailure("process-exit") from None
    except TimeoutError:
        _terminate_reap(process, response_fd)
        raise HostFailure("timeout") from None
    except InterruptedError:
        _terminate_reap(process, response_fd)
        raise HostFailure("cancelled") from None
    except WorkerFailure as error:
        _terminate_reap(process, response_fd)
        # A child that exits unsuccessfully before completing its frame is a
        # process failure, not an IPC claim from its untrusted byte stream.
        if str(error) == "output limit":
            raise HostFailure("output-limit") from None
        if process.returncode != 0:
            raise HostFailure("process-exit") from None
        raise HostFailure("ipc") from None
    except (OSError, ValueError):
        _terminate_reap(process, response_fd)
        raise HostFailure("ipc") from None
    except HostFailure:
        _terminate_reap(process, response_fd)
        raise
    finally:
        try:
            os.close(response_fd)
        except OSError:
            pass
    _close_standard_pipes(process)
    if (
        process.returncode != 0
        or (response is not None and response.get("type") == RESULT and bool(stdout))
        or (response is not None and response.get("type") == RESULT and bool(stderr))
        or len(stdout) > HARD_LIMITS["stdout_bytes"]
        or len(stderr) > HARD_LIMITS["stderr_bytes"]
    ):
        raise HostFailure("process-exit")
    if response is None:
        raise HostFailure("ipc")
    result = response.get("result")
    if response.get("type") == "decode-failure":
        code = response.get("code")
        if code in {"snapshot", "import", "ipc", "decoder", "recursion", "memory", "output-limit"}:
            raise HostFailure(str(code))
        raise HostFailure("decoder")
    if response.get("type") != RESULT or not isinstance(result, Mapping):
        raise HostFailure("decode protocol rejected")
    _validate_worker_metrics(response.get("metrics"))
    _enforce_result_limits(result, measure_decoded, measure_retained)
    try:
        materialized = decode_result_from_dict(result)
    except HostFailure:
        raise HostFailure("ipc") from None
    _validate_elapsed(monotonic_ns() - run_started, REGRESSION_LIMITS["successful_parent_total_ns"])
    _validate_parent_growth(parent_before, rss())
    return materialized


def _validate_worker_metrics(value: object) -> None:
    """Metrics are required protocol fields from the hash-pinned worker, never hints."""
    if not isinstance(value, Mapping) or set(value) != {
        "child_import_ns",
        "child_load_ns",
        "child_decode_ns",
        "worker_peak_rss_bytes",
    }:
        raise HostFailure("ipc")
    caps = {
        "child_import_ns": REGRESSION_LIMITS["child_import_ns"],
        "child_load_ns": REGRESSION_LIMITS["child_load_ns"],
        "child_decode_ns": REGRESSION_LIMITS["child_decode_ns"],
        "worker_peak_rss_bytes": REGRESSION_LIMITS["worker_peak_rss_bytes"],
    }
    if any(
        type(value[name]) is not int or value[name] < 0 or value[name] > cap
        for name, cap in caps.items()
    ):
        raise HostFailure("process-exit")


def _validate_elapsed(elapsed: int, limit: int) -> None:
    if type(elapsed) is not int or elapsed < 0 or elapsed > limit:
        raise HostFailure("process-exit")


def _parent_rss() -> int:
    """Approved B1 parent measurement: macOS ru_maxrss is already bytes."""
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if type(value) is not int or value < 0:
        raise HostFailure("process-exit")
    return value


def _validate_parent_growth(before: int, after: int) -> None:
    if type(before) is not int or type(after) is not int or after < before:
        raise HostFailure("process-exit")
    if after - before > REGRESSION_LIMITS["parent_retained_growth_bytes"]:
        raise HostFailure("process-exit")


def _collect_response(
    process: subprocess.Popen[bytes], response_fd: int, cancellation: CancellationToken | None
) -> tuple[Mapping[str, object], bytes, bytes]:
    """Selector-driven bounded drain; no background readers survive this call."""
    buffers = {"response": bytearray(), "stdout": bytearray(), "stderr": bytearray()}
    sources: list[tuple[str, int]] = [("response", response_fd)]
    if process.stdout is not None:
        sources.append(("stdout", process.stdout.fileno()))
    if process.stderr is not None:
        sources.append(("stderr", process.stderr.fileno()))
    selector = selectors.DefaultSelector()
    for name, fd in sources:
        selector.register(fd, selectors.EVENT_READ, name)
    deadline = time.monotonic() + HARD_LIMITS["wall_deadline_ms"] / 1000
    try:
        while selector.get_map():
            if cancellation is not None and cancellation.cancelled:
                raise InterruptedError
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError
            for key, _ in selector.select(min(remaining, 0.05)):
                data = os.read(key.fd, 65537)
                if not data:
                    selector.unregister(key.fd)
                    continue
                name = key.data
                buffers[name].extend(data)
                if len(buffers[name]) > _pipe_limit(name):
                    raise WorkerFailure("output limit")
    finally:
        selector.close()
    return (
        read_frame(_reader(bytes(buffers["response"])), HARD_LIMITS["encoded_bytes"]),
        bytes(buffers["stdout"]),
        bytes(buffers["stderr"]),
    )


def _pipe_limit(name: str) -> int:
    return HARD_LIMITS["encoded_bytes"] + 4 if name == "response" else HARD_LIMITS[f"{name}_bytes"]


def _drain_pipes(process: subprocess.Popen[bytes]) -> tuple[bytes, bytes]:
    return (
        process.stdout.read() if process.stdout is not None else b"",
        process.stderr.read() if process.stderr is not None else b"",
    )


def _decoded_bytes(value: object) -> int:
    """Count canonical decoded JSON independently of its framed representation."""
    try:
        return len(json.dumps(value, allow_nan=False, separators=(",", ":")).encode())
    except (TypeError, ValueError):
        raise HostFailure("ipc") from None


def _enforce_result_limits(
    raw_result: object,
    measure_decoded: Callable[[object], int] | None = None,
    measure_retained: Callable[[object], int] | None = None,
) -> None:
    """Apply B1's raw settled-result accounting before typed materialization."""
    decoded = (measure_decoded or _decoded_bytes)(raw_result)
    retained = (measure_retained or _deep_size)(raw_result)
    if (
        type(decoded) is not int
        or type(retained) is not int
        or decoded < 0
        or retained < 0
    ):
        raise HostFailure("ipc")
    if decoded > HARD_LIMITS["decoded_bytes"] or retained > HARD_LIMITS["retained_result_bytes"]:
        raise HostFailure("output-limit")


def _deep_size(value: object, seen: set[int] | None = None) -> int:
    """Cycle-safe retained object accounting; shared references count once."""
    visited = seen if seen is not None else set()
    identity = id(value)
    if identity in visited:
        return 0
    visited.add(identity)
    total = sys.getsizeof(value)
    if isinstance(value, Mapping):
        return total + sum(
            _deep_size(key, visited) + _deep_size(item, visited)
            for key, item in value.items()
        )
    if isinstance(value, tuple | list | set | frozenset):
        return total + sum(
            _deep_size(item, visited) for item in value
        )
    if is_dataclass(value):
        return total + sum(
            _deep_size(getattr(value, field.name), visited) for field in fields(value)
        )
    if hasattr(value, "__dict__"):
        return total + _deep_size(vars(value), visited)
    return total


def _terminate_reap(process: subprocess.Popen[bytes], *fds: int) -> None:
    cleanup_started = time.monotonic_ns()
    terminate_started: int | None = None
    kill_started: int | None = None
    try:
        if process.poll() is None:
            terminate_started = time.monotonic_ns()
            process.terminate()
            try:
                process.wait(HARD_LIMITS["terminate_grace_ms"] / 1000)
            except subprocess.TimeoutExpired:
                kill_started = time.monotonic_ns()
                process.kill()
                process.wait()
    finally:
        for fd in fds:
            try:
                os.close(fd)
            except OSError:
                pass
        _close_standard_pipes(process)
    _validate_cleanup_times(
        time.monotonic_ns() - cleanup_started,
        None if terminate_started is None else time.monotonic_ns() - terminate_started,
        None if kill_started is None else time.monotonic_ns() - kill_started,
    )


def _validate_cleanup_times(
    total_ns: int, terminate_to_reap_ns: int | None, kill_to_reap_ns: int | None
) -> None:
    if (
        type(total_ns) is not int
        or total_ns < 0
        or total_ns > REGRESSION_LIMITS["timeout_cleanup_total_ns"]
    ):
        raise HostFailure("process-exit")
    if terminate_to_reap_ns is not None and (
        type(terminate_to_reap_ns) is not int
        or terminate_to_reap_ns < 0
        or terminate_to_reap_ns > REGRESSION_LIMITS["terminate_to_reap_ns"]
    ):
        raise HostFailure("process-exit")
    if kill_to_reap_ns is not None and (
        type(kill_to_reap_ns) is not int
        or kill_to_reap_ns < 0
        or kill_to_reap_ns > REGRESSION_LIMITS["kill_to_reap_ns"]
    ):
        raise HostFailure("process-exit")


def _close_standard_pipes(process: subprocess.Popen[bytes]) -> None:
    for pipe in (process.stdout, process.stderr):
        if pipe is not None:
            try:
                pipe.close()
            except OSError:
                pass


def _spawn_fixed_worker(
    process_factory: Callable[..., subprocess.Popen[bytes]], payload: bytes
) -> tuple[subprocess.Popen[bytes], int]:
    request_read, request_write = os.pipe()
    response_read, response_write = os.pipe()
    os.set_inheritable(request_read, True)
    os.set_inheritable(response_write, True)
    try:
        worker = Path(__file__).with_name("worker.py")
        process = process_factory(
            [sys.executable, "-I", "-B", str(worker), str(request_read), str(response_write)],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(Path(__file__).resolve().parent),
            env={"PATH": os.defpath, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1"},
            close_fds=True,
            pass_fds=(request_read, response_write),
        )
    except BaseException:
        os.close(request_read)
        os.close(request_write)
        os.close(response_read)
        os.close(response_write)
        raise
    os.close(request_read)
    os.close(response_write)
    try:
        _write_all(request_write, payload)
    except BaseException:
        _terminate_reap(process, response_read)
        raise
    finally:
        os.close(request_write)
    return process, response_read


def _write_all(fd: int, payload: bytes) -> None:
    view = memoryview(payload)
    while view:
        written = os.write(fd, view)
        view = view[written:]


def _read_fd_frame(fd: int) -> Mapping[str, object]:
    with os.fdopen(fd, "rb", closefd=False) as response_pipe:
        return read_frame(response_pipe.read, HARD_LIMITS["encoded_bytes"])


def _reader(value: bytes) -> Callable[[int], bytes]:
    offset = 0

    def read(count: int) -> bytes:
        nonlocal offset
        chunk = value[offset : offset + count]
        offset += len(chunk)
        return chunk

    return read
