"""Black-box C1-B2 protocol/model verification from literal source fixtures."""

from __future__ import annotations

from time import sleep

import numpy as np
import pytest

from pico_logic_analyzer.driver import CaptureRecovery, RecoveryError
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
    encode_frame,
    encode_identity_request,
    parse_capture_response,
    parse_identity,
)
from pico_logic_analyzer.transport import FakeTransport, TransportClosed, TransportTimeout

from .golden import (
    CAPTURE_RESPONSE,
    FALLING_REQUEST,
    IDENTITY_REQUEST,
    IDENTITY_RESPONSE,
    RISING_REQUEST,
)


def _device() -> DeviceInfo:
    return DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 1_000_000, 1_000_000, 131_072, 24)


def _config(edge: str = "rising") -> CaptureConfig:
    return CaptureConfig(1_000_000, 170, 85, 0, edge)  # type: ignore[arg-type]


def test_encoder_matches_literal_rising_and_falling_requests() -> None:
    assert encode_capture_request(_config("rising")) == RISING_REQUEST
    assert encode_capture_request(_config("falling")) == FALLING_REQUEST


def test_identity_encoder_matches_literal_source_fixture() -> None:
    assert encode_identity_request() == IDENTITY_REQUEST


def test_frame_encoder_escapes_each_reserved_payload_byte() -> None:
    assert encode_frame(1, b"\xaa\x55\xf0") == bytes.fromhex("55 aa 01 f0 5a f0 a5 f0 00 aa 55")


def test_identity_parses_when_one_byte_fragments_are_buffered() -> None:
    parser = ByteParser()
    for byte in IDENTITY_RESPONSE:
        parser.feed(bytes((byte,)))
    assert parse_identity(parser) == _device()


def test_identity_round_trip_uses_one_byte_fake_transport_fragments() -> None:
    transport = FakeTransport([bytes((byte,)) for byte in IDENTITY_RESPONSE])
    parser = ByteParser(transport.read_exact(len(IDENTITY_RESPONSE), timeout=0.1))
    assert parse_identity(parser) == _device()


@pytest.mark.parametrize(
    "payload",
    [
        b"LOGIC_ANALYZER_TEST_BOARD_V6_0\nFREQ:1\nBLASTFREQ:1\nBUFFER:1\n",
        IDENTITY_RESPONSE + b"EXTRA:1\n",
        b"X" * 128,
        b"LOGIC_ANALYZER_TEST_BOARD_V6_0\nFREQ:-1\nBLASTFREQ:1\nBUFFER:1\nCHANNELS:1\n",
        b"LOGIC_ANALYZER_TEST_BOARD_V5_9\nFREQ:1\nBLASTFREQ:1\nBUFFER:1\nCHANNELS:1\n",
    ],
)
def test_identity_rejects_bad_field_surface(payload: bytes) -> None:
    parser = ByteParser(payload)
    with pytest.raises(ProtocolError):
        parse_identity(parser)


@pytest.mark.parametrize(
    "trailing",
    [b"X", b"EXTRA:1\n", b"CAPTURE_STARTED\n"],
)
def test_identity_rejects_any_already_buffered_trailing_phase_bytes(trailing: bytes) -> None:
    with pytest.raises(ProtocolError):
        parse_identity(ByteParser(IDENTITY_RESPONSE + trailing))


def test_capture_parser_preserves_coalesced_status_count_and_payload() -> None:
    config = CaptureConfig(1_000_000, 2, 1, 0, "rising")
    samples, device = parse_capture_response(ByteParser(CAPTURE_RESPONSE), config, _device())
    assert device == _device()
    assert samples.dtype == np.dtype("uint8")
    assert samples.tolist() == [1, 0, 1]


def test_capture_parser_rejects_already_buffered_trailing_bytes() -> None:
    config = CaptureConfig(1_000_000, 2, 1, 0, "rising")
    with pytest.raises(ProtocolError):
        parse_capture_response(ByteParser(CAPTURE_RESPONSE + b"X"), config, _device())


def test_capture_parser_accepts_one_byte_fragmented_response() -> None:
    parser = ByteParser()
    for byte in CAPTURE_RESPONSE:
        parser.feed(bytes((byte,)))
    samples, _ = parse_capture_response(
        parser, CaptureConfig(1_000_000, 2, 1, 0, "rising"), _device()
    )
    assert samples.tobytes() == b"\x01\x00\x01"


@pytest.mark.parametrize(
    "payload",
    [
        b"CAPTURE_ERROR\n",
        b"CAPTURE_STARTED\n" + (4).to_bytes(4, "little"),
        b"CAPTURE_STARTED\n" + (3).to_bytes(4, "little") + b"\x01\x00\x01\x01",
        b"CAPTURE_STARTED\n" + (3).to_bytes(4, "little") + b"\x01\x00",
    ],
)
def test_capture_parser_rejects_status_count_truncation_or_timestamp(payload: bytes) -> None:
    with pytest.raises(ProtocolError):
        parse_capture_response(
            ByteParser(payload), CaptureConfig(1_000_000, 2, 1, 0, "rising"), _device()
        )


def test_capture_parser_rejects_oversized_count_before_sample_read() -> None:
    payload = b"CAPTURE_STARTED\n" + (131_073).to_bytes(4, "little")
    with pytest.raises(ProtocolError):
        parse_capture_response(
            ByteParser(payload), CaptureConfig(1_000_000, 2, 1, 0, "rising"), _device()
        )


def test_fake_transport_timeout_disconnect_idempotent_close_and_exact_cancel_byte() -> None:
    transport = FakeTransport([b"a", b"bc"])
    assert transport.read_exact(3, timeout=0.1) == b"abc"
    with pytest.raises(TransportTimeout):
        transport.read_exact(1, timeout=0.1)
    transport.cancel_recovery(timeout=0.1)
    assert transport.writes == [b"\xff"]
    transport.close()
    transport.close()
    with pytest.raises(TransportClosed):
        transport.read_exact(1, timeout=0.1)


@pytest.mark.parametrize("timeout", [float("nan"), float("inf"), float("-inf"), 0.0, -0.1])
def test_transport_and_recovery_reject_nonfinite_or_nonpositive_timeouts(timeout: float) -> None:
    transport = FakeTransport()
    with pytest.raises(ValueError):
        transport.write(b"x", timeout)
    with pytest.raises(ValueError):
        CaptureRecovery(transport, lambda: None).timeout_or_cancel(timeout)


class _FailingTransport(FakeTransport):
    def __init__(self, failure: str, trace: list[str]) -> None:
        super().__init__()
        self.failure = failure
        self.trace = trace

    def write(self, data: bytes, timeout: float) -> None:
        self.trace.append("write")
        if self.failure == "write":
            raise OSError("write failed")
        super().write(data, timeout)

    def read_exact(self, size: int, timeout: float) -> bytes:
        self.trace.append("drain")
        if self.failure == "drain":
            raise OSError("drain failed")
        return super().read_exact(size, timeout)

    def close(self) -> None:
        self.trace.append("close")
        super().close()


@pytest.mark.parametrize("failure", ["write", "drain", "identify"])
def test_recovery_closes_on_write_drain_or_reidentify_failure(failure: str) -> None:
    trace: list[str] = []
    transport = _FailingTransport(failure, trace)

    def reopen_and_identify() -> None:
        trace.append("identify")
        if failure == "identify":
            raise OSError("identity failed")

    with pytest.raises(RecoveryError):
        CaptureRecovery(transport, reopen_and_identify).timeout_or_cancel(0.1)
    assert transport.closed
    assert trace[-1] in {"close", "identify"}


def test_recovery_drains_before_close_and_reidentify() -> None:
    trace: list[str] = []
    transport = _FailingTransport("none", trace)
    CaptureRecovery(transport, lambda: trace.append("identify")).timeout_or_cancel(0.1)
    assert trace[:4] == ["write", "drain", "close", "identify"]
    assert trace[4:] in ([], ["close"])


def test_recovery_sends_one_raw_cancel_closes_then_runs_identity_callback() -> None:
    transport = FakeTransport()
    identities: list[DeviceInfo] = []

    def reopen_and_identify() -> None:
        identities.append(parse_identity(ByteParser(IDENTITY_RESPONSE)))

    recovery = CaptureRecovery(transport, reopen_and_identify)
    recovery.timeout_or_cancel(timeout=0.1)
    assert transport.writes == [b"\xff"]
    assert transport.closed
    assert identities == [_device()]
    with pytest.raises(RecoveryError):
        recovery.timeout_or_cancel(timeout=0.1)
    assert transport.writes == [b"\xff"]


def test_capture_model_d0_and_trigger_time_boundaries() -> None:
    config = CaptureConfig(100, 2, 1, 0, "rising")
    result = CaptureResult(config, np.array([0, 1, 1], dtype=np.uint8), _device())
    assert result.trigger_index == 2
    assert result.time_seconds(1) == -0.01
    assert result.time_seconds(2) == 0.0


@pytest.mark.parametrize(
    "kwargs",
    [
        {"sample_rate_hz": 0},
        {"post_trigger_samples": 0},
        {"trigger_channel": 8},
        {"trigger_edge": "other"},
        {"channel_ids": (0, 1, 2, 3, 4, 5, 6)},
    ],
)
def test_capture_config_rejects_outside_cycle1_boundary(kwargs: dict[str, object]) -> None:
    baseline: dict[str, object] = {
        "sample_rate_hz": 100,
        "pre_trigger_samples": 2,
        "post_trigger_samples": 1,
        "trigger_channel": 0,
        "trigger_edge": "rising",
    }
    baseline.update(kwargs)
    with pytest.raises(ValidationError):
        CaptureConfig(**baseline)  # type: ignore[arg-type]


def test_capture_result_rejects_noncontiguous_samples() -> None:
    config = CaptureConfig(100, 2, 1, 0, "rising")
    with pytest.raises(ValidationError):
        CaptureResult(config, np.arange(6, dtype=np.uint8)[::2], _device())


@pytest.mark.parametrize(
    "device",
    [
        DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 99, 100, 10, 8),
        DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 100, 100, 2, 8),
    ],
)
def test_capture_result_rejects_config_outside_device_limits(device: DeviceInfo) -> None:
    config = CaptureConfig(100, 2, 1, 0, "rising")
    with pytest.raises(ValidationError):
        CaptureResult(config, np.array([0, 0, 0], dtype=np.uint8), device)


class _ContinuousDrainTransport(FakeTransport):
    def __init__(self) -> None:
        super().__init__()
        self.read_calls = 0

    def read_exact(self, size: int, timeout: float) -> bytes:
        self.read_calls += 1
        return b"x"


def test_recovery_continuous_input_stops_at_fixed_drain_limit_before_close() -> None:
    transport = _ContinuousDrainTransport()
    reopened: list[bool] = []
    CaptureRecovery(transport, lambda: reopened.append(True)).timeout_or_cancel(0.1)
    assert transport.writes == [b"\xff"]
    assert transport.read_calls == 4096
    assert transport.closed and reopened == [True]


class _SlowDrainTransport(FakeTransport):
    def __init__(self) -> None:
        super().__init__()
        self.timeouts: list[float] = []

    def read_exact(self, size: int, timeout: float) -> bytes:
        self.timeouts.append(timeout)
        if len(self.timeouts) == 1:
            sleep(0.005)
            return b"x"
        raise TransportTimeout("scripted slow drain elapsed the budget")


def test_recovery_drain_uses_one_overall_timeout_budget_not_one_per_byte() -> None:
    transport = _SlowDrainTransport()
    CaptureRecovery(transport, lambda: None).timeout_or_cancel(0.02)
    assert len(transport.timeouts) == 2
    assert 0 < transport.timeouts[1] < transport.timeouts[0]


@pytest.mark.parametrize(
    "field",
    ["sample_rate_hz", "pre_trigger_samples", "post_trigger_samples"],
)
def test_capture_request_rejects_values_outside_uint32(field: str) -> None:
    values: dict[str, object] = {
        "sample_rate_hz": 1,
        "pre_trigger_samples": 0,
        "post_trigger_samples": 1,
        "trigger_channel": 0,
        "trigger_edge": "rising",
    }
    values[field] = 2**32
    with pytest.raises((ValidationError, ProtocolError)):
        encode_capture_request(CaptureConfig(**values))  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "field,value",
    [
        ("sample_rate_hz", True),
        ("sample_rate_hz", 1.5),
        ("pre_trigger_samples", True),
        ("post_trigger_samples", 1.5),
        ("trigger_channel", False),
    ],
)
def test_capture_config_rejects_bool_and_float_fields_at_model_boundary(
    field: str, value: object
) -> None:
    values: dict[str, object] = {
        "sample_rate_hz": 100,
        "pre_trigger_samples": 2,
        "post_trigger_samples": 1,
        "trigger_channel": 0,
        "trigger_edge": "rising",
    }
    values[field] = value
    with pytest.raises(ValidationError):
        CaptureConfig(**values)  # type: ignore[arg-type]


@pytest.mark.parametrize("field", ["sample_rate_hz", "pre_trigger_samples", "post_trigger_samples"])
def test_capture_config_rejects_uint32_overflow_at_model_boundary(field: str) -> None:
    values: dict[str, object] = {
        "sample_rate_hz": 100,
        "pre_trigger_samples": 2,
        "post_trigger_samples": 1,
        "trigger_channel": 0,
        "trigger_edge": "rising",
    }
    values[field] = 2**32
    with pytest.raises(ValidationError):
        CaptureConfig(**values)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("labels", "mapping"),
    [
        (tuple(["D0"] * 7 + ["X" * 129]), tuple(f"D{i}" for i in range(8))),
        (tuple(f"D{i}" for i in range(8)), tuple(["D0"] * 7 + [1])),
    ],
)
def test_capture_result_rejects_nonstring_or_overlong_labels_and_mappings(
    labels: tuple[object, ...], mapping: tuple[object, ...]
) -> None:
    config = CaptureConfig(100, 2, 1, 0, "rising")
    with pytest.raises(ValidationError):
        CaptureResult(
            config,
            np.array([0, 0, 0], dtype=np.uint8),
            _device(),
            labels,  # type: ignore[arg-type]
            mapping,  # type: ignore[arg-type]
        )


def test_capture_parser_uses_negotiated_buffer_size_as_hard_bound() -> None:
    small_device = DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 100, 100, 2, 8)
    payload = b"CAPTURE_STARTED\n" + (3).to_bytes(4, "little")
    with pytest.raises(ProtocolError):
        parse_capture_response(
            ByteParser(payload), CaptureConfig(1, 2, 1, 0, "rising"), small_device
        )


def test_capture_parser_rejects_rate_above_negotiated_device_limit() -> None:
    limited_device = DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 100, 100, 10, 8)
    with pytest.raises(ValidationError):
        encode_capture_request(CaptureConfig(101, 2, 1, 0, "rising"), limited_device)
