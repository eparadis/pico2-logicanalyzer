"""Independent R16 verification of inert cross-source decode equivalence."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer._decode.host import decode_private
from pico_logic_analyzer._decode.model import DecodeRequest, canonical_json
from pico_logic_analyzer.formats import import_csv_bytes
from pico_logic_analyzer.formats.replay import import_replay_bytes
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

ROOT = Path(__file__).resolve().parents[2]
SEMANTIC_PATH = ROOT / "testdata/decoders/cycle3/semantic-fixtures.json"
MATRIX_PATH = ROOT / "testdata/decoders/cycle3/option-matrix.json"
CANDIDATE_PATH = ROOT / "tests/implementation/test_c3_b3_cross_source_equivalence.py"
SEMANTIC = json.loads(SEMANTIC_PATH.read_text(encoding="utf-8"))
BY_ID = {row["id"]: row for row in SEMANTIC["timelines"]}

# Six distinct channel-requirement classes, not merely one row per decoder.
# UART TX intentionally translates the corpus's D9 witness to schema-1-safe D4.
CASES = (
    ("uart-rx-valid-default", {"rx": 4}),
    ("uart-tx-valid-default", {"tx": 4}),
    ("spi-mosi-mode0-word8", {"clk": 1, "mosi": 3}),
    ("spi-miso-mode3-word8", {"clk": 1, "miso": 2}),
    ("spi-cs-active-high-lsb-word1", {"clk": 1, "cs": 4, "mosi": 3}),
    ("i2c-shifted-start-address-ack-data-nack-stop", {"scl": 2, "sda": 5}),
)
IDS = tuple(range(8))
LABELS = tuple(f"physical-{index}" for index in IDS)


def _materialize(row: dict[str, object], target: dict[str, int]) -> tuple[int, ...]:
    """Interpret accepted transitions directly, then place logical wires physically."""
    source_mapping = row["mapping"]
    transitions = row["transitions"]
    assert isinstance(source_mapping, dict) and isinstance(transitions, dict)
    source_for_logical = {name: f"D{source_mapping[name]}" for name in target}
    scheduled: dict[int, list[tuple[int, int]]] = {}
    for logical, physical in target.items():
        for sample, level in transitions[source_for_logical[logical]]:
            scheduled.setdefault(sample, []).append((physical, level))
    levels = [0] * 8
    words = []
    for sample in range(row["sample_count"]):
        for physical, level in scheduled.get(sample, ()):
            levels[physical] = level
        words.append(sum(level << physical for physical, level in enumerate(levels)))
    return tuple(words)


def _memory(row: dict[str, object], target: dict[str, int]) -> CaptureResult:
    words = _materialize(row, target)
    rate, trigger = row["samplerate_hz"], row["trigger_index"]
    assert isinstance(rate, int) and isinstance(trigger, int)
    config = CaptureConfig(rate, trigger, len(words) - trigger, 0, "rising", IDS)
    device = DeviceInfo("LOGIC_ANALYZER_R16_INDEPENDENT_V6_0", rate, rate, len(words), 8)
    return CaptureResult(config, np.array(words, dtype=np.uint8), device, LABELS, LABELS)


def _metadata(capture: CaptureResult, schema: int) -> dict[str, object]:
    config = capture.config
    result: dict[str, object] = {
        "actual_count": len(capture.samples),
        "channel_ids": list(IDS),
        "channel_labels": list(LABELS),
        "channel_mapping": list(LABELS),
        "device": {"identity": "LOGIC_ANALYZER_R16_INDEPENDENT_V6_0", "capabilities": {
            "max_frequency_hz": config.sample_rate_hz,
            "blast_frequency_hz": config.sample_rate_hz,
            "buffer_size": len(capture.samples), "channel_count": 8}},
        "post_trigger_samples": config.post_trigger_samples,
        "pre_trigger_samples": config.pre_trigger_samples,
        "requested_count": len(capture.samples),
        "sample_rate_hz": config.sample_rate_hz,
        "schema_version": schema,
        "trigger_channel": 0, "trigger_edge": "rising",
        "trigger_index": capture.trigger_index,
    }
    if schema == 1:
        result["provisional"] = True
    else:
        result["firmware_mode"] = config.firmware_mode
        result["sample_dtype"] = str(config.sample_dtype)
    return result


def _replay(capture: CaptureResult, schema: int) -> bytes:
    # Both containers are hand-assembled rather than emitted by replay_bytes.
    encoded = json.dumps(_metadata(capture, schema), ensure_ascii=False,
                         sort_keys=True, separators=(",", ":")).encode()
    stream = io.BytesIO()
    np.savez(stream, samples=capture.samples,
             metadata=np.frombuffer(encoded, dtype=np.uint8))
    return stream.getvalue()


def _csv(capture: CaptureResult) -> bytes:
    # Explicit non-legacy labels ensure identity/rate come only from importer arguments.
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(("sample_index", "time_seconds", "trigger", *LABELS))
    rate, trigger = capture.config.sample_rate_hz, capture.trigger_index
    for index, word in enumerate(capture.samples):
        writer.writerow((index, format((index - trigger) / rate, ".12g"),
                         int(index == trigger),
                         *(int(word) >> bit & 1 for bit in IDS)))
    return stream.getvalue().encode()


def _identity(capture: CaptureResult) -> tuple[object, ...]:
    return (capture.config.sample_rate_hz, capture.config.channel_ids,
            capture.trigger_index, tuple(map(int, capture.samples)),
            capture.channel_labels, capture.channel_mapping)


def _decode(capture: CaptureResult, row: dict[str, object], mapping: dict[str, int]) -> bytes:
    request = DecodeRequest(row["decoder"], capture.config.sample_rate_hz,
                            capture.config.channel_ids, mapping,
                            tuple(map(int, capture.samples)), capture.trigger_index,
                            row["options"])
    return canonical_json(decode_private(request).to_dict())


@pytest.mark.parametrize(("timeline_id", "mapping"), CASES)
def test_four_inert_sources_have_exact_identity_and_canonical_result(
    monkeypatch: pytest.MonkeyPatch, timeline_id: str, mapping: dict[str, int]
) -> None:
    import serial

    monkeypatch.setattr(serial, "Serial", lambda *_a, **_k: pytest.fail("physical I/O"))
    row = BY_ID[timeline_id]
    memory = _memory(row, mapping)
    schema1_bytes, schema2_bytes, csv_bytes = (
        _replay(memory, 1), _replay(memory, 2), _csv(memory))
    schema1, schema2 = (import_replay_bytes(schema1_bytes),
                        import_replay_bytes(schema2_bytes))
    csv_capture = import_csv_bytes(csv_bytes, channel_ids=IDS,
                                   sample_rate_hz=memory.config.sample_rate_hz,
                                   trigger_channel=0, trigger_edge="rising")
    sources = (memory, schema1, schema2, csv_capture)
    assert len({hashlib.sha256(blob).digest()
                for blob in (schema1_bytes, schema2_bytes, csv_bytes)}) == 3
    assert [json.loads(np.load(io.BytesIO(blob))["metadata"].tobytes())["schema_version"]
            for blob in (schema1_bytes, schema2_bytes)] == [1, 2]
    assert all(_identity(source) == _identity(memory) for source in sources)
    results = [_decode(source, row, mapping) for source in sources]
    assert results == [results[0]] * 4


def test_hostile_identity_and_metadata_changes_are_observable() -> None:
    row, mapping = BY_ID["spi-mosi-mode0-word8"], {"clk": 1, "mosi": 3}
    baseline = _memory(row, mapping)
    baseline_result = _decode(baseline, row, mapping)

    changed_words = baseline.samples.copy()
    changed_words[30] ^= np.uint8(1 << 3)
    changed_sample = CaptureResult(baseline.config, changed_words, baseline.device,
                                   LABELS, LABELS)
    assert _identity(changed_sample) != _identity(baseline)
    assert _decode(changed_sample, row, mapping) != baseline_result

    remapped = _memory(row, {"clk": 1, "mosi": 2})
    assert _identity(remapped) != _identity(baseline)
    assert _decode(remapped, row, {"clk": 1, "mosi": 2}) != baseline_result

    reordered = import_csv_bytes(_csv(baseline), channel_ids=(1, 0, 2, 3, 4, 5, 6, 7),
                                 sample_rate_hz=1_152_000,
                                 trigger_channel=0, trigger_edge="rising")
    assert _identity(reordered) != _identity(baseline)

    for rate, trigger in ((1_152_001, 1), (1_152_000, 2)):
        config = CaptureConfig(rate, trigger, len(baseline.samples) - trigger,
                               0, "rising", IDS)
        hostile = CaptureResult(config, baseline.samples,
                                DeviceInfo("LOGIC_ANALYZER_R16_INDEPENDENT_V6_0", rate, rate,
                                           len(baseline.samples), 8), LABELS, LABELS)
        assert _identity(hostile) != _identity(baseline)
        assert _decode(hostile, row, mapping) != baseline_result

    renamed = import_csv_bytes(_csv(baseline).replace(b"physical-0", b"hostile-0"),
                               channel_ids=IDS, sample_rate_hz=1_152_000,
                               trigger_channel=0, trigger_edge="rising")
    assert _identity(renamed) != _identity(baseline)


def test_explicit_csv_identity_rate_trigger_and_serial_trap_are_enforced(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import serial

    from pico_logic_analyzer.model import ProtocolError

    monkeypatch.setattr(serial, "Serial", lambda *_a, **_k: pytest.fail("physical I/O"))
    capture = _memory(BY_ID["uart-rx-valid-default"], {"rx": 4})
    data = _csv(capture)
    with pytest.raises(ProtocolError, match="channel ids must be supplied"):
        import_csv_bytes(data, channel_ids=None, sample_rate_hz=1_152_000,
                         trigger_channel=0, trigger_edge="rising")
    with pytest.raises(ProtocolError, match="sample rate must be supplied"):
        import_csv_bytes(data, channel_ids=IDS, sample_rate_hz=None,
                         trigger_channel=0, trigger_edge="rising")
    with pytest.raises(ProtocolError, match="time does not match"):
        import_csv_bytes(data, channel_ids=IDS, sample_rate_hz=1_152_001,
                         trigger_channel=0, trigger_edge="rising")
    duplicate_trigger = data.replace(b"0,-8.68055555556e-07,0,", b"0,-8.68055555556e-07,1,", 1)
    with pytest.raises(ProtocolError, match="one trigger row"):
        import_csv_bytes(duplicate_trigger, channel_ids=IDS,
                         sample_rate_hz=1_152_000, trigger_channel=0,
                         trigger_edge="rising")


def test_candidate_corpus_evidence_and_six_class_scope_are_pinned() -> None:
    assert hashlib.sha256(CANDIDATE_PATH.read_bytes()).hexdigest() == (
        "90754fb7a3d32da70c1526bde29dcc359d2a9e17ac21ea0a97273650f5bd1159")
    assert hashlib.sha256(SEMANTIC_PATH.read_bytes()).hexdigest() == (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094")
    assert hashlib.sha256(MATRIX_PATH.read_bytes()).hexdigest() == (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209")
    assert "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9" in (
        ROOT / "testdata/evidence/c3-b1.json").read_text()
    assert hashlib.sha256((ROOT / "testdata/evidence/c3-b2.json").read_bytes()).hexdigest() == (
        "2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602")
    assert len(SEMANTIC["timelines"]) == 63 and len(CASES) == 6
    assert {BY_ID[name]["decoder"] for name, _ in CASES} == {"uart", "spi", "i2c"}
    assert BY_ID["uart-tx-valid-default"]["mapping"] == {"tx": 9}
    assert dict(CASES)["uart-tx-valid-default"] == {"tx": 4}
