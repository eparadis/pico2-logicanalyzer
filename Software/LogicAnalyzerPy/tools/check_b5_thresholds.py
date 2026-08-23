#!/usr/bin/env python3
"""Enforce the immutable operator-approved B5 ceilings without rebasing."""

from __future__ import annotations

import json
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


def validate(report: dict[str, object]) -> None:
    if report.get("method") != "c2-b5-playwright-production-v2":
        raise AssertionError("frozen benchmark method changed")
    measured = {
        "load": report["load_p95_ms"],
        "interaction": report["interaction_p95_ms"],
    }
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
        if item.get("iterations") != 2 or not 0 < item.get("rows", 0) <= 100:
            raise AssertionError("bus iteration or row bound changed")
    if set(measured) != set(TIMING_CEILINGS):
        raise AssertionError("required timing group omitted or substituted")
    for name, value in measured.items():
        if type(value) not in (int, float):
            raise AssertionError(f"{name} p95 is not numeric")
        absolute, regression = TIMING_CEILINGS[name]
        if value > absolute or value > regression:
            raise AssertionError(f"{name} exceeds approved ceiling")
    loads = report.get("loads")
    if not isinstance(loads, list) or len(loads) != 16:
        raise AssertionError("required load observations changed")
    if max(item["commands"] for item in loads) > 46_129:
        raise AssertionError("Canvas command ceiling exceeded")
    if max(item["dom_nodes"] for item in loads) >= 1_000:
        raise AssertionError("DOM ceiling exceeded")
    if report.get("memory_reliable") is not False or report.get("used_js_heap_bytes") is not None:
        raise AssertionError("unapproved memory evidence")


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) == 2 else Path("web/test-results/c2-b5-performance.json")
    validate(json.loads(path.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
