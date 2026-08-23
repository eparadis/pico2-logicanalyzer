"""Loopback-only inert Cycle 2 web shell."""
from __future__ import annotations

import asyncio
import hmac
import ipaddress
import secrets
import threading
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Final

from aiohttp import web

ASSET_ROOT = Path(__file__).with_name("assets")
COOKIE = "pico_la_capability"
MAX_REQUEST_BYTES = 1 << 20
ORIGIN_SCHEME: Final = "http"
_OWNERSHIP_LOCK = threading.Lock()
_OWNED_SERVERS: set[tuple[str, int]] = set()


def _loopback(host: str) -> str:
    try:
        address = ipaddress.ip_address(host)
    except ValueError as exc:
        raise ValueError("--host must be a literal loopback address") from exc
    if not address.is_loopback:
        raise ValueError("--host must be a literal loopback address")
    return host


def canonical_authority(host: str, port: int) -> str:
    """Return the sole accepted Host authority; headers never influence it."""
    _loopback(host)
    if not 1 <= port <= 65535:
        raise ValueError("canonical port must be between 1 and 65535")
    return f"[{host}]:{port}" if ":" in host else f"{host}:{port}"


def valid_mutation_origin(origin: str | None, canonical_origin: str) -> bool:
    """Accept only the single literal origin constructed when the server binds."""
    return origin is not None and hmac.compare_digest(origin, canonical_origin)


def _single_capability(request: web.Request, expected: str) -> bool:
    """Validate a single, exact cookie without relying on lossy cookie parsing."""
    cookie_headers = request.headers.getall("Cookie", [])
    values: list[str] = []
    for header in cookie_headers:
        for item in header.split(";"):
            name, separator, value = item.strip().partition("=")
            if separator and name == COOKIE:
                values.append(value)
    return len(values) == 1 and hmac.compare_digest(values[0], expected)


def _single_origin(request: web.Request, canonical_origin: str) -> bool:
    origins = request.headers.getall("Origin", [])
    return len(origins) == 1 and valid_mutation_origin(origins[0], canonical_origin)


def _reserve_server(host: str, port: int) -> tuple[str, int]:
    """Reserve an explicit local bind within this process before starting aiohttp."""
    owner = (host, port)
    with _OWNERSHIP_LOCK:
        if owner in _OWNED_SERVERS:
            raise RuntimeError("local web server already owns this loopback address")
        _OWNED_SERVERS.add(owner)
    return owner


def _release_server(owner: tuple[str, int]) -> None:
    with _OWNERSHIP_LOCK:
        _OWNED_SERVERS.discard(owner)


def create_app(host: str, port: int) -> web.Application:
    """Create an inert server. It deliberately imports neither driver nor transport."""
    host = _loopback(host)
    if not 0 <= port <= 65535:
        raise ValueError("--port must be between 0 and 65535")
    app = web.Application(client_max_size=MAX_REQUEST_BYTES)
    app["canonical_host"] = host
    app["canonical_port"] = port
    app["capability"] = secrets.token_urlsafe(32)
    app["capability_active"] = True
    app["canonical_origin"] = (
        f"{ORIGIN_SCHEME}://{canonical_authority(host, port)}" if port else None
    )
    app["shutdown_requested"] = False
    app["shutdown_event"] = asyncio.Event()

    @web.middleware
    async def canonical_host(
        request: web.Request,
        handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
    ) -> web.StreamResponse:
        expected = canonical_authority(app["canonical_host"], app["canonical_port"])
        if request.host != expected:
            return web.Response(status=400, text="invalid Host\n")
        return await handler(request)

    app.middlewares.append(canonical_host)

    @web.middleware
    async def request_limit(
        request: web.Request,
        handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
    ) -> web.StreamResponse:
        content_length = request.content_length
        if content_length is not None and content_length > MAX_REQUEST_BYTES:
            return web.Response(status=413, text="request too large\n")
        return await handler(request)

    app.middlewares.append(request_limit)

    @web.middleware
    async def websocket_boundary(
        request: web.Request,
        handler: Callable[[web.Request], Awaitable[web.StreamResponse]],
    ) -> web.StreamResponse:
        if request.headers.get("Upgrade", "").lower() == "websocket" and (
            app["canonical_origin"] is None
            or not _single_origin(request, app["canonical_origin"])
            or not _single_capability(request, app["capability"])
        ):
            return web.Response(status=403, text="forbidden\n")
        return await handler(request)

    app.middlewares.append(websocket_boundary)

    async def health(_: web.Request) -> web.Response:
        return web.json_response({"status": "ready", "api_version": "v1"})

    async def index(_: web.Request) -> web.FileResponse:
        response = web.FileResponse(ASSET_ROOT / "index.html")
        response.set_cookie(COOKIE, app["capability"], httponly=True, samesite="Strict", path="/")
        return response

    async def options(_: web.Request) -> web.Response:
        return web.Response(status=405, text="method not allowed\n")

    async def shutdown(request: web.Request) -> web.Response:
        # The shell has no device work.  Keep all checks before its only state change.
        if (
            not app["capability_active"]
            or app["canonical_origin"] is None
            or not _single_origin(request, app["canonical_origin"])
            or not _single_capability(request, app["capability"])
        ):
            return web.Response(status=403, text="forbidden\n")
        app["capability_active"] = False
        app["shutdown_requested"] = True
        response = web.Response(status=204)
        response.del_cookie(COOKIE, path="/")
        asyncio.get_running_loop().call_later(0.01, app["shutdown_event"].set)
        return response

    app.router.add_get("/api/v1/health", health)
    app.router.add_get("/api/v1/readiness", health)
    app.router.add_post("/api/v1/shutdown", shutdown, name="shutdown")
    app.router.add_get("/", index)
    app.router.add_static("/assets/", ASSET_ROOT / "assets", show_index=False)
    app.router.add_route("OPTIONS", "/{path:.*}", options)
    return app


def run(host: str, port: int) -> int:
    try:
        return asyncio.run(_serve(host, port))
    except OSError:
        return 1


async def _serve(host: str, port: int) -> int:
    app = create_app(host, port)
    owner = _reserve_server(host, port)
    runner = web.AppRunner(app)
    try:
        await runner.setup()
        site = web.TCPSite(runner, host=host, port=port)
        await site.start()
        sockets = getattr(site._server, "sockets", [])
        if len(sockets) != 1:
            raise OSError("loopback server did not create exactly one listener")
        actual_port = int(sockets[0].getsockname()[1])
        authority = canonical_authority(host, actual_port)
        app["canonical_port"] = actual_port
        app["canonical_origin"] = f"{ORIGIN_SCHEME}://{authority}"
        print(f"pico-la web: ready {app['canonical_origin']}/", flush=True)
        await app["shutdown_event"].wait()
        return 0
    finally:
        await runner.cleanup()
        _release_server(owner)


def capability_matches(received: str, expected: str) -> bool:
    """Future mutating API endpoints use this constant-time comparison."""
    return hmac.compare_digest(received, expected)
