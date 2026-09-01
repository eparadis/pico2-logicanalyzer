"""Independent C3-B4 hosted-harness checks for candidate db94d6b4a63a."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

CANDIDATE = "db94d6b4a63aefbd1ec185a6492344be3df98842"
CANDIDATE_TREE = "26f3afe065e0202d9289e7ccb4a8fb47a9329a31"
PRIOR_CANDIDATE = "8cd114fa316f10db4d403197f3204771ccd36638"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "2b7c35159c9f6a6b521830290c4c4a4e17a1f7753911dad97c94161084256d82"
FORCED_NODE = (
    "tests/implementation/test_c3_b2_private_host.py::"
    "test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure"
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
    (
        "tests/implementation/test_cycle3_fixtures.py::"
        "test_cycle3_fixture_surface_is_present_and_rebuildable"
    ),
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_candidate_binding_and_exact_workflow_digest"
    ),
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order"
    ),
    FORCED_NODE,
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_candidate_binding_and_exact_workflow_digest"
    ),
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_partition_has_exact_ordered_unique_ignores_and_deselections"
    ),
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_every_candidate_b2_b3_b4_module_is_retained"
    ),
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_partition_is_the_only_workflow_change_from_round4"
    ),
)
ROUND5_STALE = {
    "test_candidate_binding_and_exact_workflow_digest",
    "test_partition_has_exact_ordered_unique_ignores_and_deselections",
    "test_every_candidate_b2_b3_b4_module_is_retained",
    "test_partition_is_the_only_workflow_change_from_round4",
}
ROUND5_RETAINED = {
    "test_all_remaining_round4_behavior_and_scope_nodes_are_retained",
    "test_runner_guard_remains_first_and_prebootstrap",
    "test_no_product_fixture_limit_threshold_manifest_or_lock_drift",
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


def test_candidate_tree_and_workflow_digest_are_exact() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_full_history_checkout_and_job_wide_no_bytecode_precede_python_steps() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    job_header = (
        "  validate:\n"
        "    runs-on: macos-15-intel\n"
        "    env:\n"
        '      PYTHONDONTWRITEBYTECODE: "1"\n'
        "    steps:\n"
    )
    checkout = (
        "      - uses: actions/checkout@v4\n"
        "        with:\n"
        "          fetch-depth: 0\n"
    )
    assert text.count(job_header) == 1
    assert text.count(checkout) == 1
    assert text.index(job_header) < text.index(checkout) < text.index("actions/setup-python@v5")
    assert text.index(job_header) < text.index("run: python -m venv .venv")


def test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert ignores == IGNORES
    assert deselects == DESELECTS
    assert len(ignores) == len(set(ignores)) == 15
    assert len(deselects) == len(set(deselects)) == 8
    assert all((ROOT / item).is_file() for item in ignores)
    assert all((ROOT / node.split("::", 1)[0]).is_file() for node in deselects)
    source = (ROOT / FORCED_NODE.split("::", 1)[0]).read_text(encoding="utf-8")
    parametrization = (
        '@pytest.mark.parametrize("cancelled", [False, True], '
        'ids=("timeout", "cancelled"))'
    )
    assert parametrization in source
    assert 7 + 2 == 9


def test_focused_forced_kill_runs_once_with_inherited_sigterm_ignore() -> None:
    command = (
        "trap '' TERM; "
        'exec "$1" -m pytest -q "$2" --tb=short --disable-warnings'
    )
    run = subprocess.run(
        ["bash", "-c", command, "round6", sys.executable, FORCED_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "2 passed" in run.stdout
    assert run.stderr == ""


def test_focused_gate_is_once_no_retry_and_broad_only_on_success() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    focused_command = (
        "            .venv/bin/python -m pytest -q \\\n"
        f"              {FORCED_NODE} \\\n"
        "              --tb=short --disable-warnings\n"
    )
    assert text.count(focused_command) == 1
    assert text.count(f"--deselect {FORCED_NODE}") == 1
    assert text.count(FORCED_NODE) == 2
    assert text.count("trap '' TERM") == 1
    assert text.count("focused_status=$?") == 1
    assert text.count('if [ "$focused_status" -eq 0 ]; then') == 1
    assert text.count("status=$focused_status") == 1
    broad = '.venv/bin/python -m pytest -m "not hardware" --tb=short --disable-warnings'
    assert text.count(broad) == 1
    assert text.index('if [ "$focused_status" -eq 0 ]; then') < text.index(broad)
    assert text.index(broad) < text.index("else\n            status=$focused_status")
    assert "retry" not in text.lower()


def test_focused_and_broad_share_one_bounded_sanitized_log_and_status() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count('log_file="$(mktemp)"') == 1
    assert text.count(': >"$log_file"') == 1
    assert text.count('>>"$log_file" 2>&1') == 2
    assert text.count('report="$(sanitize_report "$log_file")"') == 1
    assert text.count('printf \'%s\\n\' "$report"') == 1
    assert text.count('if [ "$status" -ne 0 ]; then') == 1
    assert text.count('exit "$status"') == 1
    focused = text.index(') >>"$log_file" 2>&1')
    broad = text.index('>>"$log_file" 2>&1', focused + 1)
    report = text.index('report="$(sanitize_report "$log_file")"')
    assert focused < broad < report < text.index('exit "$status"')


def test_only_four_round5_identity_nodes_are_disposed() -> None:
    source = (ROOT / "tests/verification/test_c3_b4_public_round5.py").read_text(
        encoding="utf-8"
    )
    nodes = set(re.findall(r"^def (test_[^(]+)\(", source, re.MULTILINE))
    assert nodes == ROUND5_STALE | ROUND5_RETAINED
    selected_round5 = {
        node.split("::", 1)[1]
        for node in DESELECTS
        if node.startswith("tests/verification/test_c3_b4_public_round5.py::")
    }
    assert selected_round5 == ROUND5_STALE
    assert nodes - selected_round5 == ROUND5_RETAINED


def test_every_current_candidate_b2_b3_b4_module_remains_unignored() -> None:
    candidate_modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/"
            r"test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(candidate_modules) == 19
    assert "tests/verification/test_c3_b4_public_round5.py" in candidate_modules
    ignores, _ = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert candidate_modules.isdisjoint(ignores)


def test_runner_guard_and_every_other_gate_byte_are_preserved() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    assert current.count("runs-on: macos-15-intel") == 1
    assert current.count('architecture="$(uname -m)"') == 1
    assert current.count('if [ "$architecture" != "x86_64" ]; then') == 1
    assert current.index("Verify governed macOS x86_64 runner") < current.index(
        "actions/checkout@v4"
    )

    restored = current.replace(
        "    env:\n" '      PYTHONDONTWRITEBYTECODE: "1"\n', ""
    ).replace(
        "      - uses: actions/checkout@v4\n"
        "        with:\n"
        "          fetch-depth: 0\n",
        "      - uses: actions/checkout@v4\n",
    )
    current_start = restored.index("          set +e\n")
    current_end = restored.index("          set -e\n", current_start) + len(
        "          set -e\n"
    )
    prior_start = prior.index("          set +e\n")
    prior_end = prior.index("          set -e\n", prior_start) + len("          set -e\n")
    restored = restored[:current_start] + prior[prior_start:prior_end] + restored[current_end:]
    assert restored == prior


def test_no_product_fixture_limit_threshold_lock_or_manifest_drift() -> None:
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
    )
    assert not {path for path in changed if any(part in path for part in prohibited)}
    assert changed == {
        ".github/workflows/logic-analyzer-python-cycle2.yml",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-3.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-6.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-5.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round5.py",
    }
