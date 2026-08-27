"""Fresh static verification of the immutable final C3-B1 binder."""

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
BINDER = ROOT / "testdata/decoders/cycle3/b1-final-candidate.json"
RATIONALE = ROOT / "docs/reviews/c3-b1-final-candidate.md"
PROPOSAL = ROOT / "testdata/decoders/cycle3/threshold-proposal-round-2.json"
APPROVAL = ROOT / "docs/reviews/c3-b1-threshold-approval.md"

ROLE_KEYS = {
    "semantic_fixture_implementation",
    "semantic_fixture_verification",
    "semantic_fixture_acceptance",
    "preexecution_runner_implementation",
    "preexecution_runner_verification",
    "preexecution_runner_acceptance",
}
COMMAND_IDS = {
    "python_dependency_check",
    "python_ruff",
    "python_mypy_product",
    "python_mypy_characterization",
    "fixture_determinism",
    "runner_binding",
    "installed_cli_help",
    "cycle2_evidence_b1",
    "cycle2_evidence_b2",
    "cycle2_evidence_b3",
    "cycle2_evidence_b4",
    "cycle2_evidence_b5",
    "cycle2_evidence_b6",
    "python_applicable_nonhardware",
    "frontend_lint",
    "frontend_typecheck",
    "frontend_unit",
    "frontend_build",
    "frontend_assets",
    "frontend_browser",
    "frontend_performance",
}
EXCLUSIONS = {
    "product decoder host or public decode API before the B1 checkpoint",
    "C#/.NET/pythonnet/libsigrokdecode/sigrok-cli or external decoder runtime",
    "hardware, USB, serial, firmware, or physical decode evidence",
    "wheel, sdist, upload, publication, or distribution",
    "non-macOS support claim",
    "Cycle 4",
}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text())
    assert isinstance(value, dict)
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


DIGEST_PATHS = {
    ("project_license", "sha256"): ROOT / "docs/reviews/c3-b1-project-license-review-round-1.md",
    ("semantic_fixture", "generator_sha256"): ROOT / "scripts/generate_cycle3_fixtures.py",
    ("semantic_fixture", "manifest_sha256"): ROOT / "testdata/decoders/cycle3/manifest.json",
    ("semantic_fixture", "experiment_caps_sha256"): ROOT
    / "testdata/decoders/cycle3/experiment-caps.json",
    ("semantic_fixture", "verification_record_sha256"): ROOT
    / "docs/reviews/c3-b1-semantic-fixture-verification-round-9.md",
    ("semantic_fixture", "accumulated_record_sha256"): ROOT
    / "docs/reviews/c3-b1-semantic-fixture-accumulated-validation-round-2.md",
    ("semantic_fixture", "acceptance_record_sha256"): ROOT
    / "docs/reviews/c3-b1-semantic-fixture-acceptance-round-2.md",
    ("preexecution_runner", "binding_sha256"): ROOT
    / "tools/cycle3_characterize/candidate-binding.json",
    ("preexecution_runner", "launch_sha256"): ROOT / "tools/cycle3_characterize/launch.json",
    ("preexecution_runner", "runner_sha256"): ROOT / "tools/cycle3_characterize/runner.py",
    ("preexecution_runner", "worker_sha256"): ROOT / "tools/cycle3_characterize/worker.py",
    ("preexecution_runner", "method_sha256"): ROOT / "docs/cycle-3-characterization-method.md",
    ("preexecution_runner", "verification_test_sha256"): ROOT
    / "tests/verification/test_c3_b1_preexecution_runner_candidate.py",
    ("preexecution_runner", "verification_record_sha256"): ROOT
    / "docs/reviews/c3-b1-preexecution-runner-verification-round-2.md",
    ("preexecution_runner", "accumulated_record_sha256"): ROOT
    / "docs/reviews/c3-b1-preexecution-runner-accumulated-validation-round-2.md",
    ("preexecution_runner", "acceptance_record_sha256"): ROOT
    / "docs/reviews/c3-b1-preexecution-runner-acceptance-round-2.md",
    ("raw_baseline", "environment_sha256"): ROOT / "testdata/decoders/cycle3-raw/environment.json",
    ("raw_baseline", "hostile_observations_sha256"): ROOT
    / "testdata/decoders/cycle3-raw/hostile-observations.json",
    ("raw_baseline", "manifest_sha256"): ROOT / "testdata/decoders/cycle3-raw/manifest.json",
    ("raw_baseline", "observations_sha256"): ROOT
    / "testdata/decoders/cycle3-raw/observations.json",
    ("raw_baseline", "requests_sha256"): ROOT / "testdata/decoders/cycle3-raw/requests.json",
    ("raw_baseline", "verification_test_sha256"): ROOT
    / "tests/verification/test_c3_b1_raw_baseline_candidate.py",
    ("raw_baseline", "verification_record_sha256"): ROOT
    / "docs/reviews/c3-b1-raw-baseline-verification-round-1.md",
    ("raw_baseline", "accumulated_record_sha256"): ROOT
    / "docs/reviews/c3-b1-raw-baseline-accumulated-validation-round-1.md",
    ("raw_baseline", "acceptance_record_sha256"): ROOT
    / "docs/reviews/c3-b1-raw-baseline-acceptance-round-1.md",
    ("approved_thresholds", "proposal_sha256"): PROPOSAL,
    ("approved_thresholds", "rationale_sha256"): ROOT
    / "docs/reviews/c3-b1-threshold-proposal-rationale-round-2.md",
    ("approved_thresholds", "verification_test_sha256"): ROOT
    / "tests/verification/test_c3_b1_threshold_proposal_round2.py",
    ("approved_thresholds", "verification_record_sha256"): ROOT
    / "docs/reviews/c3-b1-threshold-proposal-verification-round-2.md",
    ("approved_thresholds", "accumulated_record_sha256"): ROOT
    / "docs/reviews/c3-b1-threshold-proposal-accumulated-validation-round-2.md",
    ("approved_thresholds", "acceptance_record_sha256"): ROOT
    / "docs/reviews/c3-b1-threshold-proposal-acceptance-round-2.md",
    ("approved_thresholds", "operator_approval_sha256"): APPROVAL,
}


def _validate(value: object) -> None:
    if not isinstance(value, dict) or set(value) != {
        "schema",
        "batch",
        "status",
        "support_scope",
        "governing",
        "environment",
        "internal_role_map",
        "evidence",
        "closed_findings",
        "historical_invalidations_preserved",
        "frozen_commands",
        "pytest_applicability",
        "exclusions",
        "next_gate",
    }:
        raise ValueError("shape")
    if value["schema"] != "cycle3-b1-final-candidate/v1" or value["batch"] != "C3-B1":
        raise ValueError("schema")
    if (
        value["status"] != "candidate-not-accepted"
        or value["next_gate"] != "fresh final C3-B1 verification"
    ):
        raise ValueError("status")
    if value["support_scope"] != "macOS-only" or value["environment"] != {
        "os": "macOS 15.7.7 build 24G720",
        "architecture": "x86_64",
        "machine_model": "Macmini8,1",
        "python": "3.12.13",
        "node": "22.14.0",
        "browser": "Chromium 133.0.6943.16",
        "automation": "Playwright 1.50.1",
    }:
        raise ValueError("environment")
    roles = value["internal_role_map"]
    if set(roles) != ROLE_KEYS:
        raise ValueError("roles")
    identities = [entry.get("identity", entry.get("final_identity")) for entry in roles.values()]
    if len(set(identities)) != 6 or any(not identity for identity in identities):
        raise ValueError("role separation")
    if not roles["semantic_fixture_implementation"].get("history_is_preserved") or not roles[
        "preexecution_runner_implementation"
    ].get("history_is_preserved"):
        raise ValueError("history")
    evidence = value["evidence"]
    if set(evidence) != {
        "project_license",
        "semantic_fixture",
        "preexecution_runner",
        "raw_baseline",
        "approved_thresholds",
    }:
        raise ValueError("evidence")
    if evidence["project_license"].get("verdict") != "pass":
        raise ValueError("license")
    for (group, field), path in DIGEST_PATHS.items():
        if evidence[group].get(field) != _sha(path):
            raise ValueError("digest")
    proposal = _load(PROPOSAL)
    limits = proposal["limits"]
    if evidence["approved_thresholds"].get("limit_count") != 29 or len(limits) != 29:
        raise ValueError("limits")
    if any(
        type(item["value"]) is not int
        or item["accept"] != item["value"]
        or item["reject"] != item["value"] + 1
        for item in limits
    ):
        raise ValueError("boundaries")
    approval = APPROVAL.read_text()
    if (
        "approved" not in approval.lower()
        or evidence["approved_thresholds"].get("operator_approval_commit")
        != "b6d904064ab7b9e195eedded1c55efc306eeb925"
    ):
        raise ValueError("approval")
    if set(value["closed_findings"]) != {"C3B1-RI011", "C3B1-RI013", "C3B1-TPV001"}:
        raise ValueError("findings")
    if len(value["historical_invalidations_preserved"]) != 4:
        raise ValueError("invalidations")
    commands = value["frozen_commands"]
    if len(commands) != 21 or {item.get("id") for item in commands} != COMMAND_IDS:
        raise ValueError("commands")
    if any(
        item.get("cwd") not in {"Software/LogicAnalyzerPy", "Software/LogicAnalyzerPy/web"}
        or not isinstance(item.get("argv"), list)
        or not item["argv"]
        for item in commands
    ):
        raise ValueError("command shape")
    applicability = value["pytest_applicability"]
    if applicability != {
        "selected": 637,
        "deselected_historical": 3,
        "classification_record": (
            "docs/reviews/c3-b1-threshold-proposal-accumulated-validation-round-2.md"
        ),
    }:
        raise ValueError("applicability")
    if set(value["exclusions"]) != EXCLUSIONS:
        raise ValueError("exclusions")


def test_exact_scope_schema_roles_digests_order_limits_approval_and_authority() -> None:
    assert _sha(BINDER) == "1c2cbaa7d99c247b9779b3f7f3654358fcc6e5219ddb030dfb5904faaa9aa29a"
    assert _sha(RATIONALE) == "4203c2b2ea079d13a72cac3474299cf93d9f3d8b4f4ae6480fdb289674b3d30b"
    binder = _load(BINDER)
    _validate(binder)
    commits = []
    for group in binder["evidence"].values():
        commits.extend(value for key, value in group.items() if key.endswith("commit"))
    commits.extend([binder["governing"]["commit"], binder["governing"]["assignment_commit"]])
    for commit in commits:
        subprocess.run(["git", "merge-base", "--is-ancestor", commit, "HEAD"], cwd=REPO, check=True)
    for group in ("semantic_fixture", "preexecution_runner", "raw_baseline", "approved_thresholds"):
        entry = binder["evidence"][group]
        candidate = entry.get("candidate_commit", entry.get("proposal_commit"))
        tree = entry.get("candidate_tree", entry.get("proposal_tree"))
        assert (
            subprocess.check_output(
                ["git", "rev-parse", f"{candidate}^{{tree}}"], cwd=REPO, text=True
            ).strip()
            == tree
        )
    text = RATIONALE.read_text()
    assert "no B1 manifest, checkpoint, or B2 authority" in text
    assert "rights-holder/counsel limitation" in text
    assert "still mandatory in that order" in text


def test_complete_implementation_histories_are_explicitly_bound() -> None:
    roles = _load(BINDER)["internal_role_map"]
    assert roles["semantic_fixture_implementation"].get("history") == [
        "c3-b1-semantic-fixture-implementor-1",
        "c3-b1-semantic-fixture-implementor-replacement-1",
        "c3-b1-semantic-fixture-implementor-replacement-2",
        "c3-b1-semantic-fixture-implementor-replacement-3",
        "c3-b1-semantic-fixture-implementor-replacement-4",
        "c3-b1-semantic-fixture-implementor-replacement-5",
        "c3-b1-semantic-fixture-implementor-replacement-6",
    ]
    assert roles["preexecution_runner_implementation"].get("history") == [
        "c3-b1-pre-execution-runner-implementor-1",
        "c3-b1-pre-execution-runner-implementor-replacement-1",
        "c3-b1-pre-execution-runner-implementor-replacement-2",
        "c3-b1-pre-execution-runner-implementor-replacement-3",
    ]


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "evidence",
        "role",
        "digest",
        "commit",
        "status",
        "environment",
        "command",
        "limit",
        "approval",
        "finding",
        "applicability",
        "exclusion",
    ],
)
def test_nonvacuous_closed_mutation_matrix(mutation: str) -> None:
    value = copy.deepcopy(_load(BINDER))
    _validate(value)
    if mutation == "missing":
        value.pop("next_gate")
    elif mutation == "extra":
        value["unexpected"] = True
    elif mutation == "evidence":
        value["evidence"].pop("raw_baseline")
    elif mutation == "role":
        value["internal_role_map"]["semantic_fixture_verification"]["identity"] = value[
            "internal_role_map"
        ]["semantic_fixture_acceptance"]["identity"]
    elif mutation == "digest":
        value["evidence"]["raw_baseline"]["requests_sha256"] = "0" * 64
    elif mutation == "commit":
        value["evidence"]["approved_thresholds"]["operator_approval_commit"] = "0" * 40
    elif mutation == "status":
        value["status"] = "accepted"
    elif mutation == "environment":
        value["environment"]["architecture"] = "arm64"
    elif mutation == "command":
        value["frozen_commands"].pop()
    elif mutation == "limit":
        value["evidence"]["approved_thresholds"]["limit_count"] = 28
    elif mutation == "approval":
        value["evidence"]["approved_thresholds"]["operator_approval_sha256"] = "0" * 64
    elif mutation == "finding":
        value["closed_findings"].pop()
    elif mutation == "applicability":
        value["pytest_applicability"]["selected"] = 638
    elif mutation == "exclusion":
        value["exclusions"].pop()
    with pytest.raises(ValueError):
        _validate(value)
