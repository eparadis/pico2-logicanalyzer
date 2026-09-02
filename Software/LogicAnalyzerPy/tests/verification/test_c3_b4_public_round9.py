"""Independent C3-B4 exact-Python checks for candidate 3b8de59f8fc5."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

CANDIDATE = "3b8de59f8fc5276a92d5ea5fef5b48b259374a52"
CANDIDATE_TREE = "aee4e77238ce2dfd8d311b47873dfe3ebb21d4d6"
PRIOR_CANDIDATE = "fefc3307c2de0a680bf44cdcbbabf2e804495a4a"
FAILED_EVIDENCE = "5cc615044c0bcaac6f640e5decc74503025745f3"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "b25d28ae03bc203dccc819d90aca8f76199e2b034e5b5e7b94575e2ed4a64a84"
RAW_ENVIRONMENT = ROOT / "testdata/decoders/cycle3-raw/environment.json"
RAW_B1_NODE = (
    "tests/verification/test_c3_b1_raw_baseline_candidate_replacement.py::"
    "test_candidate_identity_digest_environment_schema_and_summary_arithmetic"
)
FORCED_NODE = (
    "tests/implementation/test_c3_b2_private_host.py::"
    "test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure"
)
SECOND_NODE = (
    "tests/verification/test_c3_b2_private_host_round3.py::"
    "test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation"
)
IGNORES = (
    "tests/verification/test_c3_b1_threshold_proposal_round2.py",
    "tests/verification/test_c3_b1_final_candidate.py",
    "tests/verification/test_c3_b1_raw_baseline_candidate.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding.py",
    "tests/verification/test_c3_b1_semantic_fixture_candidate.py",
    "tests/verification/test_c3_b1_threshold_proposal_round3.py",
    "tests/verification/test_c3_b1_preexecution_runner_candidate.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py",
    "tests/verification/test_c3_b1_final_candidate_round3.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py",
    "tests/verification/test_c3_b1_semantic_fixture_correction_round2.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round2.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round3.py",
    "tests/verification/test_c3_b1_threshold_proposal.py",
    "tests/verification/test_c3_b1_semantic_fixture_correction.py",
)
DESELECTS = (
    "tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable",
    "tests/verification/test_c3_b4_public_round4.py::test_candidate_binding_and_exact_workflow_digest",
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order"
    ),
    FORCED_NODE,
    "tests/verification/test_c3_b4_public_round5.py::test_candidate_binding_and_exact_workflow_digest",
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_partition_has_exact_ordered_unique_ignores_and_deselections"
    ),
    "tests/verification/test_c3_b4_public_round5.py::test_every_candidate_b2_b3_b4_module_is_retained",
    "tests/verification/test_c3_b4_public_round5.py::test_partition_is_the_only_workflow_change_from_round4",
    "tests/verification/test_c3_b4_public_round6.py::test_candidate_tree_and_workflow_digest_are_exact",
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases"
    ),
    "tests/verification/test_c3_b4_public_round6.py::test_runner_guard_and_every_other_gate_byte_are_preserved",
    SECOND_NODE,
    "tests/verification/test_c3_b4_public_round7.py::test_candidate_tree_and_workflow_digest_are_exact",
    "tests/verification/test_c3_b4_public_round7.py::test_redaction_log_status_and_no_retry_are_byte_preserved",
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases"
    ),
    "tests/verification/test_c3_b4_public_round7.py::test_second_sigterm_node_remains_selected_and_passes",
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_focused_gate_is_once_no_retry_and_broad_only_on_success"
    ),
    "tests/verification/test_c3_b4_public_round8.py::test_candidate_tree_and_workflow_digest_are_exact",
    (
        "tests/verification/test_c3_b4_public_round8.py::"
        "test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged"
    ),
    (
        "tests/verification/test_c3_b4_public_round8.py::"
        "test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases"
    ),
)
ROUND8_DISPOSED = {
    "test_candidate_tree_and_workflow_digest_are_exact",
    "test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged",
    "test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases",
}


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=REPOSITORY,
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def _partition(text: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    return (
        tuple(re.findall(r"--ignore ([^\s\\]+)", text)),
        tuple(re.findall(r"--deselect ([^\s\\]+)", text)),
    )


def test_candidate_tree_failed_evidence_and_workflow_digest_are_exact() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert _git("rev-parse", "5cc6150^{commit}").strip() == FAILED_EVIDENCE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_setup_python_is_exact_31213_once_before_both_clean_environments() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    setup = (
        "      - uses: actions/setup-python@v5\n"
        '        with: {python-version: "3.12.13"}\n'
    )
    assert text.count("actions/setup-python@v5") == 1
    assert text.count(setup) == 1
    assert 'python-version: "3.12"' not in text
    assert text.index(setup) < text.index("run: python -m venv .venv")
    assert text.index(setup) < text.index("run: python -m venv .venv-web")


def test_accepted_raw_b1_replacement_is_selected_and_matches_exact_runtime() -> None:
    environment = json.loads(RAW_ENVIRONMENT.read_text(encoding="utf-8"))
    expected = environment["python"]["version"]
    assert sys.version_info[:3] == (3, 12, 13)
    assert sys.version == expected
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert RAW_B1_NODE not in deselects
    assert RAW_B1_NODE.split("::", 1)[0] not in ignores
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", RAW_B1_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "1 passed" in run.stdout
    assert run.stderr == ""


def test_node_2214_and_exact_focused_three_case_command_are_unchanged() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count('node-version: "22.14.0"') == 1
    focused = (
        "            .venv/bin/python -m pytest -q \\\n"
        f"              {FORCED_NODE} \\\n"
        f"              {SECOND_NODE} \\\n"
        "              --tb=short --disable-warnings\n"
    )
    assert text.count(focused) == 1
    command = (
        "trap '' TERM; "
        'exec "$1" -m pytest -q "$2" "$3" --tb=short --disable-warnings'
    )
    run = subprocess.run(
        ["bash", "-c", command, "round9", sys.executable, FORCED_NODE, SECOND_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "3 passed" in run.stdout
    assert run.stderr == ""


def test_only_python_pin_and_three_round8_selectors_change_workflow_bytes() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    restored = current.replace('python-version: "3.12.13"', 'python-version: "3.12"')
    for node in DESELECTS[-3:]:
        restored = restored.replace(f"              --deselect {node} \\\n", "")
    assert restored == prior


def test_partition_is_exact_ordered_twenty_selectors_twenty_one_cases() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert ignores == IGNORES
    assert deselects == DESELECTS
    assert len(ignores) == len(set(ignores)) == 15
    assert len(deselects) == len(set(deselects)) == 20
    assert all((ROOT / item).is_file() for item in ignores)
    assert all((ROOT / node.split("::", 1)[0]).is_file() for node in deselects)
    assert 19 + 2 == 21


def test_only_three_round8_identity_nodes_are_disposed_and_six_retained() -> None:
    relative = "tests/verification/test_c3_b4_public_round8.py"
    source = (ROOT / relative).read_text(encoding="utf-8")
    nodes = set(re.findall(r"^def (test_[^(]+)\(", source, re.MULTILINE))
    disposed = {
        node.split("::", 1)[1] for node in DESELECTS if node.startswith(f"{relative}::")
    }
    assert len(nodes) == 9
    assert disposed == ROUND8_DISPOSED
    assert len(nodes - disposed) == 6


def test_all_current_b2_b3_b4_modules_are_unignored_and_prior_gates_remain() -> None:
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/"
            r"test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 22
    assert "tests/verification/test_c3_b4_public_round8.py" in modules
    ignores, _ = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert modules.isdisjoint(ignores)

    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("runs-on: macos-15-intel") == 1
    assert text.count("fetch-depth: 0") == 1
    assert text.count('PYTHONDONTWRITEBYTECODE: "1"') == 1
    assert text.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert text.count("trap '' TERM") == 1
    assert text.index("Verify governed macOS x86_64 runner") < text.index(
        "actions/checkout@v4"
    )
    assert text.count(FORCED_NODE) == text.count(SECOND_NODE) == 2
    assert text.count(" -m pytest ") == 2


def test_no_product_b1_b2_b3_fixture_limit_threshold_lock_or_manifest_drift() -> None:
    changed = set(_git("diff", "--name-only", f"{PRIOR_CANDIDATE}..{CANDIDATE}").splitlines())
    prohibited = (
        "/src/",
        "/testdata/",
        "/fixtures/",
        "/requirements-dev.in",
        "/requirements-dev.lock",
        "/requirements-web.in",
        "/requirements-web.lock",
        "/pyproject.toml",
        "/package-lock.json",
        "/test_c3_b1_",
        "/test_c3_b2_",
        "/test_c3_b3_",
    )
    assert not {path for path in changed if any(part in path for part in prohibited)}
    assert changed == {
        ".github/workflows/logic-analyzer-python-cycle2.yml",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-6.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-9.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-8.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round8.py",
    }
