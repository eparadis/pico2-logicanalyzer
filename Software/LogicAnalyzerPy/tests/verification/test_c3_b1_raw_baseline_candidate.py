"""Independent reproduction of the immutable C3-B1 raw baseline."""

from __future__ import annotations

import hashlib
import json
import platform
import resource
import statistics
import sys
import time
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest

from tools.cycle3_characterize.runner import (
    RunnerFailure,
    _orchestration_execute_approved_snapshot,
    _private_last_evidence,
    load_caps,
    run_internal_probe,
    verify_launch_identity,
)

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
FIXTURE_ROOT = ROOT / "testdata" / "decoders" / "cycle3"
RAW_ROOT = ROOT / "testdata" / "decoders" / "cycle3-raw"
REPORT = Path("/private/tmp/c3-b1-raw-baseline-verifier-report.json")
CHANNEL_ORDER = {
    "uart": ("rx", "tx"),
    "spi": ("clk", "miso", "mosi", "cs"),
    "i2c": ("scl", "sda"),
}
HOSTILE = {
    "limits": "success",
    "malformed": "expected_failure",
    "items": "expected_failure",
    "stdout_flood": "expected_failure",
    "stderr_flood": "expected_failure",
    "diagnostic_flood": "expected_failure",
    "recursion_over": "expected_failure",
    "address_space_over": "success",
    "hang": "expected_failure",
    "ignore_term": "expected_failure",
}
SUBJECT_COMMIT = "2ae1e4335c38a5cf717491c7936f857292f71498"
SUBJECT_TREE = "772b13476c97a976eb3a304e9b87aec8011260ec"
COLLECTION_EXECUTABLE = (
    "/Users/ed/git/pico2-logicanalyzer/Software/LogicAnalyzerPy/.venv/bin/python"
)
EXPECTED_IDENTITY = {
    "binding_sha256": "144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98",
    "caps_sha256": "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d",
    "fixture_candidate_commit": "a98d328aab92f3dad66988fb70cc567946dc89d0",
    "fixture_candidate_tree": "450aadcf26bd6c74860872bfbf0a0a1b32d94f3b",
    "fixture_manifest_sha256": (
        "ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f"
    ),
    "runner_acceptance_commit": "bf1fc5eaa232bf09e66df77bd1c4be3e1ae4ffbd",
    "runner_acceptance_sha256": (
        "6dae8c73787dc7908e0ec311c84325251482d32073cc2fd6083147ead943e060"
    ),
    "runner_acceptance_tree": "5ec3ec00d09ab4ac5dd0d6ab258e19dcbb09ab64",
    "runner_candidate_commit": "ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a",
    "runner_candidate_tree": "457240c481afcdf20ef41a74208749e112efa9b6",
    "semantic_fixture_sha256": (
        "1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329"
    ),
}


def _load(name: str) -> dict[str, Any]:
    value = json.loads((RAW_ROOT / name).read_text())
    assert isinstance(value, dict)
    return value


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _derive_requests() -> list[dict[str, object]]:
    """Derive only from transitions/mapping/count/rate/options/provenance."""
    fixture = json.loads((FIXTURE_ROOT / "semantic-fixtures.json").read_text())
    provenance = json.loads((FIXTURE_ROOT / "provenance.json").read_text())
    file_sets = {item["decoder"]: item["paths"] for item in provenance["decoder_file_sets"]}
    derived = []
    for timeline in fixture["timelines"]:
        decoder = timeline["decoder"]
        mapping = timeline["mapping"]
        channels = [mapping.get(logical, 255) for logical in CHANNEL_ORDER[decoder]]
        states: dict[int, int] = {}
        changes: dict[int, list[tuple[int, int]]] = {}
        for pin_name, transitions in timeline["transitions"].items():
            pin = int(pin_name.removeprefix("D"))
            assert transitions and transitions[0][0] == 0
            for sample, value in transitions:
                changes.setdefault(sample, []).append((pin, value))
        samples = []
        for sample in range(timeline["sample_count"]):
            for pin, value in changes.get(sample, []):
                states[pin] = value
            assert all(physical == 255 or physical in states for physical in channels)
            samples.append(sum(value << pin for pin, value in states.items()))
        derived.append(
            {
                "id": timeline["id"],
                "request": {
                    "version": 1,
                    "decoder": decoder,
                    "files": list(file_sets[decoder]),
                    "samplerate": timeline["samplerate_hz"],
                    "channels": channels,
                    "samples": samples,
                    "options": timeline["options"],
                },
            }
        )
    assert len(derived) == 63
    return derived


def _triple(values: list[int]) -> dict[str, int]:
    return {"min": min(values), "median": int(statistics.median(values)), "max": max(values)}


def _canonical(path: Path) -> bool:
    value = json.loads(path.read_text(encoding="utf-8"))
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"
    return path.read_text(encoding="utf-8") == encoded


def _range_relation(fresh: dict[str, int], recorded: dict[str, int]) -> str:
    if fresh["max"] < recorded["min"]:
        return "fresh-lower-nonoverlap"
    if fresh["min"] > recorded["max"]:
        return "fresh-higher-nonoverlap"
    return "overlap"


def _assert_manifest(manifest: dict[str, Any], expected: dict[str, str]) -> None:
    assert set(manifest) == {
        "coverage", "decoders", "files", "identity", "repetitions", "schema",
        "timeline_count",
    }
    assert manifest["schema"] == "cycle3-raw-manifest/v1"
    assert manifest["timeline_count"] == 63 and manifest["repetitions"] == 5
    assert manifest["decoders"] == ["uart", "spi", "i2c"]
    assert manifest["identity"] == EXPECTED_IDENTITY
    assert manifest["files"] == {
        name: digest for name, digest in expected.items() if name != "manifest.json"
    }


def _assert_snapshot_summary(case: dict[str, Any]) -> None:
    repetitions = case["repetitions"]
    assert len(repetitions) == 5
    assert case["summary"]["successes"] == 5
    assert case["summary"]["failures"] == 0
    for field, triple in case["summary"]["counts"].items():
        assert triple == _triple([rep["counts"][field] for rep in repetitions])
    extractors = {
        "launch_ns": lambda rep: rep["launch_ns"],
        "reap_ns": lambda rep: rep["reap_ns"],
        "total_ns": lambda rep: rep["total_ns"],
        "parent_total_ns": lambda rep: rep["parent_total_ns"],
        "parent_before_ru_maxrss": lambda rep: rep["parent_before"]["ru_maxrss"],
        "parent_after_ru_maxrss": lambda rep: rep["parent_after"]["ru_maxrss"],
        "child_load_ns": lambda rep: rep["diagnostics"]["load_ns"],
        "child_import_ns": lambda rep: rep["diagnostics"]["import_ns"],
        "child_decode_ns": lambda rep: rep["diagnostics"]["decode_ns"],
        "child_maxrss": lambda rep: rep["diagnostics"]["maxrss"],
    }
    assert set(case["summary"]["fields"]) == set(extractors)
    for field, extract in extractors.items():
        assert case["summary"]["fields"][field] == _triple(
            [extract(rep) for rep in repetitions]
        )


def _optional_triple(values: list[int]) -> dict[str, int | None]:
    if not values:
        return {"min": None, "median": None, "max": None}
    return _triple(values)


def _assert_hostile_summary(case: dict[str, Any]) -> None:
    repetitions = case["repetitions"]
    observations = [rep["observation"] for rep in repetitions]
    successes = [observation for observation in observations if observation["ok"]]
    failures = [observation for observation in observations if not observation["ok"]]
    summary = case["summary"]
    assert len(repetitions) == 5
    assert summary["successes"] == len(successes)
    assert summary["failures"] == len(failures)
    count_fields = set().union(*(set(item.get("counts", {})) for item in successes))
    assert set(summary["counts"]) == count_fields
    for field in count_fields:
        assert summary["counts"][field] == _triple(
            [item["counts"][field] for item in successes]
        )

    def values(key: str) -> list[int]:
        result: list[int] = []
        selected = (
            observations
            if key in {"parent_before_ru_maxrss", "parent_after_ru_maxrss"}
            else successes
        )
        for observation in selected:
            diagnostics = observation.get("diagnostics")
            candidate: object | None
            if key.startswith("child_"):
                field = key.removeprefix("child_")
                candidate = diagnostics.get(field) if isinstance(diagnostics, dict) else None
            elif key == "parent_before_ru_maxrss":
                candidate = observation["parent_before"]["ru_maxrss"]
            elif key == "parent_after_ru_maxrss":
                candidate = observation["parent_after"]["ru_maxrss"]
            else:
                candidate = observation.get(key)
            if type(candidate) is int:
                result.append(candidate)
        return result

    assert set(summary["fields"]) == {
        "child_decode_ns", "child_import_ns", "child_load_ns", "child_maxrss",
        "launch_ns", "parent_after_ru_maxrss", "parent_before_ru_maxrss",
        "parent_total_ns", "reap_ns", "total_ns",
    }
    for field, triple in summary["fields"].items():
        assert triple == _optional_triple(values(field))

    for field, triple in summary["cleanup"].items():
        assert triple == _optional_triple(
            [item["cleanup"][field] for item in failures]
        )


def _semantic(value: dict[str, Any]) -> dict[str, Any]:
    diagnostics = json.loads(value["diagnostics"])
    for name in ("load_ns", "import_ns", "decode_ns", "maxrss"):
        diagnostics.pop(name)
    return {**value, "diagnostics": diagnostics}


def _recorded_semantic(observation: dict[str, Any]) -> dict[str, Any]:
    return _semantic(observation["value"])


def _run_snapshot(request: dict[str, object]) -> tuple[Any, int, int, Any]:
    before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    started = time.monotonic_ns()
    result = _orchestration_execute_approved_snapshot(request)
    parent_total = time.monotonic_ns() - started
    after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    evidence = _private_last_evidence()
    assert evidence.disposition == "completed"
    assert evidence.reaped and evidence.descriptors_closed
    assert len(evidence.closed_fds) == 2
    return result, parent_total, max(before, after), evidence


def test_candidate_identity_digest_environment_schema_and_summary_arithmetic() -> None:
    expected = {
        "environment.json": "fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34",
        "hostile-observations.json": (
            "d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080"
        ),
        "manifest.json": "7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e",
        "observations.json": "28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd",
        "requests.json": "fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c",
    }
    assert SUBJECT_COMMIT == "2ae1e4335c38a5cf717491c7936f857292f71498"
    assert SUBJECT_TREE == "772b13476c97a976eb3a304e9b87aec8011260ec"
    assert {name: _sha(RAW_ROOT / name) for name in expected} == expected
    assert all(_canonical(RAW_ROOT / name) for name in expected)
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
    assert environment["caps"] == load_caps()
    assert environment["warmup_rule"] == (
        "one unrecorded status-only warm-up before five independent retained "
        "repetitions per snapshot and hostile case"
    )
    assert environment["repetitions"] == 5
    assert len(environment["source_digests"]) == 9
    for relative, digest in environment["source_digests"].items():
        path = REPOSITORY / relative
        assert _sha(path) == digest
    verify_launch_identity()
    manifest = _load("manifest.json")
    _assert_manifest(manifest, expected)

    observation_document = _load("observations.json")
    assert set(observation_document) == {"schema", "observations"}
    assert observation_document["schema"] == "cycle3-raw-observations/v1"
    observations = observation_document["observations"]
    assert len(observations) == 63
    for case in observations:
        assert set(case) == {"id", "repetitions", "summary", "warmup_unrecorded"}
        assert case["warmup_unrecorded"] == {"ok": True}
        assert all(rep["ok"] for rep in case["repetitions"])
        _assert_snapshot_summary(case)

    hostile_document = _load("hostile-observations.json")
    assert set(hostile_document) == {"schema", "observations"}
    assert hostile_document["schema"] == "cycle3-raw-hostile/v1"
    assert len(hostile_document["observations"]) == 10
    for case in hostile_document["observations"]:
        assert set(case) == {
            "classification", "kind", "repetitions", "summary", "warmup_unrecorded"
        }
        _assert_hostile_summary(case)


def test_manifest_and_summary_mutations_are_non_vacuously_rejected() -> None:
    expected = {
        name: _sha(RAW_ROOT / name)
        for name in ("environment.json", "hostile-observations.json", "observations.json",
                     "requests.json", "manifest.json")
    }
    manifest = _load("manifest.json")
    mutated_manifest = deepcopy(manifest)
    mutated_manifest["files"]["requests.json"] = "0" * 64
    with pytest.raises(AssertionError):
        _assert_manifest(mutated_manifest, expected)
    case = _load("observations.json")["observations"][0]
    mutated_case = deepcopy(case)
    mutated_case["summary"]["counts"]["input_samples"]["max"] += 1
    with pytest.raises(AssertionError):
        _assert_snapshot_summary(mutated_case)
    hostile_case = _load("hostile-observations.json")["observations"][-1]
    mutated_hostile = deepcopy(hostile_case)
    mutated_hostile["summary"]["cleanup"]["kill_to_reap_ns"]["median"] += 1
    with pytest.raises(AssertionError):
        _assert_hostile_summary(mutated_hostile)


def test_requests_are_independently_derived_before_raw_request_comparison() -> None:
    independently_derived = _derive_requests()
    raw_requests = _load("requests.json")["requests"]
    assert independently_derived == raw_requests


def test_fresh_complete_snapshot_and_hostile_reproduction() -> None:
    derived = _derive_requests()
    recorded = {item["id"]: item for item in _load("observations.json")["observations"]}
    report: dict[str, Any] = {
        "schema": "cycle3-raw-independent-reproduction/v2",
        "candidate": {"commit": SUBJECT_COMMIT, "tree": SUBJECT_TREE},
        "counts": {
            "snapshot_cases": 63,
            "snapshot_warmups": 63,
            "snapshot_retained": 315,
            "hostile_cases": 10,
            "hostile_warmups": 10,
            "hostile_retained": 50,
            "recovery_warmups": 8,
            "recovery_retained": 40,
            "child_launches": 486,
        },
        "snapshots": {},
        "hostile": {},
    }
    for item in derived:
        case_id = item["id"]
        request = item["request"]
        _run_snapshot(request)  # explicitly unrecorded warm-up
        repetitions = []
        for _ in range(5):
            result, parent_total, parent_rss, cleanup = _run_snapshot(request)
            diagnostics = json.loads(result.diagnostics)
            repetitions.append(
                {
                    "semantic": _semantic(result.value),
                    "counts": dict(result.counts),
                    "timing": {
                        "launch_ns": result.launch_ns,
                        "reap_ns": result.reap_ns,
                        "total_ns": result.total_ns,
                        "parent_total_ns": parent_total,
                        "child_load_ns": diagnostics["load_ns"],
                        "child_import_ns": diagnostics["import_ns"],
                        "child_decode_ns": diagnostics["decode_ns"],
                    },
                    "memory": {
                        "child_maxrss": diagnostics["maxrss"],
                        "parent_ru_maxrss": parent_rss,
                    },
                    "cleanup": {
                        "disposition": cleanup.disposition,
                        "reaped": cleanup.reaped,
                        "descriptors_closed": cleanup.descriptors_closed,
                        "closed_fd_count": len(cleanup.closed_fds),
                    },
                }
            )
        historical = recorded[case_id]
        assert all(rep["semantic"] == _recorded_semantic(historical["repetitions"][0])
                   for rep in repetitions)
        stable_counts = ("input_samples", "request_bytes", "output_records", "binary_bytes",
                         "nested_depth", "nested_items", "stdout_bytes", "stderr_bytes")
        for field in stable_counts:
            expected = historical["repetitions"][0]["counts"][field]
            assert all(rep["counts"][field] == expected for rep in repetitions)
        assert all(
            rep["cleanup"]
            == {
                "disposition": "completed",
                "reaped": True,
                "descriptors_closed": True,
                "closed_fd_count": 2,
            }
            for rep in repetitions
        )
        fresh_timing = {field: _triple([rep["timing"][field] for rep in repetitions])
                        for field in repetitions[0]["timing"]}
        fresh_memory = {field: _triple([rep["memory"][field] for rep in repetitions])
                        for field in repetitions[0]["memory"]}
        recorded_fields = historical["summary"]["fields"]
        report["snapshots"][case_id] = {
            "fresh_timing": fresh_timing,
            "fresh_memory": fresh_memory,
            "recorded_fields": recorded_fields,
            "relations": {
                **{
                    field: _range_relation(triple, recorded_fields[field])
                    for field, triple in fresh_timing.items()
                },
                "child_maxrss": _range_relation(
                    fresh_memory["child_maxrss"], recorded_fields["child_maxrss"]
                ),
                "parent_ru_maxrss": {
                    "before": _range_relation(
                        fresh_memory["parent_ru_maxrss"],
                        recorded_fields["parent_before_ru_maxrss"],
                    ),
                    "after": _range_relation(
                        fresh_memory["parent_ru_maxrss"],
                        recorded_fields["parent_after_ru_maxrss"],
                    ),
                },
            },
        }

    recorded_hostile = {
        item["kind"]: item for item in _load("hostile-observations.json")["observations"]
    }
    assert {kind: value["classification"] for kind, value in recorded_hostile.items()} == HOSTILE
    for kind, classification in HOSTILE.items():
        failures = classification == "expected_failure"
        for repetition in range(6):  # one warm-up, then five retained repetitions
            retained_evidence = None
            recorded_rep = recorded_hostile[kind]["repetitions"][max(0, repetition - 1)]
            if failures:
                with pytest.raises(RunnerFailure):
                    run_internal_probe(kind)
                evidence = _private_last_evidence()
                retained_evidence = evidence
                assert evidence.reaped and evidence.descriptors_closed
                assert len(evidence.closed_fds) == 2
                assert evidence.disposition == recorded_rep["observation"]["cleanup"]["disposition"]
                if kind == "ignore_term":
                    assert evidence.kill_to_reap_ns > 0
                recovery = run_internal_probe("valid")
                recovery_evidence = _private_last_evidence()
                assert recovery_evidence.reaped and recovery_evidence.descriptors_closed
                assert len(recovery_evidence.closed_fds) == 2
                assert recovery.value == recorded_rep["recovery"]["value"]
                assert dict(recovery.counts) == recorded_rep["recovery"]["counts"]
            else:
                result = run_internal_probe(kind)
                evidence = _private_last_evidence()
                assert evidence.reaped and evidence.descriptors_closed
                assert len(evidence.closed_fds) == 2
                assert evidence.disposition == recorded_rep["observation"]["cleanup"]["disposition"]
                assert result.value == recorded_rep["observation"]["value"]
                assert dict(result.counts) == recorded_rep["observation"]["counts"]
            if repetition:
                evidence = retained_evidence or _private_last_evidence()
                report["hostile"].setdefault(kind, []).append(
                    {
                        "disposition": evidence.disposition,
                        "total_ns": evidence.total_ns,
                        "terminate_to_reap_ns": evidence.terminate_to_reap_ns,
                        "kill_to_reap_ns": evidence.kill_to_reap_ns,
                    }
                )
    assert set(report["snapshots"]) == set(recorded)
    assert set(report["hostile"]) == set(HOSTILE)
    REPORT.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
    assert not (ROOT / "tools/cycle3_characterize/__pycache__").exists()
