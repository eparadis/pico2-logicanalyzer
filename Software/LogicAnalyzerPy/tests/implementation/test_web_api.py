from __future__ import annotations

import asyncio
import json
import socket

import pytest
from aiohttp import FormData
from aiohttp.test_utils import TestClient, TestServer

from pico_logic_analyzer.web.server import COOKIE, create_app

CSV = b"sample_index,time_seconds,trigger,D0,D1\n0,-0.01,0,0,0\n1,0,1,1,0\n2,0.01,0,1,1\n"
METADATA = {
    "channel_ids": [0, 1],
    "sample_rate_hz": 100,
    "trigger_channel": 0,
    "trigger_edge": "rising",
}


async def _exercise() -> None:
    try:
        with socket.socket() as socket_probe:
            socket_probe.bind(("127.0.0.1", 0))
            port = int(socket_probe.getsockname()[1])
    except PermissionError:
        pytest.skip("sandbox prohibits loopback socket verification")
    app = create_app("127.0.0.1", port)
    server = TestServer(app, host="127.0.0.1", port=port)
    client = TestClient(server)
    await client.start_server()
    try:
        host = f"127.0.0.1:{port}"
        assert (await client.get("/api/v1/health", headers={"Host": host})).status == 200
        cookie = app["capability"]
        headers = {"Host": host, "Origin": app["canonical_origin"], "Cookie": f"{COOKIE}={cookie}"}
        form = FormData()
        form.add_field("artifact", CSV, content_type="text/csv", filename="ignored.csv")
        form.add_field("metadata", json.dumps(METADATA), content_type="application/json")
        imported = await client.post("/api/v1/imports", headers=headers, data=form)
        assert imported.status == 201
        capture_id = (await imported.json())["capture_id"]
        denied = await client.post(f"/api/v1/captures/{capture_id}/bus", json={})
        assert denied.status == 403
        bus = await client.post(
            f"/api/v1/captures/{capture_id}/bus",
            headers=headers,
            json={
                "mode": "transition",
                "channel_ids": [0, 1],
                "strobe_channel": None,
                "edge": None,
                "offset": 0,
                "limit": 10,
            },
        )
        assert bus.status == 200 and (await bus.json())["total"] == 2
        wave = await client.get(
            f"/api/v1/captures/{capture_id}/waveform?start=0&end=3&channel_ids=0&pixel_width=1",
            headers={"Host": host},
        )
        assert wave.status == 200 and len((await wave.json())["channels"][0]["transitions"]) == 2
        exported = await client.post(
            f"/api/v1/captures/{capture_id}/exports",
            headers=headers,
            json={
                "format": "bus-transition-csv",
                "channel_ids": [0],
                "strobe_channel": None,
                "edge": None,
            },
        )
        assert (
            exported.status == 200
            and exported.headers["Content-Disposition"] == 'attachment; filename="pico-la-bus.csv"'
        )
    finally:
        await client.close()


def test_import_bus_waveform_and_export_share_python_authority() -> None:
    asyncio.run(_exercise())
