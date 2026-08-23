"""Independent C1-B4 capture/export checks from the settled public contract."""

from __future__ import annotations

import csv
import io
import json
import os
import zipfile
from pathlib import Path

import numpy as np
import pytest

import pico_logic_analyzer.cli.main as cli
import pico_logic_analyzer.formats.capture as capture_format
from pico_logic_analyzer.driver import V2DeviceService
from pico_logic_analyzer.formats import (
    OutputError,
    csv_bytes,
    load_replay,
    replay_bytes,
    write_capture_outputs,
)
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo, ProtocolError

from .golden import FALLING_REQUEST, IDENTITY_REQUEST, RISING_REQUEST


def _device() -> DeviceInfo:
    return DeviceInfo("LOGIC_ANALYZER_TEST_BOARD_V6_0", 100_000, 400_000, 131_072, 24)


def _result() -> CaptureResult:
    return CaptureResult(
        CaptureConfig(100, 2, 3, 0, "rising"),
        np.array([0x00, 0x01, 0x81, 0x02, 0xFF], dtype=np.uint8),
        _device(),
    )


_EXPECTED_CSV = (
    b"sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7\n"
    b"0,-0.02,0,0,0,0,0,0,0,0,0\n"
    b"1,-0.01,0,1,0,0,0,0,0,0,0\n"
    b"2,0,1,1,0,0,0,0,0,0,1\n"
    b"3,0.01,0,0,1,0,0,0,0,0,0\n"
    b"4,0.02,0,1,1,1,1,1,1,1,1\n"
)


def test_csv_is_exact_self_timed_utf8_lf_bytes_and_independent_reader_values() -> None:
    payload = csv_bytes(_result())
    assert payload == _EXPECTED_CSV
    rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8"), newline="")))
    assert rows[1]["time_seconds"] == "-0.01"  # last pre-trigger instant
    assert rows[2]["time_seconds"] == "0" and rows[2]["trigger"] == "1"
    assert [row["trigger"] for row in rows] == ["0", "0", "1", "0", "0"]
    assert rows[2]["D0"] == "1" and rows[2]["D7"] == "1"


def test_artifact_bytes_are_deterministic_for_one_fixed_capture() -> None:
    result = _result()
    assert csv_bytes(result) == csv_bytes(result)
    assert replay_bytes(result) == replay_bytes(result)


def test_replay_has_only_safe_members_canonical_metadata_and_exact_uint8_samples() -> None:
    raw = replay_bytes(_result())
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        assert [entry.filename for entry in archive.infolist()] == ["samples.npy", "metadata.npy"]
        samples = np.load(io.BytesIO(archive.read("samples.npy")), allow_pickle=False)
        assert samples.dtype == np.dtype("uint8") and samples.ndim == 1
        assert samples.tolist() == [0, 1, 129, 2, 255]
        metadata_array = np.load(io.BytesIO(archive.read("metadata.npy")), allow_pickle=False)
    assert metadata_array.dtype == np.dtype("uint8") and metadata_array.ndim == 1
    metadata_wire = metadata_array.tobytes()
    metadata = json.loads(metadata_wire.decode("utf-8"))
    canonical = json.dumps(
        metadata, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    assert canonical == metadata_wire
    assert metadata["schema_version"] == 2 and "provisional" not in metadata
    assert metadata["trigger_index"] == 2 and metadata["requested_count"] == 5
    assert metadata["channel_ids"] == list(range(8))


@pytest.mark.parametrize(
    "edge,expected", [("rising", RISING_REQUEST), ("falling", FALLING_REQUEST)]
)
def test_capture_service_writes_literal_request_and_validates_exact_count(
    edge: str, expected: bytes
) -> None:
    config = CaptureConfig(1_000_000, 170, 85, 0, edge)  # type: ignore[arg-type]
    identity_lines = [
        "LOGIC_ANALYZER_TEST_BOARD_V6_0",
        "FREQ:1000000",
        "BLASTFREQ:1000000",
        "BUFFER:131072",
        "CHANNELS:24",
        "CAPTURE_STARTED",
    ]

    class Transport:
        writes: list[bytes] = []
        closed = False

        def open(self) -> None:
            return None

        def write(self, data: bytes, timeout: float) -> None:
            assert timeout == 1.0
            self.writes.append(data)

        def read_line(self, timeout: float) -> str:
            assert timeout == 1.0
            return identity_lines.pop(0)

        def read_exact(self, size: int, timeout: float) -> bytes:
            assert timeout == 1.0
            if size == 4:
                return (255).to_bytes(4, "little")
            assert size == 256
            return bytes(range(255)) + b"\0"

        def close(self) -> None:
            self.closed = True

    transport = Transport()
    result = V2DeviceService(lambda port, timeout: transport).capture("/dev/explicit", config, 1.0)  # type: ignore[arg-type]
    assert transport.writes == [IDENTITY_REQUEST, expected]
    assert transport.closed and result.samples.dtype == np.dtype("uint8")
    assert result.samples.tobytes() == bytes(range(255))


def test_capture_service_rejects_count_not_equal_to_request_and_closes() -> None:
    config = CaptureConfig(100, 2, 1, 0, "rising")

    class Transport:
        lines = iter(
            [
                "LOGIC_ANALYZER_TEST_BOARD_V6_0",
                "FREQ:100",
                "BLASTFREQ:100",
                "BUFFER:128",
                "CHANNELS:8",
                "CAPTURE_STARTED",
            ]
        )
        closed = False

        def open(self) -> None:
            pass

        def write(self, data: bytes, timeout: float) -> None:
            pass

        def read_line(self, timeout: float) -> str:
            return next(self.lines)

        def read_exact(self, size: int, timeout: float) -> bytes:
            return (4).to_bytes(4, "little") + b"\0\1\0\0"

        def close(self) -> None:
            self.closed = True

    transport = Transport()
    with pytest.raises(ProtocolError):
        V2DeviceService(lambda port, timeout: transport).capture("/dev/explicit", config, 1.0)  # type: ignore[arg-type]
    assert transport.closed


def test_capture_service_reads_declared_count_before_any_payload_and_closes() -> None:
    config = CaptureConfig(100, 2, 1, 0, "rising")

    class Transport:
        lines = iter(
            [
                "LOGIC_ANALYZER_TEST_BOARD_V6_0",
                "FREQ:100",
                "BLASTFREQ:100",
                "BUFFER:128",
                "CHANNELS:8",
                "CAPTURE_STARTED",
            ]
        )
        closed = False
        reads: list[int] = []

        def open(self) -> None:
            pass

        def write(self, data: bytes, timeout: float) -> None:
            pass

        def read_line(self, timeout: float) -> str:
            return next(self.lines)

        def read_exact(self, size: int, timeout: float) -> bytes:
            self.reads.append(size)
            if size == 4:
                return (0xFFFFFFFF).to_bytes(4, "little")
            raise AssertionError("payload must not be requested after an invalid declared count")

        def close(self) -> None:
            self.closed = True

    transport = Transport()
    with pytest.raises(ProtocolError):
        V2DeviceService(lambda port, timeout: transport).capture("/dev/explicit", config, 1.0)  # type: ignore[arg-type]
    assert transport.reads == [4] and transport.closed


def test_output_collision_force_and_two_file_rollback(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old csv\n")
    replay_path.write_bytes(b"old npz\n")
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), csv_path, replay_path)
    assert csv_path.read_bytes() == b"old csv\n" and replay_path.read_bytes() == b"old npz\n"

    real_replace = os.replace
    finals = {csv_path, replay_path}
    final_moves = 0

    def fail_second_final_replace(source: Path | str, destination: Path | str) -> None:
        nonlocal final_moves
        if Path(destination) in finals:
            final_moves += 1
            if final_moves == 2:
                raise OSError("injected second final rename failure")
        real_replace(source, destination)

    monkeypatch.setattr(capture_format.os, "replace", fail_second_final_replace)
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == b"old csv\n" and replay_path.read_bytes() == b"old npz\n"
    assert not list(tmp_path.glob(".*.tmp")) and not list(tmp_path.glob(".*.bak"))


def test_output_transaction_fsyncs_both_validated_temp_files(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    fsync_descriptors: list[int] = []
    monkeypatch.setattr(capture_format.os, "fsync", fsync_descriptors.append)
    write_capture_outputs(_result(), tmp_path / "capture.csv", tmp_path / "capture.npz")
    assert len(fsync_descriptors) == 2
    assert (tmp_path / "capture.csv").read_bytes() == _EXPECTED_CSV
    loaded, _ = load_replay(tmp_path / "capture.npz")
    assert loaded.tobytes() == _result().samples.tobytes()


def test_output_transaction_rejects_path_aliases_before_creating_any_artifact(
    tmp_path: Path,
) -> None:
    real = tmp_path / "real"
    real.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(real, target_is_directory=True)
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), real / "same.out", alias / "same.out")
    assert not list(real.iterdir())


def test_output_transaction_restores_first_backup_if_second_backup_cannot_be_acquired(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old csv\n")
    replay_path.write_bytes(b"old npz\n")
    original_backup = capture_format._backup
    calls = 0

    def fail_second_backup(path: Path) -> Path | None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected second backup failure")
        return original_backup(path)

    monkeypatch.setattr(capture_format, "_backup", fail_second_backup)
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == b"old csv\n" and replay_path.read_bytes() == b"old npz\n"


def test_second_original_to_backup_rename_failure_restores_and_leaves_no_empty_backup(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old csv\n")
    replay_path.write_bytes(b"old npz\n")
    real_replace = os.replace

    def fail_second_backup_move(source: Path | str, destination: Path | str) -> None:
        if Path(source) == replay_path and Path(destination).suffix == ".bak":
            raise OSError("injected original-to-backup rename failure")
        real_replace(source, destination)

    monkeypatch.setattr(capture_format.os, "replace", fail_second_backup_move)
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == b"old csv\n" and replay_path.read_bytes() == b"old npz\n"
    assert not list(tmp_path.glob(".*.bak")) and not list(tmp_path.glob(".*.tmp"))


def test_output_transaction_validates_csv_temp_before_replacing_existing_files(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old csv\n")
    replay_path.write_bytes(b"old npz\n")
    monkeypatch.setattr(capture_format, "csv_bytes", lambda result: b"wrong,header\n")
    with pytest.raises(OutputError):
        write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == b"old csv\n" and replay_path.read_bytes() == b"old npz\n"


def test_backup_cleanup_failure_after_commit_preserves_both_new_final_artifacts(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    csv_path, replay_path = tmp_path / "capture.csv", tmp_path / "capture.npz"
    csv_path.write_bytes(b"old csv\n")
    replay_path.write_bytes(b"old npz\n")
    real_unlink = Path.unlink

    def fail_backup_unlink(path: Path, *args: object, **kwargs: object) -> None:
        if path.suffix == ".bak":
            raise OSError("injected backup cleanup failure")
        real_unlink(path, *args, **kwargs)

    monkeypatch.setattr(capture_format.Path, "unlink", fail_backup_unlink)
    write_capture_outputs(_result(), csv_path, replay_path, force=True)
    assert csv_path.read_bytes() == _EXPECTED_CSV
    loaded, _ = load_replay(replay_path)
    assert loaded.tobytes() == _result().samples.tobytes()
    # Final installation is already committed; an orphaned rollback copy is
    # safer than deleting/replacing a new final after cleanup failure.
    assert list(tmp_path.glob(".*.bak"))


def test_capture_cli_uses_only_explicit_port_and_keeps_streams_clean(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    opened: list[tuple[str, CaptureConfig, float]] = []

    class Service:
        def capture(self, port: str, config: CaptureConfig, timeout: float) -> CaptureResult:
            opened.append((port, config, timeout))
            return _result()

    monkeypatch.setattr(cli, "V2DeviceService", Service)
    assert (
        cli.main(
            [
                "capture",
                "--port",
                "/dev/only-this-one",
                "--sample-rate",
                "100",
                "--trigger-channel",
                "0",
                "--edge",
                "rising",
                "--pre-samples",
                "2",
                "--post-samples",
                "3",
                "--csv",
                str(tmp_path / "out.csv"),
                "--replay",
                str(tmp_path / "out.npz"),
                "--timeout",
                "1",
            ]
        )
        == 0
    )
    assert opened == [("/dev/only-this-one", CaptureConfig(100, 2, 3, 0, "rising"), 1.0)]
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err == ""


def test_replay_validation_failure_is_exit_five_and_stderr_only(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    bad = tmp_path / "not-a-replay.npz"
    bad.write_bytes(b"not a zip")
    assert cli.main(["replay-validate", str(bad), "--json"]) == 5
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err.startswith("pico-la: ")


def test_hardware_smoke_waveform_mismatch_is_validation_exit_five_and_writes_no_evidence(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    class Service:
        def capture(self, port: str, config: CaptureConfig, timeout: float) -> CaptureResult:
            return CaptureResult(config, np.array([0, 1, 0, 1, 0], dtype=np.uint8), _device())

    evidence = tmp_path / "evidence.json"
    monkeypatch.setattr(cli, "V2DeviceService", Service)
    assert (
        cli.main(
            [
                "hardware-smoke",
                "--port",
                "/dev/explicit",
                "--signal-hz",
                "1000",
                "--sample-rate",
                "100",
                "--trigger-channel",
                "0",
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
        == 5
    )
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err.startswith("pico-la: ")
    assert not evidence.exists()


def test_hardware_smoke_evidence_records_exact_transition_measurement_and_sanitizes_port(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    # Rising D0 indices are 1, 5, 9, 13, 17: four 4-sample periods at 100 Sa/s.
    words = np.array([0, 1, 0, 0] * 5 + [0], dtype=np.uint8)

    class Service:
        def capture(self, port: str, config: CaptureConfig, timeout: float) -> CaptureResult:
            return CaptureResult(config, words, _device())

    evidence = tmp_path / "evidence.json"
    monkeypatch.setattr(cli, "V2DeviceService", Service)
    assert (
        cli.main(
            [
                "hardware-smoke",
                "--port",
                "/dev/not-for-evidence",
                "--signal-hz",
                "25",
                "--sample-rate",
                "100",
                "--trigger-channel",
                "0",
                "--edge",
                "rising",
                "--pre-samples",
                "2",
                "--post-samples",
                "19",
                "--evidence",
                str(evidence),
            ]
        )
        == 0
    )
    assert capsys.readouterr().out == ""
    payload = json.loads(evidence.read_text(encoding="utf-8"))
    assert payload["port"] == "<PORT_SUPPLIED>" and "/dev/not-for-evidence" not in str(payload)
    assert payload["transition_count"] == 5 and payload["span_samples"] == 16
    assert payload["measured_frequency_hz"] == 25
    assert payload["quantization_tolerance_fraction"] == 0.125
    assert payload["source_tolerance_fraction"] == 0.02
    assert payload["tolerance_fraction"] == 0.145
    assert payload["edge_observed"] is True and payload["waveform_nonconstant"] is True
    assert payload["actual_count"] == payload["requested_count"] == 21


def test_hardware_smoke_evidence_install_failure_is_exit_six_and_leaves_no_artifact(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    words = np.array([0, 1, 0, 0] * 5 + [0], dtype=np.uint8)

    class Service:
        def capture(self, port: str, config: CaptureConfig, timeout: float) -> CaptureResult:
            return CaptureResult(config, words, _device())

    def fail_evidence_install(source: Path | str, destination: Path | str) -> None:
        raise OSError("injected evidence rename failure")

    evidence = tmp_path / "evidence.json"
    monkeypatch.setattr(cli, "V2DeviceService", Service)
    monkeypatch.setattr(cli.os, "replace", fail_evidence_install)
    assert (
        cli.main(
            [
                "hardware-smoke",
                "--port",
                "/dev/explicit",
                "--signal-hz",
                "25",
                "--sample-rate",
                "100",
                "--trigger-channel",
                "0",
                "--edge",
                "rising",
                "--pre-samples",
                "2",
                "--post-samples",
                "19",
                "--evidence",
                str(evidence),
            ]
        )
        == 6
    )
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err.startswith("pico-la: ")
    assert not evidence.exists() and not list(tmp_path.glob(".*.tmp"))


@pytest.mark.parametrize(
    ("samples", "edge", "expected"),
    [
        (np.array([0, 1, 0, 0, 0, 1, 0, 0, 0, 1], dtype=np.uint8), "rising", 100 / 4),
        (np.array([1, 0, 1, 1, 1, 0, 1, 1, 1, 0], dtype=np.uint8), "falling", 100 / 4),
    ],
)
def test_frequency_measurement_uses_requested_edge_first_last_span(
    samples: np.ndarray[tuple[int], np.dtype[np.uint8]], edge: str, expected: float
) -> None:
    measured, count, span, quantization = cli._frequency_measurement(samples, 0, edge, 100)
    assert (measured, count, span, quantization) == (expected, 3, 8, 0.25)


def test_frequency_measurement_rejects_fewer_than_two_requested_polarity_edges() -> None:
    with pytest.raises(ProtocolError):
        cli._frequency_measurement(np.array([0, 1, 1, 1], dtype=np.uint8), 0, "rising", 100)
