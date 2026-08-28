"""Static, mutation-resistant verification of replacement final C3-B1 round 3."""

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
BINDER = ROOT / "testdata/decoders/cycle3/b1-final-candidate-round-3.json"
REVIEW = ROOT / "docs/reviews/c3-b1-final-candidate-round-3.md"
PROPOSAL = ROOT / "testdata/decoders/cycle3/threshold-proposal-round-3.json"
CANDIDATE = "4a7dc728048812cfb4cf46f010939c182ac948cf"
CANDIDATE_TREE = "5ee316695d3a4acf8f30e60da377ba6651844969"
ASSIGNMENT_DESCENDANT = "fc622c0f0892f0f9fd5daeda56f42dd037d9d69c"

ROLE_KEYS = {
    "semantic_fixture_implementation",
    "semantic_fixture_verification",
    "semantic_fixture_acceptance",
    "preexecution_runner_implementation",
    "preexecution_runner_verification",
    "preexecution_runner_acceptance",
}
FIXTURE_HISTORY = ["c3-b1-semantic-fixture-implementor-1"] + [
    f"c3-b1-semantic-fixture-implementor-replacement-{n}" for n in range(1, 8)
]
RUNNER_HISTORY = ["c3-b1-pre-execution-runner-implementor-1"] + [
    f"c3-b1-pre-execution-runner-implementor-replacement-{n}" for n in range(1, 4)
]
FINDINGS = {
    "C3B1-RI011",
    "C3B1-RI013",
    "C3B1-TPV001",
    "C3B1-FV001",
    "C3B1-MP001",
    "C3B1-MV001",
    "C3B1-MV002",
    "C3B2-IF001",
    "C3B1-RV001",
}
COMMAND_IDS = {
    "python_dependency_check",
    "python_ruff",
    "python_mypy_product",
    "python_mypy_characterization",
    "fixture_determinism",
    "runner_binding",
    "installed_cli_help",
    *(f"cycle2_evidence_b{n}" for n in range(1, 7)),
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


def load(path: Path) -> dict[str, Any]:
    result = json.loads(path.read_text())
    assert isinstance(result, dict)
    return result


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


DIGESTS = {
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
    ): "tests/verification/test_c3_b1_semantic_fixture_correction.py",
    (
        "semantic_fixture",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-semantic-fixture-correction-verification-round-1.md",
    (
        "semantic_fixture",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-semantic-fixture-correction-accumulated-validation-round-1.md",
    (
        "semantic_fixture",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-semantic-fixture-correction-acceptance-round-1.md",
    ("preexecution_runner", "binding_sha256"): "tools/cycle3_characterize/candidate-binding.json",
    ("preexecution_runner", "launch_sha256"): "tools/cycle3_characterize/launch.json",
    ("preexecution_runner", "runner_sha256"): "tools/cycle3_characterize/runner.py",
    ("preexecution_runner", "worker_sha256"): "tools/cycle3_characterize/worker.py",
    ("preexecution_runner", "method_sha256"): "docs/cycle-3-characterization-method.md",
    (
        "preexecution_runner",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_runner_fixture_rebinding.py",
    (
        "preexecution_runner",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-verification-round-1.md",
    (
        "preexecution_runner",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-accumulated-validation-round-1.md",
    (
        "preexecution_runner",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-acceptance-round-1.md",
    ("raw_baseline", "environment_sha256"): "testdata/decoders/cycle3-raw/environment.json",
    (
        "raw_baseline",
        "hostile_observations_sha256",
    ): "testdata/decoders/cycle3-raw/hostile-observations.json",
    ("raw_baseline", "manifest_sha256"): "testdata/decoders/cycle3-raw/manifest.json",
    ("raw_baseline", "observations_sha256"): "testdata/decoders/cycle3-raw/observations.json",
    ("raw_baseline", "requests_sha256"): "testdata/decoders/cycle3-raw/requests.json",
    (
        "raw_baseline",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_raw_baseline_candidate.py",
    (
        "raw_baseline",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-verification-round-3.md",
    (
        "raw_baseline",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-accumulated-validation-round-2.md",
    (
        "raw_baseline",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-raw-baseline-acceptance-round-2.md",
    (
        "approved_thresholds",
        "proposal_sha256",
    ): "testdata/decoders/cycle3/threshold-proposal-round-3.json",
    (
        "approved_thresholds",
        "rationale_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-rationale-round-3.md",
    (
        "approved_thresholds",
        "verification_test_sha256",
    ): "tests/verification/test_c3_b1_threshold_proposal_round3.py",
    (
        "approved_thresholds",
        "verification_record_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-verification-round-3.md",
    (
        "approved_thresholds",
        "accumulated_record_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-accumulated-validation-round-3.md",
    (
        "approved_thresholds",
        "acceptance_record_sha256",
    ): "docs/reviews/c3-b1-threshold-proposal-acceptance-round-3.md",
    (
        "approved_thresholds",
        "operator_approval_sha256",
    ): "docs/reviews/c3-b1-threshold-approval-round-3.md",
}


def validate(value: object) -> None:
    if not isinstance(value, dict) or set(value) != {
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
    }:
        raise ValueError("top-level shape")
    if (value["schema"], value["round"], value["batch"], value["status"]) != (
        "cycle3-b1-final-candidate/v1",
        3,
        "C3-B1",
        "candidate-not-accepted",
    ):
        raise ValueError("identity/status")
    if (
        value["support_scope"] != "macOS-only"
        or value["next_gate"] != "fresh replacement final C3-B1 verification"
    ):
        raise ValueError("authority")
    if value["governing"] != {
        "commit": "ea83a403bb6f644d33069d3bebd41d5f1e0a60c0",
        "tree": "d9fb09345ab85580cd8c877745262d1b481e366f",
        "assignment_commit": "70b6d88bb7a2bde703fdc69f8375cab7658f4100",
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
    correction = value["correction"]
    if correction != {
        "finding": "C3B2-IF001",
        "superseded_final_candidate_commit": "1f8793210a3298ed190ff30f97c84b6f9feb9b29",
        "superseded_manifest_commit": "c34a2517472a443e9d8ad7b41be800b272db9833",
        "superseded_checkpoint_commit": "06ca562558014dc0a32588493b8d92d55359ae74",
        "fixture_correction_candidate_commit": "a98d328aab92f3dad66988fb70cc567946dc89d0",
        "fixture_correction_candidate_tree": "450aadcf26bd6c74860872bfbf0a0a1b32d94f3b",
        "scope": (
            "rebind complete B1 evidence after the independently derived "
            "incomplete-UART fixture correction"
        ),
        "preserved_prior_final_binder_correction": {
            "finding": "C3B1-FV001",
            "superseded_candidate_commit": "72e7b35bb3bb8412846caef5302892f9de209c3b",
            "failed_verification_commit": "a9627e6248cf7cd2642e558429dfbddd484d3f24",
            "scope": "enumerate complete ordered fixture and runner implementation histories",
        },
    }:
        raise ValueError("correction")
    roles = value["internal_role_map"]
    if set(roles) != ROLE_KEYS:
        raise ValueError("role shape")
    identities = [entry.get("identity", entry.get("final_identity")) for entry in roles.values()]
    if len(set(identities)) != 6 or None in identities:
        raise ValueError("role separation")
    if roles["semantic_fixture_implementation"] != {
        "final_identity": FIXTURE_HISTORY[-1],
        "ordered_history": FIXTURE_HISTORY,
    } or roles["preexecution_runner_implementation"] != {
        "final_identity": RUNNER_HISTORY[-1],
        "ordered_history": RUNNER_HISTORY,
    }:
        raise ValueError("implementation histories")
    expected_roles = {
        "semantic_fixture_verification": "c3-b1-semantic-fixture-correction-verifier-1",
        "semantic_fixture_acceptance": "c3-b1-semantic-fixture-correction-acceptance-1",
        "preexecution_runner_verification": "c3-b1-pre-execution-runner-rebinding-verifier-1",
        "preexecution_runner_acceptance": "c3-b1-pre-execution-runner-rebinding-acceptance-1",
    }
    if any(roles[key] != {"identity": identity} for key, identity in expected_roles.items()):
        raise ValueError("role identities")
    evidence = value["evidence"]
    if (
        set(evidence)
        != {
            "project_license",
            "semantic_fixture",
            "preexecution_runner",
            "raw_baseline",
            "approved_thresholds",
        }
        or evidence["project_license"]["verdict"] != "pass"
    ):
        raise ValueError("evidence")
    for (group, field), path in DIGESTS.items():
        if evidence[group].get(field) != sha(ROOT / path):
            raise ValueError(f"digest {group}.{field}")
    proposal = load(PROPOSAL)
    limits = proposal["limits"]
    if (
        evidence["approved_thresholds"]["limit_count"] != 29
        or len(limits) != 29
        or len({item["id"] for item in limits}) != 29
    ):
        raise ValueError("limit inventory")
    if any(
        type(item["value"]) is not int
        or item["accept"] != item["value"]
        or item["reject"] != item["value"] + 1
        for item in limits
    ):
        raise ValueError("boundaries")
    by_id = {item["id"]: item for item in limits}
    if (
        by_id["successful_parent_total_ns"]["value"] != 1_000_000_000
        or by_id["spi_max_word_size_bits"]["value"] != 8
    ):
        raise ValueError("corrected key limits")
    thresholds = evidence["approved_thresholds"]
    if (
        thresholds["operator_approval_commit"] != "63fdfee87159251cdf525eb608340e6bc08ad010"
        or thresholds["superseded_proposal_commit"] != "395646fa1172382928581d7266723f5b044cf8f2"
        or thresholds["superseded_operator_approval_commit"]
        != "b6d904064ab7b9e195eedded1c55efc306eeb925"
    ):
        raise ValueError("approval identity")
    if set(value["closed_findings"]) != FINDINGS or len(value["closed_findings"]) != len(FINDINGS):
        raise ValueError("findings")
    if value["historical_invalidations_preserved"] != [
        "superseded semantic-fixture candidates and transferred-pass prohibition",
        "superseded preexecution runner and three UART warm-up history",
        "discarded concurrent and pre-write raw collection attempts",
        "failed threshold proposal round 1 and superseded round-2 approval",
        "superseded final-B1 candidate, manifest, and checkpoint after C3B2-IF001",
        "raw verifier round 2 path-provenance finding C3B1-RV001",
    ]:
        raise ValueError("invalidations")
    commands = value["frozen_commands"]
    if (
        len(commands) != 21
        or {item.get("id") for item in commands} != COMMAND_IDS
        or any(
            item.get("cwd") not in {"Software/LogicAnalyzerPy", "Software/LogicAnalyzerPy/web"}
            or not item.get("argv")
            for item in commands
        )
    ):
        raise ValueError("commands")
    if value["pytest_applicability"] != {
        "selected": 635,
        "deselected_historical": 2,
        "ignored_historical_modules": 4,
        "classification_record": (
            "docs/reviews/"
            "c3-b1-threshold-proposal-accumulated-validation-round-3.md"
        ),
    }:
        raise ValueError("applicability")
    if set(value["exclusions"]) != EXCLUSIONS or len(value["exclusions"]) != len(EXCLUSIONS):
        raise ValueError("exclusions")


def test_exact_candidate_scope_tree_current_bytes_and_live_history() -> None:
    assert sha(BINDER) == "a46a7b3fc5a684a77990b8f4373f710002411901d2610d1fa30d275e5b07f57c"
    assert sha(REVIEW) == "eb570fe3498232a0a206dc168a5afa0f404eca9dd8d1a173a99e746b6a6af20b"
    assert (
        subprocess.check_output(
            ["git", "rev-parse", f"{CANDIDATE}^{{tree}}"], cwd=REPO, text=True
        ).strip()
        == CANDIDATE_TREE
    )
    changed = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", CANDIDATE], cwd=REPO, text=True
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
        ASSIGNMENT_DESCENDANT,
        binder["governing"]["commit"],
        binder["governing"]["assignment_commit"],
    ]
    for group in binder["evidence"].values():
        commits.extend(v for k, v in group.items() if k.endswith("commit"))
    commits.extend(v for k, v in binder["correction"].items() if k.endswith("commit"))
    commits.extend(
        v
        for k, v in binder["correction"]["preserved_prior_final_binder_correction"].items()
        if k.endswith("commit")
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


def test_review_orders_gates_and_denies_transferred_authority() -> None:
    text = REVIEW.read_text()
    required = [
        "rights-holder or qualified-counsel limitation",
        "round-2 proposal and\napproval are explicitly superseded and confer no authority",
        "superseded B1 manifest/checkpoint supplies no B2 authority",
        "Fresh replacement final-B1 verification, complete accumulated validation,\n"
        "fresh independent acceptance, atomic replacement-manifest assembly, distinct\n"
        "manifest verification, joint manifest/verification commit, and a replacement\n"
        "B1 checkpoint are mandatory in that order",
    ]
    assert all(fragment in text for fragment in required)
    assert (
        "adds no product, fixture,\nrunner, raw, threshold, lock, workflow, manifest, "
        "checkpoint, or B2 byte"
        in text
    )


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "extra",
        "schema",
        "round",
        "status",
        "governing",
        "correction",
        "environment",
        "role-history",
        "role-collapse",
        "digest",
        "evidence-extra",
        "limit-count",
        "approval",
        "finding",
        "invalidation",
        "command-missing",
        "command-extra",
        "applicability",
        "exclusion",
        "authority",
    ],
)
def test_missing_extra_mutation_and_direct_guard_families(mutation: str) -> None:
    value = copy.deepcopy(load(BINDER))
    validate(value)
    if mutation == "missing":
        value.pop("next_gate")
    elif mutation == "extra":
        value["extra"] = True
    elif mutation == "schema":
        value["schema"] += "-mutated"
    elif mutation == "round":
        value["round"] = 2
    elif mutation == "status":
        value["status"] = "accepted"
    elif mutation == "governing":
        value["governing"]["tree"] = "0" * 40
    elif mutation == "correction":
        value["correction"]["finding"] = "C3B1-FV001"
    elif mutation == "environment":
        value["environment"]["architecture"] = "arm64"
    elif mutation == "role-history":
        value["internal_role_map"]["semantic_fixture_implementation"]["ordered_history"].pop()
    elif mutation == "role-collapse":
        value["internal_role_map"]["semantic_fixture_acceptance"]["identity"] = value[
            "internal_role_map"
        ]["semantic_fixture_verification"]["identity"]
    elif mutation == "digest":
        value["evidence"]["raw_baseline"]["requests_sha256"] = "0" * 64
    elif mutation == "evidence-extra":
        value["evidence"]["unexpected"] = {}
    elif mutation == "limit-count":
        value["evidence"]["approved_thresholds"]["limit_count"] = 28
    elif mutation == "approval":
        value["evidence"]["approved_thresholds"]["operator_approval_commit"] = "0" * 40
    elif mutation == "finding":
        value["closed_findings"].pop()
    elif mutation == "invalidation":
        value["historical_invalidations_preserved"].pop()
    elif mutation == "command-missing":
        value["frozen_commands"].pop()
    elif mutation == "command-extra":
        value["frozen_commands"].append(copy.deepcopy(value["frozen_commands"][0]))
    elif mutation == "applicability":
        value["pytest_applicability"]["selected"] = 636
    elif mutation == "exclusion":
        value["exclusions"].pop()
    elif mutation == "authority":
        value["next_gate"] = "B2 implementation"
    with pytest.raises(ValueError):
        validate(value)
