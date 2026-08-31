from __future__ import annotations

import copy
import json
import os
import resource
import subprocess
import sys
import threading
import time
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


def _request(
    decoder: str,
    options: dict[str, object] | None = None,
    samples: tuple[int, ...] = (0,),
    trigger_index: int = 0,
):
    from pico_logic_analyzer._decode.model import DecodeRequest

    mappings = {
        "uart": {"rx": 7},
        "spi": {"clk": 7, "miso": 2},
        "i2c": {"scl": 7, "sda": 2},
    }
    return DecodeRequest(
        decoder, 1, (7, 2, 19), mappings[decoder], samples, trigger_index, options or {}
    )


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


@pytest.mark.parametrize(
    ("limit", "accepted"),
    [(50_000_000, True), (50_000_001, False), (1_300_000_000, True), (1_300_000_001, False)],
)
def test_parent_launch_and_total_timing_exact_boundaries(limit: int, accepted: bool) -> None:
    from pico_logic_analyzer._decode.host import _validate_elapsed
    from pico_logic_analyzer._decode.model import HostFailure

    cap = 50_000_000 if limit < 1_000_000_000 else 1_300_000_000
    if accepted:
        _validate_elapsed(limit, cap)
    else:
        with pytest.raises(HostFailure, match="^process-exit$"):
            _validate_elapsed(limit, cap)


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
    from pico_logic_analyzer._decode.host import _collect_response, _spawn_fixed_worker
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
        process, request_fd, response_fd = _spawn_fixed_worker(subprocess.Popen)
        response, stdout, stderr = _collect_response(
            process, request_fd, payload, response_fd, None
        )
        os.close(response_fd)
        with pytest.raises(OSError):
            os.fstat(response_fd)
        process.wait(timeout=2)
        assert process.returncode == 0
        assert response["type"] == "decode-result"
        assert stdout == b""
        assert stderr == b""


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


def test_parent_owned_cancellation_is_checked_before_identity_or_spawn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host_module
    from pico_logic_analyzer._decode.model import DecodeRequest, HostFailure

    token = host_module.CancellationToken()
    token.cancel()
    calls = 0

    def factory(*_args: object, **_kwargs: object):
        nonlocal calls
        calls += 1
        raise AssertionError("cancelled request must not launch")

    request = DecodeRequest("uart", 1, (0,), {"rx": 0}, (0,), 0, {})
    with pytest.raises(HostFailure, match="cancelled"):
        host_module._decode_with_factory(request, factory, token)
    assert calls == 0


def test_stdout_ceiling_is_not_the_encoded_result_ceiling() -> None:
    from pico_logic_analyzer._decode.model import HARD_LIMITS

    assert HARD_LIMITS["stdout_bytes"] == 65_536
    assert HARD_LIMITS["stdout_bytes"] < HARD_LIMITS["encoded_bytes"]


def test_parent_rejects_missing_forged_or_over_cap_worker_metrics() -> None:
    from pico_logic_analyzer._decode.host import _validate_worker_metrics
    from pico_logic_analyzer._decode.model import HostFailure

    valid = {
        "child_import_ns": 100_000_000,
        "child_load_ns": 100_000_000,
        "child_decode_ns": 100_000_000,
        "worker_peak_rss_bytes": 134_217_728,
    }
    _validate_worker_metrics(valid)
    for invalid in ({}, {**valid, "extra": 1}, {**valid, "worker_peak_rss_bytes": 134_217_729}):
        with pytest.raises(HostFailure):
            _validate_worker_metrics(invalid)


@pytest.mark.parametrize(
    "name",
    ["child_import_ns", "child_load_ns", "child_decode_ns", "worker_peak_rss_bytes"],
)
def test_each_worker_metric_has_exact_cap_and_first_overrun(name: str) -> None:
    from pico_logic_analyzer._decode.host import _validate_worker_metrics
    from pico_logic_analyzer._decode.model import REGRESSION_LIMITS, HostFailure

    values = {key: REGRESSION_LIMITS[key] for key in REGRESSION_LIMITS if key.startswith("child_")}
    values["worker_peak_rss_bytes"] = REGRESSION_LIMITS["worker_peak_rss_bytes"]
    _validate_worker_metrics(values)
    values[name] += 1
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_worker_metrics(values)


@pytest.mark.parametrize(
    ("name", "invalid"),
    [
        (name, invalid)
        for name in ("child_import_ns", "child_load_ns", "child_decode_ns", "worker_peak_rss_bytes")
        for invalid in (-1, True, False, 1.0, "1")
    ],
)
def test_each_worker_metric_rejects_negative_bool_and_non_integer(
    name: str, invalid: object
) -> None:
    from pico_logic_analyzer._decode.host import _validate_worker_metrics
    from pico_logic_analyzer._decode.model import HostFailure

    values: dict[str, object] = {
        "child_import_ns": 0,
        "child_load_ns": 0,
        "child_decode_ns": 0,
        "worker_peak_rss_bytes": 0,
    }
    values[name] = invalid
    with pytest.raises(HostFailure, match="^ipc$"):
        _validate_worker_metrics(values)


@pytest.mark.parametrize(
    ("before", "after", "accepted"),
    [
        (10, 10 + 33_554_432, True),
        (10, 10 + 33_554_433, False),
        (11, 10, False),
    ],
)
def test_parent_rss_growth_uses_approved_b1_before_after_semantics(
    before: int, after: int, accepted: bool
) -> None:
    from pico_logic_analyzer._decode.host import _validate_parent_growth
    from pico_logic_analyzer._decode.model import HostFailure

    if accepted:
        _validate_parent_growth(before, after)
    else:
        with pytest.raises(HostFailure):
            _validate_parent_growth(before, after)


@pytest.mark.parametrize(
    ("total", "term", "kill", "accepted"),
    [
        (5_500_000_000, 300_000_000, 50_000_000, True),
        (5_500_000_001, None, None, False),
        (1, 300_000_001, None, False),
        (1, None, 50_000_001, False),
    ],
)
def test_cleanup_timing_ceilings_have_independent_boundary_checks(
    total: int, term: int | None, kill: int | None, accepted: bool
) -> None:
    from pico_logic_analyzer._decode.host import _validate_cleanup_times
    from pico_logic_analyzer._decode.model import HostFailure

    if accepted:
        _validate_cleanup_times(total, term, kill)
    else:
        with pytest.raises(HostFailure):
            _validate_cleanup_times(total, term, kill)


class _FakePipe:
    def __init__(self) -> None:
        self.closed = False

    def close(self) -> None:
        self.closed = True


class _GracefulProcess:
    def __init__(self, force_kill: bool) -> None:
        self.force_kill = force_kill
        self.events: list[str] = []
        self.finished = False
        self.stdout = _FakePipe()
        self.stderr = _FakePipe()

    def poll(self) -> None:
        return None if not self.finished else 0

    def terminate(self) -> None:
        self.events.append("terminate")

    def wait(self, _timeout: float | None = None) -> None:
        self.events.append("wait")
        if self.force_kill and len(self.events) == 2:
            raise subprocess.TimeoutExpired("worker", 0.25)
        self.finished = True

    def kill(self) -> None:
        self.events.append("kill")


@pytest.mark.parametrize(
    ("force_kill", "expected"),
    [(False, ["terminate", "wait"]), (True, ["terminate", "wait", "kill", "wait"])],
)
def test_cleanup_orders_graceful_terminate_or_forced_kill_then_reap(
    force_kill: bool, expected: list[str]
) -> None:
    from pico_logic_analyzer._decode.host import _terminate_reap

    process = _GracefulProcess(force_kill)
    _terminate_reap(process)  # type: ignore[arg-type]
    assert process.events == expected


@pytest.mark.parametrize("code", ["memory", "recursion", "decoder", "ipc", "output-limit"])
def test_worker_failure_codes_are_closed_and_never_return_partial_result(code: str) -> None:
    from pico_logic_analyzer._decode.model import FAILURE_CODES, DecodeFailure

    assert code in FAILURE_CODES
    assert DecodeFailure(code, "safe").to_dict()["code"] == code


@pytest.mark.parametrize(
    ("stage", "error", "expected"),
    [
        ("request", MemoryError(), "memory"),
        ("request", RecursionError(), "recursion"),
        ("request", ValueError(), "ipc"),
        ("load", ValueError(), "import"),
        ("lifecycle", ValueError(), "decoder"),
    ],
)
def test_fixed_worker_maps_resource_and_stage_failures_without_error_detail(
    stage: str, error: BaseException, expected: str
) -> None:
    from pico_logic_analyzer._decode.worker import _failure_code

    assert _failure_code(stage, error) == expected


@pytest.mark.parametrize(
    ("stream", "size", "accepted"),
    [
        ("stdout", 65_536, True),
        ("stderr", 65_536, True),
        ("stdout", 65_537, False),
        ("stderr", 65_537, False),
    ],
)
def test_stream_flood_boundaries_are_independent_of_result_frame_limit(
    stream: str, size: int, accepted: bool
) -> None:
    from pico_logic_analyzer._decode.host import _pipe_limit

    assert (size <= _pipe_limit(stream)) is accepted


def test_cancellation_after_a_settled_result_does_not_mutate_that_result() -> None:
    from pico_logic_analyzer._decode.host import CancellationToken, decode_private

    token = CancellationToken()
    settled = decode_private(_request("uart"))
    expected = settled.to_dict()
    token.cancel()
    assert settled.to_dict() == expected
    assert token.cancelled


@pytest.mark.parametrize(
    "failure", ["ipc", "output-limit", "memory", "recursion", "timeout", "cancelled"]
)
def test_each_failure_category_has_a_following_fresh_fixed_worker_success(failure: str) -> None:
    """The semantic host test launches a second fresh worker for the recovery assertion."""
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import DecodeRequest

    assert failure
    request = DecodeRequest("uart", 1, (7,), {"rx": 7}, (0,), 0, {})
    assert decode_private(request).decoder == "uart"


def _hostile_factory(
    response: bytes = b"", *, stdout: bytes = b"", stderr: bytes = b"", exit_code: int = 0,
    signal: bool = False, hold_open: bool = False, response_fill: int = 0,
    ignore_term: bool = False, never_read_request: bool = False, request_hold_s: float = 0,
):
    """A test-only fixed child: it accepts only the parent-created FD pair."""

    exit_line = (
        "os.kill(os.getpid(), signal.SIGTERM)\n"
        if signal
        else f"raise SystemExit({exit_code})\n"
    )
    children: list[subprocess.Popen[bytes]] = []
    script = (
        "import os, signal, sys, time\n"
        + "request_fd, response_fd = map(int, sys.argv[1:3])\n"
        + ("signal.signal(signal.SIGTERM, signal.SIG_IGN)\n" if ignore_term else "")
        + (
            f"time.sleep({request_hold_s})\nos.close(request_fd)\n"
            if never_read_request
            else "os.close(request_fd)\n"
        )
        + f"os.write(1, b'x' * {len(stdout)})\n"
        + f"os.write(2, b'x' * {len(stderr)})\n"
        + f"os.write(response_fd, b'x' * {response_fill} or "
        + f"bytes.fromhex({response.hex()!r}))\n"
        + ("time.sleep(10)\n" if hold_open else "os.close(response_fd)\n")
        + exit_line
    )

    def factory(command: list[str], **kwargs: object) -> subprocess.Popen[bytes]:
        child = subprocess.Popen(
            [sys.executable, "-c", script, command[-2], command[-1]], **kwargs
        )
        children.append(child)
        return child

    setattr(factory, "children", children)
    return factory


def _failure_frame(code: str) -> bytes:
    from pico_logic_analyzer._decode.ipc import FAILURE, encode_frame
    from pico_logic_analyzer._decode.model import HARD_LIMITS

    return encode_frame(
        FAILURE,
        {"code": code, "message": "worker rejected request"},
        HARD_LIMITS["encoded_bytes"],
    )


def _fresh_valid_decode() -> None:
    from pico_logic_analyzer._decode.host import decode_private

    assert decode_private(_request("uart")).decoder == "uart"


def _large_delivery_request():
    """A framed request materially larger than the platform pipe buffer."""
    return _request("uart", samples=(0,) * 40_000)


def test_request_delivery_never_reader_times_out_reaps_and_recovers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HARD_LIMITS, HostFailure

    monkeypatch.setattr(host, "HARD_LIMITS", {**HARD_LIMITS, "wall_deadline_ms": 25})
    factory = _hostile_factory(never_read_request=True, request_hold_s=10)
    with pytest.raises(HostFailure, match="^timeout$"):
        host._decode_with_factory(_large_delivery_request(), factory)
    _assert_reaped_closed(factory)
    monkeypatch.undo()
    _fresh_valid_decode()


def test_cancellation_during_partial_request_delivery_reaps_and_recovers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HostFailure

    token = host.CancellationToken()
    real_write = os.write
    writes: list[int] = []

    def cancel_after_partial_write(fd: int, data: object) -> int:
        written = real_write(fd, data)  # type: ignore[arg-type]
        writes.append(written)
        if len(writes) == 1 and written < len(data):  # type: ignore[arg-type]
            token.cancel()
        return written

    monkeypatch.setattr(host.os, "write", cancel_after_partial_write)
    factory = _hostile_factory(never_read_request=True, request_hold_s=10)
    with pytest.raises(HostFailure, match="^cancelled$"):
        host._decode_with_factory(_large_delivery_request(), factory, token)
    assert writes and token.cancelled
    _assert_reaped_closed(factory)
    _fresh_valid_decode()


def test_early_worker_exit_during_request_delivery_reaps_and_recovers() -> None:
    from pico_logic_analyzer._decode.host import _decode_with_factory
    from pico_logic_analyzer._decode.model import HostFailure

    factory = _hostile_factory(never_read_request=True, request_hold_s=0.01, exit_code=0)
    with pytest.raises(HostFailure, match="^process-exit$"):
        _decode_with_factory(_large_delivery_request(), factory)
    _assert_reaped_closed(factory)
    _fresh_valid_decode()


def _settled_result_frame(request: object, mutate: object) -> bytes:
    """Build a locally valid hostile result from an independently settled worker result."""
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
    from pico_logic_analyzer._decode.model import HARD_LIMITS

    result = copy.deepcopy(decode_private(request).to_dict())  # type: ignore[arg-type]
    mutate(result)  # type: ignore[operator]
    return encode_frame(
        RESULT,
        {
            "result": result,
            "metrics": {
                "child_import_ns": 0,
                "child_load_ns": 0,
                "child_decode_ns": 0,
                "worker_peak_rss_bytes": 0,
            },
        },
        HARD_LIMITS["encoded_bytes"],
    )


def _assert_reaped_closed(factory: object) -> None:
    children = getattr(factory, "children")
    assert len(children) == 1
    child = children[0]
    assert child.poll() is not None
    assert child.stdout is not None and child.stdout.closed
    assert child.stderr is not None and child.stderr.closed


@pytest.mark.parametrize(
    ("decoder", "samples", "mutate"),
    [
        ("uart", (0,), lambda result: result["decoder"].__setitem__("id", "i2c")),
        ("uart", (0,), lambda result: result["decoder"].__setitem__("file_set_sha256", "0" * 64)),
        ("uart", (0,), lambda result: result.__setitem__("samplerate_hz", 2)),
        ("uart", (0, 0), lambda result: result["capture"].__setitem__("sample_count", 1)),
        ("uart", (0, 0), lambda result: result["capture"].__setitem__("trigger_index", 1)),
        ("uart", (0,), lambda result: result["channels"][0].__setitem__("physical_channel", 2)),
        (
            "spi",
            (0,),
            lambda result: result.__setitem__("channels", list(reversed(result["channels"]))),
        ),
        (
            "spi",
            (0,),
            lambda result: result["channels"].append(copy.deepcopy(result["channels"][0])),
        ),
        ("uart", (0,), lambda result: result.__setitem__("options", {"baudrate": 115200})),
        ("uart", (0,), lambda result: result["options"].__setitem__("baudrate", 9600)),
        ("uart", (0,), lambda result: result["options"].__setitem__("stop_bits", 1)),
    ],
    ids=(
        "decoder-id",
        "file-set-hash",
        "samplerate",
        "capture-sample-count",
        "capture-trigger-index",
        "channel-physical-mapping",
        "channel-declaration-order",
        "duplicate-channel-declaration",
        "options-defaults-omitted",
        "option-value",
        "option-value-type",
    ),
)
def test_parent_binds_every_materialized_result_identity_to_preflight(
    decoder: str, samples: tuple[int, ...], mutate: object
) -> None:
    """A syntactically valid child result cannot alter any preflight-derived fact."""
    from pico_logic_analyzer._decode.host import _decode_with_factory
    from pico_logic_analyzer._decode.model import HostFailure

    request = _request(decoder, samples=samples)
    factory = _hostile_factory(response=_settled_result_frame(request, mutate))
    with pytest.raises(HostFailure, match="^ipc$"):
        _decode_with_factory(request, factory)  # type: ignore[arg-type]
    _assert_reaped_closed(factory)
    _fresh_valid_decode()


def test_parent_accepts_exact_preflight_projection_after_materialization() -> None:
    from pico_logic_analyzer._decode.host import _decode_with_factory

    request = _request("spi")
    factory = _hostile_factory(response=_settled_result_frame(request, lambda _result: None))
    result = _decode_with_factory(request, factory)  # type: ignore[arg-type]
    assert result.decoder == request.decoder
    assert tuple(result.channels.items()) == tuple(request.mapping.items())
    assert dict(result.options) == dict(request.options)
    _assert_reaped_closed(factory)


@pytest.mark.parametrize(
    ("name", "factory", "expected"),
    [
        ("nonzero", _hostile_factory(exit_code=7), "process-exit"),
        ("signal", _hostile_factory(signal=True), "process-exit"),
        ("truncated", _hostile_factory(response=b"\x00\x00\x00\x10{}"), "ipc"),
        ("extra", _hostile_factory(response=_failure_frame("ipc") + _failure_frame("ipc")), "ipc"),
        ("oversized", _hostile_factory(response_fill=2_097_153 + 4), "output-limit"),
        ("stdout-first-overrun", _hostile_factory(stdout=b"x" * 65_537), "output-limit"),
        ("stderr-first-overrun", _hostile_factory(stderr=b"x" * 65_537), "output-limit"),
        ("worker-memory", _hostile_factory(response=_failure_frame("memory")), "memory"),
        ("worker-recursion", _hostile_factory(response=_failure_frame("recursion")), "recursion"),
        ("worker-decoder", _hostile_factory(response=_failure_frame("decoder")), "decoder"),
        ("worker-ipc", _hostile_factory(response=_failure_frame("ipc")), "ipc"),
    ],
    ids=lambda value: value if isinstance(value, str) else None,
)
def test_parent_boundary_hostile_child_failures_reap_and_recover(
    name: str, factory: object, expected: str
) -> None:
    """Each event crosses the parent seam, leaves no partial result, then recovers."""
    from pico_logic_analyzer._decode.host import _decode_with_factory
    from pico_logic_analyzer._decode.model import HostFailure

    assert name
    with pytest.raises(HostFailure, match=f"^{expected}$"):
        _decode_with_factory(_request("uart"), factory)  # type: ignore[arg-type]
    _assert_reaped_closed(factory)
    _fresh_valid_decode()


@pytest.mark.parametrize(
    ("stream", "size"), [("stdout", 65_536), ("stderr", 65_536)]
)
def test_parent_boundary_stream_exact_boundary_is_not_rejected(stream: str, size: int) -> None:
    """A valid failure frame permits checking stream caps without a decoder result."""
    from pico_logic_analyzer._decode.host import _decode_with_factory
    from pico_logic_analyzer._decode.model import HostFailure

    kwargs = {stream: b"x" * size, "response": _failure_frame("decoder")}
    with pytest.raises(HostFailure, match="^decoder$"):
        _decode_with_factory(_request("uart"), _hostile_factory(**kwargs))
    _fresh_valid_decode()


def test_parent_boundary_timeout_cancels_open_pipes_and_recovers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HARD_LIMITS, HostFailure

    monkeypatch.setattr(
        host, "HARD_LIMITS", {**HARD_LIMITS, "wall_deadline_ms": 10}
    )
    factory = _hostile_factory(hold_open=True)
    with pytest.raises(HostFailure, match="^timeout$"):
        host._decode_with_factory(_request("uart"), factory)
    _assert_reaped_closed(factory)
    monkeypatch.undo()
    _fresh_valid_decode()


@pytest.mark.parametrize("cancelled", [False, True], ids=("timeout", "cancelled"))
def test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure(
    monkeypatch: pytest.MonkeyPatch, cancelled: bool
) -> None:
    """Forced kill is hard cleanup; its timing is regression evidence only."""
    from dataclasses import replace

    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HARD_LIMITS, REGRESSION_LIMITS, HostFailure

    class CancelsDuringDrain(host.CancellationToken):
        def __init__(self) -> None:
            super().__init__()
            self.checks = 0

        @property
        def cancelled(self) -> bool:
            self.checks += 1
            return self.checks > 1

    monkeypatch.setattr(
        host,
        "HARD_LIMITS",
        {**HARD_LIMITS, "wall_deadline_ms": 50, "terminate_grace_ms": 10},
    )
    observed: list[host._RegressionObservation] = []
    factory = _hostile_factory(hold_open=True, ignore_term=True)
    token = CancelsDuringDrain() if cancelled else None
    with pytest.raises(HostFailure, match="^cancelled$" if cancelled else "^timeout$"):
        host._decode_with_factory(
            _request("uart"), factory, token, regression_observer=observed.append
        )
    _assert_reaped_closed(factory)
    assert len(observed) == 1
    actual = observed[0]
    assert actual.terminate_to_reap_ns > 0
    if not cancelled:
        assert actual.timeout_cleanup_total_ns > 0 and actual.kill_to_reap_ns > 0
    over_ceiling = replace(
        actual,
        timeout_cleanup_total_ns=REGRESSION_LIMITS["timeout_cleanup_total_ns"] + 1,
        terminate_to_reap_ns=REGRESSION_LIMITS["terminate_to_reap_ns"] + 1,
        kill_to_reap_ns=REGRESSION_LIMITS["kill_to_reap_ns"] + 1,
    )
    with pytest.raises(HostFailure, match="^process-exit$"):
        host._validate_regression_observation(over_ceiling)


def test_parent_boundary_cancellation_while_pipes_are_open_reaps_and_recovers() -> None:
    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HostFailure

    class CancelsDuringDrain(host.CancellationToken):
        def __init__(self) -> None:
            super().__init__()
            self.checks = 0

        @property
        def cancelled(self) -> bool:
            self.checks += 1
            return self.checks > 1

    factory = _hostile_factory(hold_open=True)
    with pytest.raises(HostFailure, match="^cancelled$"):
        host._decode_with_factory(
            _request("uart"), factory, CancelsDuringDrain()
        )
    _assert_reaped_closed(factory)
    _fresh_valid_decode()


def test_selector_observes_real_cross_thread_cancellation_while_quiet_pipes_remain_open() -> None:
    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HostFailure

    token = host.CancellationToken()
    factory = _hostile_factory(hold_open=True)
    timer = threading.Timer(0.02, token.cancel)
    timer.start()
    started = time.monotonic()
    try:
        with pytest.raises(HostFailure, match="^cancelled$"):
            host._decode_with_factory(_request("uart"), factory, token)
    finally:
        timer.cancel()
    assert time.monotonic() - started < 0.5
    _assert_reaped_closed(factory)


def test_decoded_and_retained_accounting_are_independent_cycle_safe_boundaries() -> None:
    from pico_logic_analyzer._decode.host import _decoded_bytes, _deep_size, _enforce_result_limits
    from pico_logic_analyzer._decode.model import HostFailure

    value: dict[str, object] = {"text": "x"}
    value["self"] = value
    decoded = _decoded_bytes({"text": "x"})
    retained = _deep_size(value)
    assert decoded > 0
    assert retained >= sys.getsizeof(value)
    assert _deep_size(value) == retained
    for decoded, retained_size in ((2_097_152, 8_388_608), (0, 0)):
        _enforce_result_limits(
            value,
            lambda _value, count=decoded: count,
            lambda _value, count=retained_size: count,
        )
    with pytest.raises(HostFailure, match="^output-limit$"):
        _enforce_result_limits(value, lambda _value: 2_097_153, lambda _value: 0)
    with pytest.raises(HostFailure, match="^output-limit$"):
        _enforce_result_limits(value, lambda _value: 0, lambda _value: 8_388_609)


def test_worker_bootstrap_limits_are_closed_and_exact(monkeypatch: pytest.MonkeyPatch) -> None:
    import pico_logic_analyzer._decode.worker as worker

    calls: list[tuple[int, tuple[int, int]]] = []
    real_getrecursionlimit = sys.getrecursionlimit
    original_recursion = real_getrecursionlimit()
    monkeypatch.setattr(resource, "setrlimit", lambda key, value: calls.append((key, value)))
    monkeypatch.setattr(resource, "getrlimit", lambda _key: (68_719_476_736, 68_719_476_736))
    monkeypatch.setattr(sys, "setrecursionlimit", lambda _value: None)
    monkeypatch.setattr(sys, "getrecursionlimit", lambda: 320)
    worker._install_limits()
    assert calls == [(resource.RLIMIT_AS, (68_719_476_736, 68_719_476_736))]
    assert real_getrecursionlimit() == original_recursion


@pytest.mark.parametrize("as_limit, recursion", [(1, 320), (68_719_476_736, 319)])
def test_worker_bootstrap_readback_mismatch_fails(
    monkeypatch: pytest.MonkeyPatch, as_limit: int, recursion: int
) -> None:
    import pico_logic_analyzer._decode.worker as worker

    monkeypatch.setattr(resource, "setrlimit", lambda *_args: None)
    monkeypatch.setattr(resource, "getrlimit", lambda _key: (as_limit, as_limit))
    monkeypatch.setattr(sys, "setrecursionlimit", lambda _value: None)
    monkeypatch.setattr(sys, "getrecursionlimit", lambda: recursion)
    with pytest.raises(RuntimeError, match="bootstrap limits rejected"):
        worker._install_limits()


class _PostDrainProcess:
    def __init__(self, timeout: bool) -> None:
        self.timeout = timeout
        self.returncode = 0
        self.events: list[str] = []
        self.stdout = _FakePipe()
        self.stderr = _FakePipe()

    def poll(self) -> int:
        return 0

    def wait(self, timeout: float | None = None) -> None:
        self.events.append("wait")
        if self.timeout:
            raise subprocess.TimeoutExpired("worker", timeout)

    def terminate(self) -> None:
        self.events.append("terminate")

    def kill(self) -> None:
        self.events.append("kill")


@pytest.mark.parametrize("timeout", [True, False])
def test_post_drain_wait_errors_cleanup_exact_response_fd(
    monkeypatch: pytest.MonkeyPatch, timeout: bool
) -> None:
    """Exercise the normal post-drain wait branch, retaining its response FD."""
    import pico_logic_analyzer._decode.host as host
    from pico_logic_analyzer._decode.model import HostFailure

    process = _PostDrainProcess(timeout)
    request_fd = os.open(os.devnull, os.O_WRONLY)
    response_fd = os.open(os.devnull, os.O_RDONLY)
    monkeypatch.setattr(
        host, "_spawn_fixed_worker", lambda *_args: (process, request_fd, response_fd)
    )
    monkeypatch.setattr(
        host,
        "_collect_response",
        lambda *_args: ({"type": "decode-failure", "code": "decoder"}, b"", b""),
    )
    clock = iter((0, 0, 0, 0, *(2 for _ in range(32))))
    with pytest.raises(HostFailure, match="^process-exit$" if timeout else "^decoder$"):
        host._decode_with_factory(
            _request("uart"), subprocess.Popen, monotonic_ns=lambda: next(clock)
        )
    with pytest.raises(OSError):
        os.fstat(response_fd)
    with pytest.raises(OSError):
        os.fstat(request_fd)
    assert process.events == (["wait"] if not timeout else ["wait"])


def test_request_delivery_write_failure_reaps_and_closes_all_parent_fds(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host

    factory = _hostile_factory(hold_open=True)
    captured: list[int] = []
    real_pipe = os.pipe

    def record_pipe() -> tuple[int, int]:
        pair = real_pipe()
        captured.extend(pair)
        return pair

    monkeypatch.setattr(host.os, "pipe", record_pipe)
    monkeypatch.setattr(host.os, "write", lambda *_args: (_ for _ in ()).throw(OSError("write")))
    with pytest.raises(Exception, match="ipc"):
        host._decode_with_factory(_request("uart"), factory)
    assert len(captured) >= 4
    with pytest.raises(OSError):
        os.fstat(captured[1])
    with pytest.raises(OSError):
        os.fstat(captured[2])
    _assert_reaped_closed(factory)


def test_successful_parent_path_closes_its_exact_response_fd(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host

    original_spawn = host._spawn_fixed_worker
    captured: list[int] = []

    def record_spawn(*args: object):
        process, request_fd, response_fd = original_spawn(*args)  # type: ignore[arg-type]
        captured.append(request_fd)
        captured.append(response_fd)
        return process, request_fd, response_fd

    monkeypatch.setattr(host, "_spawn_fixed_worker", record_spawn)
    assert host._decode_with_factory(_request("uart"), subprocess.Popen).decoder == "uart"
    assert len(captured) == 2
    for fd in captured:
        with pytest.raises(OSError):
            os.fstat(fd)


def _valid_result_frame() -> bytes:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
    from pico_logic_analyzer._decode.model import HARD_LIMITS

    result = decode_private(_request("uart")).to_dict()
    metrics = {
        "child_import_ns": 0,
        "child_load_ns": 0,
        "child_decode_ns": 0,
        "worker_peak_rss_bytes": 0,
    }
    return encode_frame(
        RESULT, {"result": result, "metrics": metrics}, HARD_LIMITS["encoded_bytes"]
    )


@pytest.mark.parametrize("stream", ["stdout", "stderr"])
def test_parent_rejects_nonempty_stdio_on_structurally_valid_result_and_recovers(
    stream: str,
) -> None:
    from pico_logic_analyzer._decode.host import _decode_with_factory
    from pico_logic_analyzer._decode.model import HostFailure

    kwargs = {"response": _valid_result_frame(), stream: b"x"}
    factory = _hostile_factory(**kwargs)
    with pytest.raises(HostFailure, match="^process-exit$"):
        _decode_with_factory(_request("uart"), factory)
    _assert_reaped_closed(factory)
    _fresh_valid_decode()


def test_parent_accepts_structurally_valid_result_with_empty_stdio() -> None:
    from pico_logic_analyzer._decode.host import _decode_with_factory

    factory = _hostile_factory(response=_valid_result_frame())
    assert _decode_with_factory(_request("uart"), factory).decoder == "uart"
    _assert_reaped_closed(factory)


def test_regression_observation_is_not_a_product_failure_but_has_a_private_gate() -> None:
    from pico_logic_analyzer._decode.host import (
        _decode_with_factory,
        _RegressionObservation,
        _validate_regression_observation,
    )
    from pico_logic_analyzer._decode.model import REGRESSION_LIMITS, HostFailure

    observed: list[_RegressionObservation] = []
    result = _decode_with_factory(
        _request("uart"),
        _hostile_factory(response=_valid_result_frame()),
        regression_observer=observed.append,
    )
    assert result.decoder == "uart"
    assert len(observed) == 1
    over_ceiling = _RegressionObservation(
        **{
            name: REGRESSION_LIMITS[name] + 1
            for name in REGRESSION_LIMITS
        }
    )
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_regression_observation(over_ceiling)


@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-annotation-index", "gapped-annotation-index", "reordered-annotation-index",
        "duplicate-row-index", "missing-row-reference", "duplicate-row-reference",
        "undeclared-output",
        "cross-kind-output",
        "annotation-class-overrun",
        "binary-class-overrun",
        "metadata-output-mismatch", "negative-coordinate", "reversed-coordinate", "past-capture",
        "absolute-time", "relative-time",
    ],
)
def test_parent_rejects_each_closed_result_graph_edge_and_recovers(mutation: str) -> None:
    """Typed child data still needs one closed declaration/register/put graph."""
    from pico_logic_analyzer._decode.host import _decode_with_factory, decode_private
    from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
    from pico_logic_analyzer._decode.model import HARD_LIMITS, HostFailure

    request = _request("uart", samples=(0, 0))
    result = decode_private(request).to_dict()
    declarations = result["declarations"]
    assert isinstance(declarations, dict)
    annotations = declarations["annotations"]
    rows = declarations["annotation_rows"]
    binary = declarations["binary"]
    assert isinstance(annotations, list) and isinstance(rows, list) and isinstance(binary, list)
    record = {
        "emission_index": 0, "start_sample": 0, "end_sample": 0,
        "output_id": 2, "kind": "annotation", "value": {"class_index": 0, "texts": ["x"]},
        "start_time": {
            "absolute": {"numerator": 0, "denominator": 1},
            "trigger_relative": {"numerator": -1, "denominator": 1},
        },
        "end_time": {
            "absolute": {"numerator": 0, "denominator": 1},
            "trigger_relative": {"numerator": -1, "denominator": 1},
        },
    }
    if mutation == "duplicate-annotation-index":
        annotations[1]["index"] = 0
    elif mutation == "gapped-annotation-index":
        annotations[0]["index"] = 99
    elif mutation == "reordered-annotation-index":
        annotations[0]["index"], annotations[1]["index"] = 1, 0
    elif mutation == "duplicate-row-index":
        rows[1]["index"] = 0
    elif mutation == "missing-row-reference":
        rows[0]["annotation_indices"] = [999]
    elif mutation == "duplicate-row-reference":
        rows[0]["annotation_indices"] = [12, 12]
    elif mutation == "undeclared-output":
        record["output_id"] = 999
    elif mutation == "cross-kind-output":
        record["output_id"] = 0
    elif mutation == "annotation-class-overrun":
        record["value"] = {"class_index": len(annotations), "texts": ["x"]}
    elif mutation == "binary-class-overrun":
        record.update(
            {
                "output_id": 1,
                "kind": "binary",
                "value": {"class_index": len(binary), "data_base64": ""},
            }
        )
    elif mutation == "metadata-output-mismatch":
        record.update(
            {
                "output_id": 2,
                "kind": "metadata",
                "value": {"value_type": "integer", "value": 1},
            }
        )
    elif mutation == "negative-coordinate":
        record["start_sample"] = -1
    elif mutation == "reversed-coordinate":
        record.update({"start_sample": 1, "end_sample": 0})
    elif mutation == "past-capture":
        record.update({"start_sample": 2, "end_sample": 2})
    elif mutation == "absolute-time":
        record["start_time"]["absolute"]["numerator"] = 1  # type: ignore[index]
    else:
        record["end_time"]["trigger_relative"]["numerator"] = 0  # type: ignore[index]
    result["records"] = [record]
    frame = encode_frame(RESULT, {"result": result, "metrics": {
        "child_import_ns": 0, "child_load_ns": 0, "child_decode_ns": 0, "worker_peak_rss_bytes": 0,
    }}, HARD_LIMITS["encoded_bytes"])
    factory = _hostile_factory(response=frame)
    with pytest.raises(HostFailure, match="^ipc$"):
        _decode_with_factory(request, factory)
    _assert_reaped_closed(factory)
    _fresh_valid_decode()
