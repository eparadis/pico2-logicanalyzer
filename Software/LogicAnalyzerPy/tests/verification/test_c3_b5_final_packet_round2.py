"""Independent C3-B5 round-2 checks for the corrected final packet."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "tests/implementation/test_c3_b5_final_packet.py"
RAW = ROOT / "testdata/decoders/cycle3-raw/b5-final-measurements.json"
DATA = ROOT / "testdata/decoders/cycle3"
EXPECTED_IMPLEMENTATION_SHA256 = (
    "8914ca125aa2ed132f7eabdff8d148045132bce447222d75ac9860b0175689f6"
)
EXPECTED_RAW_SHA256 = "980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e"
EXPECTED_PROPOSAL_SHA256 = (
    "98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c"
)
REGRESSION_IDS = {
    "worker_peak_rss_bytes",
    "parent_retained_growth_bytes",
    "successful_parent_total_ns",
    "launch_ns",
    "reap_ns",
    "child_load_ns",
    "child_import_ns",
    "child_decode_ns",
    "timeout_cleanup_total_ns",
    "terminate_to_reap_ns",
    "kill_to_reap_ns",
}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_corrected_collector_has_one_warmup_loop_and_one_five_repetition_loop() -> None:
    """Guard C3B5-V001 without trusting the implementor's runtime assertions."""
    assert _sha(IMPLEMENTATION) == EXPECTED_IMPLEMENTATION_SHA256
    tree = ast.parse(IMPLEMENTATION.read_text(encoding="utf-8"))
    measure = next(
        node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "_measure"
    )
    loops = [node for node in measure.body if isinstance(node, ast.For)]
    assert len(loops) == 2
    warmup, retained = loops
    assert ast.unparse(warmup.iter) == "selected"
    assert len(warmup.body) == 1 and ast.unparse(warmup.body[0]) == "observe(timeline)"
    assert ast.unparse(retained.iter) == "range(5)"
    nested = retained.body[0]
    assert isinstance(nested, ast.For) and ast.unparse(nested.iter) == "selected"
    assert "row = observe(timeline)" in ast.unparse(nested)
    assertions = [ast.unparse(node.test) for node in measure.body if isinstance(node, ast.Assert)]
    assert "launches == 18 and len(repetitions) == 15" in assertions


def test_final_measurement_packet_is_complete_bound_and_below_every_ceiling() -> None:
    assert _sha(RAW) == EXPECTED_RAW_SHA256
    proposal_path = DATA / "threshold-proposal-round-4.json"
    assert _sha(proposal_path) == EXPECTED_PROPOSAL_SHA256
    proposal = _load(proposal_path)
    result = _load(RAW)
    limits = {item["id"]: item["value"] for item in proposal["limits"]}

    assert result["launches"] == {"warmup": 3, "retained": 15, "total": 18}
    assert result["environment"] == {
        "system": "Darwin",
        "machine": "x86_64",
        "python": "3.12.13",
    }
    assert result["proposal_commit"] == "b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0"
    assert result["proposal_sha256"] == EXPECTED_PROPOSAL_SHA256
    assert len([item for item in proposal["limits"] if item["kind"] == "hard-enforcement"]) == 18
    assert limits["spi_max_word_size_bits"] == 8

    rows = result["rows"]
    assert len(rows) == 15
    assert {(row["decoder"], row["repetition"]) for row in rows} == {
        (decoder, repetition)
        for decoder in ("uart", "spi", "i2c")
        for repetition in range(5)
    }
    for row in rows:
        assert set(row) == REGRESSION_IDS | {"decoder", "repetition"}
        for metric in REGRESSION_IDS:
            assert type(row[metric]) is int
            assert 0 <= row[metric] <= limits[metric]
