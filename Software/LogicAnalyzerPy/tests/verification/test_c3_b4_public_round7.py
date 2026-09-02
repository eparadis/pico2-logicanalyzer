"""Independent C3-B4 hosted-diagnostic checks for candidate f3565c11c1d."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

CANDIDATE = "f3565c11c1d7ea4351349d141401c6f98ba3940d"
CANDIDATE_TREE = "e0346acdcc6ea64369ba612237eb583e66311bf8"
PRIOR_CANDIDATE = "db94d6b4a63aefbd1ec185a6492344be3df98842"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "7b74489c4f540a8e1a5281ae642fd77b6f8a00b403346287c40480ee49655576"
ANNOTATION_PREFIX = "::error title=Cycle 3 non-hardware pytest failure::"
FORCED_NODE = (
    "tests/implementation/test_c3_b2_private_host.py::"
    "test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure"
)
SECOND_SIGTERM_NODE = (
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
)
ROUND6_STALE = {
    "test_candidate_tree_and_workflow_digest_are_exact",
    "test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases",
    "test_runner_guard_and_every_other_gate_byte_are_preserved",
}
ROUND6_RETAINED = {
    "test_full_history_checkout_and_job_wide_no_bytecode_precede_python_steps",
    "test_focused_forced_kill_runs_once_with_inherited_sigterm_ignore",
    "test_focused_gate_is_once_no_retry_and_broad_only_on_success",
    "test_focused_and_broad_share_one_bounded_sanitized_log_and_status",
    "test_only_four_round5_identity_nodes_are_disposed",
    "test_every_current_candidate_b2_b3_b4_module_remains_unignored",
    "test_no_product_fixture_limit_threshold_lock_or_manifest_drift",
}
SANITIZE_SCRIPT = r"""LC_ALL=C tail -c 1300 | LC_ALL=C tr -cd '\11\12\15\40-\176' | sed -E \
  -e 's#https?://[^[:space:]]+#<URL_REDACTED>#g' \
  -e 's#/dev/(tty|cu\.|serial/)[^[:space:]]*#<PORT_REDACTED>#g' \
  -e 's#/(Users|home)/[^[:space:]]*#<PATH_REDACTED>#g' \
  -e 's#pico_la_capability=[^;[:space:]]+#pico_la_capability=<TOKEN_REDACTED>#g' \
  -e 's#(^|[^[:alnum:]_-])[[:alnum:]_-]{43}([^[:alnum:]_-]|$)#\1<TOKEN_REDACTED>\2#g'
"""


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


def _sanitize(raw: bytes) -> bytes:
    return subprocess.run(
        ["bash", "-c", SANITIZE_SCRIPT],
        input=raw,
        capture_output=True,
        check=True,
    ).stdout


def test_candidate_tree_and_workflow_digest_are_exact() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_exact_raw_tail_and_worst_permitted_byte_annotation_are_bounded() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert "tail -c 12000" not in text
    report = _sanitize(b"discarded" * 200 + b"%" * 1300)
    assert report == b"%" * 1300

    escape_script = r"""report="$1"
annotation=${report//%/%25}
annotation=${annotation//$'\r'/%0D}
annotation=${annotation//$'\n'/%0A}
printf '::error title=Cycle 3 non-hardware pytest failure::%s\n' "$annotation"
"""
    wrapped = subprocess.run(
        ["bash", "-c", escape_script, "round7", report.decode("ascii")],
        capture_output=True,
        check=True,
    ).stdout
    assert len(ANNOTATION_PREFIX.encode("ascii")) == 51
    assert len(wrapped) == 3952
    assert len(wrapped) <= 4096
    assert wrapped == ANNOTATION_PREFIX.encode("ascii") + b"%25" * 1300 + b"\n"

    permitted = ["\t", "\n", "\r", *(chr(value) for value in range(32, 127))]
    escaped_lengths = {
        value: len(value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A"))
        for value in permitted
    }
    assert max(escaped_lengths.values()) == 3
    assert {value for value, size in escaped_lengths.items() if size == 3} == {
        "%",
        "\r",
        "\n",
    }


def test_real_pytest_failure_suffix_survives_raw_byte_tail(tmp_path: Path) -> None:
    failing = tmp_path / "test_real_failure_suffix.py"
    failing.write_text(
        "def test_real_failure_suffix():\n"
        "    raise AssertionError('round7-real-suffix')\n",
        encoding="utf-8",
    )
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", failing.name],
        cwd=tmp_path,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 1
    report = _sanitize(b"discarded progress\n" * 200 + run.stdout + run.stderr)
    assert b"FAILED test_real_failure_suffix.py::test_real_failure_suffix" in report
    assert b"AssertionError: round7-real-suffix" in report
    assert re.search(rb"1 failed in [0-9.]+s\n$", report)


def test_redaction_log_status_and_no_retry_are_byte_preserved() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    restored = current.replace('tail -c 1300 "$1"', 'tail -c 12000 "$1"')
    for node in DESELECTS[-3:]:
        restored = restored.replace(f"              --deselect {node} \\\n", "")
    assert restored == prior
    assert current.count('log_file="$(mktemp)"') == 1
    assert current.count('>>"$log_file" 2>&1') == 2
    assert current.count('report="$(sanitize_report "$log_file")"') == 1
    assert current.count("focused_status=$?") == 1
    assert current.count('if [ "$focused_status" -eq 0 ]; then') == 1
    assert current.count('exit "$status"') == 1
    assert "retry" not in current.lower()


def test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert ignores == IGNORES
    assert deselects == DESELECTS
    assert len(ignores) == len(set(ignores)) == 15
    assert len(deselects) == len(set(deselects)) == 11
    assert all((ROOT / item).is_file() for item in ignores)
    assert all((ROOT / node.split("::", 1)[0]).is_file() for node in deselects)
    assert 10 + 2 == 12


def test_only_three_round6_identity_nodes_are_disposed() -> None:
    source = (ROOT / "tests/verification/test_c3_b4_public_round6.py").read_text(
        encoding="utf-8"
    )
    nodes = set(re.findall(r"^def (test_[^(]+)\(", source, re.MULTILINE))
    assert nodes == ROUND6_STALE | ROUND6_RETAINED
    disposed = {
        node.split("::", 1)[1]
        for node in DESELECTS
        if node.startswith("tests/verification/test_c3_b4_public_round6.py::")
    }
    assert disposed == ROUND6_STALE
    assert nodes - disposed == ROUND6_RETAINED


def test_second_sigterm_node_remains_selected_and_passes() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert SECOND_SIGTERM_NODE not in deselects
    assert SECOND_SIGTERM_NODE.split("::", 1)[0] not in ignores
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", SECOND_SIGTERM_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "1 passed" in run.stdout
    assert run.stderr == ""


def test_all_current_b2_b3_b4_modules_remain_unignored() -> None:
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/"
            r"test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 20
    assert "tests/verification/test_c3_b4_public_round6.py" in modules
    ignores, _ = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert modules.isdisjoint(ignores)


def test_prior_hosted_determinism_and_gate_order_are_preserved() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("runs-on: macos-15-intel") == 1
    assert text.count('PYTHONDONTWRITEBYTECODE: "1"') == 1
    assert text.count("fetch-depth: 0") == 1
    assert text.count('architecture="$(uname -m)"') == 1
    assert text.count('if [ "$architecture" != "x86_64" ]; then') == 1
    assert text.index("Verify governed macOS x86_64 runner") < text.index(
        "actions/checkout@v4"
    )
    assert text.count("trap '' TERM") == 1
    assert text.count(FORCED_NODE) == 2
    assert text.index("trap '' TERM") < text.index(
        '.venv/bin/python -m pytest -m "not hardware"'
    )


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
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-4.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-7.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-6.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round6.py",
    }
