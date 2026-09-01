"""R16 integration proof: inert sources reach one private decoder boundary.

This is deliberately a source-conversion test, not another decoder oracle: the
accepted C3-B1 semantic corpus supplies waveforms, and all observations cross
the frozen private host through ``DecodeRequest``/``decode_private``.
"""

from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "testdata" / "decoders" / "cycle3"
SEMANTIC_PATH = DATA / "semantic-fixtures.json"
MATRIX_PATH = DATA / "option-matrix.json"
SEMANTIC = json.loads(SEMANTIC_PATH.read_text(encoding="utf-8"))
TIMELINES = {item["id"]: item for item in SEMANTIC["timelines"]}

# This is the smallest complete protocol/source matrix: UART's two optional
# directions, SPI's MISO/MOSI/CS alternatives, and I2C's complete two-wire
# mapping.  ``uart-tx-valid-default`` is the only selected D0--D7-ineligible
# source; its D9 signal is independently represented on D4 for schema 1.
REPRESENTATIVES = (
    ("uart-rx-valid-default", {"rx": 4}),
    ("uart-tx-valid-default", {"tx": 4}),
    ("spi-mosi-mode0-word8", {"clk": 1, "mosi": 3}),
    ("spi-miso-mode3-word8", {"clk": 1, "miso": 2}),
    ("spi-cs-active-high-lsb-word1", {"clk": 1, "cs": 4, "mosi": 3}),
    ("i2c-shifted-start-address-ack-data-nack-stop", {"scl": 2, "sda": 5}),
)
CHANNEL_IDS = tuple(range(8))
LABELS = tuple(f"D{channel}" for channel in CHANNEL_IDS)


def _wave_words(timeline: dict[str, object], mapping: dict[str, int]) -> tuple[int, ...]:
    """Build the eight physical wires directly from C3-B1 transitions."""
    source_mapping = timeline["mapping"]
    transitions = timeline["transitions"]
    assert isinstance(source_mapping, dict) and isinstance(transitions, dict)
    source_to_target = {
        f"D{source_mapping[pin]}": f"D{physical}" for pin, physical in mapping.items()
    }
    events: dict[int, list[tuple[str, int]]] = {}
    for source_wire, changes in transitions.items():
        if source_wire not in source_to_target:
            continue
        assert isinstance(changes, list)
        for sample, value in changes:
            events.setdefault(sample, []).append((source_to_target[source_wire], value))
    state = {label: 0 for label in LABELS}
    for label in tuple(source_to_target.values()):
        initial = [value for wire, value in events[0] if wire == label]
        assert len(initial) == 1
        state[label] = initial[0]
    words: list[int] = []
    sample_count = timeline["sample_count"]
    assert isinstance(sample_count, int)
    for sample in range(sample_count):
        for wire, value in events.get(sample, []):
            state[wire] = value
        words.append(sum((state[f"D{bit}"] & 1) << bit for bit in CHANNEL_IDS))
    return tuple(words)


def _capture(timeline: dict[str, object], mapping: dict[str, int]):
    from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

    rate = timeline["samplerate_hz"]
    trigger = timeline["trigger_index"]
    assert isinstance(rate, int) and isinstance(trigger, int)
    words = _wave_words(timeline, mapping)
    config = CaptureConfig(rate, trigger, len(words) - trigger, 0, "rising", CHANNEL_IDS)
    return CaptureResult(
        config,
        np.asarray(words, dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_R16_INERT_V6_0", rate, rate, len(words), 8),
        LABELS,
        LABELS,
    )


def _schema1_bytes(timeline: dict[str, object], mapping: dict[str, int]) -> bytes:
    """Independently construct the legacy, fixed-eight-channel replay container."""
    capture = _capture(timeline, mapping)
    rate = capture.config.sample_rate_hz
    trigger, count = capture.trigger_index, len(capture.samples)
    metadata = {
        "actual_count": count,
        "channel_ids": list(CHANNEL_IDS),
        "channel_labels": list(LABELS),
        "channel_mapping": list(LABELS),
        "device": {
            "capabilities": {
                "blast_frequency_hz": rate,
                "buffer_size": count,
                "channel_count": 8,
                "max_frequency_hz": rate,
            },
            "identity": "LOGIC_ANALYZER_R16_SCHEMA1_V6_0",
        },
        "post_trigger_samples": count - trigger,
        "pre_trigger_samples": trigger,
        "provisional": True,
        "requested_count": count,
        "sample_rate_hz": rate,
        "schema_version": 1,
        "trigger_channel": 0,
        "trigger_edge": "rising",
        "trigger_index": trigger,
    }
    encoded = json.dumps(metadata, sort_keys=True, separators=(",", ":")).encode("utf-8")
    output = io.BytesIO()
    np.savez(output, samples=capture.samples, metadata=np.frombuffer(encoded, dtype=np.uint8))
    return output.getvalue()


def _request(capture, timeline: dict[str, object], mapping: dict[str, int]):
    from pico_logic_analyzer._decode.model import DecodeRequest

    return DecodeRequest(
        timeline["decoder"],
        capture.config.sample_rate_hz,
        capture.config.channel_ids,
        mapping,
        tuple(int(word) for word in capture.samples),
        capture.trigger_index,
        timeline["options"],
    )


def _capture_identity(capture) -> tuple[object, ...]:
    return (
        capture.config.sample_rate_hz,
        capture.config.channel_ids,
        capture.trigger_index,
        tuple(int(word) for word in capture.samples),
        capture.channel_labels,
        capture.channel_mapping,
    )


def _with_config(capture, *, rate: int | None = None, trigger: int | None = None):
    from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

    chosen_rate = capture.config.sample_rate_hz if rate is None else rate
    chosen_trigger = capture.trigger_index if trigger is None else trigger
    config = CaptureConfig(
        chosen_rate, chosen_trigger, len(capture.samples) - chosen_trigger, 0, "rising", CHANNEL_IDS
    )
    device = DeviceInfo(
        capture.device.identity,
        max(chosen_rate, capture.device.max_frequency_hz),
        max(chosen_rate, capture.device.blast_frequency_hz),
        capture.device.buffer_size,
        capture.device.channel_count,
    )
    return CaptureResult(
        config, capture.samples, device, capture.channel_labels, capture.channel_mapping
    )


def _schema_version(data: bytes) -> int:
    with np.load(io.BytesIO(data), allow_pickle=False) as archive:
        return json.loads(archive["metadata"].tobytes())["schema_version"]


@pytest.mark.parametrize(("timeline_id", "mapping"), REPRESENTATIVES)
def test_r16_all_inert_source_paths_produce_byte_identical_private_results(
    monkeypatch: pytest.MonkeyPatch, timeline_id: str, mapping: dict[str, int]
) -> None:
    import serial

    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json
    from pico_logic_analyzer.formats import csv_bytes, import_csv_bytes, replay_bytes
    from pico_logic_analyzer.formats.replay import import_replay_bytes

    timeline = TIMELINES[timeline_id]
    # Any accidental serial/live-capture route makes this proof fail immediately.
    monkeypatch.setattr(serial, "Serial", lambda *_args, **_kwargs: pytest.fail("serial opened"))

    memory = _capture(timeline, mapping)
    schema1_data = _schema1_bytes(timeline, mapping)
    schema2_data = replay_bytes(_capture(timeline, mapping))
    csv_data = csv_bytes(_capture(timeline, mapping))
    schema1 = import_replay_bytes(schema1_data)
    schema2 = import_replay_bytes(schema2_data)
    csv = import_csv_bytes(
        csv_data,
        channel_ids=CHANNEL_IDS,
        sample_rate_hz=memory.config.sample_rate_hz,
        trigger_channel=0,
        trigger_edge="rising",
    )

    assert _schema_version(schema1_data) == 1
    assert _schema_version(schema2_data) == 2
    source_digests = {
        hashlib.sha256(data).digest() for data in (schema1_data, schema2_data, csv_data)
    }
    assert len(source_digests) == 3
    assert _capture_identity(memory) == _capture_identity(schema1) == _capture_identity(schema2)
    assert _capture_identity(memory) == _capture_identity(csv)
    outputs = tuple(
        canonical_json(decode_private(_request(source, timeline, mapping)).to_dict())
        for source in (memory, schema1, schema2, csv)
    )
    assert len(set(outputs)) == 1


def test_r16_hostile_capture_changes_cannot_silently_claim_equivalence() -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json
    from pico_logic_analyzer.formats import csv_bytes, import_csv_bytes
    from pico_logic_analyzer.model import CaptureResult

    timeline = TIMELINES["spi-mosi-mode0-word8"]
    mapping = {"clk": 1, "mosi": 3}
    baseline = _capture(timeline, mapping)
    baseline_bytes = canonical_json(decode_private(_request(baseline, timeline, mapping)).to_dict())
    # Sample 30 is a selected MOSI bit edge in this accepted SPI witness.  Keep
    # all metadata coherent while flipping only that packed D3 bit.
    changed_samples = baseline.samples.copy()
    changed_samples[30] ^= np.uint8(1 << 3)
    changed_sample = CaptureResult(
        baseline.config,
        changed_samples,
        baseline.device,
        baseline.channel_labels,
        baseline.channel_mapping,
    )
    assert _capture_identity(changed_sample) != _capture_identity(baseline)
    changed_sample_bytes = canonical_json(
        decode_private(_request(changed_sample, timeline, mapping)).to_dict()
    )
    assert changed_sample_bytes != baseline_bytes
    changed_mapping = {"clk": 1, "mosi": 2}
    changed_capture = _capture(timeline, changed_mapping)
    assert _capture_identity(changed_capture) != _capture_identity(baseline)
    changed_mapping_bytes = canonical_json(
        decode_private(_request(changed_capture, timeline, changed_mapping)).to_dict()
    )
    assert changed_mapping_bytes != baseline_bytes
    changed_order = import_csv_bytes(
        csv_bytes(baseline),
        channel_ids=(1, 0, 2, 3, 4, 5, 6, 7),
        sample_rate_hz=baseline.config.sample_rate_hz,
        trigger_channel=0,
        trigger_edge="rising",
    )
    assert _capture_identity(changed_order) != _capture_identity(baseline)
    changed_rate = _with_config(baseline, rate=baseline.config.sample_rate_hz + 1)
    changed_rate_bytes = canonical_json(
        decode_private(_request(changed_rate, timeline, mapping)).to_dict()
    )
    assert changed_rate_bytes != baseline_bytes
    changed_trigger = _with_config(baseline, trigger=baseline.trigger_index + 1)
    changed_trigger_bytes = canonical_json(
        decode_private(_request(changed_trigger, timeline, mapping)).to_dict()
    )
    assert changed_trigger_bytes != baseline_bytes
    changed_metadata = import_csv_bytes(
        csv_bytes(baseline).replace(b"D0", b"wire0"),
        channel_ids=CHANNEL_IDS,
        sample_rate_hz=baseline.config.sample_rate_hz,
        trigger_channel=0,
        trigger_edge="rising",
    )
    assert _capture_identity(changed_metadata) != _capture_identity(baseline)


def test_r16_corpus_and_evidence_identities_and_coverage_are_frozen() -> None:
    assert len(SEMANTIC["timelines"]) == 63
    assert {TIMELINES[timeline_id]["decoder"] for timeline_id, _mapping in REPRESENTATIVES} == {
        "uart",
        "spi",
        "i2c",
    }
    assert hashlib.sha256(SEMANTIC_PATH.read_bytes()).hexdigest() == (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    )
    assert hashlib.sha256(MATRIX_PATH.read_bytes()).hexdigest() == (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209"
    )
    assert "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9" in (
        ROOT / "testdata" / "evidence" / "c3-b1.json"
    ).read_text(encoding="utf-8")
    b2_digest = hashlib.sha256(
        (ROOT / "testdata" / "evidence" / "c3-b2.json").read_bytes()
    ).hexdigest()
    assert b2_digest == ("2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602")
