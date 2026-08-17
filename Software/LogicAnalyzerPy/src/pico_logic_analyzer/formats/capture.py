"""Deterministic Cycle 1 capture artifacts and their two-file transaction."""

from __future__ import annotations

import csv
import io
import json
import os
import tempfile
from pathlib import Path

import numpy as np

from pico_logic_analyzer.formats.replay import load_replay
from pico_logic_analyzer.model import CaptureResult, ProtocolError


class OutputError(OSError):
    """A capture artifact could not be safely installed."""


def _metadata(result: CaptureResult) -> dict[str, object]:
    device = result.device
    config = result.config
    return {
        "actual_count": len(result.samples),
        "channel_ids": list(config.channel_ids),
        "channel_labels": list(result.channel_labels),
        "channel_mapping": list(result.channel_mapping),
        "device": {
            "capabilities": {
                "blast_frequency_hz": device.blast_frequency_hz,
                "buffer_size": device.buffer_size,
                "channel_count": device.channel_count,
                "max_frequency_hz": device.max_frequency_hz,
            },
            "identity": device.identity,
        },
        "post_trigger_samples": config.post_trigger_samples,
        "pre_trigger_samples": config.pre_trigger_samples,
        "provisional": True,
        "requested_count": config.requested_count,
        "sample_rate_hz": config.sample_rate_hz,
        "schema_version": 1,
        "trigger_channel": config.trigger_channel,
        "trigger_edge": config.trigger_edge,
        "trigger_index": result.trigger_index,
    }


def csv_bytes(result: CaptureResult) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    for row in _csv_rows(result):
        writer.writerow(row)
    return output.getvalue().encode("utf-8")


def _csv_rows(result: CaptureResult) -> list[list[str | int]]:
    rows: list[list[str | int]] = [
        ["sample_index", "time_seconds", "trigger", *result.channel_labels]
    ]
    rate = result.config.sample_rate_hz
    for index, word in enumerate(result.samples):
        rows.append(
            [
                index,
                format((index - result.trigger_index) / rate, ".12g"),
                int(index == result.trigger_index),
                *(int((int(word) >> bit) & 1) for bit in range(8)),
            ]
        )
    return rows


def _validate_csv_temp(path: Path, result: CaptureResult) -> None:
    try:
        with path.open("r", encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))
    except (OSError, UnicodeError, csv.Error) as exc:
        raise OutputError("invalid CSV temporary artifact") from exc
    expected = [[str(value) for value in row] for row in _csv_rows(result)]
    if rows != expected:
        raise OutputError("CSV validation did not match capture")


def replay_bytes(result: CaptureResult) -> bytes:
    metadata = json.dumps(
        _metadata(result), ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    output = io.BytesIO()
    # np.savez is deliberately uncompressed: deterministic member data and an allowed ZIP method.
    np.savez(output, samples=result.samples, metadata=np.frombuffer(metadata, dtype=np.uint8))
    return output.getvalue()


def _write_temp(path: Path, data: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as file:
            file.write(data)
            file.flush()
            os.fsync(file.fileno())
        return temp
    except Exception:
        temp.unlink(missing_ok=True)
        raise


def _backup(path: Path) -> Path | None:
    if not path.exists():
        return None
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".bak", dir=path.parent)
    os.close(descriptor)
    backup = Path(name)
    try:
        os.replace(path, backup)
    except Exception:
        backup.unlink(missing_ok=True)
        raise
    return backup


def write_capture_outputs(
    result: CaptureResult, csv_path: Path, replay_path: Path, *, force: bool = False
) -> None:
    """Validate temps, then atomically install or restore both final artifacts."""
    csv_path, replay_path = Path(csv_path), Path(replay_path)
    if csv_path.resolve() == replay_path.resolve():
        raise OutputError("CSV and replay paths must differ")
    if not force and (csv_path.exists() or replay_path.exists()):
        raise OutputError("output exists; use --force to replace it")
    csv_temp: Path | None = None
    replay_temp: Path | None = None
    backups: dict[Path, Path | None] = {}
    installed: list[Path] = []
    try:
        expected_csv = csv_bytes(result)
        csv_temp = _write_temp(csv_path, expected_csv)
        replay_temp = _write_temp(replay_path, replay_bytes(result))
        _validate_csv_temp(csv_temp, result)
        loaded, metadata = load_replay(replay_temp)
        if not np.array_equal(loaded, result.samples) or metadata != _metadata(result):
            raise OutputError("replay validation did not match capture")
        # Record each backup immediately: a later move failure must not lose the
        # earlier original from rollback bookkeeping.
        backups[csv_path] = _backup(csv_path)
        backups[replay_path] = _backup(replay_path)
        os.replace(csv_temp, csv_path)
        csv_temp = None
        installed.append(csv_path)
        os.replace(replay_temp, replay_path)
        replay_temp = None
        installed.append(replay_path)
        for final, backup in tuple(backups.items()):
            if backup is not None:
                try:
                    backup.unlink()
                except OSError:
                    # Finals are already installed; an orphaned backup is safer
                    # than attempting an impossible rollback after success.
                    pass
                backups[final] = None
    except Exception as exc:
        for final in installed:
            final.unlink(missing_ok=True)
        for final, backup in backups.items():
            if backup is not None and backup.exists():
                os.replace(backup, final)
        if isinstance(exc, OutputError | ProtocolError):
            raise OutputError(str(exc)) from exc
        raise OutputError(f"could not write capture outputs: {exc}") from exc
    finally:
        if csv_temp is not None:
            csv_temp.unlink(missing_ok=True)
        if replay_temp is not None:
            replay_temp.unlink(missing_ok=True)
        for backup in backups.values():
            if backup is not None:
                backup.unlink(missing_ok=True)
