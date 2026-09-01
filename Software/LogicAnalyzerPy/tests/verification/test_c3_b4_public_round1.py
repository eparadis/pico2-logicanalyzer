"""Independent C3-B4 checks for immutable candidate ce34d7972305aee1af0c7c0691b28adee3b13ca9."""

from __future__ import annotations

import dataclasses
import hashlib
import json
import subprocess
import sys
import tomllib
import typing
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

CANDIDATE = "ce34d7972305aee1af0c7c0691b28adee3b13ca9"
CANDIDATE_TREE = "4e6d493edcf9fbc6abe10f04c18834b9d4e0736b"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
SNAPSHOT_ROOT = (
    ROOT
    / "src/pico_logic_analyzer/_decoder_snapshots"
    / "407b5ef039aa0474c400c0721749baa126e53270"
)
CLI = Path(sys.executable).with_name("pico-la")
DIAGNOSTIC_LIMIT = 8192

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


def _capture(channel_ids: tuple[int, ...] = (0, 1)) -> CaptureResult:
    config = CaptureConfig(1_000_000, 0, 4, channel_ids[0], "rising", channel_ids)
    labels = tuple(f"D{channel}" for channel in channel_ids)
    return CaptureResult(
        config,
        np.asarray([0, 1, 1, 0], dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_B4_VERIFY_V6_0", 1_000_000, 1_000_000, 4, 24),
        labels,
        labels,
    )


def _run_cli(cwd: Path, *arguments: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run([str(CLI), *arguments], cwd=cwd, capture_output=True, check=False)


def test_exact_candidate_and_literal_vector_digests_are_bound() -> None:
    tree = subprocess.run(
        ["git", "show", "-s", "--format=%T", CANDIDATE],
        cwd=REPOSITORY,
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", CANDIDATE, "HEAD"],
        cwd=REPOSITORY,
        capture_output=True,
        check=False,
    )
    assert tree == CANDIDATE_TREE
    assert ancestry.returncode == 0
    vectors_path = ROOT / "testdata/decoders/cycle3/typed-vectors.json"
    assert hashlib.sha256(vectors_path.read_bytes()).hexdigest() == (
        "b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf"
    )
    vectors = json.loads(vectors_path.read_text(encoding="utf-8"))
    goldens = {
        item["vector_id"]: bytes.fromhex(item["hex"])
        for item in vectors["cli_utf8_goldens"]
    }
    assert len(vectors["vectors"]) == len(goldens) == 12
    for vector in vectors["vectors"]:
        independently_encoded = json.dumps(
            vector["object"],
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8") + b"\n"
        assert independently_encoded == goldens[vector["id"]]


def test_exact_public_models_are_frozen_slotted_and_do_not_leak_unlisted_payload_models() -> None:
    import pico_logic_analyzer.decode as public

    exact_named_models = {
        "DecodeResult",
        "DecoderIdentity",
        "DecodeCaptureIdentity",
        "DecodeDeclarations",
        "AnnotationDeclaration",
        "AnnotationRowDeclaration",
        "BinaryDeclaration",
        "MetadataDeclaration",
        "RationalTime",
        "RecordTime",
        "AnnotationRecord",
        "PythonRecord",
        "BinaryRecord",
        "MetadataRecord",
        "NullValue",
        "BoolValue",
        "IntegerValue",
        "FloatValue",
        "StringValue",
        "BytesValue",
        "ListValue",
        "TupleValue",
        "SpiDataValue",
    }
    for name in exact_named_models:
        model = getattr(public, name)
        assert dataclasses.is_dataclass(model)
        assert model.__dataclass_params__.frozen
        assert "__slots__" in vars(model)

    # The normative exact class set has no annotation/binary/metadata payload
    # models. A public record field therefore must not expose one in its type.
    for record_name in ("AnnotationRecord", "BinaryRecord", "MetadataRecord"):
        value_type = typing.get_type_hints(getattr(public, record_name))["value"]
        assert not (
            isinstance(value_type, type)
            and dataclasses.is_dataclass(value_type)
            and value_type.__name__ not in exact_named_models
        ), f"{record_name}.value leaks unlisted model {value_type.__name__}"


def test_packaged_snapshot_is_exact_closed_and_byte_identical() -> None:
    actual = {
        str(path.relative_to(SNAPSHOT_ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in SNAPSHOT_ROOT.rglob("*")
        if path.is_file()
    }
    assert actual == SNAPSHOT_DIGESTS
    for relative, digest in SNAPSHOT_DIGESTS.items():
        source = REPOSITORY / "Software/decoders" / relative
        assert hashlib.sha256(source.read_bytes()).hexdigest() == digest
        assert (SNAPSHOT_ROOT / relative).read_bytes() == source.read_bytes()


def test_pep639_metadata_matches_the_accepted_engineering_disposition() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    assert project["project"]["license"] == "GPL-3.0-only"
    assert project["project"]["license-files"] == [
        "LICENSE",
        "LICENSES/GPL-2.0-or-later.txt",
        "LICENSES/MIT.txt",
        "ATTRIBUTION.md",
    ]
    assert project["project"]["dependencies"] == ["numpy==2.2.2", "pyserial==3.5"]
    assert project["project"]["optional-dependencies"] == {"web": ["aiohttp==3.11.12"]}
    assert (ROOT / "LICENSE").read_bytes() == (REPOSITORY / "LICENSE").read_bytes()
    attribution = (ROOT / "ATTRIBUTION.md").read_text(encoding="utf-8")
    assert "project-history/rights confirmation required" in attribution
    assert "not legal advice" in " ".join(attribution.lower().split())


def test_external_installed_replay_and_csv_paths_are_byte_identical(tmp_path: Path) -> None:
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


def test_tightened_spi_word_size_is_enforced_before_host_delegation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public

    monkeypatch.setattr(
        public,
        "_decode_private",
        lambda *_args, **_kwargs: pytest.fail("host delegated despite tightened SPI maximum"),
    )
    with pytest.raises(ValueError):
        public.decode_capture(
            _capture(),
            "spi",
            {"clk": 0, "mosi": 1},
            {"wordsize": 8},
            {"spi_max_word_size_bits": 4},
        )


def test_tightened_diagnostic_limit_is_enforced_on_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import HostFailure

    def fail(*_args: object, **_kwargs: object) -> object:
        raise HostFailure("timeout")

    monkeypatch.setattr(public, "_decode_private", fail)
    try:
        public.decode_capture(_capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 1})
    except ValueError:
        return  # Rejecting an impossible tightening before launch is conforming.
    except public.DecodeError as error:
        assert len(error.message.encode("utf-8")) <= 1
    else:
        pytest.fail("host failure was returned as success")


def test_empty_csv_metadata_is_input_exit_five(tmp_path: Path) -> None:
    from pico_logic_analyzer.formats import csv_bytes

    csv = tmp_path / "capture.csv"
    csv.write_bytes(csv_bytes(_capture()))
    run = _run_cli(
        tmp_path,
        "decode",
        "--csv",
        str(csv),
        "--channels",
        "",
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


def test_usage_diagnostics_are_bounded_by_the_approved_ceiling(tmp_path: Path) -> None:
    hostile_decoder = "x" * (DIAGNOSTIC_LIMIT + 1)
    run = _run_cli(
        tmp_path,
        "decode",
        "--replay",
        "inert.npz",
        "--decoder",
        hostile_decoder,
        "--channel",
        "rx=0",
    )
    assert run.returncode == 2
    assert run.stdout == b""
    assert len(run.stderr) <= DIAGNOSTIC_LIMIT


def test_offline_decode_imports_neither_serial_nor_web(tmp_path: Path) -> None:
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
