"""Independent static verification of the C3B2-IF002 fixture correction."""

from __future__ import annotations

import ast
import base64
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
DATA = ROOT / "testdata/decoders/cycle3"
GENERATOR = ROOT / "scripts/generate_cycle3_fixtures.py"
CANDIDATE = "3af6b9f80dd52611e14acca407707d1da7b8d9ac"
CANDIDATE_TREE = "14c010153ea5542617e601e4126047c561a48483"
FINDING_RECORD = "8c2b5dcfa7b607cb5c07ab95580c9d72f5433f96"
TIMELINE = "i2c-unshifted-repeated-start"

CANDIDATE_PATHS = {
    "Software/LogicAnalyzerPy/docs/reviews/"
    "c3-b1-semantic-fixture-correction-implementation-round-2.md",
    "Software/LogicAnalyzerPy/scripts/generate_cycle3_fixtures.py",
    "Software/LogicAnalyzerPy/testdata/decoders/cycle3/manifest.json",
    "Software/LogicAnalyzerPy/testdata/decoders/cycle3/semantic-fixtures.json",
    "Software/LogicAnalyzerPy/tests/implementation/test_cycle3_fixtures.py",
}

EXPECTED_DIGESTS = {
    "generator": "a101ae13cba938aa4d574fd1df3e4cc09dc845b2a643088cfee4a79313c3266f",
    "semantic-fixtures.json": (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    ),
    "manifest.json": "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9",
    "provenance.json": "e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4",
    "option-matrix.json": (
        "5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209"
    ),
    "typed-vectors.json": (
        "b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf"
    ),
    "experiment-caps.json": (
        "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d"
    ),
}


def _git(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=REPO, check=True, stdout=subprocess.PIPE
    ).stdout


def _git_json(revision: str, path: str) -> dict[str, Any]:
    value = json.loads(_git("show", f"{revision}:{path}"))
    assert isinstance(value, dict)
    return value


def _sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _timeline(corpus: dict[str, Any], timeline_id: str) -> dict[str, Any]:
    return next(item for item in corpus["timelines"] if item["id"] == timeline_id)


def _address_outputs(timeline: dict[str, Any]) -> tuple[int, bytes, str]:
    records = timeline["expected_records"]
    python_record = next(
        record
        for record in records
        if record["kind"] == "python"
        and record["value"]["value"][0].get("value") == "ADDRESS WRITE"
    )
    binary_record = next(
        record
        for record in records
        if record["kind"] == "binary" and record["value"]["class_index"] == 1
    )
    annotation = next(
        record
        for record in records
        if record["kind"] == "annotation"
        and record["value"]["class_index"] == 7
        and record["value"]["texts"][0].startswith("Address write:")
    )
    return (
        python_record["value"]["value"][1]["value"],
        base64.b64decode(binary_record["value"]["data_base64"], validate=True),
        annotation["value"]["texts"][-1],
    )


def test_exact_candidate_tree_scope_and_implementation_identity() -> None:
    assert _git("rev-parse", f"{CANDIDATE}^{{tree}}").decode().strip() == CANDIDATE_TREE
    paths = set(
        _git("diff", "--name-only", FINDING_RECORD, CANDIDATE).decode().splitlines()
    )
    assert paths == CANDIDATE_PATHS
    record = _git(
        "show",
        f"{CANDIDATE}:Software/LogicAnalyzerPy/docs/reviews/"
        "c3-b1-semantic-fixture-correction-implementation-round-2.md",
    ).decode()
    assert "c3-b1-semantic-fixture-implementor-replacement-8" in record
    assert "candidate not accepted" in record.lower()


def test_frozen_source_uses_same_conditionally_shifted_value_for_outputs() -> None:
    source = _git("show", f"{CANDIDATE}:Software/decoders/i2c/pd.py").decode()
    start = source.index("    def handle_address_or_data")
    end = source.index("    def get_ack", start)
    method = source[start:end]
    assert "if self.options['address_format'] == 'shifted':\n                    d >>= 1" in method
    assert "self.putp(ss_byte, es_byte, [cmd, d])" in method
    assert "self.putb(ss_byte, es_byte, [bin_class, bytes([d])])" in method
    assert "texts = [t.format(b = d) for t in texts]" in method


def test_exact_one_semantic_record_delta_across_all_63_timelines() -> None:
    path = "Software/LogicAnalyzerPy/testdata/decoders/cycle3/semantic-fixtures.json"
    before = _git_json(FINDING_RECORD, path)
    after = _git_json(CANDIDATE, path)
    assert len(before["timelines"]) == len(after["timelines"]) == 63
    before_by_id = {item["id"]: item for item in before["timelines"]}
    after_by_id = {item["id"]: item for item in after["timelines"]}
    assert before_by_id.keys() == after_by_id.keys()
    assert {
        key for key in before_by_id if before_by_id[key] != after_by_id[key]
    } == {TIMELINE}
    old = before_by_id[TIMELINE]
    new = after_by_id[TIMELINE]
    assert len(old["expected_records"]) == len(new["expected_records"])
    changed = [
        index
        for index, (left, right) in enumerate(
            zip(old["expected_records"], new["expected_records"], strict=True)
        )
        if left != right
    ]
    assert changed == [4]
    old_record = old["expected_records"][4]
    new_record = new["expected_records"][4]
    expected_old = json.loads(json.dumps(new_record))
    expected_old["value"]["data_base64"] = "UA=="
    assert old_record == expected_old
    assert new_record["value"]["data_base64"] == "oA=="


def test_unshifted_and_shifted_outputs_are_cross_kind_consistent() -> None:
    corpus = _git_json(
        CANDIDATE,
        "Software/LogicAnalyzerPy/testdata/decoders/cycle3/semantic-fixtures.json",
    )
    unshifted = _timeline(corpus, TIMELINE)
    assert unshifted["options"]["address_format"] == "unshifted"
    assert _address_outputs(unshifted) == (0xA0, b"\xa0", "A0")
    shifted = next(
        item
        for item in corpus["timelines"]
        if item["decoder"] == "i2c"
        and item["options"].get("address_format") == "shifted"
        and _address_outputs(item) == (0x50, b"\x50", "50")
    )
    assert shifted["id"] != TIMELINE


def test_generator_is_generic_and_manifest_digests_close() -> None:
    source = _git(
        "show",
        f"{CANDIDATE}:Software/LogicAnalyzerPy/scripts/generate_cycle3_fixtures.py",
    )
    text = source.decode()
    tree = ast.parse(text)
    imports = {
        node.module.split(".")[0]
        if isinstance(node, ast.ImportFrom) and node.module
        else alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import | ast.ImportFrom)
        for alias in node.names
    }
    assert imports <= {"__future__", "argparse", "base64", "copy", "hashlib", "json", "pathlib"}
    helper = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "i2c_byte"
    )
    helper_text = ast.get_source_segment(text, helper)
    assert helper_text is not None
    assert TIMELINE not in helper_text
    emitted_rule = (
        'emitted = value >> 1 if address and address_format == "shifted" else value'
    )
    assert emitted_rule in helper_text
    assert "base64.b64encode(bytes([emitted]))" in helper_text
    assert "tag_integer(emitted)" in helper_text
    manifest_path = "Software/LogicAnalyzerPy/testdata/decoders/cycle3/manifest.json"
    manifest = _git_json(CANDIDATE, manifest_path)
    assert _sha(source) == EXPECTED_DIGESTS["generator"] == manifest["generator_sha256"]
    for artifact in manifest["artifacts"]:
        name = artifact["path"]
        blob = _git(
            "show", f"{CANDIDATE}:Software/LogicAnalyzerPy/testdata/decoders/cycle3/{name}"
        )
        assert _sha(blob) == EXPECTED_DIGESTS[name] == artifact["sha256"]
    assert _sha(_git("show", f"{CANDIDATE}:{manifest_path}")) == EXPECTED_DIGESTS["manifest.json"]


def test_implementation_assertion_is_non_vacuous() -> None:
    path = "Software/LogicAnalyzerPy/tests/implementation/test_cycle3_fixtures.py"
    source = _git("show", f"{CANDIDATE}:{path}").decode()
    assert "base64.b64decode(address_binary[\"value\"][\"data_base64\"])" in source
    assert "== bytes(\n            [expected_address]\n        )" in source
    assert "address_python[\"value\"][\"value\"][1][\"value\"] == expected_address" in source
    assert "address_annotation[\"value\"][\"texts\"][-1] == f\"{expected_address:02X}\"" in source
    assert "((full_i2c, 0x50), (repeated, 0xA0))" in source
