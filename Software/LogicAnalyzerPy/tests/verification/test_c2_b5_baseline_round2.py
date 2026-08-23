"""Independent round-two validation of the frozen C2-B5 baseline."""

from __future__ import annotations

import hashlib
import io
import json
import math
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).parents[2]
WEB = ROOT / "web"
BENCHMARKS = WEB / "benchmarks"
BASELINE = ROOT / "docs/performance/c2-b5-baseline-round-1.json"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _nearest(values: list[float], fraction: float) -> float:
    ordered = sorted(values)
    return ordered[max(0, math.ceil(len(ordered) * fraction) - 1)]


def _samples(path: Path) -> np.ndarray[Any, Any]:
    with zipfile.ZipFile(path) as archive:
        assert set(archive.namelist()) == {"samples.npy", "metadata.npy"}
        return np.load(io.BytesIO(archive.read("samples.npy")), allow_pickle=False)


def test_frozen_fixture_corpus_and_bus_patterns_are_literal() -> None:
    manifest = json.loads((BENCHMARKS / "fixtures.json").read_text(encoding="utf-8"))
    roles = {role for item in manifest["fixtures"] for role in item["roles"]}
    assert roles == {
        "empty", "schema-1", "constant", "sparse", "dense", "maximum-8",
        "maximum-16", "maximum-24", "bus-representative", "bus-worst",
    }
    for item in manifest["fixtures"]:
        if item["artifact"] is None:
            assert item["sample_count"] == 0 and item["sha256"] is None
            continue
        path = BENCHMARKS / item["artifact"]
        assert _sha256(path) == item["sha256"]
        assert path.stat().st_size == item["payload_bytes"]
        samples = _samples(path)
        assert samples.shape == (item["sample_count"],)
        assert samples.dtype == {8: np.uint8, 16: np.uint16, 24: np.uint32}[item["width"]]
        if "bus-representative" in item["roles"]:
            values = samples.astype(np.uint32)
            assert np.array_equal((values >> 7) & 1, (np.arange(len(values)) // 8) & 1)
            assert len(np.unique(values & 0x7F)) > 2
        if "bus-worst" in item["roles"]:
            assert np.count_nonzero(samples[1:] != samples[:-1]) == len(samples) - 1


def test_baseline_digests_identity_bounds_and_sanitization() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    assert report["schema_version"] == 2
    assert report["method"] == "c2-b5-playwright-production-v2"
    assert report["threshold"] is None
    assert report["viewport"] == {"width": 1280, "height": 900, "device_pixel_ratio": 1}
    assert report["browser"] and report["automation"] == "Playwright 1.50.1"
    assert report["node"] == "v22.14.0"
    assert report["host"] == {"platform": "darwin", "release": "24.6.0", "architecture": "x64"}
    assert report["fixture_manifest_sha256"] == _sha256(BENCHMARKS / "fixtures.json")
    assert report["fixture_generator_sha256"] == _sha256(BENCHMARKS / "generate_fixtures.py")
    assert report["benchmark_script_sha256"] == _sha256(WEB / "tests/performance.spec.ts")
    assert report["production_asset_manifest_sha256"] == _sha256(WEB / "production-assets.json")
    assert report["memory_reliable"] is False and report["used_js_heap_bytes"] is None
    serialized = BASELINE.read_text(encoding="utf-8")
    for forbidden in ("/Users/", "/dev/", "127.0.0.1", "pico_la_capability", "secret", "token"):
        assert forbidden not in serialized


def test_raw_load_and_interaction_statistics_recompute_exactly() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    loads = report["loads"]
    required = {
        "empty", "constant-8", "sparse-16", "dense-24", "maximum-8",
        "maximum-16", "maximum-24", "bus-representative-8",
    }
    assert Counter(item["name"] for item in loads) == Counter({name: 2 for name in required})
    assert report["load_iterations_per_case"] == 2
    assert report["load_iterations"] == len(loads) == 16
    assert report["load_median_ms"] == _nearest([item["milliseconds"] for item in loads], 0.5)
    assert report["load_p95_ms"] == _nearest([item["milliseconds"] for item in loads], 0.95)
    for statistics in report["load_statistics"]:
        raw = statistics["initial_ready_paint_ms"]
        assert statistics["iterations"] == len(raw) == 2
        assert statistics["median_ms"] == _nearest(raw, 0.5)
        assert statistics["p95_ms"] == _nearest(raw, 0.95)
    interactions = report["interactions_ms"]
    assert report["warmup_iterations"] == 3
    assert report["interaction_iterations"] == len(interactions) == 30
    assert report["interaction_median_ms"] == _nearest(interactions, 0.5)
    assert report["interaction_p95_ms"] == _nearest(interactions, 0.95)
    assert max(item["commands"] for item in loads) <= 24 * (2 * 960 + 2) + 1
    assert max(item["dom_nodes"] for item in loads) < 1000


def test_raw_bus_statistics_cover_both_roles_and_modes() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    observations = report["bus_observations"]
    assert {(item["roles"][0], item["mode"]) for item in observations} == {
        ("bus-representative", "transition"),
        ("bus-representative", "distinct-strobe"),
        ("bus-worst", "transition"),
        ("bus-worst", "distinct-strobe"),
    }
    payloads = {item["name"]: item.get("payload_bytes") for item in report["fixtures"]}
    assert report["bus_iterations_per_mode_and_role"] == 2
    for item in observations:
        raw = item["timings_ms"]
        assert item["iterations"] == len(raw) == 2
        assert item["row_counts"] == [100, 100] and item["rows"] == 100
        assert item["payload_bytes"] == payloads[item["fixture"]]
        assert item["median_ms"] == _nearest(raw, 0.5)
        assert item["p95_ms"] == _nearest(raw, 0.95)
