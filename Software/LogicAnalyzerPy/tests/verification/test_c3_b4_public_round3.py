"""Independent C3-B4 checks for candidate e93b0d85bb57c014979c648373e48af845e7b01f."""

from __future__ import annotations

import dataclasses
import hashlib
import subprocess
import sys
import typing
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

CANDIDATE = "e93b0d85bb57c014979c648373e48af845e7b01f"
CANDIDATE_TREE = "fa428dd9a43bba52eb6dd7ce345fde883dc88af8"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
CLI = Path(sys.executable).with_name("pico-la")
DIAGNOSTIC_BYTES = 8192
SNAPSHOT_ROOT = (
    ROOT
    / "src/pico_logic_analyzer/_decoder_snapshots"
    / "407b5ef039aa0474c400c0721749baa126e53270"
)
SNAPSHOT_DIGESTS = {
    "sigrokdecode.py": "385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a",
    "uart/__init__.py": "351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f",
    "uart/pd.py": "67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc",
    "spi/__init__.py": "91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c",
    "spi/pd.py": "ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d",
    "i2c/__init__.py": "37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f",
    "i2c/pd.py": "b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305",
    "common/srdhelper/__init__.py": (
        "125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1"
    ),
    "common/srdhelper/mod.py": (
        "602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6"
    ),
}


def _capture() -> CaptureResult:
    return CaptureResult(
        CaptureConfig(1_000_000, 0, 4, 0, "rising", (0, 1)),
        np.asarray([0, 1, 1, 0], dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_B4_VERIFY_R3_V6_0", 1_000_000, 1_000_000, 4, 24),
        ("D0", "D1"),
        ("D0", "D1"),
    )


def _decode_arguments(mode: str, flag: str, value: str) -> list[str]:
    source = [f"--{mode}", "inert.csv" if mode == "csv" else "inert.npz"]
    metadata = ["--channels", "0,1"] if mode == "csv" else []
    return [
        "decode",
        *source,
        *metadata,
        flag,
        value,
        "--decoder",
        "uart",
        "--channel",
        "rx=0",
    ]


def test_candidate_binding_and_closed_snapshot_resources() -> None:
    tree = subprocess.run(
        ["git", "show", "-s", "--format=%T", CANDIDATE],
        cwd=REPOSITORY,
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    assert tree == CANDIDATE_TREE
    actual = {
        str(path.relative_to(SNAPSHOT_ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in SNAPSHOT_ROOT.rglob("*")
        if path.is_file()
    }
    assert actual == SNAPSHOT_DIGESTS


def test_v001_exact_record_value_surface_remains_closed_and_immutable() -> None:
    import pico_logic_analyzer.decode as public

    source: dict[str, object] = {"class_index": 0, "texts": ("A",)}
    time = public.RecordTime(public.RationalTime(0, 1), public.RationalTime(0, 1))
    record = public.AnnotationRecord(0, 0, 0, 0, time, time, source)
    source["class_index"] = 1
    assert record.value == {"class_index": 0, "texts": ("A",)}
    assert not hasattr(record.value, "__setitem__")
    for name in ("AnnotationRecord", "BinaryRecord", "MetadataRecord"):
        annotation = typing.get_type_hints(getattr(public, name))["value"]
        assert not (isinstance(annotation, type) and dataclasses.is_dataclass(annotation))


def test_v002_public_spi_and_diagnostic_tightening_remain_prelaunch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import HostFailure

    monkeypatch.setattr(
        public, "_decode_private", lambda *_args, **_kwargs: pytest.fail("SPI host launched")
    )
    with pytest.raises(ValueError):
        public.decode_capture(
            _capture(),
            "spi",
            {"clk": 0, "mosi": 1},
            {"wordsize": 8},
            {"spi_max_word_size_bits": 4},
        )
    with pytest.raises(ValueError):
        public.decode_capture(_capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 27})
    monkeypatch.setattr(
        public,
        "_decode_private",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(HostFailure("process-exit")),
    )
    with pytest.raises(public.DecodeError) as raised:
        public.decode_capture(_capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 28})
    assert len(raised.value.message.encode("utf-8")) <= 28


@pytest.mark.parametrize(
    ("flag", "value"),
    (("--sample-rate", "invalid"), ("--trigger-channel", "invalid"), ("--edge", "sideways")),
)
def test_v003_csv_malformed_metadata_is_exit_five_before_read_mapping_or_launch(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    flag: str,
    value: str,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer.cli import main as cli

    monkeypatch.setattr(cli, "_read_inert", lambda *_args: pytest.fail("capture read"))
    monkeypatch.setattr(cli, "_decode_channels", lambda *_args: pytest.fail("mapping parsed"))
    monkeypatch.setattr(public, "decode_capture", lambda *_args: pytest.fail("host launched"))
    assert cli.main(_decode_arguments("csv", flag, value)) == 5
    captured = capsys.readouterr()
    assert captured.out == ""
    assert 0 < len(captured.err.encode("utf-8")) <= DIAGNOSTIC_BYTES


@pytest.mark.parametrize(
    ("flag", "value"),
    (("--sample-rate", "invalid"), ("--trigger-channel", "invalid"), ("--edge", "sideways")),
)
def test_v003_replay_malformed_metadata_is_exit_two_before_read_mapping_or_launch(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    flag: str,
    value: str,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer.cli import main as cli

    monkeypatch.setattr(cli, "_read_inert", lambda *_args: pytest.fail("capture read"))
    monkeypatch.setattr(cli, "_decode_channels", lambda *_args: pytest.fail("mapping parsed"))
    monkeypatch.setattr(public, "decode_capture", lambda *_args: pytest.fail("host launched"))
    assert cli.main(_decode_arguments("replay", flag, value)) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert 0 < len(captured.err.encode("utf-8")) <= DIAGNOSTIC_BYTES


@pytest.mark.parametrize(
    ("flag", "value"),
    (("--sample-rate", "1000000"), ("--trigger-channel", "0"), ("--edge", "rising")),
)
def test_v003_replay_valid_but_forbidden_metadata_is_exit_five_before_read(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    flag: str,
    value: str,
) -> None:
    from pico_logic_analyzer.cli import main as cli

    monkeypatch.setattr(cli, "_read_inert", lambda *_args: pytest.fail("capture read"))
    assert cli.main(_decode_arguments("replay", flag, value)) == 5
    captured = capsys.readouterr()
    assert captured.out == ""
    assert 0 < len(captured.err.encode("utf-8")) <= DIAGNOSTIC_BYTES


def test_v004_installed_argparse_diagnostics_remain_bounded_utf8(tmp_path: Path) -> None:
    for hostile in ("x" * 20_000, "\N{SNOWMAN}" * 20_000):
        run = subprocess.run(
            [
                str(CLI),
                "decode",
                "--replay",
                "inert.npz",
                "--decoder",
                hostile,
                "--channel",
                "rx=0",
            ],
            cwd=tmp_path,
            capture_output=True,
            check=False,
        )
        assert run.returncode == 2
        assert run.stdout == b""
        assert 0 < len(run.stderr) <= DIAGNOSTIC_BYTES
        run.stderr.decode("utf-8")


def test_offline_cli_does_not_import_optional_web_or_serial(tmp_path: Path) -> None:
    from pico_logic_analyzer.formats import replay_bytes

    replay = tmp_path / "capture.npz"
    replay.write_bytes(replay_bytes(_capture()))
    program = """
import builtins
import sys
original = builtins.__import__
def guarded(name, *args, **kwargs):
    if name.split('.', 1)[0] in {'serial', 'aiohttp'}:
        raise RuntimeError('optional dependency imported')
    return original(name, *args, **kwargs)
builtins.__import__ = guarded
from pico_logic_analyzer.cli.main import main
raise SystemExit(main(sys.argv[1:]))
"""
    run = subprocess.run(
        [
            sys.executable,
            "-c",
            program,
            "decode",
            "--replay",
            str(replay),
            "--decoder",
            "uart",
            "--channel",
            "rx=0",
        ],
        cwd=tmp_path,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stderr.decode("utf-8", errors="replace")
    assert run.stderr == b""
