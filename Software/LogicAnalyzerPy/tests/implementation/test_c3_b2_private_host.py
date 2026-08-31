from __future__ import annotations

import json
import os
import subprocess
from collections import namedtuple
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
MATRIX = json.loads((ROOT / "testdata/decoders/cycle3/option-matrix.json").read_text())
VECTORS = json.loads((ROOT / "testdata/decoders/cycle3/typed-vectors.json").read_text())
THRESHOLDS = json.loads(
    (ROOT / "testdata/decoders/cycle3/threshold-proposal-round-4.json").read_text()
)
SEMANTIC = json.loads((ROOT / "testdata/decoders/cycle3/semantic-fixtures.json").read_text())


def _request(decoder: str, options: dict[str, object] | None = None):
    from pico_logic_analyzer._decode.model import DecodeRequest

    mappings = {
        "uart": {"rx": 7},
        "spi": {"clk": 7, "miso": 2},
        "i2c": {"scl": 7, "sda": 2},
    }
    return DecodeRequest(decoder, 1, (7, 2, 19), mappings[decoder], (0,), 0, options or {})


def test_private_host_exposes_only_internal_immutable_request_model() -> None:
    from pico_logic_analyzer._decode.model import DecodeRequest, HostFailure

    request = _request("uart")
    assert request.decoder == "uart"
    with pytest.raises(HostFailure):
        DecodeRequest("unknown", 0, (), {}, (), 0, {})


@pytest.mark.parametrize("decoder", ["uart", "spi", "i2c"])
def test_default_options_and_mapping_materialize_immutably(
    decoder: str,
) -> None:
    mutable: dict[str, object] = {}
    request = _request(decoder, mutable)
    mutable["bad"] = True
    assert "bad" not in request.options


@pytest.mark.parametrize("options", [{"wordsize": True}, {"wordsize": 9}, {"cpol": 2}])
def test_spi_option_type_and_boundary_rejections(options: dict[str, object]) -> None:
    from pico_logic_analyzer._decode.model import RequestFailure

    with pytest.raises(RequestFailure):
        _request("spi", options)


@pytest.mark.parametrize(
    "options",
    [{"data_bits": True}, {"sample_point": 100}, {"rx_packet_delim": 256}, {"rx_packet_len": 0}],
)
def test_uart_option_rejections(options: dict[str, object]) -> None:
    from pico_logic_analyzer._decode.model import RequestFailure

    with pytest.raises(RequestFailure):
        _request("uart", options)


def test_private_tagged_values_and_failure_schema_are_closed() -> None:
    from pico_logic_analyzer._decode.model import (
        DecodeFailure,
        ResultFailure,
        SpiData,
        tagged_value,
    )

    assert tagged_value([1, b"x"])["tag"] == "list"
    assert tagged_value(b"\x00") == {"tag": "bytes", "value": "AA=="}
    assert tagged_value(SpiData(0, 1, 2)) == {"tag": "spi-data", "ss": 0, "es": 1, "val": 2}
    assert DecodeFailure("snapshot", "safe").to_dict()["schema"].endswith("/v1")
    with pytest.raises(ResultFailure):
        tagged_value(float("inf"))


def test_exact_loaded_spi_data_type_normalizes_before_generic_tuple_handling() -> None:
    from pico_logic_analyzer._decode.compat import OUTPUT_PYTHON, ApiV3Host
    from pico_logic_analyzer._decode.loader import load_frozen_decoder

    descriptor = load_frozen_decoder("spi")
    assert descriptor.spi_data_type is not None
    host = ApiV3Host(
        ("clk", "miso", "mosi", "cs"),
        {"clk": 7, "mosi": 2},
        (7, 2),
        (0,),
        1,
        0,
        {},
        descriptor.spi_data_type,
    )
    output = host.register(OUTPUT_PYTHON)
    host.put(0, 0, output, descriptor.spi_data_type(0, 0, 1))
    assert host.records[0].to_dict()["value"] == {"tag": "spi-data", "ss": 0, "es": 0, "val": 1}


def test_failure_taxonomy_and_safe_message_are_closed() -> None:
    from pico_logic_analyzer._decode.model import DecodeFailure, RequestFailure

    expected = {
        "snapshot",
        "import",
        "ipc",
        "decoder",
        "recursion",
        "memory",
        "process-exit",
        "timeout",
        "cancelled",
        "output-limit",
    }
    assert {DecodeFailure(code, "safe").code for code in expected} == expected
    with pytest.raises(RequestFailure):
        DecodeFailure("decoder", "Traceback /private/tmp")


def test_capture_order_resolves_mapping_and_rejects_sentinel_or_packed_overflow() -> None:
    from pico_logic_analyzer._decode.model import DecodeRequest, RequestFailure

    request = DecodeRequest("spi", 1, (19, 7, 2), {"clk": 7, "miso": 2}, (7,), 0, {})
    assert dict(request.channel_positions) == {"clk": 1, "miso": 2}
    for mapping in ({"clk": 7}, {"clk": 7, "miso": 255}, {"clk": 7, "miso": 7}):
        with pytest.raises(RequestFailure):
            DecodeRequest("spi", 1, (7, 2, 19), mapping, (0,), 0, {})
    with pytest.raises(RequestFailure):
        DecodeRequest("uart", 1, (7,), {"rx": 7}, (2,), 0, {})


def test_option_matrix_rejects_every_unsupported_row() -> None:
    from pico_logic_analyzer._decode.model import RequestFailure

    rejected = [row for row in MATRIX["rows"] if row["disposition"] == "unsupported"]
    assert rejected
    for row in rejected:
        options = dict(row.get("selected_width_context") or {})
        options[row["option"]] = row["value"]
        with pytest.raises(RequestFailure, match="options rejected"):
            _request(row["decoder"], options)


def test_option_matrix_materializes_supported_direct_rows() -> None:
    supported = [
        row
        for row in MATRIX["rows"]
        if row["disposition"] in {"direct-fixture", "static-equivalence"}
        and row["option"] not in {"duplicate-cli"}
    ]
    assert supported
    for row in supported:
        options = dict(row.get("selected_width_context") or {})
        options[row["option"]] = row["value"]
        request = _request(row["decoder"], options)
        assert request.options[row["option"]] == row["value"]


def test_closed_tag_vectors_and_canonical_result_shape() -> None:
    from pico_logic_analyzer._decode.model import (
        AnnotationDeclaration,
        CaptureIdentity,
        DecodeRecord,
        DecodeResult,
        RationalTime,
        RecordTime,
        SpiData,
        canonical_json,
        tagged_value,
    )

    raw_values = [None, True, 1, 1.25, "x", b"x", [1], (1,), SpiData(0, 1, 2)]
    assert {tagged_value(value)["tag"] for value in raw_values} == set(VECTORS["python_value_tags"])
    result = DecodeResult(
        "uart",
        "a" * 64,
        1,
        CaptureIdentity(1, 0, (7,)),
        {"rx": 7},
        {"baudrate": 1},
        (AnnotationDeclaration("output", 0, "output"),),
        (
            DecodeRecord(
                0,
                0,
                1,
                0,
                "python",
                SpiData(0, 0, 1),
                RecordTime(RationalTime(0, 1), RationalTime(0, 1)),
                RecordTime(RationalTime(0, 1), RationalTime(0, 1)),
            ),
        ),
    )
    encoded = canonical_json(result.to_dict())
    assert json.loads(encoded)["schema"] == VECTORS["schema"]
    assert encoded.endswith(b"\n")


def test_typed_vectors_round_trip_to_exact_canonical_golden_bytes() -> None:
    from pico_logic_analyzer._decode.model import canonical_json, decode_result_from_dict

    for golden in VECTORS["cli_utf8_goldens"]:
        literal = json.loads(bytes.fromhex(golden["hex"]))
        expected = bytes.fromhex(golden["hex"])
        assert canonical_json(decode_result_from_dict(literal).to_dict()) == expected


def _compat(spi_data_type: type[object] | None = None):
    from pico_logic_analyzer._decode.compat import ApiV3Host

    return ApiV3Host(
        ("clk", "miso", "mosi", "cs"),
        {"clk": 7, "mosi": 2},
        (7, 2),
        (0, 1, 3, 2, 3),
        10,
        1,
        {},
        spi_data_type,
    )


def test_api_v3_wait_edge_semantics_and_optional_sentinel() -> None:
    from pico_logic_analyzer._decode.compat import EndOfInput

    host = _compat()
    assert host.has_channel(0) is True
    assert host.has_channel(1) is False
    assert host.wait({}) == (0, 255, 0, 255)
    assert host.samplenum == 0 and host.matched == (True,)
    assert host.wait({}) == (1, 255, 0, 255)
    assert host.wait({"skip": 0}) == (1, 255, 0, 255)
    assert host.wait([{0: "r"}, {0: "e"}]) == (0, 255, 1, 255)
    assert host.matched == (False, True)
    assert host.wait({0: "r"}) == (1, 255, 1, 255)
    with pytest.raises(EndOfInput):
        host.wait({0: "r"})

    conjunction = _compat()
    assert conjunction.wait({2: "h", 0: "f"}) == (0, 255, 1, 255)
    assert conjunction.matched == (True,)
    assert conjunction.wait({0: "r"}) == (1, 255, 1, 255)


def test_round_four_parent_timing_and_spi_wordsize_limits_are_exact() -> None:
    from pico_logic_analyzer._decode.model import HARD_LIMITS, REGRESSION_LIMITS

    assert REGRESSION_LIMITS["parent_retained_growth_bytes"] == 33_554_432
    assert REGRESSION_LIMITS["successful_parent_total_ns"] == 1_300_000_000
    assert REGRESSION_LIMITS["launch_ns"] == 50_000_000
    assert HARD_LIMITS["spi_max_word_size_bits"] == 8


def test_all_twenty_nine_operator_approved_limit_literals_match_round_four() -> None:
    from pico_logic_analyzer._decode.model import HARD_LIMITS, REGRESSION_LIMITS

    expected = {item["id"]: item["value"] for item in THRESHOLDS["limits"]}
    assert len(expected) == 29
    assert {**HARD_LIMITS, **REGRESSION_LIMITS} == expected


@pytest.mark.parametrize(
    "condition",
    [None, [], {"skip": -1}, {"skip": 0, 0: "r"}, {0: "l"}, {4: "r"}, {"0": "r"}],
)
def test_api_v3_wait_rejects_outside_focused_surface(condition: object) -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host
    from pico_logic_analyzer._decode.model import ResultFailure

    with pytest.raises(ResultFailure):
        _compat().wait(condition)
    with pytest.raises(ResultFailure):
        ApiV3Host(("rx",), {"rx": 255}, (7,), (0,), 1, 0, {})


def test_api_v3_register_put_normalizes_request_wide_order() -> None:
    from pico_logic_analyzer._decode.compat import (
        OUTPUT_ANN,
        OUTPUT_BINARY,
        OUTPUT_META,
        OUTPUT_PYTHON,
    )
    from pico_logic_analyzer._decode.model import ResultFailure

    host = _compat()
    python_id = host.register(OUTPUT_PYTHON)
    annotation_id = host.register(OUTPUT_ANN)
    binary_id = host.register(OUTPUT_BINARY)
    metadata_id = host.register(OUTPUT_META, meta=(int, "name", "description"))
    host.put(0, 1, python_id, ("x", b"\x00"))
    host.put(0, 1, annotation_id, [0, ["A"]])
    host.put(0, 5, binary_id, (1, b"\x00"))
    host.put(5, 5, metadata_id, 7)
    assert [record.kind for record in host.records] == [
        "python",
        "annotation",
        "binary",
        "metadata",
    ]
    assert [record.emission_index for record in host.records] == [0, 1, 2, 3]
    assert host.records[2].to_dict()["value"] == {"class_index": 1, "data_base64": "AA=="}
    with pytest.raises(ResultFailure):
        host.put(0, 6, 99, None)


def test_api_v3_python_rejects_cycles_unknowns_and_bad_coordinates() -> None:
    from pico_logic_analyzer._decode.compat import OUTPUT_PYTHON
    from pico_logic_analyzer._decode.model import ResultFailure

    host = _compat()
    output = host.register(OUTPUT_PYTHON)
    cycle: list[object] = []
    cycle.append(cycle)
    for value in (cycle, {"not": "closed"}, {1}, float("inf")):
        with pytest.raises(ResultFailure):
            host.put(0, 1, output, value)
    with pytest.raises(ResultFailure):
        host.put(-1, 1, output, None)


def test_api_v3_normalizes_exact_spi_data_and_tracks_single_metadata_call() -> None:
    from pico_logic_analyzer._decode.compat import OUTPUT_META, OUTPUT_PYTHON, SRD_CONF_SAMPLERATE
    from pico_logic_analyzer._decode.model import ResultFailure

    data = namedtuple("Data", ["ss", "es", "val"])
    data.__module__ = "spi.pd"
    host = _compat(data)
    python_id = host.register(OUTPUT_PYTHON)
    metadata_id = host.register(OUTPUT_META, meta=(int, "Bitrate", "description"))
    host.put(0, 1, python_id, [data(0, 1, 3)])
    assert host.records[0].to_dict()["value"] == {
        "tag": "list",
        "value": [{"tag": "spi-data", "ss": 0, "es": 1, "val": 3}],
    }
    host.metadata(SRD_CONF_SAMPLERATE, 10)
    assert host.metadata_calls == ((SRD_CONF_SAMPLERATE, 10),)
    with pytest.raises(ResultFailure):
        host.metadata(SRD_CONF_SAMPLERATE, 10)
    with pytest.raises(ResultFailure):
        host.register(OUTPUT_META, meta=(bool, "bad", "bad"))
    with pytest.raises(ResultFailure):
        host.put(0, 1, metadata_id, True)


def test_frozen_shim_uppercase_adapter_preserves_noncatchable_end() -> None:
    from pico_logic_analyzer._decode.compat import EndOfInput, ShimAdapter

    adapter = ShimAdapter(_compat())
    assert adapter.HasChannel(0) is True
    assert adapter.Wait({}) == (0, 255, 0, 255)
    with pytest.raises(EndOfInput):
        adapter.Wait({"skip": 5})


def test_private_ipc_frames_are_incremental_closed_and_bounded() -> None:
    from pico_logic_analyzer._decode.ipc import REQUEST, encode_frame, read_frame
    from pico_logic_analyzer._decode.model import WorkerFailure

    fields = {
        "decoder": "uart",
        "file_set_sha256": "a" * 64,
        "samplerate_hz": 1,
        "channel_ids": [0],
        "mapping": {"rx": 0},
        "samples": [0],
        "trigger_index": 0,
        "options": {},
    }
    frame = encode_frame(REQUEST, fields, 512)
    parts = iter([frame[:1], frame[1:4], frame[4:7], frame[7:]])

    def read(_count: int) -> bytes:
        return next(parts, b"")

    assert read_frame(read, 512)["decoder"] == "uart"
    with pytest.raises(WorkerFailure):
        read_frame(lambda _count: b"", 512)
    oversized = b"\x00\x00\x01\x00"
    with pytest.raises(WorkerFailure):
        read_frame(lambda count: oversized[:count], 16)
    with pytest.raises(WorkerFailure):
        encode_frame(REQUEST, fields, 8)


@pytest.mark.parametrize(
    "raw",
    [
        b'{"version":1,"type":"decode-request","version":1}',
        b'{"version":NaN,"type":"decode-request"}',
        b'{"version":1,"type":"unknown"}',
        b'{"version":1,"type":"decode-request","extra":1}',
    ],
)
def test_private_ipc_rejects_noncanonical_json_and_trailing_frames(raw: bytes) -> None:
    from pico_logic_analyzer._decode.ipc import read_frame
    from pico_logic_analyzer._decode.model import WorkerFailure

    frame = len(raw).to_bytes(4, "big") + raw
    with pytest.raises(WorkerFailure):
        read_frame(_byte_reader(frame), 512)
    valid = b'{"version":1,"type":"decode-failure","code":"ipc","message":"x"}'
    second = len(valid).to_bytes(4, "big") + valid
    with pytest.raises(WorkerFailure):
        read_frame(_byte_reader(second + second), 512)


def _byte_reader(value: bytes):
    offset = 0

    def read(count: int) -> bytes:
        nonlocal offset
        chunk = value[offset : offset + count]
        offset += len(chunk)
        return chunk

    return read


def test_identity_root_is_the_repository_root() -> None:
    from pico_logic_analyzer._decode.identity import ROOT

    assert (ROOT / "Software/decoders/sigrokdecode.py").is_file()


def test_fixed_worker_uses_fd_transport_and_reaps_two_inert_launches() -> None:
    from pico_logic_analyzer._decode.host import _read_fd_frame, _spawn_fixed_worker
    from pico_logic_analyzer._decode.ipc import REQUEST, encode_frame

    fields = {
        "decoder": "uart",
        "file_set_sha256": "a" * 64,
        "samplerate_hz": 1,
        "channel_ids": [0],
        "mapping": {"rx": 0},
        "samples": [0],
        "trigger_index": 0,
        "options": {},
    }
    payload = encode_frame(REQUEST, fields, 512)
    for _ in range(2):
        process, response_fd = _spawn_fixed_worker(subprocess.Popen, payload)
        response = _read_fd_frame(response_fd)
        os.close(response_fd)
        process.wait(timeout=2)
        assert process.returncode == 0
        assert response["type"] == "decode-result"
        assert process.stdout is not None and process.stdout.read() == b""
        assert process.stderr is not None and process.stderr.read() == b""


@pytest.mark.parametrize("decoder", ["uart", "spi", "i2c"])
def test_pinned_loader_returns_only_frozen_descriptors(decoder: str) -> None:
    from pico_logic_analyzer._decode.loader import load_frozen_decoder

    first = load_frozen_decoder(decoder)
    second = load_frozen_decoder(decoder)
    assert first.identity.decoder == decoder
    assert first.decoder_class is not second.decoder_class
    assert (first.spi_data_type is not None) is (decoder == "spi")


def test_lifecycle_projects_fake_descriptor_and_clean_end() -> None:
    from pico_logic_analyzer._decode.compat import OUTPUT_ANN, OUTPUT_PYTHON
    from pico_logic_analyzer._decode.identity import DecoderIdentity
    from pico_logic_analyzer._decode.lifecycle import run_lifecycle
    from pico_logic_analyzer._decode.loader import FrozenDescriptor
    from pico_logic_analyzer._decode.model import DecodeRequest

    calls: list[str] = []

    class Fake:
        channels = (("rx", "RX"),)
        optional_channels = ()
        annotations = (("byte", "Byte"),)
        annotation_rows = (("row", "Row", (0,)),)
        binary = ()

        def __init__(self) -> None:
            calls.append("constructor")

        def start(self) -> None:
            calls.append("start")
            self.python = self.cObj.Register(OUTPUT_PYTHON)
            self.annotation = self.cObj.Register(OUTPUT_ANN)

        def metadata(self, key: int, value: int) -> None:
            assert (key, value) == (0, 10)
            calls.append("metadata")

        def decode(self) -> None:
            calls.append("decode")
            self.cObj.Wait({})
            self.cObj.Put(0, 1, self.python, ("byte", 1))
            self.cObj.Put(0, 1, self.annotation, [0, ["01"]])
            self.cObj.Wait({"skip": 2})

    identity = DecoderIdentity("uart", (), "a" * 64)
    descriptor = FrozenDescriptor(identity, Fake, Fake, None)
    request = DecodeRequest("uart", 10, (4,), {"rx": 4}, (0, 1), 0, {})
    result = run_lifecycle(descriptor, request)
    assert calls == ["constructor", "start", "metadata", "decode"]
    assert result.capture.sample_count == 2
    assert [record.kind for record in result.records] == ["python", "annotation"]
    assert result.records[0].start_time.absolute.denominator == 10
    assert result.records[1].value.to_dict() == {"class_index": 0, "texts": ["01"]}
    assert [item.identifier for item in result.declarations if hasattr(item, "identifier")] == [
        "byte",
        "row",
    ]


def test_lifecycle_rejects_decoder_exception_without_partial_result() -> None:
    from pico_logic_analyzer._decode.identity import DecoderIdentity
    from pico_logic_analyzer._decode.lifecycle import run_lifecycle
    from pico_logic_analyzer._decode.loader import FrozenDescriptor
    from pico_logic_analyzer._decode.model import DecodeRequest, ResultFailure

    class Broken:
        channels = (("rx", "RX"),)
        optional_channels = ()
        annotations = ()
        annotation_rows = ()
        binary = ()

        def start(self) -> None:
            pass

        def metadata(self, _key: int, _value: int) -> None:
            pass

        def decode(self) -> None:
            raise RuntimeError("bad decoder")

    descriptor = FrozenDescriptor(DecoderIdentity("uart", (), "a" * 64), Broken, Broken, None)
    request = DecodeRequest("uart", 1, (4,), {"rx": 4}, (0,), 0, {})
    with pytest.raises(ResultFailure, match="lifecycle decoder rejected"):
        run_lifecycle(descriptor, request)


def test_uart_boundary_incomplete_runs_twice_through_fresh_private_workers() -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import DecodeRequest, canonical_json

    fixture_path = ROOT / "testdata/decoders/cycle3/semantic-fixtures.json"
    timeline = next(
        item
        for item in json.loads(fixture_path.read_text())["timelines"]
        if item["id"] == "uart-msb-9bit-boundary-incomplete"
    )
    transitions = timeline["transitions"]["D4"]
    samples = tuple(
        next(value for start, value in reversed(transitions) if start <= sample)
        for sample in range(timeline["sample_count"])
    )
    request = DecodeRequest(
        "uart", timeline["samplerate_hz"], (4,), {"rx": 4}, samples,
        timeline["trigger_index"], timeline["options"],
    )
    first = decode_private(request)
    second = decode_private(request)
    assert first.to_dict()["records"] == timeline["expected_records"]
    assert canonical_json(first.to_dict()) == canonical_json(second.to_dict())


@pytest.mark.parametrize("timeline", SEMANTIC["timelines"], ids=lambda item: item["id"])
def test_every_corrected_semantic_timeline_matches_the_closed_private_host(
    timeline: dict[str, object],
) -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import DecodeRequest

    mapping = timeline["mapping"]
    transitions = timeline["transitions"]
    assert isinstance(mapping, dict) and isinstance(transitions, dict)
    channel_ids = tuple(mapping.values())
    state: dict[str, int] = {}
    events: dict[int, list[tuple[str, int]]] = {}
    for channel, rows in transitions.items():
        assert isinstance(channel, str) and isinstance(rows, list)
        for index, value in rows:
            events.setdefault(index, []).append((channel, value))
    for physical in channel_ids:
        initial = [value for channel, value in events[0] if channel == f"D{physical}"]
        assert len(initial) == 1
        state[f"D{physical}"] = initial[0]
    samples = []
    for index in range(timeline["sample_count"]):
        for channel, value in events.get(index, []):
            state[channel] = value
        samples.append(
            sum(
                (state[f"D{physical}"] & 1) << position
                for position, physical in enumerate(channel_ids)
            )
        )
    result = decode_private(
        DecodeRequest(
            timeline["decoder"],
            timeline["samplerate_hz"],
            channel_ids,
            mapping,
            tuple(samples),
            timeline["trigger_index"],
            timeline["options"],
        )
    )
    assert result.to_dict()["records"] == timeline["expected_records"]


def test_parent_rejects_preflight_before_its_process_factory_runs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host_module
    from pico_logic_analyzer._decode.model import DecodeRequest, HostFailure

    calls = 0

    def factory(*_args: object, **_kwargs: object):
        nonlocal calls
        calls += 1
        raise AssertionError("process factory must remain untouched")

    def reject(_decoder: str) -> object:
        raise HostFailure("identity rejected")

    monkeypatch.setattr(host_module, "verify_decoder", reject)
    request = DecodeRequest("uart", 1, (0,), {"rx": 0}, (0,), 0, {})
    with pytest.raises(HostFailure):
        host_module._decode_with_factory(request, factory)
    assert calls == 0
