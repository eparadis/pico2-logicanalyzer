"""Independent static verification of the C3-B1 round-4 threshold proposal."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "testdata" / "decoders"
RAW = DATA / "cycle3-raw"
CURRENT = DATA / "cycle3/threshold-proposal-round-4.json"
PRIOR = DATA / "cycle3/threshold-proposal-round-3.json"
RATIONALE = ROOT / "docs/reviews/c3-b1-threshold-proposal-rationale-round-4.md"
SUBJECT_COMMIT = "b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0"
SUBJECT_TREE = "e8661f094ba0423ca08055ea785bbfcde8554d71"

EXPECTED_VALUES = {
    "input_samples": 65_536,
    "request_bytes": 4_194_304,
    "wall_deadline_ms": 5_000,
    "terminate_grace_ms": 250,
    "worker_address_space_bytes": 68_719_476_736,
    "worker_peak_rss_bytes": 134_217_728,
    "parent_retained_growth_bytes": 33_554_432,
    "recursion_limit": 320,
    "output_records": 16_384,
    "encoded_bytes": 2_097_152,
    "decoded_bytes": 2_097_152,
    "stdout_bytes": 65_536,
    "stderr_bytes": 65_536,
    "diagnostic_bytes": 8_192,
    "text_bytes": 524_288,
    "binary_bytes": 262_144,
    "nested_depth": 32,
    "nested_items": 16_384,
    "retained_result_bytes": 8_388_608,
    "successful_parent_total_ns": 1_300_000_000,
    "launch_ns": 50_000_000,
    "reap_ns": 50_000_000,
    "child_load_ns": 100_000_000,
    "child_import_ns": 100_000_000,
    "child_decode_ns": 100_000_000,
    "timeout_cleanup_total_ns": 5_500_000_000,
    "terminate_to_reap_ns": 300_000_000,
    "kill_to_reap_ns": 50_000_000,
    "spi_max_word_size_bits": 8,
}
EXPECTED_DERIVATIONS = {
    "input_samples": "next_power_of_two(raw_max * 128)",
    "request_bytes": "next_power_of_two(raw_max * 2048)",
    "wall_deadline_ms": (
        "unchanged experimentally enforced deadline; successful parent total rounded "
        "up from 156.549612 ms"
    ),
    "terminate_grace_ms": "unchanged experimentally enforced grace",
    "worker_address_space_bytes": ("unchanged verified macOS x86_64 RLIMIT_AS compatibility floor"),
    "worker_peak_rss_bytes": "next_power_of_two(raw_max * 4)",
    "parent_retained_growth_bytes": "next_power_of_two(raw_max * 16)",
    "recursion_limit": "unchanged experimentally enforced recursion limit",
    "output_records": "next_power_of_two(raw_max * 256)",
    "encoded_bytes": "next_power_of_two(raw_max * 256)",
    "decoded_bytes": "next_power_of_two(raw_max * 256)",
    "stdout_bytes": "64-KiB defensive floor for a channel required to remain empty on success",
    "stderr_bytes": "64-KiB defensive floor for a channel required to remain empty on success",
    "diagnostic_bytes": "next_power_of_two(raw_max * 32)",
    "text_bytes": "next_power_of_two(raw_max * 1024)",
    "binary_bytes": "raw_max * 65536",
    "nested_depth": "raw_max * 4",
    "nested_items": "next_power_of_two(raw_max * 32)",
    "retained_result_bytes": "next_power_of_two(raw_max * 256)",
    "successful_parent_total_ns": "ceil_to_100ms(raw_max * 8)",
    "launch_ns": "ceil_to_50ms(raw_max * 8)",
    "reap_ns": "50-ms scheduling floor above raw_max * 64",
    "child_load_ns": "100-ms scheduling floor above raw_max * 16",
    "child_import_ns": "ceil_to_50ms(raw_max * 8)",
    "child_decode_ns": "100-ms scheduling floor above raw_max * 32",
    "timeout_cleanup_total_ns": "wall deadline + grace + 250-ms cleanup allowance",
    "terminate_to_reap_ns": "250-ms grace + 50-ms cleanup allowance",
    "kill_to_reap_ns": "50-ms scheduling floor above raw_max * 16",
    "spi_max_word_size_bits": (
        "largest directly characterized and independently reproduced SPI word size"
    ),
}
EXPECTED_EVIDENCE = {
    "accepted_fixture_commit": "3af6b9f80dd52611e14acca407707d1da7b8d9ac",
    "accepted_runner_commit": "380d5dd77ae6c6f8648391e3c849c13c4b98fe8a",
    "runner_acceptance_commit": "01f059cb5f60e885c7d19e8bf5376bdb27dcca19",
    "raw_candidate_commit": "d0d9dbe87f7841f09f261556de0909475e048b95",
    "raw_verification_commit": "17397360770f3aab7d79a479a53499b50a1245cd",
    "raw_accumulated_commit": "7295e4d9472632f92bb22e6a06e001609b2590e6",
    "raw_acceptance_commit": "72168f4ca0f90e16e99a72537e159818a434dea1",
    "superseded_proposal_commit": "b260d9ecc0e74ed2502dda89beebb851ddfedb77",
    "superseded_operator_approval_commit": "63fdfee87159251cdf525eb608340e6bc08ad010",
    "environment_sha256": "d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f",
    "hostile_observations_sha256": (
        "af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91"
    ),
    "raw_manifest_sha256": "5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8",
    "observations_sha256": "ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee",
    "requests_sha256": "fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c",
    "experiment_caps_sha256": "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d",
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
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _ceil(value: int, quantum: int) -> int:
    return ((value + quantum - 1) // quantum) * quantum


def _power(value: int) -> int:
    return 1 << (value - 1).bit_length()


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
    return special.get(name, "nanoseconds" if name.endswith("_ns") else "bytes")


def _maxima() -> tuple[dict[str, int | None], int, int]:
    snapshots = _load(RAW / "observations.json")["observations"]
    hostile = _load(RAW / "hostile-observations.json")["observations"]
    rows = [row for case in snapshots for row in case["repetitions"]]
    hostile_rows = [row["observation"] for case in hostile for row in case["repetitions"]]
    maxima: dict[str, int | None] = {
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
    successful = max(row["parent_total_ns"] for row in rows)
    maxima.update(
        {
            "wall_deadline_ms": (successful + 999_999) // 1_000_000,
            "terminate_grace_ms": 250,
            "worker_address_space_bytes": None,
            "worker_peak_rss_bytes": max(row["diagnostics"]["maxrss"] for row in rows),
            "parent_retained_growth_bytes": max(
                row["parent_after"]["ru_maxrss"] - row["parent_before"]["ru_maxrss"] for row in rows
            ),
            "recursion_limit": 320,
            "successful_parent_total_ns": successful,
            "launch_ns": max(row["launch_ns"] for row in rows),
            "reap_ns": max(row["reap_ns"] for row in rows),
            "child_load_ns": max(row["diagnostics"]["load_ns"] for row in rows),
            "child_import_ns": max(row["diagnostics"]["import_ns"] for row in rows),
            "child_decode_ns": max(row["diagnostics"]["decode_ns"] for row in rows),
            "timeout_cleanup_total_ns": max(row["cleanup"]["total_ns"] for row in hostile_rows),
            "terminate_to_reap_ns": max(
                row["cleanup"]["terminate_to_reap_ns"] for row in hostile_rows
            ),
            "kill_to_reap_ns": max(row["cleanup"]["kill_to_reap_ns"] for row in hostile_rows),
            "spi_max_word_size_bits": 8,
        }
    )
    return maxima, len(rows), len(hostile_rows)


def _formula(raw: dict[str, int | None]) -> dict[str, int]:
    value = {name: number for name, number in raw.items() if number is not None}
    return {
        "input_samples": _power(value["input_samples"] * 128),
        "request_bytes": _power(value["request_bytes"] * 2_048),
        "wall_deadline_ms": 5_000,
        "terminate_grace_ms": 250,
        "worker_address_space_bytes": 68_719_476_736,
        "worker_peak_rss_bytes": _power(value["worker_peak_rss_bytes"] * 4),
        "parent_retained_growth_bytes": _power(value["parent_retained_growth_bytes"] * 16),
        "recursion_limit": 320,
        "output_records": _power(value["output_records"] * 256),
        "encoded_bytes": _power(value["encoded_bytes"] * 256),
        "decoded_bytes": _power(value["decoded_bytes"] * 256),
        "stdout_bytes": 65_536,
        "stderr_bytes": 65_536,
        "diagnostic_bytes": _power(value["diagnostic_bytes"] * 32),
        "text_bytes": _power(value["text_bytes"] * 1_024),
        "binary_bytes": value["binary_bytes"] * 65_536,
        "nested_depth": value["nested_depth"] * 4,
        "nested_items": _power(value["nested_items"] * 32),
        "retained_result_bytes": _power(value["retained_result_bytes"] * 256),
        "successful_parent_total_ns": _ceil(value["successful_parent_total_ns"] * 8, 100_000_000),
        "launch_ns": _ceil(value["launch_ns"] * 8, 50_000_000),
        "reap_ns": max(50_000_000, value["reap_ns"] * 64),
        "child_load_ns": max(100_000_000, value["child_load_ns"] * 16),
        "child_import_ns": _ceil(value["child_import_ns"] * 8, 50_000_000),
        "child_decode_ns": max(100_000_000, value["child_decode_ns"] * 32),
        "timeout_cleanup_total_ns": 5_500_000_000,
        "terminate_to_reap_ns": 300_000_000,
        "kill_to_reap_ns": max(50_000_000, value["kill_to_reap_ns"] * 16),
        "spi_max_word_size_bits": 8,
    }


def _feasible(values: dict[str, int], caps: dict[str, int]) -> None:
    if any(values[name] > caps[name] for name in HARD & set(caps)):
        raise ValueError("weakened cap")
    if values["successful_parent_total_ns"] > values["wall_deadline_ms"] * 1_000_000:
        raise ValueError("deadline")
    if (
        values["timeout_cleanup_total_ns"]
        > (values["wall_deadline_ms"] + values["terminate_grace_ms"] + 250) * 1_000_000
    ):
        raise ValueError("cleanup")
    if values["terminate_to_reap_ns"] > (values["terminate_grace_ms"] + 50) * 1_000_000:
        raise ValueError("terminate")
    if values["spi_max_word_size_bits"] != 8:
        raise ValueError("spi")


def _validate(proposal: object, prior: dict[str, Any] | None = None) -> None:
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
    if proposal["schema"] != "cycle3-threshold-proposal/v1" or proposal["round"] != 4:
        raise ValueError("schema")
    if proposal["status"] != "proposal-not-approved":
        raise ValueError("status")
    if (
        proposal["environment"]
        != {
            "os": "macOS 15.7.7 build 24G720",
            "architecture": "x86_64",
            "machine_model": "Macmini8,1",
            "python": "3.12.13",
        }
        or proposal["evidence"] != EXPECTED_EVIDENCE
    ):
        raise ValueError("evidence/environment")
    digest_paths = {
        "environment_sha256": RAW / "environment.json",
        "hostile_observations_sha256": RAW / "hostile-observations.json",
        "raw_manifest_sha256": RAW / "manifest.json",
        "observations_sha256": RAW / "observations.json",
        "requests_sha256": RAW / "requests.json",
        "experiment_caps_sha256": DATA / "cycle3/experiment-caps.json",
    }
    if any(proposal["evidence"][key] != _sha(path) for key, path in digest_paths.items()):
        raise ValueError("digest")
    limits = proposal["limits"]
    if not isinstance(limits, list) or len(limits) != 29:
        raise ValueError("count")
    ids = [item.get("id") for item in limits if isinstance(item, dict)]
    if len(ids) != 29 or len(set(ids)) != 29 or set(ids) != set(EXPECTED_VALUES):
        raise ValueError("ids")
    maxima, snapshot_rows, hostile_rows = _maxima()
    if (snapshot_rows, hostile_rows) != (315, 50) or _formula(maxima) != EXPECTED_VALUES:
        raise ValueError("formula calculation")
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
        if item["raw_max"] != maxima[name] or item["derivation"] != EXPECTED_DERIVATIONS[name]:
            raise ValueError("maximum/formula")
        expected_cap = 5_000_000_000 if name == "successful_parent_total_ns" else caps.get(name)
        if item["experiment_cap"] != expected_cap:
            raise ValueError("cap identity")
    values = {item["id"]: item["value"] for item in limits}
    _feasible(values, caps)
    previous = prior or _load(PRIOR)
    previous_values = {item["id"]: item["value"] for item in previous["limits"]}
    changed = {name for name in values if values[name] != previous_values.get(name)}
    if changed != {"parent_retained_growth_bytes", "successful_parent_total_ns", "launch_ns"}:
        raise ValueError("26/3 comparison")


def test_round4_identity_maxima_formula_comparison_rationale_and_authority() -> None:
    assert SUBJECT_COMMIT == "b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0"
    assert SUBJECT_TREE == "e8661f094ba0423ca08055ea785bbfcde8554d71"
    assert _sha(CURRENT) == "98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c"
    assert _sha(RATIONALE) == "58ef6451033603989617b195ab2d0184c75e243cbcad3ec99df3b2d41027242c"
    proposal = _load(CURRENT)
    assert CURRENT.read_text(encoding="utf-8") == json.dumps(proposal, separators=(",", ":")) + "\n"
    _validate(proposal)
    maxima, snapshot_rows, hostile_rows = _maxima()
    assert (snapshot_rows, hostile_rows, len(maxima)) == (315, 50, 29)
    assert maxima["parent_retained_growth_bytes"] == 1_757_184
    assert maxima["successful_parent_total_ns"] == 156_549_612
    assert maxima["launch_ns"] == 6_008_633
    assert _power(1_757_184 * 16) == 33_554_432
    assert _ceil(156_549_612 * 8, 100_000_000) == 1_300_000_000
    assert _ceil(6_008_633 * 8, 50_000_000) == 50_000_000
    rationale = RATIONALE.read_text(encoding="utf-8")
    assert "Exactly 26 of 29" in rationale
    assert "two increases and one decrease" in rationale
    assert "neither transfers authority" in rationale
    assert "No numeric value becomes authoritative" in rationale


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
        "cap_identity",
        "unit",
        "kind",
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
        "comparison",
    ],
)
def test_round4_non_vacuous_negative_mutation_matrix(mutation: str) -> None:
    value = copy.deepcopy(_load(CURRENT))
    prior = copy.deepcopy(_load(PRIOR))
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
        by_id["launch_ns"]["derivation"] = "raw_max * 8"
    elif mutation == "weaken":
        by_id["nested_depth"].update({"value": 41, "accept": 41, "reject": 42})
    elif mutation == "cap_identity":
        by_id["retained_result_bytes"]["experiment_cap"] += 1
    elif mutation == "unit":
        by_id["request_bytes"]["unit"] = "samples"
    elif mutation == "kind":
        by_id["request_bytes"]["kind"] = "regression-ceiling"
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
        value["evidence"]["superseded_operator_approval_commit"] = "0" * 40
    elif mutation == "environment":
        value["environment"]["architecture"] = "arm64"
    elif mutation == "comparison":
        next(item for item in prior["limits"] if item["id"] == "input_samples")["value"] -= 1
    with pytest.raises(ValueError):
        _validate(value, prior)


@pytest.mark.parametrize("mutation", ["weaken", "deadline", "cleanup", "terminate", "spi"])
def test_round4_cross_limit_mutations_reach_specific_guard(mutation: str) -> None:
    values = dict(EXPECTED_VALUES)
    caps = {
        item["id"]: item["value"] for item in _load(DATA / "cycle3/experiment-caps.json")["caps"]
    }
    if mutation == "weaken":
        values["nested_depth"] = caps["nested_depth"] + 1
    elif mutation == "deadline":
        values["successful_parent_total_ns"] = 5_000_000_001
    elif mutation == "cleanup":
        values["timeout_cleanup_total_ns"] = 5_500_000_001
    elif mutation == "terminate":
        values["terminate_to_reap_ns"] = 300_000_001
    elif mutation == "spi":
        values["spi_max_word_size_bits"] = 9
    with pytest.raises(ValueError, match=mutation if mutation != "weaken" else "weakened cap"):
        _feasible(values, caps)
