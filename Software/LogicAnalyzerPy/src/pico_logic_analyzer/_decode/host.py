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
from dataclasses import dataclass, fields, is_dataclass
from pathlib import Path

from .identity import verify_decoder
from .ipc import REQUEST, RESULT, encode_frame, read_frame
from .model import (
    HARD_LIMITS,
    REGRESSION_LIMITS,
    AnnotationDeclaration,
    AnnotationRowDeclaration,
    AnnotationValue,
    BinaryDeclaration,
    BinaryValue,
    DecodeRequest,
    DecodeResult,
    HostFailure,
    MetadataDeclaration,
    MetadataValue,
    RequestFailure,
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


@dataclass(frozen=True)
class _ExpectedResultProjection:
    """Request/identity facts retained before the untrusted worker is spawned."""

    decoder: str
    file_set_sha256: str
    samplerate_hz: int
    sample_count: int
    trigger_index: int
    channel_ids: tuple[int, ...]
    channels: tuple[tuple[str, int], ...]
    options: tuple[tuple[str, type[object], object], ...]


@dataclass(frozen=True)
class _RegressionObservation:
    """Per-call private measurements for external regression evidence only."""

    child_import_ns: int
    child_load_ns: int
    child_decode_ns: int
    worker_peak_rss_bytes: int
    parent_retained_growth_bytes: int
    successful_parent_total_ns: int
    launch_ns: int
    reap_ns: int
    timeout_cleanup_total_ns: int = 0
    terminate_to_reap_ns: int = 0
    kill_to_reap_ns: int = 0


def decode_private(
    request: DecodeRequest,
    cancellation: CancellationToken | None = None,
    *,
    limits: Mapping[str, int] | None = None,
) -> DecodeResult:
    """Run one fresh fixed worker only after identity and request preflight succeed."""
    return _decode_with_factory(request, subprocess.Popen, cancellation, limits=limits)


def _decode_with_factory(
    request: DecodeRequest,
    process_factory: Callable[..., subprocess.Popen[bytes]],
    cancellation: CancellationToken | None = None,
    measure_rss: Callable[[], int] | None = None,
    monotonic_ns: Callable[[], int] = time.monotonic_ns,
    measure_decoded: Callable[[object], int] | None = None,
    measure_retained: Callable[[object], int] | None = None,
    regression_observer: Callable[[_RegressionObservation], None] | None = None,
    limits: Mapping[str, int] | None = None,
) -> DecodeResult:
    """Injection seam for inert preflight-order tests; never exposed by the package."""
    effective_limits = _effective_limits(limits)
    run_started = monotonic_ns()
    rss = measure_rss or _parent_rss
    parent_before = rss()
    if cancellation is not None and cancellation.cancelled:
        raise HostFailure("cancelled")
    identity = verify_decoder(request.decoder)
    expected = _expected_result_projection(request, identity.decoder, identity.file_set_sha256)
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
        effective_limits["request_bytes"],
    )
    launch_started = monotonic_ns()
    process, request_fd, response_fd = _spawn_fixed_worker(process_factory, effective_limits)
    response: Mapping[str, object] | None = None
    stdout = b""
    stderr = b""

    def observe_cleanup(cleanup: _CleanupObservation, timed_out: bool) -> None:
        if regression_observer is not None:
            regression_observer(
                _RegressionObservation(
                    child_import_ns=0,
                    child_load_ns=0,
                    child_decode_ns=0,
                    worker_peak_rss_bytes=0,
                    parent_retained_growth_bytes=0,
                    successful_parent_total_ns=0,
                    launch_ns=0,
                    reap_ns=0,
                    timeout_cleanup_total_ns=(monotonic_ns() - run_started) if timed_out else 0,
                    terminate_to_reap_ns=cleanup.terminate_to_reap_ns,
                    kill_to_reap_ns=cleanup.kill_to_reap_ns,
                )
            )

    try:
        launch_ns = monotonic_ns() - launch_started
        response, stdout, stderr = _collect_response(
            process, request_fd, payload, response_fd, cancellation, effective_limits
        )
        try:
            reap_started = monotonic_ns()
            process.wait(timeout=effective_limits["terminate_grace_ms"] / 1000)
            reap_ns = monotonic_ns() - reap_started
        except subprocess.TimeoutExpired:
            raise HostFailure("process-exit") from None
    except TimeoutError:
        observe_cleanup(
            _terminate_reap(
                process,
                request_fd,
                response_fd,
                monotonic_ns=monotonic_ns,
                limits=effective_limits,
            ),
            True,
        )
        raise HostFailure("timeout") from None
    except InterruptedError:
        observe_cleanup(
            _terminate_reap(
                process,
                request_fd,
                response_fd,
                monotonic_ns=monotonic_ns,
                limits=effective_limits,
            ),
            False,
        )
        raise HostFailure("cancelled") from None
    except KeyboardInterrupt:
        observe_cleanup(
            _terminate_reap(
                process,
                request_fd,
                response_fd,
                monotonic_ns=monotonic_ns,
                limits=effective_limits,
            ),
            False,
        )
        raise HostFailure("cancelled") from None
    except WorkerFailure as error:
        observe_cleanup(
            _terminate_reap(
                process,
                request_fd,
                response_fd,
                monotonic_ns=monotonic_ns,
                limits=effective_limits,
            ),
            False,
        )
        # A child that exits unsuccessfully before completing its frame is a
        # process failure, not an IPC claim from its untrusted byte stream.
        if str(error) == "output limit":
            raise HostFailure("output-limit") from None
        if str(error) == "request pipe closed":
            raise HostFailure("process-exit") from None
        if process.returncode != 0:
            raise HostFailure("process-exit") from None
        raise HostFailure("ipc") from None
    except (OSError, ValueError):
        observe_cleanup(
            _terminate_reap(
                process,
                request_fd,
                response_fd,
                monotonic_ns=monotonic_ns,
                limits=effective_limits,
            ),
            False,
        )
        raise HostFailure("ipc") from None
    except HostFailure:
        observe_cleanup(
            _terminate_reap(
                process,
                request_fd,
                response_fd,
                monotonic_ns=monotonic_ns,
                limits=effective_limits,
            ),
            False,
        )
        raise
    finally:
        try:
            os.close(request_fd)
        except OSError:
            pass
        try:
            os.close(response_fd)
        except OSError:
            pass
    _close_standard_pipes(process)
    if (
        process.returncode != 0
        or (response is not None and response.get("type") == RESULT and bool(stdout))
        or (response is not None and response.get("type") == RESULT and bool(stderr))
        or len(stdout) > effective_limits["stdout_bytes"]
        or len(stderr) > effective_limits["stderr_bytes"]
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
    metrics = _worker_metrics(response.get("metrics"))
    _enforce_result_limits(result, measure_decoded, measure_retained, effective_limits)
    try:
        materialized = decode_result_from_dict(result)
    except HostFailure:
        raise HostFailure("ipc") from None
    _validate_result_projection(materialized, expected)
    _validate_result_graph(materialized)
    _enforce_typed_result_limits(materialized, effective_limits)
    parent_after = rss()
    observation = _RegressionObservation(
        **metrics,
        parent_retained_growth_bytes=parent_after - parent_before,
        successful_parent_total_ns=monotonic_ns() - run_started,
        launch_ns=launch_ns,
        reap_ns=reap_ns,
    )
    if regression_observer is not None:
        regression_observer(observation)
    return materialized


def _expected_result_projection(
    request: DecodeRequest, decoder: str, file_set_sha256: str
) -> _ExpectedResultProjection:
    """Copy every result-visible preflight fact before child-controlled bytes exist."""
    channels = tuple(request.mapping.items())
    return _ExpectedResultProjection(
        decoder,
        file_set_sha256,
        request.samplerate,
        len(request.samples),
        request.trigger_index,
        tuple(physical for _, physical in channels),
        channels,
        tuple((key, type(value), value) for key, value in sorted(request.options.items())),
    )


def _validate_result_projection(
    result: DecodeResult, expected: _ExpectedResultProjection
) -> None:
    """Reject a locally valid result that does not describe this exact request."""
    actual_options = tuple((key, type(value), value) for key, value in result.options.items())
    if (
        result.decoder != expected.decoder
        or result.file_set_sha256 != expected.file_set_sha256
        or result.samplerate_hz != expected.samplerate_hz
        or result.capture.sample_count != expected.sample_count
        or result.capture.trigger_index != expected.trigger_index
        or result.capture.channel_ids != expected.channel_ids
        or tuple(result.channels.items()) != expected.channels
        or actual_options != expected.options
    ):
        raise HostFailure("ipc")


_REGISTERED_OUTPUT_KINDS: Mapping[str, tuple[str, ...]] = {
    # These are the frozen API-v3 register orders, not fixture records.  Output
    # ids are allocation positions in ApiV3Host.register().
    "uart": ("python", "binary", "annotation"),
    "spi": ("python", "annotation", "binary", "metadata"),
    "i2c": ("python", "annotation", "binary", "metadata"),
}


def _validate_result_graph(result: DecodeResult) -> None:
    """Validate the complete post-materialization declaration/put graph.

    The child controls every member of ``result``.  This deliberately makes no
    best-effort correction: any broken edge is a single IPC failure before the
    result is observable by a caller.
    """
    try:
        annotation = tuple(
            item for item in result.declarations if type(item) is AnnotationDeclaration
        )
        rows = tuple(item for item in result.declarations if type(item) is AnnotationRowDeclaration)
        binary = tuple(item for item in result.declarations if type(item) is BinaryDeclaration)
        metadata = tuple(item for item in result.declarations if type(item) is MetadataDeclaration)
        _validate_declaration_collection(annotation)
        _validate_declaration_collection(rows)
        _validate_declaration_collection(binary)
        annotation_indices = {item.index for item in annotation}
        for row in rows:
            if not row.annotation_indices or len(row.annotation_indices) != len(
                set(row.annotation_indices)
            ):
                raise ValueError
            if any(index not in annotation_indices for index in row.annotation_indices):
                raise ValueError
        output_kinds = _REGISTERED_OUTPUT_KINDS[result.decoder]
        metadata_by_output = {item.output_id: item for item in metadata}
        if len(metadata_by_output) != len(metadata):
            raise ValueError
        if any(
            item.output_id >= len(output_kinds)
            or output_kinds[item.output_id] != "metadata"
            or item.value_type != "integer"
            or not item.name
            or not item.description
            for item in metadata
        ):
            raise ValueError
        for record in result.records:
            # API-v3's ``put`` permits the terminal sample coordinate equal to
            # the capture extent (an interval end, rather than an array index).
            if not 0 <= record.start_sample <= record.end_sample <= result.capture.sample_count:
                raise ValueError
            if (
                record.output_id >= len(output_kinds)
                or output_kinds[record.output_id] != record.kind
            ):
                raise ValueError
            _validate_record_time(record.start_sample, record.start_time, result)
            _validate_record_time(record.end_sample, record.end_time, result)
            if record.kind == "annotation":
                if (
                    type(record.value) is not AnnotationValue
                    or record.value.class_index >= len(annotation)
                ):
                    raise ValueError
            elif record.kind == "binary":
                if type(record.value) is not BinaryValue or record.value.class_index >= len(binary):
                    raise ValueError
            elif record.kind == "metadata":
                if (
                    type(record.value) is not MetadataValue
                    or record.output_id not in metadata_by_output
                ):
                    raise ValueError
                if record.value.value_type != metadata_by_output[record.output_id].value_type:
                    raise ValueError
    except (KeyError, ValueError):
        raise HostFailure("ipc") from None


def _validate_declaration_collection(
    declarations: tuple[AnnotationDeclaration, ...]
    | tuple[AnnotationRowDeclaration, ...]
    | tuple[BinaryDeclaration, ...],
) -> None:
    if (
        tuple(item.index for item in declarations) != tuple(range(len(declarations)))
        or len({item.identifier for item in declarations}) != len(declarations)
        or any(not item.identifier or not item.description for item in declarations)
    ):
        raise ValueError


def _validate_record_time(sample: int, time_value: object, result: DecodeResult) -> None:
    absolute = getattr(time_value, "absolute", None)
    relative = getattr(time_value, "trigger_relative", None)
    if (
        absolute is None
        or relative is None
        or absolute.numerator != sample
        or absolute.denominator != result.samplerate_hz
        or relative.numerator != sample - result.capture.trigger_index
        or relative.denominator != result.samplerate_hz
    ):
        raise ValueError


def _worker_metrics(value: object) -> dict[str, int]:
    """Validate the hostile worker metric frame without enforcing regressions."""
    if not isinstance(value, Mapping) or set(value) != {
        "child_import_ns",
        "child_load_ns",
        "child_decode_ns",
        "worker_peak_rss_bytes",
    } or any(type(value[name]) is not int or value[name] < 0 for name in value):
        raise HostFailure("ipc")
    return {name: value[name] for name in value}


def _validate_worker_metrics(value: object) -> None:
    """Metrics are required protocol fields from the hash-pinned worker, never hints."""
    metrics = _worker_metrics(value)
    caps = {
        "child_import_ns": REGRESSION_LIMITS["child_import_ns"],
        "child_load_ns": REGRESSION_LIMITS["child_load_ns"],
        "child_decode_ns": REGRESSION_LIMITS["child_decode_ns"],
        "worker_peak_rss_bytes": REGRESSION_LIMITS["worker_peak_rss_bytes"],
    }
    if any(
        metrics[name] > cap
        for name, cap in caps.items()
    ):
        raise HostFailure("process-exit")


def _validate_regression_observation(observation: _RegressionObservation) -> None:
    """Pure exact-candidate regression gate; never called by product decode."""
    if any(
        type(getattr(observation, name)) is not int
        or getattr(observation, name) < 0
        or getattr(observation, name) > limit
        for name, limit in REGRESSION_LIMITS.items()
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
    process: subprocess.Popen[bytes],
    request_fd: int,
    payload: bytes,
    response_fd: int,
    cancellation: CancellationToken | None,
    limits: Mapping[str, int] = HARD_LIMITS,
) -> tuple[Mapping[str, object], bytes, bytes]:
    """Stream request and drain every child pipe under one parent deadline."""
    buffers = {"response": bytearray(), "stdout": bytearray(), "stderr": bytearray()}
    sources: list[tuple[str, int]] = [("response", response_fd)]
    if process.stdout is not None:
        sources.append(("stdout", process.stdout.fileno()))
    if process.stderr is not None:
        sources.append(("stderr", process.stderr.fileno()))
    selector = selectors.DefaultSelector()
    request = memoryview(payload)
    os.set_blocking(request_fd, False)
    for _, fd in sources:
        os.set_blocking(fd, False)
    selector.register(request_fd, selectors.EVENT_WRITE, "request")
    for name, fd in sources:
        selector.register(fd, selectors.EVENT_READ, name)
    deadline = time.monotonic() + limits["wall_deadline_ms"] / 1000
    try:
        while selector.get_map():
            if cancellation is not None and cancellation.cancelled:
                raise InterruptedError
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError
            for key, _ in selector.select(min(remaining, 0.05)):
                if key.data == "request":
                    try:
                        written = os.write(key.fd, request)
                    except BlockingIOError:
                        continue
                    except BrokenPipeError:
                        raise WorkerFailure("request pipe closed") from None
                    if written <= 0:
                        raise WorkerFailure("request pipe closed")
                    request = request[written:]
                    if not request:
                        selector.unregister(key.fd)
                        os.close(request_fd)
                    continue
                try:
                    data = os.read(key.fd, 65537)
                except BlockingIOError:
                    continue
                if not data:
                    selector.unregister(key.fd)
                    continue
                name = key.data
                buffers[name].extend(data)
                if len(buffers[name]) > _pipe_limit(name, limits):
                    raise WorkerFailure("output limit")
    finally:
        selector.close()
    return (
        read_frame(_reader(bytes(buffers["response"])), limits["encoded_bytes"]),
        bytes(buffers["stdout"]),
        bytes(buffers["stderr"]),
    )


def _pipe_limit(name: str, limits: Mapping[str, int] = HARD_LIMITS) -> int:
    return limits["encoded_bytes"] + 4 if name == "response" else limits[f"{name}_bytes"]


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
    limits: Mapping[str, int] = HARD_LIMITS,
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
    if decoded > limits["decoded_bytes"] or retained > limits["retained_result_bytes"]:
        raise HostFailure("output-limit")


def _enforce_typed_result_limits(
    result: DecodeResult, limits: Mapping[str, int]
) -> None:
    text_bytes = sum(len(str(item.to_dict()).encode()) for item in result.declarations)
    binary_bytes = 0
    nested_items = 0
    nested_depth = 0
    for record in result.records:
        if record.kind == "annotation" and isinstance(record.value, AnnotationValue):
            text_bytes += sum(len(text.encode()) for text in record.value.texts)
        elif record.kind == "binary" and isinstance(record.value, BinaryValue):
            binary_bytes += len(record.value.data)
        elif record.kind == "python":
            text, binary, items, depth = _measure_typed_value(record.value)
            text_bytes += text
            binary_bytes += binary
            nested_items += items
            nested_depth = max(nested_depth, depth)
    if (
        len(result.records) > limits["output_records"]
        or text_bytes > limits["text_bytes"]
        or binary_bytes > limits["binary_bytes"]
        or nested_items > limits["nested_items"]
        or nested_depth > limits["nested_depth"]
    ):
        raise HostFailure("output-limit")


def _measure_typed_value(value: object, depth: int = 1) -> tuple[int, int, int, int]:
    if isinstance(value, str):
        return len(value.encode()), 0, 1, depth
    if type(value) is bytes:
        return 0, len(value), 1, depth
    if isinstance(value, tuple | list):
        children = [_measure_typed_value(item, depth + 1) for item in value]
        return (
            sum(item[0] for item in children),
            sum(item[1] for item in children),
            1 + sum(item[2] for item in children),
            max((depth, *(item[3] for item in children))),
        )
    return 0, 0, 1, depth


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


@dataclass(frozen=True)
class _CleanupObservation:
    terminate_to_reap_ns: int
    kill_to_reap_ns: int


def _terminate_reap(
    process: subprocess.Popen[bytes],
    *fds: int,
    monotonic_ns: Callable[[], int] = time.monotonic_ns,
    limits: Mapping[str, int] = HARD_LIMITS,
) -> _CleanupObservation:
    terminate_started: int | None = None
    kill_started: int | None = None
    reaped_at: int | None = None
    try:
        if process.poll() is None:
            terminate_started = monotonic_ns()
            process.terminate()
            try:
                process.wait(limits["terminate_grace_ms"] / 1000)
                reaped_at = monotonic_ns()
            except subprocess.TimeoutExpired:
                kill_started = monotonic_ns()
                process.kill()
                process.wait()
                reaped_at = monotonic_ns()
    finally:
        for fd in fds:
            try:
                os.close(fd)
            except OSError:
                pass
        _close_standard_pipes(process)
    finished = reaped_at if reaped_at is not None else monotonic_ns()
    return _CleanupObservation(
        0 if terminate_started is None else finished - terminate_started,
        0 if kill_started is None else finished - kill_started,
    )


def _effective_limits(limits: Mapping[str, int] | None) -> dict[str, int]:
    if limits is None:
        return dict(HARD_LIMITS)
    if set(limits) != set(HARD_LIMITS):
        raise RequestFailure("limits rejected")
    effective: dict[str, int] = {}
    for key, ceiling in HARD_LIMITS.items():
        value = limits.get(key)
        if type(value) is not int or value <= 0 or value > ceiling:
            raise RequestFailure("limits rejected")
        effective[key] = value
    return effective


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
    process_factory: Callable[..., subprocess.Popen[bytes]],
    limits: Mapping[str, int] = HARD_LIMITS,
) -> tuple[subprocess.Popen[bytes], int, int]:
    request_read, request_write = os.pipe()
    response_read, response_write = os.pipe()
    os.set_inheritable(request_read, True)
    os.set_inheritable(response_write, True)
    try:
        worker = Path(__file__).with_name("worker.py")
        arguments = [
            sys.executable,
            "-I",
            "-B",
            str(worker),
            str(request_read),
            str(response_write),
        ]
        if (
            limits["worker_address_space_bytes"] != HARD_LIMITS["worker_address_space_bytes"]
            or limits["recursion_limit"] != HARD_LIMITS["recursion_limit"]
        ):
            arguments.extend(
                (
                    str(limits["worker_address_space_bytes"]),
                    str(limits["recursion_limit"]),
                )
            )
        process = process_factory(
            arguments,
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
    return process, request_write, response_read


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
