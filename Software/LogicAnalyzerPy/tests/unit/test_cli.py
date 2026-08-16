from __future__ import annotations

import pytest

from pico_logic_analyzer.cli.main import main


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
