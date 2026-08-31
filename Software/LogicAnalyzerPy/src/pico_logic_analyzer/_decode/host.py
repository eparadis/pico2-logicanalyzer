"""Private parent boundary; no public API or caller-controlled execution route."""

from __future__ import annotations

import os
import select
import subprocess
import sys
from collections.abc import Callable, Mapping
from pathlib import Path

from .identity import verify_decoder
from .ipc import REQUEST, RESULT, encode_frame, read_frame
from .model import (
    HARD_LIMITS,
    DecodeRequest,
    DecodeResult,
    HostFailure,
    WorkerFailure,
    decode_result_from_dict,
)


def decode_private(request: DecodeRequest) -> DecodeResult:
    """Run one fresh fixed worker only after identity and request preflight succeed."""
    return _decode_with_factory(request, subprocess.Popen)


def _decode_with_factory(
    request: DecodeRequest, process_factory: Callable[..., subprocess.Popen[bytes]]
) -> DecodeResult:
    """Injection seam for inert preflight-order tests; never exposed by the package."""
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
    process, response_fd = _spawn_fixed_worker(process_factory, payload)
    try:
        _wait_readable(response_fd, HARD_LIMITS["wall_deadline_ms"])
        response = _read_fd_frame(response_fd)
        try:
            process.wait(timeout=HARD_LIMITS["terminate_grace_ms"] / 1000)
        except subprocess.TimeoutExpired:
            raise HostFailure("process-exit") from None
    except TimeoutError:
        _terminate_reap(process)
        raise HostFailure("timeout") from None
    except (OSError, WorkerFailure, ValueError):
        _terminate_reap(process)
        raise HostFailure("ipc") from None
    finally:
        try:
            os.close(response_fd)
        except OSError:
            pass
    stdout = process.stdout.read() if process.stdout is not None else b""
    stderr = process.stderr.read() if process.stderr is not None else b""
    if (
        process.returncode != 0
        or len(stdout) > HARD_LIMITS["encoded_bytes"]
        or len(stderr) > HARD_LIMITS["stderr_bytes"]
    ):
        raise HostFailure("process-exit")
    result = response.get("result")
    if response.get("type") == "decode-failure":
        code = response.get("code")
        if code in {"snapshot", "import", "ipc", "decoder", "recursion", "memory", "output-limit"}:
            raise HostFailure(str(code))
        raise HostFailure("decoder")
    if response.get("type") != RESULT or not isinstance(result, Mapping):
        raise HostFailure("decode protocol rejected")
    try:
        return decode_result_from_dict(result)
    except HostFailure:
        raise HostFailure("ipc") from None


def _wait_readable(fd: int, deadline_ms: int) -> None:
    ready, _, _ = select.select([fd], [], [], deadline_ms / 1000)
    if not ready:
        raise TimeoutError


def _terminate_reap(process: subprocess.Popen[bytes]) -> None:
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(HARD_LIMITS["terminate_grace_ms"] / 1000)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


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
