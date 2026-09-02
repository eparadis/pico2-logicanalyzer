"""B5 implementation proof: final-packet invariants and fresh measurements.

This test deliberately owns no decoder behaviour.  It checks that the accepted
B1--B4 packets are complete and ordered, and records/validates the one fresh
five-repetition measurement set used by the B5 candidate.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
DATA = ROOT / "testdata" / "decoders" / "cycle3"
EVIDENCE = ROOT / "testdata" / "evidence"
RAW = ROOT / "testdata" / "decoders" / "cycle3-raw" / "b5-final-measurements.json"
METHOD = ROOT / "docs" / "cycle-3-characterization-method.md"
THRESHOLDS = DATA / "threshold-proposal-round-4.json"
PROPOSAL_COMMIT = "b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0"
PROPOSAL_SHA256 = "98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c"
MANIFESTS = {
    "C3-B1": "3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae",
    "C3-B2": "2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602",
    "C3-B3": "4d17a6f0a1401799f1d7c0c65870744aada26eb2a3b1b8d5c723d447ceb4fac1",
    "C3-B4": "699443c5ed9cb2ddd668b4b486311e251647cadf5aeb3a435263dd2597e0f72c",
}
REGRESSION_IDS = {
    "worker_peak_rss_bytes", "parent_retained_growth_bytes", "successful_parent_total_ns",
    "launch_ns", "reap_ns", "child_load_ns", "child_import_ns", "child_decode_ns",
    "timeout_cleanup_total_ns", "terminate_to_reap_ns", "kill_to_reap_ns",
}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _checkpoint_text() -> str:
    return (ROOT / "docs" / "cycle-3-orchestration-progress.md").read_text(encoding="utf-8")


def test_b5_pre_manifest_packet_is_complete_and_b5_artifacts_are_absent() -> None:
    """Independently enforce final R1--R25/condition 1--17 traceability."""
    validator_spec = importlib.util.spec_from_file_location(
        "cycle3_validator", ROOT / "scripts" / "validate_cycle3_evidence.py"
    )
    assert validator_spec and validator_spec.loader
    validator = importlib.util.module_from_spec(validator_spec)
    validator_spec.loader.exec_module(validator)

    requirement_ids: set[str] = set()
    condition_ids: set[int] = set()
    progress = _checkpoint_text()
    offsets: list[int] = []
    for checkpoint, digest in MANIFESTS.items():
        path = EVIDENCE / f"{checkpoint.lower()}.json"
        assert path.is_file() and _sha(path) == digest
        manifest = _load(path)
        validator.validate(manifest)
        assert manifest["checkpoint"] == checkpoint
        requirement_ids.update(item["id"] for item in manifest["requirements"])
        condition_ids.update(item["id"] for item in manifest["stopping_conditions"])
        marker = f"### Checkpoint {checkpoint}"
        offsets.append(progress.index(marker))
        section = progress[progress.index(marker):]
        assert "State: Complete." in section[:7000]
        roles = manifest["roles"]
        assert len(
            {
                roles["implementation"],
                roles["verification"],
                roles["acceptance"],
                roles["manifest_verifier"],
            }
        ) == 4
    assert offsets == sorted(offsets)
    assert requirement_ids == {f"R{number}" for number in range(1, 26)}
    # Condition 15 is the B5-owned fresh-measurement gate below; every other
    # condition is already mapped by the accepted B1--B4 packets.
    assert condition_ids == set(range(1, 18)) - {15}

    # B5 may not pre-create any terminal-chain material before acceptance.
    prohibited = (
        EVIDENCE / "c3-b5.json",
        ROOT / "docs" / "cycle-3-completion.md",
        ROOT / "docs" / "cycle-3-completion-seal.md",
    )
    assert not any(path.exists() for path in prohibited)
    assert "Checkpoint C3-B5" not in progress


def _request(timeline: dict[str, Any]):
    from pico_logic_analyzer._decode.model import DecodeRequest

    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    transitions = timeline["transitions"]
    assert isinstance(transitions, dict)
    channels = tuple(mapping.values())
    state: dict[str, int] = {}
    changes: dict[int, list[tuple[str, int]]] = {}
    for wire, events in transitions.items():
        assert isinstance(events, list)
        for sample, value in events:
            changes.setdefault(sample, []).append((wire, value))
    for physical in channels:
        initial = [value for wire, value in changes[0] if wire == f"D{physical}"]
        assert len(initial) == 1
        state[f"D{physical}"] = initial[0]
    samples = []
    for sample in range(timeline["sample_count"]):
        for wire, value in changes.get(sample, []):
            state[wire] = value
        samples.append(
            sum((state[f"D{physical}"] & 1) << index for index, physical in enumerate(channels))
        )
    return DecodeRequest(
        timeline["decoder"], timeline["samplerate_hz"], channels, mapping,
        tuple(samples), timeline["trigger_index"], timeline["options"],
    )


def _measure() -> dict[str, Any]:
    from pico_logic_analyzer._decode.host import _decode_with_factory

    semantic = _load(DATA / "semantic-fixtures.json")
    selected = [
        next(item for item in semantic["timelines"] if item["decoder"] == decoder)
        for decoder in ("uart", "spi", "i2c")
    ]
    repetitions: list[dict[str, int | str]] = []
    for warmup in (True, False):
        for repetition in range(5):
            for timeline in selected:
                observations: list[Any] = []
                _decode_with_factory(
                    _request(timeline), subprocess.Popen, regression_observer=observations.append
                )
                assert len(observations) == 1
                observation = observations[0]
                row = {name: getattr(observation, name) for name in REGRESSION_IDS}
                row.update({"decoder": timeline["decoder"], "repetition": repetition})
                if not warmup:
                    repetitions.append(row)
    return {
        "schema": "cycle3-b5-final-measurements/v1",
        "environment": {
            "system": platform.system(),
            "machine": platform.machine(),
            "python": platform.python_version(),
        },
        "proposal_commit": PROPOSAL_COMMIT,
        "proposal_sha256": _sha(THRESHOLDS),
        "method_sha256": _sha(METHOD),
        "fixture_sha256": _sha(DATA / "semantic-fixtures.json"),
        "rows": repetitions,
    }


def test_b5_final_measurements_are_fresh_complete_and_within_approved_ceilings() -> None:
    """Record all observations (no retry/outlier deletion) or validate their exact set."""
    proposal = _load(THRESHOLDS)
    ceilings = {item["id"]: item["value"] for item in proposal["limits"]}
    assert _sha(THRESHOLDS) == PROPOSAL_SHA256
    assert proposal["round"] == 4 and len(REGRESSION_IDS) == 11
    assert ceilings["spi_max_word_size_bits"] == 8
    hard = [item for item in proposal["limits"] if item["kind"] == "hard-enforcement"]
    assert len(hard) == 18
    assert all(
        item["accept"] == item["value"] and item["reject"] == item["value"] + 1
        for item in hard
    )
    assert platform.system() == "Darwin" and platform.machine() == "x86_64"
    assert sys.version_info[:3] == (3, 12, 13)
    if os.environ.get("C3_B5_WRITE_MEASUREMENTS") == "1":
        RAW.write_text(
            json.dumps(_measure(), sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8"
        )
    assert RAW.is_file(), "fresh B5 raw measurements have not been collected"
    result = _load(RAW)
    assert result["proposal_commit"] == PROPOSAL_COMMIT
    assert result["proposal_sha256"] == PROPOSAL_SHA256
    assert result["method_sha256"] == _sha(METHOD)
    assert result["fixture_sha256"] == _sha(DATA / "semantic-fixtures.json")
    assert result["environment"] == {"system": "Darwin", "machine": "x86_64", "python": "3.12.13"}
    rows = result["rows"]
    assert len(rows) == 15
    assert {(row["decoder"], row["repetition"]) for row in rows} == {
        (decoder, rep) for decoder in ("uart", "spi", "i2c") for rep in range(5)
    }
    for row in rows:
        assert set(row) == REGRESSION_IDS | {"decoder", "repetition"}
        assert all(
            type(row[name]) is int and 0 <= row[name] <= ceilings[name]
            for name in REGRESSION_IDS
        )
