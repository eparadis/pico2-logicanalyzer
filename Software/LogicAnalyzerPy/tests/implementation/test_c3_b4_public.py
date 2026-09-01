"""Focused implementation checks for the Cycle 3 public decode surface."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tomllib
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
SNAPSHOT = (
    ROOT
    / "src/pico_logic_analyzer/_decoder_snapshots"
    / "407b5ef039aa0474c400c0721749baa126e53270"
)


def _capture():
    from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

    config = CaptureConfig(1_000_000, 0, 4, 0, "rising", (0, 1))
    return CaptureResult(
        config,
        np.asarray([0, 1, 1, 0], dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_B4_TEST_V6_0", 1_000_000, 1_000_000, 4, 8),
        ("D0", "D1"),
        ("D0", "D1"),
    )


def test_public_exports_are_stable_and_models_are_immutable() -> None:
    from pico_logic_analyzer.decode import (
        AnnotationRecord,
        BinaryRecord,
        DecodeCaptureIdentity,
        DecodeDeclarations,
        DecodeResult,
        DecoderIdentity,
        MetadataRecord,
        PythonRecord,
        decode_capture,
    )

    assert callable(decode_capture)
    assert all(
        item.__dataclass_params__.frozen
        for item in (
            DecodeResult,
            DecoderIdentity,
            DecodeCaptureIdentity,
            DecodeDeclarations,
            AnnotationRecord,
            PythonRecord,
            BinaryRecord,
            MetadataRecord,
        )
    )


def test_record_values_are_immutable_without_unlisted_payload_models() -> None:
    import dataclasses
    import typing

    import pico_logic_analyzer.decode as public

    for record_name in ("AnnotationRecord", "BinaryRecord", "MetadataRecord"):
        value_type = typing.get_type_hints(getattr(public, record_name))["value"]
        assert not (isinstance(value_type, type) and dataclasses.is_dataclass(value_type))


def test_public_call_delegates_once_and_rejects_limit_weakening(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import HARD_LIMITS

    calls: list[object] = []

    def fake(request: object, *, limits: object = None) -> object:
        calls.append((request, limits))
        raise RuntimeError("delegated")

    monkeypatch.setattr(public, "_decode_private", fake)
    with pytest.raises(RuntimeError, match="delegated"):
        public.decode_capture(_capture(), "uart", {"rx": 0}, {})
    assert len(calls) == 1
    with pytest.raises(ValueError, match="limits"):
        public.decode_capture(
            _capture(),
            "uart",
            {"rx": 0},
            {},
            {"input_samples": HARD_LIMITS["input_samples"] + 1},
        )
    assert len(calls) == 1


def test_every_approved_limit_rejects_weakening_before_delegation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import HARD_LIMITS

    monkeypatch.setattr(
        public,
        "_decode_private",
        lambda *_args, **_kwargs: pytest.fail("worker launched"),
    )
    for key, ceiling in HARD_LIMITS.items():
        with pytest.raises(ValueError, match="tighten"):
            public.decode_capture(
                _capture(), "uart", {"rx": 0}, {}, {key: ceiling + 1}
            )


def test_tightened_spi_and_diagnostic_limits_reject_before_delegation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public

    monkeypatch.setattr(
        public,
        "_decode_private",
        lambda *_args, **_kwargs: pytest.fail("worker launched"),
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
        public.decode_capture(
            _capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 1}
        )


def test_b1_literal_object_vectors_and_cli_bytes_match_public_models() -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import decode_result_from_dict

    vectors = json.loads(
        (ROOT / "testdata/decoders/cycle3/typed-vectors.json").read_text(encoding="utf-8")
    )
    goldens = {
        item["vector_id"]: bytes.fromhex(item["hex"])
        for item in vectors["cli_utf8_goldens"]
    }
    assert len(vectors["vectors"]) == len(goldens) == 12
    for vector in vectors["vectors"]:
        private = decode_result_from_dict(vector["object"])
        result = public._public_result(private)
        assert public.canonical_json(result) == goldens[vector["id"]]
        if vector["kind"] != "python":
            assert not hasattr(result.records[0].value, "__setitem__")


def test_tightened_diagnostic_limit_bounds_a_host_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import HostFailure

    monkeypatch.setattr(
        public,
        "_decode_private",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(HostFailure("timeout")),
    )
    with pytest.raises(public.DecodeError) as raised:
        public.decode_capture(
            _capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 28}
        )
    assert len(raised.value.message.encode()) <= 28


def test_package_snapshot_is_exact_and_closed() -> None:
    expected = {
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
    actual = {
        str(path.relative_to(SNAPSHOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in SNAPSHOT.rglob("*")
        if path.is_file()
    }
    assert actual == expected
    for relative in expected:
        source = REPOSITORY / "Software/decoders" / relative
        assert (SNAPSHOT / relative).read_bytes() == source.read_bytes()


def test_package_metadata_and_license_resources_match_b1_disposition() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert project["build-system"]["requires"] == [
        "setuptools==77.0.3",
        "wheel==0.45.1",
    ]
    assert project["project"]["license"] == "GPL-3.0-only"
    assert project["project"]["license-files"] == [
        "LICENSE",
        "LICENSES/GPL-2.0-or-later.txt",
        "LICENSES/MIT.txt",
        "ATTRIBUTION.md",
    ]
    assert project["tool"]["setuptools"]["packages"]["find"]["exclude"] == [
        "pico_logic_analyzer._decoder_snapshots*"
    ]
    attribution = (ROOT / "ATTRIBUTION.md").read_text(encoding="utf-8")
    assert "project-history/rights confirmation required" in attribution
    assert "not\nlegal advice, a warranty, or a certification of rights" in attribution.lower()
    assert (ROOT / "LICENSE").read_bytes() == (REPOSITORY / "LICENSE").read_bytes()
    assert "Version 2, June 1991" in (
        ROOT / "LICENSES/GPL-2.0-or-later.txt"
    ).read_text(encoding="utf-8")
    assert "MIT License" in (ROOT / "LICENSES/MIT.txt").read_text(encoding="utf-8")


def _run_cli(cwd: Path, *arguments: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        [sys.executable, "-m", "pico_logic_analyzer", *arguments],
        cwd=cwd,
        capture_output=True,
        check=False,
    )


def test_installed_cli_replay_and_explicit_csv_are_byte_identical(tmp_path: Path) -> None:
    from pico_logic_analyzer.formats import csv_bytes, replay_bytes

    capture = _capture()
    replay = tmp_path / "capture.npz"
    csv = tmp_path / "capture.csv"
    replay.write_bytes(replay_bytes(capture))
    csv.write_bytes(csv_bytes(capture))
    common = ("--decoder", "uart", "--channel", "rx=0")
    replay_run = _run_cli(tmp_path, "decode", "--replay", str(replay), *common)
    csv_run = _run_cli(
        tmp_path,
        "decode",
        "--csv",
        str(csv),
        "--channels",
        "0,1",
        "--sample-rate",
        "1000000",
        "--trigger-channel",
        "0",
        "--edge",
        "rising",
        *common,
    )
    assert replay_run.returncode == csv_run.returncode == 0
    assert replay_run.stderr == csv_run.stderr == b""
    assert replay_run.stdout == csv_run.stdout
    assert replay_run.stdout.endswith(b"\n") and not replay_run.stdout.endswith(b"\n\n")
    assert json.loads(replay_run.stdout)["schema"] == "pico-logic-analyzer.decode-result/v1"


def test_installed_library_runs_from_outside_source_tree(tmp_path: Path) -> None:
    from pico_logic_analyzer.formats import replay_bytes

    replay = tmp_path / "capture.npz"
    replay.write_bytes(replay_bytes(_capture()))
    code = """
from pathlib import Path
from pico_logic_analyzer.decode import DecodeResult, canonical_json, decode_capture
from pico_logic_analyzer.formats.replay import import_replay_bytes
capture = import_replay_bytes(Path('capture.npz').read_bytes())
result = decode_capture(capture, 'uart', {'rx': 0}, {})
assert isinstance(result, DecodeResult)
assert result.json_bytes() == canonical_json(result)
print(result.schema)
"""
    run = subprocess.run(
        [sys.executable, "-c", code], cwd=tmp_path, capture_output=True, check=False
    )
    assert run.returncode == 0, run.stderr.decode()
    assert run.stdout == b"pico-logic-analyzer.decode-result/v1\n"
    assert run.stderr == b""


@pytest.mark.parametrize(
    ("arguments", "code", "diagnostic"),
    [
        (
            (
                "decode",
                "--replay",
                "missing.npz",
                "--channels",
                "0,1",
                "--decoder",
                "uart",
                "--channel",
                "rx=0",
            ),
            5,
            b"forbidden with replay",
        ),
        (
            ("decode", "--csv", "missing.csv", "--decoder", "uart", "--channel", "rx=0"),
            5,
            b"CSV requires",
        ),
    ],
)
def test_cli_input_failures_are_stderr_only(
    tmp_path: Path, arguments: tuple[str, ...], code: int, diagnostic: bytes
) -> None:
    run = _run_cli(tmp_path, *arguments)
    assert run.returncode == code
    assert run.stdout == b""
    assert diagnostic in run.stderr


def test_decode_cli_does_not_import_serial_or_web(tmp_path: Path) -> None:
    from pico_logic_analyzer.formats import replay_bytes

    replay = tmp_path / "capture.npz"
    replay.write_bytes(replay_bytes(_capture()))
    code = """
import builtins
import sys
original = builtins.__import__
def guarded(name, *args, **kwargs):
    if name.split('.', 1)[0] in {'serial', 'aiohttp'}:
        raise RuntimeError('forbidden optional import')
    return original(name, *args, **kwargs)
builtins.__import__ = guarded
from pico_logic_analyzer.cli.main import main
raise SystemExit(main(sys.argv[1:]))
"""
    run = subprocess.run(
        [
            sys.executable,
            "-c",
            code,
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
    assert run.returncode == 0, run.stderr.decode()
    assert run.stderr == b""


def test_cli_duplicate_unknown_and_invalid_assignments_are_usage_errors(
    tmp_path: Path,
) -> None:
    from pico_logic_analyzer.formats import replay_bytes

    replay = tmp_path / "capture.npz"
    replay.write_bytes(replay_bytes(_capture()))
    cases = (
        ("--channel", "rx=0", "--channel", "rx=1"),
        ("--channel", "rx=nope"),
        ("--channel", "rx=0", "--option", "unknown=value"),
        ("--channel", "rx=0", "--option", "baudrate=10", "--option", "baudrate=20"),
    )
    for extra in cases:
        run = _run_cli(
            tmp_path,
            "decode",
            "--replay",
            str(replay),
            "--decoder",
            "uart",
            *extra,
        )
        assert run.returncode == 2
        assert run.stdout == b""
        assert run.stderr.startswith(b"pico-la:")


@pytest.mark.parametrize("channels", ("", "0,x", "0,0", "0,24", "0"))
def test_invalid_csv_channel_metadata_is_input_exit_five(
    tmp_path: Path, channels: str
) -> None:
    from pico_logic_analyzer.formats import csv_bytes

    csv = tmp_path / "capture.csv"
    csv.write_bytes(csv_bytes(_capture()))
    run = _run_cli(
        tmp_path,
        "decode",
        "--csv",
        str(csv),
        "--channels",
        channels,
        "--sample-rate",
        "1000000",
        "--trigger-channel",
        "0",
        "--edge",
        "rising",
        "--decoder",
        "uart",
        "--channel",
        "rx=0",
    )
    assert run.returncode == 5
    assert run.stdout == b""
    assert len(run.stderr) <= 8192


def test_all_cli_diagnostics_are_bounded(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from pico_logic_analyzer.cli import main as cli

    hostile = "x" * 8193
    argparse_run = _run_cli(
        tmp_path,
        "decode",
        "--replay",
        "inert.npz",
        "--decoder",
        hostile,
        "--channel",
        "rx=0",
    )
    assert argparse_run.returncode == 2
    assert argparse_run.stdout == b""
    assert len(argparse_run.stderr) <= 8192

    monkeypatch.setattr(
        cli,
        "_decode",
        lambda _arguments: (_ for _ in ()).throw(ValueError(hostile)),
    )
    assert cli.main(
        [
            "decode",
            "--replay",
            "inert.npz",
            "--decoder",
            "uart",
            "--channel",
            "rx=0",
        ]
    ) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert len(captured.err.encode("utf-8")) <= 8192


def test_cli_legacy_d0_d7_rate_inference_is_the_only_omission(tmp_path: Path) -> None:
    from pico_logic_analyzer.formats import csv_bytes
    from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

    config = CaptureConfig(1_000_000, 1, 3, 0, "rising", tuple(range(8)))
    capture = CaptureResult(
        config,
        np.asarray([0, 1, 1, 0], dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_B4_LEGACY_V6_0", 1_000_000, 1_000_000, 4, 8),
    )
    legacy = tmp_path / "legacy.csv"
    legacy.write_bytes(csv_bytes(capture))
    run = _run_cli(
        tmp_path,
        "decode",
        "--csv",
        str(legacy),
        "--channels",
        "0,1,2,3,4,5,6,7",
        "--trigger-channel",
        "0",
        "--edge",
        "rising",
        "--decoder",
        "uart",
        "--channel",
        "rx=0",
    )
    assert run.returncode == 0, run.stderr.decode()
    nonlegacy = tmp_path / "nonlegacy.csv"
    nonlegacy.write_bytes(csv_bytes(_capture()))
    rejected = _run_cli(
        tmp_path,
        "decode",
        "--csv",
        str(nonlegacy),
        "--channels",
        "0,1",
        "--trigger-channel",
        "0",
        "--edge",
        "rising",
        "--decoder",
        "uart",
        "--channel",
        "rx=0",
    )
    assert rejected.returncode == 5
    assert rejected.stdout == b""


def test_cli_decoder_failure_is_exit_seven_and_stderr_only(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer.cli.main import main
    from pico_logic_analyzer.formats import replay_bytes

    replay = tmp_path / "capture.npz"
    replay.write_bytes(replay_bytes(_capture()))

    def fail(*_args: object, **_kwargs: object) -> object:
        raise public.DecodeError("timeout", "decoder failed: timeout")

    monkeypatch.setattr(public, "decode_capture", fail)
    code = main(
        [
            "decode",
            "--replay",
            str(replay),
            "--decoder",
            "uart",
            "--channel",
            "rx=0",
        ]
    )
    captured = capsys.readouterr()
    assert code == 7
    assert captured.out == ""
    assert captured.err == "pico-la: decoder failed: timeout\n"
