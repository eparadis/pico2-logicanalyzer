"""Independent C2-B4 bus and public-contract verification."""

from __future__ import annotations

import asyncio
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from multidict import CIMultiDict

from pico_logic_analyzer.analysis import bus_csv_bytes, sampled_rows, transition_rows
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo
from pico_logic_analyzer.web import server as web_server
from pico_logic_analyzer.web.server import create_app

ROOT = Path(__file__).parents[2]


def _device() -> DeviceInfo:
    return DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 1_000, 1_000, 4_096, 24)


def _capture(samples: list[int]) -> CaptureResult:
    # Packed bit 0=D9, bit 1=D0, bit 2=D5 strobe, bit 3=D2.
    config = CaptureConfig(100, 2, len(samples) - 2, 9, "rising", (9, 0, 5, 2))
    return CaptureResult(config, np.asarray(samples, dtype=np.uint16), _device())


def test_literal_reordered_bus_rows_edges_times_and_csv() -> None:
    result = _capture([0b0000, 0b0011, 0b1111, 0b1101, 0b1001, 0b1110])
    # Requested bus order D2,D9,D0 is independently interpreted LSB first.
    transitions = transition_rows(result, (2, 9, 0))
    assert [
        (
            row.sample_index,
            row.time_seconds,
            row.binary,
            row.hexadecimal,
            row.decimal,
            row.end_sample_index,
            row.end_time_seconds,
            row.duration_seconds,
        )
        for row in transitions
    ] == [
        (0, "-0.02", "000", "0x0", 0, 1, "-0.01", "0.01"),
        (1, "-0.01", "110", "0x6", 6, 2, "0", "0.01"),
        (2, "0", "111", "0x7", 7, 3, "0.01", "0.01"),
        (3, "0.01", "011", "0x3", 3, 5, "0.03", "0.02"),
        (5, "0.03", "101", "0x5", 5, None, None, None),
    ]
    rising = sampled_rows(result, (2, 9, 0), 5, "rising")
    assert [(row.sample_index, row.decimal) for row in rising] == [
        (2, 7),
        (5, 5),
    ]
    falling = sampled_rows(result, (2, 9, 0), 5, "falling")
    assert [(row.sample_index, row.decimal) for row in falling] == [
        (4, 3)
    ]
    assert bus_csv_bytes(transitions) == (
        b"sample_index,time_seconds,binary,hexadecimal,decimal,end_sample_index,"
        b"end_time_seconds,duration_seconds\n"
        b"0,-0.02,000,0x0,0,1,-0.01,0.01\n"
        b"1,-0.01,110,0x6,6,2,0,0.01\n"
        b"2,0,111,0x7,7,3,0.01,0.01\n"
        b"3,0.01,011,0x3,3,5,0.03,0.02\n"
        b"5,0.03,101,0x5,5,,,\n"
    )


def test_openapi_freezes_every_public_wire_shape_and_generated_types() -> None:
    document = json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8"))
    paths = document["paths"]
    expected = {
        "/api/v1/health": "get",
        "/api/v1/readiness": "get",
        "/api/v1/imports": "post",
        "/api/v1/captures/{capture_id}": "get",
        "/api/v1/captures/{capture_id}/channels": "get",
        "/api/v1/captures/{capture_id}/waveform": "get",
        "/api/v1/captures/{capture_id}/bus": "post",
        "/api/v1/captures/{capture_id}/exports": "post",
        "/api/v1/operations/{operation_id}": "get",
        "/api/v1/operations/{operation_id}/cancel": "post",
        "/api/v1/shutdown": "post",
    }
    assert {path: next(iter(operation)) for path, operation in paths.items()} == expected

    for path, method in expected.items():
        operation = paths[path][method]
        if method == "post" and path != "/api/v1/shutdown":
            assert "requestBody" in operation, f"{path} has no frozen request shape"
        for status, response in operation["responses"].items():
            if status == "204":
                continue
            if "$ref" not in response:
                assert response.get("content"), f"{path} {status} has no response schema"

    multipart = paths["/api/v1/imports"]["post"]["requestBody"]["content"][
        "multipart/form-data"
    ]["schema"]
    assert multipart["additionalProperties"] is False
    assert set(multipart["properties"]) == {"artifact", "metadata"}

    generated = (ROOT / "web/src/api.generated.ts").read_text(encoding="utf-8")
    for required_type in (
        "CaptureMetadata",
        "Channel",
        "WaveformWindow",
        "BusRequest",
        "BusPage",
        "ExportRequest",
        "Operation",
        "ErrorEnvelope",
    ):
        assert required_type in generated


def test_waveform_window_preserves_transitions_in_narrow_pulses() -> None:
    app = create_app("127.0.0.1", 4173)
    result = CaptureResult(
        CaptureConfig(100, 2, 6, 0, "rising", (0,)),
        np.asarray([0, 0, 1, 0, 0, 0, 0, 0], dtype=np.uint8),
        _device(),
    )
    app["captures"]["c00000001"] = result
    handler = next(
        route.handler
        for route in app.router.routes()
        if route.method == "GET"
        and route.resource.canonical == "/api/v1/captures/{capture_id}/waveform"
    )
    request = SimpleNamespace(
        match_info={"capture_id": "c00000001"},
        query={"start": "0", "end": "8", "pixel_width": "2", "channel_ids": "0"},
    )
    response = asyncio.run(handler(request))
    payload = json.loads(response.body)
    points = payload["channels"][0]["transitions"]
    assert points == [
        {"sample_index": 0, "value": 0},
        {"sample_index": 2, "value": 1},
        {"sample_index": 3, "value": 0},
        {"sample_index": 7, "value": 0},
    ]


def test_replay_import_does_not_require_csv_metadata(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app = create_app("127.0.0.1", 4173)
    handler = next(
        route.handler
        for route in app.router.routes()
        if route.method == "POST" and route.resource.canonical == "/api/v1/imports"
    )

    async def replay_parts(_: object) -> tuple[bytes, None]:
        return b"literal-replay-container", None

    monkeypatch.setattr(web_server, "_multipart_import", replay_parts)
    request = SimpleNamespace(
        headers=CIMultiDict({
            "Origin": app["canonical_origin"],
            "Cookie": f"pico_la_capability={app['capability']}",
        })
    )
    response = asyncio.run(handler(request))
    assert response.status != 400
