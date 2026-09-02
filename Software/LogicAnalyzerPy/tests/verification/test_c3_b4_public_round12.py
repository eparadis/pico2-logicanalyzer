"""Independent C3-B4 hosted-failure checks for candidate c7650876544e."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

CANDIDATE = "c7650876544e477c277200c4f2fcbd23c67fe245"
CANDIDATE_TREE = "87e36568aae7fe0cc55cfc1f584cc8b025c52769"
PRIOR_CANDIDATE = "fb2f4d63df41f7d5d0c2253c59f02803dac14a55"
FAILED_VERIFIER = "773460d980349d6449cb2f522558ad2f03808f9a"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990"
ARTIFACT_NODE = (
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_downloaded_artifact_hash_size_layout_and_runtime_are_exact"
)
DEADLINE_NODE = (
    "tests/implementation/test_cycle3_preexecution_runner.py::"
    "test_small_private_deadline_is_enforced_by_an_actual_child"
)
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
FOCUSED_COMMAND = (
    "trap '' TERM; "
    'exec "$1" -m pytest -q "$2" "$3" --tb=short --disable-warnings'
)
ARCHIVE = REPOSITORY / (
    ".tmp/c3-b4-ci/round11/"
    "cpython-3.12.13+20260623-x86_64-apple-darwin-install_only_stripped.tar.gz"
)
ARTIFACT_PYTHON = REPOSITORY / ".tmp/c3-b4-ci/round11/python-root/bin/python3.12"
NEW_DESELECTS = (
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_both_venvs_originate_from_managed_python_and_reverify",
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_candidate_tree_and_workflow_digest_are_exact",
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_partition_is_exact_fifteen_ignores_thirty_two_selectors_thirty_three_cases",
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_only_six_stale_round10_nodes_are_disposed_and_all_modules_remain",
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_candidate_qualified_collection_is_exact",
)


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments], cwd=REPOSITORY, capture_output=True, check=True, text=True
    ).stdout


def _partition(text: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    return (
        tuple(re.findall(r"--ignore ([^\s\\]+)", text)),
        tuple(re.findall(r"--deselect ([^\s\\]+)", text)),
    )


def _pytest(node: str, environment: dict[str, str | None]) -> subprocess.CompletedProcess[str]:
    script = "import os; " + "; ".join(
        (
            f"os.environ.pop({key!r}, None)"
            if value is None
            else f"os.environ[{key!r}]={value!r}"
        )
        for key, value in environment.items()
    )
    script += f"; import pytest; raise SystemExit(pytest.main(['-q', {node!r}]))"
    return subprocess.run(
        [sys.executable, "-c", script], cwd=ROOT, capture_output=True, check=False, text=True
    )


def test_candidate_tree_failed_verifier_and_workflow_digest_are_exact() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert _git("cat-file", "-t", FAILED_VERIFIER).strip() == "commit"
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_actual_hang_keeps_200ms_deadline_and_recovery_uses_default_profile() -> None:
    source = (ROOT / "tests/implementation/test_cycle3_preexecution_runner.py").read_text()
    block = (
        'profile = private_test_profile({"wall_deadline_ms": 200, '
        '"terminate_grace_ms": 20})\n'
        "    with pytest.raises(RunnerFailure):\n"
        '        run_internal_probe("hang", _profile=profile)\n'
        '    assert run_internal_probe("valid").value["version"] == 1\n'
    )
    assert source.count(block) == 1
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", DEADLINE_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout


def test_artifact_present_branch_uses_hosted_environment_and_passes() -> None:
    assert ARCHIVE.is_file() and ARTIFACT_PYTHON.is_file()
    result = _pytest(
        ARTIFACT_NODE,
        {
            "PICO_LA_PYTHON_ARCHIVE": str(ARCHIVE),
            "PICO_LA_PYTHON": str(ARTIFACT_PYTHON),
        },
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout and "skipped" not in result.stdout


def test_artifact_absent_branch_is_one_classified_skip() -> None:
    result = _pytest(
        ARTIFACT_NODE, {"PICO_LA_PYTHON_ARCHIVE": None, "PICO_LA_PYTHON": None}
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 skipped" in result.stdout
    assert "workflow-provisioned artifact is unavailable" in result.stdout


def test_partial_artifact_environment_fails_closed() -> None:
    for environment in (
        {"PICO_LA_PYTHON_ARCHIVE": str(ARCHIVE), "PICO_LA_PYTHON": None},
        {"PICO_LA_PYTHON_ARCHIVE": None, "PICO_LA_PYTHON": str(ARTIFACT_PYTHON)},
    ):
        result = _pytest(ARTIFACT_NODE, environment)
        assert result.returncode == 1
        assert "1 failed" in result.stdout
        assert "skipped" not in result.stdout


def test_partition_is_exact_fifteen_ignores_thirty_seven_selectors_thirty_eight_cases() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    prior_ignores, prior_deselects = _partition(prior)
    ignores, deselects = _partition(current)
    assert ignores == prior_ignores
    assert len(ignores) == len(set(ignores)) == 15
    assert len(prior_deselects) == len(set(prior_deselects)) == 32
    assert deselects == (*prior_deselects, *NEW_DESELECTS)
    assert len(deselects) == len(set(deselects)) == 37
    assert 36 + 2 == 38


def test_exact_stale_nodes_only_and_all_current_modules_remain() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert deselects[-5:] == NEW_DESELECTS
    round11 = ROOT / "tests/verification/test_c3_b4_public_round11.py"
    nodes = set(re.findall(r"^def (test_[^(]+)\(", round11.read_text(), re.MULTILINE))
    disposed = {
        node.split("::", 1)[1]
        for node in deselects
        if node.startswith("tests/verification/test_c3_b4_public_round11.py::")
    }
    assert len(nodes) == 10 and len(disposed) == 4 and len(nodes - disposed) == 6
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 25
    assert modules.isdisjoint(ignores)


def test_raw_b1_focused_and_hosted_guards_remain_green() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    ignores, deselects = _partition(text)
    assert RAW_B1_NODE not in deselects
    assert RAW_B1_NODE.split("::", 1)[0] not in ignores
    raw = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", RAW_B1_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert raw.returncode == 0, raw.stdout + raw.stderr
    assert "1 passed" in raw.stdout
    focused = subprocess.run(
        [
            "/bin/sh",
            "-c",
            FOCUSED_COMMAND,
            "round12",
            sys.executable,
            FORCED_NODE,
            SECOND_NODE,
        ],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert focused.returncode == 0, focused.stdout + focused.stderr
    assert "3 passed" in focused.stdout
    assert text.count('node-version: "22.14.0"') == 1
    assert text.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert text.count("fetch-depth: 0") == 1
    assert text.count('PYTHONDONTWRITEBYTECODE: "1"') == 1
    assert text.index("Verify governed macOS x86_64 runner") < text.index("actions/checkout@v4")


def test_candidate_qualified_collection_is_exact() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    command = [sys.executable, "-m", "pytest", "--collect-only", "-q", "-m", "not hardware"]
    for ignored in (*ignores, "tests/verification/test_c3_b4_public_round12.py"):
        command.extend(("--ignore", ignored))
    for node in deselects:
        command.extend(("--deselect", node))
    result = subprocess.run(
        command, cwd=ROOT, capture_output=True, check=False, text=True
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1460/1498 tests collected (38 deselected)" in result.stdout


def test_no_product_b1_b2_b3_fixture_limit_threshold_lock_or_manifest_drift() -> None:
    changed = set(_git("diff", "--name-only", f"{PRIOR_CANDIDATE}..{CANDIDATE}").splitlines())
    assert changed == {
        ".github/workflows/logic-analyzer-python-cycle2.yml",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-12.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-11.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle3_preexecution_runner.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round11.py",
    }
    prohibited = (
        "/src/",
        "/testdata/",
        "/fixtures/",
        "/requirements-dev.lock",
        "/requirements-web.lock",
        "/pyproject.toml",
        "/package-lock.json",
        "/test_c3_b1_",
        "/test_c3_b2_",
        "/test_c3_b3_",
    )
    assert not {path for path in changed if any(part in path for part in prohibited)}
