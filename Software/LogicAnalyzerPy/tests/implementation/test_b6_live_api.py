from __future__ import annotations

import asyncio
import json
import threading
from collections import deque
from types import SimpleNamespace

import numpy as np
import pytest
from multidict import CIMultiDict

from pico_logic_analyzer.driver import CaptureCancelled, V2DeviceService
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo
from pico_logic_analyzer.transport import TransportTimeout
from pico_logic_analyzer.web.server import COOKIE, create_app

DEVICE = DeviceInfo("LOGIC_ANALYZER_PICO_V6_0", 100_000_000, 125_000_000, 393_216, 24)
PORT = "/machine/local/secret-port"


def _handler(app: object, method: str, path: str) -> object:
    return next(
        route.handler
        for route in app.router.routes()
        if route.method == method and route.resource.canonical == path
    )


def _request(app: object, payload: object | None = None, **values: object) -> object:
    async def body() -> object:
        return payload

    return SimpleNamespace(
        headers=CIMultiDict(
            {
                "Origin": app["canonical_origin"],
                "Cookie": f"{COOKIE}={app['capability']}",
            }
        ),
        json=body,
        **values,
    )


def _capture(config: CaptureConfig) -> CaptureResult:
    dtype = config.sample_dtype
    samples = np.arange(config.requested_count, dtype=dtype)
    return CaptureResult(config, samples, DEVICE)


class FakeService:
    def __init__(self, *, block: bool = False) -> None:
        self.ports: list[str] = []
        self.identities = 0
        self.captures = 0
        self.block = block
        self.closed = True

    def identify(self, port: str, timeout: float = 10.0) -> DeviceInfo:
        assert 0 < timeout <= 30
        self.ports.append(port)
        self.identities += 1
        self.closed = True
        return DEVICE

    def capture_cancellable(
        self, port: str, config: CaptureConfig, cancelled: threading.Event, timeout: float = 10.0
    ) -> CaptureResult:
        self.ports.append(port)
        self.captures += 1
        self.closed = False
        try:
            if self.block:
                assert cancelled.wait(2)
                raise CaptureCancelled("private path must never escape")
            return _capture(config)
        finally:
            self.closed = True


class FailingService(FakeService):
    def __init__(self, failure: str) -> None:
        super().__init__()
        self.failure = failure

    def identify(self, port: str, timeout: float = 10.0) -> DeviceInfo:
        if self.failure == "identify":
            raise ConnectionError(f"cannot open {port}")
        return super().identify(port, timeout)

    def capture_cancellable(
        self, port: str, config: CaptureConfig, cancelled: threading.Event, timeout: float = 10.0
    ) -> CaptureResult:
        if self.failure == "timeout":
            self.closed = True
            raise TimeoutError(f"capture timed out on {port}")
        return super().capture_cancellable(port, config, cancelled, timeout)


CAPTURE_BODY = {
    "sample_rate_hz": 100_000,
    "pre_trigger_samples": 4,
    "post_trigger_samples": 12,
    "trigger_channel": 0,
    "trigger_edge": "rising",
    "channel_ids": list(range(8)),
    "timeout_seconds": 2,
}


def test_identify_capture_reconnect_and_second_capture_are_opaque() -> None:
    async def exercise() -> None:
        service = FakeService()
        app = create_app("127.0.0.1", 4173, device_port=PORT, device_service=service)
        identify = _handler(app, "POST", "/api/v1/device/identify")
        reconnect = _handler(app, "POST", "/api/v1/device/reconnect")
        live = _handler(app, "POST", "/api/v1/device/captures")
        operation = _handler(app, "GET", "/api/v1/operations/{operation_id}")

        identified = await identify(_request(app))
        public = json.loads(identified.body)
        assert public == {
            "device_id": "device-1",
            "connected": True,
            "max_frequency_hz": 100_000_000,
            "blast_frequency_hz": 125_000_000,
            "buffer_size": 393_216,
            "channel_count": 24,
        }
        assert PORT not in identified.text and DEVICE.identity not in identified.text
        assert (await reconnect(_request(app))).status == 200

        capture_ids = []
        for width in (8, 16, 24):
            body = {**CAPTURE_BODY, "channel_ids": list(range(width))}
            accepted = await live(_request(app, body))
            assert accepted.status == 202 and PORT not in accepted.text
            operation_id = json.loads(accepted.body)["operation_id"]
            for _ in range(100):
                await asyncio.sleep(0)
                current = await operation(
                    SimpleNamespace(match_info={"operation_id": operation_id})
                )
                payload = json.loads(current.body)
                if payload["state"] == "succeeded":
                    capture_ids.append(payload["capture_id"])
                    break
            else:
                raise AssertionError("fake capture did not complete")
        assert len(set(capture_ids)) == 3
        assert service.identities == 2 and service.captures == 3 and service.closed
        assert service.ports == [PORT, PORT, PORT, PORT, PORT]
        await app.cleanup()

    asyncio.run(exercise())


def test_cancel_conflict_shutdown_and_errors_leave_no_serial_owner_or_secret() -> None:
    async def exercise() -> None:
        service = FakeService(block=True)
        app = create_app("127.0.0.1", 4173, device_port=PORT, device_service=service)
        live = _handler(app, "POST", "/api/v1/device/captures")
        cancel = _handler(app, "POST", "/api/v1/operations/{operation_id}/cancel")
        operation = _handler(app, "GET", "/api/v1/operations/{operation_id}")
        first = await live(_request(app, CAPTURE_BODY))
        operation_id = json.loads(first.body)["operation_id"]
        await asyncio.sleep(0)
        assert (await live(_request(app, CAPTURE_BODY))).status == 409
        cancelling = await cancel(
            _request(app, match_info={"operation_id": operation_id})
        )
        assert cancelling.status == 200
        for _ in range(100):
            await asyncio.sleep(0)
            terminal = await operation(SimpleNamespace(match_info={"operation_id": operation_id}))
            if json.loads(terminal.body)["state"] == "cancelled":
                break
        assert service.closed and app["operation_task"] is None
        assert PORT not in terminal.text and "private path" not in terminal.text
        await app.cleanup()

    asyncio.run(exercise())


def test_live_api_requires_launch_port_and_exact_capture_shape() -> None:
    async def exercise() -> None:
        app = create_app("127.0.0.1", 4173, device_service=FakeService())
        identify = _handler(app, "POST", "/api/v1/device/identify")
        live = _handler(app, "POST", "/api/v1/device/captures")
        assert (await identify(_request(app))).status == 409
        assert (await live(_request(app, CAPTURE_BODY))).status == 409
        configured = create_app(
            "127.0.0.1", 4174, device_port=PORT, device_service=FakeService()
        )
        configured_live = _handler(configured, "POST", "/api/v1/device/captures")
        invalid = await configured_live(_request(configured, {**CAPTURE_BODY, "port": PORT}))
        assert invalid.status == 400 and PORT not in invalid.text
        await app.cleanup()
        await configured.cleanup()

    asyncio.run(exercise())


def test_live_mutations_reuse_exact_origin_and_cookie_boundary() -> None:
    async def exercise() -> None:
        service = FakeService()
        app = create_app("127.0.0.1", 4173, device_port=PORT, device_service=service)
        for path in (
            "/api/v1/device/identify",
            "/api/v1/device/reconnect",
            "/api/v1/device/captures",
        ):
            handler = _handler(app, "POST", path)
            denied = await handler(
                SimpleNamespace(headers=CIMultiDict(), json=_request(app, CAPTURE_BODY).json)
            )
            assert denied.status == 403
        assert service.ports == []
        await app.cleanup()

    asyncio.run(exercise())


def test_first_live_request_reserves_before_body_await() -> None:
    async def exercise() -> None:
        app = create_app("127.0.0.1", 4173, device_port=PORT, device_service=FakeService())
        live = _handler(app, "POST", "/api/v1/device/captures")
        gate = asyncio.Event()

        async def delayed_body() -> object:
            await gate.wait()
            return CAPTURE_BODY

        first = asyncio.create_task(
            live(
                SimpleNamespace(
                    headers=_request(app).headers,
                    json=delayed_body,
                )
            )
        )
        await asyncio.sleep(0)
        assert (await live(_request(app, CAPTURE_BODY))).status == 409
        gate.set()
        assert (await first).status == 202
        await app.cleanup()

    asyncio.run(exercise())


def test_shutdown_cancels_live_owner_and_closes_fake_serial() -> None:
    async def exercise() -> None:
        service = FakeService(block=True)
        app = create_app("127.0.0.1", 4173, device_port=PORT, device_service=service)
        live = _handler(app, "POST", "/api/v1/device/captures")
        shutdown = _handler(app, "POST", "/api/v1/shutdown")
        await live(_request(app, CAPTURE_BODY))
        await asyncio.sleep(0)
        response = await shutdown(_request(app))
        assert response.status == 204
        for _ in range(100):
            await asyncio.sleep(0)
            if app["operation_task"] is None:
                break
        assert service.closed and app["operation"]["state"] == "cancelled"
        await app.cleanup()

    asyncio.run(exercise())


class RecoveryTransport:
    def __init__(self, lines: list[str]) -> None:
        self.lines = deque(lines)
        self.writes: list[bytes] = []
        self.closed = False

    def open(self) -> None:
        self.closed = False

    def close(self) -> None:
        self.closed = True

    def write(self, data: bytes, timeout: float) -> None:
        self.writes.append(bytes(data))

    def read_line(self, timeout: float) -> str:
        if not self.lines:
            raise TransportTimeout("waiting for trigger")
        return self.lines.popleft()

    def read_exact(self, size: int, timeout: float) -> bytes:
        raise TransportTimeout("bounded recovery drain")


def test_device_owner_cancel_sends_one_recovery_byte_closes_and_reidentifies() -> None:
    identity = [
        "LOGIC_ANALYZER_PICO_V6_0",
        "FREQ:100000000",
        "BLASTFREQ:125000000",
        "BUFFER:393216",
        "CHANNELS:24",
    ]
    capture = RecoveryTransport(identity.copy())
    reopened = RecoveryTransport(identity.copy())
    transports = deque((capture, reopened))
    service = V2DeviceService(lambda _port, _timeout: transports.popleft())  # type: ignore[arg-type]
    cancelled = threading.Event()
    cancelled.set()
    with pytest.raises(CaptureCancelled):
        service.capture_cancellable(
            PORT,
            CaptureConfig(100_000, 4, 12, 0, "rising", tuple(range(8))),
            cancelled,
            1.0,
        )
    assert capture.writes[-1] == b"\xff" and capture.writes.count(b"\xff") == 1
    assert capture.closed and reopened.closed and not transports


def test_disconnect_and_timeout_are_terminal_sanitized_and_cleanup_owned() -> None:
    async def exercise() -> None:
        disconnected = create_app(
            "127.0.0.1", 4173, device_port=PORT, device_service=FailingService("identify")
        )
        identify = _handler(disconnected, "POST", "/api/v1/device/identify")
        response = await identify(_request(disconnected))
        assert response.status == 503 and PORT not in response.text
        timed_out_service = FailingService("timeout")
        timed_out = create_app(
            "127.0.0.1", 4174, device_port=PORT, device_service=timed_out_service
        )
        live = _handler(timed_out, "POST", "/api/v1/device/captures")
        operation = _handler(timed_out, "GET", "/api/v1/operations/{operation_id}")
        accepted = await live(_request(timed_out, CAPTURE_BODY))
        operation_id = json.loads(accepted.body)["operation_id"]
        for _ in range(100):
            await asyncio.sleep(0)
            terminal = await operation(SimpleNamespace(match_info={"operation_id": operation_id}))
            if json.loads(terminal.body)["state"] == "failed":
                break
        assert timed_out_service.closed and timed_out["operation_task"] is None
        assert PORT not in terminal.text
        await disconnected.cleanup()
        await timed_out.cleanup()

    asyncio.run(exercise())
