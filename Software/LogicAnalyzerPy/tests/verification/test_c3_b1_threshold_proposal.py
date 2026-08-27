"""Independent static verification of the C3-B1 threshold proposal."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
DATA = ROOT / "testdata/decoders"
RAW = DATA / "cycle3-raw"
PROPOSAL_PATH = DATA / "cycle3/threshold-proposal-round-1.json"
RATIONALE_PATH = ROOT / "docs/reviews/c3-b1-threshold-proposal-rationale-round-1.md"

HARD_IDS = {
    "input_samples",
    "request_bytes",
    "wall_deadline_ms",
    "terminate_grace_ms",
    "worker_address_space_bytes",
    "recursion_limit",
    "output_records",
    "encoded_bytes",
    "decoded_bytes",
    "stdout_bytes",
    "stderr_bytes",
    "diagnostic_bytes",
    "text_bytes",
    "binary_bytes",
    "nested_depth",
    "nested_items",
    "retained_result_bytes",
    "spi_max_word_size_bits",
}
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
UNITS = {
    **{
        name: "bytes"
        for name in (
            "request_bytes",
            "worker_address_space_bytes",
            "worker_peak_rss_bytes",
            "parent_retained_growth_bytes",
            "encoded_bytes",
            "decoded_bytes",
            "stdout_bytes",
            "stderr_bytes",
            "diagnostic_bytes",
            "text_bytes",
            "binary_bytes",
            "retained_result_bytes",
        )
    },
    **{
        name: "nanoseconds"
        for name in REGRESSION_IDS - {"worker_peak_rss_bytes", "parent_retained_growth_bytes"}
    },
    "input_samples": "samples",
    "wall_deadline_ms": "milliseconds",
    "terminate_grace_ms": "milliseconds",
    "recursion_limit": "frames",
    "output_records": "records",
    "nested_depth": "levels",
    "nested_items": "items",
    "spi_max_word_size_bits": "bits",
}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text())
    assert isinstance(value, dict)
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _next_power_of_two(value: int) -> int:
    return 1 << (value - 1).bit_length()


def _ceil(value: int, quantum: int) -> int:
    return ((value + quantum - 1) // quantum) * quantum


def _raw_maxima() -> dict[str, int | None]:
    observations = _load(RAW / "observations.json")["observations"]
    hostile = _load(RAW / "hostile-observations.json")["observations"]
    rows = [rep for case in observations for rep in case["repetitions"]]
    failures = [rep["observation"] for case in hostile for rep in case["repetitions"]]
    maxima: dict[str, int | None] = {
        name: max(rep["counts"][name] for rep in rows)
        for name in (
            "input_samples",
            "request_bytes",
            "output_records",
            "encoded_bytes",
            "decoded_bytes",
            "stdout_bytes",
            "stderr_bytes",
            "diagnostic_bytes",
            "text_bytes",
            "binary_bytes",
            "nested_depth",
            "nested_items",
            "retained_result_bytes",
        )
    }
    maxima.update(
        {
            "successful_parent_total_ns": max(rep["parent_total_ns"] for rep in rows),
            "launch_ns": max(rep["launch_ns"] for rep in rows),
            "reap_ns": max(rep["reap_ns"] for rep in rows),
            "child_load_ns": max(rep["diagnostics"]["load_ns"] for rep in rows),
            "child_import_ns": max(rep["diagnostics"]["import_ns"] for rep in rows),
            "child_decode_ns": max(rep["diagnostics"]["decode_ns"] for rep in rows),
            "worker_peak_rss_bytes": max(rep["diagnostics"]["maxrss"] for rep in rows),
            "parent_retained_growth_bytes": max(
                rep["parent_after"]["ru_maxrss"] - rep["parent_before"]["ru_maxrss"] for rep in rows
            ),
            "timeout_cleanup_total_ns": max(
                rep["cleanup"]["total_ns"] for rep in failures if rep.get("cleanup")
            ),
            "terminate_to_reap_ns": max(
                rep["cleanup"]["terminate_to_reap_ns"] for rep in failures if rep.get("cleanup")
            ),
            "kill_to_reap_ns": max(
                rep["cleanup"]["kill_to_reap_ns"] for rep in failures if rep.get("cleanup")
            ),
            "wall_deadline_ms": (max(rep["parent_total_ns"] for rep in rows) + 1_000_000 - 1)
            // 1_000_000,
            "terminate_grace_ms": 250,
            "worker_address_space_bytes": None,
            "recursion_limit": 320,
            "spi_max_word_size_bits": 8,
        }
    )
    return maxima


def _expected_values(raw: dict[str, int | None]) -> dict[str, int]:
    integer = {key: value for key, value in raw.items() if value is not None}
    return {
        "input_samples": _next_power_of_two(integer["input_samples"] * 128),
        "request_bytes": _next_power_of_two(integer["request_bytes"] * 2048),
        "wall_deadline_ms": 5000,
        "terminate_grace_ms": 250,
        "worker_address_space_bytes": 64 * 1024**3,
        "worker_peak_rss_bytes": _next_power_of_two(integer["worker_peak_rss_bytes"] * 4),
        "parent_retained_growth_bytes": _next_power_of_two(
            integer["parent_retained_growth_bytes"] * 16
        ),
        "recursion_limit": 320,
        "output_records": _next_power_of_two(integer["output_records"] * 256),
        "encoded_bytes": _next_power_of_two(integer["encoded_bytes"] * 256),
        "decoded_bytes": _next_power_of_two(integer["decoded_bytes"] * 256),
        "stdout_bytes": 64 * 1024,
        "stderr_bytes": 64 * 1024,
        "diagnostic_bytes": _next_power_of_two(integer["diagnostic_bytes"] * 32),
        "text_bytes": _next_power_of_two(integer["text_bytes"] * 1024),
        "binary_bytes": integer["binary_bytes"] * 65536,
        "nested_depth": integer["nested_depth"] * 4,
        "nested_items": _next_power_of_two(integer["nested_items"] * 32),
        "retained_result_bytes": _next_power_of_two(integer["retained_result_bytes"] * 256),
        "successful_parent_total_ns": _ceil(integer["successful_parent_total_ns"] * 8, 100_000_000),
        "launch_ns": _ceil(integer["launch_ns"] * 8, 50_000_000),
        "reap_ns": max(50_000_000, integer["reap_ns"] * 64),
        "child_load_ns": max(100_000_000, integer["child_load_ns"] * 16),
        "child_import_ns": _ceil(integer["child_import_ns"] * 8, 50_000_000),
        "child_decode_ns": max(100_000_000, integer["child_decode_ns"] * 32),
        "timeout_cleanup_total_ns": 5_000_000_000 + 250_000_000 + 250_000_000,
        "terminate_to_reap_ns": 250_000_000 + 50_000_000,
        "kill_to_reap_ns": max(50_000_000, integer["kill_to_reap_ns"] * 16),
        "spi_max_word_size_bits": 8,
    }


def _validate(value: object) -> None:
    if not isinstance(value, dict) or set(value) != {
        "schema",
        "round",
        "status",
        "environment",
        "evidence",
        "boundary_policy",
        "limits",
    }:
        raise ValueError("proposal shape")
    if value["schema"] != "cycle3-threshold-proposal/v1" or value["round"] != 1:
        raise ValueError("schema")
    if value["status"] != "proposal-not-approved":
        raise ValueError("approval status")
    if value["environment"] != {
        "os": "macOS 15.7.7 build 24G720",
        "architecture": "x86_64",
        "machine_model": "Macmini8,1",
        "python": "3.12.13",
    }:
        raise ValueError("environment")
    evidence = value["evidence"]
    fixed_evidence = {
        "accepted_fixture_commit": "7c57a347bbe575e3f451383ea498f56abc362f26",
        "corrected_runner_commit": "48d139f86aabcfa3e34567473c05ade13340107f",
        "raw_candidate_commit": "397981adf0f89115647203e749db1b1e5b3384cf",
        "raw_verification_commit": "9ac10d77cf1e8c492e7b5dae564baa43b09ebf71",
        "raw_accumulated_commit": "b49bd4932c4c091529b6c93f45de1f3f807e83f2",
        "raw_acceptance_commit": "7baa53bf8efe3de66722220ce20b0042f27f3cab",
        "proposal_assignment_commit": "29ac7847b3f4ce1ebd5fc33d4f627b5d838f6f6d",
    }
    if any(evidence.get(name) != expected for name, expected in fixed_evidence.items()):
        raise ValueError("evidence commit")
    digest_paths = {
        "environment_sha256": RAW / "environment.json",
        "hostile_observations_sha256": RAW / "hostile-observations.json",
        "raw_manifest_sha256": RAW / "manifest.json",
        "observations_sha256": RAW / "observations.json",
        "requests_sha256": RAW / "requests.json",
        "experiment_caps_sha256": DATA / "cycle3/experiment-caps.json",
    }
    if any(evidence.get(name) != _sha(path) for name, path in digest_paths.items()):
        raise ValueError("evidence digest")
    limits = value["limits"]
    if not isinstance(limits, list) or len(limits) != 29:
        raise ValueError("limit count")
    ids = [item.get("id") for item in limits if isinstance(item, dict)]
    if len(ids) != 29 or set(ids) != HARD_IDS | REGRESSION_IDS or len(ids) != len(set(ids)):
        raise ValueError("closed ids")
    raw = _raw_maxima()
    expected = _expected_values(raw)
    caps = _load(DATA / "cycle3/experiment-caps.json")
    cap_values = {item["id"]: item["value"] for item in caps["caps"]}
    for item in limits:
        if set(item) != {
            "id",
            "kind",
            "unit",
            "value",
            "accept",
            "reject",
            "raw_max",
            "experiment_cap",
            "derivation",
            "rationale",
        }:
            raise ValueError("limit shape")
        name = item["id"]
        if item["kind"] != ("hard-enforcement" if name in HARD_IDS else "regression-ceiling"):
            raise ValueError("kind")
        if item["unit"] != UNITS[name]:
            raise ValueError("unit")
        if any(
            type(item[field]) is not int or item[field] <= 0
            for field in ("value", "accept", "reject")
        ):
            raise ValueError("integer boundary")
        if (
            item["value"] != expected[name]
            or item["accept"] != item["value"]
            or item["reject"] != item["value"] + 1
        ):
            raise ValueError("formula boundary")
        if item["raw_max"] != raw[name]:
            raise ValueError("raw maximum")
        expected_cap = (
            5_000_000_000 if name == "successful_parent_total_ns" else cap_values.get(name)
        )
        if item["experiment_cap"] != expected_cap:
            raise ValueError("experiment cap")
        if expected_cap is not None and item["value"] > expected_cap:
            raise ValueError("weakened cap")
        if not isinstance(item["derivation"], str) or not item["derivation"]:
            raise ValueError("derivation")
    by_id = {item["id"]: item["value"] for item in limits}
    if by_id["successful_parent_total_ns"] > by_id["wall_deadline_ms"] * 1_000_000:
        raise ValueError("deadline contradiction")
    if (
        by_id["timeout_cleanup_total_ns"]
        > (by_id["wall_deadline_ms"] + by_id["terminate_grace_ms"] + 250) * 1_000_000
    ):
        raise ValueError("cleanup contradiction")
    if by_id["terminate_to_reap_ns"] > (by_id["terminate_grace_ms"] + 50) * 1_000_000:
        raise ValueError("grace contradiction")
    if by_id["spi_max_word_size_bits"] > 8:
        raise ValueError("SPI evidence")


def test_exact_candidate_hashes_evidence_environment_formulas_and_feasibility() -> None:
    assert _sha(PROPOSAL_PATH) == "61d1273114d98bf6652b5401bf146e8d44fd6a51242c317a502719dfb036e080"
    assert (
        _sha(RATIONALE_PATH) == "112d5606b7912cce2e99bc16189d1783829eb79733b72d1d469d0beab1ca42b0"
    )
    proposal = _load(PROPOSAL_PATH)
    _validate(proposal)
    assert proposal["environment"] == {
        "os": "macOS 15.7.7 build 24G720",
        "architecture": "x86_64",
        "machine_model": "Macmini8,1",
        "python": "3.12.13",
    }
    evidence = proposal["evidence"]
    expected_digests = {
        "environment_sha256": "environment.json",
        "hostile_observations_sha256": "hostile-observations.json",
        "raw_manifest_sha256": "manifest.json",
        "observations_sha256": "observations.json",
        "requests_sha256": "requests.json",
        "experiment_caps_sha256": "../cycle3/experiment-caps.json",
    }
    for field, relative in expected_digests.items():
        assert evidence[field] == _sha(RAW / relative)
    values = {item["id"]: item["value"] for item in proposal["limits"]}
    assert values["request_bytes"] > values["input_samples"] * 8
    assert values["retained_result_bytes"] <= values["worker_peak_rss_bytes"]
    assert values["worker_peak_rss_bytes"] < values["worker_address_space_bytes"]
    rationale = RATIONALE_PATH.read_text()
    assert "proposal, not approved limits" in rationale
    assert "No value is operator-approved" in rationale


def _formula_correct_baseline() -> dict[str, Any]:
    proposal = copy.deepcopy(_load(PROPOSAL_PATH))
    item = next(item for item in proposal["limits"] if item["id"] == "successful_parent_total_ns")
    item.update({"value": 900_000_000, "accept": 900_000_000, "reject": 900_000_001})
    _validate(proposal)
    return proposal


def _mutate(name: str, replacement: Any) -> dict[str, Any]:
    proposal = _formula_correct_baseline()
    item = next(item for item in proposal["limits"] if item["id"] == name)
    item.update(replacement)
    return proposal


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "duplicate",
        "boolean",
        "float",
        "zero",
        "negative",
        "raw_max",
        "formula",
        "weakened_cap",
        "unit",
        "accept",
        "reject",
        "deadline",
        "cleanup",
        "terminate",
        "spi",
        "approved",
        "digest",
        "commit",
        "environment",
    ],
)
def test_complete_negative_mutation_matrix(mutation: str) -> None:
    proposal = _formula_correct_baseline()
    if mutation == "missing":
        proposal["limits"].pop()
    elif mutation == "extra":
        proposal["limits"].append({"id": "extra"})
    elif mutation == "duplicate":
        proposal["limits"][-1] = copy.deepcopy(proposal["limits"][0])
    elif mutation in {"boolean", "float", "zero", "negative"}:
        proposal = _mutate(
            "input_samples",
            {"value": {"boolean": True, "float": 1.5, "zero": 0, "negative": -1}[mutation]},
        )
    elif mutation == "raw_max":
        proposal = _mutate("output_records", {"raw_max": 35})
    elif mutation == "formula":
        proposal = _mutate("nested_items", {"value": 8192, "accept": 8192, "reject": 8193})
    elif mutation == "weakened_cap":
        proposal = _mutate("nested_depth", {"value": 41, "accept": 41, "reject": 42})
    elif mutation == "unit":
        proposal = _mutate("request_bytes", {"unit": "samples"})
    elif mutation == "accept":
        proposal = _mutate("text_bytes", {"accept": 524287})
    elif mutation == "reject":
        proposal = _mutate("text_bytes", {"reject": 524290})
    elif mutation == "deadline":
        proposal = _mutate(
            "successful_parent_total_ns",
            {"value": 6_000_000_000, "accept": 6_000_000_000, "reject": 6_000_000_001},
        )
    elif mutation == "cleanup":
        proposal = _mutate(
            "timeout_cleanup_total_ns",
            {"value": 5_500_000_001, "accept": 5_500_000_001, "reject": 5_500_000_002},
        )
    elif mutation == "terminate":
        proposal = _mutate(
            "terminate_to_reap_ns",
            {"value": 300_000_001, "accept": 300_000_001, "reject": 300_000_002},
        )
    elif mutation == "spi":
        proposal = _mutate("spi_max_word_size_bits", {"value": 9, "accept": 9, "reject": 10})
    elif mutation == "approved":
        proposal["status"] = "approved"
    elif mutation == "digest":
        proposal["evidence"]["requests_sha256"] = "0" * 64
    elif mutation == "commit":
        proposal["evidence"]["raw_candidate_commit"] = "0" * 40
    elif mutation == "environment":
        proposal["environment"]["architecture"] = "arm64"
    with pytest.raises(ValueError):
        _validate(proposal)
