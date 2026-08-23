from __future__ import annotations

import hashlib
import json
from pathlib import Path

from pico_logic_analyzer.formats.replay import import_replay_bytes

ROOT = Path(__file__).parents[2]
BENCHMARK = ROOT / "web" / "benchmarks"
BASELINE = ROOT / "docs" / "performance" / "c2-b5-baseline-round-1.json"


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_frozen_b5_fixture_corpus_is_complete_and_self_authenticating() -> None:
    manifest = json.loads((BENCHMARK / "fixtures.json").read_text(encoding="utf-8"))
    fixtures = manifest["fixtures"]
    roles = {role for fixture in fixtures for role in fixture["roles"]}
    assert roles == {
        "empty",
        "schema-1",
        "constant",
        "sparse",
        "dense",
        "maximum-8",
        "maximum-16",
        "maximum-24",
        "bus-representative",
        "bus-worst",
    }
    assert manifest["device_buffer_bytes"] == 384 * 1024
    expected_maximum = {8: 393_216, 16: 196_608, 24: 98_304}
    for fixture in fixtures:
        if fixture["artifact"] is None:
            assert fixture == {
                "artifact": None,
                "name": "empty",
                "roles": ["empty"],
                "sample_count": 0,
                "sha256": None,
            }
            continue
        path = BENCHMARK / fixture["artifact"]
        data = path.read_bytes()
        assert len(data) == fixture["payload_bytes"]
        assert _digest(path) == fixture["sha256"]
        capture = import_replay_bytes(data)
        assert len(capture.samples) == fixture["sample_count"]
        assert len(capture.config.channel_ids) == fixture["width"]
        for role in fixture["roles"]:
            if role.startswith("maximum-"):
                assert fixture["sample_count"] == expected_maximum[fixture["width"]]


def test_b5_baseline_freezes_method_and_measurements_but_no_threshold() -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    assert report["method"] == "c2-b5-playwright-production-v1"
    assert report["threshold"] is None
    assert report["viewport"] == {"width": 1280, "height": 900, "device_pixel_ratio": 1}
    assert report["warmup_iterations"] == 3
    assert report["load_iterations"] == len(report["loads"]) == 15
    assert report["interaction_iterations"] == 30
    assert report["fixture_manifest_sha256"] == _digest(BENCHMARK / "fixtures.json")
    assert report["fixture_generator_sha256"] == _digest(BENCHMARK / "generate_fixtures.py")
    assert report["benchmark_script_sha256"] == _digest(
        ROOT / "web" / "tests" / "performance.spec.ts"
    )
    assert report["production_asset_manifest_sha256"] == _digest(
        ROOT / "web" / "production-assets.json"
    )
    assert {item["name"] for item in report["loads"]} >= {
        "empty",
        "constant-8",
        "sparse-16",
        "dense-24",
        "maximum-8",
        "maximum-16",
        "maximum-24",
        "bus-representative-8",
    }
    assert report["load_median_ms"] > 0 and report["load_p95_ms"] > 0
    assert report["interaction_median_ms"] > 0 and report["interaction_p95_ms"] > 0
    assert max(item["commands"] for item in report["loads"]) <= 24 * (960 * 2 + 2) + 1
    assert max(item["dom_nodes"] for item in report["loads"]) < 1000
    serialized = BASELINE.read_text(encoding="utf-8")
    for forbidden in ("/Users/", "/dev/", "127.0.0.1", "pico_la_capability"):
        assert forbidden not in serialized
