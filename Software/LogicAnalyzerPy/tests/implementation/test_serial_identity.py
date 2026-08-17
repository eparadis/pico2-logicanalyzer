from __future__ import annotations

from dataclasses import dataclass

import pytest

from pico_logic_analyzer.driver.device import V2DeviceService, list_candidates
from pico_logic_analyzer.transport.serial import SerialTransport, SerialTransportError


class _FakeSerial:
    def __init__(self, **kwargs: object) -> None:
        self.kwargs = kwargs
        self.port: str | None = None
        self.dtr = False
        self.rts = False
        self.is_open = False
        self.in_waiting = 0
        self.writes: list[bytes] = []
        self.reads: list[bytes] = []
        self.timeout: float | None = None
        self.write_timeout: float | None = None
        self.closed = False

    def open(self) -> None:
        self.is_open = True

    def read(self, size: int) -> bytes:
        if not self.reads:
            return b""
        chunk = self.reads.pop(0)
        return chunk[:size]

    def write(self, data: bytes) -> int:
        self.writes.append(data)
        return len(data)

    def flush(self) -> None:
        pass

    def close(self) -> None:
        self.closed = True
        self.is_open = False


def test_serial_configures_before_open_stabilizes_and_closes() -> None:
    made: list[_FakeSerial] = []

    def factory(**kwargs: object) -> _FakeSerial:
        made.append(_FakeSerial(**kwargs))
        return made[-1]

    transport = SerialTransport("/dev/fake", 1, serial_factory=factory, sleeper=lambda _: None)
    transport.open()
    connection = made[0]
    assert connection.kwargs == {
        "port": None,
        "baudrate": 115200,
        "bytesize": 8,
        "parity": "N",
        "stopbits": 1,
        "timeout": 1,
        "write_timeout": 1,
        "xonxoff": False,
        "rtscts": False,
        "dsrdtr": False,
    }
    assert connection.port == "/dev/fake" and connection.dtr and connection.rts
    transport.close()
    assert connection.closed


def test_serial_line_rejects_unterminated_limit() -> None:
    connection = _FakeSerial()
    connection.reads = [b"a"] * 128
    transport = SerialTransport(
        "fake", 1, serial_factory=lambda **_: connection, sleeper=lambda _: None
    )
    transport.open()
    with pytest.raises(SerialTransportError):
        transport.read_line(10)
    assert not connection.closed


@dataclass
class _Port:
    device: str
    vid: int | None
    pid: int | None
    serial_number: str | None = None
    location: str | None = None
    description: str | None = None


def test_candidate_listing_filters_vid_pid_and_retains_absent_optional_metadata() -> None:
    candidates = list_candidates(
        lambda: [
            _Port("/dev/cu.usbmodem1", 0x1209, 0x3020),
            _Port("/dev/ttyACM0", 0x1209, 0x3020, "abc", None, "Pico"),
            _Port("/dev/other", None, None),
        ]
    )
    assert [candidate.device for candidate in candidates] == ["/dev/cu.usbmodem1", "/dev/ttyACM0"]
    assert candidates[0].json_object()["location"] is None


class _ScriptedTransport:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.closed = False
        self.writes: list[bytes] = []

    def open(self) -> None:
        pass

    def write(self, data: bytes, timeout: float) -> None:
        self.writes.append(data)

    def read_line(self, timeout: float) -> str:
        return self.lines.pop(0)

    def close(self) -> None:
        self.closed = True


def test_identity_service_closes_for_each_explicit_reopen_identity() -> None:
    transports: list[_ScriptedTransport] = []

    def factory(port: str, timeout: float) -> _ScriptedTransport:
        transport = _ScriptedTransport(
            ["LOGIC_ANALYZER_TEST_V6_0", "FREQ:1", "BLASTFREQ:2", "BUFFER:3", "CHANNELS:8"]
        )
        transports.append(transport)
        return transport

    first, second = V2DeviceService(factory).identify_after_reopen("/dev/fake", 1)
    assert first == second
    assert len(transports) == 2 and all(item.closed for item in transports)
    assert all(item.writes == [bytes.fromhex("55 aa 00 aa 55")] for item in transports)
