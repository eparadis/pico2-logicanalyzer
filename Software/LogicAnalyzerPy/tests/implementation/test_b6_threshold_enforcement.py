from __future__ import annotations

import copy
import hashlib
import json
import math
from collections.abc import Callable
from pathlib import Path
from typing import Any

import pytest

from tools.check_b5_thresholds import TIMING_CEILINGS, validate

ROOT = Path(__file__).parents[2]
BASELINE = ROOT / "docs/performance/c2-b5-baseline-round-1.json"
B6_RUN = ROOT / "docs/performance/c2-b6-threshold-enforcement.json"


def _rank(values: list[float], fraction: float) -> float:
    return sorted(values)[math.ceil(len(values) * fraction) - 1]


def test_approved_b5_thresholds_accept_frozen_baseline() -> None:
    validate(json.loads(BASELINE.read_text(encoding="utf-8")))


def test_b6_run_enforces_thresholds_and_freezes_current_product_identity() -> None:
    report = json.loads(B6_RUN.read_text(encoding="utf-8"))
    validate(report)
    assert (
        report["production_asset_manifest_sha256"]
        == hashlib.sha256((ROOT / "web/production-assets-b6.json").read_bytes()).hexdigest()
    )
    assert (
        report["benchmark_script_sha256"]
        == hashlib.sha256((ROOT / "web/tests/b6-performance.spec.ts").read_bytes()).hexdigest()
    )
    package = json.loads((ROOT / "web/package.json").read_text(encoding="utf-8"))
    assert package["scripts"]["benchmark:b6"].endswith(
        "&& python3 ../tools/check_b5_thresholds.py test-results/c2-b6-performance.json"
    )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda report: report["viewport"].update(width=1279), "viewport"),
        (lambda report: report["fixtures"][2].update(sha256="0" * 64), "fixture identity"),
        (lambda report: report["interactions_ms"].__setitem__(0, 999.0), "raw timings"),
        (lambda report: report["loads"][0].update(name="constant-8"), "load role"),
        (lambda report: report.update(production_asset_manifest_sha256="0" * 64), "manifest"),
    ],
)
def test_verifier_observed_evidence_mutations_are_rejected(
    mutation: Callable[[dict[str, Any]], None], message: str
) -> None:
    report = json.loads(B6_RUN.read_text(encoding="utf-8"))
    mutation(report)
    with pytest.raises(AssertionError, match=message):
        validate(report)


@pytest.mark.parametrize("metric", sorted(TIMING_CEILINGS))
def test_each_approved_ceiling_is_independently_enforced(metric: str) -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    if metric == "load":
        report["loads"][2]["milliseconds"] = TIMING_CEILINGS[metric][1] + 0.001
        name = report["loads"][2]["name"]
        raw = [item["milliseconds"] for item in report["loads"] if item["name"] == name]
        item = next(item for item in report["load_statistics"] if item["name"] == name)
        item.update(initial_ready_paint_ms=raw, median_ms=_rank(raw, 0.5), p95_ms=_rank(raw, 0.95))
        all_raw = [item["milliseconds"] for item in report["loads"]]
        report["load_median_ms"] = _rank(all_raw, 0.5)
        report["load_p95_ms"] = _rank(all_raw, 0.95)
    elif metric == "interaction":
        for index in range(3):
            report["interactions_ms"][index] = TIMING_CEILINGS[metric][1] + 0.001
        report["interaction_median_ms"] = _rank(report["interactions_ms"], 0.5)
        report["interaction_p95_ms"] = _rank(report["interactions_ms"], 0.95)
    else:
        role, mode = metric.split(":")
        item = next(
            item
            for item in report["bus_observations"]
            if item["roles"] == [role] and item["mode"] == mode
        )
        item["timings_ms"][0] = TIMING_CEILINGS[metric][1] + 0.001
        item["median_ms"] = _rank(item["timings_ms"], 0.5)
        item["p95_ms"] = _rank(item["timings_ms"], 0.95)
    with pytest.raises(AssertionError, match="exceeds approved ceiling"):
        validate(copy.deepcopy(report))
