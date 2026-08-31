"""Independent adversarial checks for the immutable C3-B2 private host."""

from __future__ import annotations

import copy
import os
import subprocess
import sys
from collections.abc import Callable

import pytest

from pico_logic_analyzer._decode.host import _decode_with_factory, decode_private
from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
from pico_logic_analyzer._decode.model import HARD_LIMITS, DecodeRequest, HostFailure


def _request() -> DecodeRequest:
    return DecodeRequest("uart", 1, (0,), {"rx": 0}, (0,), 0, {})


def _response_factory(frame: bytes) -> Callable[..., subprocess.Popen[bytes]]:
    """Return a child that writes only verifier-selected response bytes."""

    def factory(args: list[str], **kwargs: object) -> subprocess.Popen[bytes]:
        response_fd = int(args[-1])
        program = "import os,sys; os.write(int(sys.argv[1]), bytes.fromhex(sys.argv[2]))"
        return subprocess.Popen(
            [sys.executable, "-I", "-B", "-c", program, str(response_fd), frame.hex()],
            **kwargs,
        )

    return factory


def _valid_result_dict() -> dict[str, object]:
    return decode_private(_request()).to_dict()


def _frame(result: dict[str, object]) -> bytes:
    metrics = {
        "child_import_ns": 0,
        "child_load_ns": 0,
        "child_decode_ns": 0,
        "worker_peak_rss_bytes": 0,
    }
    return encode_frame(
        RESULT, {"result": result, "metrics": metrics}, HARD_LIMITS["encoded_bytes"]
    )


@pytest.mark.parametrize(
    "mutate",
    [
        lambda result: result["decoder"].__setitem__("id", "i2c"),  # type: ignore[union-attr]
        lambda result: result["decoder"].__setitem__("file_set_sha256", "0" * 64),  # type: ignore[union-attr]
        lambda result: result.__setitem__("samplerate_hz", 2),
        lambda result: result["capture"].__setitem__("sample_count", 2),  # type: ignore[union-attr]
        lambda result: result["channels"][0].__setitem__("physical_channel", 23),  # type: ignore[index,union-attr]
        lambda result: result.__setitem__("options", {"baudrate": 9600}),
    ],
    ids=("decoder-id", "file-set-hash", "samplerate", "capture", "channels", "options"),
)
def test_parent_rejects_result_identity_that_does_not_match_request(
    mutate: Callable[[dict[str, object]], None],
) -> None:
    """R6/R9 require result identity to remain bound to the preflighted request."""
    result = copy.deepcopy(_valid_result_dict())
    mutate(result)
    with pytest.raises(HostFailure, match="^ipc$"):
        _decode_with_factory(_request(), _response_factory(_frame(result)))

    # A hostile result must not poison a later fresh fixed-worker request.
    recovered = decode_private(_request())
    assert recovered.decoder == "uart"
    assert recovered.file_set_sha256 != "0" * 64


def test_candidate_file_descriptors_are_closed_after_valid_decode() -> None:
    before = set(os.listdir("/dev/fd"))
    decode_private(_request())
    after = set(os.listdir("/dev/fd"))
    assert after == before


def test_private_surface_has_no_public_decode_export() -> None:
    import pico_logic_analyzer

    assert not hasattr(pico_logic_analyzer, "decode_private")
    assert not hasattr(pico_logic_analyzer, "decode_capture")
