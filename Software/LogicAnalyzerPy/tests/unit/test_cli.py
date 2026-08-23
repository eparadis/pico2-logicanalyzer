from __future__ import annotations

import sys

import pytest

from pico_logic_analyzer.cli import main as cli
from pico_logic_analyzer.cli.main import main
from pico_logic_analyzer.model import DeviceInfo, ProtocolError


def test_module_help_lists_capture_contract(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as raised:
        main(["--help"])
    assert raised.value.code == 0
    assert "capture" in capsys.readouterr().out


def test_capture_help_exposes_both_edges(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as raised:
        main(["capture", "--help"])
    assert raised.value.code == 0
    assert "{rising,falling}" in capsys.readouterr().out


def test_web_without_optional_extra_has_actionable_error(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setitem(sys.modules, "aiohttp", None)
    monkeypatch.delitem(sys.modules, "pico_logic_analyzer.web.server", raising=False)
    assert main(["web"]) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "pip install 'pico-logic-analyzer[web]'" in captured.err


def test_devices_json_is_stdout_only(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(cli, "list_candidates", lambda: [])
    assert cli.main(["devices", "--json"]) == 0
    captured = capsys.readouterr()
    assert captured.out == '{"devices":[]}\n' and captured.err == ""


def test_info_text_and_json_use_explicit_port(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    device = DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 1, 2, 3, 8)
    calls: list[tuple[str, float]] = []

    class Service:
        def identify(self, port: str, timeout: float) -> DeviceInfo:
            calls.append((port, timeout))
            return device

    monkeypatch.setattr(cli, "V2DeviceService", Service)
    assert cli.main(["info", "--port", "/dev/explicit", "--timeout", "2", "--json"]) == 0
    captured = capsys.readouterr()
    assert calls == [("/dev/explicit", 2.0)]
    assert captured.out == ('{"blast_frequency_hz":2,"buffer_size":3,"channel_count":8,'
                            '"identity":"LOGIC_ANALYZER_TEST_V6_0","max_frequency_hz":1}\n')
    assert captured.err == ""


def test_info_connection_error_is_stderr_exit_three(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    class Service:
        def identify(self, port: str, timeout: float) -> DeviceInfo:
            raise ConnectionError("permission denied")

    monkeypatch.setattr(cli, "V2DeviceService", Service)
    assert cli.main(["info", "--port", "/dev/explicit"]) == 3
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err == "pico-la: permission denied\n"


def test_info_protocol_error_is_stderr_exit_three(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    class Service:
        def identify(self, port: str, timeout: float) -> DeviceInfo:
            raise ProtocolError("malformed identity")

    monkeypatch.setattr(cli, "V2DeviceService", Service)
    assert cli.main(["info", "--port", "/dev/explicit"]) == 3
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err == "pico-la: malformed identity\n"
