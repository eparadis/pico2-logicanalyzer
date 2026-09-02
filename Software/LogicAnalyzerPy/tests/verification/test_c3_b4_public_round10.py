"""Independent C3-B4 managed-Python checks for candidate ab6744c3263b."""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

CANDIDATE = "ab6744c3263b504e1b4006ece64be12962ce8b47"
CANDIDATE_TREE = "7450014af13a8d61120de078d2c1c7d730f70c39"
PRIOR_CANDIDATE = "3b8de59f8fc5276a92d5ea5fef5b48b259374a52"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "f5b2a05ba66d54944e624ee0c6777f39d4cffc8a5aa3bf719086a1f1b28d5cc8"
SETUP_UV_COMMIT = "c771a70e6277c0a99b617c7a806ffedaca235ff9"
EXPECTED_VERSION = "3.12.13 (main, Jun 23 2026, 15:54:40) [Clang 22.1.3 ]"
MANAGED_KEY = "cpython-3.12.13-macos-x86_64-none"
MANAGED_PYTHON = Path(
    "/Users/ed/.local/share/uv/python/cpython-3.12.13-macos-x86_64-none/"
    "bin/python3.12"
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
NEW_DESELECTS = (
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_official_intel_label_and_guard_are_first_and_prebootstrap"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_full_history_checkout_and_job_wide_no_bytecode_precede_python_steps"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_candidate_tree_failed_evidence_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_setup_python_is_exact_31213_once_before_both_clean_environments"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_only_python_pin_and_three_round8_selectors_change_workflow_bytes"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_partition_is_exact_ordered_twenty_selectors_twenty_one_cases"
    ),
)
ROUND9_DISPOSED = {
    "test_candidate_tree_failed_evidence_and_workflow_digest_are_exact",
    "test_setup_python_is_exact_31213_once_before_both_clean_environments",
    "test_only_python_pin_and_three_round8_selectors_change_workflow_bytes",
    "test_partition_is_exact_ordered_twenty_selectors_twenty_one_cases",
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


def test_setup_uv_is_immutable_v9_exact_0126_and_cache_disabled() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    block = (
        f"      - uses: astral-sh/setup-uv@{SETUP_UV_COMMIT} # v9.0.0\n"
        "        with:\n"
        '          version: "0.12.6"\n'
        "          enable-cache: false\n"
    )
    assert len(SETUP_UV_COMMIT) == 40
    int(SETUP_UV_COMMIT, 16)
    assert text.count(block) == 1
    assert text.count("astral-sh/setup-uv@") == 1
    assert "actions/setup-python" not in text
    assert "python-version:" not in text
    version = subprocess.run(
        ["uv", "--version"], capture_output=True, check=True, text=True
    ).stdout.strip()
    assert version.startswith("uv 0.12.6 ")


def test_cache_install_and_managed_interpreter_paths_are_repo_ignored() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("UV_CACHE_DIR: ${{ github.workspace }}/.tmp/c3-b4-ci/uv-cache") == 1
    assert text.count(
        "UV_PYTHON_INSTALL_DIR: ${{ github.workspace }}/.tmp/c3-b4-ci/uv-python"
    ) == 1
    expected_python = (
        "PICO_LA_PYTHON: ${{ github.workspace }}/.tmp/c3-b4-ci/uv-python/"
        f"{MANAGED_KEY}/bin/python3.12"
    )
    assert text.count(expected_python) == 1
    ignored = _git("check-ignore", ".tmp/c3-b4-ci/uv-cache/probe")
    assert ignored.strip() == ".tmp/c3-b4-ci/uv-cache/probe"


def test_exact_managed_identity_guard_precedes_dependencies() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    expected = f'PICO_LA_EXPECTED_PYTHON: "{EXPECTED_VERSION}"'
    assert text.count(expected) == 1
    assert text.count("uv python install 3.12.13 --no-bin") == 1
    for fragment in (
        'assert sys.version == os.environ["PICO_LA_EXPECTED_PYTHON"]',
        'assert platform.machine() == "x86_64"',
        f'assert sys.base_prefix.endswith("/{MANAGED_KEY}")',
        'assert (Path(sys.base_prefix) / "BUILD").read_text() == "20260623"',
    ):
        assert fragment in text
    guard = text.index('"$PICO_LA_PYTHON" -c')
    assert guard < text.index("actions/setup-node@v4")
    assert guard < text.index("pip install --require-hashes -r requirements-dev.lock")

    run = subprocess.run(
        [
            str(MANAGED_PYTHON),
            "-c",
            (
                "import platform,sys; from pathlib import Path; "
                f"assert sys.version == {EXPECTED_VERSION!r}; "
                "assert platform.machine() == 'x86_64'; "
                f"assert sys.base_prefix.endswith('/{MANAGED_KEY}'); "
                "assert (Path(sys.base_prefix)/'BUILD').read_text() == '20260623'"
            ),
        ],
        capture_output=True,
        check=False,
        text=True,
    )
    assert run.returncode == 0, run.stdout + run.stderr


def test_both_venvs_originate_from_managed_python_and_reverify(tmp_path: Path) -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines()]
    assert lines.count('"$PICO_LA_PYTHON" -m venv .venv') == 1
    assert lines.count('"$PICO_LA_PYTHON" -m venv .venv-web') == 1
    recheck = (
        " -c 'import os, platform, sys; "
        'assert sys.version == os.environ["PICO_LA_EXPECTED_PYTHON"]; '
        'assert platform.machine() == "x86_64"\''
    )
    assert lines.count(f".venv/bin/python{recheck}") == 1
    assert lines.count(f".venv-web/bin/python{recheck}") == 1
    for name in ("core", "web"):
        environment = tmp_path / name
        create = subprocess.run(
            [str(MANAGED_PYTHON), "-m", "venv", environment],
            capture_output=True,
            check=False,
            text=True,
        )
        assert create.returncode == 0, create.stdout + create.stderr
        check = subprocess.run(
            [
                str(environment / "bin/python"),
                "-c",
                (
                    "import platform,sys; "
                    f"assert sys.version == {EXPECTED_VERSION!r}; "
                    "assert platform.machine() == 'x86_64'; "
                    f"assert sys.base_prefix.endswith('/{MANAGED_KEY}')"
                ),
            ],
            capture_output=True,
            check=False,
            text=True,
        )
        assert check.returncode == 0, check.stdout + check.stderr


def test_raw_b1_focused_three_and_prior_hosted_guards_remain_green() -> None:
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

    command = (
        "trap '' TERM; "
        'exec "$1" -m pytest -q "$2" "$3" --tb=short --disable-warnings'
    )
    focused = subprocess.run(
        ["bash", "-c", command, "round10", sys.executable, FORCED_NODE, SECOND_NODE],
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
    assert text.count("runs-on: macos-15-intel") == 1
    assert text.index("Verify governed macOS x86_64 runner") < text.index(
        "actions/checkout@v4"
    )


def test_partition_is_exact_fifteen_ignores_twenty_six_selectors_twenty_seven_cases() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    prior_ignores, prior_deselects = _partition(prior)
    ignores, deselects = _partition(current)
    assert prior_ignores == IGNORES
    assert ignores == IGNORES
    assert len(prior_deselects) == len(set(prior_deselects)) == 20
    assert deselects == (*prior_deselects, *NEW_DESELECTS)
    assert len(deselects) == len(set(deselects)) == 26
    assert 25 + 2 == 27


def test_predicted_stale_nodes_only_and_all_modules_remain() -> None:
    relative = "tests/verification/test_c3_b4_public_round9.py"
    source = (ROOT / relative).read_text(encoding="utf-8")
    nodes = set(re.findall(r"^def (test_[^(]+)\(", source, re.MULTILINE))
    _, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    disposed = {
        node.split("::", 1)[1] for node in deselects if node.startswith(f"{relative}::")
    }
    assert len(nodes) == 9
    assert disposed == ROUND9_DISPOSED
    assert len(nodes - disposed) == 5
    assert deselects[-6:] == NEW_DESELECTS

    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/"
            r"test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 23
    ignores, _ = _partition(WORKFLOW.read_text(encoding="utf-8"))
    assert modules.isdisjoint(ignores)


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
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-7.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-10.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-9.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round9.py",
    }
