"""Explicit-port V2 identity and normal-capture services."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import asdict, dataclass
from importlib import import_module
from math import isfinite
from threading import Event
from time import monotonic, sleep
from typing import Any

from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo, ProtocolError
from pico_logic_analyzer.protocol import (
    ByteParser,
    encode_capture_request,
    encode_identity_request,
    parse_capture_response,
    parse_identity,
)
from pico_logic_analyzer.transport.serial import DEFAULT_TIMEOUT_SECONDS, SerialTransport

from .recovery import CaptureRecovery


class CaptureCancelled(RuntimeError):
    """A requested live capture was cancelled after bounded recovery."""


@dataclass(frozen=True, slots=True)
class PortCandidate:
    device: str
    vid: int | None
    pid: int | None
    serial_number: str | None
    location: str | None
    description: str | None

    def json_object(self) -> dict[str, object | None]:
        return asdict(self)


def list_candidates(comports: Callable[[], Any] | None = None) -> list[PortCandidate]:
    if comports is None:
        try:
            list_ports = import_module("serial.tools.list_ports")
        except ImportError as exc:  # pragma: no cover - packaging failure
            raise ConnectionError("pySerial is not installed") from exc
        comports = list_ports.comports
    candidates = [
        PortCandidate(
            device=str(record.device),
            vid=record.vid,
            pid=record.pid,
            serial_number=getattr(record, "serial_number", None),
            location=getattr(record, "location", None),
            description=getattr(record, "description", None),
        )
        for record in comports()
        if getattr(record, "vid", None) == 0x1209 and getattr(record, "pid", None) == 0x3020
    ]
    return sorted(candidates, key=lambda candidate: candidate.device)


class V2DeviceService:
    def __init__(
        self, transport_factory: Callable[[str, float], SerialTransport] = SerialTransport
    ) -> None:
        self._transport_factory = transport_factory

    def identify(self, port: str, timeout: float = DEFAULT_TIMEOUT_SECONDS) -> DeviceInfo:
        transport = self._transport_factory(port, timeout)
        try:
            transport.open()
            transport.write(encode_identity_request(), timeout)
            response = b"".join(
                (transport.read_line(timeout) + "\n").encode("ascii") for _ in range(5)
            )
            return parse_identity(ByteParser(response))
        except (ConnectionError, TimeoutError, ProtocolError, ValueError):
            raise
        except Exception as exc:
            raise ConnectionError(f"identity read failed on {port}: {exc}") from exc
        finally:
            transport.close()

    def identify_after_reopen(
        self, port: str, timeout: float = DEFAULT_TIMEOUT_SECONDS
    ) -> tuple[DeviceInfo, DeviceInfo]:
        """Opt-in lifecycle smoke primitive; callers provide the one explicit port."""
        return self.identify(port, timeout), self.identify(port, timeout)

    def capture(
        self, port: str, config: CaptureConfig, timeout: float = DEFAULT_TIMEOUT_SECONDS
    ) -> CaptureResult:
        """Perform one bounded normal capture on the explicit port."""
        transport = self._transport_factory(port, timeout)
        try:
            transport.open()
            transport.write(encode_identity_request(), timeout)
            identity = b"".join(
                (transport.read_line(timeout) + "\n").encode("ascii") for _ in range(5)
            )
            device = parse_identity(ByteParser(identity))
            config.validate_for(device)
            transport.write(encode_capture_request(config, device), timeout)
            status = transport.read_line(timeout)
            count_bytes = transport.read_exact(4, timeout)
            count = int.from_bytes(count_bytes, "little")
            payload_size = count * config.bytes_per_word
            if count != config.requested_count or payload_size > device.buffer_size:
                raise ProtocolError("invalid capture count")
            # Count was checked before this allocation-free, negotiated-bounded read.
            count_and_payload = count_bytes + transport.read_exact(payload_size + 1, timeout)
            samples, _ = parse_capture_response(
                ByteParser((status + "\n").encode("ascii") + count_and_payload), config, device
            )
            return CaptureResult(
                config=config,
                samples=samples,
                device=device,
                channel_mapping=tuple(f"GPIO{channel + 2}" for channel in config.channel_ids),
            )
        except (ConnectionError, TimeoutError, ProtocolError, ValueError):
            raise
        except Exception as exc:
            raise ConnectionError(f"capture failed on {port}: {exc}") from exc
        finally:
            transport.close()

    def capture_cancellable(
        self,
        port: str,
        config: CaptureConfig,
        cancelled: Event,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
    ) -> CaptureResult:
        """Capture with same-thread timeout/cancel recovery ownership."""
        if not isinstance(cancelled, Event):
            raise TypeError("cancelled must be a threading.Event")
        transport = self._transport_factory(port, timeout)
        in_flight = False
        recovered = False
        deadline = monotonic() + timeout
        try:
            transport.open()
            transport.write(encode_identity_request(), timeout)
            identity = b"".join(
                (transport.read_line(max(0.001, deadline - monotonic())) + "\n").encode("ascii")
                for _ in range(5)
            )
            device = parse_identity(ByteParser(identity))
            config.validate_for(device)
            transport.write(encode_capture_request(config, device), timeout)
            in_flight = True
            while True:
                if cancelled.is_set():
                    CaptureRecovery(
                        transport, lambda: self.identify(port, min(timeout, 2.0))
                    ).timeout_or_cancel(timeout, drain_limit=4096)
                    recovered = True
                    raise CaptureCancelled("capture cancelled")
                remaining = deadline - monotonic()
                if remaining <= 0:
                    CaptureRecovery(
                        transport, lambda: self.identify(port, min(timeout, 2.0))
                    ).timeout_or_cancel(timeout, drain_limit=4096)
                    recovered = True
                    raise TimeoutError("capture timed out")
                try:
                    status = transport.read_line(min(0.1, remaining))
                    break
                except TimeoutError:
                    continue
            count_bytes = transport.read_exact(4, max(0.001, deadline - monotonic()))
            count = int.from_bytes(count_bytes, "little")
            payload_size = count * config.bytes_per_word
            if count != config.requested_count or payload_size > device.buffer_size:
                raise ProtocolError("invalid capture count")
            count_and_payload = count_bytes + transport.read_exact(
                payload_size + 1, max(0.001, deadline - monotonic())
            )
            samples, _ = parse_capture_response(
                ByteParser((status + "\n").encode("ascii") + count_and_payload), config, device
            )
            return CaptureResult(
                config=config,
                samples=samples,
                device=device,
                channel_mapping=tuple(f"GPIO{channel + 2}" for channel in config.channel_ids),
            )
        except TimeoutError:
            if in_flight and not recovered:
                CaptureRecovery(
                    transport, lambda: self.identify(port, min(timeout, 2.0))
                ).timeout_or_cancel(timeout, drain_limit=4096)
                recovered = True
            raise
        finally:
            if not recovered or not in_flight:
                transport.close()

    def recovery_capture(
        self,
        port: str,
        idle_config: CaptureConfig,
        signal_config: CaptureConfig,
        cancel_after: float,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        *,
        sleeper: Callable[[float], None] = sleep,
    ) -> CaptureResult:
        """Internally cancel one in-flight idle capture, then re-identify and recapture.

        This is deliberately only the hardware-smoke orchestration primitive, not
        a general public abort facility.
        """
        if (
            type(cancel_after) not in (int, float)
            or type(timeout) not in (int, float)
            or not isfinite(cancel_after)
            or not isfinite(timeout)
            or cancel_after <= 0
            or timeout <= 0
            or cancel_after >= timeout
        ):
            raise ValueError("cancel-after must be finite, positive, and less than timeout")
        transport = self._transport_factory(port, timeout)
        in_flight = False
        recovered = False
        try:
            transport.open()
            transport.write(encode_identity_request(), timeout)
            identity = b"".join(
                (transport.read_line(timeout) + "\n").encode("ascii") for _ in range(5)
            )
            device = parse_identity(ByteParser(identity))
            idle_config.validate_for(device)
            transport.write(encode_capture_request(idle_config, device), timeout)
            in_flight = True
            try:
                sleeper(cancel_after)
            except (KeyboardInterrupt, TimeoutError):
                CaptureRecovery(transport, lambda: self.identify(port, timeout)).timeout_or_cancel(
                    timeout, drain_limit=4096
                )
                recovered = True
                raise
            CaptureRecovery(transport, lambda: self.identify(port, timeout)).timeout_or_cancel(
                timeout, drain_limit=4096
            )
            recovered = True
            return self.capture(port, signal_config, timeout)
        finally:
            # Recovery owns its close on the in-flight path; ordinary setup
            # failures still close immediately and never send cancellation.
            if not recovered or not in_flight:
                transport.close()
