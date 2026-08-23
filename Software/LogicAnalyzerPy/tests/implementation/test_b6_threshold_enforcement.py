from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import pytest

from tools.check_b5_thresholds import TIMING_CEILINGS, validate

ROOT = Path(__file__).parents[2]
BASELINE = ROOT / "docs/performance/c2-b5-baseline-round-1.json"
B6_RUN = ROOT / "docs/performance/c2-b6-threshold-enforcement.json"


def test_approved_b5_thresholds_accept_frozen_baseline() -> None:
    validate(json.loads(BASELINE.read_text(encoding="utf-8")))


def test_b6_run_enforces_thresholds_and_freezes_current_product_identity() -> None:
    report = json.loads(B6_RUN.read_text(encoding="utf-8"))
    validate(report)
    assert report["production_asset_manifest_sha256"] == hashlib.sha256(
        (ROOT / "web/production-assets-b6.json").read_bytes()
    ).hexdigest()
    assert report["benchmark_script_sha256"] == hashlib.sha256(
        (ROOT / "web/tests/b6-performance.spec.ts").read_bytes()
    ).hexdigest()


@pytest.mark.parametrize("metric", sorted(TIMING_CEILINGS))
def test_each_approved_ceiling_is_independently_enforced(metric: str) -> None:
    report = json.loads(BASELINE.read_text(encoding="utf-8"))
    if metric == "load":
        report["load_p95_ms"] = TIMING_CEILINGS[metric][1] + 0.001
    elif metric == "interaction":
        report["interaction_p95_ms"] = TIMING_CEILINGS[metric][1] + 0.001
    else:
        role, mode = metric.split(":")
        item = next(
            item
            for item in report["bus_observations"]
            if item["roles"] == [role] and item["mode"] == mode
        )
        item["p95_ms"] = TIMING_CEILINGS[metric][1] + 0.001
    with pytest.raises(AssertionError, match="exceeds approved ceiling"):
        validate(copy.deepcopy(report))
