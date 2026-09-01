"""Independent, SPI-only C3-B3 conformance checks.

Expected values and defaults are assembled only from the accepted C3-B1
semantic corpus, option matrix, and provenance fixtures.  This module never
imports a frozen decoder source to derive an oracle.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
DATA = ROOT / "testdata" / "decoders" / "cycle3"
SEMANTIC_PATH = DATA / "semantic-fixtures.json"
MATRIX_PATH = DATA / "option-matrix.json"
PROVENANCE_PATH = DATA / "provenance.json"
SEMANTIC = json.loads(SEMANTIC_PATH.read_text(encoding="utf-8"))
MATRIX = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
PROVENANCE = json.loads(PROVENANCE_PATH.read_text(encoding="utf-8"))
SPI_TIMELINES = tuple(item for item in SEMANTIC["timelines"] if item["decoder"] == "spi")
SPI_DIRECT_ROWS = tuple(
    item
    for item in MATRIX["rows"]
    if item["decoder"] == "spi" and item["disposition"] == "direct-fixture"
)
SPI_UNSUPPORTED_ROWS = tuple(
    item
    for item in MATRIX["rows"]
    if item["decoder"] == "spi" and item["disposition"] == "unsupported"
)
SPI_BY_ID = {item["id"]: item for item in SPI_TIMELINES}


def _matrix_spi_defaults() -> dict[str, object]:
    """Use only accepted default-classification rows as the option oracle."""
    rows = tuple(
        row
        for row in MATRIX["rows"]
        if row["decoder"] == "spi" and row["classification"] == "default"
    )
    expected_keys = {"cs_polarity", "cpol", "cpha", "bitorder", "wordsize"}
    assert len(rows) == 5
    assert {row["option"] for row in rows} == expected_keys
    assert len({row["option"] for row in rows}) == len(rows)
    assert {row["disposition"] for row in rows} == {"direct-fixture"}
    return {row["option"]: row["value"] for row in rows}


def _samples(timeline: dict[str, object]) -> tuple[int, ...]:
    """Pack fixture physical channels in their declared capture order."""
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
        "spi",
        timeline["samplerate_hz"],
        tuple(mapping.values()),
        mapping,
        _samples(timeline),
        timeline["trigger_index"],
        timeline["options"],
    )


def _expected_result(timeline: dict[str, object]) -> dict[str, object]:
    identity = next(item for item in PROVENANCE["decoder_file_sets"] if item["decoder"] == "spi")
    return {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "decoder": {"id": "spi", "file_set_sha256": identity["sha256"]},
        "samplerate_hz": timeline["samplerate_hz"],
        "capture": {
            "sample_count": timeline["sample_count"],
            "trigger_index": timeline["trigger_index"],
        },
        "channels": [
            {"decoder_channel": channel, "physical_channel": physical}
            for channel, physical in timeline["mapping"].items()
        ],
        "options": dict(sorted({**_matrix_spi_defaults(), **timeline["options"]}.items())),
        "declarations": timeline["declarations"],
        "records": timeline["expected_records"],
    }


def _assert_timeline(timeline: dict[str, object]) -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json, decode_result_from_dict

    expected = _expected_result(timeline)
    expected_object = decode_result_from_dict(expected)
    observed = decode_private(_request(timeline))
    # This equality covers all annotation, binary, metadata, and Python records,
    # including SPI DATA/tagged values; canonical bytes protect their order/form.
    assert observed == expected_object
    assert observed.to_dict() == expected
    assert canonical_json(observed.to_dict()) == canonical_json(expected)


@pytest.mark.parametrize("timeline", SPI_TIMELINES, ids=lambda item: item["id"])
def test_all_accepted_spi_timelines_match_full_results_and_canonical_bytes(
    timeline: dict[str, object],
) -> None:
    assert len(SPI_TIMELINES) == 6
    assert {item["id"] for item in SPI_TIMELINES} == {
        "spi-mosi-mode0-word8",
        "spi-miso-mode3-word8",
        "spi-cs-active-high-lsb-word1",
        "spi-incomplete-no-cs",
        "direct-spi-cs_polarity-activeneglow",
        "direct-spi-bitorder-msbnegfirst",
    }
    _assert_timeline(timeline)


@pytest.mark.parametrize("row", SPI_DIRECT_ROWS, ids=lambda item: item["id"])
def test_every_spi_direct_option_row_resolves_to_its_accepted_timeline(
    row: dict[str, object],
) -> None:
    assert len(SPI_DIRECT_ROWS) == 10
    fixture = row["fixture"]
    assert isinstance(fixture, str) and fixture in SPI_BY_ID
    _assert_timeline(SPI_BY_ID[fixture])


def test_all_unsupported_spi_rows_reject_before_any_worker_spawn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host_module
    from pico_logic_analyzer._decode.model import DecodeRequest, RequestFailure

    assert len(SPI_UNSUPPORTED_ROWS) == 20
    spawned = 0

    def forbidden_spawn(*_args: object, **_kwargs: object):
        nonlocal spawned
        spawned += 1
        raise AssertionError("unsupported SPI option reached worker spawn")

    monkeypatch.setattr(host_module, "_spawn_fixed_worker", forbidden_spawn)
    for row in SPI_UNSUPPORTED_ROWS:
        with pytest.raises(RequestFailure, match="options rejected"):
            DecodeRequest(
                "spi", 1, (1, 3), {"clk": 1, "mosi": 3}, (0,), 0,
                {row["option"]: row["value"]},
            )
    assert spawned == 0


def test_spi_optional_mapping_sentinels_and_noncontiguous_reordered_channels_are_exact() -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host

    pins = ("clk", "miso", "mosi", "cs")
    miso_only = ApiV3Host(pins, {"clk": 1, "miso": 2}, (1, 2), (2,), 1, 0, {})
    mosi_only = ApiV3Host(pins, {"clk": 1, "mosi": 3}, (1, 3), (2,), 1, 0, {})
    no_cs = ApiV3Host(
        pins, {"clk": 1, "miso": 2, "mosi": 3}, (1, 2, 3), (2,), 1, 0, {}
    )
    assert miso_only.wait({}) == (0, 1, 255, 255)
    assert tuple(miso_only.has_channel(index) for index in range(4)) == (
        True,
        True,
        False,
        False,
    )
    assert mosi_only.wait({}) == (0, 255, 1, 255)
    assert tuple(mosi_only.has_channel(index) for index in range(4)) == (
        True,
        False,
        True,
        False,
    )
    assert no_cs.wait({}) == (0, 1, 0, 255)
    assert tuple(no_cs.has_channel(index) for index in range(4)) == (
        True,
        True,
        True,
        False,
    )
    noncontiguous_reordered = ApiV3Host(
        pins,
        {"clk": 19, "miso": 7, "mosi": 12, "cs": 3},
        (12, 3, 19, 7),
        (1, 2),
        2,
        0,
        {},
    )
    assert noncontiguous_reordered.wait({}) == (0, 0, 1, 0)
    assert noncontiguous_reordered.wait({}) == (0, 0, 0, 1)


def test_spi_repeated_run_canonical_stability_and_fixture_identity_are_exact() -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json

    timeline = SPI_BY_ID["spi-mosi-mode0-word8"]
    first = canonical_json(decode_private(_request(timeline)).to_dict())
    second = canonical_json(decode_private(_request(timeline)).to_dict())
    assert first == second == canonical_json(_expected_result(timeline))
    assert hashlib.sha256(SEMANTIC_PATH.read_bytes()).hexdigest() == (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    )
    assert hashlib.sha256(MATRIX_PATH.read_bytes()).hexdigest() == (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209"
    )
    b1 = (ROOT / "testdata" / "evidence" / "c3-b1.json").read_text(encoding="utf-8")
    assert "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9" in b1
    assert hashlib.sha256(
        (ROOT / "testdata" / "evidence" / "c3-b2.json").read_bytes()
    ).hexdigest() == "2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602"


def test_spi_snapshot_digests_file_set_and_import_roots_are_closed() -> None:
    expected = {
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
    for relative, digest in expected.items():
        assert hashlib.sha256((REPOSITORY / relative).read_bytes()).hexdigest() == digest
    spi_set = next(item for item in PROVENANCE["decoder_file_sets"] if item["decoder"] == "spi")
    assert spi_set["sha256"] == "96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193"
    source_roots: dict[str, set[str]] = {}
    for relative in expected:
        tree = ast.parse((REPOSITORY / relative).read_text(encoding="utf-8"))
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
        "Software/decoders/sigrokdecode.py": set(),
        "Software/decoders/spi/__init__.py": {"pd"},
        "Software/decoders/spi/pd.py": {"collections", "sigrokdecode"},
    }
