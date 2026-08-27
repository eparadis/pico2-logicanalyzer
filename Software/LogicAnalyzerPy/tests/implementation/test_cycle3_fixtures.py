from __future__ import annotations

import ast
import base64
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


def test_static_spi_bit_span_recurrence_and_i2c_bitrate_arithmetic() -> None:
    """Keep two source recurrences reviewable without invoking a decoder.

    spi.handle_bit() inserts newest-first, estimates ``es`` from the prior
    newest start, then closes the prior newest entry at the current sample.
    Thus sampling at 10..150 has final newest [150, 170], not [150, 290].
    I2C increments pdu_bits in handle_address_or_data only: its two octets
    plus the post-NACK partial bit at SCL 370 are 17 increments; ACK/NACK
    use get_ack and do not increment it.
    """
    bits: list[list[int]] = []
    for sample in range(10, 151, 20):
        end = sample if not bits else sample + sample - bits[0][1]
        bits.insert(0, [1, sample, end])
        if len(bits) > 1:
            bits[1][2] = sample
    assert bits[0] == [1, 150, 170]
    assert int(1_152_000 * 17 / 371) == 52_787


def test_uart_i2c_use_ordinary_bit_lists_and_v1_binds_real_decoder_sets() -> None:
    fixtures = load("semantic-fixtures.json")

    def tags(value: object) -> set[str]:
        if isinstance(value, list):
            return set().union(*(tags(item) for item in value)) if value else set()
        if not isinstance(value, dict):
            return set()
        return ({value["tag"]} if "tag" in value else set()) | set().union(
            *(tags(item) for item in value.values())
        )

    for timeline in fixtures["timelines"]:
        observed = tags(timeline["expected_records"])
        if timeline["decoder"] == "spi":
            continue
        assert "spi-data" not in observed
    provenance = load("provenance.json")
    sets = {entry["decoder"]: entry for entry in provenance["decoder_file_sets"]}
    assert set(sets) == {"uart", "spi", "i2c"}
    assert all(len(entry["sha256"]) == 64 and entry["paths"] for entry in sets.values())
    vectors = load("typed-vectors.json")["vectors"]
    for vector in vectors:
        root = vector["object"]
        decoder = root["decoder"]["id"]
        assert root["decoder"]["file_set_sha256"] == sets[decoder]["sha256"]
        assert root["declarations"]
        assert root["options"]
    error = next(
        item
        for item in fixtures["timelines"]
        if item["id"] == "uart-parity-invalid-stop-break-idle-packet"
    )
    assert "PACKET" not in [
        record["value"]["value"][0]["value"]
        for record in error["expected_records"]
        if record["kind"] == "python"
    ]


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
        "common.srdhelper.mod (relative package import .mod)",
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
        (
            row["decoder"],
            row["option"],
            repr(row["value"]),
            row["rejection_rule"],
            repr(row.get("selected_width_context")),
        )
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
    delimiter_rows = [
        row
        for row in rows
        if row["decoder"] == "uart" and row["option"] in {"rx_packet_delim", "tx_packet_delim"}
    ]
    assert not any("_packet_delim_width_" in row["option"] for row in rows)
    timelines = {
        timeline["id"]: timeline for timeline in load("semantic-fixtures.json")["timelines"]
    }
    for direction in ("rx", "tx"):
        option = f"{direction}_packet_delim"
        for width in range(5, 10):
            maximum = (1 << width) - 1
            accepted = next(
                row
                for row in delimiter_rows
                if row["option"] == option
                and row["value"] == maximum
                and row["disposition"] == "direct-fixture"
                and row.get("selected_width_context") == {"data_bits": width}
            )
            assert accepted["fixture"]
            timeline = timelines[accepted["fixture"]]
            assert timeline["options"][option] == maximum
            assert timeline["options"]["data_bits"] == width
            assert timeline["mapping"] == {direction: 4}
            data = next(
                record
                for record in timeline["expected_records"]
                if record["kind"] == "python" and record["value"]["value"][0]["value"] == "DATA"
            )
            assert data["value"]["value"][1]["value"] == (1 if direction == "tx" else 0)
            assert data["value"]["value"][2]["value"][0]["value"] == maximum
            triples = data["value"]["value"][2]["value"][1]["value"]
            assert len(triples) == width
            assert [triple["value"][0]["value"] for triple in triples] == [1] * width
            expected_b64 = base64.b64encode(
                maximum.to_bytes((width + 7) // 8, byteorder="big")
            ).decode("ascii")
            assert [
                record["value"]["data_base64"]
                for record in timeline["expected_records"]
                if record["kind"] == "binary"
            ] == [expected_b64, expected_b64]
            assert any(
                record["kind"] == "annotation"
                and record["value"].get("class_index") == 16 + (direction == "tx")
                for record in timeline["expected_records"]
            )
            assert any(
                row["option"] == option
                and row["value"] == maximum + 1
                and row["disposition"] == "unsupported"
                and row.get("selected_width_context") == {"data_bits": width}
                for row in delimiter_rows
            )


def test_direct_option_witnesses_bind_value_to_stimulus_wait_and_output() -> None:
    """A direct row cannot pass merely because its ID/options were renamed.

    The source fixture generator gives every direct row an independently
    placed finite trace and a final source-branch emission.  This check binds
    the matrix value to all three observable layers and rejects a future
    baseline deep-copy whose expected output happens to look plausible.
    """
    rows = [
        row for row in load("option-matrix.json")["rows"] if row["disposition"] == "direct-fixture"
    ]
    timelines = {
        timeline["id"]: timeline for timeline in load("semantic-fixtures.json")["timelines"]
    }
    direct_rows = [row for row in rows if row["fixture"].startswith("direct-")]
    assert direct_rows
    for row in direct_rows:
        timeline = timelines[row["fixture"]]
        assert timeline["options"][row["option"]] == row["value"]
        # Input edge positions and waits are literal protocol timing, while
        # DATA/format/parity/stop/packet records appear in source state order.
        edges = tuple(
            (channel, tuple(tuple(edge) for edge in values))
            for channel, values in sorted(timeline["transitions"].items())
        )
        waits = tuple(wait["sample"] for wait in timeline["expected_wait_trace"])
        assert min(edge[0] for _, values in edges for edge in values if edge[0]) > 0
        assert max(waits) > 1
        records = timeline["expected_records"]
        assert [item["emission_index"] for item in records] == list(range(len(records)))
        tags = [item["value"]["value"][0]["value"] for item in records if item["kind"] == "python"]
        if row["decoder"] == "uart":
            assert tags.index("DATA") < tags.index("FRAME")
            width = timeline["samplerate_hz"] // int(timeline["options"].get("baudrate", 115200))
            bits_n = int(timeline["options"].get("data_bits", 8))
            frame_start = timeline["transitions"]["D4"][1][0]
            point = int(timeline["options"].get("sample_point", 50))
            stop_bits = float(timeline["options"].get("stop_bits", 1.0))
            slots = 1 + bits_n + int(timeline["options"].get("parity", "none") != "none")
            slots += 0 if stop_bits == 0 else int(stop_bits) + int(stop_bits != int(stop_bits))
            centres = [
                frame_start + ((width - 1) * point + 99) // 100 + slot * width
                for slot in range(slots)
            ]
            waits = timeline["expected_wait_trace"]
            raw_start = (
                "r"
                if timeline["options"].get("invert_rx") == "yes"
                or timeline["options"].get("invert_tx") == "yes"
                else "f"
            )
            assert (
                waits[0]["condition"][0]["0" if "rx" in timeline["mapping"] else "1"] == raw_start
            )
            centre_waits = [
                wait
                for wait in waits[1:-1]
                if wait["matched"][0] and "skip" in wait["condition"][0]
            ]
            assert [wait["sample"] for wait in centre_waits] == centres
            frame_len = int(
                (1 + bits_n + (timeline["options"].get("parity", "none") != "none") + stop_bits)
                * width
            )
            terminal = waits[-1]
            assert len(terminal["condition"]) == 3
            assert terminal["condition"][2]["skip"] == frame_start + 2 * frame_len - centres[-1]
            half_floor, half_ceil = width // 2, (width + 1) // 2
            start = records[0]
            assert (start["start_sample"], start["end_sample"]) == (
                centres[0] - half_floor,
                centres[0] + half_ceil,
            )
            data_record = next(
                item
                for item in records
                if item["kind"] == "python" and item["value"]["value"][0]["value"] == "DATA"
            )
            assert (data_record["start_sample"], data_record["end_sample"]) == (
                centres[1] - half_floor,
                centres[bits_n] + half_ceil,
            )
            frame = next(
                item
                for item in records
                if item["kind"] == "python" and item["value"]["value"][0]["value"] == "FRAME"
            )
            assert frame["end_sample"] == centres[-1] + half_ceil
        if row["decoder"] == "uart" and row["option"] == "parity" and row["value"] != "none":
            assert tags.index("PARITYBIT") > tags.index("DATA")
        if row["decoder"] == "uart" and row["option"] == "stop_bits" and row["value"] != 0.0:
            assert tags.index("STOPBIT") > tags.index("DATA")
        if row["option"].endswith("packet_len") and row["value"] == 1:
            assert any(item["value"].get("class_index") in {16, 17} for item in records)
    # The snapshot uses ceil() for sample centres: 10 samples/bit at 50%
    # therefore samples the start slot at 6, not the floor value 5.
    default_uart = timelines["direct-uart-parity-none"]
    assert default_uart["expected_wait_trace"][1]["sample"] == 15
    active_low = timelines["direct-spi-cs_polarity-activeneglow"]
    cs_tags = [
        item["value"]["value"][0]["value"]
        for item in active_low["expected_records"]
        if item["kind"] == "python"
    ]
    assert cs_tags[0] == "CS-CHANGE" and cs_tags[-2:] == ["CS-CHANGE", "TRANSFER"]
    transfer = active_low["expected_records"][-1]["value"]["value"][1]
    assert transfer["value"] == [{"tag": "spi-data", "ss": 10, "es": 170, "val": 165}]
    for ident in (
        "spi-mosi-mode0-word8",
        "spi-miso-mode3-word8",
        "direct-spi-bitorder-msbnegfirst",
        "direct-spi-cs_polarity-activeneglow",
    ):
        timeline = timelines[ident]
        assert timeline["expected_wait_trace"][-1]["sample"] == timeline["sample_count"]
        assert timeline["sample_count"] == max(
            item["end_sample"] for item in timeline["expected_records"]
        )
    for value in (0, 255, 511):
        timeline = timelines[f"direct-uart-rx_packet_delim-{str(value).replace('-', 'neg')}"]
        data = next(
            item
            for item in timeline["expected_records"]
            if item["kind"] == "python" and item["value"]["value"][0]["value"] == "DATA"
        )
        assert data["value"]["value"][2]["value"][0]["value"] == value
        assert any(item["value"].get("class_index") == 16 for item in timeline["expected_records"])
    delimiter_511 = timelines["direct-uart-rx_packet_delim-511"]
    assert delimiter_511["options"]["data_bits"] == 9
    binary = [item for item in delimiter_511["expected_records"] if item["kind"] == "binary"]
    assert [item["value"]["data_base64"] for item in binary] == ["Af8=", "Af8="]
    nine = timelines["direct-uart-data_bits-9"]
    nine_tags = [
        item["value"]["value"][0]["value"]
        for item in nine["expected_records"]
        if item["kind"] == "python"
    ]
    assert nine_tags[-1] == "FRAME" and nine_tags.index("DATA") < nine_tags.index("FRAME")
    assert [
        item["value"]["data_base64"]
        for item in nine["expected_records"]
        if item["kind"] == "binary"
    ] == ["AKU=", "AKU="]
    msb = timelines["direct-uart-bit_order-msbnegfirst"]
    msb_data = next(
        item
        for item in msb["expected_records"]
        if item["kind"] == "python" and item["value"]["value"][0]["value"] == "DATA"
    )
    assert msb_data["value"]["value"][2]["value"][0]["value"] == 163
    p99 = timelines["direct-uart-sample_point-99"]
    assert p99["expected_wait_trace"][1]["sample"] == 19
    even = timelines["direct-uart-parity-even"]
    assert any(
        item["value"]["value"][0]["value"] == "PARITYBIT"
        for item in even["expected_records"]
        if item["kind"] == "python"
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

    def matches(
        timeline: dict[str, object], condition: dict[str, object], sample: int, previous: int
    ) -> bool:
        if "skip" in condition:
            return sample - previous == condition["skip"]
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
        previous = 0
        for wait_index, wait in enumerate(timeline["expected_wait_trace"]):
            alternatives = (
                wait["condition"] if isinstance(wait["condition"], list) else [wait["condition"]]
            )
            actual = (
                [False] * len(alternatives)
                if wait.get("terminal") == "end-of-input failed wait"
                else [matches(timeline, item, wait["sample"], previous) for item in alternatives]
            )
            assert wait["matched"] == actual, (timeline["id"], wait, actual)
            if wait.get("terminal") != "end-of-input failed wait":
                # A wait must return the first sample at or after the prior
                # return where *any* alternative can match. This catches a
                # tempting but false trace that jumps straight to a scheduled
                # UART centre while a generic edge is earlier.
                first = previous if wait_index == 0 else previous + 1
                earliest = next(
                    sample
                    for sample in range(first, wait["sample"] + 1)
                    if any(matches(timeline, item, sample, previous) for item in alternatives)
                )
                assert earliest == wait["sample"], (timeline["id"], previous, wait, earliest)
            assert 0 <= wait["sample"] <= timeline["sample_count"]
            previous = wait["sample"]
        assert timeline["expected_wait_trace"][-1].get("terminal") == "end-of-input failed wait"
        assert not any(timeline["expected_wait_trace"][-1]["matched"])

    by_id = {timeline["id"]: timeline for timeline in timelines}
    for ident in (
        "uart-rx-valid-default",
        "uart-tx-valid-default",
        "uart-parity-invalid-stop-break-idle-packet",
        "uart-break-low-interval",
        "uart-idle-after-valid-frame",
    ):
        timeline = by_id[ident]
        terminal = timeline["expected_wait_trace"][-1]
        prior = timeline["expected_wait_trace"][-2]["sample"]
        assert len(terminal["condition"]) == 3
        assert prior + terminal["condition"][2]["skip"] >= timeline["sample_count"]
    incomplete_uart = by_id["uart-msb-9bit-boundary-incomplete"]
    incomplete_terminal = incomplete_uart["expected_wait_trace"][-1]
    assert len(incomplete_terminal["condition"]) == 2
    assert "skip" in incomplete_terminal["condition"][0]
    assert incomplete_terminal["condition"][1] == {"0": "e"}
    idle_returns = [
        wait["sample"]
        for wait in by_id["uart-idle-after-valid-frame"]["expected_wait_trace"]
        if len(wait["condition"]) == 3 and wait["matched"] == [False, False, True]
    ]
    assert idle_returns == [201]
    for ident in ("spi-mosi-mode0-word8", "spi-miso-mode3-word8"):
        records = by_id[ident]["expected_records"]
        assert [record["kind"] for record in records[:4]] == [
            "python",
            "binary",
            "python",
            "python",
        ]
        assert records[0]["value"]["value"][0]["value"] == "CS-CHANGE"
        bits = records[2]["value"]["value"]
        assert bits[0]["value"] == "BITS"
        present = bits[1] if ident.startswith("spi-mosi") else bits[2]
        assert len(present["value"]) == 8
        assert [record["kind"] for record in records[4:13]] == ["annotation"] * 9
    uart = by_id["uart-parity-invalid-stop-break-idle-packet"]["expected_records"]
    assert not any(
        item["kind"] == "python" and item["value"]["value"][0]["value"] == "PACKET"
        for item in uart
    )
    repeated = by_id["i2c-unshifted-repeated-start"]
    assert any(
        wait["sample"] == 216 and wait["matched"] == [False, True, False]
        for wait in repeated["expected_wait_trace"]
    )
    full_i2c = by_id["i2c-shifted-start-address-ack-data-nack-stop"]
    i2c_bits = [
        item
        for item in full_i2c["expected_records"]
        if item["kind"] == "python" and item["value"]["value"][0]["value"] == "BITS"
    ]
    bit_values = [
        [entry["value"][0]["value"] for entry in item["value"]["value"][1]["value"]]
        for item in i2c_bits
    ]
    assert bit_values == [
        [0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0],
    ]
    assert [(item["start_sample"], item["end_sample"]) for item in i2c_bits] == [
        (10, 170),
        (190, 350),
    ]
    assert full_i2c["expected_records"][-2]["kind"] == "python"
    assert full_i2c["expected_records"][-3]["value"]["value"] == 52787
    # Continue the matrix/vector coverage audit with local data, keeping this
    # predicate test independent of test ordering.
    rows = load("option-matrix.json")["rows"]
    direct = {row["fixture"] for row in rows if row["disposition"] == "direct-fixture"}
    timelines = by_id
    assert all(
        row["fixture"] in direct for row in rows if row["disposition"] == "static-equivalence"
    )
    assert all(row["fixture"] in timelines for row in rows if row["disposition"] != "unsupported")
    assert all(
        timelines[row["fixture"]]["options"].get(row["option"]) == row["value"]
        for row in rows
        if row["disposition"] == "direct-fixture"
    )
    tx = timelines["uart-tx-valid-default"]["expected_records"]
    assert tx[0]["value"]["value"][1]["value"] == 1
    assert any(record["value"].get("class_index") == 1 for record in tx)
    rx = timelines["uart-rx-valid-default"]["expected_records"]
    assert [record["value"]["texts"][0] for record in rx[2:10]] == list("10100101")
    assert [(record["start_sample"], record["end_sample"]) for record in rx[2:10]] == [
        (11 + 10 * index, 21 + 10 * index) for index in range(8)
    ]
    assert [record["kind"] for record in rx[10:14]] == ["python", "annotation", "binary", "binary"]
    error_tags = {
        record["value"]["value"][0]["value"]
        for record in timelines["uart-parity-invalid-stop-break-idle-packet"]["expected_records"]
        if record["kind"] == "python"
    }
    assert {"DATA", "PARITY ERROR", "INVALID STOPBIT", "STOPBIT", "FRAME"} <= error_tags
    assert "BREAK" not in error_tags and "IDLE" not in error_tags
    break_records = timelines["uart-break-low-interval"]["expected_records"]
    assert [
        item["value"]["value"][0]["value"] for item in break_records if item["kind"] == "python"
    ][-1] == "BREAK"
    break_data = next(
        item
        for item in break_records
        if item["kind"] == "python" and item["value"]["value"][0]["value"] == "DATA"
    )
    break_triples = break_data["value"]["value"][2]["value"][1]["value"]
    assert [triple["value"][0]["value"] for triple in break_triples] == [0] * 8
    idle_records = timelines["uart-idle-after-valid-frame"]["expected_records"]
    assert idle_records[-1]["value"]["value"][0]["value"] == "IDLE"
    assert (idle_records[-1]["start_sample"], idle_records[-1]["end_sample"]) == (101, 201)
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
        root = vector["object"]
        for item in root["records"]:
            for stamp in (item["start_time"], item["end_time"]):
                assert stamp["absolute"]["denominator"] == root["samplerate_hz"]
                assert stamp["trigger_relative"]["denominator"] == root["samplerate_hz"]
                assert stamp["trigger_relative"]["numerator"] == (
                    stamp["absolute"]["numerator"] - root["capture"]["trigger_index"]
                )
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
    input_cap = next(item for item in caps["caps"] if item["id"] == "input_samples")
    corpus_max = max(item["sample_count"] for item in load("semantic-fixtures.json")["timelines"])
    assert input_cap["value"] >= corpus_max * 256
    assert f"basis_value={corpus_max}" in input_cap["rationale"]
    assert "multiplier=256" in input_cap["rationale"] and "floor=100000" in input_cap["rationale"]
    assert (
        caps["enforcement_claim"]
        == "none; static experiment-only specification, not product thresholds"
    )
    assert all(isinstance(item["value"], int) and item["value"] > 0 for item in caps["caps"])
    assert all(
        item["boundary"] == {"accept": item["value"], "reject": item["value"] + 1}
        and "basis_category=" in item["rationale"]
        and "No macOS observation" in item["rationale"]
        for item in caps["caps"]
    )
    for item in caps["caps"]:
        derivation = item["derivation"]
        computed = derivation["basis_value"] * derivation["multiplier"]
        if derivation["operation"] == "max-floor":
            computed = max(computed, derivation["floor"])
        assert derivation["operation"] in {"multiply", "max-floor"}
        assert derivation["result"] == computed == item["value"]
        assert not (derivation["basis_value"] == item["value"] and derivation["multiplier"] == 1)
        for field in (
            "operation",
            "basis_category",
            "basis_value",
            "multiplier",
            "floor",
            "result",
        ):
            assert f"{field}={derivation[field]}" in item["rationale"]
        assert str(item["value"]) in item["rationale"]
    by_cap = {item["id"]: item for item in caps["caps"]}
    assert (
        by_cap["stderr_bytes"]["derivation"]["basis_value"] == by_cap["diagnostic_bytes"]["value"]
    )
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
    assert imports <= {"__future__", "argparse", "copy", "hashlib", "json", "pathlib"}
    assert "subprocess" not in source and "importlib" not in source
    manifest = load("manifest.json")
    assert manifest["generator_sha256"] == sha256(GENERATOR)
    assert all(
        item["sha256"] == sha256(DATA / item["path"])
        for item in manifest["artifacts"]
        if item["path"] != "manifest.json"
    )
