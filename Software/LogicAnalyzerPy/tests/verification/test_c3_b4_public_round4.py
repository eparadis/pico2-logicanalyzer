"""Independent C3-B4 hosted-correction checks for candidate afa015727a791e."""

from __future__ import annotations

import hashlib
import os
import re
import stat
import subprocess
from pathlib import Path

CANDIDATE = "afa015727a791e03071b6fb6607cdb1fd231727a"
CANDIDATE_TREE = "ea19d3e2e95071c06ee7bf9fbb152e9571f72ce0"
PRIOR_PRODUCT_CANDIDATE = "e93b0d85bb57c014979c648373e48af845e7b01f"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "3df72bff1cde7fdd8619bc74e1f796d9f3d755a5e35a4d4ef2070327fa602f0e"
GUARD = """architecture="$(uname -m)"
if [ "$architecture" != "x86_64" ]; then
  printf 'unsupported runner architecture: %s (required: x86_64)\\n' "$architecture" >&2
  exit 2
fi
"""


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=REPOSITORY,
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def _prior_workflow() -> str:
    return _git("show", f"{PRIOR_PRODUCT_CANDIDATE}:{WORKFLOW_PATH}")


def test_candidate_binding_and_exact_workflow_digest() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_official_intel_label_and_guard_are_first_and_prebootstrap() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("runs-on: macos-15-intel") == 1
    assert "runs-on: macos-latest" not in text
    assert "runs-on: macos-15\n" not in text
    assert text.count("- name: Verify governed macOS x86_64 runner") == 1
    assert text.count('architecture="$(uname -m)"') == 1
    assert text.count('if [ "$architecture" != "x86_64" ]; then') == 1
    guard = text.index("- name: Verify governed macOS x86_64 runner")
    checkout = text.index("- uses: actions/checkout@v4")
    setup_python = text.index("- uses: actions/setup-python@v5")
    bootstrap = text.index("- name: Create clean core Python 3.12 environment")
    assert guard < checkout < setup_python < bootstrap
    assert re.search(r"steps:\n      - name: Verify governed macOS x86_64 runner\n", text)


def test_architecture_guard_accepts_x86_64_and_fails_other_architecture(
    tmp_path: Path,
) -> None:
    accepted = subprocess.run(
        ["bash", "-c", GUARD], capture_output=True, check=False, text=True
    )
    assert accepted.returncode == 0
    assert accepted.stdout == accepted.stderr == ""

    fake_uname = tmp_path / "uname"
    fake_uname.write_text("#!/bin/sh\nprintf '%s\\n' arm64\n", encoding="utf-8")
    fake_uname.chmod(fake_uname.stat().st_mode | stat.S_IXUSR)
    environment = dict(os.environ)
    environment["PATH"] = f"{tmp_path}:{environment['PATH']}"
    rejected = subprocess.run(
        ["bash", "-c", GUARD],
        capture_output=True,
        check=False,
        env=environment,
        text=True,
    )
    assert rejected.returncode == 2
    assert rejected.stdout == ""
    assert rejected.stderr == "unsupported runner architecture: arm64 (required: x86_64)\n"


def test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _prior_workflow()
    guard_block = """      - name: Verify governed macOS x86_64 runner
        shell: bash
        run: |
          architecture="$(uname -m)"
          if [ "$architecture" != "x86_64" ]; then
            printf 'unsupported runner architecture: %s (required: x86_64)\\n' "$architecture" >&2
            exit 2
          fi
"""
    restored = current.replace("runs-on: macos-15-intel", "runs-on: macos-latest")
    restored = restored.replace(guard_block, "")
    assert restored == prior

    marker = re.compile(r"^      - (?:name: (?P<name>.+)|uses: (?P<uses>.+))$", re.MULTILINE)
    current_steps = [
        match.group("name") or match.group("uses") for match in marker.finditer(current)
    ]
    prior_steps = [match.group("name") or match.group("uses") for match in marker.finditer(prior)]
    assert current_steps == ["Verify governed macOS x86_64 runner", *prior_steps]


def test_correction_has_no_decoder_api_threshold_fixture_or_lock_drift() -> None:
    changed = set(
        _git("diff", "--name-only", f"{PRIOR_PRODUCT_CANDIDATE}..{CANDIDATE}").splitlines()
    )
    prohibited_fragments = (
        "/src/",
        "/testdata/",
        "/requirements-dev.lock",
        "/requirements-web.lock",
        "/pyproject.toml",
        "/package-lock.json",
        "/fixtures/",
    )
    assert not {
        path for path in changed if any(fragment in path for fragment in prohibited_fragments)
    }
    assert changed == {
        ".github/workflows/logic-analyzer-python-cycle2.yml",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-1.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-4.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-3.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round3.py",
    }
