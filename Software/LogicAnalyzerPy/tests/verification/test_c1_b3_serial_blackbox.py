"""Independent C1-B3 fake-serial/device-service verification."""

from __future__ import annotations

import importlib
from collections import deque
from types import SimpleNamespace

import pytest

from pico_logic_analyzer.driver import V2DeviceService, list_candidates
from pico_logic_analyzer.model import ProtocolError
from pico_logic_analyzer.transport import (
    SerialTransport,
    SerialTransportError,
    TransportTimeout,
)

from .golden import IDENTITY_REQUEST, IDENTITY_RESPONSE

_CLI = importlib.import_module("pico_logic_analyzer.cli.main")


class _RecordingSerial:
    def __init__(
        self,
        events: list[object],
        responses: list[bytes],
        available_immediately: bool,
        **kwargs: object,
    ) -> None:
        self.events = events
        self.responses: deque[bytes] = deque(responses)
        self.events.append(("construct", kwargs))
        self.port: str | None = None
        self.is_open = False
        self.timeout: float | None = None
        self.write_timeout: float | None = None
        self._dtr = False
        self._rts = False
        self.writes: list[bytes] = []
        self._available = available_immediately

    @property
    def dtr(self) -> bool:
        return self._dtr

    @dtr.setter
    def dtr(self, value: bool) -> None:
        self.events.append(("dtr", value))
        self._dtr = value

    @property
    def rts(self) -> bool:
        return self._rts

    @rts.setter
    def rts(self, value: bool) -> None:
        self.events.append(("rts", value))
        self._rts = value

    @property
    def in_waiting(self) -> int:
        return len(self.responses[0]) if self._available and self.responses else 0

    def open(self) -> None:
        assert self.port == "/dev/fake-v2"
        self.events.append("open")
        self.is_open = True

    def close(self) -> None:
        self.events.append("close")
        self.is_open = False

    def read(self, size: int) -> bytes:
        self.events.append(("read", size))
        if not self.responses:
            return b""
        chunk = self.responses.popleft()
        if len(chunk) > size:
            self.responses.appendleft(chunk[size:])
            return chunk[:size]
        return chunk

    def write(self, data: bytes) -> int:
        self.events.append(("write", data))
        self.writes.append(data)
        self._available = True
        return len(data)

    def flush(self) -> None:
        self.events.append("flush")


def _factory(
    events: list[object], responses: list[bytes], available_immediately: bool = False
) -> tuple[object, list[_RecordingSerial]]:
    created: list[_RecordingSerial] = []

    def factory(**kwargs: object) -> _RecordingSerial:
        serial = _RecordingSerial(events, responses, available_immediately, **kwargs)
        created.append(serial)
        return serial

    return factory, created


def test_serial_configures_before_open_asserts_lines_then_stabilizes_and_drains() -> None:
    events: list[object] = []
    factory, created = _factory(events, [b"stale"], available_immediately=True)
    transport = SerialTransport(
        "/dev/fake-v2",
        timeout=1.5,
        serial_factory=factory,  # type: ignore[arg-type]
        sleeper=lambda seconds: events.append(("sleep", seconds)),
    )
    transport.open()
    settings = events[0][1]  # type: ignore[index]
    assert settings == {
        "port": None,
        "baudrate": 115200,
        "bytesize": 8,
        "parity": "N",
        "stopbits": 1,
        "timeout": 1.5,
        "write_timeout": 1.5,
        "xonxoff": False,
        "rtscts": False,
        "dsrdtr": False,
    }
    assert events[1:5] == [("dtr", True), ("rts", True), "open", ("sleep", 0.1)]
    assert any(event == ("read", 5) for event in events)
    assert created[0].port == "/dev/fake-v2"
    transport.close()
    transport.close()


def test_serial_identity_service_handles_one_byte_fragments_and_closes() -> None:
    fragments = [bytes((byte,)) for byte in IDENTITY_RESPONSE]
    events: list[object] = []
    factory, created = _factory(events, fragments)

    def transport_factory(port: str, timeout: float) -> SerialTransport:
        return SerialTransport(port, timeout, serial_factory=factory, sleeper=lambda _: None)  # type: ignore[arg-type]

    device = V2DeviceService(transport_factory).identify("/dev/fake-v2", timeout=10.0)
    assert device.identity == "LOGIC_ANALYZER_TEST_BOARD_V6_0"
    assert created[0].writes == [IDENTITY_REQUEST]
    assert created[0].is_open is False


@pytest.mark.parametrize(
    "responses,error_type",
    [
        ([b"LOGIC_ANALYZER_TEST_BOARD_V6_0\n"], TransportTimeout),
        (
            [
                b"NOT_AN_ANALYZER\n",
                b"FREQ:1\n",
                b"BLASTFREQ:1\n",
                b"BUFFER:1\n",
                b"CHANNELS:8\n",
            ],
            ProtocolError,
        ),
    ],
)
def test_identity_timeout_or_malformed_response_closes_port(
    responses: list[bytes], error_type: type[Exception]
) -> None:
    events: list[object] = []
    factory, created = _factory(events, responses)
    service = V2DeviceService(
        lambda port, timeout: SerialTransport(  # type: ignore[arg-type]
            port, timeout, serial_factory=factory, sleeper=lambda _: None
        )
    )
    with pytest.raises(error_type):
        service.identify("/dev/fake-v2", timeout=10.0)
    assert created[0].is_open is False


def test_two_identity_operations_close_then_reopen_the_same_explicit_port() -> None:
    responses = [bytes((byte,)) for byte in IDENTITY_RESPONSE] * 2
    events: list[object] = []
    factory, created = _factory(events, responses)
    service = V2DeviceService(
        lambda port, timeout: SerialTransport(  # type: ignore[arg-type]
            port, timeout, serial_factory=factory, sleeper=lambda _: None
        )
    )
    first, second = service.identify_after_reopen("/dev/fake-v2", timeout=10.0)
    assert first == second
    assert len(created) == 2
    assert all(serial.writes == [IDENTITY_REQUEST] and not serial.is_open for serial in created)


def test_candidate_listing_filters_vid_pid_sorts_and_preserves_absent_optional_metadata() -> None:
    records = [
        SimpleNamespace(
            device="/dev/cu.z",
            vid=0x1209,
            pid=0x3020,
            serial_number=None,
            location=None,
            description=None,
        ),
        SimpleNamespace(
            device="/dev/tty.usb-a",
            vid=0x1209,
            pid=0x3020,
            serial_number="S1",
            location="1-2",
            description="V2",
        ),
        SimpleNamespace(device="/dev/tty.other", vid=0x1209, pid=0x3021),
        SimpleNamespace(device="/dev/tty.unknown", vid=None, pid=None),
    ]
    candidates = list_candidates(lambda: records)
    assert [candidate.device for candidate in candidates] == ["/dev/cu.z", "/dev/tty.usb-a"]
    assert candidates[0].serial_number is None and candidates[0].location is None
    assert candidates[1].json_object()["serial_number"] == "S1"


def test_candidate_listing_never_opens_or_auto_selects() -> None:
    records = [SimpleNamespace(device="/dev/tty.only", vid=0x1209, pid=0x3020)]
    assert [candidate.device for candidate in list_candidates(lambda: records)] == ["/dev/tty.only"]


def test_info_cli_uses_only_the_explicit_port_and_keeps_json_on_stdout(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    opened: list[tuple[str, float]] = []

    class Service:
        def identify(self, port: str, timeout: float) -> object:
            opened.append((port, timeout))
            return SimpleNamespace(
                identity="LOGIC_ANALYZER_TEST_BOARD_V6_0",
                max_frequency_hz=100,
                blast_frequency_hz=100,
                buffer_size=128,
                channel_count=8,
            )

    monkeypatch.setattr(_CLI, "V2DeviceService", Service)
    assert _CLI.main(["info", "--port", "/dev/selected", "--json", "--timeout", "2"]) == 0
    captured = capsys.readouterr()
    assert opened == [("/dev/selected", 2.0)]
    assert captured.err == ""
    assert captured.out == (
        '{"blast_frequency_hz":100,"buffer_size":128,"channel_count":8,'
        '"identity":"LOGIC_ANALYZER_TEST_BOARD_V6_0","max_frequency_hz":100}\n'
    )


def test_devices_cli_json_does_not_open_or_auto_select(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    candidates = list_candidates(
        lambda: [SimpleNamespace(device="/dev/only", vid=0x1209, pid=0x3020)]
    )
    monkeypatch.setattr(_CLI, "list_candidates", lambda: candidates)
    assert _CLI.main(["devices", "--json"]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == (
        '{"devices":[{"description":null,"device":"/dev/only","location":null,'
        '"pid":12320,"serial_number":null,"vid":4617}]}\n'
    )


def test_devices_cli_text_and_info_connection_error_keep_streams_and_exit_codes(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    candidates = list_candidates(
        lambda: [
            SimpleNamespace(
                device="/dev/only",
                vid=0x1209,
                pid=0x3020,
                serial_number="S1",
                location="1-2",
                description=None,
            )
        ]
    )
    monkeypatch.setattr(_CLI, "list_candidates", lambda: candidates)
    assert _CLI.main(["devices"]) == 0
    captured = capsys.readouterr()
    assert captured.out == "/dev/only VID=1209 PID=3020 serial=S1 location=1-2\n"
    assert captured.err == ""

    class FailingService:
        def identify(self, port: str, timeout: float) -> object:
            raise ConnectionError(f"denied {port}")

    monkeypatch.setattr(_CLI, "V2DeviceService", FailingService)
    assert _CLI.main(["info", "--port", "/dev/denied"]) == 3
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "pico-la: denied /dev/denied\n"


def test_info_cli_treats_malformed_identity_as_connection_protocol_failure(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    class MalformedService:
        def identify(self, port: str, timeout: float) -> object:
            raise ProtocolError("malformed identity")

    monkeypatch.setattr(_CLI, "V2DeviceService", MalformedService)
    assert _CLI.main(["info", "--port", "/dev/malformed"]) == 3
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "pico-la: malformed identity\n"


def test_cli_never_auto_selects_an_info_port(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as raised:
        _CLI.main(["info"])
    assert raised.value.code == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err


def test_cli_rejects_future_capture_command_without_opening_a_port(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert _CLI.main(
        [
            "capture",
            "--port",
            "/dev/not-opened",
            "--sample-rate",
            "1",
            "--trigger-channel",
            "0",
            "--edge",
            "rising",
            "--pre-samples",
            "0",
            "--post-samples",
            "1",
            "--csv",
            "out.csv",
            "--replay",
            "capture.npz",
        ]
    ) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "not implemented" in captured.err


@pytest.mark.parametrize("failure", [PermissionError("denied"), OSError("unplugged")])
def test_open_permission_or_unplug_failure_is_connection_error_and_needs_no_hardware(
    failure: Exception,
) -> None:
    def factory(**kwargs: object) -> object:
        raise failure

    transport = SerialTransport("/dev/fake-v2", serial_factory=factory)  # type: ignore[arg-type]
    with pytest.raises(SerialTransportError):
        transport.open()
    assert transport.is_open is False
