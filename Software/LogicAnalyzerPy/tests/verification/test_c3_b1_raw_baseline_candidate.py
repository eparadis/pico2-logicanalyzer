"""Independent reproduction of the immutable C3-B1 raw baseline."""

from __future__ import annotations

import hashlib
import json
import resource
import statistics
import sys
import time
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


def _semantic(value: dict[str, Any]) -> dict[str, Any]:
    diagnostics = json.loads(value["diagnostics"])
    for name in ("load_ns", "import_ns", "decode_ns", "maxrss"):
        diagnostics.pop(name)
    return {**value, "diagnostics": diagnostics}


def _recorded_semantic(observation: dict[str, Any]) -> dict[str, Any]:
    return _semantic(observation["value"])


def _run_snapshot(request: dict[str, object]) -> tuple[Any, int, int]:
    before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    started = time.monotonic_ns()
    result = _orchestration_execute_approved_snapshot(request)
    parent_total = time.monotonic_ns() - started
    after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return result, parent_total, max(before, after)


def test_candidate_identity_digest_environment_schema_and_summary_arithmetic() -> None:
    expected = {
        "environment.json": "14da4608cf882286a8f62f0e59f596d91753244b619046d14d7f445a89012a4f",
        "hostile-observations.json": (
            "c956be536fc1fd5c23ebfd33b6bb51377e0f806ace57dfc02fc8888521f801ad"
        ),
        "manifest.json": "0706b84a0965a36e5b5d20c35c6d4ba9ab774f3bb7532e29f322dcd5a76d0efa",
        "observations.json": "a282ccd92ffa27ceda4624d6138de61d48314a0b352f004e3d0770c8b3bc2f03",
        "requests.json": "fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c",
    }
    assert {name: _sha(RAW_ROOT / name) for name in expected} == expected
    environment = _load("environment.json")
    assert environment["runner_candidate_commit"] == "48d139f86aabcfa3e34567473c05ade13340107f"
    assert environment["runner_candidate_tree"] == "fc36f73089ee6d1c86e3bd6c922c44dffe15477b"
    assert environment["executable"] == sys.executable
    assert environment["python"] == sys.version
    assert environment["caps"] == load_caps()
    assert environment["warmup"] == "one status-only unrecorded run per case"
    assert environment["repetitions"] == 5
    for relative, digest in environment["digests"].items():
        path = REPOSITORY / relative if relative.startswith("Software/") else ROOT / relative
        assert _sha(path) == digest
    verify_launch_identity()
    manifest = _load("manifest.json")
    assert manifest["timeline_count"] == 63 and manifest["repetitions"] == 5
    assert manifest["files"] == {
        name: digest for name, digest in expected.items() if name != "manifest.json"
    }

    observations = _load("observations.json")["observations"]
    assert len(observations) == 63
    for case in observations:
        assert case["warmup_unrecorded"] == {"ok": True}
        assert len(case["repetitions"]) == 5 and all(rep["ok"] for rep in case["repetitions"])
        assert case["summary"]["successes"] == 5 and case["summary"]["failures"] == 0
        for field, triple in case["summary"]["counts"].items():
            assert triple == _triple([rep["counts"][field] for rep in case["repetitions"]])


def test_requests_are_independently_derived_before_raw_request_comparison() -> None:
    independently_derived = _derive_requests()
    raw_requests = _load("requests.json")["requests"]
    assert independently_derived == raw_requests


def test_fresh_complete_snapshot_and_hostile_reproduction() -> None:
    derived = _derive_requests()
    recorded = {item["id"]: item for item in _load("observations.json")["observations"]}
    report: dict[str, Any] = {"snapshots": {}, "hostile": {}}
    for item in derived:
        case_id = item["id"]
        request = item["request"]
        _run_snapshot(request)  # explicitly unrecorded warm-up
        repetitions = []
        for _ in range(5):
            result, parent_total, parent_rss = _run_snapshot(request)
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
        fresh_timing = {field: _triple([rep["timing"][field] for rep in repetitions])
                        for field in repetitions[0]["timing"]}
        fresh_memory = {field: _triple([rep["memory"][field] for rep in repetitions])
                        for field in repetitions[0]["memory"]}
        report["snapshots"][case_id] = {
            "fresh_timing": fresh_timing,
            "fresh_memory": fresh_memory,
            "recorded_fields": historical["summary"]["fields"],
        }

    recorded_hostile = {
        item["kind"]: item for item in _load("hostile-observations.json")["observations"]
    }
    assert {kind: value["classification"] for kind, value in recorded_hostile.items()} == HOSTILE
    for kind, classification in HOSTILE.items():
        failures = classification == "expected_failure"
        for repetition in range(6):  # one warm-up, then five retained repetitions
            retained_evidence = None
            if failures:
                with pytest.raises(RunnerFailure):
                    run_internal_probe(kind)
                evidence = _private_last_evidence()
                retained_evidence = evidence
                assert evidence.reaped and evidence.descriptors_closed
                assert len(evidence.closed_fds) == 2
                if kind == "hang":
                    assert evidence.disposition == "terminated-and-reaped"
                if kind == "ignore_term":
                    assert evidence.disposition == "killed-and-reaped"
                    assert evidence.kill_to_reap_ns > 0
                recovery = run_internal_probe("valid")
                assert recovery.value["version"] == 1 and _private_last_evidence().reaped
            else:
                result = run_internal_probe(kind)
                assert result.value["version"] == 1 and _private_last_evidence().reaped
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
    REPORT.write_text(json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n")
    assert not (ROOT / "tools/cycle3_characterize/__pycache__").exists()
