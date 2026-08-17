"""Explicit-port V2 identity service; capture remains a later batch."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import asdict, dataclass
from importlib import import_module
from typing import Any

from pico_logic_analyzer.model import DeviceInfo, ProtocolError
from pico_logic_analyzer.protocol import ByteParser, encode_identity_request, parse_identity
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
