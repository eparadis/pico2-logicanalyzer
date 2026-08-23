"""Fresh C2-B4 round-four checker and maximum replay verification."""

from __future__ import annotations

import asyncio
import copy
import importlib.util
import io
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from multidict import CIMultiDict

from pico_logic_analyzer.web import server as web_server
from pico_logic_analyzer.web.server import COOKIE, create_app

ROOT = Path(__file__).parents[2]


def _checker() -> object:
    spec = importlib.util.spec_from_file_location("round4_openapi", ROOT / "tools/check_openapi.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _contract() -> tuple[dict[str, object], str]:
    return (
        json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8")),
        (ROOT / "web/src/api.generated.ts").read_text(encoding="utf-8"),
    )


def test_checker_rejects_nested_wire_type_mutation() -> None:
    checker = _checker()
    document, types = _contract()
    mutated = copy.deepcopy(document)
    mutated["components"]["schemas"]["BusPage"]["properties"]["rows"]["items"][
        "properties"
    ]["decimal"]["type"] = "string"
    with pytest.raises(AssertionError):
        checker.validate(mutated, types)


def test_checker_rejects_generated_bus_type_mutation() -> None:
    checker = _checker()
    document, types = _contract()
    mutated_types = types.replace("decimal: number", "decimal: string")
    assert mutated_types != types
    with pytest.raises(AssertionError):
        checker.validate(document, mutated_types)


def _maximum_schema1_replay() -> bytes:
    count = 16_777_216
    metadata = {
        "actual_count": count,
        "channel_ids": list(range(8)),
        "channel_labels": [f"D{i}" for i in range(8)],
        "channel_mapping": [f"D{i}" for i in range(8)],
        "device": {
            "capabilities": {
                "blast_frequency_hz": 1_000_000,
                "buffer_size": count,
                "channel_count": 8,
                "max_frequency_hz": 1_000_000,
            },
            "identity": "LOGIC_ANALYZER_TEST_V6_0",
        },
        "post_trigger_samples": count - 1,
        "pre_trigger_samples": 1,
        "provisional": True,
        "requested_count": count,
        "sample_rate_hz": 100,
        "schema_version": 1,
        "trigger_channel": 0,
        "trigger_edge": "rising",
        "trigger_index": 1,
    }
    metadata_bytes = json.dumps(
        metadata, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    output = io.BytesIO()
    np.savez(
        output,
        samples=np.zeros(count, dtype=np.uint8),
        metadata=np.frombuffer(metadata_bytes, dtype=np.uint8),
    )
    return output.getvalue()


def test_maximum_accepted_schema1_replay_completes_browser_import(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def exercise() -> None:
        artifact = _maximum_schema1_replay()
        assert len(artifact) <= web_server.MAX_UPLOAD_BYTES
        app = create_app("127.0.0.1", 4173)
        handler = next(
            route.handler
            for route in app.router.routes()
            if route.method == "POST" and route.resource.canonical == "/api/v1/imports"
        )

        async def parts(_: object) -> tuple[bytes, None, str]:
            return artifact, None, "application/x-pico-la-replay"

        monkeypatch.setattr(web_server, "_multipart_import", parts)
        headers = CIMultiDict({
            "Origin": app["canonical_origin"],
            "Cookie": f"{COOKIE}={app['capability']}",
        })
        response = await handler(SimpleNamespace(headers=headers))
        assert response.status == 202
        for _ in range(200):
            if app["operation"]["state"] in {"succeeded", "failed", "cancelled"}:
                break
            await asyncio.sleep(0.01)
        assert app["operation"]["state"] == "succeeded"
        capture_id = app["operation"]["capture_id"]
        assert len(app["captures"][capture_id].samples) == 16_777_216
        await app.cleanup()

    asyncio.run(exercise())
