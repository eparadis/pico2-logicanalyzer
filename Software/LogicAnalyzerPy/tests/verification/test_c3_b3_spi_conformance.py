"""Fresh hostile verification of the frozen C3-B3 SPI candidate."""

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
CORPUS = ROOT / "testdata" / "decoders" / "cycle3"
SEMANTIC_BYTES = (CORPUS / "semantic-fixtures.json").read_bytes()
MATRIX_BYTES = (CORPUS / "option-matrix.json").read_bytes()
SEMANTIC = json.loads(SEMANTIC_BYTES)
MATRIX = json.loads(MATRIX_BYTES)
PROVENANCE = json.loads((CORPUS / "provenance.json").read_text(encoding="utf-8"))
TIMELINES = tuple(row for row in SEMANTIC["timelines"] if row["decoder"] == "spi")
BY_ID = {row["id"]: row for row in TIMELINES}
DIRECT = tuple(
    row for row in MATRIX["rows"]
    if row["decoder"] == "spi" and row["disposition"] == "direct-fixture"
)
UNSUPPORTED = tuple(
    row for row in MATRIX["rows"]
    if row["decoder"] == "spi" and row["disposition"] == "unsupported"
)


def _defaults() -> dict[str, object]:
    rows = tuple(
        row for row in MATRIX["rows"]
        if row["decoder"] == "spi" and row["classification"] == "default"
    )
    expected = {
        "cs_polarity": "active-low", "cpol": 0, "cpha": 0,
        "bitorder": "msb-first", "wordsize": 8,
    }
    assert len(rows) == 5
    assert {row["disposition"] for row in rows} == {"direct-fixture"}
    result = {row["option"]: row["value"] for row in rows}
    assert result == expected
    return result


def _samples(timeline: dict[str, object]) -> tuple[int, ...]:
    mapping = timeline["mapping"]
    transitions = timeline["transitions"]
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
        if row["decoder"] == "spi"
    )
    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    return {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "decoder": {"id": "spi", "file_set_sha256": file_set},
        "samplerate_hz": timeline["samplerate_hz"],
        "capture": {
            "sample_count": timeline["sample_count"],
            "trigger_index": timeline["trigger_index"],
        },
        "channels": [
            {"decoder_channel": channel, "physical_channel": physical}
            for channel, physical in mapping.items()
        ],
        "options": dict(sorted((_defaults() | timeline["options"]).items())),
        "declarations": timeline["declarations"],
        "records": timeline["expected_records"],
    }


def _observed(timeline: dict[str, object]) -> dict[str, object]:
    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    request = DecodeRequest(
        "spi", timeline["samplerate_hz"], tuple(mapping.values()), mapping,
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
    assert hashlib.sha256(
        (ROOT / "testdata/evidence/c3-b2.json").read_bytes()
    ).hexdigest() == "2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602"
    b1 = (ROOT / "testdata/evidence/c3-b1.json").read_text(encoding="utf-8")
    assert "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9" in b1
    assert hashlib.sha256(
        (ROOT / "tests/implementation/test_c3_b3_spi_conformance.py").read_bytes()
    ).hexdigest() == "e35c8d2ac472a7ae4c557daaba54521696971f871ef158d794c3d754cfdc0250"


@pytest.mark.parametrize("timeline", TIMELINES, ids=lambda row: row["id"])
def test_all_six_timelines_are_full_typed_exact_and_repeatable(
    timeline: dict[str, object],
) -> None:
    assert len(TIMELINES) == len(BY_ID) == 6
    expected = _expected(timeline)
    first, second = _observed(timeline), _observed(timeline)
    assert _matches(first, expected)
    assert first == second
    records = first["records"]
    assert isinstance(records, list)
    assert [row["emission_index"] for row in records] == list(range(len(records)))
    assert {row["kind"] for row in records} <= {
        "annotation", "binary", "metadata", "python",
    }


@pytest.mark.parametrize("row", DIRECT, ids=lambda row: row["id"])
def test_all_ten_direct_rows_resolve_to_exact_fixtures(row: dict[str, object]) -> None:
    assert len(DIRECT) == 10
    assert row["fixture"] in BY_ID
    timeline = BY_ID[row["fixture"]]
    assert _matches(_observed(timeline), _expected(timeline))


@pytest.mark.parametrize("row", UNSUPPORTED, ids=lambda row: row["id"])
def test_all_twenty_unsupported_rows_reject_before_spawn(
    monkeypatch: pytest.MonkeyPatch, row: dict[str, object],
) -> None:
    import pico_logic_analyzer._decode.host as host

    assert len(UNSUPPORTED) == 20
    monkeypatch.setattr(host, "_spawn_fixed_worker", lambda *_a, **_k: pytest.fail("spawned"))
    with pytest.raises(RequestFailure, match="^options rejected$"):
        DecodeRequest(
            "spi", 1, (11, 23), {"clk": 11, "mosi": 23}, (0,), 0,
            {row["option"]: row["value"]},
        )


def test_semantic_dimensions_and_record_families_are_closed() -> None:
    assert set(BY_ID) == {
        "spi-mosi-mode0-word8", "spi-miso-mode3-word8",
        "spi-cs-active-high-lsb-word1", "spi-incomplete-no-cs",
        "direct-spi-cs_polarity-activeneglow",
        "direct-spi-bitorder-msbnegfirst",
    }
    options = [row["options"] for row in TIMELINES]
    assert {row.get("cpol", 0) for row in options} == {0, 1}
    assert {row.get("cpha", 0) for row in options} == {0, 1}
    assert {row.get("bitorder", "msb-first") for row in options} == {
        "msb-first", "lsb-first",
    }
    assert {row.get("cs_polarity", "active-low") for row in options} == {
        "active-low", "active-high",
    }
    assert {row.get("wordsize", 8) for row in options} == {1, 8}
    incomplete = BY_ID["spi-incomplete-no-cs"]["expected_records"]
    assert len(incomplete) == 1
    assert incomplete[0]["value"]["value"] == [
        {"tag": "string", "value": "CS-CHANGE"},
        {"tag": "null"}, {"tag": "null"},
    ]
    kinds = {record["kind"] for row in TIMELINES for record in row["expected_records"]}
    assert kinds == {"annotation", "binary", "metadata", "python"}


def test_optional_pin_sentinels_has_channel_and_reordered_mapping() -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host

    pins = ("clk", "miso", "mosi", "cs")
    cases = (
        ({"clk": 11, "miso": 7}, (11, 7), (2,), (0, 1, 255, 255),
         (True, True, False, False)),
        ({"clk": 11, "mosi": 23}, (11, 23), (2,), (0, 255, 1, 255),
         (True, False, True, False)),
        ({"clk": 11, "miso": 7, "mosi": 23}, (11, 7, 23), (2,),
         (0, 1, 0, 255), (True, True, True, False)),
    )
    for mapping, channels, samples, vector, present in cases:
        host = ApiV3Host(pins, mapping, channels, samples, 1, 0, {})
        assert host.wait({}) == vector
        assert tuple(host.has_channel(index) for index in range(4)) == present
    reordered = ApiV3Host(
        pins, {"clk": 19, "miso": 7, "mosi": 12, "cs": 3},
        (12, 3, 19, 7), (1, 2), 2, 0, {},
    )
    assert (reordered.wait({}), reordered.wait({})) == (
        (0, 0, 1, 0), (0, 0, 0, 1),
    )


@pytest.mark.parametrize(
    "mutation",
    ["declaration", "record", "order", "python-tag", "spi-tag", "binary", "metadata"],
)
def test_hostile_result_mutations_are_detected(mutation: str) -> None:
    timeline = BY_ID["spi-mosi-mode0-word8"]
    observed = _observed(timeline)
    hostile = copy.deepcopy(_expected(timeline))
    records = hostile["records"]
    if mutation == "declaration":
        hostile["declarations"]["annotations"][0]["description"] += " hostile"
    elif mutation == "record":
        records[0]["end_sample"] += 1
    elif mutation == "order":
        records[0], records[1] = records[1], records[0]
    elif mutation == "python-tag":
        records[3]["value"]["value"][0]["value"] = "HOSTILE"
    elif mutation == "spi-tag":
        records[2]["value"]["value"][1]["value"][0]["tag"] = "hostile"
    elif mutation == "binary":
        records[1]["value"]["data_base64"] = "AA=="
    else:
        records[-1]["value"]["value"] += 1
    assert not _matches(observed, hostile)
    assert canonical_json(observed) != canonical_json(hostile)


@pytest.mark.parametrize("mutation", ["mapping", "option", "default", "boundary"])
def test_hostile_request_and_oracle_mutations_are_detected(mutation: str) -> None:
    timeline = BY_ID["spi-mosi-mode0-word8"]
    observed = _observed(timeline)
    hostile = copy.deepcopy(_expected(timeline))
    if mutation == "mapping":
        hostile["channels"][1]["physical_channel"] = 31
    elif mutation == "option":
        hostile["options"]["cpha"] = 1
    elif mutation == "default":
        hostile["options"]["wordsize"] = 7
    else:
        assert _defaults()["wordsize"] == 8
        with pytest.raises(RequestFailure, match="^options rejected$"):
            DecodeRequest("spi", 1, (1, 3), {"clk": 1, "mosi": 3}, (0,), 0,
                          {"wordsize": 9})
        return
    assert not _matches(observed, hostile)


def test_candidate_oracle_imports_are_closed_and_defaults_are_matrix_sourced() -> None:
    candidate = ROOT / "tests/implementation/test_c3_b3_spi_conformance.py"
    tree = ast.parse(candidate.read_text(encoding="utf-8"))
    functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
    assert "_matrix_spi_defaults" in functions
    roots = {
        alias.name.split(".")[0]
        for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        (node.module or "").split(".")[0]
        for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)
    }
    assert roots <= {
        "__future__", "ast", "hashlib", "json", "pathlib", "pytest",
        "pico_logic_analyzer",
    }
    assert _defaults() == {
        "cs_polarity": "active-low", "cpol": 0, "cpha": 0,
        "bitorder": "msb-first", "wordsize": 8,
    }


def test_snapshot_hashes_file_set_and_direct_import_roots_are_exact() -> None:
    files = {
        "Software/decoders/sigrokdecode.py": (
            "385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a"
        ),
        "Software/decoders/spi/__init__.py": (
            "91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c"
        ),
        "Software/decoders/spi/pd.py": (
            "ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d"
        ),
    }
    assert {path: hashlib.sha256((REPO / path).read_bytes()).hexdigest()
            for path in files} == files
    spi = next(row for row in PROVENANCE["decoder_file_sets"] if row["decoder"] == "spi")
    assert spi["sha256"] == "96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193"
    roots: dict[str, set[str]] = {}
    for path in files:
        tree = ast.parse((REPO / path).read_text(encoding="utf-8"))
        roots[path] = {
            alias.name.split(".")[0]
            for node in ast.walk(tree) if isinstance(node, ast.Import)
            for alias in node.names
        } | {
            (node.module or "").split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module is not None
        }
    assert roots == {
        "Software/decoders/sigrokdecode.py": set(),
        "Software/decoders/spi/__init__.py": {"pd"},
        "Software/decoders/spi/pd.py": {"collections", "sigrokdecode"},
    }
