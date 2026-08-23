#!/usr/bin/env python3
"""Independently audit one raw Cycle 2 B3 schema-2 capture and its CSV."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from pathlib import Path

import numpy as np


def _channels(value: str) -> tuple[int, ...]:
    values = tuple(int(item) for item in value.split(","))
    if not values or len(set(values)) != len(values):
        raise argparse.ArgumentTypeError("channels must be nonempty and unique")
    return values


def _canonical_csv(samples: np.ndarray, metadata: dict[str, object]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    labels = metadata["channel_labels"]
    channels = metadata["channel_ids"]
    trigger_index = metadata["trigger_index"]
    rate = metadata["sample_rate_hz"]
    assert isinstance(labels, list) and isinstance(channels, list)
    assert isinstance(trigger_index, int) and isinstance(rate, int)
    writer.writerow(["sample_index", "time_seconds", "trigger", *labels])
    for index, word in enumerate(samples):
        writer.writerow(
            [
                index,
                format((index - trigger_index) / rate, ".12g"),
                int(index == trigger_index),
                *(int((int(word) >> bit) & 1) for bit in range(len(channels))),
            ]
        )
    return output.getvalue().encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay", type=Path, required=True)
    parser.add_argument("--csv", dest="csv_path", type=Path, required=True)
    parser.add_argument("--channels", type=_channels, required=True)
    parser.add_argument("--mask", type=lambda value: int(value, 0), required=True)
    parser.add_argument("--dtype", choices=("uint8", "uint16", "uint32"), required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    with np.load(args.replay, allow_pickle=False) as payload:
        samples = payload["samples"]
        metadata_bytes = payload["metadata"]
    metadata = json.loads(metadata_bytes.tobytes().decode("utf-8"))
    expected_dtype = np.dtype(args.dtype)
    if samples.ndim != 1 or samples.dtype != expected_dtype or len(samples) != 6144:
        raise SystemExit("raw schema-2 sample shape, dtype, or count mismatch")
    if not isinstance(metadata, dict):
        raise SystemExit("metadata is not an object")
    expected = {
        "schema_version": 2,
        "sample_dtype": args.dtype,
        "sample_rate_hz": 100000,
        "requested_count": 6144,
        "actual_count": 6144,
        "pre_trigger_samples": 2048,
        "post_trigger_samples": 4096,
        "trigger_index": 2048,
        "trigger_channel": 0,
        "trigger_edge": "rising",
        "channel_ids": list(args.channels),
    }
    if any(metadata.get(key) != value for key, value in expected.items()):
        raise SystemExit("raw schema-2 metadata mismatch")
    words = samples.astype(np.uint32, copy=False)
    projection = words & np.uint32(args.mask)
    highs = projection == args.mask
    lows = projection == 0
    rising = np.flatnonzero((projection[1:] != projection[:-1]) & (projection[1:] == args.mask)) + 1
    if not highs.any() or not lows.any() or len(rising) < 2:
        raise SystemExit("driven-mask lows/highs or rising transitions missing")
    span = int(rising[-1] - rising[0])
    measured = 100000 * (len(rising) - 1) / span
    tolerance = 0.02 + 2 / span
    if abs(measured - 1000) / 1000 > tolerance:
        raise SystemExit("driven-mask frequency outside tolerance")
    upper_byte_zero = not bool(np.any(words & np.uint32(0xFF000000)))
    if args.dtype == "uint32" and not upper_byte_zero:
        raise SystemExit("24-channel upper byte is nonzero")
    reconstructed = _canonical_csv(samples, metadata)
    original = args.csv_path.read_bytes()
    if original != reconstructed:
        raise SystemExit("CSV does not equal independently reconstructed canonical CSV")
    report = {
        "actual_count": 6144,
        "csv_sha256": hashlib.sha256(original).hexdigest(),
        "dtype": args.dtype,
        "driven_mask": hex(args.mask),
        "frequency_hz": measured,
        "rising_transitions": int(len(rising)),
        "schema_version": 2,
        "tolerance_fraction": tolerance,
        "upper_byte_zero": upper_byte_zero,
    }
    args.out.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
