from __future__ import annotations

import ast
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[2]
DATA = ROOT / "testdata" / "decoders" / "cycle3"
GENERATOR = ROOT / "scripts" / "generate_cycle3_fixtures.py"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name: str) -> object:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def level_at(transitions: list[list[int]], sample: int) -> int:
    return [level for at, level in transitions if at <= sample][-1]


def test_cycle3_fixture_surface_is_present_and_rebuildable() -> None:
    """This initially failed because B1 had no static fixture generator or corpus."""
    assert GENERATOR.is_file()
    required = {
        "manifest.json",
        "provenance.json",
        "semantic-fixtures.json",
        "option-matrix.json",
        "typed-vectors.json",
        "experiment-caps.json",
    }
    assert {path.name for path in DATA.glob("*.json")} == required
    before = {path.name: sha256(path) for path in DATA.glob("*.json")}
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--check"], cwd=ROOT, text=True, capture_output=True
    )
    assert result.returncode == 0, result.stderr
    result = subprocess.run(
        [sys.executable, str(GENERATOR)], cwd=ROOT, text=True, capture_output=True
    )
    assert result.returncode == 0, result.stderr
    assert before == {path.name: sha256(path) for path in DATA.glob("*.json")}


def test_provenance_is_closed_and_matches_checked_in_static_sources() -> None:
    provenance = load("provenance.json")
    assert provenance["import_commit"] == "407b5ef039aa0474c400c0721749baa126e53270"
    assert provenance["prior_gitlink"] == "0235970293590f673a253950e6c61017cefa97df"
    assert provenance["permitted_imports"] == [
        "i2c.pd (relative package import .pd)",
        "spi.pd (relative package import .pd)",
        "uart.pd (relative package import .pd)",
        "common.srdhelper",
        "collections.namedtuple",
        "enum.Enum",
        "enum.IntEnum",
        "enum.unique",
        "itertools.chain",
        "math.ceil",
        "math.floor",
        "re",
        "sigrokdecode",
    ]
    assert {item["path"] for item in provenance["files"]} == {
        "Software/decoders/sigrokdecode.py",
        "Software/decoders/uart/__init__.py",
        "Software/decoders/uart/pd.py",
        "Software/decoders/spi/__init__.py",
        "Software/decoders/spi/pd.py",
        "Software/decoders/i2c/__init__.py",
        "Software/decoders/i2c/pd.py",
        "Software/decoders/common/srdhelper/__init__.py",
        "Software/decoders/common/srdhelper/mod.py",
    }
    for item in provenance["files"]:
        assert sha256(ROOT.parents[1] / item["path"]) == item["sha256"]
        if item["path"].endswith("sigrokdecode.py"):
            assert item["license"] == "unobserved-in-file"
            assert item["notice_observation"] == "no copyright or GPL notice in local shim bytes"
        else:
            assert item["license"] == "GPL-2.0-or-later"
            assert "GPLv2-or-later" in item["notice_observation"]


def test_semantics_sentinels_options_tags_and_caps_are_closed() -> None:
    fixtures = load("semantic-fixtures.json")
    assert {item["id"] for item in fixtures["edge_decisions"]} == {
        "wait-empty",
        "search-skip",
        "simultaneous-alternatives",
        "interval-boundary",
        "end-of-input",
    }
    assert all(item["decision"] and item["expected_calls"] for item in fixtures["edge_decisions"])
    assert {timeline["decoder"] for timeline in fixtures["timelines"]} == {"uart", "spi", "i2c"}
    assert {
        record["kind"]
        for timeline in fixtures["timelines"]
        for record in timeline["expected_records"]
    } == {"annotation", "python", "binary", "metadata"}
    assert {item["id"] for item in fixtures["optional_pin_cases"]} == {
        "uart-rx-only",
        "uart-tx-only",
        "spi-miso-only",
        "spi-mosi-only",
        "spi-no-cs",
    }
    assert all(255 in item["compatibility_pins"] for item in fixtures["optional_pin_cases"])
    matrix = load("option-matrix.json")["rows"]
    assert matrix and {row["disposition"] for row in matrix} <= {
        "direct-fixture",
        "static-equivalence",
        "unsupported",
    }
    assert all(row["id"] and (row["fixture"] or row["rejection_rule"]) for row in matrix)
    assert {row["option"] for row in matrix if row["classification"] == "default"} >= {
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
        "wordsize",
        "address_format",
    }
    direct_ids = {timeline["id"] for timeline in fixtures["timelines"]}
    assert all(
        row["fixture"] in direct_ids for row in matrix if row["disposition"] == "direct-fixture"
    )


def test_hand_authored_protocol_cases_have_real_trace_declarations_and_times() -> None:
    """Reject the replacement candidate's prior one-edge/generic-record pattern."""
    fixtures = load("semantic-fixtures.json")
    timelines = {item["id"]: item for item in fixtures["timelines"]}
    required = {
        "uart-rx-valid-default",
        "uart-tx-valid-default",
        "uart-parity-invalid-stop-break-idle-packet",
        "uart-msb-9bit-boundary-incomplete",
        "spi-mosi-mode0-word8",
        "spi-miso-mode3-word8",
        "spi-cs-active-high-lsb-word1",
        "spi-incomplete-no-cs",
        "i2c-shifted-start-address-ack-data-nack-stop",
        "i2c-unshifted-repeated-start",
        "i2c-incomplete-boundary",
    }
    assert required <= timelines.keys()
    registration = {
        "uart": {"python": 0, "binary": 1, "annotation": 2},
        "spi": {"python": 0, "annotation": 1, "binary": 2, "metadata": 3},
        "i2c": {"python": 0, "annotation": 1, "binary": 2, "metadata": 3},
    }
    for timeline in timelines.values():
        assert timeline["expected_wait_trace"]
        assert timeline["declarations"]["annotations"]
        assert max(len(edges) for edges in timeline["transitions"].values()) >= 2
        assert "direct closed option row" not in timeline["meaning"]
        records = timeline["expected_records"]
        for wait in timeline["expected_wait_trace"]:
            assert isinstance(wait["sample"], int) and wait["sample"] >= 0
            assert all(isinstance(value, bool) for value in wait["matched"])
            assert len(wait["pins"]) == {"uart": 2, "spi": 4, "i2c": 2}[timeline["decoder"]]
            assert all(value in {0, 1, 255} for value in wait["pins"])
        assert [item["emission_index"] for item in records] == list(range(len(records)))
        for item in records:
            assert item["output_id"] == registration[timeline["decoder"]][item["kind"]]
            assert item["start_sample"] <= item["end_sample"]
            for stamp, sample in (
                (item["start_time"], item["start_sample"]),
                (item["end_time"], item["end_sample"]),
            ):
                assert stamp["absolute"] == {
                    "numerator": sample,
                    "denominator": timeline["samplerate_hz"],
                }
                assert stamp["trigger_relative"]["numerator"] == sample - timeline["trigger_index"]
                assert stamp["trigger_relative"]["denominator"] == timeline["samplerate_hz"]
    assert all(255 in item["compatibility_pins"] for item in fixtures["optional_pin_cases"])
    decisions = {item["id"]: item for item in fixtures["edge_decisions"]}
    assert decisions["wait-empty"]["expected_calls"][0]["sample"] == 0
    assert decisions["search-skip"]["expected_calls"][0]["previous_sample"] is None
    assert decisions["simultaneous-alternatives"]["expected_calls"][0]["matched"] == [True, True]


def test_matrix_equivalence_is_named_source_specific_and_caps_cover_all_categories() -> None:
    rows = load("option-matrix.json")["rows"]
    assert len({row["id"] for row in rows}) == len(rows)
    semantic_rows = {
        (row["decoder"], row["option"], repr(row["value"]), row["rejection_rule"])
        for row in rows
        if row["disposition"] == "unsupported"
    }
    assert len(semantic_rows) == len([row for row in rows if row["disposition"] == "unsupported"])
    direct = {row["fixture"] for row in rows if row["disposition"] == "direct-fixture"}
    assert direct
    assert all(row["fixture"] for row in rows if row["disposition"] != "unsupported")
    assert all(
        row["equivalence_argument"] and "source" in row["equivalence_argument"]
        for row in rows
        if row["disposition"] == "static-equivalence"
    )


def test_static_wait_predicates_and_source_order_are_truthful() -> None:
    """Evaluate literal r/f/e/h/skip predicates without importing a decoder.

    This is deliberately stronger than pin-vector checking: the rejected B1
    candidates could normalize pins while still claiming false edge matches.
    """
    timelines = load("semantic-fixtures.json")["timelines"]
    channel_order = {
        "uart": ("rx", "tx"),
        "spi": ("clk", "miso", "mosi", "cs"),
        "i2c": ("scl", "sda"),
    }

    def matches(timeline: dict[str, object], condition: dict[str, object], sample: int) -> bool:
        if "skip" in condition:
            return True
        for index, wanted in condition.items():
            channel = channel_order[timeline["decoder"]][int(index)]
            if channel not in timeline["mapping"]:
                return False
            edges = timeline["transitions"][f"D{timeline['mapping'][channel]}"]
            current = level_at(edges, sample)
            previous = level_at(edges, sample - 1) if sample else current
            if wanted == "h" and current != 1:
                return False
            if wanted == "l" and current != 0:
                return False
            if wanted == "r" and not (previous == 0 and current == 1):
                return False
            if wanted == "f" and not (previous == 1 and current == 0):
                return False
            if wanted == "e" and previous == current:
                return False
        return True

    for timeline in timelines:
        for wait in timeline["expected_wait_trace"]:
            alternatives = (
                wait["condition"] if isinstance(wait["condition"], list) else [wait["condition"]]
            )
            actual = (
                [False] * len(alternatives)
                if wait.get("terminal") == "end-of-input failed wait"
                else [matches(timeline, item, wait["sample"]) for item in alternatives]
            )
            assert wait["matched"] == actual, (timeline["id"], wait, actual)
            assert 0 <= wait["sample"] <= timeline["sample_count"]
        assert timeline["expected_wait_trace"][-1].get("terminal") == "end-of-input failed wait"
        assert not any(timeline["expected_wait_trace"][-1]["matched"])

    by_id = {timeline["id"]: timeline for timeline in timelines}
    for ident in ("spi-mosi-mode0-word8", "spi-miso-mode3-word8"):
        records = by_id[ident]["expected_records"]
        assert [record["kind"] for record in records[:3]] == ["binary", "python", "python"]
        bits = records[1]["value"]["value"]
        assert bits[0]["value"] == "BITS"
        present = bits[1] if ident.startswith("spi-mosi") else bits[2]
        assert len(present["value"]) == 8
        assert [record["kind"] for record in records[3:12]] == ["annotation"] * 9
    uart = by_id["uart-parity-invalid-stop-break-idle-packet"]["expected_records"]
    packet_index = next(
        i
        for i, item in enumerate(uart)
        if item["kind"] == "python" and item["value"]["value"][0]["value"] == "PACKET"
    )
    assert packet_index < next(
        i
        for i, item in enumerate(uart)
        if item["kind"] == "python" and item["value"]["value"][0]["value"] == "PARITY ERROR"
    )
    repeated = by_id["i2c-unshifted-repeated-start"]
    assert any(
        wait["sample"] == 176 and wait["matched"] == [False, True, False]
        for wait in repeated["expected_wait_trace"]
    )
    # Continue the matrix/vector coverage audit with local data, keeping this
    # predicate test independent of test ordering.
    rows = load("option-matrix.json")["rows"]
    direct = {row["fixture"] for row in rows if row["disposition"] == "direct-fixture"}
    timelines = by_id
    assert all(
        row["fixture"] in direct for row in rows if row["disposition"] == "static-equivalence"
    )
    assert all(row["fixture"] in timelines for row in rows if row["disposition"] != "unsupported")
    tx = timelines["uart-tx-valid-default"]["expected_records"]
    assert tx[0]["value"]["value"][1]["value"] == 1
    assert any(record["value"].get("class_index") == 1 for record in tx)
    error_tags = {
        record["value"]["value"][0]["value"]
        for record in timelines["uart-parity-invalid-stop-break-idle-packet"]["expected_records"]
        if record["kind"] == "python"
    }
    assert {"PARITY ERROR", "INVALID STOPBIT", "BREAK", "IDLE", "FRAME"} <= error_tags
    assert {row["option"] for row in rows} >= {
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
        "cs_polarity",
        "cpol",
        "cpha",
        "bitorder",
        "wordsize",
        "address_format",
    }
    cap_ids = {item["id"] for item in load("experiment-caps.json")["caps"]}
    assert {
        "wall_deadline_ms",
        "terminate_grace_ms",
        "input_samples",
        "request_bytes",
        "output_records",
        "encoded_bytes",
        "decoded_bytes",
        "stdout_bytes",
        "stderr_bytes",
        "diagnostic_bytes",
        "text_bytes",
        "binary_bytes",
        "nested_depth",
        "nested_items",
        "retained_result_bytes",
        "recursion_limit",
        "worker_address_space_bytes",
    } <= cap_ids
    vectors = load("typed-vectors.json")
    assert vectors["schema"] == "pico-logic-analyzer.decode-result/v1"
    assert set(vectors["python_value_tags"]) == {
        "null",
        "bool",
        "integer",
        "float",
        "string",
        "bytes",
        "list",
        "tuple",
        "spi-data",
    }
    assert set(vectors["record_kinds"]) == {"annotation", "python", "binary", "metadata"}
    assert {vector["kind"] for vector in vectors["vectors"]} == {
        "annotation",
        "python",
        "binary",
        "metadata",
    }
    assert {vector["tag"] for vector in vectors["vectors"] if vector["kind"] == "python"} == set(
        vectors["python_value_tags"]
    )
    goldens = {
        golden["vector_id"]: bytes.fromhex(golden["hex"]) for golden in vectors["cli_utf8_goldens"]
    }
    assert set(goldens) == {vector["id"] for vector in vectors["vectors"]}
    for vector in vectors["vectors"]:
        assert (
            goldens[vector["id"]]
            == json.dumps(
                vector["object"],
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
                allow_nan=False,
            ).encode("utf-8")
            + b"\n"
        )
    caps = load("experiment-caps.json")
    assert (
        caps["enforcement_claim"]
        == "none; static experiment-only specification, not product thresholds"
    )
    assert all(isinstance(item["value"], int) and item["value"] > 0 for item in caps["caps"])
    assert {item["id"] for item in caps["caps"]} == {
        "wall_deadline_ms",
        "terminate_grace_ms",
        "input_samples",
        "request_bytes",
        "output_records",
        "encoded_bytes",
        "decoded_bytes",
        "stdout_bytes",
        "stderr_bytes",
        "diagnostic_bytes",
        "text_bytes",
        "binary_bytes",
        "nested_depth",
        "nested_items",
        "retained_result_bytes",
        "recursion_limit",
        "worker_address_space_bytes",
    }
    assert all(
        item["unit"]
        and item["domain"]
        and item["rationale"]
        and item["boundary"]["reject"] == item["value"] + 1
        for item in caps["caps"]
    )


def test_generator_is_static_and_contains_no_runtime_oracle() -> None:
    source = GENERATOR.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = {
        name.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for name in node.names
    } | {
        node.module.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    assert imports <= {"__future__", "argparse", "hashlib", "json", "pathlib"}
    assert "subprocess" not in source and "importlib" not in source
    manifest = load("manifest.json")
    assert manifest["generator_sha256"] == sha256(GENERATOR)
    assert all(
        item["sha256"] == sha256(DATA / item["path"])
        for item in manifest["artifacts"]
        if item["path"] != "manifest.json"
    )
