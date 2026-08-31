"""Fixed private worker entrypoint; invoked only by the private parent."""

from __future__ import annotations

import os
import resource
import sys
from pathlib import Path
from typing import cast


def main(request_fd: int, response_fd: int) -> int:
    """Run one inert FD-only bootstrap; decoder loading is deliberately absent in 3b1."""
    _install_limits()
    source_root = Path(__file__).resolve().parents[2]
    if str(source_root) not in sys.path:
        sys.path.insert(0, str(source_root))
    from pico_logic_analyzer._decode.ipc import FAILURE, REQUEST, RESULT, encode_frame, read_frame
    from pico_logic_analyzer._decode.lifecycle import run_lifecycle
    from pico_logic_analyzer._decode.loader import load_frozen_decoder
    from pico_logic_analyzer._decode.model import HARD_LIMITS, DecodeRequest, WorkerFailure

    sys.setrecursionlimit(HARD_LIMITS["recursion_limit"])
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
        descriptor = load_frozen_decoder(decode_request.decoder)
        stage = "lifecycle"
        result = run_lifecycle(descriptor, decode_request)
        stage = "result"
        frame = encode_frame(RESULT, {"result": result.to_dict()}, HARD_LIMITS["encoded_bytes"])
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


def _install_limits() -> None:
    address_space = 68719476736
    resource.setrlimit(resource.RLIMIT_AS, (address_space, address_space))
    resource.setrlimit(resource.RLIMIT_CPU, (6, 6))
    sys.setrecursionlimit(320)


if __name__ == "__main__":
    os.environ.clear()
    if len(sys.argv) != 3 or not all(argument.isdecimal() for argument in sys.argv[1:]):
        raise SystemExit(2)
    raise SystemExit(main(int(sys.argv[1]), int(sys.argv[2])))
