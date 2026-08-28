"""Independent static verification for the corrected incomplete UART fixture."""

from __future__ import annotations

import ast
import copy
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
DATA = ROOT / "testdata/decoders/cycle3"
GENERATOR = ROOT / "scripts/generate_cycle3_fixtures.py"
CANDIDATE = "a98d328aab92f3dad66988fb70cc567946dc89d0"
CANDIDATE_TREE = "450aadcf26bd6c74860872bfbf0a0a1b32d94f3b"
PARENT = f"{CANDIDATE}^"
TIMELINE_ID = "uart-msb-9bit-boundary-incomplete"

CANDIDATE_PATHS = {
    "Software/LogicAnalyzerPy/docs/reviews/"
    "c3-b1-semantic-fixture-correction-implementation-round-1.md",
    "Software/LogicAnalyzerPy/scripts/generate_cycle3_fixtures.py",
    "Software/LogicAnalyzerPy/testdata/decoders/cycle3/experiment-caps.json",
    "Software/LogicAnalyzerPy/testdata/decoders/cycle3/manifest.json",
    "Software/LogicAnalyzerPy/testdata/decoders/cycle3/semantic-fixtures.json",
    "Software/LogicAnalyzerPy/tests/implementation/test_cycle3_fixtures.py",
}

EXPECTED_DIGESTS = {
    "generator": "d872fe9f6c1cb3407a8d05d7b9e03e3bb34b10baee8fa47e55b57bb4b64574f6",
    "semantic-fixtures.json": (
        "1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329"
    ),
    "experiment-caps.json": (
        "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d"
    ),
    "manifest.json": "ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f",
    "provenance.json": "e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4",
    "option-matrix.json": (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209"
    ),
    "typed-vectors.json": (
        "b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf"
    ),
}

EXPECTED_WAITS = [
    ({"condition": [{"0": "f"}, {"0": "e"}], "sample": 1, "matched": [True, True]}),
    ({"condition": [{"skip": 9}, {"0": "e"}], "sample": 10, "matched": [True, False]}),
    ({"condition": [{"skip": 10}, {"0": "e"}], "sample": 11, "matched": [False, True]}),
    (
        {
            "condition": [{"skip": 9}, {"0": "e"}, {"skip": 110}],
            "sample": 20,
            "matched": [True, False, False],
        }
    ),
    (
        {
            "condition": [{"skip": 10}, {"0": "e"}, {"skip": 101}],
            "sample": 21,
            "matched": [False, True, False],
        }
    ),
    ({"condition": [{"skip": 9}, {"0": "e"}], "sample": 30, "matched": [True, False]}),
    ({"condition": [{"skip": 10}, {"0": "e"}], "sample": 31, "matched": [False, True]}),
    (
        {
            "condition": [{"skip": 9}, {"0": "e"}, {"skip": 110}],
            "sample": 40,
            "matched": [True, False, False],
        }
    ),
    (
        {
            "condition": [{"skip": 10}, {"0": "e"}, {"skip": 101}],
            "sample": 41,
            "matched": [False, True, False],
        }
    ),
    ({"condition": [{"skip": 9}, {"0": "e"}], "sample": 50, "matched": [True, False]}),
    (
        {
            "condition": [{"skip": 10}, {"0": "e"}],
            "sample": 56,
            "matched": [False, False],
            "terminal": "end-of-input failed wait",
        }
    ),
]
EXPECTED_PINS = [
    [0, 255],
    [0, 255],
    [1, 255],
    [1, 255],
    [0, 255],
    [0, 255],
    [1, 255],
    [1, 255],
    [0, 255],
    [0, 255],
    [0, 255],
]


def _load(name: str) -> dict[str, Any]:
    value = json.loads((DATA / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _git_bytes(revision: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        cwd=REPO,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout


def _sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha(path: Path) -> str:
    return _sha_bytes(path.read_bytes())


def _canonical(value: object) -> bytes:
    return (
        json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode()
        + b"\n"
    )


def _timeline() -> dict[str, Any]:
    return next(
        item
        for item in _load("semantic-fixtures.json")["timelines"]
        if item["id"] == TIMELINE_ID
    )


def _time(sample: int) -> dict[str, dict[str, int]]:
    return {
        "absolute": {"numerator": sample, "denominator": 1_152_000},
        "trigger_relative": {"numerator": sample - 1, "denominator": 1_152_000},
    }


def _record(
    emission: int,
    kind: str,
    output_id: int,
    start: int,
    end: int,
    value: dict[str, object],
) -> dict[str, object]:
    return {
        "emission_index": emission,
        "start_sample": start,
        "end_sample": end,
        "start_time": _time(start),
        "end_time": _time(end),
        "output_id": output_id,
        "kind": kind,
        "value": value,
    }


EXPECTED_RECORDS = [
    _record(
        0,
        "python",
        0,
        5,
        15,
        {
            "tag": "list",
            "value": [
                {"tag": "string", "value": "STARTBIT"},
                {"tag": "integer", "value": 0},
                {"tag": "integer", "value": 0},
            ],
        },
    ),
    _record(
        1,
        "annotation",
        2,
        5,
        15,
        {"class_index": 2, "texts": ["Start bit", "Start", "S"]},
    ),
    *[
        _record(
            2 + index,
            "annotation",
            2,
            15 + 10 * index,
            25 + 10 * index,
            {"class_index": 12, "texts": [str(value)]},
        )
        for index, value in enumerate((1, 0, 1, 0))
    ],
]


def _validate_declarations(value: object) -> None:
    if not isinstance(value, dict):
        raise ValueError("declarations")
    annotations = value.get("annotations")
    rows = value.get("annotation_rows")
    binary = value.get("binary")
    if (
        not isinstance(annotations, list)
        or not isinstance(rows, list)
        or not isinstance(binary, list)
    ):
        raise ValueError("declarations")
    annotation_ids = [
        "rx-data",
        "tx-data",
        "rx-start",
        "tx-start",
        "rx-parity-ok",
        "tx-parity-ok",
        "rx-parity-err",
        "tx-parity-err",
        "rx-stop",
        "tx-stop",
        "rx-warning",
        "tx-warning",
        "rx-data-bit",
        "tx-data-bit",
        "rx-break",
        "tx-break",
        "rx-packet",
        "tx-packet",
    ]
    if [(item.get("index"), item.get("id")) for item in annotations] != list(
        enumerate(annotation_ids)
    ):
        raise ValueError("annotations")
    row_ids = [
        "rx-data-bits",
        "rx-data-vals",
        "rx-warnings",
        "rx-breaks",
        "rx-packets",
        "tx-data-bits",
        "tx-data-vals",
        "tx-warnings",
        "tx-breaks",
        "tx-packets",
    ]
    row_members = [
        [12],
        [0, 2, 4, 6, 8],
        [10],
        [14],
        [16],
        [13],
        [1, 3, 5, 7, 9],
        [11],
        [15],
        [17],
    ]
    if [
        (item.get("index"), item.get("id"), item.get("annotation_indices"))
        for item in rows
    ] != [(index, row_ids[index], row_members[index]) for index in range(10)]:
        raise ValueError("rows")
    if [(item.get("index"), item.get("id")) for item in binary] != [
        (0, "rx"),
        (1, "tx"),
        (2, "rxtx"),
    ] or value.get("metadata") != []:
        raise ValueError("binary or metadata")


def _validate_timeline(value: object) -> None:
    if not isinstance(value, dict):
        raise ValueError("timeline")
    expected_scalar = {
        "id": TIMELINE_ID,
        "decoder": "uart",
        "meaning": "9-bit MSB first boundary; end preserves already-emitted bit annotations",
        "mapping": {"rx": 4},
        "options": {"data_bits": 9, "bit_order": "msb-first", "sample_point": 99},
        "sample_count": 56,
        "samplerate_hz": 1_152_000,
        "trigger_index": 1,
        "transitions": {
            "D4": [[0, 1], [1, 0], [11, 1], [21, 0], [31, 1], [41, 0], [51, 0]]
        },
    }
    if any(value.get(key) != expected for key, expected in expected_scalar.items()):
        raise ValueError("timeline identity")
    expected_waits = [
        {**wait, "pins": pins} for wait, pins in zip(EXPECTED_WAITS, EXPECTED_PINS, strict=True)
    ]
    if value.get("expected_wait_trace") != expected_waits:
        raise ValueError("wait trace")
    if value.get("expected_records") != EXPECTED_RECORDS:
        raise ValueError("records")
    _validate_declarations(value.get("declarations"))


def test_exact_candidate_identity_tree_scope_and_blobs() -> None:
    tree = subprocess.check_output(
        ["git", "rev-parse", f"{CANDIDATE}^{{tree}}"], cwd=REPO, text=True
    ).strip()
    assert tree == CANDIDATE_TREE
    output = subprocess.check_output(
        ["git", "diff-tree", "--root", "--no-commit-id", "--name-status", "-r", CANDIDATE],
        cwd=REPO,
        text=True,
    )
    changed = {line.split("\t", 1)[1] for line in output.splitlines()}
    assert changed == CANDIDATE_PATHS
    for relative in CANDIDATE_PATHS:
        assert (REPO / relative).read_bytes() == _git_bytes(CANDIDATE, relative)


def test_exact_source_derived_timeline_records_declarations_and_order() -> None:
    timeline = _timeline()
    _validate_timeline(timeline)
    assert [wait["sample"] for wait in timeline["expected_wait_trace"]] == [
        1,
        10,
        11,
        20,
        21,
        30,
        31,
        40,
        41,
        50,
        56,
    ]
    assert [record["emission_index"] for record in timeline["expected_records"]] == list(range(6))
    assert not {
        "DATA",
        "FRAME",
        "STOPBIT",
    } & {
        tagged.get("value")
        for record in timeline["expected_records"]
        if record["kind"] == "python"
        for tagged in record["value"].get("value", [])
        if tagged.get("tag") == "string"
    }


@pytest.mark.parametrize(
    "mutation",
    [
        "old-centre",
        "missing-idle",
        "reordered-idle",
        "matched",
        "pins",
        "missing-emission",
        "stale-emissions",
        "invented-complete",
        "record-coordinate",
        "record-tag",
        "option",
        "transition",
        "boundary",
        "declaration",
    ],
)
def test_nonvacuous_correction_mutation_matrix(mutation: str) -> None:
    original = _timeline()
    _validate_timeline(original)
    value = copy.deepcopy(original)
    if mutation == "old-centre":
        value["expected_wait_trace"][1]["sample"] = 6
    elif mutation == "missing-idle":
        value["expected_wait_trace"][3]["condition"].pop()
        value["expected_wait_trace"][3]["matched"].pop()
    elif mutation == "reordered-idle":
        value["expected_wait_trace"][3]["condition"][1:] = reversed(
            value["expected_wait_trace"][3]["condition"][1:]
        )
    elif mutation == "matched":
        value["expected_wait_trace"][4]["matched"] = [True, False, False]
    elif mutation == "pins":
        value["expected_wait_trace"][8]["pins"] = [1, 255]
    elif mutation == "missing-emission":
        value["expected_records"].pop()
    elif mutation == "stale-emissions":
        value["expected_records"] = value["expected_records"][:2]
    elif mutation == "invented-complete":
        value["expected_records"].append(
            _record(6, "python", 0, 15, 56, {"tag": "string", "value": "DATA"})
        )
    elif mutation == "record-coordinate":
        value["expected_records"][0]["start_sample"] = 0
    elif mutation == "record-tag":
        value["expected_records"][0]["value"]["tag"] = "tuple"
    elif mutation == "option":
        value["options"]["sample_point"] = 50
    elif mutation == "transition":
        value["transitions"]["D4"][-1][1] = 1
    elif mutation == "boundary":
        value["sample_count"] = 55
    elif mutation == "declaration":
        value["declarations"]["annotations"][12]["id"] = "derived-output"
    assert value != original
    with pytest.raises(ValueError):
        _validate_timeline(value)


def test_generator_is_static_stdlib_only_and_has_no_runtime_oracle_route() -> None:
    source = GENERATOR.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = {
        node.module.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    } | {
        alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    assert imports == {"__future__", "argparse", "copy", "hashlib", "json", "pathlib"}
    forbidden_calls = {"exec", "eval", "compile", "__import__", "open"}
    called_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    assert not forbidden_calls & called_names
    lowered = source.lower()
    for forbidden in (
        "cycle3-raw",
        "cycle3_characterize",
        "subprocess",
        "pythonnet",
        "libsigrokdecode",
        "sigrok-cli",
    ):
        assert forbidden not in lowered
    assert _load("semantic-fixtures.json")["oracle"] == (
        "independently authored declarative timelines; no runtime output"
    )


def _tagged_depth(value: object) -> int:
    if not isinstance(value, dict):
        return 0
    children = value.get("value")
    if value.get("tag") in {"list", "tuple"} and isinstance(children, list):
        return 1 + max((_tagged_depth(child) for child in children), default=0)
    return 1


def test_manifest_digests_and_every_cap_formula_recompute() -> None:
    fixtures = _load("semantic-fixtures.json")
    caps = _load("experiment-caps.json")["caps"]
    cap_by_id = {item["id"]: item for item in caps}
    manifest = _load("manifest.json")
    assert _sha(GENERATOR) == EXPECTED_DIGESTS["generator"]
    assert manifest["generator_sha256"] == EXPECTED_DIGESTS["generator"]
    assert _sha(DATA / "manifest.json") == EXPECTED_DIGESTS["manifest.json"]
    for artifact in manifest["artifacts"]:
        assert _sha(DATA / artifact["path"]) == artifact["sha256"]
        assert artifact["sha256"] == EXPECTED_DIGESTS[artifact["path"]]

    fixture_bytes = len(_canonical(fixtures))
    max_capture = max(item["sample_count"] for item in fixtures["timelines"])
    max_records = max(len(item["expected_records"]) for item in fixtures["timelines"])
    max_record_bytes = max(
        len(_canonical(record))
        for timeline in fixtures["timelines"]
        for record in timeline["expected_records"]
    )
    max_depth = max(
        _tagged_depth(record["value"])
        for timeline in fixtures["timelines"]
        for record in timeline["expected_records"]
    )
    basis = {
        "scheduling-policy-quantum-ms": 50,
        "corpus-max-input-samples": max_capture,
        "fixture-corpus-bytes": fixture_bytes,
        "corpus-max-records": max_records,
        "largest-record-bytes": max_record_bytes,
        "cap:diagnostic_bytes": cap_by_id["diagnostic_bytes"]["value"],
        "corpus-max-nested-depth": max_depth,
    }
    for cap in caps:
        derivation = cap["derivation"]
        assert derivation["basis_value"] == basis[derivation["basis_category"]]
        multiplied = derivation["basis_value"] * derivation["multiplier"]
        expected = (
            max(multiplied, derivation["floor"])
            if derivation["operation"] == "max-floor"
            else multiplied
        )
        assert derivation["operation"] in {"multiply", "max-floor"}
        assert cap["value"] == derivation["result"] == expected
        assert cap["boundary"] == {"accept": expected, "reject": expected + 1}
    assert fixture_bytes == 725_879
    assert cap_by_id["request_bytes"]["value"] == 46_456_256
    assert cap_by_id["retained_result_bytes"]["value"] == 185_825_024
    assert cap_by_id["worker_address_space_bytes"]["value"] == 68_719_476_736


def test_unrelated_authorities_counts_and_option_links_are_preserved() -> None:
    for name in ("provenance.json", "option-matrix.json", "typed-vectors.json"):
        relative = f"Software/LogicAnalyzerPy/testdata/decoders/cycle3/{name}"
        assert (DATA / name).read_bytes() == _git_bytes(PARENT, relative)
        assert _sha(DATA / name) == EXPECTED_DIGESTS[name]
    fixtures = _load("semantic-fixtures.json")
    assert len(fixtures["timelines"]) == 63
    assert len(fixtures["edge_decisions"]) == 5
    assert len(fixtures["optional_pin_cases"]) == 5
    rows = _load("option-matrix.json")["rows"]
    assert len(rows) == 165
    assert len({row["id"] for row in rows}) == 165
    assert Counter(row["disposition"] for row in rows) == {
        "direct-fixture": 62,
        "unsupported": 103,
    }
    timeline_ids = {timeline["id"] for timeline in fixtures["timelines"]}
    for row in rows:
        if row["disposition"] == "direct-fixture":
            assert row["fixture"] in timeline_ids
    sample_point = next(row for row in rows if row["id"] == "uart-sample_point-99")
    assert sample_point["fixture"] == "direct-uart-sample_point-99"
    assert sample_point["fixture"] != TIMELINE_ID


def test_historical_inventory_failure_and_broad_mypy_non_gate_are_not_weakened() -> None:
    generated = {
        "manifest.json",
        "provenance.json",
        "semantic-fixtures.json",
        "option-matrix.json",
        "typed-vectors.json",
        "experiment-caps.json",
    }
    extras = {path.name for path in DATA.glob("*.json")} - generated
    assert extras == {
        "b1-final-candidate.json",
        "b1-final-candidate-round-2.json",
        "threshold-proposal-round-1.json",
        "threshold-proposal-round-2.json",
    }
    diff = subprocess.check_output(
        ["git", "diff", PARENT, CANDIDATE, "--", *sorted(CANDIDATE_PATHS)],
        cwd=REPO,
        text=True,
    )
    assert "type: ignore" not in diff
    assert not any(
        path.endswith(("pyproject.toml", "mypy.ini", "requirements-dev.lock"))
        for path in CANDIDATE_PATHS
    )
