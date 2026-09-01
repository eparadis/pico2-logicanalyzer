"""Independent, UART-only C3-B3 conformance checks.

The expected values are assembled exclusively from the checked-in accepted
cycle-3 corpus.  This module neither imports the frozen decoder sources nor
uses an external/reference decoder host.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "testdata" / "decoders" / "cycle3"
SEMANTIC = json.loads((DATA / "semantic-fixtures.json").read_text(encoding="utf-8"))
MATRIX = json.loads((DATA / "option-matrix.json").read_text(encoding="utf-8"))
PROVENANCE = json.loads((DATA / "provenance.json").read_text(encoding="utf-8"))
UART_TIMELINES = tuple(item for item in SEMANTIC["timelines"] if item["decoder"] == "uart")
UART_DIRECT_ROWS = tuple(
    item
    for item in MATRIX["rows"]
    if item["decoder"] == "uart" and item["disposition"] == "direct-fixture"
)
UART_UNSUPPORTED_ROWS = tuple(
    item
    for item in MATRIX["rows"]
    if item["decoder"] == "uart" and item["disposition"] == "unsupported"
)
UART_BY_ID = {item["id"]: item for item in UART_TIMELINES}


def _matrix_uart_defaults() -> dict[str, object]:
    """Use only the accepted default-classification rows as the options oracle."""
    rows = tuple(
        row
        for row in MATRIX["rows"]
        if row["decoder"] == "uart" and row["classification"] == "default"
    )
    expected_keys = {
        "baudrate",
        "data_bits",
        "parity",
        "stop_bits",
        "bit_order",
        "format",
        "invert_rx",
        "invert_tx",
        "sample_point",
        "rx_packet_delim",
        "tx_packet_delim",
        "rx_packet_len",
        "tx_packet_len",
    }
    assert len(rows) == 13
    assert {row["option"] for row in rows} == expected_keys
    assert len({row["option"] for row in rows}) == len(rows)
    assert {row["disposition"] for row in rows} == {"direct-fixture"}
    return {row["option"]: row["value"] for row in rows}


def _samples(timeline: dict[str, object]) -> tuple[int, ...]:
    """Pack physical channels in the declared mapping order from fixture transitions."""
    mapping = timeline["mapping"]
    transitions = timeline["transitions"]
    assert isinstance(mapping, dict) and isinstance(transitions, dict)
    channel_ids = tuple(mapping.values())
    state: dict[str, int] = {}
    events: dict[int, list[tuple[str, int]]] = {}
    for wire, changes in transitions.items():
        assert isinstance(wire, str) and isinstance(changes, list)
        for sample, value in changes:
            events.setdefault(sample, []).append((wire, value))
    for physical in channel_ids:
        initial = [value for wire, value in events[0] if wire == f"D{physical}"]
        assert len(initial) == 1
        state[f"D{physical}"] = initial[0]
    packed: list[int] = []
    for sample in range(timeline["sample_count"]):
        for wire, value in events.get(sample, []):
            state[wire] = value
        packed.append(
            sum(
                (state[f"D{physical}"] & 1) << position
                for position, physical in enumerate(channel_ids)
            )
        )
    return tuple(packed)


def _request(timeline: dict[str, object]):
    from pico_logic_analyzer._decode.model import DecodeRequest

    mapping = timeline["mapping"]
    assert isinstance(mapping, dict)
    return DecodeRequest(
        "uart",
        timeline["samplerate_hz"],
        tuple(mapping.values()),
        mapping,
        _samples(timeline),
        timeline["trigger_index"],
        timeline["options"],
    )


def _expected_result(timeline: dict[str, object]) -> dict[str, object]:
    identity = next(item for item in PROVENANCE["decoder_file_sets"] if item["decoder"] == "uart")
    return {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "decoder": {"id": "uart", "file_set_sha256": identity["sha256"]},
        "samplerate_hz": timeline["samplerate_hz"],
        "capture": {
            "sample_count": timeline["sample_count"],
            "trigger_index": timeline["trigger_index"],
        },
        "channels": [
            {"decoder_channel": channel, "physical_channel": physical}
            for channel, physical in timeline["mapping"].items()
        ],
        "options": dict(sorted({**_matrix_uart_defaults(), **timeline["options"]}.items())),
        "declarations": timeline["declarations"],
        "records": timeline["expected_records"],
    }


def _assert_timeline(timeline: dict[str, object]) -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json, decode_result_from_dict

    expected = _expected_result(timeline)
    expected_object = decode_result_from_dict(expected)
    observed = decode_private(_request(timeline))
    # Equality covers declarations and the complete emission-ordered typed records;
    # canonical bytes separately protect ordering/representation at the boundary.
    assert observed == expected_object
    assert observed.to_dict() == expected
    assert canonical_json(observed.to_dict()) == canonical_json(expected)


@pytest.mark.parametrize("timeline", UART_TIMELINES, ids=lambda item: item["id"])
def test_all_accepted_uart_timelines_match_full_results_and_canonical_bytes(
    timeline: dict[str, object],
) -> None:
    assert len(UART_TIMELINES) == 54
    _assert_timeline(timeline)


@pytest.mark.parametrize("row", UART_DIRECT_ROWS, ids=lambda item: item["id"])
def test_every_uart_direct_option_row_resolves_to_its_accepted_timeline(
    row: dict[str, object],
) -> None:
    assert len(UART_DIRECT_ROWS) == 50
    fixture = row["fixture"]
    assert isinstance(fixture, str) and fixture in UART_BY_ID
    _assert_timeline(UART_BY_ID[fixture])


def test_all_unsupported_uart_rows_reject_before_any_worker_spawn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host_module
    from pico_logic_analyzer._decode.model import DecodeRequest, RequestFailure

    assert len(UART_UNSUPPORTED_ROWS) == 77
    spawned = 0

    def forbidden_spawn(*_args: object, **_kwargs: object):
        nonlocal spawned
        spawned += 1
        raise AssertionError("unsupported UART option reached worker spawn")

    monkeypatch.setattr(host_module, "_spawn_fixed_worker", forbidden_spawn)
    for row in UART_UNSUPPORTED_ROWS:
        options = dict(row.get("selected_width_context") or {})
        options[row["option"]] = row["value"]
        with pytest.raises(RequestFailure, match="options rejected"):
            DecodeRequest("uart", 1, (4,), {"rx": 4}, (0,), 0, options)
    assert spawned == 0


def test_uart_optional_mapping_sentinels_and_noncontiguous_reordered_channels_are_exact() -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host

    rx_only = ApiV3Host(("rx", "tx"), {"rx": 1}, (1,), (0, 1), 1, 0, {})
    tx_only = ApiV3Host(("rx", "tx"), {"tx": 0}, (0,), (0, 1), 1, 0, {})
    assert rx_only.wait({}) == (0, 255)
    assert rx_only.wait({}) == (1, 255)
    assert tx_only.wait({}) == (255, 0)
    assert tx_only.wait({}) == (255, 1)
    assert rx_only.has_channel(0) and not rx_only.has_channel(1)
    assert not tx_only.has_channel(0) and tx_only.has_channel(1)
    noncontiguous_reordered = ApiV3Host(
        ("rx", "tx"), {"rx": 19, "tx": 7}, (7, 19), (1, 2), 1, 0, {}
    )
    assert noncontiguous_reordered.wait({}) == (0, 1)
    assert noncontiguous_reordered.wait({}) == (1, 0)


def test_uart_snapshot_digests_file_set_and_import_roots_are_closed() -> None:
    expected = {
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
    for relative, digest in expected.items():
        assert hashlib.sha256((ROOT.parents[1] / relative).read_bytes()).hexdigest() == digest
    uart_set = next(item for item in PROVENANCE["decoder_file_sets"] if item["decoder"] == "uart")
    assert uart_set["sha256"] == "eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3"
    source_roots: dict[str, set[str]] = {}
    for relative in expected:
        tree = ast.parse((ROOT.parents[1] / relative).read_text(encoding="utf-8"))
        source_roots[relative] = {
            (node.module or "").split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module is not None
        } | {
            alias.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        }
    assert source_roots == {
        "Software/decoders/uart/__init__.py": {"pd"},
        "Software/decoders/uart/pd.py": {"common", "math", "sigrokdecode"},
        "Software/decoders/common/srdhelper/__init__.py": {"mod"},
        "Software/decoders/common/srdhelper/mod.py": {"enum", "itertools", "re"},
    }
