"""Independent C3-B4 hosted-partition checks for candidate 8cd114fa316f."""

from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

CANDIDATE = "8cd114fa316f10db4d403197f3204771ccd36638"
CANDIDATE_TREE = "5b4c8f46ca626861a3191282aa5e2b282f806246"
PRIOR_CANDIDATE = "afa015727a791e03071b6fb6607cdb1fd231727a"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
WORKFLOW_PATH = Path(".github/workflows/logic-analyzer-python-cycle2.yml")
WORKFLOW = REPOSITORY / WORKFLOW_PATH
WORKFLOW_DIGEST = "5c6b9cb1904d2096592bfc13e3854df24ddf84cba921df320556555b457eacff"
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
)
CURRENT_CYCLE3_MODULES = {
    "tests/implementation/test_c3_b2_private_host.py",
    "tests/implementation/test_c3_b3_cross_source_equivalence.py",
    "tests/implementation/test_c3_b3_i2c_conformance.py",
    "tests/implementation/test_c3_b3_spi_conformance.py",
    "tests/implementation/test_c3_b3_uart_conformance.py",
    "tests/implementation/test_c3_b4_public.py",
    "tests/verification/test_c3_b2_private_host.py",
    "tests/verification/test_c3_b2_private_host_round2.py",
    "tests/verification/test_c3_b2_private_host_round3.py",
    "tests/verification/test_c3_b2_private_host_round4.py",
    "tests/verification/test_c3_b3_cross_source_equivalence.py",
    "tests/verification/test_c3_b3_i2c_conformance.py",
    "tests/verification/test_c3_b3_spi_conformance.py",
    "tests/verification/test_c3_b3_uart_conformance.py",
    "tests/verification/test_c3_b4_public_round1.py",
    "tests/verification/test_c3_b4_public_round2.py",
    "tests/verification/test_c3_b4_public_round3.py",
    "tests/verification/test_c3_b4_public_round4.py",
}


def _git(*arguments: str) -> str:
    return subprocess.run(
        ["git", *arguments],
        cwd=REPOSITORY,
        capture_output=True,
        check=True,
        text=True,
    ).stdout


def _workflow_partition(text: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    ignores = tuple(re.findall(r"--ignore ([^\s\\]+)", text))
    deselects = tuple(re.findall(r"--deselect ([^\s\\]+)", text))
    return ignores, deselects


def test_candidate_binding_and_exact_workflow_digest() -> None:
    assert _git("show", "-s", "--format=%T", CANDIDATE).strip() == CANDIDATE_TREE
    assert hashlib.sha256(WORKFLOW.read_bytes()).hexdigest() == WORKFLOW_DIGEST


def test_partition_has_exact_ordered_unique_ignores_and_deselections() -> None:
    actual_ignores, actual_deselects = _workflow_partition(WORKFLOW.read_text())
    assert actual_ignores == IGNORES
    assert actual_deselects == DESELECTS
    assert len(actual_ignores) == len(set(actual_ignores)) == 15
    assert len(actual_deselects) == len(set(actual_deselects)) == 3
    assert all((ROOT / item).is_file() for item in actual_ignores)
    for node in actual_deselects:
        path, name = node.split("::", 1)
        assert (ROOT / path).is_file()
        assert f"def {name}(" in (ROOT / path).read_text(encoding="utf-8")


def test_every_candidate_b2_b3_b4_module_is_retained() -> None:
    candidate_files = {
        line.removeprefix("Software/LogicAnalyzerPy/")
        for line in _git("ls-tree", "-r", "--name-only", CANDIDATE).splitlines()
        if re.fullmatch(
            r"Software/LogicAnalyzerPy/tests/(?:implementation|verification)/"
            r"test_c3_b[234].*\.py",
            line,
        )
    }
    assert candidate_files == CURRENT_CYCLE3_MODULES
    ignores, deselects = _workflow_partition(WORKFLOW.read_text())
    assert candidate_files.isdisjoint(ignores)
    affected = {node.split("::", 1)[0] for node in deselects} & candidate_files
    assert affected == {"tests/verification/test_c3_b4_public_round4.py"}
    round4_prefix = "tests/verification/test_c3_b4_public_round4.py::"
    assert sum(node.startswith(round4_prefix) for node in deselects) == 2


def test_all_remaining_round4_behavior_and_scope_nodes_are_retained() -> None:
    round4 = (ROOT / "tests/verification/test_c3_b4_public_round4.py").read_text(
        encoding="utf-8"
    )
    nodes = tuple(re.findall(r"^def (test_[^(]+)\(", round4, re.MULTILINE))
    assert nodes == (
        "test_candidate_binding_and_exact_workflow_digest",
        "test_official_intel_label_and_guard_are_first_and_prebootstrap",
        "test_architecture_guard_accepts_x86_64_and_fails_other_architecture",
        "test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order",
        "test_correction_has_no_decoder_api_threshold_fixture_or_lock_drift",
    )
    deselected_names = {node.split("::", 1)[1] for node in DESELECTS[1:]}
    assert set(nodes) - deselected_names == {
        "test_official_intel_label_and_guard_are_first_and_prebootstrap",
        "test_architecture_guard_accepts_x86_64_and_fails_other_architecture",
        "test_correction_has_no_decoder_api_threshold_fixture_or_lock_drift",
    }


def test_partition_is_the_only_workflow_change_from_round4() -> None:
    current = WORKFLOW.read_text(encoding="utf-8")
    prior = _git("show", f"{PRIOR_CANDIDATE}:{WORKFLOW_PATH}")
    invocation_start = current.index(
        '          .venv/bin/python -m pytest -m "not hardware" --tb=short '
        "--disable-warnings \\\n"
    )
    invocation_end = current.index('            >"$log_file" 2>&1\n', invocation_start)
    invocation_end += len('            >"$log_file" 2>&1\n')
    restored = (
        current[:invocation_start]
        + '          .venv/bin/python -m pytest -m "not hardware" --tb=short '
        '--disable-warnings >"$log_file" 2>&1\n'
        + current[invocation_end:]
    )
    assert restored == prior


def test_runner_guard_remains_first_and_prebootstrap() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("runs-on: macos-15-intel") == 1
    assert "runs-on: macos-latest" not in text
    assert text.count('architecture="$(uname -m)"') == 1
    assert text.count('if [ "$architecture" != "x86_64" ]; then') == 1
    guard = text.index("- name: Verify governed macOS x86_64 runner")
    checkout = text.index("- uses: actions/checkout@v4")
    bootstrap = text.index("- name: Create clean core Python 3.12 environment")
    assert text.index("steps:\n") < guard < checkout < bootstrap


def test_no_product_fixture_limit_threshold_manifest_or_lock_drift() -> None:
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
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-accumulated-validation-round-2.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-5.md",
        "Software/LogicAnalyzerPy/docs/reviews/c3-b4-verification-round-4.md",
        "Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py",
        "Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round4.py",
    }
