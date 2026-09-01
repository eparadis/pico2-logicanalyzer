"""Independent, I2C-only C3-B3 conformance checks.

Expected values and the sole default are assembled only from the accepted
C3-B1 semantic corpus, option matrix, and provenance fixture.  In particular,
this module never imports decoder sources to construct its oracle.
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
I2C_TIMELINES = tuple(item for item in SEMANTIC["timelines"] if item["decoder"] == "i2c")
I2C_DIRECT_ROWS = tuple(
    item
    for item in MATRIX["rows"]
    if item["decoder"] == "i2c" and item["disposition"] == "direct-fixture"
)
I2C_UNSUPPORTED_ROWS = tuple(
    item
    for item in MATRIX["rows"]
    if item["decoder"] == "i2c" and item["disposition"] == "unsupported"
)
I2C_BY_ID = {item["id"]: item for item in I2C_TIMELINES}


def _matrix_i2c_defaults() -> dict[str, object]:
    """Use only accepted default-classification rows as the option oracle."""
    rows = tuple(
        row
        for row in MATRIX["rows"]
        if row["decoder"] == "i2c" and row["classification"] == "default"
    )
    assert len(rows) == 1
    assert rows[0]["option"] == "address_format"
    assert rows[0]["value"] == "shifted"
    assert rows[0]["disposition"] == "direct-fixture"
    return {rows[0]["option"]: rows[0]["value"]}


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
        "i2c",
        timeline["samplerate_hz"],
        tuple(mapping.values()),
        mapping,
        _samples(timeline),
        timeline["trigger_index"],
        timeline["options"],
    )


def _expected_result(timeline: dict[str, object]) -> dict[str, object]:
    identity = next(item for item in PROVENANCE["decoder_file_sets"] if item["decoder"] == "i2c")
    return {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "decoder": {"id": "i2c", "file_set_sha256": identity["sha256"]},
        "samplerate_hz": timeline["samplerate_hz"],
        "capture": {
            "sample_count": timeline["sample_count"],
            "trigger_index": timeline["trigger_index"],
        },
        "channels": [
            {"decoder_channel": channel, "physical_channel": physical}
            for channel, physical in timeline["mapping"].items()
        ],
        "options": dict(sorted({**_matrix_i2c_defaults(), **timeline["options"]}.items())),
        "declarations": timeline["declarations"],
        "records": timeline["expected_records"],
    }


def _assert_timeline(timeline: dict[str, object]) -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json, decode_result_from_dict

    expected = _expected_result(timeline)
    expected_object = decode_result_from_dict(expected)
    observed = decode_private(_request(timeline))
    # Complete typed, emission-ordered records cover annotation, binary,
    # metadata, and Python outputs; canonical bytes protect their wire form.
    assert observed == expected_object
    assert observed.to_dict() == expected
    assert canonical_json(observed.to_dict()) == canonical_json(expected)


@pytest.mark.parametrize("timeline", I2C_TIMELINES, ids=lambda item: item["id"])
def test_all_accepted_i2c_timelines_match_full_results_and_canonical_bytes(
    timeline: dict[str, object],
) -> None:
    assert len(I2C_TIMELINES) == 3
    assert set(I2C_BY_ID) == {
        "i2c-shifted-start-address-ack-data-nack-stop",
        "i2c-unshifted-repeated-start",
        "i2c-incomplete-boundary",
    }
    _assert_timeline(timeline)


@pytest.mark.parametrize("row", I2C_DIRECT_ROWS, ids=lambda item: item["id"])
def test_every_i2c_direct_option_row_resolves_to_its_accepted_timeline(
    row: dict[str, object],
) -> None:
    assert len(I2C_DIRECT_ROWS) == 2
    fixture = row["fixture"]
    assert isinstance(fixture, str) and fixture in I2C_BY_ID
    _assert_timeline(I2C_BY_ID[fixture])


def test_all_unsupported_i2c_rows_reject_before_any_worker_spawn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host_module
    from pico_logic_analyzer._decode.model import DecodeRequest, RequestFailure

    assert len(I2C_UNSUPPORTED_ROWS) == 6
    spawned = 0

    def forbidden_spawn(*_args: object, **_kwargs: object):
        nonlocal spawned
        spawned += 1
        raise AssertionError("unsupported I2C option reached worker spawn")

    monkeypatch.setattr(host_module, "_spawn_fixed_worker", forbidden_spawn)
    for row in I2C_UNSUPPORTED_ROWS:
        with pytest.raises(RequestFailure, match="^options rejected$"):
            DecodeRequest(
                "i2c",
                1,
                (19, 7),
                {"scl": 19, "sda": 7},
                (0,),
                0,
                {row["option"]: row["value"]},
            )
    assert spawned == 0


def test_i2c_noncontiguous_reordered_physical_mapping_and_pin_order_are_exact() -> None:
    from pico_logic_analyzer._decode.compat import ApiV3Host

    host = ApiV3Host(
        ("scl", "sda"),
        {"scl": 19, "sda": 7},
        (7, 19),
        (1, 2),
        2,
        0,
        {},
    )
    assert host.wait({}) == (0, 1)
    assert host.wait({}) == (1, 0)
    assert tuple(host.has_channel(index) for index in range(2)) == (True, True)


def test_i2c_repeated_run_stability_fixture_identities_and_default_are_exact() -> None:
    from pico_logic_analyzer._decode.host import decode_private
    from pico_logic_analyzer._decode.model import canonical_json

    timeline = I2C_BY_ID["i2c-shifted-start-address-ack-data-nack-stop"]
    first = canonical_json(decode_private(_request(timeline)).to_dict())
    second = canonical_json(decode_private(_request(timeline)).to_dict())
    assert first == second == canonical_json(_expected_result(timeline))
    assert _matrix_i2c_defaults() == {"address_format": "shifted"}
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
    ).hexdigest() == ("2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602")


def test_i2c_snapshot_digests_file_set_and_import_roots_are_closed() -> None:
    expected = {
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
    for relative, digest in expected.items():
        assert hashlib.sha256((REPOSITORY / relative).read_bytes()).hexdigest() == digest
    i2c_set = next(item for item in PROVENANCE["decoder_file_sets"] if item["decoder"] == "i2c")
    assert i2c_set["sha256"] == "dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae"
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
        "Software/decoders/i2c/__init__.py": {"pd"},
        "Software/decoders/i2c/pd.py": {"common", "sigrokdecode"},
        "Software/decoders/common/srdhelper/__init__.py": {"mod"},
        "Software/decoders/common/srdhelper/mod.py": {"enum", "itertools", "re"},
    }
