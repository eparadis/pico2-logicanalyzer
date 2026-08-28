"""Independent verification of the corrected-fixture C3-B1 raw baseline."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
RAW_ROOT = ROOT / "testdata" / "decoders" / "cycle3-raw"
REPORT = Path("/private/tmp/c3-b1-raw-baseline-verifier-replacement-report.json")
SUBJECT_COMMIT = "d0d9dbe87f7841f09f261556de0909475e048b95"
SUBJECT_TREE = "a749b4e192246afab34eb6f11438d64eaeaa4d0c"
COLLECTION_EXECUTABLE = (
    "/Users/ed/git/pico2-logicanalyzer/Software/LogicAnalyzerPy/.venv/bin/python"
)
EXPECTED_DIGESTS = {
    "environment.json": "d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f",
    "requests.json": "fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c",
    "observations.json": "ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee",
    "hostile-observations.json": "af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91",
    "manifest.json": "5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8",
}
EXPECTED_IDENTITY = {
    "binding_sha256": "4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7",
    "caps_sha256": "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d",
    "fixture_candidate_commit": "3af6b9f80dd52611e14acca407707d1da7b8d9ac",
    "fixture_candidate_tree": "14c010153ea5542617e601e4126047c561a48483",
    "fixture_manifest_sha256": "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9",
    "runner_acceptance_commit": "01f059cb5f60e885c7d19e8bf5376bdb27dcca19",
    "runner_acceptance_sha256": "f1963a6cfe7de8c62c2f3de150f0bbb7ffe0e3c93998d2dc352ffdbe4b3eb5bd",
    "runner_acceptance_tree": "1c15252a26e5a4af571228dbf37999e385026f87",
    "runner_candidate_commit": "380d5dd77ae6c6f8648391e3c849c13c4b98fe8a",
    "runner_candidate_tree": "aa55b4884c39981026ba233b48dc8f360d404c8a",
    "semantic_fixture_sha256": "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094",
}


def _load_prior() -> ModuleType:
    path = Path(__file__).with_name("test_c3_b1_raw_baseline_candidate.py")
    spec = importlib.util.spec_from_file_location("_c3_b1_prior_raw_verifier", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.SUBJECT_COMMIT = SUBJECT_COMMIT
    module.SUBJECT_TREE = SUBJECT_TREE
    module.EXPECTED_IDENTITY = EXPECTED_IDENTITY
    module.REPORT = REPORT
    return module


PRIOR = _load_prior()


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(name: str) -> dict[str, Any]:
    value = json.loads((RAW_ROOT / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_candidate_identity_digest_environment_schema_and_summary_arithmetic() -> None:
    assert SUBJECT_COMMIT == "d0d9dbe87f7841f09f261556de0909475e048b95"
    assert SUBJECT_TREE == "a749b4e192246afab34eb6f11438d64eaeaa4d0c"
    assert {name: _sha(RAW_ROOT / name) for name in EXPECTED_DIGESTS} == EXPECTED_DIGESTS
    assert all(PRIOR._canonical(RAW_ROOT / name) for name in EXPECTED_DIGESTS)

    environment = _load("environment.json")
    assert set(environment) == {
        "caps", "collector_sha256", "discrepancy_policy", "identity", "machine",
        "python", "repetitions", "resource_mechanisms", "schema", "source_digests",
        "warmup_rule",
    }
    assert environment["schema"] == "cycle3-raw-environment/v1"
    assert environment["identity"] == EXPECTED_IDENTITY
    assert environment["python"]["executable"] == COLLECTION_EXECUTABLE
    assert environment["python"]["version"] == sys.version
    assert environment["python"]["implementation"] == platform.python_implementation() == "CPython"
    assert environment["caps"] == PRIOR.load_caps()
    assert len(environment["caps"]) == 17
    assert environment["repetitions"] == 5
    assert environment["warmup_rule"] == (
        "one unrecorded status-only warm-up before five independent retained "
        "repetitions per snapshot and hostile case"
    )
    assert len(environment["source_digests"]) == 9
    for relative, digest in environment["source_digests"].items():
        assert _sha(REPOSITORY / relative) == digest
    PRIOR.verify_launch_identity()

    manifest = _load("manifest.json")
    PRIOR._assert_manifest(manifest, EXPECTED_DIGESTS)
    observations = _load("observations.json")
    assert set(observations) == {"schema", "observations"}
    assert observations["schema"] == "cycle3-raw-observations/v1"
    assert len(observations["observations"]) == 63
    for case in observations["observations"]:
        assert set(case) == {"id", "repetitions", "summary", "warmup_unrecorded"}
        assert case["warmup_unrecorded"] == {"ok": True}
        assert all(rep["ok"] for rep in case["repetitions"])
        PRIOR._assert_snapshot_summary(case)

    hostile = _load("hostile-observations.json")
    assert set(hostile) == {"schema", "observations"}
    assert hostile["schema"] == "cycle3-raw-hostile/v1"
    assert len(hostile["observations"]) == 10
    for case in hostile["observations"]:
        assert set(case) == {
            "classification", "kind", "repetitions", "summary", "warmup_unrecorded"
        }
        PRIOR._assert_hostile_summary(case)


def test_manifest_and_summary_mutations_are_non_vacuously_rejected() -> None:
    PRIOR.test_manifest_and_summary_mutations_are_non_vacuously_rejected()


def test_requests_are_independently_derived_before_raw_request_comparison() -> None:
    PRIOR.test_requests_are_independently_derived_before_raw_request_comparison()


def test_fresh_complete_snapshot_and_hostile_reproduction() -> None:
    PRIOR.test_fresh_complete_snapshot_and_hostile_reproduction()
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    assert report["counts"]["child_launches"] == 486
    assert len(report["snapshots"]) == 63
    assert len(report["hostile"]) == 10
    report["discrepancy_policy"] = (
        "Per-case timing/RSS triples and range relations are transparent observations, "
        "not thresholds and not semantic or stable-count verdict inputs."
    )
    REPORT.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
