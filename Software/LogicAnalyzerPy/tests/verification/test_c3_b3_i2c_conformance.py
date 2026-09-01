"""Fresh independent hostile verification of the frozen C3-B3 I2C candidate."""

from __future__ import annotations

import ast
import copy
import hashlib
import json
from pathlib import Path

import pytest

from pico_logic_analyzer._decode.host import decode_private
from pico_logic_analyzer._decode.model import DecodeRequest, RequestFailure, canonical_json

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
CORPUS = ROOT / "testdata/decoders/cycle3"
SEMANTIC_BYTES = (CORPUS / "semantic-fixtures.json").read_bytes()
MATRIX_BYTES = (CORPUS / "option-matrix.json").read_bytes()
SEMANTIC = json.loads(SEMANTIC_BYTES)
MATRIX = json.loads(MATRIX_BYTES)
PROVENANCE = json.loads((CORPUS / "provenance.json").read_text(encoding="utf-8"))
TIMELINES = tuple(row for row in SEMANTIC["timelines"] if row["decoder"] == "i2c")
BY_ID = {row["id"]: row for row in TIMELINES}
DIRECT = tuple(
    row for row in MATRIX["rows"]
    if row["decoder"] == "i2c" and row["disposition"] == "direct-fixture"
)
UNSUPPORTED = tuple(
    row for row in MATRIX["rows"]
    if row["decoder"] == "i2c" and row["disposition"] == "unsupported"
)


def _default() -> dict[str, object]:
    rows = tuple(
        row for row in MATRIX["rows"]
        if row["decoder"] == "i2c" and row["classification"] == "default"
    )
    assert len(rows) == 1
    assert rows[0] == next(row for row in DIRECT if row["id"] == "i2c-address_format-shifted")
    assert (rows[0]["option"], rows[0]["value"]) == ("address_format", "shifted")
    return {rows[0]["option"]: rows[0]["value"]}


def _samples(timeline: dict[str, object]) -> tuple[int, ...]:
    mapping, transitions = timeline["mapping"], timeline["transitions"]
    assert isinstance(mapping, dict) and isinstance(transitions, dict)
    events: dict[int, list[tuple[str, int]]] = {}
    for wire, changes in transitions.items():
        for sample, level in changes:
            events.setdefault(sample, []).append((wire, level))
    levels: dict[str, int] = {}
    packed: list[int] = []
    for sample in range(timeline["sample_count"]):
        levels.update(events.get(sample, ()))
        packed.append(sum(
            levels[f"D{physical}"] << bit
            for bit, physical in enumerate(mapping.values())
        ))
    return tuple(packed)


def _expected(timeline: dict[str, object]) -> dict[str, object]:
    file_set = next(
        row["sha256"] for row in PROVENANCE["decoder_file_sets"]
        if row["decoder"] == "i2c"
    )
    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    return {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "decoder": {"id": "i2c", "file_set_sha256": file_set},
        "samplerate_hz": timeline["samplerate_hz"],
        "capture": {
            "sample_count": timeline["sample_count"],
            "trigger_index": timeline["trigger_index"],
        },
        "channels": [
            {"decoder_channel": channel, "physical_channel": physical}
            for channel, physical in mapping.items()
        ],
        "options": dict(sorted((_default() | timeline["options"]).items())),
        "declarations": timeline["declarations"],
        "records": timeline["expected_records"],
    }


def _observed(timeline: dict[str, object]) -> dict[str, object]:
    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    request = DecodeRequest(
        "i2c", timeline["samplerate_hz"], tuple(mapping.values()), mapping,
        _samples(timeline), timeline["trigger_index"], timeline["options"],
    )
    return decode_private(request).to_dict()


def _matches(observed: dict[str, object], expected: dict[str, object]) -> bool:
    return observed == expected and canonical_json(observed) == canonical_json(expected)


def test_exact_candidate_and_accepted_artifact_identities() -> None:
    assert hashlib.sha256(SEMANTIC_BYTES).hexdigest() == (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    )
    assert hashlib.sha256(MATRIX_BYTES).hexdigest() == (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209"
    )
    assert hashlib.sha256((ROOT / "testdata/evidence/c3-b2.json").read_bytes()).hexdigest() == (
        "2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602"
    )
    b1 = (ROOT / "testdata/evidence/c3-b1.json").read_text(encoding="utf-8")
    assert "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9" in b1
    assert hashlib.sha256(
        (ROOT / "tests/implementation/test_c3_b3_i2c_conformance.py").read_bytes()
    ).hexdigest() == "20c04a6f1eeb77760fe16b522ccaf1b1def8b8ca5a3418b29b3af6471bd433c3"


@pytest.mark.parametrize("timeline", TIMELINES, ids=lambda row: row["id"])
def test_all_three_timelines_are_full_typed_exact_and_repeatable(
    timeline: dict[str, object],
) -> None:
    assert len(TIMELINES) == len(BY_ID) == 3
    expected = _expected(timeline)
    first, second = _observed(timeline), _observed(timeline)
    assert _matches(first, expected)
    assert first == second
    records = first["records"]
    assert isinstance(records, list)
    assert [record["emission_index"] for record in records] == list(range(len(records)))
    assert {record["kind"] for record in records} <= {
        "annotation", "binary", "metadata", "python",
    }


@pytest.mark.parametrize("row", DIRECT, ids=lambda row: row["id"])
def test_both_direct_rows_resolve_to_exact_accepted_fixtures(row: dict[str, object]) -> None:
    assert len(DIRECT) == 2
    assert row["fixture"] in BY_ID
    timeline = BY_ID[row["fixture"]]
    assert _matches(_observed(timeline), _expected(timeline))


@pytest.mark.parametrize("row", UNSUPPORTED, ids=lambda row: row["id"])
def test_all_six_unsupported_rows_reject_before_spawn(
    monkeypatch: pytest.MonkeyPatch, row: dict[str, object],
) -> None:
    import pico_logic_analyzer._decode.host as host

    assert len(UNSUPPORTED) == 6
    monkeypatch.setattr(host, "_spawn_fixed_worker", lambda *_a, **_k: pytest.fail("spawned"))
    with pytest.raises(RequestFailure, match="^options rejected$"):
        DecodeRequest(
            "i2c", 1, (19, 7), {"scl": 19, "sda": 7}, (0,), 0,
            {row["option"]: row["value"]},
        )


def test_semantic_dimensions_records_and_incomplete_boundary_are_closed() -> None:
    assert set(BY_ID) == {
        "i2c-shifted-start-address-ack-data-nack-stop",
        "i2c-unshifted-repeated-start", "i2c-incomplete-boundary",
    }
    all_records = [record for row in TIMELINES for record in row["expected_records"]]
    assert {record["kind"] for record in all_records} == {
        "annotation", "binary", "metadata", "python",
    }
    python_names = {
        record["value"]["value"][0]["value"]
        for record in all_records if record["kind"] == "python"
    }
    assert {
        "START", "START REPEAT", "STOP", "ACK", "NACK", "BITS",
        "ADDRESS WRITE", "DATA WRITE",
    } == python_names
    annotation_classes = {
        record["value"]["class_index"]
        for record in all_records if record["kind"] == "annotation"
    }
    assert annotation_classes == {0, 1, 2, 3, 4, 5, 7, 9}
    declarations = TIMELINES[0]["declarations"]
    assert {row["id"] for row in declarations["annotations"]} == {
        "start", "repeat-start", "stop", "ack", "nack", "bit",
        "address-read", "address-write", "data-read", "data-write", "warning",
    }
    assert {row["id"] for row in declarations["binary"]} == {
        "address-read", "address-write", "data-read", "data-write",
    }
    incomplete = BY_ID["i2c-incomplete-boundary"]["expected_records"]
    assert len(incomplete) == 2
    assert [record["kind"] for record in incomplete] == ["python", "annotation"]
    assert incomplete[0]["value"]["value"][0]["value"] == "START"


def test_noncontiguous_reordered_scl_sda_mapping_and_pin_order() -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host

    host = ApiV3Host(
        ("scl", "sda"), {"scl": 19, "sda": 7}, (7, 19), (1, 2), 2, 0, {},
    )
    assert (host.wait({}), host.wait({})) == ((0, 1), (1, 0))
    assert tuple(host.has_channel(index) for index in range(2)) == (True, True)


@pytest.mark.parametrize(
    "mutation",
    ["declaration", "coordinate", "order", "tag", "binary", "metadata", "format"],
)
def test_hostile_full_result_mutations_are_detected(mutation: str) -> None:
    timeline = BY_ID["i2c-shifted-start-address-ack-data-nack-stop"]
    observed = _observed(timeline)
    hostile = copy.deepcopy(_expected(timeline))
    records = hostile["records"]
    if mutation == "declaration":
        hostile["declarations"]["annotations"][0]["description"] += " hostile"
    elif mutation == "coordinate":
        records[0]["start_sample"] += 1
    elif mutation == "order":
        records[0], records[1] = records[1], records[0]
    elif mutation == "tag":
        records[0]["value"]["value"][0]["tag"] = "integer"
    elif mutation == "binary":
        next(row for row in records if row["kind"] == "binary")["value"]["data_base64"] = "AA=="
    elif mutation == "metadata":
        next(row for row in records if row["kind"] == "metadata")["value"]["value"] += 1
    else:
        hostile["options"]["address_format"] = "unshifted"
    assert not _matches(observed, hostile)


@pytest.mark.parametrize("mutation", ["mapping", "fixture", "default", "provenance"])
def test_hostile_binding_and_provenance_mutations_are_detected(mutation: str) -> None:
    timeline = BY_ID["i2c-shifted-start-address-ack-data-nack-stop"]
    observed = _observed(timeline)
    hostile = copy.deepcopy(_expected(timeline))
    if mutation == "mapping":
        hostile["channels"][0]["physical_channel"] = 31
    elif mutation == "fixture":
        hostile = _expected(BY_ID["i2c-unshifted-repeated-start"])
    elif mutation == "default":
        hostile["options"]["address_format"] = "wide"
    else:
        hostile["decoder"]["file_set_sha256"] = "0" * 64
    assert not _matches(observed, hostile)


def test_snapshot_hashes_file_set_and_candidate_import_roots_are_closed() -> None:
    files = {
        "Software/decoders/sigrokdecode.py": (
            "385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a"
        ),
        "Software/decoders/i2c/__init__.py": (
            "37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f"
        ),
        "Software/decoders/i2c/pd.py": (
            "b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305"
        ),
        "Software/decoders/common/srdhelper/__init__.py": (
            "125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1"
        ),
        "Software/decoders/common/srdhelper/mod.py": (
            "602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6"
        ),
    }
    assert {
        path: hashlib.sha256((REPO / path).read_bytes()).hexdigest() for path in files
    } == files
    i2c = next(row for row in PROVENANCE["decoder_file_sets"] if row["decoder"] == "i2c")
    assert i2c["sha256"] == "dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae"
    candidate = ROOT / "tests/implementation/test_c3_b3_i2c_conformance.py"
    tree = ast.parse(candidate.read_text(encoding="utf-8"))
    imports = {
        alias.name.split(".")[0]
        for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        (node.module or "").split(".")[0]
        for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)
    }
    assert imports <= {
        "__future__", "ast", "hashlib", "json", "pathlib", "pytest",
        "pico_logic_analyzer",
    }
