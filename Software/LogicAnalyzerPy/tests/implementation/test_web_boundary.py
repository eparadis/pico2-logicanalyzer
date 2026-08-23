from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
from multidict import CIMultiDict

from pico_logic_analyzer.web import server
from pico_logic_analyzer.web.server import (
    COOKIE,
    canonical_authority,
    create_app,
    valid_mutation_origin,
)


def _shutdown_handler(app: object) -> object:
    return next(route.handler for route in app.router["shutdown"] if route.method == "POST")


def test_loopback_canonical_authority_rejects_non_loopback_and_ephemeral() -> None:
    assert canonical_authority("127.0.0.1", 4173) == "127.0.0.1:4173"
    with pytest.raises(ValueError):
        canonical_authority("0.0.0.0", 4173)
    with pytest.raises(ValueError):
        canonical_authority("127.0.0.1", 0)


def test_mutation_origin_requires_exact_canonical_value() -> None:
    origin = "http://127.0.0.1:4173"
    assert valid_mutation_origin(origin, origin)
    assert not valid_mutation_origin(None, origin)
    assert not valid_mutation_origin("null", origin)
    assert not valid_mutation_origin("http://localhost:4173", origin)


def test_host_middleware_rejects_alternate_authorities() -> None:
    app = create_app("127.0.0.1", 4173)
    middleware = app.middlewares[0]

    async def handler(_: object) -> object:
        return "accepted"

    accepted = asyncio.run(middleware(SimpleNamespace(host="127.0.0.1:4173"), handler))
    rejected = asyncio.run(middleware(SimpleNamespace(host="localhost:4173"), handler))
    assert accepted == "accepted"
    assert rejected.status == 400


def test_initial_html_cookie_is_host_only_and_not_in_body() -> None:
    app = create_app("127.0.0.1", 4173)
    index = next(
        route.handler
        for route in app.router.routes()
        if route.method == "GET" and route.resource.canonical == "/"
    )
    response = asyncio.run(index(SimpleNamespace()))
    cookie = response.cookies[COOKIE]
    assert cookie["httponly"] and cookie["samesite"] == "Strict" and cookie["path"] == "/"
    assert not cookie["domain"]
    assert app["capability"] not in response.headers.get("Location", "")


@pytest.mark.parametrize(
    ("origin", "cookie"),
    [
        (None, None),
        ("null", None),
        ("https://127.0.0.1:4173", None),
        ("http://localhost:4173", None),
        ("http://127.0.0.1:4173", "invalid"),
        ("http://127.0.0.1:4173", "one; pico_la_capability=two"),
    ],
)
def test_shutdown_rejects_invalid_boundary_before_state_change(
    origin: str | None, cookie: str | None
) -> None:
    app = create_app("127.0.0.1", 4173)
    headers: dict[str, str] = {}
    if origin is not None:
        headers["Origin"] = origin
    if cookie is not None:
        headers["Cookie"] = f"{COOKIE}={cookie}"
    request = SimpleNamespace(headers=CIMultiDict(headers))
    response = asyncio.run(_shutdown_handler(app)(request))
    assert response.status == 403
    assert app["shutdown_requested"] is False


def test_shutdown_requires_canonical_origin_and_expires_capability() -> None:
    app = create_app("127.0.0.1", 4173)
    request = SimpleNamespace(
        headers=CIMultiDict({
            "Origin": app["canonical_origin"],
            "Cookie": f"{COOKIE}={app['capability']}",
        })
    )
    response = asyncio.run(_shutdown_handler(app)(request))
    assert response.status == 204 and app["shutdown_requested"] is True
    assert response.cookies[COOKIE]["max-age"] == "0"
    assert asyncio.run(_shutdown_handler(app)(request)).status == 403


def test_invalid_websocket_upgrade_is_rejected_before_route_handling() -> None:
    app = create_app("127.0.0.1", 4173)
    middleware = app.middlewares[2]
    request = SimpleNamespace(headers=CIMultiDict({"Upgrade": "websocket"}))

    async def handler(_: object) -> object:
        return "accepted"

    response = asyncio.run(middleware(request, handler))
    assert response.status == 403


def test_declared_oversized_request_is_rejected_before_handler() -> None:
    app = create_app("127.0.0.1", 4173)
    middleware = app.middlewares[1]
    request = SimpleNamespace(content_length=(1 << 20) + 1)

    async def handler(_: object) -> object:
        return "accepted"

    assert asyncio.run(middleware(request, handler)).status == 413


def test_duplicate_server_ownership_is_bounded_and_released() -> None:
    owner = server._reserve_server("127.0.0.1", 4173)
    with pytest.raises(RuntimeError, match="already owns"):
        server._reserve_server("127.0.0.1", 4173)
    server._release_server(owner)
    server._release_server(owner)
