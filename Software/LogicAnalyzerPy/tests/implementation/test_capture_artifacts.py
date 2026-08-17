from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.cli import main as cli
from pico_logic_analyzer.cli.main import _frequency_measurement
from pico_logic_analyzer.driver import V2DeviceService
from pico_logic_analyzer.formats import OutputError, csv_bytes, load_replay, write_capture_outputs
from pico_logic_analyzer.formats import capture as artifacts
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo


def _result() -> CaptureResult:
    device = DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 100_000, 200_000, 64, 8)
    return CaptureResult(
        CaptureConfig(100, 2, 3, 0, "rising"), np.array([0, 1, 3, 2, 0], dtype=np.uint8), device
    )


def test_csv_is_self_timed_and_deterministic() -> None:
    rows = list(csv.reader(csv_bytes(_result()).decode("utf-8").splitlines()))
    assert rows[0] == [
        "sample_index",
        "time_seconds",
        "trigger",
        "D0",
        "D1",
        "D2",
        "D3",
        "D4",
        "D5",
        "D6",
        "D7",
    ]
    assert rows[2][1:4] == ["-0.01", "0", "1"]  # last pre-trigger
    assert rows[3][1:4] == ["0", "1", "1"]  # first post-trigger at time zero


def test_outputs_round_trip_and_reject_collisions(tmp_path: Path) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    write_capture_outputs(_result(), csv_path, replay_path)
    samples, metadata = load_replay(replay_path)
    assert samples.tolist() == [0, 1, 3, 2, 0] and metadata["trigger_index"] == 2
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), csv_path, replay_path)


def test_two_output_install_rolls_back_replaced_originals(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old-csv")
    replay_path.write_bytes(b"old-npz")
    real_replace = artifacts.os.replace

    def fail_second(source: str | Path, target: str | Path) -> None:
        if Path(target) == replay_path and str(source).endswith(".tmp"):
            raise OSError("injected second rename failure")
        real_replace(source, target)

    monkeypatch.setattr(artifacts.os, "replace", fail_second)
    with pytest.raises(OutputError, match="injected second rename failure"):
        write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == b"old-csv"
    assert replay_path.read_bytes() == b"old-npz"
    assert not list(tmp_path.glob(".*.tmp")) and not list(tmp_path.glob(".*.bak"))


def test_second_backup_acquisition_failure_restores_first_original(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old-csv")
    replay_path.write_bytes(b"old-npz")
    real_replace = artifacts.os.replace

    def fail_second_backup(source: str | Path, target: str | Path) -> None:
        if Path(source) == replay_path and str(target).endswith(".bak"):
            raise OSError("injected second backup failure")
        real_replace(source, target)

    monkeypatch.setattr(artifacts.os, "replace", fail_second_backup)
    with pytest.raises(OutputError, match="injected second backup failure"):
        write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == b"old-csv"
    assert replay_path.read_bytes() == b"old-npz"
    assert not list(tmp_path.glob(".*.tmp")) and not list(tmp_path.glob(".*.bak"))


def test_capture_service_reads_count_before_payload_and_keeps_gpio_mapping() -> None:
    class Transport:
        def __init__(self, *_: object) -> None:
            self.lines = iter(
                [
                    "LOGIC_ANALYZER_TEST_V6_0",
                    "FREQ:100",
                    "BLASTFREQ:200",
                    "BUFFER:8",
                    "CHANNELS:8",
                    "CAPTURE_STARTED",
                ]
            )
            self.reads = iter([b"\x03\0\0\0", b"\x01\x00\x01\0"])
            self.writes: list[bytes] = []
            self.closed = False

        def open(self) -> None:
            pass

        def write(self, value: bytes, _: float) -> None:
            self.writes.append(value)

        def read_line(self, _: float) -> str:
            return next(self.lines)

        def read_exact(self, _: int, __: float) -> bytes:
            return next(self.reads)

        def close(self) -> None:
            self.closed = True

    transport = Transport()
    result = V2DeviceService(lambda *_: transport).capture(
        "/dev/explicit", CaptureConfig(10, 1, 2, 0, "falling"), 1
    )
    assert result.samples.tolist() == [1, 0, 1]
    assert result.channel_mapping == (
        "GPIO2",
        "GPIO3",
        "GPIO4",
        "GPIO5",
        "GPIO6",
        "GPIO7",
        "GPIO8",
        "GPIO9",
    )
    assert transport.closed and len(transport.writes) == 2


def test_frequency_measurement_reports_endpoint_quantization() -> None:
    measured, count, span, quantization = _frequency_measurement(
        np.array([0, 1, 0, 1, 0, 1, 0], dtype=np.uint8), 0, "rising", 100
    )
    assert (measured, count, span, quantization) == (50.0, 3, 4, 0.5)


def test_hardware_smoke_evidence_write_failure_is_output_exit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    device = DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 100_000, 200_000, 64, 8)

    class Service:
        def capture(self, _: str, config: CaptureConfig, __: float) -> CaptureResult:
            return CaptureResult(
                config, np.array([0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=np.uint8), device
            )

    evidence = tmp_path / "evidence.json"
    monkeypatch.setattr(cli, "V2DeviceService", Service)
    monkeypatch.setattr(
        cli.os, "replace", lambda *_: (_ for _ in ()).throw(OSError("injected rename"))
    )
    assert (
        cli.main(
            [
                "hardware-smoke",
                "--port",
                "/dev/explicit",
                "--signal-hz",
                "50",
                "--sample-rate",
                "100",
                "--trigger-channel",
                "0",
                "--edge",
                "rising",
                "--pre-samples",
                "2",
                "--post-samples",
                "7",
                "--evidence",
                str(evidence),
            ]
        )
        == 6
    )
    captured = capsys.readouterr()
    assert captured.out == "" and "could not write hardware evidence" in captured.err
    assert not evidence.exists() and not list(tmp_path.glob(".*.tmp"))


def test_recovery_capture_writes_one_ff_reidentifies_then_recaptures() -> None:
    identity = ["LOGIC_ANALYZER_TEST_V6_0", "FREQ:100", "BLASTFREQ:200", "BUFFER:64", "CHANNELS:8"]

    class Transport:
        def __init__(self, lines: list[str], reads: list[bytes] | None = None) -> None:
            self.lines, self.reads, self.writes, self.closed = (
                iter(lines),
                iter(reads or []),
                [],
                False,
            )

        def open(self) -> None:
            pass

        def write(self, value: bytes, _: float) -> None:
            self.writes.append(value)

        def read_line(self, _: float) -> str:
            return next(self.lines)

        def read_exact(self, _: int, __: float) -> bytes:
            try:
                return next(self.reads)
            except StopIteration:
                raise TimeoutError("drained") from None

        def close(self) -> None:
            self.closed = True

    first, second = Transport(identity), Transport(identity)
    third = Transport([*identity, "CAPTURE_STARTED"], [b"\x03\0\0\0", b"\x01\0\x01\0"])
    transports = iter([first, second, third])
    service = V2DeviceService(lambda *_: next(transports))
    idle = CaptureConfig(100, 1, 2, 1, "rising")
    signal = CaptureConfig(100, 1, 2, 0, "rising")
    result = service.recovery_capture("/dev/explicit", idle, signal, 0.1, 1, sleeper=lambda _: None)
    assert result.samples.tolist() == [1, 0, 1]
    assert first.writes[-1] == b"\xff" and first.writes.count(b"\xff") == 1
    assert first.closed and second.closed and third.closed


def test_recovery_capture_rejects_boolean_delay_before_transport_creation() -> None:
    created: list[object] = []
    service = V2DeviceService(lambda *_: created.append(object()))
    config = CaptureConfig(100, 1, 2, 0, "rising")
    with pytest.raises(ValueError, match="cancel-after"):
        service.recovery_capture("/dev/explicit", config, config, True, 2)
    assert created == []


def test_recovery_smoke_writes_sanitized_evidence_and_cancel_exit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    device = DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 100_000, 200_000, 64, 8)

    class Service:
        def recovery_capture(
            self,
            port: str,
            idle: CaptureConfig,
            signal: CaptureConfig,
            delay: float,
            timeout: float,
        ) -> CaptureResult:
            assert (port, idle.trigger_channel, signal.trigger_channel, delay, timeout) == (
                "/dev/explicit",
                1,
                0,
                0.1,
                1.0,
            )
            return CaptureResult(
                signal, np.array([0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=np.uint8), device
            )

    evidence = tmp_path / "recovery.json"
    monkeypatch.setattr(cli, "V2DeviceService", Service)
    arguments = [
        "hardware-recovery-smoke",
        "--port",
        "/dev/explicit",
        "--idle-channel",
        "1",
        "--idle-level",
        "0",
        "--cancel-after",
        "0.1",
        "--signal-channel",
        "0",
        "--signal-hz",
        "50",
        "--sample-rate",
        "100",
        "--edge",
        "rising",
        "--pre-samples",
        "2",
        "--post-samples",
        "7",
        "--evidence",
        str(evidence),
        "--timeout",
        "1",
    ]
    assert cli.main(arguments) == 0
    manifest = json.loads(evidence.read_text())
    assert manifest["cancel_byte"] == "ff" and manifest["port"] == "<PORT_SUPPLIED>"
    assert capsys.readouterr().out == ""

    class Cancelled:
        def recovery_capture(self, *_: object) -> CaptureResult:
            raise KeyboardInterrupt

    monkeypatch.setattr(cli, "V2DeviceService", Cancelled)
    assert cli.main(arguments) == 4
    assert capsys.readouterr().out == ""
