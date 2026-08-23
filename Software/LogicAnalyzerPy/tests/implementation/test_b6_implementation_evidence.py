from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "testdata" / "evidence" / "c2-b6-implementation.json"


def test_b6_implementation_evidence_is_complete_and_sanitized() -> None:
    raw = EVIDENCE.read_text(encoding="utf-8")
    evidence = json.loads(raw)

    assert evidence["candidate_commit"] == "4640f746c080087fc9783d89a18e3c8e5573a454"
    assert evidence["candidate_tree"] == "50945a9387709e7637d98294ba5b9cc08dc87cfd"
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
    assert [capture["dtype"] for capture in hardware["captures"]] == ["uint8", "uint16", "uint32"]
    assert [capture["driven_mask_hex"] for capture in hardware["captures"]] == [
        "0x01",
        "0x0101",
        "0x810101",
    ]
    assert [capture["driven_projection"] for capture in hardware["captures"]] == [
        [0, 0x01],
        [0, 0x0101],
        [0, 0x810101],
    ]
    assert all(capture["rising_edges_per_driven_channel"] == 31 for capture in hardware["captures"])
    assert all(capture["expected_signal_frequency_hz"] == 1000 for capture in hardware["captures"])
    assert [capture["npz_sha256"] for capture in hardware["captures"]] == [
        "edd4ca5f3d6b70575f540f09bb6e77e648f3e2ed8d1bb14a5954aefa7cb76c71",
        "63f3ecc846c1b451f6832ff1c8adba864c70e6ec14901cc5c6b4e143511b24a0",
        "75ae2fa1884f1725800babc37321bf653c989336bba3bc922d423f7e1ff0622e",
    ]
    assert [capture["csv_sha256"] for capture in hardware["captures"]] == [
        "af443f08089ac51aa3d93343730a864f172a948c14be68fa972399dbceb66311",
        "67830a7eafdadfced8145ba50a388fe7714002db23d3f9675ae5ce0f047d5548",
        "5cc335356ba8271ff20d44b81b9a8460f442b8f0147ec8228a29cc1dacbd2264",
    ]
    assert hardware["captures"][2]["bits_24_through_31_zero"] is True
    assert hardware["csv_channel_order_labels_and_bits_match_npz"] is True
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
        "transition_count": 42,
        "measured_frequency_hz": 1011.5963483839131,
        "expected_frequency_hz": 1000,
        "artifact_sha256": "f72dd947d455b84ee0a12bbce48b7ff84c9c27ed749486b9f2d2623c45cd8862",
        "persistent_device_change": False,
    }
    assert all(value is False for value in evidence["sanitization"].values())

    forbidden = ("/dev/", "usbmodem", "usbserial", "logic_analyzer_pico")
    assert not any(value in raw.lower() for value in forbidden)
