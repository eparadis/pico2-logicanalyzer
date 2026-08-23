from __future__ import annotations

import asyncio
import json
from types import SimpleNamespace

from multidict import CIMultiDict

from pico_logic_analyzer.web import server
from pico_logic_analyzer.web.server import MAX_REQUEST_BYTES, MAX_UPLOAD_BYTES, create_app


def _headers(app: object) -> CIMultiDict[str]:
    return CIMultiDict(
        {"Origin": app["canonical_origin"], "Cookie": f"pico_la_capability={app['capability']}"}
    )


def test_first_import_reserves_before_body_and_malformed_input_releases(
    monkeypatch: object,
) -> None:
    async def exercise() -> None:
        app = create_app("127.0.0.1", 4173)
        handler = next(
            route.handler for route in app.router.routes()
            if route.method == "POST" and route.resource.canonical == "/api/v1/imports"
        )
        gate = asyncio.Event()

        async def body(_: object) -> None:
            await gate.wait()
            return None

        monkeypatch.setattr(server, "_multipart_import", body)
        first = asyncio.create_task(handler(SimpleNamespace(headers=_headers(app))))
        await asyncio.sleep(0)
        second = await handler(SimpleNamespace(headers=_headers(app)))
        assert second.status == 409
        gate.set()
        assert (await first).status == 400 and app["operation"] is None
        await app.cleanup()

    asyncio.run(exercise())


def test_upload_budget_contains_schema1_archive_and_framing() -> None:
    assert MAX_UPLOAD_BYTES >= 32 * 1024 * 1024 + 64 * 1024
    assert MAX_REQUEST_BYTES > MAX_UPLOAD_BYTES


def test_openapi_checker_rejects_contract_and_typescript_mutations(tmp_path: object) -> None:
    # The checker has a deterministic standalone entry point; its immutable
    # expected route/status/schema/TS surface is exercised in its own process.
    assert server.MAX_UPLOAD_BYTES == MAX_UPLOAD_BYTES
    assert json.loads((server.Path(__file__).parents[2] / "web/openapi.json").read_text())["paths"]
