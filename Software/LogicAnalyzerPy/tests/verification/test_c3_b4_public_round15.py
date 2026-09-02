"""Independent hosted-portability checks for C3-B4 candidate 921f8984b45d."""

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

CANDIDATE = "921f8984b45d78d544494733c9fcd043a788f866"
CANDIDATE_TREE = "0b0ea4529e6c2279cdd5b6b766377ea5e75a73e7"
PRIOR_CANDIDATE = "42327be9c3ab6a85d2d17ae21a7cdf3d84633142"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990"
SCRATCH_PARENT = REPOSITORY / ".tmp/c3-b4-ci"
LOCAL_ARCHIVE = REPOSITORY / (
    ".tmp/c3-b4-ci/round11/"
    "cpython-3.12.13+20260623-x86_64-apple-darwin-install_only_stripped.tar.gz"
)
LOCAL_PYTHON = REPOSITORY / ".tmp/c3-b4-ci/round11/python-root/bin/python3.12"
R12_PRESENT_NODE = (
    "tests/verification/test_c3_b4_public_round12.py::"
    "test_artifact_present_branch_uses_hosted_environment_and_passes"
)
R12_COLLECTION_NODE = (
    "tests/verification/test_c3_b4_public_round12.py::"
    "test_candidate_qualified_collection_is_exact"
)
R14_DESCENDANT_NODE = (
    "tests/verification/test_c3_b4_public_round14.py::"
    "test_round12_immutable_collection_passes_with_descendants_and_leaks_nothing"
)
RETAINED_FOCUSED_NODES = (
    "tests/verification/test_c3_b4_public_round11.py::"
    "test_raw_b1_focused_and_prior_hosted_guards_remain_green",
    "tests/verification/test_c3_b4_public_round12.py::"
    "test_raw_b1_focused_and_hosted_guards_remain_green",
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


def _run_node(
    node: str, archive: str | None, python: str | None
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    for key, value in (
        ("PICO_LA_PYTHON_ARCHIVE", archive),
        ("PICO_LA_PYTHON", python),
    ):
        if value is None:
            environment.pop(key, None)
        else:
            environment[key] = value
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", node],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        check=False,
        text=True,
    )


def _available_artifact_pair() -> tuple[Path, Path]:
    hosted_archive = os.environ.get("PICO_LA_PYTHON_ARCHIVE")
    hosted_python = os.environ.get("PICO_LA_PYTHON")
    assert (hosted_archive is None) == (hosted_python is None)
    if hosted_archive is None:
        return LOCAL_ARCHIVE, LOCAL_PYTHON
    return Path(hosted_archive), Path(hosted_python)


def _immutable_collection(candidate: str) -> tuple[subprocess.CompletedProcess[str], Path]:
    ignores, deselects = _partition(_git("show", f"{candidate}:{WORKFLOW_PATH}"))
    SCRATCH_PARENT.mkdir(parents=True, exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix="r15-candidate-", dir=SCRATCH_PARENT))
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


def test_hosted_pair_is_forwarded_and_both_partial_states_fail_closed() -> None:
    archive, python = _available_artifact_pair()
    assert archive.is_file() and python.is_file()
    complete = _run_node(R12_PRESENT_NODE, str(archive), str(python))
    assert complete.returncode == 0, complete.stdout + complete.stderr
    assert "1 passed" in complete.stdout
    for partial in ((str(archive), None), (None, str(python))):
        result = _run_node(R12_PRESENT_NODE, *partial)
        assert result.returncode == 1
        assert "1 failed" in result.stdout and "skipped" not in result.stdout


def test_current_environment_selects_hosted_pair_or_local_absent_fallback() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", R12_PRESENT_NODE],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout
    source = (ROOT / "tests/verification/test_c3_b4_public_round12.py").read_text()
    branch = source.split(
        "def test_artifact_present_branch_uses_hosted_environment_and_passes() -> None:\n",
        maxsplit=1,
    )[1].split("\ndef test_", maxsplit=1)[0]
    assert branch.index("if hosted_archive is None:") < branch.index(
        "archive_path = ARCHIVE"
    )
    assert "assert (hosted_archive is None) == (hosted_python is None)" in branch


def test_r12_and_r14_collection_proofs_are_descendant_safe_and_leak_free() -> None:
    before = set(SCRATCH_PARENT.glob("r12-c765-*"))
    for node in (R12_COLLECTION_NODE, R14_DESCENDANT_NODE):
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", node],
            cwd=ROOT,
            capture_output=True,
            check=False,
            text=True,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        assert "1 passed" in result.stdout
    assert set(SCRATCH_PARENT.glob("r12-c765-*")) == before
    round14 = (ROOT / "tests/verification/test_c3_b4_public_round14.py").read_text()
    proof = round14.split(
        "def test_round12_immutable_collection_passes_with_descendants_and_leaks_nothing() "
        "-> None:\n",
        maxsplit=1,
    )[1].split("\ndef test_", maxsplit=1)[0]
    assert 'descendant = "tests/verification/test_c3_b4_public_round14.py"' in proof
    assert "r13-verifier-draft" not in proof and ".tmp/" not in proof


def test_current_candidate_collection_is_immutable_exact_and_leak_free() -> None:
    result, scratch = _immutable_collection(CANDIDATE)
    assert not scratch.exists()
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1479/1517 tests collected (38 deselected)" in result.stdout


def test_signal_context_partition_guards_and_all_modules_remain() -> None:
    assert signal.getsignal(signal.SIGTERM) != signal.SIG_IGN
    signal_child = subprocess.run(
        [
            "/bin/sh",
            "-c",
            "trap '' TERM; exec \"$1\" -c 'import signal; "
            "assert signal.getsignal(signal.SIGTERM) == signal.SIG_IGN'",
            "round15",
            sys.executable,
        ],
        capture_output=True,
        check=False,
        text=True,
    )
    assert signal_child.returncode == 0, signal_child.stdout + signal_child.stderr
    focused = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *RETAINED_FOCUSED_NODES],
        cwd=ROOT,
        capture_output=True,
        check=False,
        text=True,
    )
    assert focused.returncode == 0, focused.stdout + focused.stderr
    assert "2 passed" in focused.stdout
    current = WORKFLOW.read_text(encoding="utf-8")
    ignores, deselects = _partition(current)
    assert len(ignores) == len(set(ignores)) == 15
    assert len(deselects) == len(set(deselects)) == 37
    assert 36 + 2 == 38
    modules = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/test_c3_b[234].*\.py",
            line,
        )
    }
    assert len(modules) == 27
    assert modules.isdisjoint(ignores)


def test_no_product_b1_b2_b3_fixture_limit_threshold_lock_or_manifest_drift() -> None:
    changed = set(_git("diff", "--name-only", f"{PRIOR_CANDIDATE}..{CANDIDATE}").splitlines())
    assert changed == {
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-15.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-14.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round12.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round14.py",
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
