from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parents[2]
DATA = ROOT / "testdata" / "decoders" / "cycle3"


def load(name: str) -> object:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def level_at(transitions: list[list[int]], sample: int) -> int:
    applicable = [level for at, level in transitions if at <= sample]
    assert applicable, f"no declared level at sample {sample}"
    return applicable[-1]


def test_timelines_define_a_finite_capture_boundary() -> None:
    """EOI and boundary records cannot be reviewed without an exact sample count."""
    timelines = load("semantic-fixtures.json")["timelines"]
    assert all(
        isinstance(timeline.get("sample_count"), int) and timeline["sample_count"] > 0
        for timeline in timelines
    )


def test_wait_pin_vectors_match_declared_transitions() -> None:
    """Every mapped pin returned by a wait must equal its timeline at that sample."""
    channel_order = {
        "uart": ("rx", "tx"),
        "spi": ("clk", "miso", "mosi", "cs"),
        "i2c": ("scl", "sda"),
    }
    timelines = load("semantic-fixtures.json")["timelines"]
    discrepancies: list[str] = []
    for timeline in timelines:
        for wait_index, wait in enumerate(timeline["expected_wait_trace"]):
            for pin_index, decoder_channel in enumerate(channel_order[timeline["decoder"]]):
                physical = timeline["mapping"].get(decoder_channel)
                expected = 255
                if physical is not None:
                    expected = level_at(timeline["transitions"][f"D{physical}"], wait["sample"])
                actual = wait["pins"][pin_index]
                if actual != expected:
                    discrepancies.append(
                        f"{timeline['id']} wait {wait_index} sample {wait['sample']} "
                        f"{decoder_channel}: expected {expected}, got {actual}"
                    )
    assert not discrepancies, "\n".join(discrepancies)


def test_spi_records_follow_the_static_putdata_branch() -> None:
    """The checked-in SPI putdata() branch emits binary, BITS, DATA, then annotations."""
    timelines = {
        timeline["id"]: timeline
        for timeline in load("semantic-fixtures.json")["timelines"]
    }
    for fixture_id in ("spi-mosi-mode0-word8", "spi-miso-mode3-word8"):
        records = timelines[fixture_id]["expected_records"]
        kinds = [record["kind"] for record in records]
        assert kinds[:3] == ["binary", "python", "python"]
        python_commands = [
            record["value"]["value"][0]["value"]
            for record in records
            if record["kind"] == "python"
        ]
        assert python_commands[:2] == ["BITS", "DATA"]
        assert sum(record["kind"] == "annotation" for record in records) >= 9


def test_named_uart_packet_and_i2c_repeated_start_branches_are_present() -> None:
    timelines = {
        timeline["id"]: timeline
        for timeline in load("semantic-fixtures.json")["timelines"]
    }
    uart_commands = {
        record["value"]["value"][0]["value"]
        for record in timelines[
            "uart-parity-invalid-stop-break-idle-packet"
        ]["expected_records"]
        if record["kind"] == "python"
    }
    assert "PACKET" in uart_commands

    i2c_commands = [
        record["value"]["value"][0]["value"]
        for record in timelines["i2c-unshifted-repeated-start"]["expected_records"]
        if record["kind"] == "python"
    ]
    assert "START REPEAT" in i2c_commands


def test_matrix_direct_rows_name_fixtures_that_materialize_the_row_value() -> None:
    """A direct linkage must be evidenced by the named fixture, not its name alone."""
    timelines = {
        timeline["id"]: timeline
        for timeline in load("semantic-fixtures.json")["timelines"]
    }
    defaults = {
        "uart": {
            "baudrate": 115200,
            "data_bits": 8,
            "parity": "none",
            "stop_bits": 1.0,
            "bit_order": "lsb-first",
            "format": "hex",
            "invert_rx": "no",
            "invert_tx": "no",
            "sample_point": 50,
            "rx_packet_delim": -1,
            "tx_packet_delim": -1,
            "rx_packet_len": -1,
            "tx_packet_len": -1,
        },
        "spi": {
            "cs_polarity": "active-low",
            "cpol": 0,
            "cpha": 0,
            "bitorder": "msb-first",
            "wordsize": 8,
        },
        "i2c": {"address_format": "shifted"},
    }
    discrepancies: list[str] = []
    for row in load("option-matrix.json")["rows"]:
        if row["disposition"] != "direct-fixture":
            continue
        timeline = timelines[row["fixture"]]
        materialized = {**defaults[row["decoder"]], **timeline["options"]}
        if materialized.get(row["option"]) != row["value"]:
            discrepancies.append(
                f"{row['id']} -> {row['fixture']} materializes "
                f"{materialized.get(row['option'])!r}, not {row['value']!r}"
            )
    assert not discrepancies, "\n".join(discrepancies)


def test_static_equivalence_arguments_are_option_specific() -> None:
    rows = [
        row
        for row in load("option-matrix.json")["rows"]
        if row["disposition"] == "static-equivalence"
    ]
    by_argument: dict[str, set[str]] = {}
    for row in rows:
        by_argument.setdefault(row["equivalence_argument"], set()).add(row["option"])
    assert all(len(options) == 1 for options in by_argument.values()), by_argument


def test_cap_values_have_value_specific_independent_rationales() -> None:
    caps = load("experiment-caps.json")["caps"]
    assert len({cap["rationale"] for cap in caps}) == len(caps)
    assert all(str(cap["value"]) in cap["rationale"] for cap in caps)
