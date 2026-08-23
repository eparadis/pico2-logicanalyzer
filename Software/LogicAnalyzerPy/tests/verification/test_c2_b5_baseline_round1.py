"""Independent C2-B5 fixture and reproducibility checks."""

from __future__ import annotations

import hashlib
import io
import json
import zipfile
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parents[2]
BENCHMARKS = ROOT / "web/benchmarks"
BASELINE = ROOT / "docs/performance/c2-b5-baseline-round-1.json"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _inert_members(path: Path) -> tuple[np.ndarray, dict[str, object]]:
    with zipfile.ZipFile(path) as archive:
        assert set(archive.namelist()) == {"samples.npy", "metadata.npy"}
        samples = np.load(io.BytesIO(archive.read("samples.npy")), allow_pickle=False)
        metadata_bytes = np.load(
            io.BytesIO(archive.read("metadata.npy")), allow_pickle=False
        ).tobytes()
    return samples, json.loads(metadata_bytes)


def test_fixture_manifest_digests_widths_and_members_are_independent() -> None:
    manifest = json.loads((BENCHMARKS / "fixtures.json").read_text(encoding="utf-8"))
    required_roles = {
        "empty", "schema-1", "constant", "sparse", "dense", "maximum-8",
        "maximum-16", "maximum-24", "bus-representative", "bus-worst",
    }
    assert {role for item in manifest["fixtures"] for role in item["roles"]} == required_roles
    expected_dtype = {8: np.dtype("uint8"), 16: np.dtype("uint16"), 24: np.dtype("uint32")}
    for item in manifest["fixtures"]:
        if item["artifact"] is None:
            assert item["name"] == "empty" and item["sample_count"] == 0
            continue
        path = BENCHMARKS / item["artifact"]
        assert _sha256(path) == item["sha256"]
        assert path.stat().st_size == item["payload_bytes"]
        samples, metadata = _inert_members(path)
        assert samples.dtype == expected_dtype[item["width"]]
        assert samples.shape == (item["sample_count"],)
        assert metadata["channel_ids"] == list(range(item["width"]))
        assert metadata["channel_labels"] == [f"D{index}" for index in range(item["width"])]


def test_each_required_render_case_has_multiple_initial_observations() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    counts = Counter(item["name"] for item in report["loads"])
    required = {
        "empty", "constant-8", "sparse-16", "dense-24", "maximum-8",
        "maximum-16", "maximum-24", "bus-representative-8",
    }
    assert required <= counts.keys()
    assert all(counts[name] >= 2 for name in required)


def test_baseline_preserves_raw_samples_for_independent_percentiles() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    interactions = report["interactions_ms"]
    assert len(interactions) == report["interaction_iterations"] == 30
    ordered = sorted(interactions)
    assert report["interaction_median_ms"] == ordered[14]
    assert report["interaction_p95_ms"] == ordered[28]


def test_baseline_measures_representative_and_worst_bus_tables() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    observations = report["bus_observations"]
    roles = {role for item in observations for role in item["roles"]}
    assert {"bus-representative", "bus-worst"} <= roles
    assert all(item["iterations"] >= 2 for item in observations)
    assert all(item["rows"] <= 100 and item["payload_bytes"] > 0 for item in observations)
    assert all(item["median_ms"] > 0 and item["p95_ms"] > 0 for item in observations)
