"""Independent C1-B5 observable recovery tests using literal V2 inputs."""

from __future__ import annotations

import importlib
import json
from collections import deque
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.driver import V2DeviceService
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo
from pico_logic_analyzer.transport import TransportTimeout

from .golden import IDENTITY_REQUEST, RISING_REQUEST

_CLI = importlib.import_module("pico_logic_analyzer.cli.main")
_IDENTITY = [
    "LOGIC_ANALYZER_TEST_BOARD_V6_0",
    "FREQ:1000000",
    "BLASTFREQ:1000000",
    "BUFFER:131072",
    "CHANNELS:8",
]


class _RecoveryTransport:
    def __init__(self, lines: list[str], payload: bytes = b"") -> None:
        self.lines = deque(lines)
        self.payload = payload
        self.writes: list[bytes] = []
        self.events: list[str] = []

    def open(self) -> None:
        self.events.append("open")

    def close(self) -> None:
        self.events.append("close")

    def write(self, data: bytes, timeout: float) -> None:
        assert timeout == 1.0
        self.writes.append(bytes(data))
        self.events.append(f"write:{data.hex()}")

    def read_line(self, timeout: float) -> str:
        assert timeout == 1.0
        return self.lines.popleft()

    def read_exact(self, size: int, timeout: float) -> bytes:
        assert timeout > 0
        if not self.payload:
            raise TransportTimeout("bounded fake drain")
        result, self.payload = self.payload[:size], self.payload[size:]
        return result


def test_recovery_capture_sends_literal_ff_after_inflight_and_reopens_before_second_capture() -> (
    None
):
    initial = _RecoveryTransport(_IDENTITY.copy())
    reidentified = _RecoveryTransport(_IDENTITY.copy())
    periodic = _RecoveryTransport(
        _IDENTITY + ["CAPTURE_STARTED"],
        (255).to_bytes(4, "little") + bytes(index % 2 for index in range(255)) + b"\x00",
    )
    transports = deque([initial, reidentified, periodic])
    service = V2DeviceService(lambda port, timeout: transports.popleft())  # type: ignore[arg-type]
    idle = CaptureConfig(1_000_000, 170, 85, 1, "rising")
    signal = CaptureConfig(1_000_000, 170, 85, 0, "rising")

    result = service.recovery_capture(
        "/dev/explicit", idle, signal, 0.1, 1.0, sleeper=lambda _: None
    )

    assert result.samples.dtype == np.dtype("uint8") and len(result.samples) == 255
    assert result.samples[:4].tolist() == [0, 1, 0, 1]
    assert initial.writes[0] == IDENTITY_REQUEST
    assert initial.writes[-1] == b"\xff"
    assert initial.writes.count(b"\xff") == 1
    assert initial.events[-1] == "close"
    assert reidentified.writes == [IDENTITY_REQUEST]
    assert reidentified.events[-1] == "close"
    assert periodic.writes == [IDENTITY_REQUEST, RISING_REQUEST]
    assert periodic.events[-1] == "close"


def test_keyboard_interrupt_after_inflight_still_cancels_closes_and_reidentifies() -> None:
    initial = _RecoveryTransport(_IDENTITY.copy())
    reidentified = _RecoveryTransport(_IDENTITY.copy())
    transports = deque([initial, reidentified])
    service = V2DeviceService(lambda port, timeout: transports.popleft())  # type: ignore[arg-type]
    config = CaptureConfig(1_000_000, 170, 85, 0, "rising")

    def interrupted(_: float) -> None:
        raise KeyboardInterrupt

    with pytest.raises(KeyboardInterrupt):
        service.recovery_capture("/dev/explicit", config, config, 0.1, 1.0, sleeper=interrupted)
    assert initial.writes.count(b"\xff") == 1 and initial.events[-1] == "close"
    assert reidentified.writes == [IDENTITY_REQUEST] and reidentified.events[-1] == "close"


def test_malformed_setup_closes_without_sending_cancellation() -> None:
    malformed = _RecoveryTransport(["NOT_ANALYZER", *_IDENTITY[1:]])
    service = V2DeviceService(lambda port, timeout: malformed)  # type: ignore[arg-type]
    config = CaptureConfig(1_000_000, 170, 85, 0, "rising")

    with pytest.raises(Exception):
        service.recovery_capture("/dev/explicit", config, config, 0.1, 1.0, sleeper=lambda _: None)
    assert b"\xff" not in malformed.writes and malformed.events[-1] == "close"


@pytest.mark.parametrize(
    ("cancel_after", "timeout"),
    [(True, 2.0), (float("nan"), 1.0), (float("inf"), 1.0), (0.0, 1.0), (1.0, 1.0)],
)
def test_recovery_cancel_after_is_strictly_finite_positive_float_below_timeout(
    cancel_after: object, timeout: float
) -> None:
    constructed = False

    def factory(port: str, timeout: float) -> object:
        nonlocal constructed
        constructed = True
        raise AssertionError("invalid cancel-after must not open a transport")

    service = V2DeviceService(factory)  # type: ignore[arg-type]
    config = CaptureConfig(1_000_000, 170, 85, 0, "rising")
    with pytest.raises(ValueError):
        service.recovery_capture("/dev/explicit", config, config, cancel_after, timeout)  # type: ignore[arg-type]
    assert constructed is False


def test_recovery_cli_requires_explicit_port_without_constructing_service(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(
        _CLI,
        "V2DeviceService",
        lambda: (_ for _ in ()).throw(AssertionError("must not auto-select")),
    )
    with pytest.raises(SystemExit) as raised:
        _CLI.main(
            [
                "hardware-recovery-smoke",
                "--idle-channel",
                "1",
                "--idle-level",
                "0",
                "--cancel-after",
                "0.1",
                "--signal-channel",
                "0",
                "--signal-hz",
                "25",
                "--sample-rate",
                "100",
                "--edge",
                "rising",
                "--pre-samples",
                "2",
                "--post-samples",
                "3",
                "--evidence",
                "x.json",
            ]
        )
    assert raised.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == "" and "--port" in captured.err


def test_recovery_cli_writes_sanitized_atomic_evidence(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    result = CaptureResult(
        CaptureConfig(100, 2, 3, 0, "rising"),
        np.array([0, 1, 0, 1, 0], dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 100, 400, 128, 8),
    )

    class Service:
        def recovery_capture(self, *args: object) -> CaptureResult:
            return result

    monkeypatch.setattr(_CLI, "V2DeviceService", Service)
    evidence = tmp_path / "recovery.json"
    supplied_port = "/dev/machine-local-port"
    assert (
        _CLI.main(
            [
                "hardware-recovery-smoke",
                "--port",
                supplied_port,
                "--idle-channel",
                "1",
                "--idle-level",
                "0",
                "--cancel-after",
                "0.1",
                "--signal-channel",
                "0",
                "--signal-hz",
                "25",
                "--sample-rate",
                "100",
                "--edge",
                "rising",
                "--pre-samples",
                "2",
                "--post-samples",
                "3",
                "--evidence",
                str(evidence),
            ]
        )
        == 0
    )
    captured = capsys.readouterr()
    assert captured.out == captured.err == ""
    manifest = json.loads(evidence.read_text(encoding="utf-8"))
    assert manifest["port"] == "<PORT_SUPPLIED>" and manifest["cancel_byte"] == "ff"
    assert supplied_port not in evidence.read_text(encoding="utf-8")
