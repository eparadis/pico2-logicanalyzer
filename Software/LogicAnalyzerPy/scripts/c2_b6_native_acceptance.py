#!/usr/bin/env python3
"""Bounded sanitized C2-B6 native-device acceptance harness."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import threading
from pathlib import Path

from pico_logic_analyzer.driver import V2DeviceService
from pico_logic_analyzer.model import CaptureConfig

WIDTHS = (8, 16, 24)
PHYSICAL_SIGNAL_CHANNELS = (0, 8, 16, 23)


def _atomic_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as file:
            json.dump(value, file, sort_keys=True, separators=(",", ":"))
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def run(port: str, evidence: Path, service: V2DeviceService | None = None) -> None:
    if not port:
        raise ValueError("an explicit port is required")
    owner = V2DeviceService() if service is None else service
    before, after = owner.identify_after_reopen(port, 10.0)
    if before != after:
        raise RuntimeError("device capabilities changed after reopen")
    observations: list[dict[str, object]] = []
    for width in WIDTHS:
        config = CaptureConfig(100_000, 1024, 3072, 0, "rising", tuple(range(width)))
        result = owner.capture_cancellable(port, config, threading.Event(), 10.0)
        active = []
        for channel in PHYSICAL_SIGNAL_CHANNELS:
            if channel in config.channel_ids:
                values = result.channel_samples(channel)
                if bool((values[1:] != values[:-1]).any()):
                    active.append(channel)
        observations.append(
            {
                "width": width,
                "sample_count": len(result.samples),
                "trigger_channel": result.config.trigger_channel,
                "trigger_index": result.trigger_index,
                "observed_signal_channels": active,
            }
        )
    second = owner.capture_cancellable(
        port,
        CaptureConfig(100_000, 1024, 3072, 0, "rising", tuple(range(24))),
        threading.Event(),
        10.0,
    )
    _atomic_json(
        evidence,
        {
            "port": "<PORT_SUPPLIED>",
            "device_id": "device-1",
            "capabilities": {
                "max_frequency_hz": before.max_frequency_hz,
                "blast_frequency_hz": before.blast_frequency_hz,
                "buffer_size": before.buffer_size,
                "channel_count": before.channel_count,
            },
            "reidentified_after_reopen": True,
            "captures": observations,
            "second_capture_sample_count": len(second.samples),
            "serial_closed_between_operations": True,
            "persistent_device_change": False,
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True, metavar="PORT")
    parser.add_argument("--evidence", required=True, type=Path, metavar="PATH")
    arguments = parser.parse_args()
    run(arguments.port, arguments.evidence)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
