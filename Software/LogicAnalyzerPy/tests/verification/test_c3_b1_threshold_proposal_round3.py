"""Independent static verification of the C3-B1 round-3 threshold proposal."""

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
CURRENT = DATA / "cycle3/threshold-proposal-round-3.json"
PRIOR = DATA / "cycle3/threshold-proposal-round-2.json"
RATIONALE = ROOT / "docs/reviews/c3-b1-threshold-proposal-rationale-round-3.md"
SUBJECT_COMMIT = "b260d9ecc0e74ed2502dda89beebb851ddfedb77"
SUBJECT_TREE = "8a65628df5ba63727e8305e901b9954fe0bec7e5"

EXPECTED_VALUES = {
    "input_samples": 65_536,
    "request_bytes": 4_194_304,
    "wall_deadline_ms": 5_000,
    "terminate_grace_ms": 250,
    "worker_address_space_bytes": 68_719_476_736,
    "worker_peak_rss_bytes": 134_217_728,
    "parent_retained_growth_bytes": 16_777_216,
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
    "successful_parent_total_ns": 1_000_000_000,
    "launch_ns": 100_000_000,
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
        "up from 123.103531 ms"
    ),
    "terminate_grace_ms": "unchanged experimentally enforced grace",
    "worker_address_space_bytes": (
        "unchanged verified macOS x86_64 RLIMIT_AS compatibility floor"
    ),
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
HARD = {
    "input_samples", "request_bytes", "wall_deadline_ms", "terminate_grace_ms",
    "worker_address_space_bytes", "recursion_limit", "output_records",
    "encoded_bytes", "decoded_bytes", "stdout_bytes", "stderr_bytes",
    "diagnostic_bytes", "text_bytes", "binary_bytes", "nested_depth",
    "nested_items", "retained_result_bytes", "spi_max_word_size_bits",
}
EXPECTED_EVIDENCE = {
    "accepted_fixture_commit": "a98d328aab92f3dad66988fb70cc567946dc89d0",
    "accepted_runner_commit": "ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a",
    "runner_acceptance_commit": "bf1fc5eaa232bf09e66df77bd1c4be3e1ae4ffbd",
    "raw_candidate_commit": "2ae1e4335c38a5cf717491c7936f857292f71498",
    "raw_verification_commit": "10a6a1f72fc4973c112bd1da0877ffdc2590f3f8",
    "raw_accumulated_commit": "68242a9b2a173432ad465b514dac9369821c3723",
    "raw_acceptance_commit": "115e2d022f26dbd211616dea05ed91bdb1a2cb62",
    "superseded_proposal_commit": "395646fa1172382928581d7266723f5b044cf8f2",
    "superseded_operator_approval_commit": "b6d904064ab7b9e195eedded1c55efc306eeb925",
    "environment_sha256": "fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34",
    "hostile_observations_sha256": (
        "d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080"
    ),
    "raw_manifest_sha256": "7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e",
    "observations_sha256": "28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd",
    "requests_sha256": "fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c",
    "experiment_caps_sha256": (
        "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d"
    ),
}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _ceil(value: int, quantum: int) -> int:
    return ((value + quantum - 1) // quantum) * quantum


def _next_power_of_two(value: int) -> int:
    return 1 << (value - 1).bit_length()


def _unit(name: str) -> str:
    special = {
        "input_samples": "samples", "wall_deadline_ms": "milliseconds",
        "terminate_grace_ms": "milliseconds", "recursion_limit": "frames",
        "output_records": "records", "nested_depth": "levels",
        "nested_items": "items", "spi_max_word_size_bits": "bits",
    }
    if name in special:
        return special[name]
    return "nanoseconds" if name.endswith("_ns") else "bytes"


def _maxima() -> dict[str, int | None]:
    snapshots = _load(RAW / "observations.json")["observations"]
    hostile = _load(RAW / "hostile-observations.json")["observations"]
    rows = [row for case in snapshots for row in case["repetitions"]]
    hostile_rows = [row["observation"] for case in hostile for row in case["repetitions"]]
    maxima: dict[str, int | None] = {
        name: max(row["counts"][name] for row in rows)
        for name in (
            "input_samples", "request_bytes", "output_records", "encoded_bytes",
            "decoded_bytes", "stdout_bytes", "stderr_bytes", "diagnostic_bytes",
            "text_bytes", "binary_bytes", "nested_depth", "nested_items",
            "retained_result_bytes",
        )
    }
    successful_parent = max(row["parent_total_ns"] for row in rows)
    maxima.update(
        {
            "wall_deadline_ms": (successful_parent + 999_999) // 1_000_000,
            "terminate_grace_ms": 250,
            "worker_address_space_bytes": None,
            "worker_peak_rss_bytes": max(row["diagnostics"]["maxrss"] for row in rows),
            "parent_retained_growth_bytes": max(
                row["parent_after"]["ru_maxrss"] - row["parent_before"]["ru_maxrss"]
                for row in rows
            ),
            "recursion_limit": 320,
            "successful_parent_total_ns": successful_parent,
            "launch_ns": max(row["launch_ns"] for row in rows),
            "reap_ns": max(row["reap_ns"] for row in rows),
            "child_load_ns": max(row["diagnostics"]["load_ns"] for row in rows),
            "child_import_ns": max(row["diagnostics"]["import_ns"] for row in rows),
            "child_decode_ns": max(row["diagnostics"]["decode_ns"] for row in rows),
            "timeout_cleanup_total_ns": max(
                row["cleanup"]["total_ns"] for row in hostile_rows
            ),
            "terminate_to_reap_ns": max(
                row["cleanup"]["terminate_to_reap_ns"] for row in hostile_rows
            ),
            "kill_to_reap_ns": max(
                row["cleanup"]["kill_to_reap_ns"] for row in hostile_rows
            ),
            "spi_max_word_size_bits": 8,
        }
    )
    return maxima


def _formula_values(maxima: dict[str, int | None]) -> dict[str, int]:
    raw = {name: value for name, value in maxima.items() if value is not None}
    return {
        "input_samples": _next_power_of_two(raw["input_samples"] * 128),
        "request_bytes": _next_power_of_two(raw["request_bytes"] * 2_048),
        "wall_deadline_ms": 5_000,
        "terminate_grace_ms": 250,
        "worker_address_space_bytes": 68_719_476_736,
        "worker_peak_rss_bytes": _next_power_of_two(raw["worker_peak_rss_bytes"] * 4),
        "parent_retained_growth_bytes": _next_power_of_two(
            raw["parent_retained_growth_bytes"] * 16
        ),
        "recursion_limit": 320,
        "output_records": _next_power_of_two(raw["output_records"] * 256),
        "encoded_bytes": _next_power_of_two(raw["encoded_bytes"] * 256),
        "decoded_bytes": _next_power_of_two(raw["decoded_bytes"] * 256),
        "stdout_bytes": 65_536,
        "stderr_bytes": 65_536,
        "diagnostic_bytes": _next_power_of_two(raw["diagnostic_bytes"] * 32),
        "text_bytes": _next_power_of_two(raw["text_bytes"] * 1_024),
        "binary_bytes": raw["binary_bytes"] * 65_536,
        "nested_depth": raw["nested_depth"] * 4,
        "nested_items": _next_power_of_two(raw["nested_items"] * 32),
        "retained_result_bytes": _next_power_of_two(raw["retained_result_bytes"] * 256),
        "successful_parent_total_ns": _ceil(raw["successful_parent_total_ns"] * 8, 100_000_000),
        "launch_ns": _ceil(raw["launch_ns"] * 8, 50_000_000),
        "reap_ns": max(50_000_000, raw["reap_ns"] * 64),
        "child_load_ns": max(100_000_000, raw["child_load_ns"] * 16),
        "child_import_ns": _ceil(raw["child_import_ns"] * 8, 50_000_000),
        "child_decode_ns": max(100_000_000, raw["child_decode_ns"] * 32),
        "timeout_cleanup_total_ns": 5_500_000_000,
        "terminate_to_reap_ns": 300_000_000,
        "kill_to_reap_ns": max(50_000_000, raw["kill_to_reap_ns"] * 16),
        "spi_max_word_size_bits": 8,
    }


def _validate_cap_relationships(values: dict[str, int], caps: dict[str, int]) -> None:
    for name in HARD & set(caps):
        if values[name] > caps[name]:
            raise ValueError("weakened cap")


def _validate_feasibility(values: dict[str, int]) -> None:
    if values["successful_parent_total_ns"] > values["wall_deadline_ms"] * 1_000_000:
        raise ValueError("deadline")
    if values["timeout_cleanup_total_ns"] > (
        values["wall_deadline_ms"] + values["terminate_grace_ms"] + 250
    ) * 1_000_000:
        raise ValueError("cleanup")
    if values["terminate_to_reap_ns"] > (values["terminate_grace_ms"] + 50) * 1_000_000:
        raise ValueError("terminate")
    if values["spi_max_word_size_bits"] != 8:
        raise ValueError("spi")


def _validate(proposal: object, prior: dict[str, Any] | None = None) -> None:
    if not isinstance(proposal, dict) or set(proposal) != {
        "schema", "round", "status", "environment", "evidence", "boundary_policy", "limits"
    }:
        raise ValueError("shape")
    if proposal["schema"] != "cycle3-threshold-proposal/v1" or proposal["round"] != 3:
        raise ValueError("schema")
    if proposal["status"] != "proposal-not-approved":
        raise ValueError("status")
    if proposal["environment"] != {
        "os": "macOS 15.7.7 build 24G720", "architecture": "x86_64",
        "machine_model": "Macmini8,1", "python": "3.12.13",
    }:
        raise ValueError("environment")
    if proposal["evidence"] != EXPECTED_EVIDENCE:
        raise ValueError("evidence")
    digest_paths = {
        "environment_sha256": RAW / "environment.json",
        "hostile_observations_sha256": RAW / "hostile-observations.json",
        "raw_manifest_sha256": RAW / "manifest.json",
        "observations_sha256": RAW / "observations.json",
        "requests_sha256": RAW / "requests.json",
        "experiment_caps_sha256": DATA / "cycle3/experiment-caps.json",
    }
    if any(proposal["evidence"][name] != _sha(path) for name, path in digest_paths.items()):
        raise ValueError("digest")
    limits = proposal["limits"]
    if not isinstance(limits, list) or len(limits) != 29:
        raise ValueError("count")
    ids = [item.get("id") for item in limits if isinstance(item, dict)]
    if len(ids) != 29 or len(set(ids)) != 29 or set(ids) != set(EXPECTED_VALUES):
        raise ValueError("ids")
    maxima = _maxima()
    formulas = _formula_values(maxima)
    if formulas != EXPECTED_VALUES:
        raise ValueError("formula calculation")
    caps_document = _load(DATA / "cycle3/experiment-caps.json")
    caps = {item["id"]: item["value"] for item in caps_document["caps"]}
    for item in limits:
        name = item["id"]
        if set(item) != {
            "id", "kind", "unit", "value", "accept", "reject", "raw_max",
            "experiment_cap", "derivation", "rationale",
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
            item["value"] != formulas[name]
            or item["accept"] != item["value"]
            or item["reject"] != item["value"] + 1
        ):
            raise ValueError("boundary")
        if item["raw_max"] != maxima[name] or item["derivation"] != EXPECTED_DERIVATIONS[name]:
            raise ValueError("maximum/formula")
        expected_cap = 5_000_000_000 if name == "successful_parent_total_ns" else caps.get(name)
        if item["experiment_cap"] != expected_cap:
            raise ValueError("cap identity")
        if expected_cap is not None and item["value"] > expected_cap:
            raise ValueError("weakened cap")
    values = {item["id"]: item["value"] for item in limits}
    _validate_cap_relationships(values, caps)
    _validate_feasibility(values)
    previous = prior or _load(PRIOR)
    previous_values = {item["id"]: item["value"] for item in previous["limits"]}
    changed = {name for name in values if values[name] != previous_values.get(name)}
    if changed != {"successful_parent_total_ns"}:
        raise ValueError("28/1 comparison")


def test_round3_identity_maxima_formula_comparison_and_authority() -> None:
    assert SUBJECT_COMMIT == "b260d9ecc0e74ed2502dda89beebb851ddfedb77"
    assert SUBJECT_TREE == "8a65628df5ba63727e8305e901b9954fe0bec7e5"
    assert _sha(CURRENT) == "7fb9e88aaa5888e1a3133ff2234253bdfbbc4bd7151fc3a3be3c387dd619f510"
    assert _sha(RATIONALE) == "8ea67712009a8a730c6eba8834e063179b709f07dfcdc5ffd7e9a55f6a93c58b"
    proposal = _load(CURRENT)
    assert CURRENT.read_text(encoding="utf-8") == (
        json.dumps(proposal, separators=(",", ":")) + "\n"
    )
    _validate(proposal)
    maxima = _maxima()
    assert len(maxima) == 29
    assert maxima["successful_parent_total_ns"] == 123_103_531
    assert 123_103_531 * 8 == 984_828_248
    assert _ceil(984_828_248, 100_000_000) == 1_000_000_000
    assert round(1_000_000_000 / 123_103_531, 2) == 8.12
    assert 1_000_000_000 <= 5_000 * 1_000_000
    rationale = RATIONALE.read_text(encoding="utf-8")
    assert "Exactly 28 of 29" in rationale
    assert "approximately 8.12 times" in rationale
    assert "one fifth" in rationale
    assert "supersedes proposal `395646f...`" in rationale
    assert "operator-approval record\n`b6d9040...`; neither transfers authority" in rationale
    assert "No numeric value becomes\nauthoritative" in rationale


@pytest.mark.parametrize(
    "mutation",
    [
        "missing", "extra", "duplicate", "bool", "float", "zero", "negative",
        "maximum", "formula", "weaken", "cap_identity", "unit", "accept", "reject",
        "deadline", "cleanup", "terminate", "spi", "approved", "digest", "commit",
        "environment", "comparison",
    ],
)
def test_round3_non_vacuous_negative_mutation_matrix(mutation: str) -> None:
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
        by_id["input_samples"]["value"] = {
            "bool": True, "float": 1.5, "zero": 0, "negative": -1
        }[mutation]
    elif mutation == "maximum":
        by_id["output_records"]["raw_max"] += 1
    elif mutation == "formula":
        by_id["successful_parent_total_ns"]["derivation"] = "raw_max * 8"
    elif mutation == "weaken":
        by_id["nested_depth"].update({"value": 41, "accept": 41, "reject": 42})
    elif mutation == "cap_identity":
        by_id["retained_result_bytes"]["experiment_cap"] += 1
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
        value["evidence"]["superseded_operator_approval_commit"] = "0" * 40
    elif mutation == "environment":
        value["environment"]["architecture"] = "arm64"
    elif mutation == "comparison":
        next(item for item in prior["limits"] if item["id"] == "input_samples")["value"] -= 1
    with pytest.raises(ValueError):
        _validate(value, prior)


@pytest.mark.parametrize("mutation", ["weaken", "deadline", "cleanup", "terminate", "spi"])
def test_cross_limit_mutations_reach_their_specific_guard(mutation: str) -> None:
    values = dict(EXPECTED_VALUES)
    caps_document = _load(DATA / "cycle3/experiment-caps.json")
    caps = {item["id"]: item["value"] for item in caps_document["caps"]}
    if mutation == "weaken":
        values["nested_depth"] = caps["nested_depth"] + 1
        with pytest.raises(ValueError, match="weakened cap"):
            _validate_cap_relationships(values, caps)
        return
    if mutation == "deadline":
        values["successful_parent_total_ns"] = 5_000_000_001
    elif mutation == "cleanup":
        values["timeout_cleanup_total_ns"] = 5_500_000_001
    elif mutation == "terminate":
        values["terminate_to_reap_ns"] = 300_000_001
    elif mutation == "spi":
        values["spi_max_word_size_bits"] = 9
    with pytest.raises(ValueError, match=mutation):
        _validate_feasibility(values)
