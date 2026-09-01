"""Fixed private worker entrypoint; invoked only by the private parent."""

from __future__ import annotations

import os
import resource
import sys
import time
from pathlib import Path
from typing import cast

BOOTSTRAP_ADDRESS_SPACE_BYTES = 68_719_476_736
BOOTSTRAP_RECURSION_LIMIT = 320


def main(
    request_fd: int,
    response_fd: int,
    address_space_bytes: int = BOOTSTRAP_ADDRESS_SPACE_BYTES,
    recursion_limit: int = BOOTSTRAP_RECURSION_LIMIT,
) -> int:
    """Run one fixed FD-only bootstrap and the hash-pinned decoder lifecycle."""
    _install_limits(address_space_bytes, recursion_limit)
    source_root = Path(__file__).resolve().parents[2]
    if str(source_root) not in sys.path:
        sys.path.insert(0, str(source_root))
    import_started = time.monotonic_ns()
    from pico_logic_analyzer._decode.ipc import FAILURE, REQUEST, RESULT, encode_frame, read_frame
    from pico_logic_analyzer._decode.lifecycle import run_lifecycle
    from pico_logic_analyzer._decode.loader import load_frozen_decoder
    from pico_logic_analyzer._decode.model import HARD_LIMITS, DecodeRequest, WorkerFailure
    imported = time.monotonic_ns()

    if (
        HARD_LIMITS["worker_address_space_bytes"] != BOOTSTRAP_ADDRESS_SPACE_BYTES
        or HARD_LIMITS["recursion_limit"] != BOOTSTRAP_RECURSION_LIMIT
    ):
        raise RuntimeError("bootstrap limits rejected")

    sys.setrecursionlimit(recursion_limit)
    stage = "request"
    try:
        with os.fdopen(request_fd, "rb", closefd=True) as request_pipe:
            request = read_frame(request_pipe.read, HARD_LIMITS["request_bytes"])
        if request.get("type") != REQUEST:
            raise WorkerFailure("worker request rejected")
        decode_request = DecodeRequest(
            cast(str, request["decoder"]),
            cast(int, request["samplerate_hz"]),
            tuple(cast(list[int], request["channel_ids"])),
            cast(dict[str, int], request["mapping"]),
            tuple(cast(list[int], request["samples"])),
            cast(int, request["trigger_index"]),
            cast(dict[str, object], request["options"]),
        )
        stage = "load"
        loaded_started = time.monotonic_ns()
        descriptor = load_frozen_decoder(decode_request.decoder)
        loaded = time.monotonic_ns()
        stage = "lifecycle"
        result = run_lifecycle(descriptor, decode_request)
        decoded = time.monotonic_ns()
        stage = "result"
        # On the supported macOS platform ru_maxrss is measured in bytes.
        metrics = {
            "child_import_ns": imported - import_started,
            "child_load_ns": loaded - loaded_started,
            "child_decode_ns": decoded - loaded,
            "worker_peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        }
        frame = encode_frame(
            RESULT, {"result": result.to_dict(), "metrics": metrics}, HARD_LIMITS["encoded_bytes"]
        )
        with os.fdopen(response_fd, "wb", closefd=True) as response_pipe:
            response_pipe.write(frame)
            response_pipe.flush()
        return 0
    except BaseException as error:
        code = _failure_code(stage, error)
        frame = encode_frame(
            FAILURE,
            {"code": code, "message": "worker rejected request"},
            HARD_LIMITS["diagnostic_bytes"],
        )
        with os.fdopen(response_fd, "wb", closefd=True) as response_pipe:
            response_pipe.write(frame)
            response_pipe.flush()
        return 0


def _failure_code(stage: str, error: BaseException) -> str:
    if isinstance(error, MemoryError):
        return "memory"
    if isinstance(error, RecursionError):
        return "recursion"
    if stage == "load":
        return "import"
    if stage == "request":
        return "ipc"
    return "decoder"


def _install_limits(
    address_space_bytes: int = BOOTSTRAP_ADDRESS_SPACE_BYTES,
    recursion_limit: int = BOOTSTRAP_RECURSION_LIMIT,
) -> None:
    if (
        type(address_space_bytes) is not int
        or not 1 <= address_space_bytes <= BOOTSTRAP_ADDRESS_SPACE_BYTES
        or type(recursion_limit) is not int
        or not 1 <= recursion_limit <= BOOTSTRAP_RECURSION_LIMIT
    ):
        raise RuntimeError("bootstrap limits rejected")
    resource.setrlimit(
        resource.RLIMIT_AS, (address_space_bytes, address_space_bytes)
    )
    sys.setrecursionlimit(recursion_limit)
    if resource.getrlimit(resource.RLIMIT_AS) != (
        address_space_bytes,
        address_space_bytes,
    ) or sys.getrecursionlimit() != recursion_limit:
        raise RuntimeError("bootstrap limits rejected")


if __name__ == "__main__":
    os.environ.clear()
    if len(sys.argv) not in {3, 5} or not all(argument.isdecimal() for argument in sys.argv[1:]):
        raise SystemExit(2)
    selected = (
        (BOOTSTRAP_ADDRESS_SPACE_BYTES, BOOTSTRAP_RECURSION_LIMIT)
        if len(sys.argv) == 3
        else (int(sys.argv[3]), int(sys.argv[4]))
    )
    raise SystemExit(main(int(sys.argv[1]), int(sys.argv[2]), *selected))
