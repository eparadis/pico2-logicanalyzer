"""Explicit-port V2 identity and normal-capture services."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import asdict, dataclass
from importlib import import_module
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
        """Perform one bounded normal D0--D7 capture on the explicit port."""
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
            if count != config.requested_count or count > device.buffer_size:
                raise ProtocolError("invalid capture count")
            # Count was checked before this allocation-free, negotiated-bounded read.
            count_and_payload = count_bytes + transport.read_exact(count + 1, timeout)
            samples, _ = parse_capture_response(
                ByteParser((status + "\n").encode("ascii") + count_and_payload), config, device
            )
            return CaptureResult(
                config=config,
                samples=samples,
                device=device,
                channel_mapping=tuple(f"GPIO{index}" for index in range(2, 10)),
            )
        except (ConnectionError, TimeoutError, ProtocolError, ValueError):
            raise
        except Exception as exc:
            raise ConnectionError(f"capture failed on {port}: {exc}") from exc
        finally:
            transport.close()
