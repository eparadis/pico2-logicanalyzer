"""Static, mutation-resistant verification of replacement final C3-B1 round 4."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
BINDER = ROOT / "testdata/decoders/cycle3/b1-final-candidate-round-4.json"
REVIEW = ROOT / "docs/reviews/c3-b1-final-candidate-round-4.md"
PROPOSAL = ROOT / "testdata/decoders/cycle3/threshold-proposal-round-4.json"
CANDIDATE = "7246dcbe55a60ef7ee9196f4bf265c7c75141d55"
CANDIDATE_TREE = "51e895a1e2c95580d04bc8a31ed8d58a85613e1a"
ASSIGNMENT = "212fc3327715bd31a3bc3cd59b10d746ec4c7108"
VERIFIER_ASSIGNMENT = "4299312"

TOP_LEVEL_KEYS = {
    "schema",
    "round",
    "batch",
    "status",
    "support_scope",
    "governing",
    "correction",
    "environment",
    "internal_role_map",
    "evidence",
    "closed_findings",
    "historical_invalidations_preserved",
    "frozen_commands",
    "pytest_applicability",
    "exclusions",
    "next_gate",
}
COMPONENT_DIGESTS = {
    "correction": "bb51f91e667a6a1366857a395186b9dd163b14703a934ec1002f42d32e74d5bf",
    "internal_role_map": "61a853e5263ccaf4e4621803caef4b2c17656cd3f058515c17da26dc19bce83a",
    "evidence": "782c6b0a6f5d00fff09ea2629c3121d7c601f8709f257c4131ff6f81c2346db4",
    "closed_findings": "6910c271918965f6d5731ffd3719ec55651f06858e7831e6ed04483dc184fbfd",
    "historical_invalidations_preserved": (
        "bc202bdfe9a54cfa3fdb67be450545a1dcab4cde95476d6e6ee2060fb925af86"
    ),
    "frozen_commands": "9d0aa405662d8cdc8cb3d87465225f9a9769300d3150a29c9349a300ee8aed7c",
    "pytest_applicability": "9e1aa766a3aee994735f762d66de9d17b3ea44056f3bced3c477c0831bc95949",
    "exclusions": "db4f4bb3eea39d99bdc8590be8266ea2cc150a1308e1fa5a7978a22f453cca66",
}
EXPECTED_LIMITS = {
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
COMMAND_IDS = {
    "python_dependency_check",
    "python_ruff",
    "python_mypy_product",
    "python_mypy_characterization",
    "fixture_determinism",
    "runner_binding",
    "installed_cli_help",
    *(f"cycle2_evidence_b{number}" for number in range(1, 7)),
    "python_applicable_nonhardware",
    "frontend_lint",
    "frontend_typecheck",
    "frontend_unit",
    "frontend_build",
    "frontend_assets",
    "frontend_browser",
    "frontend_performance",
}
LIVE_DIGEST_PATHS = {
    ("project_license", "sha256"): "docs/reviews/c3-b1-project-license-review-round-1.md",
    ("semantic_fixture", "generator_sha256"): "scripts/generate_cycle3_fixtures.py",
    (
        "semantic_fixture",
        "semantic_fixture_sha256",
    ): "testdata/decoders/cycle3/semantic-fixtures.json",
    ("semantic_fixture", "manifest_sha256"): "testdata/decoders/cycle3/manifest.json",
    ("semantic_fixture", "experiment_caps_sha256"): "testdata/decoders/cycle3/experiment-caps.json",
    (
        "semantic_fixture",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_semantic_fixture_correction_round2.py",
    (
        "semantic_fixture",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-semantic-fixture-correction-verification-round-2.md",
    (
        "semantic_fixture",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-semantic-fixture-correction-accumulated-validation-round-2.md",
    (
        "semantic_fixture",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-semantic-fixture-correction-acceptance-round-2.md",
    ("preexecution_runner", "binding_sha256"): "tools/cycle3_characterize/candidate-binding.json",
    ("preexecution_runner", "launch_sha256"): "tools/cycle3_characterize/launch.json",
    ("preexecution_runner", "runner_sha256"): "tools/cycle3_characterize/runner.py",
    ("preexecution_runner", "worker_sha256"): "tools/cycle3_characterize/worker.py",
    ("preexecution_runner", "method_sha256"): "docs/cycle-3-characterization-method.md",
    (
        "preexecution_runner",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py",
    (
        "preexecution_runner",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-verification-round-5.md",
    (
        "preexecution_runner",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-accumulated-validation-round-3.md",
    (
        "preexecution_runner",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-acceptance-round-3.md",
    ("raw_baseline", "environment_sha256"): "testdata/decoders/cycle3-raw/environment.json",
    ("raw_baseline", "requests_sha256"): "testdata/decoders/cycle3-raw/requests.json",
    ("raw_baseline", "observations_sha256"): "testdata/decoders/cycle3-raw/observations.json",
    (
        "raw_baseline",
        "hostile_observations_sha256",
    ): "testdata/decoders/cycle3-raw/hostile-observations.json",
    ("raw_baseline", "manifest_sha256"): "testdata/decoders/cycle3-raw/manifest.json",
    (
        "raw_baseline",
        "collection_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-collection-replacement-round-1.md",
    (
        "raw_baseline",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_raw_baseline_candidate_replacement.py",
    (
        "raw_baseline",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-verification-round-4.md",
    (
        "raw_baseline",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-accumulated-validation-round-3.md",
    (
        "raw_baseline",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-acceptance-round-3.md",
    (
        "approved_thresholds",
        "proposal_sha256",
    ): "testdata/decoders/cycle3/threshold-proposal-round-4.json",
    (
        "approved_thresholds",
        "rationale_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-rationale-round-4.md",
    (
        "approved_thresholds",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_threshold_proposal_round4.py",
    (
        "approved_thresholds",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-verification-round-4.md",
    (
        "approved_thresholds",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-accumulated-validation-round-4.md",
    (
        "approved_thresholds",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-acceptance-round-4.md",
    (
        "approved_thresholds",
        "operator_approval_sha256",
    ): "docs/reviews/c3-b1-threshold-approval-round-4.md",
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text())
    assert isinstance(value, dict)
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(encoded.encode()).hexdigest()


def validate(value: object) -> None:
    if not isinstance(value, dict) or set(value) != TOP_LEVEL_KEYS:
        raise ValueError("top-level shape")
    if (value["schema"], value["round"], value["batch"], value["status"]) != (
        "cycle3-b1-final-candidate/v1",
        4,
        "C3-B1",
        "candidate-not-accepted",
    ):
        raise ValueError("schema/status")
    if value["support_scope"] != "macOS-only":
        raise ValueError("authority")
    if value["governing"] != {
        "commit": "ea83a403bb6f644d33069d3bebd41d5f1e0a60c0",
        "tree": "d9fb09345ab85580cd8c877745262d1b481e366f",
        "assignment_commit": ASSIGNMENT,
    }:
        raise ValueError("governing")
    if value["environment"] != {
        "os": "macOS 15.7.7 build 24G720",
        "architecture": "x86_64",
        "machine_model": "Macmini8,1",
        "python": "3.12.13",
        "node": "22.14.0",
        "browser": "Chromium 133.0.6943.16",
        "automation": "Playwright 1.50.1",
    }:
        raise ValueError("environment")
    for key, expected in COMPONENT_DIGESTS.items():
        if canonical_sha(value[key]) != expected:
            raise ValueError(f"frozen component {key}")

    roles = value["internal_role_map"]
    identities = [entry.get("identity", entry.get("final_identity")) for entry in roles.values()]
    if len(identities) != 6 or None in identities or len(set(identities)) != 6:
        raise ValueError("role separation")
    fixture_history = roles["semantic_fixture_implementation"]["ordered_history"]
    runner_history = roles["preexecution_runner_implementation"]["ordered_history"]
    if fixture_history != ["c3-b1-semantic-fixture-implementor-1"] + [
        f"c3-b1-semantic-fixture-implementor-replacement-{number}" for number in range(1, 9)
    ]:
        raise ValueError("fixture role history")
    if runner_history != ["c3-b1-pre-execution-runner-implementor-1"] + [
        f"c3-b1-pre-execution-runner-implementor-replacement-{number}" for number in range(1, 5)
    ]:
        raise ValueError("runner role history")

    evidence = value["evidence"]
    if set(evidence) != {
        "project_license",
        "semantic_fixture",
        "preexecution_runner",
        "raw_baseline",
        "approved_thresholds",
    }:
        raise ValueError("evidence shape")
    for (group, field), relative_path in LIVE_DIGEST_PATHS.items():
        if evidence[group].get(field) != sha(ROOT / relative_path):
            raise ValueError(f"live digest {group}.{field}")

    proposal = load(PROPOSAL)
    limits = proposal["limits"]
    by_id = {item["id"]: item for item in limits}
    if (
        len(limits) != 29
        or len(by_id) != 29
        or evidence["approved_thresholds"]["limit_count"] != 29
    ):
        raise ValueError("limit inventory")
    if {name: item["value"] for name, item in by_id.items()} != EXPECTED_LIMITS:
        raise ValueError("exact limits")
    if evidence["approved_thresholds"]["limits"] != EXPECTED_LIMITS:
        raise ValueError("bound limits")
    if any(
        type(item["value"]) is not int
        or item["accept"] != item["value"]
        or item["reject"] != item["value"] + 1
        for item in limits
    ):
        raise ValueError("inclusive boundaries")
    thresholds = evidence["approved_thresholds"]
    if (
        thresholds["proposal_commit"] != "b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0"
        or thresholds["operator_approval_commit"] != "afd45856ee261158521b902dabdf926e5f1f922a"
        or thresholds["superseded_proposal_commit"] != "b260d9ecc0e74ed2502dda89beebb851ddfedb77"
        or thresholds["superseded_operator_approval_commit"]
        != "63fdfee87159251cdf525eb608340e6bc08ad010"
    ):
        raise ValueError("approval authority")

    commands = value["frozen_commands"]
    if len(commands) != 21 or {item.get("id") for item in commands} != COMMAND_IDS:
        raise ValueError("command inventory")
    if any(
        item.get("cwd") not in {"Software/LogicAnalyzerPy", "Software/LogicAnalyzerPy/web"}
        or not item.get("argv")
        for item in commands
    ):
        raise ValueError("command shape")
    applicability = value["pytest_applicability"]
    if (
        applicability.get("inventory_modules"),
        applicability.get("included_modules"),
        applicability.get("excluded_modules"),
        applicability.get("collected"),
        applicability.get("passed"),
        applicability.get("inherited_classified_skips"),
    ) != (56, 41, 15, 608, 602, 6):
        raise ValueError("applicability")
    expected_next = (
        "fresh replacement round-4 final C3-B1 verification, then complete root accumulated "
        "validation, fresh independent acceptance, atomic replacement-manifest assembly, "
        "distinct manifest verification, joint manifest/verifier commit, and replacement B1 "
        "checkpoint; only that checkpoint may resume B2"
    )
    if value["next_gate"] != expected_next:
        raise ValueError("gate order")


def test_exact_candidate_scope_tree_bytes_ancestry_and_live_digests() -> None:
    assert sha(BINDER) == "a186af26805c804613271641e5f57b1393ae31d79fa800a29249e37efc0650fd"
    assert sha(REVIEW) == "591459742b9453e94047438ec79a6e2bdd54ed3b6d0c71207bbae4c64b563d73"
    assert (
        subprocess.check_output(
            ["git", "rev-parse", f"{CANDIDATE}^{{tree}}"], cwd=REPO, text=True
        ).strip()
        == CANDIDATE_TREE
    )
    changed = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", CANDIDATE],
        cwd=REPO,
        text=True,
    ).splitlines()
    assert changed == [str(REVIEW.relative_to(REPO)), str(BINDER.relative_to(REPO))]
    for path in (BINDER, REVIEW):
        committed = subprocess.check_output(
            ["git", "show", f"{CANDIDATE}:{path.relative_to(REPO)}"], cwd=REPO
        )
        assert committed == path.read_bytes()

    binder = load(BINDER)
    validate(binder)
    commits = [
        CANDIDATE,
        VERIFIER_ASSIGNMENT,
        binder["governing"]["commit"],
        binder["governing"]["assignment_commit"],
    ]
    for group in binder["evidence"].values():
        commits.extend(value for key, value in group.items() if key.endswith("commit"))
    commits.extend(value for key, value in binder["correction"].items() if key.endswith("commit"))
    commits.extend(
        value
        for key, value in binder["correction"]["preserved_prior_final_binder_correction"].items()
        if key.endswith("commit")
    )
    for commit in commits:
        subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=REPO, check=True)
    for group, commit_key, tree_key in (
        ("semantic_fixture", "candidate_commit", "candidate_tree"),
        ("preexecution_runner", "candidate_commit", "candidate_tree"),
        ("raw_baseline", "candidate_commit", "candidate_tree"),
        ("approved_thresholds", "proposal_commit", "proposal_tree"),
    ):
        entry = binder["evidence"][group]
        assert (
            subprocess.check_output(
                ["git", "rev-parse", f"{entry[commit_key]}^{{tree}}"], cwd=REPO, text=True
            ).strip()
            == entry[tree_key]
        )


def test_review_preserves_scope_limitations_findings_and_gate_order() -> None:
    text = REVIEW.read_text()
    required = [
        "candidate-not-accepted",
        "rights-holder or qualified-counsel confirmation",
        "C3B2-IF001",
        "C3B2-IF002",
        "C3B1-RA001",
        "C3B1-RV002",
        "C3B1-RV003",
        "Exactly 26 values remain unchanged from round 3",
        "Only that checkpoint may resume B2",
    ]
    assert all(fragment in text for fragment in required)
    assert "adds no product, fixture,\nrunner, raw, threshold, lock, workflow, manifest" in text


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "schema",
        "status",
        "authority",
        "governing",
        "correction",
        "environment",
        "role-collapse",
        "history",
        "digest",
        "evidence",
        "limit",
        "approval",
        "finding",
        "invalidation",
        "command",
        "applicability",
        "exclusion",
        "order",
    ],
)
def test_mutation_matrix_rejects_every_required_family(mutation: str) -> None:
    value = copy.deepcopy(load(BINDER))
    validate(value)
    if mutation == "missing":
        value.pop("next_gate")
    elif mutation == "extra":
        value["unexpected"] = True
    elif mutation == "schema":
        value["schema"] = "cycle3-b1-final-candidate/v2"
    elif mutation == "status":
        value["status"] = "accepted"
    elif mutation == "authority":
        value["support_scope"] = "cross-platform"
    elif mutation == "governing":
        value["governing"]["tree"] = "0" * 40
    elif mutation == "correction":
        value["correction"]["findings"].pop()
    elif mutation == "environment":
        value["environment"]["architecture"] = "arm64"
    elif mutation == "role-collapse":
        roles = value["internal_role_map"]
        roles["semantic_fixture_acceptance"]["identity"] = roles["semantic_fixture_verification"][
            "identity"
        ]
    elif mutation == "history":
        value["internal_role_map"]["preexecution_runner_implementation"]["ordered_history"].pop()
    elif mutation == "digest":
        value["evidence"]["raw_baseline"]["requests_sha256"] = "0" * 64
    elif mutation == "evidence":
        value["evidence"].pop("project_license")
    elif mutation == "limit":
        value["evidence"]["approved_thresholds"]["limits"]["launch_ns"] += 1
    elif mutation == "approval":
        value["evidence"]["approved_thresholds"]["operator_approval_commit"] = "0" * 40
    elif mutation == "finding":
        value["closed_findings"].pop()
    elif mutation == "invalidation":
        value["historical_invalidations_preserved"].pop()
    elif mutation == "command":
        value["frozen_commands"].pop()
    elif mutation == "applicability":
        value["pytest_applicability"]["collected"] += 1
    elif mutation == "exclusion":
        value["exclusions"].pop()
    elif mutation == "order":
        value["next_gate"] = "resume B2"
    with pytest.raises(ValueError):
        validate(value)
