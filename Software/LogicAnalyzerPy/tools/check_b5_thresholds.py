#!/usr/bin/env python3
"""Enforce the immutable operator-approved B5 ceilings without rebasing."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

TIMING_CEILINGS = {
    "load": (1000.0, 772.0999999986961),
    "interaction": (750.0, 580.3000000026077),
    "bus-representative:transition": (500.0, 261.4499999973923),
    "bus-representative:distinct-strobe": (300.0, 116.7250000052154),
    "bus-worst:transition": (900.0, 710.1499999947846),
    "bus-worst:distinct-strobe": (500.0, 263.1999999973923),
}

FIXTURE_DIGESTS = {
    "empty": None,
    "schema1-8": "c2f4d446b754c09e57412f02bde8d751f18a997d14d1df72bdc49654ab0a7457",
    "constant-8": "51b98c66622aa724118713ad1dcb409d6415ce3491f431e12ee9f770640c26e1",
    "sparse-16": "39e53e363b6aab3cdd6f1fdae2083e5f7ffe78196ccf033fb4496e6ca0a36f6a",
    "dense-24": "f48f87ecaf743a224b0344c0a4025dee72e0ecb6c64f1e546f7c85f514e3f5e3",
    "maximum-8": "13a1de3c93c24f3a2ffcf51f7e635a1180fed5bc376ada689933c9e5505e5ccc",
    "maximum-16": "a05394ce8b4ffd1efb54e023afe54fd311698f7a671f2a089c0773c3cfbddd14",
    "maximum-24": "c582841605c6d4c212057864eb01fe200aaa3c085aaf532643dea575669ce702",
    "bus-representative-8": "6cbd86b4346e7922d1685c08e8c49ed49bb7e820a5714bea1ba5e10c266328c3",
}
LOAD_ROLES = {
    "empty",
    "constant-8",
    "sparse-16",
    "dense-24",
    "maximum-8",
    "maximum-16",
    "maximum-24",
    "bus-representative-8",
}
PRODUCT_IDENTITIES = {
    (
        "2efeca32fcac6eb8c98480d49d02b304b9985121d9f2fe3f85e8ffe47e1c930b",
        "00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9",
    ),
    (
        "68dd480c3e8df3cc0409053c81834cb082e64243d22e08d2217a675d63e18265",
        "c27b08c3fbbce7ead5e7afa4b92bffdaf9623f46f4319d92c78942ab2e59059d",
    ),
}


def nearest_rank(values: list[float], fraction: float) -> float:
    if not values or any(
        type(value) not in (int, float) or not math.isfinite(value) for value in values
    ):
        raise AssertionError("raw timings must be finite numeric values")
    return sorted(values)[max(0, math.ceil(len(values) * fraction) - 1)]


def validate(report: dict[str, object]) -> None:
    if report.get("method") != "c2-b5-playwright-production-v2":
        raise AssertionError("frozen benchmark method changed")
    frozen_method = {
        "schema_version": 2,
        "warmup_iterations": 3,
        "load_iterations_per_case": 2,
        "load_iterations": 16,
        "interaction_iterations": 30,
        "bus_iterations_per_mode_and_role": 2,
        "statistics": {
            "method": "nearest-rank",
            "index_formula": "max(0, ceil(p * n) - 1) on ascending raw samples",
            "median_p": 0.5,
            "high_percentile": "p95",
            "high_percentile_p": 0.95,
            "rounding": (
                "none; JSON retains the raw IEEE-754 millisecond values returned by the "
                "timing clocks"
            ),
        },
        "timing": (
            "performance.now around UI action through API completion, rendered Canvas/table "
            "DOM, and next animation frame; Node performance.now brackets empty navigation/"
            "load/paint"
        ),
        "browser": "133.0.6943.16",
        "automation": "Playwright 1.50.1",
        "node": "v22.14.0",
        "host": {"platform": "darwin", "release": "24.6.0", "architecture": "x64"},
    }
    if any(report.get(key) != value for key, value in frozen_method.items()):
        raise AssertionError("frozen benchmark method metadata changed")
    if report.get("viewport") != {"width": 1280, "height": 900, "device_pixel_ratio": 1}:
        raise AssertionError("frozen viewport changed")
    if (
        report.get("fixture_manifest_sha256")
        != "dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350"
    ):
        raise AssertionError("fixture manifest changed")
    if (
        report.get("fixture_generator_sha256")
        != "3e0be8f90e6dc846803a28bb278b21f797ddc0576f5371149beb9ad185fb29c4"
    ):
        raise AssertionError("fixture generator changed")
    product_identity = (
        report.get("benchmark_script_sha256"),
        report.get("production_asset_manifest_sha256"),
    )
    if product_identity not in PRODUCT_IDENTITIES:
        raise AssertionError("benchmark script or production asset manifest changed")
    fixtures = report.get("fixtures")
    if (
        not isinstance(fixtures, list)
        or {item.get("name"): item.get("sha256") for item in fixtures if isinstance(item, dict)}
        != FIXTURE_DIGESTS
    ):
        raise AssertionError("fixture identity changed")
    loads = report.get("loads")
    statistics = report.get("load_statistics")
    interactions = report.get("interactions_ms")
    if not isinstance(loads, list) or len(loads) != 16 or not isinstance(statistics, list):
        raise AssertionError("required load observations changed")
    if not isinstance(interactions, list) or len(interactions) != 30:
        raise AssertionError("required interaction observations changed")
    names = [item.get("name") for item in loads if isinstance(item, dict)]
    if set(names) != LOAD_ROLES or any(names.count(name) != 2 for name in LOAD_ROLES):
        raise AssertionError("required load role omitted or substituted")
    by_name = {item.get("name"): item for item in statistics if isinstance(item, dict)}
    if set(by_name) != LOAD_ROLES:
        raise AssertionError("load statistics role omitted or substituted")
    for name in LOAD_ROLES:
        raw = [item["milliseconds"] for item in loads if item.get("name") == name]
        item = by_name[name]
        if item.get("iterations") != 2 or item.get("initial_ready_paint_ms") != raw:
            raise AssertionError("load raw timings changed")
        if item.get("median_ms") != nearest_rank(raw, 0.5) or item.get("p95_ms") != nearest_rank(
            raw, 0.95
        ):
            raise AssertionError("load statistics do not derive from raw timings")
    load_raw = [item["milliseconds"] for item in loads]
    if report.get("load_median_ms") != nearest_rank(load_raw, 0.5) or report.get(
        "load_p95_ms"
    ) != nearest_rank(load_raw, 0.95):
        raise AssertionError("aggregate load statistics do not derive from raw timings")
    if report.get("interaction_median_ms") != nearest_rank(interactions, 0.5) or report.get(
        "interaction_p95_ms"
    ) != nearest_rank(interactions, 0.95):
        raise AssertionError("interaction statistics do not derive from raw timings")
    measured = {"load": report["load_p95_ms"], "interaction": report["interaction_p95_ms"]}
    observations = report["bus_observations"]
    if not isinstance(observations, list):
        raise AssertionError("bus observations are missing")
    for item in observations:
        if not isinstance(item, dict):
            raise AssertionError("invalid bus observation")
        roles = item.get("roles")
        if not isinstance(roles, list) or len(roles) != 1:
            raise AssertionError("each bus group must have one frozen role")
        measured[f"{roles[0]}:{item.get('mode')}"] = item.get("p95_ms")
        raw = item.get("timings_ms")
        if not isinstance(raw, list) or len(raw) != 2:
            raise AssertionError("bus raw timings changed")
        if item.get("median_ms") != nearest_rank(raw, 0.5) or item.get("p95_ms") != nearest_rank(
            raw, 0.95
        ):
            raise AssertionError("bus statistics do not derive from raw timings")
        if (
            item.get("iterations") != 2
            or item.get("row_counts") != [item.get("rows")] * 2
            or not 0 < item.get("rows", 0) <= 100
        ):
            raise AssertionError("bus iteration or row bound changed")
    if set(measured) != set(TIMING_CEILINGS):
        raise AssertionError("required timing group omitted or substituted")
    for name, value in measured.items():
        if type(value) not in (int, float):
            raise AssertionError(f"{name} p95 is not numeric")
        absolute, regression = TIMING_CEILINGS[name]
        if value > absolute or value > regression:
            raise AssertionError(f"{name} exceeds approved ceiling")
    if max(item["commands"] for item in loads) > 46_129:
        raise AssertionError("Canvas command ceiling exceeded")
    if max(item["dom_nodes"] for item in loads) >= 1_000:
        raise AssertionError("DOM ceiling exceeded")
    if report.get("memory_reliable") is not False or report.get("used_js_heap_bytes") is not None:
        raise AssertionError("unapproved memory evidence")
    if (
        report.get("production_asset_manifest_sha256")
        == "c27b08c3fbbce7ead5e7afa4b92bffdaf9623f46f4319d92c78942ab2e59059d"
    ):
        if report.get("bounds") != {
            "waveform_request_max_span_samples": 393216,
            "waveform_pixel_width": 960,
            "canvas_command_formula": "channel_count * (pixel_width * 2 + 2) + 1",
            "canvas_command_ceiling": 46129,
            "dom_node_ceiling_exclusive": 1000,
        }:
            raise AssertionError("frozen request/Canvas/DOM bounds changed")
        if report.get("nondisclosure") != {
            "raw_port": False,
            "serial_number": False,
            "location": False,
            "token": False,
        }:
            raise AssertionError("nondisclosure evidence changed")


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) == 2 else Path("web/test-results/c2-b5-performance.json")
    validate(json.loads(path.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
