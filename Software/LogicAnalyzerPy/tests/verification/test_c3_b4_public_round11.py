"""Independent C3-B4 artifact checks for candidate fb2f4d63df41."""

from __future__ import annotations

import hashlib
import os
import platform
import re
import subprocess
import sys
import tarfile
from pathlib import Path

import pytest

CANDIDATE = "fb2f4d63df41f7d5d0c2253c59f02803dac14a55"
CANDIDATE_TREE = "57faa63344049874e09ebaa89807de8ea6188547"
PRIOR_CANDIDATE = "ab6744c3263b504e1b4006ece64be12962ce8b47"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "153c9b3987200eef271f4f26c0253622e0f087a12c1d89216971d67062041318"
ARTIFACT_NAME = (
    "cpython-3.12.13+20260623-x86_64-apple-darwin-install_only_stripped.tar.gz"
)
ARTIFACT_URL = (
    "https://github.com/astral-sh/python-build-standalone/releases/download/"
    f"20260623/{ARTIFACT_NAME.replace('+', '%2B')}"
)
ARTIFACT_SHA256 = "a6bbea996c5f14eb55ab275889d2df45408deec504b4a7219d7b59c045b2555e"
EXPECTED_VERSION = "3.12.13 (main, Jun 23 2026, 15:54:40) [Clang 22.1.3 ]"
MANAGED_KEY = "cpython-3.12.13-macos-x86_64-none"
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
NEW_DESELECTS = (
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_candidate_tree_and_workflow_digest_are_exact",
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_setup_uv_is_immutable_v9_exact_0126_and_cache_disabled",
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_cache_install_and_managed_interpreter_paths_are_repo_ignored",
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_exact_managed_identity_guard_precedes_dependencies",
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_partition_is_exact_fifteen_ignores_twenty_six_selectors_twenty_seven_cases",
    "tests/verification/test_c3_b4_public_round10.py::"
    "test_predicted_stale_nodes_only_and_all_modules_remain",
)


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


def test_artifact_identity_url_and_https_only_download_are_exact() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count(f"PICO_LA_PYTHON_URL: {ARTIFACT_URL}") == 1
    assert text.count(f"PICO_LA_PYTHON_SHA256: {ARTIFACT_SHA256}") == 1
    archive_environment = (
        "PICO_LA_PYTHON_ARCHIVE: ${{ github.workspace }}/.tmp/c3-b4-ci/"
        f"{ARTIFACT_NAME}"
    )
    assert text.count(archive_environment) == 1
    assert text.count(
        "curl --fail --location --proto '=https' --tlsv1.2 "
        '--output "$PICO_LA_PYTHON_ARCHIVE" "$PICO_LA_PYTHON_URL"'
    ) == 1
    assert "actions/setup-python" not in text
    assert "astral-sh/setup-uv" not in text
    assert "uv python install" not in text


def test_downloaded_artifact_hash_size_layout_and_runtime_are_exact() -> None:
    archive_value = os.environ.get("PICO_LA_PYTHON_ARCHIVE")
    python_value = os.environ.get("PICO_LA_PYTHON")
    if archive_value is None and python_value is None:
        pytest.skip(
            "workflow-provisioned artifact is unavailable; immutable URL, digest, "
            "and extraction contract remain covered statically"
        )
    assert archive_value is not None and python_value is not None
    archive_path = Path(archive_value)
    python_path = Path(python_value)
    assert archive_path.is_file()
    assert archive_path.stat().st_size == 24_690_991
    assert hashlib.sha256(archive_path.read_bytes()).hexdigest() == ARTIFACT_SHA256
    with tarfile.open(archive_path, "r:gz") as archive:
        names = archive.getnames()
    assert names and all(name == "python" or name.startswith("python/") for name in names)
    assert python_path.is_file()
    result = subprocess.run(
        [
            str(python_path),
            "-c",
            (
                "import platform,sys; "
                f"assert sys.version == {EXPECTED_VERSION!r}; "
                "assert platform.machine() == 'x86_64'"
            ),
        ],
        capture_output=True,
        check=False,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_checksum_extraction_and_guard_are_ordered_before_dependencies() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    fragments = (
        'install -d "$PICO_LA_PYTHON_ROOT"',
        "curl --fail --location --proto '=https' --tlsv1.2",
        "shasum -a 256 --check --strict",
        'tar -xzf "$PICO_LA_PYTHON_ARCHIVE" --strip-components 1 -C "$PICO_LA_PYTHON_ROOT"',
        'assert sys.version == os.environ["PICO_LA_EXPECTED_PYTHON"]',
        'assert platform.machine() == "x86_64"',
        f'assert sys.base_prefix.endswith("/{MANAGED_KEY}")',
        "actions/setup-node@v4",
        "pip install --require-hashes -r requirements-dev.lock",
    )
    positions = [text.index(fragment) for fragment in fragments]
    assert positions == sorted(positions)
    assert 'PICO_LA_EXPECTED_PYTHON: "' + EXPECTED_VERSION + '"' in text
    assert '"BUILD"' not in text


def test_both_venvs_remain_bound_to_exact_artifact_interpreter() -> None:
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


def test_raw_b1_focused_and_prior_hosted_guards_remain_green() -> None:
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
    assert platform.machine() == "x86_64"
    assert text.count('node-version: "22.14.0"') == 1
    assert text.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert text.count("fetch-depth: 0") == 1
    assert text.count('PYTHONDONTWRITEBYTECODE: "1"') == 1
    assert text.count("runs-on: macos-15-intel") == 1
    assert text.index("Verify governed macOS x86_64 runner") < text.index("actions/checkout@v4")
    focused = subprocess.run(
        [
            "/bin/sh",
            "-c",
            FOCUSED_COMMAND,
            "round11",
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


def test_partition_is_exact_fifteen_ignores_thirty_two_selectors_thirty_three_cases() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    prior_ignores, prior_deselects = _partition(prior)
    ignores, deselects = _partition(current)
    assert ignores == prior_ignores
    assert len(ignores) == len(set(ignores)) == 15
    assert len(prior_deselects) == len(set(prior_deselects)) == 26
    assert deselects == (*prior_deselects, *NEW_DESELECTS)
    assert len(deselects) == len(set(deselects)) == 32
    assert 31 + 2 == 33


def test_only_six_stale_round10_nodes_are_disposed_and_all_modules_remain() -> None:
    relative = "tests/verification/test_c3_b4_public_round10.py"
    source = (ROOT / relative).read_text(encoding="utf-8")
    nodes = set(re.findall(r"^def (test_[^(]+)\(", source, re.MULTILINE))
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    disposed = {node for node in deselects if node.startswith(f"{relative}::")}
    assert len(nodes) == 9
    assert tuple(node for node in deselects if node.startswith(f"{relative}::")) == NEW_DESELECTS
    assert len(disposed) == 6
    assert len(nodes - {node.split("::", 1)[1] for node in disposed}) == 3
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 24
    assert modules.isdisjoint(ignores)


def test_candidate_qualified_collection_is_exact() -> None:
    ignores, deselects = _partition(WORKFLOW.read_text(encoding="utf-8"))
    command = [sys.executable, "-m", "pytest", "--collect-only", "-q", "-m", "not hardware"]
    for ignored in (*ignores, "tests/verification/test_c3_b4_public_round11.py"):
        command.extend(("--ignore", ignored))
    for node in deselects:
        command.extend(("--deselect", node))
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1454/1487 tests collected (33 deselected)" in result.stdout


def test_no_product_b1_b2_b3_fixture_limit_threshold_lock_or_manifest_drift() -> None:
    changed = set(_git("diff", "--name-only", f"{PRIOR_CANDIDATE}..{CANDIDATE}").splitlines())
    assert changed == {
        ".github/workflows/logic-analyzer-python-cycle2.yml",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-11.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-10.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round10.py",
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
