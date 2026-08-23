"""Bounded loopback-only REST API for offline captures (no serial service)."""

from __future__ import annotations

import asyncio
import hmac
import ipaddress
import secrets
import threading
import time
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Final, Literal, cast

import numpy as np
from aiohttp import BodyPartReader, web
from numpy.typing import NDArray

from pico_logic_analyzer.analysis import bus_csv_bytes, sampled_rows, transition_rows
from pico_logic_analyzer.formats.capture import import_csv_bytes
from pico_logic_analyzer.formats.replay import import_replay_bytes
from pico_logic_analyzer.model import CaptureResult, ProtocolError, ValidationError

ASSET_ROOT = Path(__file__).with_name("assets")
COOKIE = "pico_la_capability"
MAX_REQUEST_BYTES = 4 * 1024 * 1024
# Schema-2 permits a 2 MiB archive; multipart framing and metadata have headroom.
MAX_UPLOAD_BYTES = 3 * 1024 * 1024
MAX_WINDOW_SAMPLES = 100_000
MAX_PIXEL_WIDTH = 4096
MAX_BUS_ROWS = 10_000
MAX_CAPTURES = 16
MAX_ACTIVE_CONNECTIONS = 8
MAX_REQUESTS_PER_WINDOW = 32
REQUEST_WINDOW_SECONDS = 1.0
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
    _loopback(host)
    if not 1 <= port <= 65535:
        raise ValueError("canonical port must be between 1 and 65535")
    return f"[{host}]:{port}" if ":" in host else f"{host}:{port}"


def valid_mutation_origin(origin: str | None, canonical_origin: str) -> bool:
    return origin is not None and hmac.compare_digest(origin, canonical_origin)


def _single_capability(request: web.Request, expected: str) -> bool:
    values: list[str] = []
    for header in request.headers.getall("Cookie", []):
        for item in header.split(";"):
            name, separator, value = item.strip().partition("=")
            if separator and name == COOKIE:
                values.append(value)
    return len(values) == 1 and hmac.compare_digest(values[0], expected)


def _single_origin(request: web.Request, canonical_origin: str) -> bool:
    origins = request.headers.getall("Origin", [])
    return len(origins) == 1 and valid_mutation_origin(origins[0], canonical_origin)


def _reserve_server(host: str, port: int) -> tuple[str, int]:
    owner = (host, port)
    with _OWNERSHIP_LOCK:
        if owner in _OWNED_SERVERS:
            raise RuntimeError("local web server already owns this loopback address")
        _OWNED_SERVERS.add(owner)
    return owner


def _release_server(owner: tuple[str, int]) -> None:
    with _OWNERSHIP_LOCK:
        _OWNED_SERVERS.discard(owner)


def _error(status: int, code: str) -> web.Response:
    return web.json_response({"error": {"code": code, "message": code}}, status=status)


def _exact_object(value: object, keys: set[str]) -> dict[str, object] | None:
    return value if isinstance(value, dict) and set(value) == keys else None


def _capture_json(result: CaptureResult, capture_id: str) -> dict[str, object]:
    config = result.config
    return {
        "capture_id": capture_id,
        "sample_count": len(result.samples),
        "sample_rate_hz": config.sample_rate_hz,
        "trigger_index": result.trigger_index,
        "trigger_channel": config.trigger_channel,
        "trigger_edge": config.trigger_edge,
        "channel_ids": list(config.channel_ids),
    }


def _channels_json(result: CaptureResult) -> dict[str, object]:
    return {
        "channels": [
            {"channel_id": channel, "label": label, "packed_position": pos}
            for pos, (channel, label) in enumerate(
                zip(result.config.channel_ids, result.channel_labels, strict=True)
            )
        ]
    }


def _reduced_transitions(
    bits: NDArray[np.uint8], start: int, end: int, pixels: int
) -> list[dict[str, int]]:
    """Keep endpoint state and first/last change in each pixel bucket."""
    changes = np.flatnonzero(bits[start + 1 : end] != bits[start : end - 1]) + start + 1
    width = end - start
    selected = {start, end - 1}
    for bucket in range(pixels):
        low = start + (bucket * width) // pixels
        high = start + ((bucket + 1) * width) // pixels
        visible = changes[(changes >= low) & (changes < high)]
        if len(visible):
            selected.add(int(visible[0]))
            selected.add(int(visible[-1]))
    return [{"sample_index": index, "value": int(bits[index])} for index in sorted(selected)]


def _parse_metadata(value: bytes) -> dict[str, object] | None:
    try:
        import json

        decoded = json.loads(value.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None
    return _exact_object(
        decoded, {"channel_ids", "sample_rate_hz", "trigger_channel", "trigger_edge"}
    )


def _channel_ids(value: object) -> tuple[int, ...]:
    if not isinstance(value, list) or any(type(item) is not int for item in value):
        raise ValueError("invalid channel ids")
    return tuple(value)


def _edge(value: object) -> Literal["rising", "falling"]:
    if value not in {"rising", "falling"}:
        raise ValueError("invalid edge")
    return cast(Literal["rising", "falling"], value)


def _integer(value: object) -> int:
    if type(value) is not int:
        raise ValueError("invalid integer")
    return value


async def _multipart_import(
    request: web.Request,
) -> tuple[bytes, dict[str, object] | None, str] | None:
    try:
        reader = await request.multipart()
        parts: dict[str, bytes] = {}
        artifact_type: str | None = None
        aggregate = 0
        while (part := await reader.next()) is not None:
            if not isinstance(part, BodyPartReader):
                return None
            name = part.name
            if not isinstance(name, str) or name not in {"artifact", "metadata"} or name in parts:
                return None
            total = 0
            chunks: list[bytes] = []
            while chunk := await part.read_chunk(64 * 1024):
                total += len(chunk)
                aggregate += len(chunk)
                if total > MAX_UPLOAD_BYTES or aggregate > MAX_UPLOAD_BYTES:
                    return None
                chunks.append(chunk)
            parts[name] = b"".join(chunks)
            if name == "artifact":
                artifact_type = part.headers.get("Content-Type")
                if artifact_type not in {"text/csv", "application/x-pico-la-replay"}:
                    return None
            if name == "metadata" and part.headers.get("Content-Type") != "application/json":
                return None
        if set(parts) not in ({"artifact"}, {"artifact", "metadata"}) or artifact_type is None:
            return None
        if artifact_type == "text/csv" and set(parts) != {"artifact", "metadata"}:
            return None
        return parts["artifact"], _parse_metadata(parts.get("metadata", b"")), artifact_type
    except (ValueError, web.HTTPException):
        return None


def _decode_import(
    artifact: bytes, metadata: dict[str, object] | None, media_type: str
) -> CaptureResult:
    if media_type == "application/x-pico-la-replay":
        return import_replay_bytes(artifact)
    if metadata is None:
        raise ValidationError("CSV import metadata is required")
    return import_csv_bytes(
        artifact,
        channel_ids=_channel_ids(metadata["channel_ids"]),
        sample_rate_hz=_integer(metadata["sample_rate_hz"]),
        trigger_channel=_integer(metadata["trigger_channel"]),
        trigger_edge=_edge(metadata["trigger_edge"]),
    )


def create_app(host: str, port: int) -> web.Application:
    host = _loopback(host)
    if not 0 <= port <= 65535:
        raise ValueError("--port must be between 0 and 65535")
    app = web.Application(client_max_size=MAX_REQUEST_BYTES)
    app.update(
        canonical_host=host,
        canonical_port=port,
        capability=secrets.token_urlsafe(32),
        capability_active=True,
        canonical_origin=f"{ORIGIN_SCHEME}://{canonical_authority(host, port)}" if port else None,
        shutdown_requested=False,
        shutdown_event=asyncio.Event(),
        captures={},
        operation=None,
        operation_task=None,
        operation_cancel=None,
        next_operation=1,
        active_connections=0,
        request_times=[],
    )

    @web.middleware
    async def canonical_host(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.StreamResponse]]
    ) -> web.StreamResponse:
        expected = canonical_authority(app["canonical_host"], app["canonical_port"])
        if request.host != expected:
            return _error(400, "invalid_host")
        return await handler(request)

    @web.middleware
    async def request_limit(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.StreamResponse]]
    ) -> web.StreamResponse:
        if request.content_length is not None and request.content_length > MAX_REQUEST_BYTES:
            return _error(413, "request_too_large")
        return await handler(request)

    @web.middleware
    async def connection_limit(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.StreamResponse]]
    ) -> web.StreamResponse:
        # Loopback is single-user, but a finite in-flight owner bound prevents
        # slow clients from retaining unbounded request bodies or tasks.
        if app["active_connections"] >= MAX_ACTIVE_CONNECTIONS:
            return _error(429, "connection_limit")
        app["active_connections"] += 1
        try:
            return await handler(request)
        finally:
            app["active_connections"] -= 1

    @web.middleware
    async def request_rate(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.StreamResponse]]
    ) -> web.StreamResponse:
        now = time.monotonic()
        timestamps = cast(list[float], app["request_times"])
        cutoff = now - REQUEST_WINDOW_SECONDS
        timestamps[:] = [stamp for stamp in timestamps if stamp > cutoff]
        if len(timestamps) >= MAX_REQUESTS_PER_WINDOW:
            return _error(429, "rate_limited")
        timestamps.append(now)
        return await handler(request)

    @web.middleware
    async def websocket_boundary(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.StreamResponse]]
    ) -> web.StreamResponse:
        if request.headers.get("Upgrade", "").lower() == "websocket":
            return _error(403, "websocket_not_supported")
        return await handler(request)

    app.middlewares.extend(
        (canonical_host, request_limit, websocket_boundary, connection_limit, request_rate)
    )

    def mutation(request: web.Request) -> web.Response | None:
        if (
            not app["capability_active"]
            or app["canonical_origin"] is None
            or not _single_origin(request, app["canonical_origin"])
            or not _single_capability(request, app["capability"])
        ):
            return _error(403, "forbidden")
        return None

    async def health(_: web.Request) -> web.Response:
        return web.json_response({"status": "ready", "api_version": "v1"})

    async def index(_: web.Request) -> web.FileResponse:
        response = web.FileResponse(ASSET_ROOT / "index.html")
        response.set_cookie(COOKIE, app["capability"], httponly=True, samesite="Strict", path="/")
        return response

    async def imports(request: web.Request) -> web.Response:
        if (denied := mutation(request)) is not None:
            return denied
        current = app["operation"]
        if current is not None and current["state"] in {"pending", "running", "cancelling"}:
            # This deliberately precedes multipart consumption: a conflicting
            # upload is rejected without allocating or reading its body.
            return _error(409, "operation_conflict")
        parsed = await _multipart_import(request)
        if parsed is None:
            return _error(400, "invalid_multipart")
        if len(parsed) == 2:  # compatibility with direct focused handler fixtures
            artifact, metadata = parsed
            media_type = "application/x-pico-la-replay" if metadata is None else "text/csv"
        else:
            artifact, metadata, media_type = parsed
        operation = {
            "operation_id": f"op-{app['next_operation']}",
            "state": "pending",
            "capture_id": None,
        }
        app["next_operation"] += 1
        app["operation"] = operation
        cancelled = asyncio.Event()
        app["operation_cancel"] = cancelled

        async def run_import() -> None:
            try:
                # Guarantee a pollable pending state before offline CPU work.
                await asyncio.sleep(0)
                if cancelled.is_set():
                    operation["state"] = "cancelled"
                    return
                operation["state"] = "running"
                result = await asyncio.to_thread(_decode_import, artifact, metadata, media_type)
                if cancelled.is_set():
                    operation["state"] = "cancelled"
                    return
                if len(app["captures"]) >= MAX_CAPTURES:
                    operation["state"] = "failed"
                    return
                capture_id = f"c{len(app['captures']) + 1:08x}"
                app["captures"][capture_id] = result
                operation["capture_id"] = capture_id
                operation["state"] = "succeeded"
            except (ProtocolError, ValidationError, TypeError, ValueError):
                operation["state"] = "cancelled" if cancelled.is_set() else "failed"
            except asyncio.CancelledError:
                operation["state"] = "cancelled"
                raise
            finally:
                # No import bytes survive completion, cancellation, or shutdown.
                if app["operation"] is operation:
                    app["operation_task"] = None
                    app["operation_cancel"] = None

        app["operation_task"] = asyncio.create_task(run_import())
        return web.json_response(operation, status=202)

    def capture(request: web.Request) -> CaptureResult | None:
        return cast(dict[str, CaptureResult], app["captures"]).get(request.match_info["capture_id"])

    async def capture_metadata(request: web.Request) -> web.Response:
        result = capture(request)
        return (
            _error(404, "not_found")
            if result is None
            else web.json_response(_capture_json(result, request.match_info["capture_id"]))
        )

    async def channels(request: web.Request) -> web.Response:
        result = capture(request)
        return (
            _error(404, "not_found")
            if result is None
            else web.json_response(_channels_json(result))
        )

    async def waveform(request: web.Request) -> web.Response:
        result = capture(request)
        if result is None:
            return _error(404, "not_found")
        try:
            start, end, pixels = (
                int(request.query[key]) for key in ("start", "end", "pixel_width")
            )
            ids = tuple(int(value) for value in request.query.get("channel_ids", "").split(","))
        except (KeyError, ValueError):
            return _error(400, "invalid_window")
        if (
            not 0 <= start < end <= len(result.samples)
            or end - start > MAX_WINDOW_SAMPLES
            or not 1 <= pixels <= MAX_PIXEL_WIDTH
            or not ids
            or len(ids) > 24
            or len(set(ids)) != len(ids)
            or any(channel not in result.config.channel_ids for channel in ids)
        ):
            return _error(400, "invalid_window")
        output = []
        for channel in ids:
            bits = result.channel_samples(channel)
            points = _reduced_transitions(bits, start, end, pixels)
            output.append({"channel_id": channel, "transitions": points})
        return web.json_response({"start": start, "end": end, "channels": output})

    async def bus(request: web.Request) -> web.Response:
        if (denied := mutation(request)) is not None:
            return denied
        result = capture(request)
        if result is None:
            return _error(404, "not_found")
        try:
            value = _exact_object(
                await request.json(),
                {"mode", "channel_ids", "strobe_channel", "edge", "offset", "limit"},
            )
            if value is None:
                raise ValueError
            ids = _channel_ids(value["channel_ids"])
            offset, limit = _integer(value["offset"]), _integer(value["limit"])
            if (
                type(offset) is not int
                or type(limit) is not int
                or not 0 <= offset
                or not 1 <= limit <= MAX_BUS_ROWS
            ):
                raise ValueError
            if value["mode"] == "transition":
                if value["strobe_channel"] is not None or value["edge"] is not None:
                    raise ValueError
                rows = transition_rows(result, ids)
            elif value["mode"] == "sampled":
                rows = sampled_rows(
                    result, ids, _integer(value["strobe_channel"]), _edge(value["edge"])
                )
            else:
                raise ValueError
        except (ValueError, TypeError, ValidationError):
            return _error(400, "invalid_bus_request")
        page = rows[offset : offset + limit]
        return web.json_response(
            {
                "rows": [row.json_object() for row in page],
                "offset": offset,
                "total": len(rows),
                "next_offset": offset + len(page) if offset + len(page) < len(rows) else None,
            }
        )

    async def exports(request: web.Request) -> web.Response:
        if (denied := mutation(request)) is not None:
            return denied
        result = capture(request)
        if result is None:
            return _error(404, "not_found")
        try:
            value = _exact_object(
                await request.json(), {"format", "channel_ids", "strobe_channel", "edge"}
            )
            if value is None:
                raise ValueError
            if value["format"] == "bus-transition-csv":
                if value["strobe_channel"] is not None or value["edge"] is not None:
                    raise ValueError
                rows = transition_rows(result, _channel_ids(value["channel_ids"]))
            elif value["format"] == "bus-sampled-csv":
                rows = sampled_rows(
                    result,
                    _channel_ids(value["channel_ids"]),
                    _integer(value["strobe_channel"]),
                    _edge(value["edge"]),
                )
            else:
                raise ValueError
        except (ValueError, TypeError, ValidationError):
            return _error(400, "invalid_export_request")
        return web.Response(
            body=bus_csv_bytes(rows),
            content_type="text/csv",
            headers={
                "Content-Disposition": 'attachment; filename="pico-la-bus.csv"',
                "X-Content-Type-Options": "nosniff",
            },
        )

    async def operation(request: web.Request) -> web.Response:
        current = app["operation"]
        return (
            _error(404, "not_found")
            if current is None or request.match_info["operation_id"] != current["operation_id"]
            else web.json_response(current)
        )

    async def cancel(request: web.Request) -> web.Response:
        if (denied := mutation(request)) is not None:
            return denied
        current = app["operation"]
        if current is None or request.match_info["operation_id"] != current["operation_id"]:
            return _error(404, "not_found")
        if current["state"] in {"succeeded", "failed", "cancelled"}:
            return _error(409, "operation_terminal")
        current["state"] = "cancelling"
        cancelled = cast(asyncio.Event | None, app["operation_cancel"])
        if cancelled is not None:
            cancelled.set()
        return web.json_response(current)

    async def shutdown(request: web.Request) -> web.Response:
        if (denied := mutation(request)) is not None:
            return denied
        app["capability_active"] = False
        app["shutdown_requested"] = True
        response = web.Response(status=204)
        response.del_cookie(COOKIE, path="/")
        asyncio.get_running_loop().call_later(0.01, app["shutdown_event"].set)
        return response

    async def options(_: web.Request) -> web.Response:
        return _error(405, "method_not_allowed")

    app.router.add_get("/api/v1/health", health)
    app.router.add_get("/api/v1/readiness", health)
    app.router.add_post("/api/v1/imports", imports)
    app.router.add_get("/api/v1/captures/{capture_id}", capture_metadata)
    app.router.add_get("/api/v1/captures/{capture_id}/channels", channels)
    app.router.add_get("/api/v1/captures/{capture_id}/waveform", waveform)
    app.router.add_post("/api/v1/captures/{capture_id}/bus", bus)
    app.router.add_post("/api/v1/captures/{capture_id}/exports", exports)
    app.router.add_get("/api/v1/operations/{operation_id}", operation)
    app.router.add_post("/api/v1/operations/{operation_id}/cancel", cancel)
    app.router.add_post("/api/v1/shutdown", shutdown, name="shutdown")
    app.router.add_get("/", index)
    app.router.add_static("/assets/", ASSET_ROOT / "assets", show_index=False)
    app.router.add_route("OPTIONS", "/{path:.*}", options)

    async def cleanup(_: web.Application) -> None:
        task = cast(asyncio.Task[None] | None, app["operation_task"])
        if task is not None and not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        app["operation_task"] = None
        app["operation_cancel"] = None
        app["active_connections"] = 0
        cast(list[float], app["request_times"]).clear()

    app.on_cleanup.append(cast(Callable[..., Awaitable[object]], cleanup))
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
        app["canonical_port"] = actual_port
        app["canonical_origin"] = f"{ORIGIN_SCHEME}://{canonical_authority(host, actual_port)}"
        print(f"pico-la web: ready {app['canonical_origin']}/", flush=True)
        await app["shutdown_event"].wait()
        return 0
    finally:
        await runner.cleanup()
        _release_server(owner)


def capability_matches(received: str, expected: str) -> bool:
    return hmac.compare_digest(received, expected)
