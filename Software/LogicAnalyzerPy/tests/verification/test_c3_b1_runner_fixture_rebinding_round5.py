"""Portable static verification of the RA001 replacement runner candidate.

The safe test inventory is derived from the immutable candidate tree. Optional
B2 and superseded verifier paths are tested synthetically and never opened.
"""

from __future__ import annotations

import ast
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
SUBJECT_COMMIT = "380d5dd77ae6c6f8648391e3c849c13c4b98fe8a"
SUBJECT_TREE = "aa55b4884c39981026ba233b48dc8f360d404c8a"
RA001_COMMIT = "91ee8f818ce6bb26196d673cdf6975e9a7248d6a"
RV002_COMMIT = "1dcd62ff6b0a527b57b25a817488b323942a90ae"
RV003_COMMIT = "cb3a9743495aed686e6adb9c123812a2724aa9f7"
SUPERSEDED_CANDIDATE = "55d22640334ef05176568f275c3e4e7ec63c3336"
IMPLEMENTATION_RECORD = (
    ROOT
    / "docs/reviews/"
    "c3-b1-preexecution-runner-fixture-rebinding-implementation-round-3.md"
)
IMPLEMENTATION_RECORD_SHA256 = (
    "bbf2cb087ec97790c2403b7406560656d84ebb4f600190a3a881c7143fa8bf0e"
)
EXPECTED_HASHES = {
    "docs/cycle-3-characterization-method.md": (
        "f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341"
    ),
    "tools/cycle3_characterize/runner.py": (
        "0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80"
    ),
    "tools/cycle3_characterize/candidate-binding.json": (
        "4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7"
    ),
    "tests/implementation/test_cycle3_preexecution_runner.py": (
        "1511083a3254a44bd95f33f75d9cf5adb022162b20a9e0c274929f4f9325ad19"
    ),
    "testdata/decoders/cycle3/semantic-fixtures.json": (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    ),
    "testdata/decoders/cycle3/manifest.json": (
        "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9"
    ),
    "testdata/decoders/cycle3/experiment-caps.json": (
        "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d"
    ),
}
VERIFIER5 = "tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py"
OPTIONAL_B2 = "tests/implementation/test_c3_b2_private_host.py"
SUPERSEDED_VERIFIERS = {
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round3.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py",
}
CURRENT_GATE_MODULES = {
    "tests/implementation/test_cycle3_fixtures.py",
    "tests/implementation/test_cycle3_preexecution_runner.py",
    VERIFIER5,
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        cwd=REPOSITORY,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _candidate_test_modules() -> set[str]:
    prefix = "Software/LogicAnalyzerPy/"
    return {
        line.removeprefix(prefix)
        for line in _git(
            "ls-tree", "-r", "--name-only", SUBJECT_COMMIT, f"{prefix}tests"
        ).splitlines()
        if Path(line).name.startswith("test_") and line.endswith(".py")
    }


def _excluded(module: str) -> bool:
    return Path(module).name.startswith("test_c3_") and module not in CURRENT_GATE_MODULES


def _partition(modules: set[str]) -> tuple[set[str], set[str]]:
    excluded = {module for module in modules if _excluded(module)}
    return modules - excluded, excluded


def test_exact_candidate_tree_and_record_only_delta_from_ra001() -> None:
    assert _git("rev-parse", f"{SUBJECT_COMMIT}^{{tree}}") == SUBJECT_TREE
    assert _git("diff", "--name-status", RA001_COMMIT, SUBJECT_COMMIT).splitlines() == [
        "A\tSoftware/LogicAnalyzerPy/docs/reviews/"
        "c3-b1-preexecution-runner-fixture-rebinding-implementation-round-3.md"
    ]
    assert _sha256(IMPLEMENTATION_RECORD) == IMPLEMENTATION_RECORD_SHA256


def test_runner_fixture_method_and_binding_bytes_are_exact() -> None:
    for relative, expected in EXPECTED_HASHES.items():
        path = ROOT / relative
        assert _sha256(path) == expected, relative
        assert _git(
            "rev-parse", f"{SUBJECT_COMMIT}:Software/LogicAnalyzerPy/{relative}"
        ) == _git(
            "rev-parse", f"{SUPERSEDED_CANDIDATE}:Software/LogicAnalyzerPy/{relative}"
        )


def test_binding_closes_fixture_identity_and_all_sources() -> None:
    binding = json.loads(
        (ROOT / "tools/cycle3_characterize/candidate-binding.json").read_text()
    )
    assert binding["accepted_fixture"] == {
        "candidate_commit": "3af6b9f80dd52611e14acca407707d1da7b8d9ac",
        "candidate_tree": "14c010153ea5542617e601e4126047c561a48483",
        "caps_sha256": EXPECTED_HASHES[
            "testdata/decoders/cycle3/experiment-caps.json"
        ],
        "manifest_sha256": EXPECTED_HASHES[
            "testdata/decoders/cycle3/manifest.json"
        ],
        "semantic_fixture_sha256": EXPECTED_HASHES[
            "testdata/decoders/cycle3/semantic-fixtures.json"
        ],
    }
    assert len(binding["sources"]) == 24
    for path, digest in binding["sources"].items():
        source = REPOSITORY / path if path.startswith("Software/") else ROOT / path
        assert _sha256(source) == digest, path


def test_all_seventeen_positive_caps_remain_exactly_bound() -> None:
    caps = json.loads(
        (ROOT / "testdata/decoders/cycle3/experiment-caps.json").read_text()
    )["caps"]
    assert len(caps) == 17
    assert len({entry["id"] for entry in caps}) == 17
    assert all(type(entry["value"]) is int and entry["value"] > 0 for entry in caps)


def test_record_preserves_ra001_and_transfers_no_result_or_authority() -> None:
    record = IMPLEMENTATION_RECORD.read_text()
    for literal in (
        RA001_COMMIT,
        SUPERSEDED_CANDIDATE,
        "candidate-not-accepted",
        "does not transfer",
        "No result or authority",
        "include-only",
        "No raw verifier",
    ):
        assert literal in record
    assert "A broad\n`pytest -m \"not hardware\"` command is forbidden" in record


def test_clean_candidate_plus_verifier5_inventory_is_exact() -> None:
    candidate = _candidate_test_modules()
    clean = candidate | {VERIFIER5}
    included, excluded = _partition(clean)
    assert len(candidate) == 51
    assert len(clean) == 52
    assert len(included) == 40
    assert len(excluded) == 12
    assert included & excluded == set()
    assert included | excluded == clean
    assert CURRENT_GATE_MODULES <= included
    assert OPTIONAL_B2 not in clean
    assert SUPERSEDED_VERIFIERS.isdisjoint(clean)
    assert all(
        not Path(module).name.startswith("test_c3_")
        or module in CURRENT_GATE_MODULES
        for module in included
    )


def test_optional_b2_and_superseded_verifiers_are_synthetically_excluded() -> None:
    clean = _candidate_test_modules() | {VERIFIER5}
    clean_included, _ = _partition(clean)
    optional = clean | {OPTIONAL_B2} | SUPERSEDED_VERIFIERS
    included, excluded = _partition(optional)
    assert included == clean_included
    assert {OPTIONAL_B2} | SUPERSEDED_VERIFIERS <= excluded
    assert len(optional) == 55
    assert len(included) == 40
    assert len(excluded) == 15


def test_unknown_future_c3_module_fails_closed() -> None:
    future = "tests/verification/test_c3_future_unknown.py"
    included, excluded = _partition(_candidate_test_modules() | {VERIFIER5, future})
    assert future not in included
    assert future in excluded


def test_excluded_partition_covers_every_forbidden_downstream_class() -> None:
    _, excluded = _partition(_candidate_test_modules() | {VERIFIER5})
    required_names = {
        "test_c3_b1_raw_baseline_candidate.py",
        "test_c3_b1_threshold_proposal.py",
        "test_c3_b1_threshold_proposal_round2.py",
        "test_c3_b1_threshold_proposal_round3.py",
        "test_c3_b1_final_candidate.py",
        "test_c3_b1_final_candidate_round3.py",
        "test_c3_b1_preexecution_runner_candidate.py",
        "test_c3_b1_runner_fixture_rebinding.py",
        "test_c3_b1_runner_fixture_rebinding_round2.py",
        "test_c3_b1_semantic_fixture_candidate.py",
        "test_c3_b1_semantic_fixture_correction.py",
        "test_c3_b1_semantic_fixture_correction_round2.py",
    }
    assert required_names <= {Path(module).name for module in excluded}


def test_safe_partition_has_no_direct_decoder_raw_or_b2_import() -> None:
    included, _ = _partition(_candidate_test_modules() | {VERIFIER5})
    forbidden_imports = (
        "pico_logic_analyzer._decode",
        "tools.cycle3_characterize.snapshot_host",
        "test_c3_b1_raw_baseline_candidate",
        "test_c3_b2_private_host",
    )
    for module in included:
        # This is the explicitly allowed inert runner suite; it imports the
        # snapshot host to exercise its validation helpers without launching it.
        if module == "tests/implementation/test_cycle3_preexecution_runner.py":
            continue
        tree = ast.parse((ROOT / module).read_text(), filename=module)
        imported: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module)
        assert not any(
            name == forbidden or name.startswith(f"{forbidden}.")
            for name in imported
            for forbidden in forbidden_imports
        ), (module, imported)


def test_rv002_and_rv003_failures_transfer_no_authority() -> None:
    rv002 = _git(
        "show", f"{RV002_COMMIT}:Software/LogicAnalyzerPy/docs/cycle-3-orchestration-progress.md"
    )
    rv003 = _git(
        "show", f"{RV003_COMMIT}:Software/LogicAnalyzerPy/docs/cycle-3-orchestration-progress.md"
    )
    assert "C3B1-RV002" in rv002
    assert "transfers no authority" in rv002
    assert "C3B1-RV003" in rv003
    assert "verifier-4's pass transfers no authority" in rv003
    assert "must create only a new\n  verifier test/review" in rv003
