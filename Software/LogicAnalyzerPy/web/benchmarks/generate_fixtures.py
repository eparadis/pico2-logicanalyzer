#!/usr/bin/env python3
"""Generate the frozen deterministic C2-B5 rendering corpus."""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path

import numpy as np

from pico_logic_analyzer.formats import replay_bytes
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

ROOT = Path(__file__).parent
FIXTURES = ROOT / "fixtures"
SAMPLE_RATE = 1_000_000
BUFFER_BYTES = 384 * 1024


def result(width: int, count: int, pattern: str) -> CaptureResult:
    dtype = (np.uint8, np.uint16, np.uint32)[(width - 1) // 8]
    indices = np.arange(count, dtype=np.uint32)
    mask = np.uint32((1 << width) - 1)
    if pattern == "constant":
        samples = np.zeros(count, dtype=dtype)
    elif pattern == "sparse":
        samples = (((indices // 4096) * np.uint32(0x9E37)) & mask).astype(dtype)
    else:
        samples = ((indices ^ (indices >> 1)) & mask).astype(dtype)
    trigger = count // 2
    config = CaptureConfig(SAMPLE_RATE, trigger, count - trigger, 0, "rising", tuple(range(width)))
    device = DeviceInfo("LOGIC_ANALYZER_PICO_2_V6_0", 100_000_000, 100_000_000, BUFFER_BYTES, 24)
    return CaptureResult(config, samples, device)


def schema1_bytes() -> bytes:
    count = 1_024
    metadata = {
        "schema_version": 1,
        "provisional": True,
        "sample_rate_hz": SAMPLE_RATE,
        "requested_count": count,
        "actual_count": count,
        "pre_trigger_samples": count // 2,
        "post_trigger_samples": count // 2,
        "trigger_index": count // 2,
        "trigger_channel": 0,
        "trigger_edge": "rising",
        "channel_ids": list(range(8)),
        "channel_labels": [f"D{i}" for i in range(8)],
        "channel_mapping": [f"D{i}" for i in range(8)],
        "device": {
            "identity": "LOGIC_ANALYZER_PICO_2_V6_0",
            "capabilities": {
                "max_frequency_hz": 100_000_000,
                "blast_frequency_hz": 100_000_000,
                "buffer_size": BUFFER_BYTES,
                "channel_count": 24,
            },
        },
    }
    encoded = json.dumps(
        metadata, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    output = io.BytesIO()
    np.savez(
        output,
        samples=(np.arange(count, dtype=np.uint8) ^ (np.arange(count, dtype=np.uint8) >> 1)),
        metadata=np.frombuffer(encoded, dtype=np.uint8),
    )
    return output.getvalue()


def main() -> int:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    definitions = [
        ("constant-8", 8, 65_536, "constant", ["constant"]),
        ("sparse-16", 16, 196_608, "sparse", ["sparse"]),
        ("dense-24", 24, 32_768, "dense", ["dense", "bus-worst"]),
        ("maximum-8", 8, 393_216, "dense", ["maximum-8"]),
        ("maximum-16", 16, 196_608, "dense", ["maximum-16"]),
        ("maximum-24", 24, 98_304, "dense", ["maximum-24"]),
        ("bus-representative-8", 8, 4_096, "sparse", ["bus-representative"]),
    ]
    entries: list[dict[str, object]] = [
        {"name": "empty", "roles": ["empty"], "sample_count": 0, "artifact": None, "sha256": None}
    ]
    legacy = schema1_bytes()
    legacy_path = FIXTURES / "schema1-8.npz"
    legacy_path.write_bytes(legacy)
    entries.append(
        {
            "name": "schema1-8",
            "roles": ["schema-1"],
            "width": 8,
            "sample_count": 1_024,
            "pattern": "dense",
            "artifact": f"fixtures/{legacy_path.name}",
            "sha256": hashlib.sha256(legacy).hexdigest(),
            "payload_bytes": len(legacy),
        }
    )
    for name, width, count, pattern, roles in definitions:
        data = replay_bytes(result(width, count, pattern))
        path = FIXTURES / f"{name}.npz"
        path.write_bytes(data)
        entries.append(
            {
                "name": name,
                "roles": roles,
                "width": width,
                "sample_count": count,
                "pattern": pattern,
                "artifact": f"fixtures/{path.name}",
                "sha256": hashlib.sha256(data).hexdigest(),
                "payload_bytes": len(data),
            }
        )
    manifest = {
        "schema_version": 1,
        "generator": "generate_fixtures.py",
        "sample_rate_hz": SAMPLE_RATE,
        "device_buffer_bytes": BUFFER_BYTES,
        "fixtures": entries,
    }
    (ROOT / "fixtures.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
