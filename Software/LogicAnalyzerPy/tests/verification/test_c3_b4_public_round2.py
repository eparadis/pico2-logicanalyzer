"""Independent C3-B4 checks for corrected candidate bd1bd07c2501c0c28ed6ae494c4fa298571e058f."""

from __future__ import annotations

import dataclasses
import hashlib
import json
import subprocess
import sys
import typing
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

CANDIDATE = "bd1bd07c2501c0c28ed6ae494c4fa298571e058f"
CANDIDATE_TREE = "bd544dee2b19a44ee256e44f2f6afc2371142afd"
ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
CLI = Path(sys.executable).with_name("pico-la")
DIAGNOSTIC_BYTES = 8192


def _capture() -> CaptureResult:
    return CaptureResult(
        CaptureConfig(1_000_000, 0, 4, 0, "rising", (0, 1)),
        np.asarray([0, 1, 1, 0], dtype=np.uint8),
        DeviceInfo("LOGIC_ANALYZER_B4_VERIFY_R2_V6_0", 1_000_000, 1_000_000, 4, 24),
        ("D0", "D1"),
        ("D0", "D1"),
    )


def _run_cli(cwd: Path, *arguments: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run([str(CLI), *arguments], cwd=cwd, capture_output=True, check=False)


def _time(public: object, value: dict[str, object]) -> object:
    rational = getattr(public, "RationalTime")
    record_time = getattr(public, "RecordTime")
    absolute = typing.cast(dict[str, int], value["absolute"])
    relative = typing.cast(dict[str, int], value["trigger_relative"])
    return record_time(
        rational(absolute["numerator"], absolute["denominator"]),
        rational(relative["numerator"], relative["denominator"]),
    )


def _python_value(public: object, value: dict[str, object]) -> object:
    tag = value["tag"]
    classes = {
        "null": "NullValue",
        "bool": "BoolValue",
        "integer": "IntegerValue",
        "float": "FloatValue",
        "string": "StringValue",
        "bytes": "BytesValue",
        "list": "ListValue",
        "tuple": "TupleValue",
        "spi-data": "SpiDataValue",
    }
    model = getattr(public, classes[typing.cast(str, tag)])
    if tag == "null":
        return model()
    if tag == "bytes":
        import base64

        return model(base64.b64decode(typing.cast(str, value["value"]), validate=True))
    if tag in {"list", "tuple"}:
        children = typing.cast(list[dict[str, object]], value["value"])
        return model(tuple(_python_value(public, child) for child in children))
    if tag == "spi-data":
        return model(value["ss"], value["es"], value["val"])
    return model(value["value"])


def _public_vector(public: object, raw: dict[str, object]) -> object:
    declarations_raw = typing.cast(dict[str, list[dict[str, object]]], raw["declarations"])
    declarations = getattr(public, "DecodeDeclarations")(
        tuple(
            getattr(public, "AnnotationDeclaration")(
                item["index"], item["id"], item["description"]
            )
            for item in declarations_raw["annotations"]
        ),
        tuple(
            getattr(public, "AnnotationRowDeclaration")(
                item["index"],
                item["id"],
                item["description"],
                tuple(typing.cast(list[int], item["annotation_indices"])),
            )
            for item in declarations_raw["annotation_rows"]
        ),
        tuple(
            getattr(public, "BinaryDeclaration")(
                item["index"], item["id"], item["description"]
            )
            for item in declarations_raw["binary"]
        ),
        tuple(
            getattr(public, "MetadataDeclaration")(
                item["output_id"], item["value_type"], item["name"], item["description"]
            )
            for item in declarations_raw["metadata"]
        ),
    )
    records = []
    for item in typing.cast(list[dict[str, object]], raw["records"]):
        common = (
            item["emission_index"],
            item["output_id"],
            item["start_sample"],
            item["end_sample"],
            _time(public, typing.cast(dict[str, object], item["start_time"])),
            _time(public, typing.cast(dict[str, object], item["end_time"])),
        )
        value = typing.cast(dict[str, object], item["value"])
        if item["kind"] == "python":
            records.append(getattr(public, "PythonRecord")(*common, _python_value(public, value)))
        else:
            if item["kind"] == "annotation":
                value = {**value, "texts": tuple(typing.cast(list[str], value["texts"]))}
            model = {
                "annotation": "AnnotationRecord",
                "binary": "BinaryRecord",
                "metadata": "MetadataRecord",
            }[typing.cast(str, item["kind"])]
            records.append(getattr(public, model)(*common, value))
    decoder = typing.cast(dict[str, object], raw["decoder"])
    capture = typing.cast(dict[str, int], raw["capture"])
    channels = typing.cast(list[dict[str, object]], raw["channels"])
    options = typing.cast(dict[str, object], raw["options"])
    return getattr(public, "DecodeResult")(
        getattr(public, "DecoderIdentity")(decoder["id"], decoder["file_set_sha256"]),
        raw["samplerate_hz"],
        tuple((item["decoder_channel"], item["physical_channel"]) for item in channels),
        tuple(sorted(options.items())),
        getattr(public, "DecodeCaptureIdentity")(
            capture["sample_count"], capture["trigger_index"]
        ),
        declarations,
        tuple(records),
    )


def test_candidate_binding_and_all_twelve_public_object_vectors() -> None:
    tree = subprocess.run(
        ["git", "show", "-s", "--format=%T", CANDIDATE],
        cwd=REPOSITORY,
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    assert tree == CANDIDATE_TREE
    vectors_path = ROOT / "testdata/decoders/cycle3/typed-vectors.json"
    assert hashlib.sha256(vectors_path.read_bytes()).hexdigest() == (
        "b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf"
    )
    vectors = json.loads(vectors_path.read_text(encoding="utf-8"))
    goldens = {
        item["vector_id"]: bytes.fromhex(item["hex"])
        for item in vectors["cli_utf8_goldens"]
    }
    import pico_logic_analyzer.decode as public

    for vector in vectors["vectors"]:
        actual = public.canonical_json(_public_vector(public, vector["object"]))
        assert actual == goldens[vector["id"]]


def test_v001_exact_class_set_and_record_values_are_deeply_immutable() -> None:
    import pico_logic_analyzer.decode as public

    source: dict[str, object] = {"class_index": 0, "texts": ("A",)}
    record = public.AnnotationRecord(
        0,
        0,
        0,
        1,
        public.RecordTime(public.RationalTime(0, 1), public.RationalTime(0, 1)),
        public.RecordTime(public.RationalTime(1, 1), public.RationalTime(1, 1)),
        source,
    )
    source["class_index"] = 9
    assert record.value["class_index"] == 0
    assert not hasattr(record.value, "__setitem__")
    for name in ("AnnotationRecord", "BinaryRecord", "MetadataRecord"):
        annotation = typing.get_type_hints(getattr(public, name))["value"]
        assert not (isinstance(annotation, type) and dataclasses.is_dataclass(annotation))
    with pytest.raises(ValueError):
        public.BinaryRecord(
            0,
            0,
            0,
            1,
            record.start_time,
            record.end_time,
            {"class_index": 0, "data_base64": "YQ"},
        )


def test_v002_spi_tightening_rejects_before_both_public_and_private_launch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode import host
    from pico_logic_analyzer._decode.model import DecodeRequest, RequestFailure

    monkeypatch.setattr(
        public, "_decode_private", lambda *_args, **_kwargs: pytest.fail("public delegated")
    )
    with pytest.raises(ValueError):
        public.decode_capture(
            _capture(),
            "spi",
            {"clk": 0, "mosi": 1},
            {"wordsize": 8},
            {"spi_max_word_size_bits": 4},
        )

    request = DecodeRequest(
        "spi", 1_000_000, (0, 1), {"clk": 0, "mosi": 1}, (0, 1, 1, 0), 0, {"wordsize": 8}
    )
    monkeypatch.setattr(host, "verify_decoder", lambda *_args: pytest.fail("identity read"))
    with pytest.raises(RequestFailure):
        host._decode_with_factory(
            request,
            lambda *_args, **_kwargs: pytest.fail("worker launched"),
            limits={**host.HARD_LIMITS, "spi_max_word_size_bits": 4},
        )


def test_v002_every_stable_failure_obeys_tightened_diagnostic_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer.decode as public
    from pico_logic_analyzer._decode.model import FAILURE_CODES, HostFailure

    with pytest.raises(ValueError):
        public.decode_capture(_capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 27})
    for code in FAILURE_CODES:
        monkeypatch.setattr(
            public,
            "_decode_private",
            lambda *_args, selected=code, **_kwargs: (_ for _ in ()).throw(
                HostFailure(selected)
            ),
        )
        with pytest.raises(public.DecodeError) as raised:
            public.decode_capture(
                _capture(), "uart", {"rx": 0}, {}, {"diagnostic_bytes": 28}
            )
        assert len(raised.value.message.encode("utf-8")) <= 28


@pytest.mark.parametrize("channels", ("", "0,x", "0,0", "0,24", "0"))
def test_v003_invalid_channel_metadata_is_exit_five(tmp_path: Path, channels: str) -> None:
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


@pytest.mark.parametrize(
    ("flag", "value"),
    (("--sample-rate", "invalid"), ("--trigger-channel", "invalid"), ("--edge", "sideways")),
)
def test_all_parser_invalid_csv_metadata_is_exit_five(
    tmp_path: Path, flag: str, value: str
) -> None:
    arguments = [
        "decode",
        "--csv",
        str(tmp_path / "inert.csv"),
        "--channels",
        "0,1",
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
    ]
    arguments[arguments.index(flag) + 1] = value
    run = _run_cli(tmp_path, *arguments)
    assert run.returncode == 5
    assert run.stdout == b""


def test_v004_aggregate_ascii_and_unicode_diagnostics_are_bounded(tmp_path: Path) -> None:
    for hostile in ("x" * 20_000, "\N{SNOWMAN}" * 20_000):
        run = _run_cli(
            tmp_path,
            "decode",
            "--replay",
            "inert.npz",
            "--decoder",
            hostile,
            "--channel",
            "rx=0",
        )
        assert run.returncode == 2
        assert run.stdout == b""
        assert 0 < len(run.stderr) <= DIAGNOSTIC_BYTES
        run.stderr.decode("utf-8")
