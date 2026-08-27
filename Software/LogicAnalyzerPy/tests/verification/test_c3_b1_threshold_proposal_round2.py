"""Fresh static verification of the corrected C3-B1 threshold proposal."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "testdata/decoders"
RAW = DATA / "cycle3-raw"
CURRENT = DATA / "cycle3/threshold-proposal-round-2.json"
OLD = DATA / "cycle3/threshold-proposal-round-1.json"
RATIONALE = ROOT / "docs/reviews/c3-b1-threshold-proposal-rationale-round-2.md"

EXPECTED_VALUES = {
    "input_samples": 65536,
    "request_bytes": 4194304,
    "wall_deadline_ms": 5000,
    "terminate_grace_ms": 250,
    "worker_address_space_bytes": 68719476736,
    "worker_peak_rss_bytes": 134217728,
    "parent_retained_growth_bytes": 16777216,
    "recursion_limit": 320,
    "output_records": 16384,
    "encoded_bytes": 2097152,
    "decoded_bytes": 2097152,
    "stdout_bytes": 65536,
    "stderr_bytes": 65536,
    "diagnostic_bytes": 8192,
    "text_bytes": 524288,
    "binary_bytes": 262144,
    "nested_depth": 32,
    "nested_items": 16384,
    "retained_result_bytes": 8388608,
    "successful_parent_total_ns": 900000000,
    "launch_ns": 100000000,
    "reap_ns": 50000000,
    "child_load_ns": 100000000,
    "child_import_ns": 100000000,
    "child_decode_ns": 100000000,
    "timeout_cleanup_total_ns": 5500000000,
    "terminate_to_reap_ns": 300000000,
    "kill_to_reap_ns": 50000000,
    "spi_max_word_size_bits": 8,
}
HARD = {
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


def _load(path: Path) -> dict[str, Any]:
    result = json.loads(path.read_text())
    assert isinstance(result, dict)
    return result


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _ceil(value: int, quantum: int) -> int:
    return ((value + quantum - 1) // quantum) * quantum


def _unit(name: str) -> str:
    special = {
        "input_samples": "samples",
        "wall_deadline_ms": "milliseconds",
        "terminate_grace_ms": "milliseconds",
        "recursion_limit": "frames",
        "output_records": "records",
        "nested_depth": "levels",
        "nested_items": "items",
        "spi_max_word_size_bits": "bits",
    }
    if name in special:
        return special[name]
    if name.endswith("_ns"):
        return "nanoseconds"
    return "bytes"


def _maxima() -> dict[str, int | None]:
    snapshots = _load(RAW / "observations.json")["observations"]
    hostile = _load(RAW / "hostile-observations.json")["observations"]
    rows = [row for case in snapshots for row in case["repetitions"]]
    failed = [
        row["observation"]
        for case in hostile
        for row in case["repetitions"]
        if row["observation"].get("cleanup")
    ]
    result: dict[str, int | None] = {
        name: max(row["counts"][name] for row in rows)
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
    result.update(
        {
            "wall_deadline_ms": (max(row["parent_total_ns"] for row in rows) + 999999) // 1000000,
            "terminate_grace_ms": 250,
            "worker_address_space_bytes": None,
            "recursion_limit": 320,
            "worker_peak_rss_bytes": max(row["diagnostics"]["maxrss"] for row in rows),
            "parent_retained_growth_bytes": max(
                row["parent_after"]["ru_maxrss"] - row["parent_before"]["ru_maxrss"] for row in rows
            ),
            "successful_parent_total_ns": max(row["parent_total_ns"] for row in rows),
            "launch_ns": max(row["launch_ns"] for row in rows),
            "reap_ns": max(row["reap_ns"] for row in rows),
            "child_load_ns": max(row["diagnostics"]["load_ns"] for row in rows),
            "child_import_ns": max(row["diagnostics"]["import_ns"] for row in rows),
            "child_decode_ns": max(row["diagnostics"]["decode_ns"] for row in rows),
            "timeout_cleanup_total_ns": max(row["cleanup"]["total_ns"] for row in failed),
            "terminate_to_reap_ns": max(row["cleanup"]["terminate_to_reap_ns"] for row in failed),
            "kill_to_reap_ns": max(row["cleanup"]["kill_to_reap_ns"] for row in failed),
            "spi_max_word_size_bits": 8,
        }
    )
    return result


def _validate(proposal: object) -> None:
    if not isinstance(proposal, dict) or set(proposal) != {
        "schema",
        "round",
        "status",
        "environment",
        "evidence",
        "boundary_policy",
        "limits",
    }:
        raise ValueError("shape")
    if proposal["schema"] != "cycle3-threshold-proposal/v1" or proposal["round"] != 2:
        raise ValueError("schema")
    if proposal["status"] != "proposal-not-approved":
        raise ValueError("status")
    if proposal["environment"] != {
        "os": "macOS 15.7.7 build 24G720",
        "architecture": "x86_64",
        "machine_model": "Macmini8,1",
        "python": "3.12.13",
    }:
        raise ValueError("environment")
    evidence = proposal["evidence"]
    commits = {
        "accepted_fixture_commit": "7c57a347bbe575e3f451383ea498f56abc362f26",
        "corrected_runner_commit": "48d139f86aabcfa3e34567473c05ade13340107f",
        "raw_candidate_commit": "397981adf0f89115647203e749db1b1e5b3384cf",
        "raw_verification_commit": "9ac10d77cf1e8c492e7b5dae564baa43b09ebf71",
        "raw_accumulated_commit": "b49bd4932c4c091529b6c93f45de1f3f807e83f2",
        "raw_acceptance_commit": "7baa53bf8efe3de66722220ce20b0042f27f3cab",
        "proposal_assignment_commit": "b663d76b63626b1a64a99f4962dcf43a19e99b78",
        "superseded_proposal_assignment_commit": "29ac7847b3f4ce1ebd5fc33d4f627b5d838f6f6d",
        "superseded_proposal_commit": "e3a1d7c28a88a037e694d81c8c3406589fba040e",
        "failed_proposal_verification_assignment_commit": (
            "8762de1b46244369a0e4c062d22285eb44747413"
        ),
        "failed_proposal_verification_commit": "e47dc308ff3a7e22679d0bf1e9730f753eb29f47",
    }
    if any(evidence.get(key) != value for key, value in commits.items()):
        raise ValueError("commit")
    paths = {
        "environment_sha256": RAW / "environment.json",
        "hostile_observations_sha256": RAW / "hostile-observations.json",
        "raw_manifest_sha256": RAW / "manifest.json",
        "observations_sha256": RAW / "observations.json",
        "requests_sha256": RAW / "requests.json",
        "experiment_caps_sha256": DATA / "cycle3/experiment-caps.json",
    }
    if any(evidence.get(key) != _sha(path) for key, path in paths.items()):
        raise ValueError("digest")
    limits = proposal["limits"]
    if not isinstance(limits, list) or len(limits) != 29:
        raise ValueError("count")
    ids = [item.get("id") for item in limits if isinstance(item, dict)]
    if set(ids) != set(EXPECTED_VALUES) or len(ids) != len(set(ids)):
        raise ValueError("ids")
    maxima = _maxima()
    caps = {
        item["id"]: item["value"] for item in _load(DATA / "cycle3/experiment-caps.json")["caps"]
    }
    for item in limits:
        name = item["id"]
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
            raise ValueError("entry")
        if item["kind"] != ("hard-enforcement" if name in HARD else "regression-ceiling"):
            raise ValueError("kind")
        if item["unit"] != _unit(name):
            raise ValueError("unit")
        if any(
            type(item[field]) is not int or item[field] <= 0
            for field in ("value", "accept", "reject")
        ):
            raise ValueError("type")
        if (
            item["value"] != EXPECTED_VALUES[name]
            or item["accept"] != item["value"]
            or item["reject"] != item["value"] + 1
        ):
            raise ValueError("boundary")
        if item["raw_max"] != maxima[name]:
            raise ValueError("maximum")
        expected_cap = 5_000_000_000 if name == "successful_parent_total_ns" else caps.get(name)
        if item["experiment_cap"] != expected_cap:
            raise ValueError("cap identity")
        if expected_cap is not None and item["value"] > expected_cap:
            raise ValueError("weakened")
    by_id = {item["id"]: item["value"] for item in limits}
    if by_id["successful_parent_total_ns"] > by_id["wall_deadline_ms"] * 1_000_000:
        raise ValueError("deadline")
    if (
        by_id["timeout_cleanup_total_ns"]
        > (by_id["wall_deadline_ms"] + by_id["terminate_grace_ms"] + 250) * 1_000_000
    ):
        raise ValueError("cleanup")
    if by_id["terminate_to_reap_ns"] > (by_id["terminate_grace_ms"] + 50) * 1_000_000:
        raise ValueError("terminate")
    if by_id["spi_max_word_size_bits"] > 8:
        raise ValueError("spi")


def test_round2_identity_formula_scope_provenance_and_rationale() -> None:
    assert _sha(CURRENT) == "94882b710f2d569c0ea0535366a0c1c3df3514aa20a18e4cd35f652177458ec2"
    assert _sha(RATIONALE) == "18a6b58a2b05f7dd7aa302a6e1bb4d074621440648a2e735a1d16d9708b209b0"
    proposal = _load(CURRENT)
    _validate(proposal)
    assert 105815301 * 8 == 846522408
    assert _ceil(105815301 * 8, 100000000) == 900000000
    current = copy.deepcopy(proposal)
    old = copy.deepcopy(_load(OLD))
    current["round"] = old["round"]
    current["evidence"] = old["evidence"]
    corrected = next(x for x in current["limits"] if x["id"] == "successful_parent_total_ns")
    prior = next(x for x in old["limits"] if x["id"] == "successful_parent_total_ns")
    corrected.update({key: prior[key] for key in ("value", "accept", "reject", "rationale")})
    assert current == old
    rationale = RATIONALE.read_text()
    successful = next(x for x in proposal["limits"] if x["id"] == "successful_parent_total_ns")
    assert "8.51 times" in successful["rationale"]
    assert "900 ms" in rationale
    assert "not approved limits" in rationale
    assert "No value is operator-approved" in rationale


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "duplicate",
        "bool",
        "float",
        "zero",
        "negative",
        "maximum",
        "formula",
        "weaken",
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
def test_round2_negative_mutation_matrix(mutation: str) -> None:
    value = copy.deepcopy(_load(CURRENT))
    by_id = {item["id"]: item for item in value["limits"]}
    if mutation == "missing":
        value["limits"].pop()
    elif mutation == "extra":
        value["limits"].append({"id": "extra"})
    elif mutation == "duplicate":
        value["limits"][-1] = copy.deepcopy(value["limits"][0])
    elif mutation in {"bool", "float", "zero", "negative"}:
        by_id["input_samples"]["value"] = {"bool": True, "float": 1.5, "zero": 0, "negative": -1}[
            mutation
        ]
    elif mutation == "maximum":
        by_id["output_records"]["raw_max"] += 1
    elif mutation == "formula":
        by_id["successful_parent_total_ns"].update(
            {"value": 1_000_000_000, "accept": 1_000_000_000, "reject": 1_000_000_001}
        )
    elif mutation == "weaken":
        by_id["nested_depth"].update({"value": 41, "accept": 41, "reject": 42})
    elif mutation == "unit":
        by_id["request_bytes"]["unit"] = "samples"
    elif mutation == "accept":
        by_id["text_bytes"]["accept"] -= 1
    elif mutation == "reject":
        by_id["text_bytes"]["reject"] += 1
    elif mutation == "deadline":
        by_id["successful_parent_total_ns"].update(
            {"value": 6_000_000_000, "accept": 6_000_000_000, "reject": 6_000_000_001}
        )
    elif mutation == "cleanup":
        by_id["timeout_cleanup_total_ns"].update(
            {"value": 5_500_000_001, "accept": 5_500_000_001, "reject": 5_500_000_002}
        )
    elif mutation == "terminate":
        by_id["terminate_to_reap_ns"].update(
            {"value": 300_000_001, "accept": 300_000_001, "reject": 300_000_002}
        )
    elif mutation == "spi":
        by_id["spi_max_word_size_bits"].update({"value": 9, "accept": 9, "reject": 10})
    elif mutation == "approved":
        value["status"] = "approved"
    elif mutation == "digest":
        value["evidence"]["requests_sha256"] = "0" * 64
    elif mutation == "commit":
        value["evidence"]["superseded_proposal_commit"] = "0" * 40
    elif mutation == "environment":
        value["environment"]["architecture"] = "arm64"
    with pytest.raises(ValueError):
        _validate(value)
