from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "testdata" / "evidence" / "c2-b6-implementation.json"


def test_b6_implementation_evidence_is_complete_and_sanitized() -> None:
    raw = EVIDENCE.read_text(encoding="utf-8")
    evidence = json.loads(raw)

    assert evidence["source_revision"] == "844cf3fbcf8a01530ea05a63b02260f3d22ffedc"
    hardware = evidence["hardware_boundary"]
    assert hardware["public_device_id"] == "device-1"
    assert hardware["port"] == "<PORT_SUPPLIED>"
    assert hardware["capabilities"] == {"channel_count": 24, "buffer_size": 393216}
    assert [capture["width"] for capture in hardware["captures"]] == [8, 16, 24]
    assert [capture["observed_signal_channels"] for capture in hardware["captures"]] == [
        [0],
        [0, 8],
        [0, 8, 16, 23],
    ]
    assert all(capture["sample_count"] == 4096 for capture in hardware["captures"])
    assert all(capture["trigger_index"] == 1024 for capture in hardware["captures"])
    assert hardware["reidentified_after_reopen"] is True
    assert hardware["second_capture_sample_count"] == 4096
    assert hardware["serial_closed_between_operations"] is True
    assert hardware["persistent_device_change"] is False

    assert evidence["production_browser"] == {"tests_passed": 1, "exit_status": 0}
    assert evidence["fixed_low_recovery"] == {
        "idle_channel": 1,
        "idle_level": 0,
        "cancel_byte_hex": "ff",
        "reidentified": True,
        "sample_count": 6144,
        "transition_count": 41,
        "signal_frequency_hz": 1000,
        "persistent_device_change": False,
    }
    assert all(value is False for value in evidence["sanitization"].values())

    forbidden = ("/dev/", "usbmodem", "usbserial", "logic_analyzer_pico")
    assert not any(value in raw.lower() for value in forbidden)
