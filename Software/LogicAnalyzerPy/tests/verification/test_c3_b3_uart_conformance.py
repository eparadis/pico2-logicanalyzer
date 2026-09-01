"""Independent hostile verification of the exact C3-B3 UART candidate."""

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
PROVENANCE = json.loads((CORPUS / "provenance.json").read_text(encoding="utf-8"))
SEMANTIC = json.loads(SEMANTIC_BYTES)
MATRIX = json.loads(MATRIX_BYTES)
TIMELINES = tuple(row for row in SEMANTIC["timelines"] if row["decoder"] == "uart")
BY_ID = {row["id"]: row for row in TIMELINES}
DIRECT = tuple(
    row for row in MATRIX["rows"]
    if row["decoder"] == "uart" and row["disposition"] == "direct-fixture"
)
UNSUPPORTED = tuple(
    row for row in MATRIX["rows"]
    if row["decoder"] == "uart" and row["disposition"] == "unsupported"
)


def _accepted_defaults() -> dict[str, object]:
    rows = [
        row for row in MATRIX["rows"]
        if row["decoder"] == "uart" and row["classification"] == "default"
    ]
    keys = {
        "baudrate", "data_bits", "parity", "stop_bits", "bit_order", "format",
        "invert_rx", "invert_tx", "sample_point", "rx_packet_delim",
        "tx_packet_delim", "rx_packet_len", "tx_packet_len",
    }
    assert len(rows) == len(keys) == 13
    assert {row["option"] for row in rows} == keys
    assert {row["disposition"] for row in rows} == {"direct-fixture"}
    return {row["option"]: row["value"] for row in rows}


def _packed_samples(timeline: dict[str, object]) -> tuple[int, ...]:
    mapping = timeline["mapping"]
    transitions = timeline["transitions"]
    assert isinstance(mapping, dict) and isinstance(transitions, dict)
    events: dict[int, list[tuple[str, int]]] = {}
    for wire, changes in transitions.items():
        for sample, level in changes:
            events.setdefault(sample, []).append((wire, level))
    levels: dict[str, int] = {}
    result: list[int] = []
    for sample in range(timeline["sample_count"]):
        levels.update(events.get(sample, ()))
        result.append(sum(
            levels[f"D{physical}"] << bit
            for bit, physical in enumerate(mapping.values())
        ))
    return tuple(result)


def _expected(timeline: dict[str, object]) -> dict[str, object]:
    file_set = next(
        row["sha256"] for row in PROVENANCE["decoder_file_sets"]
        if row["decoder"] == "uart"
    )
    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    return {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "decoder": {"id": "uart", "file_set_sha256": file_set},
        "samplerate_hz": timeline["samplerate_hz"],
        "channels": [
            {"decoder_channel": decoder, "physical_channel": physical}
            for decoder, physical in mapping.items()
        ],
        "options": dict(sorted((_accepted_defaults() | timeline["options"]).items())),
        "capture": {
            "sample_count": timeline["sample_count"],
            "trigger_index": timeline["trigger_index"],
        },
        "declarations": timeline["declarations"],
        "records": timeline["expected_records"],
    }


def _observed(timeline: dict[str, object]) -> dict[str, object]:
    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    request = DecodeRequest(
        "uart", timeline["samplerate_hz"], tuple(mapping.values()), mapping,
        _packed_samples(timeline), timeline["trigger_index"], timeline["options"],
    )
    return decode_private(request).to_dict()


def _matches(observed: dict[str, object], expected: dict[str, object]) -> bool:
    return observed == expected and canonical_json(observed) == canonical_json(expected)


def test_exact_candidate_and_accepted_fixture_identities() -> None:
    assert hashlib.sha256(SEMANTIC_BYTES).hexdigest() == (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    )
    assert hashlib.sha256(MATRIX_BYTES).hexdigest() == (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209"
    )
    assert hashlib.sha256(
        (ROOT / "tests/implementation/test_c3_b3_uart_conformance.py").read_bytes()
    ).hexdigest() == "6ebad5ba914a41904fc6965dbc592e201e0d1bee8211efb030e2bd18a6d5bd16"
    assert hashlib.sha256(
        (ROOT / "docs/reviews/c3-b3-uart-implementation-round-1.md").read_bytes()
    ).hexdigest() == "bf7ffcd8e147139a7f02436f324858408e414937dac0a0140ee33432debbe56c"


@pytest.mark.parametrize("timeline", TIMELINES, ids=lambda row: row["id"])
def test_all_54_uart_timelines_are_exact_and_repeat_deterministically(
    timeline: dict[str, object],
) -> None:
    assert len(TIMELINES) == 54 and len(BY_ID) == 54
    expected = _expected(timeline)
    first = _observed(timeline)
    second = _observed(timeline)
    assert _matches(first, expected)
    assert first == second
    assert canonical_json(first) == canonical_json(second)
    records = first["records"]
    assert isinstance(records, list)
    assert [row["emission_index"] for row in records] == list(range(len(records)))
    assert {row["kind"] for row in records} <= {"annotation", "python", "binary", "metadata"}


@pytest.mark.parametrize("row", DIRECT, ids=lambda row: row["id"])
def test_all_50_direct_rows_bind_to_a_complete_exact_timeline(row: dict[str, object]) -> None:
    assert len(DIRECT) == 50
    fixture = row["fixture"]
    assert fixture in BY_ID
    assert _matches(_observed(BY_ID[fixture]), _expected(BY_ID[fixture]))


@pytest.mark.parametrize("row", UNSUPPORTED, ids=lambda row: row["id"])
def test_all_77_unsupported_rows_reject_during_request_construction(
    monkeypatch: pytest.MonkeyPatch, row: dict[str, object],
) -> None:
    import pico_logic_analyzer._decode.host as host

    assert len(UNSUPPORTED) == 77
    monkeypatch.setattr(host, "_spawn_fixed_worker", lambda *_a, **_k: pytest.fail("spawned"))
    options = dict(row.get("selected_width_context") or {})
    options[row["option"]] = row["value"]
    with pytest.raises(RequestFailure, match="^options rejected$"):
        DecodeRequest("uart", 1, (17,), {"rx": 17}, (1,), 0, options)


def test_optional_pin_sentinel_and_reordered_noncontiguous_mapping() -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host

    rx = ApiV3Host(("rx", "tx"), {"rx": 17}, (17,), (0, 1), 1, 0, {})
    tx = ApiV3Host(("rx", "tx"), {"tx": 3}, (3,), (1, 0), 1, 0, {})
    both = ApiV3Host(("rx", "tx"), {"rx": 17, "tx": 3}, (3, 17), (1, 2), 1, 0, {})
    assert (rx.wait({}), rx.wait({})) == ((0, 0xFF), (1, 0xFF))
    assert (tx.wait({}), tx.wait({})) == ((0xFF, 1), (0xFF, 0))
    assert (both.wait({}), both.wait({})) == ((0, 1), (1, 0))


@pytest.mark.parametrize("mutation", ["declaration", "record", "order", "bytes"])
def test_hostile_expected_result_mutations_are_detected(mutation: str) -> None:
    timeline = BY_ID["uart-rx-valid-default"]
    observed = _observed(timeline)
    hostile = copy.deepcopy(_expected(timeline))
    if mutation == "declaration":
        hostile["declarations"]["annotations"][0]["description"] += " hostile"
    elif mutation == "record":
        hostile["records"][0]["start_sample"] += 1
    elif mutation == "order":
        hostile["records"][0], hostile["records"][1] = hostile["records"][1], hostile["records"][0]
    else:
        hostile["records"][1]["value"]["texts"][0] += " hostile"
    assert not _matches(observed, hostile)
    assert canonical_json(observed) != canonical_json(hostile)


def test_matrix_fixture_binding_mutation_is_detected() -> None:
    row = copy.deepcopy(DIRECT[0])
    original = BY_ID[row["fixture"]]
    row["fixture"] = "uart-tx-valid-default"
    rebound = BY_ID[row["fixture"]]
    assert row["fixture"] != original["id"]
    assert not _matches(_observed(rebound), _expected(original))


def test_defaults_are_matrix_only_and_candidate_imports_are_closed() -> None:
    candidate = ROOT / "tests/implementation/test_c3_b3_uart_conformance.py"
    tree = ast.parse(candidate.read_text(encoding="utf-8"))
    functions = {
        node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
    }
    assert "_matrix_uart_defaults" in functions
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
    assert _accepted_defaults()["baudrate"] == 115200


def test_snapshot_helper_hashes_and_uart_file_set_are_exact() -> None:
    files = {
        "Software/decoders/uart/__init__.py": (
            "351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f"
        ),
        "Software/decoders/uart/pd.py": (
            "67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc"
        ),
        "Software/decoders/common/srdhelper/__init__.py": (
            "125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1"
        ),
        "Software/decoders/common/srdhelper/mod.py": (
            "602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6"
        ),
    }
    assert {path: hashlib.sha256((REPO / path).read_bytes()).hexdigest() for path in files} == files
    uart = next(row for row in PROVENANCE["decoder_file_sets"] if row["decoder"] == "uart")
    assert uart["sha256"] == "eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3"
