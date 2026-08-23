"""Fresh independent C2-B4 round-three concurrency and replay bounds."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
from multidict import CIMultiDict

from pico_logic_analyzer.web import server as web_server
from pico_logic_analyzer.web.server import COOKIE, MAX_REQUEST_BYTES, MAX_UPLOAD_BYTES, create_app


def _mutation_headers(app: object) -> CIMultiDict[str]:
    return CIMultiDict({
        "Origin": app["canonical_origin"],  # type: ignore[index]
        "Cookie": f"{COOKIE}={app['capability']}",  # type: ignore[index]
    })


def test_first_concurrent_import_reserves_owner_before_reading_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    async def exercise() -> None:
        app = create_app("127.0.0.1", 4173)
        handler = next(
            route.handler
            for route in app.router.routes()
            if route.method == "POST" and route.resource.canonical == "/api/v1/imports"
        )
        first_reading = asyncio.Event()
        release = asyncio.Event()
        entered = 0

        async def blocking_body(_: object) -> tuple[bytes, None, str]:
            nonlocal entered
            entered += 1
            if entered == 1:
                first_reading.set()
            await release.wait()
            return b"not-a-replay", None, "application/x-pico-la-replay"

        monkeypatch.setattr(web_server, "_multipart_import", blocking_body)
        request = SimpleNamespace(headers=_mutation_headers(app))
        first = asyncio.create_task(handler(request))
        await asyncio.wait_for(first_reading.wait(), timeout=0.5)
        second = asyncio.create_task(handler(request))
        await asyncio.sleep(0)
        observed_entered = entered
        observed_second_status = second.result().status if second.done() else None
        release.set()
        responses = await asyncio.gather(first, second)
        # The second request must have received 409 without entering body parsing.
        assert observed_entered == 1
        assert observed_second_status == 409
        assert sorted(response.status for response in responses) == [202, 409]
        await app.cleanup()

    asyncio.run(exercise())


def test_browser_replay_boundary_accommodates_accepted_schema1_archive_limit() -> None:
    accepted_archive_bytes = 32 * 1024 * 1024
    # Multipart framing requires additional headroom beyond the artifact itself.
    assert MAX_UPLOAD_BYTES >= accepted_archive_bytes
    assert MAX_REQUEST_BYTES > MAX_UPLOAD_BYTES
