from __future__ import annotations

import numpy as np
import pytest

from pico_logic_analyzer.driver import CaptureRecovery
from pico_logic_analyzer.model import (
    CaptureConfig,
    CaptureResult,
    DeviceInfo,
    ProtocolError,
    ValidationError,
)
from pico_logic_analyzer.protocol import (
    ByteParser,
    encode_capture_request,
    encode_identity_request,
    parse_capture_response,
    parse_identity,
)
from pico_logic_analyzer.transport import FakeTransport, TransportTimeout


def _device() -> DeviceInfo:
    return DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 1_000_000, 2_000_000, 1024, 8)


def test_capture_model_trigger_boundary() -> None:
    config = CaptureConfig(100, 2, 3, 0, "rising")
    result = CaptureResult(config, np.array([0, 1, 2, 3, 4], dtype=np.uint8), _device())
    assert result.trigger_index == 2
    assert result.time_seconds(1) == -0.01
    assert result.time_seconds(2) == 0


def test_capture_model_rejects_non_cycle_one_channels() -> None:
    with pytest.raises(ValidationError):
        CaptureConfig(1, 0, 1, 0, "rising", (0,))


def test_device_version_requires_v6_0_or_newer() -> None:
    with pytest.raises(ValidationError):
        DeviceInfo("LOGIC_ANALYZER_TEST_V5_9", 1, 1, 1, 8)
    assert DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 1, 1, 1, 8).identity.endswith("V6_0")
    assert DeviceInfo("LOGIC_ANALYZER_TEST_V7_1", 1, 1, 1, 8).identity.endswith("V7_1")


def test_capture_request_has_explicit_layout_and_escaping() -> None:
    request = encode_capture_request(CaptureConfig(1_000_000, 170, 85, 0, "falling"))
    assert request.startswith(b"\x55\xaa\x01") and request.endswith(b"\xaa\x55")
    assert b"\xf0\x5a" in request and b"\xf0\xa5" in request


def test_identity_request_is_exact_golden_frame() -> None:
    assert encode_identity_request() == bytes.fromhex("55 aa 00 aa 55")


def test_capture_request_validates_negotiated_capabilities() -> None:
    config = CaptureConfig(101, 1, 2, 0, "rising")
    with pytest.raises(ValidationError):
        config.validate_for(DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 100, 200, 3, 8))


def test_identity_and_coalesced_capture_status_binary_parse() -> None:
    identity = ByteParser(
        b"LOGIC_ANALYZER_TEST_V6_0\nFREQ:100\nBLASTFREQ:200\nBUFFER:8\nCHANNELS:8\n"
    )
    device = parse_identity(identity)
    capture = ByteParser(b"CAPTURE_STARTED\n\x03\0\0\0\x01\x02\x03\0")
    samples, _ = parse_capture_response(capture, CaptureConfig(1, 1, 2, 0, "rising"), device)
    assert samples.tolist() == [1, 2, 3]


def test_identity_rejects_extra_ascii_line() -> None:
    parser = ByteParser(
        b"LOGIC_ANALYZER_TEST_V6_0\nFREQ:1\nBLASTFREQ:2\nBUFFER:3\nCHANNELS:8\nEXTRA:1\n"
    )
    with pytest.raises(ProtocolError):
        parse_identity(parser)


def test_capture_rejects_count_and_timestamps() -> None:
    parser = ByteParser(b"CAPTURE_STARTED\n\x04\0\0\0")
    with pytest.raises(ProtocolError):
        parse_capture_response(parser, CaptureConfig(1, 1, 2, 0, "rising"), _device())


def test_fake_transport_is_fragmented_bounded_and_cancelable() -> None:
    transport = FakeTransport([b"a", b"bc"])
    assert transport.read_exact(3, 1) == b"abc"
    transport.cancel_recovery(1)
    assert transport.writes == [b"\xff"]
    with pytest.raises(TransportTimeout):
        transport.read_exact(1, 1)


def test_recovery_sends_one_byte_closes_and_reidentifies() -> None:
    transport = FakeTransport([])
    reopened: list[bool] = []
    CaptureRecovery(transport, lambda: reopened.append(True)).timeout_or_cancel(1)
    assert transport.writes == [b"\xff"]
    assert transport.closed and reopened == [True]


@pytest.mark.parametrize("timeout", [float("nan"), float("inf"), 0.0])
def test_transport_rejects_non_finite_timeout(timeout: float) -> None:
    with pytest.raises(ValueError):
        FakeTransport().write(b"x", timeout)
