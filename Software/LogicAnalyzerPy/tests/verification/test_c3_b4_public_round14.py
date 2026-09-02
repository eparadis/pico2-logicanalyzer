"""Independent durable C3-B4 collection checks for candidate 42327be9c3ab."""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

CANDIDATE = "42327be9c3ab6a85d2d17ae21a7cdf3d84633142"
CANDIDATE_TREE = "bc51cc4cc333e5e4df946a75dff8ace9c6d6f8d5"
PRIOR_CANDIDATE = "d6cc54afa991f2d6ffed4d9e91cb7d6ebecb9511"
IMMUTABLE_R12_CANDIDATE = "c7650876544e477c277200c4f2fcbd23c67fe245"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990"
SCRATCH_PARENT = REPOSITORY / ".tmp/c3-b4-ci"
RETAINED_FOCUSED_NODES = (
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_raw_b1_focused_and_prior_hosted_guards_remain_green",
    "tests/verification/test_c3_b4_public_round12.py::"
    "test_raw_b1_focused_and_hosted_guards_remain_green",
)
R12_COLLECTION_NODE = (
    "tests/verification/test_c3_b4_public_round12.py::"
    "test_candidate_qualified_collection_is_exact"
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


def _immutable_collection(candidate: str) -> tuple[subprocess.CompletedProcess[str], Path]:
    workflow = _git("show", f"{candidate}:{WORKFLOW_PATH}")
    ignores, deselects = _partition(workflow)
    SCRATCH_PARENT.mkdir(parents=True, exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="r14-candidate-", dir=SCRATCH_PARENT))
    try:
        archive_path = scratch / "candidate.tar"
        subprocess.run(
            [
                "git",
                "archive",
                "--format=tar",
                "--prefix=Software/LogicAnalyzerPy/",
                "--output",
                str(archive_path),
                f"{candidate}:Software/LogicAnalyzerPy",
            ],
            cwd=REPOSITORY,
            capture_output=True,
            check=True,
            text=True,
        )
        with tarfile.open(archive_path, "r:") as archive:
            members = archive.getmembers()
            for member in members:
                path = PurePosixPath(member.name)
                assert not path.is_absolute()
                assert path.parts[:2] == ("Software", "LogicAnalyzerPy")
                assert ".." not in path.parts
            archive.extractall(scratch, members=members, filter="data")
        candidate_root = scratch / "Software/LogicAnalyzerPy"
        temporary_root = scratch / "tmp"
        temporary_root.mkdir()
        command = [
            sys.executable,
            "-m",
            "pytest",
            "--collect-only",
            "-q",
            "-m",
            "not hardware",
            "-p",
            "no:cacheprovider",
        ]
        for ignored in ignores:
            command.extend(("--ignore", ignored))
        for node in deselects:
            command.extend(("--deselect", node))
        environment = os.environ.copy()
        environment.update(
            {
                "PYTHONDONTWRITEBYTECODE": "1",
                "PYTHONPATH": str(candidate_root / "src"),
                "TMPDIR": str(temporary_root),
            }
        )
        result = subprocess.run(
            command,
            cwd=candidate_root,
            env=environment,
            capture_output=True,
            check=False,
            text=True,
        )
    finally:
        shutil.rmtree(scratch)
    return result, scratch


def test_candidate_tree_and_unchanged_workflow_are_exact() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST
    assert _git("diff", "--name-only", f"{PRIOR_CANDIDATE}..{CANDIDATE}", "--", WORKFLOW_PATH) == ""


def test_round13_signal_context_correction_is_real_and_both_functions_pass() -> None:
    command_block = (
        "FOCUSED_COMMAND = (\n"
        "    \"trap '' TERM; \"\n"
        "    'exec \"$1\" -m pytest -q \"$2\" \"$3\" --tb=short --disable-warnings'\n"
        ")\n"
    )
    for relative in (
        "tests/verification/test_c3_b4_public_round11.py",
        "tests/verification/test_c3_b4_public_round12.py",
    ):
        assert (ROOT / relative).read_text().count(command_block) == 1
    assert signal.getsignal(signal.SIGTERM) != signal.SIG_IGN
    inherited = subprocess.run(
        [
            "/bin/sh",
            "-c",
            "trap '' TERM; exec \"$1\" -c 'import signal; "
            "assert signal.getsignal(signal.SIGTERM) == signal.SIG_IGN'",
            "round14",
            sys.executable,
        ],
        capture_output=True,
        check=False,
        text=True,
    )
    assert inherited.returncode == 0, inherited.stdout + inherited.stderr
    retained = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *RETAINED_FOCUSED_NODES],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert retained.returncode == 0, retained.stdout + retained.stderr
    assert "2 passed" in retained.stdout


def test_round12_collection_contract_is_immutable_safe_and_cleanup_bounded() -> None:
    source = (ROOT / "tests/verification/test_c3_b4_public_round12.py").read_text()
    function = source.split(
        "def test_candidate_qualified_collection_is_exact() -> None:\n", maxsplit=1
    )[1].split("\ndef test_", maxsplit=1)[0]
    for fragment in (
        f'CANDIDATE = "{IMMUTABLE_R12_CANDIDATE}"',
        '_git("show", f"{CANDIDATE}:{WORKFLOW_PATH}")',
        'f"{CANDIDATE}:Software/LogicAnalyzerPy"',
        'member_path.parts[:2] == ("Software", "LogicAnalyzerPy")',
        '".." not in member_path.parts',
        'archive.extractall(scratch, members=members, filter="data")',
        '"PYTHONPATH": str(candidate_root / "src")',
        "cwd=candidate_root",
        "finally:\n        shutil.rmtree(scratch)",
        'assert "1459/1497 tests collected (38 deselected)" in result.stdout',
    ):
        assert fragment in source or fragment in function
    assert "cwd=ROOT" not in function


def test_round12_immutable_collection_passes_with_descendants_and_leaks_nothing() -> None:
    before = set(SCRATCH_PARENT.glob("r12-c765-*"))
    assert (REPOSITORY / ".tmp/c3-b4-ci/r13-verifier-draft").is_dir()
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", R12_COLLECTION_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    after = set(SCRATCH_PARENT.glob("r12-c765-*"))
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout
    assert after == before


def test_round14_candidate_collection_is_immutable_exact_and_leak_free() -> None:
    result, scratch = _immutable_collection(CANDIDATE)
    assert not scratch.exists()
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1471/1509 tests collected (38 deselected)" in result.stdout


def test_partition_hosted_guards_and_all_current_modules_are_preserved() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    assert current == prior
    ignores, deselects = _partition(current)
    assert len(ignores) == len(set(ignores)) == 15
    assert len(deselects) == len(set(deselects)) == 37
    assert 36 + 2 == 38
    assert current.count('node-version: "22.14.0"') == 1
    assert current.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert current.count("fetch-depth: 0") == 1
    assert current.count('PYTHONDONTWRITEBYTECODE: "1"') == 1
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 26
    assert modules.isdisjoint(ignores)


def test_no_product_b1_b2_b3_fixture_limit_threshold_lock_or_manifest_drift() -> None:
    changed = set(_git("diff", "--name-only", f"{PRIOR_CANDIDATE}..{CANDIDATE}").splitlines())
    assert changed == {
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-14.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round12.py",
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
