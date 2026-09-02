"""Independent C3-B4 SIGTERM-isolation checks for candidate fefc3307c2de."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

CANDIDATE = "fefc3307c2de0a680bf44cdcbbabf2e804495a4a"
CANDIDATE_TREE = "489ae588679ea4306c49304c0c1e40733b9f7938"
PRIOR_CANDIDATE = "f3565c11c1d7ea4351349d141401c6f98ba3940d"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "9e427b6090f01a2506570246189df20ced8a077b25877d1e57af374e6c0e7805"
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
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_candidate_tree_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_runner_guard_and_every_other_gate_byte_are_preserved"
    ),
    SECOND_NODE,
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_candidate_tree_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_redaction_log_status_and_no_retry_are_byte_preserved"
    ),
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases"
    ),
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_second_sigterm_node_remains_selected_and_passes"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_focused_gate_is_once_no_retry_and_broad_only_on_success"
    ),
)
ROUND6_DISPOSED = {
    "test_candidate_tree_and_workflow_digest_are_exact",
    "test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases",
    "test_runner_guard_and_every_other_gate_byte_are_preserved",
    "test_focused_gate_is_once_no_retry_and_broad_only_on_success",
}
ROUND7_DISPOSED = {
    "test_candidate_tree_and_workflow_digest_are_exact",
    "test_redaction_log_status_and_no_retry_are_byte_preserved",
    "test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases",
    "test_second_sigterm_node_remains_selected_and_passes",
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


def _test_nodes(relative: str) -> set[str]:
    source = (ROOT / relative).read_text(encoding="utf-8")
    return set(re.findall(r"^def (test_[^(]+)\(", source, re.MULTILINE))


def test_candidate_tree_and_workflow_digest_are_exact() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_one_focused_command_runs_exact_ordered_three_cases_under_sigterm_ignore() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    focused = (
        "            .venv/bin/python -m pytest -q \\\n"
        f"              {FORCED_NODE} \\\n"
        f"              {SECOND_NODE} \\\n"
        "              --tb=short --disable-warnings\n"
    )
    assert text.count(focused) == 1
    assert text.count(".venv/bin/python -m pytest -q") == 1
    assert text.count("trap '' TERM") == 1
    assert text.index("trap '' TERM") < text.index(focused)

    command = (
        "trap '' TERM; "
        'exec "$1" -m pytest -q "$2" "$3" --tb=short --disable-warnings'
    )
    run = subprocess.run(
        ["bash", "-c", command, "round8", sys.executable, FORCED_NODE, SECOND_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "3 passed" in run.stdout
    assert run.stderr == ""


def test_broad_only_on_focused_success_and_no_case_executes_twice() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("focused_status=$?") == 1
    assert text.count('if [ "$focused_status" -eq 0 ]; then') == 1
    assert text.count("status=$focused_status") == 1
    assert text.count('if [ "$status" -ne 0 ]; then') == 1
    broad = '.venv/bin/python -m pytest -m "not hardware" --tb=short --disable-warnings'
    assert text.count(broad) == 1
    assert text.index('if [ "$focused_status" -eq 0 ]; then') < text.index(broad)
    assert text.count(FORCED_NODE) == 2
    assert text.count(SECOND_NODE) == 2
    assert text.count(f"--deselect {FORCED_NODE}") == 1
    assert text.count(f"--deselect {SECOND_NODE}") == 1
    assert text.count(" -m pytest ") == 2
    assert "retry:" not in text.lower()
    assert "for attempt" not in text.lower()
    assert "while " not in text.lower()


def test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    restored = current.replace(f"              {SECOND_NODE} \\\n", "")
    for node in DESELECTS[-6:]:
        restored = restored.replace(f"              --deselect {node} \\\n", "")
    assert restored == prior
    assert current.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert current.count('log_file="$(mktemp)"') == 1
    assert current.count('>>"$log_file" 2>&1') == 2
    assert current.count('report="$(sanitize_report "$log_file")"') == 1
    assert current.count('exit "$status"') == 1
    for marker in (
        "<URL_REDACTED>",
        "<PORT_REDACTED>",
        "pico_la_capability=<TOKEN_REDACTED>",
        "<TOKEN_REDACTED>",
    ):
        assert marker in current


def test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert ignores == IGNORES
    assert deselects == DESELECTS
    assert len(ignores) == len(set(ignores)) == 15
    assert len(deselects) == len(set(deselects)) == 17
    assert all((ROOT / item).is_file() for item in ignores)
    assert all((ROOT / node.split("::", 1)[0]).is_file() for node in deselects)
    assert 16 + 2 == 18
    assert DESELECTS[-6:] == (
        SECOND_NODE,
        *DESELECTS[12:16],
        DESELECTS[16],
    )


def test_exact_round6_and_round7_nodes_are_retained() -> None:
    round6 = "tests/verification/test_c3_b4_public_round6.py"
    round7 = "tests/verification/test_c3_b4_public_round7.py"
    round6_nodes = _test_nodes(round6)
    round7_nodes = _test_nodes(round7)
    assert len(round6_nodes) == len(round7_nodes) == 10
    selected_round6 = {
        node.split("::", 1)[1] for node in DESELECTS if node.startswith(f"{round6}::")
    }
    selected_round7 = {
        node.split("::", 1)[1] for node in DESELECTS if node.startswith(f"{round7}::")
    }
    assert selected_round6 == ROUND6_DISPOSED
    assert selected_round7 == ROUND7_DISPOSED
    assert len(round6_nodes - selected_round6) == 6
    assert len(round7_nodes - selected_round7) == 6


def test_every_current_b2_b3_b4_module_remains_unignored() -> None:
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/"
            r"test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 21
    assert "tests/verification/test_c3_b4_public_round7.py" in modules
    ignores, _ = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert modules.isdisjoint(ignores)


def test_v001_v004_hosted_determinism_and_gate_order_remain_structurally_present() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("runs-on: macos-15-intel") == 1
    assert text.count('PYTHONDONTWRITEBYTECODE: "1"') == 1
    assert text.count("fetch-depth: 0") == 1
    assert text.count('architecture="$(uname -m)"') == 1
    assert text.count('if [ "$architecture" != "x86_64" ]; then') == 1
    assert text.index("Verify governed macOS x86_64 runner") < text.index(
        "actions/checkout@v4"
    )
    required = (
        "python -m ruff check .",
        "python -m mypy src",
        "python -m mypy --strict tests/implementation/c3_b4_consumer.py",
        "python -m pico_logic_analyzer decode --help",
        "npm run lint",
        "npm run typecheck",
        "npm test -- --run",
        "npm run build",
        "scripts/check_web_assets.py",
        "npm run test:browser",
    )
    positions = [text.index(item) for item in required]
    assert positions == sorted(positions)


def test_no_product_b2_b3_fixture_limit_threshold_lock_or_manifest_drift() -> None:
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
        "/test_c3_b2_",
        "/test_c3_b3_",
    )
    assert not {path for path in changed if any(part in path for part in prohibited)}
    assert changed == {
        ".github/workflows/logic-analyzer-python-cycle2.yml",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-5.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-8.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-7.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round7.py",
    }
