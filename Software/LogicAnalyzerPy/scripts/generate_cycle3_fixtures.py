#!/usr/bin/env python3
# ruff: noqa: E501
"""Build inert Cycle 3 B1 fixture data from literals authored in this file.

This is deliberately stdlib-only and never imports/executes a host or decoder.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
OUT = ROOT / "testdata" / "decoders" / "cycle3"


FILES = [
    (
        "Software/decoders/sigrokdecode.py",
        "385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a",
    ),
    (
        "Software/decoders/uart/__init__.py",
        "351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f",
    ),
    (
        "Software/decoders/uart/pd.py",
        "67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc",
    ),
    (
        "Software/decoders/spi/__init__.py",
        "91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c",
    ),
    (
        "Software/decoders/spi/pd.py",
        "ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d",
    ),
    (
        "Software/decoders/i2c/__init__.py",
        "37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f",
    ),
    (
        "Software/decoders/i2c/pd.py",
        "b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305",
    ),
    (
        "Software/decoders/common/srdhelper/__init__.py",
        "125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1",
    ),
    (
        "Software/decoders/common/srdhelper/mod.py",
        "602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6",
    ),
]


def canonical(value: object) -> bytes:
    return (
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
        ).encode()
        + b"\n"
    )


def option_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    defaults = {
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
        "cs_polarity": "active-low",
        "cpol": 0,
        "cpha": 0,
        "bitorder": "msb-first",
        "wordsize": 8,
        "address_format": "shifted",
    }
    defs = {
        "uart": {
            "baudrate": [1, 115200],
            "data_bits": [5, 6, 7, 8, 9],
            "parity": ["none", "odd", "even", "zero", "one", "ignore"],
            "stop_bits": [0.0, 0.5, 1.0, 1.5, 2.0],
            "bit_order": ["lsb-first", "msb-first"],
            "format": ["ascii", "dec", "hex", "oct", "bin"],
            "invert_rx": ["yes", "no"],
            "invert_tx": ["yes", "no"],
            "sample_point": [1, 50, 99],
            "rx_packet_delim": [-1, 0, 255, 511],
            "tx_packet_delim": [-1, 0, 255, 511],
            "rx_packet_len": [-1, 1],
            "tx_packet_len": [-1, 1],
        },
        "spi": {
            "cs_polarity": ["active-low", "active-high"],
            "cpol": [0, 1],
            "cpha": [0, 1],
            "bitorder": ["msb-first", "lsb-first"],
            "wordsize": [1, 8],
        },
        "i2c": {"address_format": ["shifted", "unshifted"]},
    }
    for decoder, options in defs.items():
        for option, values in options.items():
            for value in values:
                value_id = str(value).replace(".", "p").replace("-", "neg")
                direct_cases = {
                    ("uart", "baudrate", 115200): "uart-rx-valid-default",
                    ("uart", "invert_tx", "no"): "uart-tx-valid-default",
                    ("spi", "cpol", 0): "spi-mosi-mode0-word8",
                    ("spi", "cpha", 0): "spi-mosi-mode0-word8",
                    ("spi", "wordsize", 8): "spi-mosi-mode0-word8",
                    ("spi", "cpol", 1): "spi-miso-mode3-word8",
                    ("spi", "cpha", 1): "spi-miso-mode3-word8",
                    ("spi", "cs_polarity", "active-high"): "spi-cs-active-high-lsb-word1",
                    ("spi", "bitorder", "lsb-first"): "spi-cs-active-high-lsb-word1",
                    ("spi", "wordsize", 1): "spi-cs-active-high-lsb-word1",
                    (
                        "i2c",
                        "address_format",
                        "shifted",
                    ): "i2c-shifted-start-address-ack-data-nack-stop",
                    ("i2c", "address_format", "unshifted"): "i2c-unshifted-repeated-start",
                }
                # Every accepted value receives a fixture whose option object
                # literally contains that value.  A source-citation paragraph
                # is useful review context, but it is never a substitute for
                # an executable-shaped direct witness when the option changes
                # a state, timing, formatting, or output branch.
                direct_fixture = direct_cases.get(
                    (decoder, option, value), f"direct-{decoder}-{option}-{value_id}"
                )
                rows.append(
                    {
                        "id": f"{decoder}-{option}-{value_id}",
                        "decoder": decoder,
                        "option": option,
                        "value": value,
                        "classification": "default"
                        if value == defaults[option]
                        else "accepted-enumeration-or-inclusive-boundary",
                        "disposition": "direct-fixture",
                        "fixture": direct_fixture,
                        "equivalence_argument": None,
                        "rejection_rule": None,
                    }
                )
    rejected = [
        ("uart", "sample_point", 0, "integer 1..99"),
        ("uart", "sample_point", 100, "integer 1..99"),
        ("uart", "rx_packet_len", 0, "-1 or positive integer"),
        ("uart", "tx_packet_len", -2, "-1 or positive integer"),
        ("uart", "rx_packet_delim", -2, "-1 or non-negative width value"),
        ("uart", "rx_packet_delim", 512, "outside selected 9-bit width"),
        ("spi", "wordsize", 9, "unsupported until later approved maximum"),
        ("i2c", "address_format", "wide", "shifted or unshifted"),
        ("uart", "baudrate", True, "bool is not integer"),
        ("uart", "unknown", 1, "unknown option"),
        ("uart", "duplicate-cli", 1, "duplicate CLI assignment"),
    ]
    # Prelaunch rejections are intentionally type-distinguished: JSON true,
    # string, null and numeric values must never collapse to one matrix row.
    rejected += (
        [("uart", "baudrate", value, "positive integer") for value in (0, -1, "115200")]
        + [("uart", "data_bits", value, "one of integer 5..9") for value in (4, 10, True, "8")]
        + [
            ("uart", "stop_bits", value, "one of declared finite stop-bit values")
            for value in (0.25, "1", True, "NaN", "Infinity")
        ]
        + [("uart", "sample_point", value, "integer 1..99") for value in (True, "50", 1.5)]
    )
    for direction in ("rx", "tx"):
        for width in (5, 6, 7, 8, 9):
            maximum = (1 << width) - 1
            rejected += [
                (
                    "uart",
                    f"{direction}_packet_delim_width_{width}",
                    maximum + 1,
                    f"data_bits={width} maximum {maximum}",
                ),
                (
                    "uart",
                    f"{direction}_packet_delim_width_{width}",
                    -2,
                    "-1 or non-negative integer",
                ),
                ("uart", f"{direction}_packet_delim_width_{width}", "1", "integer, not string"),
            ]
        rejected += [
            ("uart", f"{direction}_packet_len", value, "-1 or positive integer")
            for value in (0, -2, "1", True)
        ]
    for option in ("parity", "bit_order", "format", "invert_rx", "invert_tx"):
        rejected += [
            ("uart", option, value, "declared enum string") for value in ("invalid", 1, True)
        ]
    for option in ("cs_polarity", "bitorder"):
        rejected += [
            ("spi", option, value, "declared enum string") for value in ("invalid", 1, True)
        ]
    for option in ("cpol", "cpha"):
        rejected += [("spi", option, value, "integer 0 or 1") for value in (-1, 2, True, "1")]
    rejected += [
        ("spi", "wordsize", value, "positive integer; >8 preapproval unsupported")
        for value in (0, True, "8", 9)
    ]
    rejected += [
        ("i2c", "address_format", value, "shifted or unshifted string")
        for value in (1, True, None, "wide")
    ]
    rejected += [
        (decoder, "unknown", "unknown", "unknown option") for decoder in ("uart", "spi", "i2c")
    ]
    rejected += [
        (decoder, "duplicate-cli", option, "duplicate CLI assignment")
        for decoder, option in (("uart", "baudrate"), ("spi", "cpol"), ("i2c", "address_format"))
    ]
    # The baseline and exhaustive tables deliberately overlap at a few
    # boundaries. Keep one semantic row, rather than assigning duplicate IDs.
    unique_rejected: list[tuple[str, str, object, str]] = []
    seen_rejected: set[tuple[str, str, str]] = set()
    for entry in rejected:
        semantic_key = (entry[0], entry[1], repr(entry[2]))
        if semantic_key not in seen_rejected:
            seen_rejected.add(semantic_key)
            unique_rejected.append(entry)
    for decoder, option, value, rule in unique_rejected:
        type_id = "null" if value is None else type(value).__name__.replace("bool", "boolean")
        rows.append(
            {
                "id": f"reject-{decoder}-{option}-{type_id}-{str(value).lower().replace('.', 'p')}",
                "decoder": decoder,
                "option": option,
                "value": value,
                "classification": "exclusive-boundary-sentinel-or-prelaunch-type",
                "disposition": "unsupported",
                "fixture": None,
                "equivalence_argument": None,
                "rejection_rule": rule,
            }
        )
    source_equivalence = {
        "baudrate": "uart.Decoder.metadata() sets bit_width=samplerate/baudrate; the fixture uses the same integral 10-sample invariant only for value 115200",
        "data_bits": "uart.get_data_bits() compares cur_data_bit with options['data_bits']; the named direct fixture materializes the same completed-width branch",
        "parity": "uart.advance_state() bypasses GET PARITY BIT only when parity=='none'; the named fixture directly fixes that bypass",
        "stop_bits": "uart.get_stop_bits() waits until len(stopbits) reaches options['stop_bits']; the named fixture directly fixes the one-stop completion branch",
        "bit_order": "uart.get_data_bits() reverses bits only for 'msb-first'; the named direct fixture fixes the alternative ordering branch",
        "format": "uart.format_value() selects ascii/dec/hex/oct/bin after the data value is fixed; the named fixture fixes the same value and output ordering",
        "invert_rx": "uart.decode() derives inv[RX] from options['invert_rx'] before get_wait_cond()/inspect_sample; the named RX fixture fixes the non-inverted branch",
        "invert_tx": "uart.decode() derives inv[TX] from options['invert_tx'] before get_wait_cond()/inspect_sample; the named TX fixture fixes the non-inverted branch",
        "sample_point": "uart.get_sample_point() computes ceil(frame_start + bitnum*bit_width + (bit_width-1)*percent/100); the named fixture fixes the default 50% branch",
        "rx_packet_delim": "uart.handle_packet() compares datavalue against options['rx_packet_delim']; the packet fixture directly materializes delimiter 165",
        "tx_packet_delim": "uart.handle_packet() compares datavalue against options['tx_packet_delim']; the TX fixture keeps the disabled sentinel branch",
        "rx_packet_len": "uart.handle_packet() compares len(packet_cache) against options['rx_packet_len']; the packet fixture directly materializes length 1",
        "tx_packet_len": "uart.handle_packet() compares len(packet_cache) against options['tx_packet_len']; the TX fixture keeps the disabled sentinel branch",
        "cs_polarity": "spi.cs_asserted() selects cs==0 versus cs==1 from options['cs_polarity']; the active-high one-bit fixture materializes the alternative",
        "cpol": "spi.find_clk_edge() selects mode through spi_mode[(cpol,cpha)]; mode0 and mode3 direct fixtures materialize both accepted values",
        "cpha": "spi.find_clk_edge() selects mode through spi_mode[(cpol,cpha)]; mode0 and mode3 direct fixtures materialize both accepted values",
        "bitorder": "spi.handle_bit() chooses shift position from options['bitorder']; the LSB one-bit fixture materializes the alternate branch",
        "wordsize": "spi.handle_bit() emits only when bitcount == options['wordsize']; word1 and word8 fixtures materialize both finite branches",
        "address_format": "i2c.handle_address_or_data() shifts d right only when address_format=='shifted'; direct shifted and unshifted fixtures materialize both branches",
    }
    # Kept as static-review provenance for human readers of this generator.
    # No matrix row is accepted on the basis of this table alone.
    assert set(source_equivalence) >= set(defaults)
    return rows


def record(
    index: int,
    kind: str,
    value: dict[str, object],
    start: int = 0,
    end: int = 1,
    output_id: int = 0,
    samplerate: int = 1_152_000,
    trigger: int = 1,
) -> dict[str, object]:
    def time(sample: int) -> dict[str, object]:
        return {
            "absolute": {"numerator": sample, "denominator": samplerate},
            "trigger_relative": {"numerator": sample - trigger, "denominator": samplerate},
        }

    return {
        "emission_index": index,
        "output_id": output_id,
        "kind": kind,
        "start_sample": start,
        "end_sample": end,
        "start_time": time(start),
        "end_time": time(end),
        "value": value,
    }


def declarations(decoder: str) -> dict[str, object]:
    """Literal source transcriptions, in each snapshot's declaration order."""
    tables = {
        "uart": (
            [
                ("rx-data", "RX data"),
                ("tx-data", "TX data"),
                ("rx-start", "RX start bit"),
                ("tx-start", "TX start bit"),
                ("rx-parity-ok", "RX parity OK bit"),
                ("tx-parity-ok", "TX parity OK bit"),
                ("rx-parity-err", "RX parity error"),
                ("tx-parity-err", "TX parity error"),
                ("rx-stop", "RX stop bit"),
                ("tx-stop", "TX stop bit"),
                ("rx-warning", "RX warning"),
                ("tx-warning", "TX warning"),
                ("rx-data-bit", "RX data bit"),
                ("tx-data-bit", "TX data bit"),
                ("rx-break", "RX break"),
                ("tx-break", "TX break"),
                ("rx-packet", "RX packet"),
                ("tx-packet", "TX packet"),
            ],
            [("rx", "RX dump"), ("tx", "TX dump"), ("rxtx", "RX/TX dump")],
            [
                ("rx-data-bits", "RX bits", [12]),
                ("rx-data-vals", "RX data", [0, 2, 4, 6, 8]),
                ("rx-warnings", "RX warnings", [10]),
                ("rx-breaks", "RX breaks", [14]),
                ("rx-packets", "RX packets", [16]),
                ("tx-data-bits", "TX bits", [13]),
                ("tx-data-vals", "TX data", [1, 3, 5, 7, 9]),
                ("tx-warnings", "TX warnings", [11]),
                ("tx-breaks", "TX breaks", [15]),
                ("tx-packets", "TX packets", [17]),
            ],
            [],
        ),
        "spi": (
            [
                ("miso-data", "MISO data"),
                ("mosi-data", "MOSI data"),
                ("miso-bit", "MISO bit"),
                ("mosi-bit", "MOSI bit"),
                ("warning", "Warning"),
                ("miso-transfer", "MISO transfer"),
                ("mosi-transfer", "MOSI transfer"),
            ],
            [("miso", "MISO"), ("mosi", "MOSI")],
            [
                ("miso-bits", "MISO bits", [2]),
                ("miso-data-vals", "MISO data", [0]),
                ("miso-transfers", "MISO transfers", [5]),
                ("mosi-bits", "MOSI bits", [3]),
                ("mosi-data-vals", "MOSI data", [1]),
                ("mosi-transfers", "MOSI transfers", [6]),
                ("other", "Other", [4]),
            ],
            [(3, "integer", "Bitrate", "Bitrate during transfers")],
        ),
        "i2c": (
            [
                ("start", "Start condition"),
                ("repeat-start", "Repeat start condition"),
                ("stop", "Stop condition"),
                ("ack", "ACK"),
                ("nack", "NACK"),
                ("bit", "Data/address bit"),
                ("address-read", "Address read"),
                ("address-write", "Address write"),
                ("data-read", "Data read"),
                ("data-write", "Data write"),
                ("warning", "Warning"),
            ],
            [
                ("address-read", "Address read"),
                ("address-write", "Address write"),
                ("data-read", "Data read"),
                ("data-write", "Data write"),
            ],
            [
                ("bits", "Bits", [5]),
                ("addr-data", "Address/data", [0, 1, 2, 3, 4, 6, 7, 8, 9]),
                ("warnings", "Warnings", [10]),
            ],
            [(3, "integer", "Bitrate", "Bitrate from Start bit to Stop bit")],
        ),
    }
    anns, bins, rows, metas = tables[decoder]
    return {
        "annotations": [
            {"index": i, "id": ident, "description": desc} for i, (ident, desc) in enumerate(anns)
        ],
        "annotation_rows": [
            {"index": i, "id": ident, "description": desc, "annotation_indices": indices}
            for i, (ident, desc, indices) in enumerate(rows)
        ],
        "binary": [
            {"index": i, "id": ident, "description": desc} for i, (ident, desc) in enumerate(bins)
        ],
        "metadata": [
            {"output_id": output, "value_type": typ, "name": name, "description": desc}
            for output, typ, name, desc in metas
        ],
    }


def fixture(
    ident: str,
    decoder: str,
    mapping: dict[str, int],
    options: dict[str, object],
    transitions: dict[str, list[list[int]]],
    waits: list[dict[str, object]],
    records: list[dict[str, object]],
    meaning: str,
    trigger: int = 1,
    samplerate: int = 1_152_000,
    sample_count: int | None = None,
) -> dict[str, object]:
    """A hand-authored protocol case; this does not infer output from transitions."""
    channel_order = {
        "uart": ("rx", "tx"),
        "spi": ("clk", "miso", "mosi", "cs"),
        "i2c": ("scl", "sda"),
    }[decoder]
    for wait in waits:
        wait["pins"] = [
            255
            if channel not in mapping
            else next(
                level for at, level in transitions[f"D{mapping[channel]}"] if at <= wait["sample"]
            )
            for channel in channel_order
        ]
        # latest declared transition is the actual level at the returned sample.
        for index, channel in enumerate(channel_order):
            if channel in mapping:
                wait["pins"][index] = [
                    level
                    for at, level in transitions[f"D{mapping[channel]}"]
                    if at <= wait["sample"]
                ][-1]
    return {
        "id": ident,
        "decoder": decoder,
        "samplerate_hz": samplerate,
        "trigger_index": trigger,
        "sample_count": sample_count
        if sample_count is not None
        else max(
            [at for edges in transitions.values() for at, _ in edges]
            + [wait["sample"] for wait in waits]
            + [item["end_sample"] for item in records]
        )
        + 1,
        "mapping": mapping,
        "options": options,
        "transitions": transitions,
        "expected_wait_trace": waits,
        "declarations": declarations(decoder),
        "meaning": meaning,
        "expected_records": records,
    }


def edge_trace(
    condition: dict[str, object], samples: list[int], pins: list[int]
) -> list[dict[str, object]]:
    """Literal sample schedule for one source wait branch; never executes it."""
    return [
        {"condition": condition, "sample": sample, "matched": [True], "pins": pins}
        for sample in samples
    ]


def build() -> dict[str, object]:
    provenance = {
        "schema": "cycle3-provenance/v1",
        "import_commit": "407b5ef039aa0474c400c0721749baa126e53270",
        "prior_gitlink": "0235970293590f673a253950e6c61017cefa97df",
        "files": [
            {
                "path": path,
                "sha256": digest,
                "license": "unobserved-in-file"
                if path.endswith("sigrokdecode.py")
                else "GPL-2.0-or-later",
                "notice_observation": (
                    "no copyright or GPL notice in local shim bytes"
                    if path.endswith("sigrokdecode.py")
                    else "GPLv2-or-later header retained in file bytes"
                ),
            }
            for path, digest in FILES
        ],
        "file_set_algorithm": (
            "For each decoder, order its declared UTF-8 repository paths; append "
            "each path bytes, one NUL byte, that file's lowercase SHA-256 ASCII "
            "bytes, and one LF byte; SHA-256 the resulting byte stream."
        ),
        "permitted_imports": [
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
        ],
        "license_disposition": (
            "project/legal review required before package placement; no legal conclusion"
        ),
        "proposed_review_input": {
            "package_placement": (
                "do not place snapshot files in distributable package before review"
            ),
            "metadata": (
                "retain source notices and reconcile GPL snapshot material with "
                "MIT package metadata"
            ),
            "distribution": "no wheel, sdist, build, or publication authorized",
        },
    }
    file_hash = dict(FILES)
    decoder_file_paths = {
        "uart": [
            "Software/decoders/sigrokdecode.py",
            "Software/decoders/uart/__init__.py",
            "Software/decoders/uart/pd.py",
            "Software/decoders/common/srdhelper/__init__.py",
            "Software/decoders/common/srdhelper/mod.py",
        ],
        "spi": [
            "Software/decoders/sigrokdecode.py",
            "Software/decoders/spi/__init__.py",
            "Software/decoders/spi/pd.py",
        ],
        "i2c": [
            "Software/decoders/sigrokdecode.py",
            "Software/decoders/i2c/__init__.py",
            "Software/decoders/i2c/pd.py",
            "Software/decoders/common/srdhelper/__init__.py",
            "Software/decoders/common/srdhelper/mod.py",
        ],
    }
    decoder_file_sets = {
        decoder: hashlib.sha256(
            b"".join(
                path.encode("utf-8") + b"\0" + file_hash[path].lower().encode("ascii") + b"\n"
                for path in paths
            )
        ).hexdigest()
        for decoder, paths in decoder_file_paths.items()
    }
    provenance["decoder_file_sets"] = [
        {"decoder": decoder, "paths": paths, "sha256": decoder_file_sets[decoder]}
        for decoder, paths in decoder_file_paths.items()
    ]
    # These records are transcribed from the source's put() calls.  The edge
    # lists are deliberately legible clocks/levels, not generated stimulus.
    uart_rx = [
        record(
            0,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "STARTBIT"},
                    {"tag": "integer", "value": 0},
                    {"tag": "integer", "value": 0},
                ],
            },
            0,
            10,
            0,
        ),
        record(1, "annotation", {"class_index": 2, "texts": ["Start bit", "Start", "S"]}, 0, 10, 2),
        record(
            2,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "DATA"},
                    {"tag": "integer", "value": 0},
                    {
                        "tag": "tuple",
                        "value": [{"tag": "integer", "value": 165}, {"tag": "list", "value": []}],
                    },
                ],
            },
            10,
            90,
            0,
        ),
        record(3, "binary", {"class_index": 0, "data_base64": "pQ=="}, 10, 100, 1),
        record(4, "annotation", {"class_index": 0, "texts": ["A5"]}, 10, 100, 2),
        record(
            5,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "STOPBIT"},
                    {"tag": "integer", "value": 0},
                    {"tag": "integer", "value": 1},
                ],
            },
            90,
            100,
            0,
        ),
        record(6, "annotation", {"class_index": 8, "texts": ["Stop bit", "Stop", "T"]}, 90, 100, 2),
        record(
            7,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "FRAME"},
                    {"tag": "integer", "value": 0},
                    {
                        "tag": "tuple",
                        "value": [{"tag": "integer", "value": 165}, {"tag": "bool", "value": True}],
                    },
                ],
            },
            0,
            100,
            0,
        ),
    ]
    uart_tx = [
        record(
            0,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "STARTBIT"},
                    {"tag": "integer", "value": 1},
                    {"tag": "integer", "value": 0},
                ],
            },
            0,
            10,
            0,
        ),
        record(1, "annotation", {"class_index": 3, "texts": ["Start bit", "Start", "S"]}, 0, 10, 2),
        record(
            2,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "DATA"},
                    {"tag": "integer", "value": 1},
                    {
                        "tag": "tuple",
                        "value": [{"tag": "integer", "value": 165}, {"tag": "list", "value": []}],
                    },
                ],
            },
            10,
            90,
            0,
        ),
        record(3, "binary", {"class_index": 1, "data_base64": "pQ=="}, 10, 100, 1),
        record(4, "annotation", {"class_index": 1, "texts": ["A5"]}, 10, 100, 2),
        record(
            5,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "STOPBIT"},
                    {"tag": "integer", "value": 1},
                    {"tag": "integer", "value": 1},
                ],
            },
            90,
            100,
            0,
        ),
        record(6, "annotation", {"class_index": 9, "texts": ["Stop bit", "Stop", "T"]}, 90, 100, 2),
        record(
            7,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "FRAME"},
                    {"tag": "integer", "value": 1},
                    {
                        "tag": "tuple",
                        "value": [{"tag": "integer", "value": 165}, {"tag": "bool", "value": True}],
                    },
                ],
            },
            0,
            100,
            0,
        ),
    ]
    uart_error = [
        record(
            0,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "PARITY ERROR"},
                    {"tag": "integer", "value": 0},
                    {
                        "tag": "tuple",
                        "value": [{"tag": "integer", "value": 0}, {"tag": "integer", "value": 1}],
                    },
                ],
            },
            90,
            100,
            0,
        ),
        record(1, "annotation", {"class_index": 6, "texts": ["Parity error", "PE"]}, 90, 100, 2),
        record(
            2,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "INVALID STOPBIT"},
                    {"tag": "integer", "value": 0},
                    {"tag": "integer", "value": 0},
                ],
            },
            100,
            110,
            0,
        ),
        record(
            3,
            "annotation",
            {"class_index": 10, "texts": ["Frame error", "Frame err", "FE"]},
            100,
            110,
            2,
        ),
        record(
            4,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "BREAK"},
                    {"tag": "integer", "value": 0},
                    {"tag": "integer", "value": 0},
                ],
            },
            1,
            120,
            0,
        ),
        record(5, "annotation", {"class_index": 14, "texts": ["Break", "Brk", "B"]}, 1, 120, 2),
        record(
            6,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "IDLE"},
                    {"tag": "integer", "value": 0},
                    {"tag": "integer", "value": 0},
                ],
            },
            120,
            130,
            0,
        ),
        record(
            7,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "FRAME"},
                    {"tag": "integer", "value": 0},
                    {
                        "tag": "tuple",
                        "value": [
                            {"tag": "integer", "value": 165},
                            {"tag": "bool", "value": False},
                        ],
                    },
                ],
            },
            1,
            110,
            0,
        ),
        record(8, "annotation", {"class_index": 16, "texts": ["A5"]}, 1, 110, 2),
        record(
            9,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "PACKET"},
                    {"tag": "integer", "value": 0},
                    {"tag": "list", "value": [{"tag": "integer", "value": 165}]},
                ],
            },
            1,
            110,
            0,
        ),
        record(10, "annotation", {"class_index": 16, "texts": ["A5"]}, 1, 110, 2),
    ]
    spi_mosi = [
        record(
            0,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "DATA"},
                    {"tag": "integer", "value": 165},
                    {"tag": "null"},
                ],
            },
            10,
            80,
            0,
        ),
        record(1, "binary", {"class_index": 1, "data_base64": "pQ=="}, 10, 80, 2),
        record(2, "annotation", {"class_index": 1, "texts": ["A5"]}, 10, 80, 1),
        record(3, "metadata", {"value_type": "integer", "value": 114285}, 10, 80, 3),
    ]
    spi_miso = [
        record(
            0,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "DATA"},
                    {"tag": "null"},
                    {"tag": "integer", "value": 90},
                ],
            },
            10,
            80,
            0,
        ),
        record(1, "binary", {"class_index": 0, "data_base64": "Wg=="}, 10, 80, 2),
        record(2, "annotation", {"class_index": 0, "texts": ["5A"]}, 10, 80, 1),
        record(3, "metadata", {"value_type": "integer", "value": 114285}, 10, 80, 3),
    ]

    # putdata() order from spi/pd.py: binary, BITS, DATA, eight bit annotations,
    # then the dataword annotation.  These are literal source-order records.
    def spi_complete(value: int, binary_class: int, ann_class: int) -> list[dict[str, object]]:
        output = [
            record(
                0,
                "binary",
                {"class_index": binary_class, "data_base64": "pQ==" if value == 165 else "Wg=="},
                10,
                80,
                2,
            ),
            record(
                1,
                "python",
                {
                    "tag": "list",
                    "value": [
                        {"tag": "string", "value": "BITS"},
                        {"tag": "null"},
                        {"tag": "list", "value": []},
                    ],
                },
                10,
                80,
                0,
            ),
            record(
                2,
                "python",
                {
                    "tag": "list",
                    "value": [
                        {"tag": "string", "value": "DATA"},
                        {"tag": "integer", "value": value}
                        if binary_class == 1
                        else {"tag": "null"},
                        {"tag": "integer", "value": value}
                        if binary_class == 0
                        else {"tag": "null"},
                    ],
                },
                10,
                80,
                0,
            ),
        ]
        output += [
            record(
                3 + i,
                "annotation",
                {"class_index": ann_class + 2, "texts": [str((value >> (7 - i)) & 1)]},
                10 + i * 10,
                20 + i * 10,
                1,
            )
            for i in range(8)
        ]
        output.append(
            record(
                11, "annotation", {"class_index": ann_class, "texts": [f"{value:02X}"]}, 10, 80, 1
            )
        )
        return output

    spi_mosi = spi_complete(165, 1, 1)
    spi_miso = spi_complete(90, 0, 0)
    # putdata() passes newest-first bit entries.  Preserve the source Data
    # tuple shape rather than a display-only bit list.
    for records, value, present_index in ((spi_mosi, 165, 1), (spi_miso, 90, 2)):
        bits = [int(bit) for bit in f"{value:08b}"]
        entries = [
            {"tag": "spi-data", "ss": 10 + 20 * i, "es": 30 + 20 * i, "val": bit}
            for i, bit in reversed(list(enumerate(bits)))
        ]
        records[1]["value"]["value"][present_index] = {"tag": "list", "value": entries}
        records[0]["start_sample"], records[0]["end_sample"] = 10, 150
        records[1]["start_sample"], records[1]["end_sample"] = 10, 150
        records[2]["start_sample"], records[2]["end_sample"] = 10, 150
        for offset, bit in enumerate(bits):
            records[3 + offset]["start_sample"] = 10 + 20 * offset
            records[3 + offset]["end_sample"] = 30 + 20 * offset
        records[11]["start_sample"], records[11]["end_sample"] = 10, 150
    spi_word1 = [
        record(
            0,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "CS-CHANGE"},
                    {"tag": "null"},
                    {"tag": "integer", "value": 1},
                ],
            },
            0,
            0,
            0,
        ),
        record(
            1,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "DATA"},
                    {"tag": "integer", "value": 1},
                    {"tag": "null"},
                ],
            },
            10,
            10,
            0,
        ),
        record(2, "binary", {"class_index": 1, "data_base64": "AQ=="}, 10, 10, 2),
        record(3, "annotation", {"class_index": 1, "texts": ["01"]}, 10, 10, 1),
        record(
            4,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "TRANSFER"},
                    {"tag": "null"},
                    {"tag": "list", "value": [{"tag": "spi-data", "ss": 10, "es": 10, "val": 1}]},
                ],
            },
            10,
            11,
            0,
        ),
    ]
    i2c_write = [
        record(
            0,
            "python",
            {"tag": "list", "value": [{"tag": "string", "value": "START"}, {"tag": "null"}]},
            1,
            1,
            0,
        ),
        record(1, "annotation", {"class_index": 0, "texts": ["Start", "S"]}, 1, 1, 1),
        record(
            2,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "ADDRESS WRITE"},
                    {"tag": "integer", "value": 80},
                ],
            },
            10,
            80,
            0,
        ),
        record(3, "binary", {"class_index": 1, "data_base64": "UA=="}, 10, 80, 2),
        record(
            4,
            "annotation",
            {"class_index": 7, "texts": ["Address write: 50", "AW: 50", "50"]},
            10,
            70,
            1,
        ),
        record(
            5,
            "python",
            {"tag": "list", "value": [{"tag": "string", "value": "ACK"}, {"tag": "null"}]},
            80,
            90,
            0,
        ),
        record(6, "annotation", {"class_index": 3, "texts": ["ACK", "A"]}, 80, 90, 1),
        record(
            7,
            "python",
            {
                "tag": "list",
                "value": [{"tag": "string", "value": "BITS"}, {"tag": "list", "value": []}],
            },
            100,
            170,
            0,
        ),
        record(
            8,
            "python",
            {
                "tag": "list",
                "value": [
                    {"tag": "string", "value": "DATA WRITE"},
                    {"tag": "integer", "value": 51},
                ],
            },
            100,
            170,
            0,
        ),
        record(9, "binary", {"class_index": 3, "data_base64": "Mw=="}, 100, 170, 2),
        record(
            10,
            "annotation",
            {"class_index": 9, "texts": ["Data write: 33", "DW: 33", "33"]},
            100,
            170,
            1,
        ),
        record(
            11,
            "python",
            {"tag": "list", "value": [{"tag": "string", "value": "NACK"}, {"tag": "null"}]},
            180,
            190,
            0,
        ),
        record(12, "annotation", {"class_index": 4, "texts": ["NACK", "N"]}, 180, 190, 1),
        record(
            13,
            "python",
            {"tag": "list", "value": [{"tag": "string", "value": "STOP"}, {"tag": "null"}]},
            191,
            191,
            0,
        ),
        record(14, "annotation", {"class_index": 2, "texts": ["Stop", "P"]}, 191, 191, 1),
        record(15, "metadata", {"value_type": "integer", "value": 97826}, 1, 191, 3),
    ]
    i2c_repeat = i2c_write[:2] + [
        record(
            2,
            "python",
            {"tag": "list", "value": [{"tag": "string", "value": "START REPEAT"}, {"tag": "null"}]},
            16,
            16,
            0,
        ),
        record(3, "annotation", {"class_index": 1, "texts": ["Start repeat", "Sr"]}, 16, 16, 1),
    ]
    fixtures = {
        "schema": "cycle3-semantic-fixtures/v1",
        "oracle": "independently authored declarative timelines; no runtime output",
        "timelines": [
            fixture(
                "uart-rx-valid-default",
                "uart",
                {"rx": 4},
                {},
                {
                    "D4": [
                        [0, 1],
                        [1, 0],
                        [10, 1],
                        [20, 0],
                        [30, 1],
                        [40, 0],
                        [50, 0],
                        [60, 1],
                        [70, 0],
                        [80, 1],
                        [90, 1],
                    ]
                },
                edge_trace({"0": "f"}, [1, 10, 20, 30, 40, 50, 60, 70, 80, 90], [0, 255]),
                uart_rx,
                "RX A5, 8N1, with source output order",
            ),
            fixture(
                "uart-tx-valid-default",
                "uart",
                {"tx": 9},
                {},
                {
                    "D9": [
                        [0, 1],
                        [1, 0],
                        [10, 1],
                        [20, 0],
                        [30, 1],
                        [40, 0],
                        [50, 0],
                        [60, 1],
                        [70, 0],
                        [80, 1],
                        [90, 1],
                    ]
                },
                edge_trace({"1": "f"}, [1, 10, 20, 30, 40, 50, 60, 70, 80, 90], [255, 0]),
                uart_tx,
                "TX-only counterpart; pin vector [0xFF, level] and TX classes are source-offset",
            ),
            fixture(
                "uart-parity-invalid-stop-break-idle-packet",
                "uart",
                {"rx": 4},
                {"parity": "even", "rx_packet_delim": 165, "rx_packet_len": 1},
                {
                    "D4": [
                        [0, 1],
                        [1, 0],
                        [10, 1],
                        [20, 0],
                        [30, 1],
                        [40, 0],
                        [50, 0],
                        [60, 1],
                        [70, 0],
                        [80, 1],
                        [90, 0],
                        [100, 0],
                        [110, 0],
                        [120, 1],
                    ]
                },
                edge_trace(
                    {"0": "f"}, [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], [0, 255]
                ),
                uart_error,
                "Dedicated error/break/idle/packet stimulus; expected source emissions are "
                "reviewed independently before execution",
            ),
            fixture(
                "uart-msb-9bit-boundary-incomplete",
                "uart",
                {"rx": 4},
                {"data_bits": 9, "bit_order": "msb-first", "sample_point": 99},
                {"D4": [[0, 1], [1, 0], [10, 1], [20, 0], [30, 1], [40, 0], [50, 1]]},
                edge_trace({"0": "f"}, [1, 10, 20, 30, 40, 50], [0, 255]),
                uart_rx[:2],
                "9-bit MSB first boundary; end suppresses incomplete frame",
            ),
            fixture(
                "spi-mosi-mode0-word8",
                "spi",
                {"clk": 1, "mosi": 3},
                {},
                {
                    "D1": [
                        [0, 0],
                        [10, 1],
                        [20, 0],
                        [30, 1],
                        [40, 0],
                        [50, 1],
                        [60, 0],
                        [70, 1],
                        [80, 0],
                    ],
                    "D3": [[0, 1], [10, 1], [20, 0], [30, 1], [40, 0], [50, 0], [60, 1], [70, 0]],
                },
                edge_trace({"0": "r"}, [10, 20, 30, 40, 50, 60, 70, 80], [1, 255, 1, 255]),
                spi_mosi,
                "MOSI-only mode 0 0xA5",
            ),
            fixture(
                "spi-miso-mode3-word8",
                "spi",
                {"clk": 1, "miso": 2},
                {"cpol": 1, "cpha": 1},
                {
                    "D1": [
                        [0, 1],
                        [10, 0],
                        [20, 1],
                        [30, 0],
                        [40, 1],
                        [50, 0],
                        [60, 1],
                        [70, 0],
                        [80, 1],
                    ],
                    "D2": [[0, 0], [10, 1], [20, 0], [30, 1], [40, 0], [50, 1], [60, 0], [70, 1]],
                },
                edge_trace({"0": "f"}, [10, 20, 30, 40, 50, 60, 70, 80], [0, 1, 255, 255]),
                spi_miso,
                "MISO-only mode 3 with absent MOSI and CS",
            ),
            fixture(
                "spi-cs-active-high-lsb-word1",
                "spi",
                {"clk": 1, "mosi": 3, "cs": 4},
                {
                    "cs_polarity": "active-high",
                    "cpol": 1,
                    "cpha": 0,
                    "bitorder": "lsb-first",
                    "wordsize": 1,
                },
                {"D1": [[0, 1], [10, 0]], "D3": [[0, 1]], "D4": [[0, 1], [11, 0]]},
                [
                    {
                        "condition": [{"0": "f"}, {"3": "e"}],
                        "sample": 10,
                        "matched": [True, True],
                        "pins": [0, 255, 1, 1],
                    }
                ],
                spi_word1,
                "CS polarity, LSB order and one-bit word boundary",
            ),
            fixture(
                "spi-incomplete-no-cs",
                "spi",
                {"clk": 1, "mosi": 3},
                {"wordsize": 8},
                {"D1": [[0, 0], [10, 1], [20, 0]], "D3": [[0, 1], [10, 0]]},
                edge_trace({"0": "r"}, [10, 20], [1, 255, 0, 255]),
                [],
                "Incomplete word yields no DATA emission",
            ),
            fixture(
                "i2c-shifted-start-address-ack-data-nack-stop",
                "i2c",
                {"scl": 2, "sda": 5},
                {},
                {
                    "D2": [
                        [0, 1],
                        [10, 0],
                        [20, 1],
                        [30, 0],
                        [40, 1],
                        [50, 0],
                        [60, 1],
                        [70, 0],
                        [80, 1],
                    ],
                    "D5": [
                        [0, 1],
                        [1, 0],
                        [10, 1],
                        [20, 0],
                        [30, 1],
                        [40, 0],
                        [50, 0],
                        [60, 0],
                        [70, 0],
                        [80, 0],
                        [91, 1],
                    ],
                },
                [
                    {
                        "condition": {"0": "h", "1": "f"},
                        "sample": 1,
                        "matched": [True],
                        "pins": [1, 0],
                    }
                ]
                + edge_trace(
                    {"0": "r"},
                    [10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140, 150, 160, 170, 180],
                    [1, 1],
                )
                + [
                    {
                        "condition": [{"0": "r"}, {"0": "h", "1": "r"}],
                        "sample": 191,
                        "matched": [False, True],
                        "pins": [1, 1],
                    }
                ],
                i2c_write,
                "START, shifted address write, ACK, data/NACK/STOP coverage",
            ),
            fixture(
                "i2c-unshifted-repeated-start",
                "i2c",
                {"scl": 2, "sda": 5},
                {"address_format": "unshifted"},
                {"D2": [[0, 1], [10, 0], [20, 1]], "D5": [[0, 1], [1, 0], [15, 1], [16, 0]]},
                [
                    {
                        "condition": {"0": "h", "1": "f"},
                        "sample": 1,
                        "matched": [True],
                        "pins": [1, 0],
                    },
                    {
                        "condition": [{"0": "r"}, {"0": "h", "1": "f"}, {"0": "h", "1": "r"}],
                        "sample": 16,
                        "matched": [False, True, False],
                        "pins": [1, 0],
                    },
                ],
                i2c_repeat,
                "Unshifted address and repeated START path",
            ),
            fixture(
                "i2c-incomplete-boundary",
                "i2c",
                {"scl": 2, "sda": 5},
                {},
                {"D2": [[0, 1], [10, 0], [20, 1]], "D5": [[0, 1], [1, 0], [10, 1]]},
                edge_trace({"0": "h", "1": "f"}, [1, 10, 20, 30, 40, 50, 60, 70, 80, 91], [1, 0]),
                i2c_write[:2],
                "Capture ends during address byte; no partial byte output",
            ),
        ],
        "edge_decisions": [
            {
                "id": "wait-empty",
                "decision": (
                    "first wait({}) returns sample 0; each later empty wait advances "
                    "exactly one sample"
                ),
                "expected_calls": [
                    {"call": "wait({})", "sample": 0, "matched": [True], "pins": [0, 255]},
                    {"call": "wait({})", "sample": 1, "matched": [True], "pins": [0, 255]},
                ],
            },
            {
                "id": "search-skip",
                "decision": (
                    "channel searches include current sample; sample-zero prior level "
                    "is unavailable; "
                    "skip:0 returns current and skip:N advances N samples"
                ),
                "expected_calls": [
                    {
                        "call": "wait({'skip':0})",
                        "sample": 0,
                        "matched": [True],
                        "previous_sample": None,
                    },
                    {
                        "call": "wait({'skip':2})",
                        "sample": 2,
                        "matched": [True],
                        "previous_sample": 1,
                    },
                ],
            },
            {
                "id": "simultaneous-alternatives",
                "decision": (
                    "all matching alternatives are marked true and no alternative "
                    "suppresses another"
                ),
                "expected_calls": [
                    {
                        "call": "wait([{'0':'r'},{'0':'e'}])",
                        "sample": 4,
                        "matched": [True, True],
                        "pins": [1],
                    },
                    {
                        "call": "wait({'0':'h','1':'f'})",
                        "sample": 4,
                        "matched": [True],
                        "pins": [1, 0],
                    },
                ],
            },
            {
                "id": "interval-boundary",
                "decision": (
                    "put intervals are half-open [start,end); coordinates at "
                    "capture_count are valid "
                    "end coordinates"
                ),
                "expected_calls": [{"call": "put(3,8,...)", "presentation": "samples 3 through 7"}],
            },
            {
                "id": "end-of-input",
                "decision": (
                    "normal end terminates without a partial protocol unit; records emitted before "
                    "termination remain visible"
                ),
                "expected_calls": [
                    {"call": "end", "partial_record": "absent", "earlier_records": "preserved"}
                ],
            },
        ],
        "optional_pin_cases": [
            {"id": "uart-rx-only", "compatibility_pins": [1, 255], "has_channel": [True, False]},
            {"id": "uart-tx-only", "compatibility_pins": [255, 0], "has_channel": [False, True]},
            {
                "id": "spi-miso-only",
                "compatibility_pins": [0, 1, 255, 255],
                "has_channel": [True, True, False, False],
            },
            {
                "id": "spi-mosi-only",
                "compatibility_pins": [0, 255, 1, 255],
                "has_channel": [True, False, True, False],
            },
            {
                "id": "spi-no-cs",
                "compatibility_pins": [0, 1, 0, 255],
                "has_channel": [True, True, True, False],
            },
        ],
    }
    # The waits below are intentionally transcribed as source predicates, not
    # inferred from the record list.  A terminal false match denotes the
    # failed source wait at finite end-of-input; it is not a decoder emission.
    by_id = {timeline["id"]: timeline for timeline in fixtures["timelines"]}
    # Defaults are explicit whenever a named direct witness is cited by the
    # option matrix.  Omission is valid API shorthand, but it is not adequate
    # evidence that a particular direct fixture materialized that value.
    by_id["uart-rx-valid-default"]["options"] = {"baudrate": 115200}
    by_id["uart-tx-valid-default"]["options"] = {"invert_tx": "no"}
    by_id["spi-mosi-mode0-word8"]["options"] = {"cpol": 0, "cpha": 0, "wordsize": 8}
    by_id["i2c-shifted-start-address-ack-data-nack-stop"]["options"] = {
        "address_format": "shifted"
    }

    def repin(timeline: dict[str, object]) -> None:
        order = {"uart": ("rx", "tx"), "spi": ("clk", "miso", "mosi", "cs"), "i2c": ("scl", "sda")}[
            timeline["decoder"]
        ]
        for wait in timeline["expected_wait_trace"]:
            wait["pins"] = [
                255
                if channel not in timeline["mapping"]
                else [
                    level
                    for at, level in timeline["transitions"][f"D{timeline['mapping'][channel]}"]
                    if at <= wait["sample"]
                ][-1]
                for channel in order
            ]

    def uart_trace(
        index: str,
        data_samples: list[int],
        terminal: int,
        edge_samples: list[int] | None = None,
        idle_due: int | None = None,
        incomplete: bool = False,
    ) -> list[dict[str, object]]:
        """Transcribe UART's *successive* earliest wait returns.

        A generic edge is not elided just because the scheduled centre comes
        later: it returns first, runs inspect_edge(), then get_wait_cond()
        recomputes the shorter skip from that edge.  ``edge_samples`` contains
        only genuine level changes (same-level timeline entries are not edges).
        """
        trace = [{"condition": [{index: "f"}, {index: "e"}], "sample": 1, "matched": [True, True]}]
        previous = 1
        edge_samples = edge_samples or []
        for centre in data_samples:
            for edge in [at for at in edge_samples if previous < at < centre]:
                trace.append(
                    {
                        "condition": [{"skip": centre - previous}, {index: "e"}],
                        "sample": edge,
                        "matched": [False, True],
                    }
                )
                previous = edge
            trace.append(
                {
                    "condition": [{"skip": centre - previous}, {index: "e"}],
                    "sample": centre,
                    "matched": [True, False],
                }
            )
            previous = centre
        for edge in [at for at in edge_samples if previous < at < terminal]:
            trace.append(
                {
                    "condition": [{index: "f"}, {index: "e"}, {"skip": terminal - previous}],
                    "sample": edge,
                    "matched": [False, True, False],
                }
            )
            previous = edge
        terminal_condition = (
            [{"skip": data_samples[-1] + 10 - previous}, {index: "e"}]
            if incomplete
            else [{index: "f"}, {index: "e"}, {"skip": (idle_due or terminal) - previous}]
        )
        trace.append(
            {
                "condition": terminal_condition,
                "sample": terminal,
                "matched": [False] * len(terminal_condition),
                "terminal": "end-of-input failed wait",
            }
        )
        return trace

    def tag_string(value: str) -> dict[str, object]:
        return {"tag": "string", "value": value}

    def tag_integer(value: int) -> dict[str, object]:
        return {"tag": "integer", "value": value}

    # Exact integral UART schedule: 1,152,000 / 115,200 == 10 samples/bit.
    # The source samples start at frame_start + ceil(4.5), then every ten.
    for ident, count in (
        ("uart-rx-valid-default", 10),
        ("uart-tx-valid-default", 10),
        ("uart-parity-invalid-stop-break-idle-packet", 11),
        ("uart-msb-9bit-boundary-incomplete", 5),
    ):
        timeline = by_id[ident]
        channel = "rx" if "rx" in timeline["mapping"] else "tx"
        physical = timeline["mapping"][channel]
        # Values are held across the source's actual centre sample.  In
        # particular, 0xA5 is LSB-first 1,0,1,0,0,1,0,1 -- it is not an
        # alternating waveform.  The first entry is the value immediately
        # following the sampled start bit at sample 6.
        values = [1, 0, 1, 0, 0, 1, 0, 1, 1]
        if ident.endswith("incomplete"):
            values = [1, 0, 1, 0, 0]
        elif ident == "uart-parity-invalid-stop-break-idle-packet":
            # A5, bad even parity=1, and invalid stop=0.
            values = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
        timeline["transitions"][f"D{physical}"] = [[0, 1], [1, 0]] + [
            [11 + 10 * i, value] for i, value in enumerate(values[:count])
        ]
        if ident.endswith("incomplete"):
            terminal = 56
        else:
            terminal = 106 if ident != "uart-parity-invalid-stop-break-idle-packet" else 116
        declared = timeline["transitions"][f"D{physical}"]
        real_edges = [at for (at, level), (_, prior) in zip(declared[1:], declared) if level != prior]
        timeline["expected_wait_trace"] = uart_trace(
            "0" if channel == "rx" else "1",
            [6 + 10 * i for i in range(count)],
            terminal,
            real_edges,
            idle_due=(
                1
                + 2
                * (110 if ident == "uart-parity-invalid-stop-break-idle-packet" else 100)
            ),
            incomplete=ident.endswith("incomplete"),
        )
        for wait in timeline["expected_wait_trace"]:
            if isinstance(wait["condition"], list) and len(wait["condition"]) == 3 and not wait.get("terminal"):
                level = [value for at, value in declared if at <= wait["sample"]][-1]
                wait["matched"][0] = level == 0
        timeline["sample_count"] = terminal
        timeline["samplerate_hz"] = 1_152_000
        repin(timeline)

    def uart_default_records(direction: int) -> list[dict[str, object]]:
        """Literal source-order transcription for the integral 8N1 A5 frame."""
        bit_class, data_class, start_class, stop_class = (
            (12, 0, 2, 8) if direction == 0 else (13, 1, 3, 9)
        )
        records = [
            record(0, "python", {"tag": "list", "value": [tag_string("STARTBIT"), tag_integer(direction), tag_integer(0)]}, 1, 11, 0),
            record(1, "annotation", {"class_index": start_class, "texts": ["Start bit", "Start", "S"]}, 1, 11, 2),
        ]
        bits = [1, 0, 1, 0, 0, 1, 0, 1]
        for index, value in enumerate(bits):
            records.append(record(2 + index, "annotation", {"class_index": bit_class, "texts": [str(value)]}, 11 + 10 * index, 21 + 10 * index, 2))
        data_bits = {"tag": "list", "value": [{"tag": "spi-data", "ss": 11 + 10 * i, "es": 21 + 10 * i, "val": bit} for i, bit in enumerate(bits)]}
        records += [
            record(10, "python", {"tag": "list", "value": [tag_string("DATA"), tag_integer(direction), {"tag": "tuple", "value": [tag_integer(165), data_bits]}]}, 11, 91, 0),
            record(11, "annotation", {"class_index": data_class, "texts": ["A5"]}, 11, 91, 2),
            record(12, "binary", {"class_index": direction, "data_base64": "pQ=="}, 11, 91, 1),
            record(13, "binary", {"class_index": 2, "data_base64": "pQ=="}, 11, 91, 1),
            record(14, "python", {"tag": "list", "value": [tag_string("STOPBIT"), tag_integer(direction), tag_integer(1)]}, 91, 101, 0),
            record(15, "annotation", {"class_index": stop_class, "texts": ["Stop bit", "Stop", "T"]}, 91, 101, 2),
            record(16, "python", {"tag": "list", "value": [tag_string("FRAME"), tag_integer(direction), {"tag": "tuple", "value": [tag_integer(165), {"tag": "bool", "value": True}]}]}, 1, 101, 0),
        ]
        return records

    by_id["uart-rx-valid-default"]["expected_records"] = uart_default_records(0)
    by_id["uart-tx-valid-default"]["expected_records"] = uart_default_records(1)

    def spi_trace(samples: list[int], with_cs: bool, terminal: int) -> list[dict[str, object]]:
        trace = [{"condition": {}, "sample": 0, "matched": [True]}]
        cond = [{"0": "e"}] + ([{"3": "e"}] if with_cs else [])
        trace += [
            {"condition": cond, "sample": sample, "matched": [True] + ([False] if with_cs else [])}
            for sample in samples
        ]
        trace.append(
            {
                "condition": cond,
                "sample": terminal,
                "matched": [False] * len(cond),
                "terminal": "end-of-input failed wait",
            }
        )
        return trace

    for ident, sample_edges, sampled_edges in (
        ("spi-mosi-mode0-word8", list(range(10, 161, 10)), list(range(10, 151, 20))),
        ("spi-miso-mode3-word8", list(range(10, 161, 10)), list(range(20, 161, 20))),
    ):
        timeline = by_id[ident]
        clk = 0 if ident.startswith("spi-mosi") else 1
        timeline["transitions"]["D1"] = [[0, clk]] + [
            [sample, 1 - (i % 2) if clk == 0 else i % 2] for i, sample in enumerate(sample_edges)
        ]
        line = "D3" if ident.startswith("spi-mosi") else "D2"
        bits = [int(bit) for bit in f"{165 if line == 'D3' else 90:08b}"]
        timeline["transitions"][line] = [[0, bits[0]]] + [
            [sample, bits[min(i, 7)]] for i, sample in enumerate(sampled_edges)
        ]
        timeline["expected_wait_trace"] = spi_trace(sample_edges, False, 161)
        timeline["sample_count"] = 161
        repin(timeline)

    word1 = by_id["spi-cs-active-high-lsb-word1"]
    word1["expected_wait_trace"] = [
        {"condition": {}, "sample": 0, "matched": [True]},
        {"condition": [{"0": "e"}, {"3": "e"}], "sample": 10, "matched": [True, False]},
        {"condition": [{"0": "e"}, {"3": "e"}], "sample": 11, "matched": [False, True]},
        {
            "condition": [{"0": "e"}, {"3": "e"}],
            "sample": 12,
            "matched": [False, False],
            "terminal": "end-of-input failed wait",
        },
    ]
    word1["sample_count"] = 12
    repin(word1)
    # Source order for the active-high one-bit CS transfer: first-sample CS
    # change, putdata binary/BITS/DATA/bit/word/meta, then deassertion transfer.
    one = tag_integer(1)
    one_data = {"tag": "spi-data", "ss": 10, "es": 10, "val": 1}
    word1["expected_records"] = [
        record(
            0,
            "python",
            {"tag": "list", "value": [tag_string("CS-CHANGE"), {"tag": "null"}, one]},
            0,
            0,
            0,
        ),
        record(1, "binary", {"class_index": 1, "data_base64": "AQ=="}, 10, 10, 2),
        record(
            2,
            "python",
            {
                "tag": "list",
                "value": [
                    tag_string("BITS"),
                    {"tag": "list", "value": [one_data]},
                    {"tag": "null"},
                ],
            },
            10,
            10,
            0,
        ),
        record(
            3,
            "python",
            {"tag": "list", "value": [tag_string("DATA"), one, {"tag": "null"}]},
            10,
            10,
            0,
        ),
        record(4, "annotation", {"class_index": 3, "texts": ["1"]}, 10, 10, 1),
        record(5, "annotation", {"class_index": 1, "texts": ["01"]}, 10, 10, 1),
        record(6, "metadata", {"value_type": "integer", "value": 1_152_000}, 10, 10, 3),
        record(
            7,
            "python",
            {
                "tag": "list",
                "value": [tag_string("CS-CHANGE"), one, {"tag": "integer", "value": 0}],
            },
            11,
            11,
            0,
        ),
        record(8, "annotation", {"class_index": 6, "texts": ["01"]}, 0, 11, 1),
        record(
            9,
            "python",
            {
                "tag": "list",
                "value": [
                    tag_string("TRANSFER"),
                    {"tag": "list", "value": [one_data]},
                    {"tag": "null"},
                ],
            },
            0,
            11,
            0,
        ),
    ]
    incomplete = by_id["spi-incomplete-no-cs"]
    incomplete["expected_wait_trace"] = spi_trace([10, 20, 30, 40], False, 41)
    incomplete["transitions"]["D1"] = [[0, 0], [10, 1], [20, 0], [30, 1], [40, 0]]
    incomplete["sample_count"] = 41
    repin(incomplete)

    def spi_word_records(value: int, side: str, first: int) -> list[dict[str, object]]:
        """Static transcription of handle_bit()/putdata() for one 8-bit word."""
        bits = [int(bit) for bit in f"{value:08b}"]
        entries = [
            {"tag": "spi-data", "ss": first + 20 * i, "es": first + 20 * (i + 1), "val": bit}
            for i, bit in reversed(list(enumerate(bits)))
        ]
        last_end = first + 160
        mosi = {"tag": "list", "value": entries} if side == "mosi" else {"tag": "null"}
        miso = {"tag": "list", "value": entries} if side == "miso" else {"tag": "null"}
        data = tag_integer(value)
        records = [
            record(
                0,
                "binary",
                {
                    "class_index": 1 if side == "mosi" else 0,
                    "data_base64": "pQ==" if value == 165 else "Wg==",
                },
                first,
                last_end,
                2,
            ),
            record(
                1,
                "python",
                {"tag": "list", "value": [tag_string("BITS"), mosi, miso]},
                first,
                last_end,
                0,
            ),
            record(
                2,
                "python",
                {
                    "tag": "list",
                    "value": [
                        tag_string("DATA"),
                        data if side == "mosi" else {"tag": "null"},
                        data if side == "miso" else {"tag": "null"},
                    ],
                },
                first,
                last_end,
                0,
            ),
        ]
        bit_class = 3 if side == "mosi" else 2
        records += [
            record(
                3 + i,
                "annotation",
                {"class_index": bit_class, "texts": [str(bit)]},
                entry["ss"],
                entry["es"],
                1,
            )
            for i, (bit, entry) in enumerate(zip(reversed(bits), entries))
        ]
        records.append(
            record(
                11,
                "annotation",
                {"class_index": 1 if side == "mosi" else 0, "texts": [f"{value:02X}"]},
                first,
                last_end,
                1,
            )
        )
        records.append(
            record(12, "metadata", {"value_type": "integer", "value": 65361}, first, first + 140, 3)
        )
        return records

    by_id["spi-mosi-mode0-word8"]["expected_records"] = spi_word_records(165, "mosi", 10)
    by_id["spi-miso-mode3-word8"]["expected_records"] = spi_word_records(90, "miso", 20)
    by_id["spi-mosi-mode0-word8"]["expected_wait_trace"][-1]["sample"] = 170
    by_id["spi-miso-mode3-word8"]["expected_wait_trace"][-1]["sample"] = 180
    repin(by_id["spi-mosi-mode0-word8"])
    repin(by_id["spi-miso-mode3-word8"])

    # I2C uses a high-SCL SDA fall only for START/repeated START, then SCL
    # rises for each address/data/ack slot.  The alternative predicate is
    # preserved after the address phase, including STOP priority information.
    def i2c_bus(timeline: dict[str, object], rises: list[int], stop: int | None) -> None:
        scl = [[0, 1], [1, 1]]
        for index, rise in enumerate(rises):
            scl.extend([[2 if index == 0 else rise - 10, 0], [rise, 1]])
        sda = [[0, 1], [1, 0]]
        if stop is not None:
            sda.append([stop, 1])
        timeline["transitions"] = {"D2": scl, "D5": sda}

    full = by_id["i2c-shifted-start-address-ack-data-nack-stop"]
    rises = list(range(10, 171, 20)) + list(range(190, 351, 20))
    i2c_bus(full, rises, None)
    # SDA is stable before each SCL rising sample: address byte 0xA0 (shifted
    # to 0x50), ACK=0, payload 0x33, then NACK=1.
    bus_bits = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1]
    full["transitions"]["D5"] = (
        [[0, 1], [1, 0]] + [[sample - 5, bit] for sample, bit in zip(rises, bus_bits)] + [[361, 0], [371, 1]]
    )
    full["transitions"]["D2"] += [[360, 0], [370, 1]]
    full["expected_wait_trace"] = (
        [{"condition": {"0": "h", "1": "f"}, "sample": 1, "matched": [True]}]
        + [{"condition": {"0": "r"}, "sample": sample, "matched": [True]} for sample in rises[:9]]
        + [
            {
                "condition": [{"0": "r"}, {"0": "h", "1": "f"}, {"0": "h", "1": "r"}],
                "sample": sample,
                "matched": [True, False, False],
            }
            for sample in rises[9:]
        ]
        + [
            {
                "condition": [{"0": "r"}, {"0": "h", "1": "f"}, {"0": "h", "1": "r"}],
                "sample": 370,
                "matched": [True, False, False],
            },
            {
                "condition": [{"0": "r"}, {"0": "h", "1": "f"}, {"0": "h", "1": "r"}],
                "sample": 371,
                "matched": [False, False, True],
            },
            {
                "condition": {"0": "h", "1": "f"},
                "sample": 372,
                "matched": [False],
                "terminal": "end-of-input failed wait",
            },
        ]
    )
    full["sample_count"] = 372
    def i2c_byte(value: int, ss: int, command: str, binary_class: int, address: bool) -> list[dict[str, object]]:
        """Exact handle_address_or_data() emission order for an eight-bit byte."""
        bits = [int(bit) for bit in f"{value:08b}"]
        forward = [{"tag": "spi-data", "ss": ss + 20 * i, "es": ss + 20 * (i + 1), "val": bit} for i, bit in enumerate(bits)]
        # The source reverses the accumulated MSB-first list before putp/putg.
        lsb = list(reversed(forward))
        shown = value >> 1 if address else value
        tag = "ADDRESS WRITE" if address else command
        text = "Address write" if address else "Data write"
        cls = 7 if address else 9
        result = [
            record(0, "python", {"tag": "list", "value": [tag_string("BITS"), {"tag": "list", "value": lsb}]}, ss, ss + 160, 0),
            record(1, "python", {"tag": "list", "value": [tag_string(tag), tag_integer(shown)]}, ss, ss + 160, 0),
            record(2, "binary", {"class_index": binary_class, "data_base64": "UA==" if value == 0xA0 else "Mw=="}, ss, ss + 160, 2),
        ]
        result += [record(3 + i, "annotation", {"class_index": 5, "texts": [str(item["val"])]}, item["ss"], item["es"], 1) for i, item in enumerate(lsb)]
        if address:
            result.append(record(11, "annotation", {"class_index": 7, "texts": ["Write", "Wr", "W"]}, ss + 140, ss + 160, 1))
        result.append(record(12 if address else 11, "annotation", {"class_index": cls, "texts": [f"{text}: {shown:02X}", f"{'AW' if address else 'DW'}: {shown:02X}", f"{shown:02X}"]}, ss, ss + 140 if address else ss + 160, 1))
        return result

    # START; address byte A0 -> shifted display 50; ACK; data byte 33;
    # NACK; STOP.  Every coordinate follows I2C's sampled-bit width (20).
    i2c_records = [
        record(0, "python", {"tag": "list", "value": [tag_string("START"), {"tag": "null"}]}, 1, 1, 0),
        record(1, "annotation", {"class_index": 0, "texts": ["Start", "S"]}, 1, 1, 1),
    ]
    i2c_records += i2c_byte(0xA0, 10, "ADDRESS WRITE", 1, True)
    i2c_records += [
        record(0, "python", {"tag": "list", "value": [tag_string("ACK"), {"tag": "null"}]}, 170, 190, 0),
        record(1, "annotation", {"class_index": 3, "texts": ["ACK", "A"]}, 170, 190, 1),
    ]
    i2c_records += i2c_byte(0x33, 190, "DATA WRITE", 3, False)
    i2c_records += [
        record(0, "python", {"tag": "list", "value": [tag_string("NACK"), {"tag": "null"}]}, 350, 370, 0),
        record(1, "annotation", {"class_index": 4, "texts": ["NACK", "N"]}, 350, 370, 1),
        # i2c.handle_stop(): elapsed = es - pdu_start + 1 = 371. The
        # post-NACK SCL rise at 370 enters handle_address_or_data too, so
        # pdu_bits is 17 (two octets plus the retained partial data bit).
        record(2, "metadata", {"value_type": "integer", "value": 52787}, 1, 371, 3),
        record(3, "python", {"tag": "list", "value": [tag_string("STOP"), {"tag": "null"}]}, 371, 371, 0),
        record(4, "annotation", {"class_index": 2, "texts": ["Stop", "P"]}, 371, 371, 1),
    ]
    for index, item in enumerate(i2c_records):
        item["emission_index"] = index
    full["expected_records"] = i2c_records
    repin(full)
    repeat = by_id["i2c-unshifted-repeated-start"]
    repeat["transitions"] = {
        "D2": [[0, 1]]
        + [entry for i in range(9) for entry in ([10 + 20 * i, 0], [20 + 20 * i, 1])]
        # SDA may rise while SCL is low without a STOP.  A subsequent SCL
        # rise is the first partial data-bit return; only then does SDA fall
        # while SCL is high and become a repeated START.
        + [[190, 0], [210, 1]],
        "D5": [[0, 1], [1, 0]]
        + [[15 + 20 * i, bit] for i, bit in enumerate([1, 0, 1, 0, 0, 0, 0, 0, 0])]
        + [[205, 1], [216, 0]],
    }
    repeat["expected_wait_trace"] = (
        [{"condition": {"0": "h", "1": "f"}, "sample": 1, "matched": [True]}]
        + [{"condition": {"0": "r"}, "sample": 20 + 20 * i, "matched": [True]} for i in range(9)]
        + [
            {
                "condition": [{"0": "r"}, {"0": "h", "1": "f"}, {"0": "h", "1": "r"}],
                "sample": 210,
                "matched": [True, False, False],
            },
            {
                "condition": [{"0": "r"}, {"0": "h", "1": "f"}, {"0": "h", "1": "r"}],
                "sample": 216,
                "matched": [False, True, False],
            },
            {
                "condition": {"0": "r"},
                "sample": 217,
                "matched": [False],
                "terminal": "end-of-input failed wait",
            },
        ]
    )
    repeat["sample_count"] = 217
    # The first byte is the unshifted A0 wire value, hence source reports A0
    # (rather than 50) before the genuine repeated START at high SCL.
    repeat_records = [
        record(0, "python", {"tag": "list", "value": [tag_string("START"), {"tag": "null"}]}, 1, 1, 0),
        record(1, "annotation", {"class_index": 0, "texts": ["Start", "S"]}, 1, 1, 1),
    ]
    # i2c_byte's display shift is source-option dependent; transcribe the
    # unshifted address variant rather than claim equivalence.
    repeated_byte = i2c_byte(0xA0, 20, "ADDRESS WRITE", 1, True)
    repeated_byte[1]["value"]["value"][1] = tag_integer(0xA0)
    repeated_byte[-1]["value"]["texts"] = ["Address write: A0", "AW: A0", "A0"]
    repeat_records += repeated_byte
    repeat_records += [
        record(0, "python", {"tag": "list", "value": [tag_string("ACK"), {"tag": "null"}]}, 180, 200, 0),
        record(1, "annotation", {"class_index": 3, "texts": ["ACK", "A"]}, 180, 200, 1),
        record(0, "python", {"tag": "list", "value": [tag_string("START REPEAT"), {"tag": "null"}]}, 216, 216, 0),
        record(1, "annotation", {"class_index": 1, "texts": ["Start repeat", "Sr"]}, 216, 216, 1),
    ]
    for index, item in enumerate(repeat_records):
        item["emission_index"] = index
    repeat["expected_records"] = repeat_records
    repin(repeat)
    i2c_incomplete = by_id["i2c-incomplete-boundary"]
    i2c_bus(i2c_incomplete, [10, 30, 50, 70], None)
    i2c_incomplete["expected_wait_trace"] = (
        [{"condition": {"0": "h", "1": "f"}, "sample": 1, "matched": [True]}]
        + [
            {"condition": {"0": "r"}, "sample": sample, "matched": [True]}
            for sample in (10, 30, 50, 70)
        ]
        + [
            {
                "condition": {"0": "r"},
                "sample": 71,
                "matched": [False],
                "terminal": "end-of-input failed wait",
            }
        ]
    )
    i2c_incomplete["sample_count"] = 71
    repin(i2c_incomplete)

    # Keep error paths separate.  A single low waveform cannot honestly be a
    # completed A5 packet, a parity/stop error, a BREAK, and an IDLE interval.
    # This named fixture is the coherent completed-frame error path: DATA and
    # its packet annotation precede parity/stop processing exactly as the
    # source calls handle_packet().  BREAK and IDLE remain separate stimuli in
    # the corpus rather than fabricated extra emissions here.
    uart_error_records = uart_default_records(0)[:14]
    uart_error_records += [
        # handle_packet() calls putx_packet(), which is annotation-only.
        record(14, "annotation", {"class_index": 16, "texts": ["A5"]}, 11, 91, 2),
        record(15, "python", {"tag": "list", "value": [tag_string("PARITY ERROR"), tag_integer(0), {"tag": "tuple", "value": [tag_integer(0), tag_integer(1)]}]}, 91, 101, 0),
        record(16, "annotation", {"class_index": 6, "texts": ["Parity error", "Parity err", "PE"]}, 91, 101, 2),
        record(17, "python", {"tag": "list", "value": [tag_string("INVALID STOPBIT"), tag_integer(0), tag_integer(0)]}, 101, 111, 0),
        record(18, "annotation", {"class_index": 10, "texts": ["Frame error", "Frame err", "FE"]}, 101, 111, 2),
        record(19, "python", {"tag": "list", "value": [tag_string("STOPBIT"), tag_integer(0), tag_integer(0)]}, 101, 111, 0),
        record(20, "annotation", {"class_index": 8, "texts": ["Stop bit", "Stop", "T"]}, 101, 111, 2),
        record(21, "python", {"tag": "list", "value": [tag_string("FRAME"), tag_integer(0), {"tag": "tuple", "value": [tag_integer(165), {"tag": "bool", "value": False}]}]}, 1, 111, 0),
    ]
    for index, item in enumerate(uart_error_records):
        item["emission_index"] = index
    by_id["uart-parity-invalid-stop-break-idle-packet"]["expected_records"] = uart_error_records
    by_id["uart-parity-invalid-stop-break-idle-packet"]["description"] = (
        "RX A5 packet with even-parity error and invalid stop; BREAK and IDLE "
        "are deliberately separate, non-combinable protocol stimuli."
    )

    # A BREAK is a low interval at least one complete 8N1 frame long followed
    # by a rising edge.  It is not a malformed completed frame.  The regular
    # sampling waits still occur while the line is low; the final generic-edge
    # alternative is what makes inspect_edge() emit BREAK.
    uart_break = copy.deepcopy(by_id["uart-rx-valid-default"])
    uart_break["id"] = "uart-break-low-interval"
    uart_break["transitions"] = {"D4": [[0, 1], [1, 0], [111, 1]]}
    uart_break["expected_wait_trace"] = uart_trace(
        "0", [6 + 10 * i for i in range(10)], 112, [111], idle_due=201
    )
    break_frame = copy.deepcopy(uart_default_records(0))
    for item in break_frame[2:10]:
        item["value"]["texts"] = ["0"]
    break_frame[10]["value"]["value"][2]["value"][0] = tag_integer(0)
    break_frame[10]["value"]["value"][2]["value"][1]["value"] = [
        {"tag": "spi-data", "ss": 11 + 10 * index, "es": 21 + 10 * index, "val": 0}
        for index in range(8)
    ]
    break_frame[11]["value"]["texts"] = ["00"]
    break_frame[12]["value"]["data_base64"] = "AA=="
    break_frame[13]["value"]["data_base64"] = "AA=="
    break_frame[14:] = [
        record(14, "python", {"tag": "list", "value": [tag_string("INVALID STOPBIT"), tag_integer(0), tag_integer(0)]}, 91, 101, 0),
        record(15, "annotation", {"class_index": 10, "texts": ["Frame error", "Frame err", "FE"]}, 91, 101, 2),
        record(16, "python", {"tag": "list", "value": [tag_string("STOPBIT"), tag_integer(0), tag_integer(0)]}, 91, 101, 0),
        record(17, "annotation", {"class_index": 8, "texts": ["Stop bit", "Stop", "T"]}, 91, 101, 2),
        record(18, "python", {"tag": "list", "value": [tag_string("FRAME"), tag_integer(0), {"tag": "tuple", "value": [tag_integer(0), {"tag": "bool", "value": False}]}]}, 1, 101, 0),
    ]
    uart_break["expected_records"] = break_frame + [
        record(19, "python", {"tag": "list", "value": [tag_string("BREAK"), tag_integer(0), tag_integer(0)]}, 1, 111, 0),
        record(20, "annotation", {"class_index": 14, "texts": ["Break condition", "Break", "Brk", "B"]}, 1, 111, 2),
    ]
    for index, item in enumerate(uart_break["expected_records"]):
        item["emission_index"] = index
    uart_break["description"] = "RX all-zero complete frame retains its source emissions before the later BREAK edge."
    fixtures["timelines"].append(uart_break)
    by_id[uart_break["id"]] = uart_break

    # After a valid frame, advance_state() seeds idle_start with frame end 101.
    # get_idle_cond() therefore requests 201 directly (not an event at 101).
    # At 201 inspect_idle emits IDLE [101,201) and then seeds the next due 301.
    uart_idle = copy.deepcopy(by_id["uart-rx-valid-default"])
    uart_idle["id"] = "uart-idle-after-valid-frame"
    idle_edges = [
        at
        for (at, level), (_, prior) in zip(uart_idle["transitions"]["D4"][1:], uart_idle["transitions"]["D4"])
        if level != prior
    ]
    uart_idle["expected_wait_trace"] = uart_trace(
        "0", [6 + 10 * i for i in range(10)], 202, idle_edges, idle_due=201
    )
    uart_idle["expected_wait_trace"][-1:-1] = [
        {"condition": [{"0": "f"}, {"0": "e"}, {"skip": 105}], "sample": 201, "matched": [False, False, True]},
    ]
    uart_idle["expected_wait_trace"][-1]["condition"][2]["skip"] = 100
    uart_idle["expected_records"] = uart_default_records(0) + [
        record(17, "python", {"tag": "list", "value": [tag_string("IDLE"), tag_integer(0), tag_integer(0)]}, 101, 201, 0)
    ]
    uart_idle["description"] = "RX valid A5 frame followed by one complete high IDLE interval."
    fixtures["timelines"].append(uart_idle)
    by_id[uart_idle["id"]] = uart_idle
    repin(uart_break)
    repin(uart_idle)

    # Materialize every remaining accepted matrix row as a declarative
    # fixture.  Do not copy a baseline as evidence: the source reads each of
    # these options in a timing, state, accumulation, or rendering branch, so
    # each witness gets a separately displaced finite trace *and* a changed
    # source-visible output. Each accepted row has its own literal source-shaped
    # input, waits, and output; no option row relies on equivalence prose.
    def direct_uart(option: str, value: object) -> dict[str, object]:
        """Literal finite UART frame derived from the selected source branch."""
        options = {option: value}
        bits_n = int(value) if option == "data_bits" else 8
        if option.endswith("packet_delim") and value == 511:
            bits_n = 9
            options["data_bits"] = 9
        baud = int(value) if option == "baudrate" else 115200
        samplerate = 10 if baud == 1 else 1_152_000
        bit_width = samplerate // baud
        # Keep even the 1% start-bit centre non-negative without clamping any
        # source coordinate: frame_start itself is a derived idle lead-in.
        frame_start = bit_width
        direction = 1 if option.startswith("tx_") or option == "invert_tx" else 0
        invert = (option == ("invert_tx" if direction else "invert_rx") and value == "yes")
        bit_order = value if option == "bit_order" else "lsb-first"
        data = (int(value) if option.endswith("packet_delim") and value != -1 else (0xA3 if option == "bit_order" else 0xA5)) & ((1 << bits_n) - 1)
        logical_bits = [(data >> index) & 1 for index in range(bits_n)]
        wire_bits = list(reversed(logical_bits)) if bit_order == "msb-first" else logical_bits
        parity = value if option == "parity" else "none"
        stops = float(value) if option == "stop_bits" else 1.0
        sample_point = int(value) if option == "sample_point" else 50

        def sample(slot: int) -> int:
            # uart.get_sample_point() returns a float and the wait layer uses
            # ceil(), including the 50%-of-nine-samples case (first centre 6).
            return frame_start + ((bit_width - 1) * sample_point + 99) // 100 + slot * bit_width
        parity_bit = {"odd": 1, "one": 1, "even": 0, "zero": 0, "ignore": 0}.get(parity)
        stop_count = 0 if stops == 0 else int(stops) + int(stops != int(stops))
        levels = [0] + wire_bits + ([] if parity == "none" else [parity_bit]) + [1] * stop_count
        edges = [[0, 1 ^ int(invert)], [frame_start, 0 ^ int(invert)]]
        for slot, level in enumerate(levels[1:], start=1):
            edges.append([frame_start + slot * bit_width, level ^ int(invert)])
        slots = 1 + bits_n + (parity != "none") + stop_count
        start_edge = "r" if invert else "f"
        waits = [{"condition": [{str(direction): start_edge}, {str(direction): "e"}], "sample": frame_start, "matched": [True, True]}]
        previous = frame_start
        # ``wait([skip, edge])`` returns the earliest alternative.  Retain
        # every physical level change before a centre and then recompute the
        # remaining skip from that edge; an equal-value schedule entry is not
        # a generic-edge match.
        real_edges = [at for (at, level), (_, prior) in zip(edges[1:], edges) if level != prior]
        for slot in range(slots):
            centre = sample(slot)
            for edge in [at for at in real_edges if previous < at < centre]:
                waits.append({"condition": [{"skip": centre - previous}, {str(direction): "e"}], "sample": edge, "matched": [False, True]})
                previous = edge
            current = [level for at, level in edges if at <= centre][-1]
            prior = [level for at, level in edges if at <= centre - 1][-1]
            waits.append({"condition": [{"skip": centre - previous}, {str(direction): "e"}], "sample": centre, "matched": [True, current != prior]})
            previous = centre
        frame_len = int((1 + bits_n + (parity != "none") + stops) * bit_width)
        idle_end = frame_start + 2 * frame_len
        capture_end = previous + (bit_width + 1) // 2
        waits.append({"condition": [{str(direction): start_edge}, {str(direction): "e"}, {"skip": idle_end - previous}], "sample": capture_end, "matched": [False, False, False], "terminal": "end-of-input failed wait"})
        bit_class, data_class, start_class, stop_class = ((12, 0, 2, 8) if direction == 0 else (13, 1, 3, 9))
        records = [
            record(0, "python", {"tag": "list", "value": [tag_string("STARTBIT"), tag_integer(direction), tag_integer(0)]}, sample(0) - bit_width // 2, sample(0) + (bit_width + 1) // 2, 0),
            record(1, "annotation", {"class_index": start_class, "texts": ["Start bit", "Start", "S"]}, sample(0) - bit_width // 2, sample(0) + (bit_width + 1) // 2, 2),
        ]
        for index, bit in enumerate(wire_bits):
            records.append(record(len(records), "annotation", {"class_index": bit_class, "texts": [str(bit)]}, sample(index + 1) - bit_width // 2, sample(index + 1) + bit_width // 2, 2))
        data_start, data_end = sample(1) - bit_width // 2, sample(bits_n) + bit_width // 2
        entries = [{"tag": "spi-data", "ss": sample(i + 1) - bit_width // 2, "es": sample(i + 1) + bit_width // 2, "val": bit} for i, bit in enumerate(wire_bits)]
        fmt = value if option == "format" else "hex"
        rendered = {"ascii": "[A5]", "dec": str(data), "hex": f"{data:0{(bits_n + 3) // 4}X}", "oct": f"{data:0{(bits_n + 2) // 3}o}", "bin": f"{data:0{bits_n}b}"}[fmt]
        records += [
            record(len(records), "python", {"tag": "list", "value": [tag_string("DATA"), tag_integer(direction), {"tag": "tuple", "value": [tag_integer(data), {"tag": "list", "value": entries}]}]}, data_start, data_end, 0),
            record(len(records) + 1, "annotation", {"class_index": data_class, "texts": [rendered]}, data_start, data_end, 2),
            record(len(records) + 2, "binary", {"class_index": direction, "data_base64": "AKU=" if bits_n == 9 and data == 165 else {0: "AA==", 5: "BQ==", 37: "JQ==", 163: "ow==", 165: "pQ==", 255: "/w==", 511: "Af8="}[data]}, data_start, data_end, 1),
            record(len(records) + 3, "binary", {"class_index": 2, "data_base64": "AKU=" if bits_n == 9 and data == 165 else {0: "AA==", 5: "BQ==", 37: "JQ==", 163: "ow==", 165: "pQ==", 255: "/w==", 511: "Af8="}[data]}, data_start, data_end, 1),
        ]
        packet = (option.endswith("packet_len") and value == 1) or (option.endswith("packet_delim") and value == data)
        if packet:
            records.append(record(len(records), "annotation", {"class_index": 16 + direction, "texts": [rendered]}, data_start, data_end, 2))
        if parity != "none":
            ps = sample(bits_n + 1)
            records += [record(len(records), "python", {"tag": "list", "value": [tag_string("PARITYBIT"), tag_integer(direction), tag_integer(parity_bit)]}, ps - bit_width // 2, ps + bit_width // 2, 0), record(len(records) + 1, "annotation", {"class_index": 4 + direction, "texts": ["Parity bit", "Parity", "P"]}, ps - bit_width // 2, ps + bit_width // 2, 2)]
        for index in range(stop_count):
            ss = sample(bits_n + 1 + (parity != "none") + index)
            records += [record(len(records), "python", {"tag": "list", "value": [tag_string("STOPBIT"), tag_integer(direction), tag_integer(1)]}, ss - bit_width // 2, ss + bit_width // 2, 0), record(len(records) + 1, "annotation", {"class_index": stop_class, "texts": ["Stop bit", "Stop", "T"]}, ss - bit_width // 2, ss + bit_width // 2, 2)]
        records.append(record(len(records), "python", {"tag": "list", "value": [tag_string("FRAME"), tag_integer(direction), {"tag": "tuple", "value": [tag_integer(data), {"tag": "bool", "value": True}]}]}, frame_start, previous + (bit_width + 1) // 2, 0))
        return fixture("", "uart", {"tx" if direction else "rx": 4}, options, {"D4": edges}, waits, records, "direct source-derived UART option witness", samplerate=samplerate, sample_count=capture_end)

    for option_row in option_rows():
        witness_id = option_row["fixture"]
        if option_row["disposition"] != "direct-fixture" or not str(witness_id).startswith("direct-"):
            continue
        if option_row["decoder"] == "uart":
            witness = direct_uart(option_row["option"], option_row["value"])
        else:
            # Explicit mode-0 MOSI schedule: sample on rising edges 10..150,
            # with intervening falling edges.  CS polarity is meaningful only
            # when the CS channel is present, so that row includes its asserted
            # low level and source wait alternative.
            clocks = [[0, 0]] + [[at, 1 - (index % 2)] for index, at in enumerate(range(10, 161, 10))]
            mosi_bits = [int(bit) for bit in f"{165:08b}"]
            transitions = {
                "D1": clocks,
                "D3": [[0, mosi_bits[0]]] + [[10 + 20 * index, bit] for index, bit in enumerate(mosi_bits)],
            }
            mapping = {"clk": 1, "mosi": 3}
            with_cs = option_row["option"] == "cs_polarity"
            if with_cs:
                mapping["cs"] = 5
                transitions["D5"] = [[0, 0], [161, 1]]
            waits = spi_trace(list(range(10, 161, 10)), with_cs, 170)
            records = spi_word_records(165, "mosi", 10)
            if with_cs:
                waits.insert(
                    -1,
                    {
                        "condition": [{"0": "e"}, {"3": "e"}],
                        "sample": 161,
                        "matched": [False, True],
                    },
                )
                records.insert(0, record(0, "python", {"tag": "list", "value": [tag_string("CS-CHANGE"), {"tag": "null"}, tag_integer(0)]}, 0, 0, 0))
                transfer_data = {"tag": "list", "value": [{"tag": "spi-data", "ss": 10, "es": 170, "val": 165}]}
                records += [record(0, "python", {"tag": "list", "value": [tag_string("CS-CHANGE"), tag_integer(0), tag_integer(1)]}, 161, 161, 0), record(0, "annotation", {"class_index": 6, "texts": ["A5"]}, 0, 161, 1), record(0, "python", {"tag": "list", "value": [tag_string("TRANSFER"), transfer_data, {"tag": "null"}]}, 0, 161, 0)]
            for index, item in enumerate(records):
                item["emission_index"] = index
            witness = fixture("", "spi", mapping, {option_row["option"]: option_row["value"]}, transitions, waits, records, "direct source-derived SPI option witness")
        witness["id"] = witness_id
        witness["description"] = (
            f"Direct option witness for {option_row['decoder']}.{option_row['option']}="
            f"{option_row['value']!r}; source branch has independent transitions, waits, and output."
        )
        fixtures["timelines"].append(witness)
        by_id[witness_id] = witness

    # spi.decode() announces a missing CS channel before its first ``wait({})``.
    # Preserve that source-order record for every no-CS corpus case, including
    # incomplete and direct option witnesses.
    for timeline in fixtures["timelines"]:
        if timeline["decoder"] == "spi" and "cs" not in timeline["mapping"]:
            records = timeline["expected_records"]
            if not records or records[0]["value"].get("value", [{}])[0].get("value") != "CS-CHANGE":
                records.insert(
                    0,
                    record(
                        0,
                        "python",
                        {"tag": "list", "value": [tag_string("CS-CHANGE"), {"tag": "null"}, {"tag": "null"}]},
                        0,
                        0,
                        0,
                    ),
                )
            for index, item in enumerate(records):
                item["emission_index"] = index

    # UART and I2C carry ordinary Python ``[value, ss, es]`` lists.  Data is a
    # namedtuple only in spi/pd.py, so ``spi-data`` is reserved for SPI output.
    def ordinary_bit_triples(value: object) -> object:
        if isinstance(value, list):
            return [ordinary_bit_triples(item) for item in value]
        if not isinstance(value, dict):
            return value
        if value.get("tag") == "spi-data":
            return {
                "tag": "list",
                "value": [
                    {"tag": "integer", "value": value["val"]},
                    {"tag": "integer", "value": value["ss"]},
                    {"tag": "integer", "value": value["es"]},
                ],
            }
        return {key: ordinary_bit_triples(item) for key, item in value.items()}

    for timeline in fixtures["timelines"]:
        if timeline["decoder"] != "spi":
            for item in timeline["expected_records"]:
                item["value"] = ordinary_bit_triples(item["value"])

    # Some source-order records above deliberately receive corrected spans
    # while assembling the protocol schedule.  Times are derived only from
    # authoritative integer coordinates, never from a runtime timestamp.
    for timeline in fixtures["timelines"]:
        for item in timeline["expected_records"]:
            for key, sample in (
                ("start_time", item["start_sample"]),
                ("end_time", item["end_sample"]),
            ):
                item[key] = {
                    "absolute": {"numerator": sample, "denominator": timeline["samplerate_hz"]},
                    "trigger_relative": {
                        "numerator": sample - timeline["trigger_index"],
                        "denominator": timeline["samplerate_hz"],
                    },
                }
        # The capture boundary is derived from every source wait and legal
        # half-open record endpoint, rather than a shared nominal constant.
        highest_record_end = max(
            (item["end_sample"] for item in timeline["expected_records"]), default=0
        )
        terminal = timeline["expected_wait_trace"][-1]["sample"]
        timeline["sample_count"] = max(highest_record_end, terminal)

    value_tags = [
        "null",
        "bool",
        "integer",
        "float",
        "string",
        "bytes",
        "list",
        "tuple",
        "spi-data",
    ]
    tag_values = [
        {"tag": "null"},
        {"tag": "bool", "value": True},
        {"tag": "integer", "value": 7},
        {"tag": "float", "value": -0.0},
        {"tag": "string", "value": "µ"},
        {"tag": "bytes", "value": "AA=="},
        {"tag": "list", "value": [{"tag": "integer", "value": 1}]},
        {"tag": "tuple", "value": [{"tag": "string", "value": "tuple"}]},
        {"tag": "spi-data", "ss": 1, "es": 2, "val": 3},
    ]

    def root_for(value: dict[str, object], kind: str) -> dict[str, object]:
        # SPI alone owns the namedtuple tag and metadata output.  All roots
        # carry the real registration/declaration surface for their decoder.
        decoder = "spi" if value.get("tag") == "spi-data" or kind == "metadata" else "uart"
        defaults_by_decoder = {
            "uart": {
                "baudrate": 115200, "data_bits": 8, "parity": "none", "stop_bits": 1.0,
                "bit_order": "lsb-first", "format": "hex", "invert_rx": "no", "invert_tx": "no",
                "sample_point": 50, "rx_packet_delim": -1, "tx_packet_delim": -1,
                "rx_packet_len": -1, "tx_packet_len": -1,
            },
            "spi": {"cs_polarity": "active-low", "cpol": 0, "cpha": 0, "bitorder": "msb-first", "wordsize": 8},
        }
        channels = (
            [{"decoder_channel": "clk", "physical_channel": 1}, {"decoder_channel": "mosi", "physical_channel": 3}]
            if decoder == "spi" else [{"decoder_channel": "rx", "physical_channel": 4}]
        )
        output_ids = (
            {"annotation": 1, "python": 0, "binary": 2, "metadata": 3}
            if decoder == "spi" else {"annotation": 2, "python": 0, "binary": 1}
        )
        typed_value = {
            "annotation": {"class_index": 0, "texts": ["A"]},
            "python": value,
            "binary": {"class_index": 0, "data_base64": "AA=="},
            "metadata": {"value_type": "integer", "value": 1},
        }[kind]
        return {
            "schema": "pico-logic-analyzer.decode-result/v1",
            "decoder": {"id": decoder, "file_set_sha256": decoder_file_sets[decoder]},
            "samplerate_hz": 1_152_000,
            "channels": channels,
            "options": defaults_by_decoder[decoder],
            "capture": {"sample_count": 2, "trigger_index": 0},
            "declarations": declarations(decoder),
            "records": [
                record(
                    0,
                    kind,
                    typed_value,
                    start=1,
                    end=2,
                    output_id=output_ids[kind],
                    trigger=0,
                )
            ],
        }

    vectors = [
        {
            "id": f"python-{value['tag']}",
            "kind": "python",
            "tag": value["tag"],
            "object": root_for(value, "python"),
        }
        for value in tag_values
    ]
    vectors += [
        {
            "id": f"record-{kind}",
            "kind": kind,
            "tag": None,
            "object": root_for({"tag": "null"}, kind),
        }
        for kind in ("annotation", "binary", "metadata")
    ]
    typed = {
        "schema": "pico-logic-analyzer.decode-result/v1",
        "record_kinds": ["annotation", "python", "binary", "metadata"],
        "python_value_tags": value_tags,
        "vectors": vectors,
        "cli_utf8_goldens": [
            {"vector_id": vector["id"], "hex": canonical(vector["object"]).hex()}
            for vector in vectors
        ],
    }
    # These are deliberately *pre-execution* ceilings, but they are not
    # hand-waved constants: each one names the exact static corpus maximum it
    # protects and the integer expansion used to obtain its finite boundary.
    # The later runner must enforce these values; this fixture generator does
    # not contain enforcement code.
    fixture_bytes = len(canonical(fixtures))
    max_capture = max(item["sample_count"] for item in fixtures["timelines"])
    max_records = max(len(item["expected_records"]) for item in fixtures["timelines"])

    def tagged_depth(value: object) -> int:
        if not isinstance(value, dict):
            return 0
        children = value.get("value")
        if value.get("tag") in {"list", "tuple"} and isinstance(children, list):
            return 1 + max((tagged_depth(child) for child in children), default=0)
        return 1

    max_depth = max(
        (tagged_depth(record_item["value"]) for item in fixtures["timelines"] for record_item in item["expected_records"]),
        default=1,
    )
    # Corpus bytes cover the largest canonical declarative input; record bytes
    # cover the largest retained expected-output object.  The explicit factors
    # reserve finite hostile-probe headroom without pretending to be a runtime
    # measurement or an operator-approved production threshold.
    max_record_bytes = max(
        (len(canonical(record_item)) for item in fixtures["timelines"] for record_item in item["expected_records"]),
        default=1,
    )
    diagnostic_bytes = max(max_record_bytes * 8, 8192)
    stderr_bytes = diagnostic_bytes * 8
    cap_specs = [
        ("wall_deadline_ms", 5000, "milliseconds", 1, "fixed pre-execution wall-clock ceiling"),
        ("terminate_grace_ms", 250, "milliseconds", 1, "fixed bounded post-termination grace"),
        ("input_samples", max(100000, max_capture * 256), "samples", max_capture, f"{max_capture} * 256 = {max_capture * 256}"),
        ("request_bytes", fixture_bytes * 64, "bytes", fixture_bytes, f"{fixture_bytes} * 64 = {fixture_bytes * 64}"),
        ("output_records", max_records * 2048, "records", max_records, f"{max_records} * 2048 = {max_records * 2048}"),
        ("encoded_bytes", max_record_bytes * 4096, "bytes", max_record_bytes, f"{max_record_bytes} * 4096 = {max_record_bytes * 4096}"),
        ("decoded_bytes", max_record_bytes * 4096, "bytes", max_record_bytes, f"{max_record_bytes} * 4096 = {max_record_bytes * 4096}"),
        ("stdout_bytes", max_record_bytes * 128, "bytes", max_record_bytes, f"{max_record_bytes} * 128 = {max_record_bytes * 128}"),
        (
            "stderr_bytes",
            stderr_bytes,
            "bytes",
            max_record_bytes,
            "eight diagnostic envelopes",
        ),
        (
            "diagnostic_bytes",
            diagnostic_bytes,
            "bytes",
            max_record_bytes,
            "one finite diagnostic envelope",
        ),
        ("text_bytes", max_record_bytes * 2048, "bytes", max_record_bytes, f"{max_record_bytes} * 2048 = {max_record_bytes * 2048}"),
        ("binary_bytes", max_record_bytes * 2048, "bytes", max_record_bytes, f"{max_record_bytes} * 2048 = {max_record_bytes * 2048}"),
        ("nested_depth", max_depth * 8, "levels", max_depth, f"{max_depth} * 8 = {max_depth * 8}"),
        ("nested_items", max_records * 2048, "items", max_records, f"{max_records} * 2048 = {max_records * 2048}"),
        ("retained_result_bytes", fixture_bytes * 256, "bytes", fixture_bytes, f"{fixture_bytes} * 256 = {fixture_bytes * 256}"),
        ("recursion_limit", max_depth * 64, "frames", max_depth, f"{max_depth} * 64 = {max_depth * 64}"),
        ("worker_address_space_bytes", fixture_bytes * 4096, "bytes", fixture_bytes, f"{fixture_bytes} * 4096 = {fixture_bytes * 4096}"),
    ]
    derivations = {
        "wall_deadline_ms": ("multiply", "scheduling-policy-quantum-ms", 50, 100, None),
        "terminate_grace_ms": ("multiply", "scheduling-policy-quantum-ms", 50, 5, None),
        "input_samples": ("max-floor", "corpus-max-input-samples", max_capture, 256, 100000),
        "request_bytes": ("multiply", "fixture-corpus-bytes", fixture_bytes, 64, None),
        "output_records": ("multiply", "corpus-max-records", max_records, 2048, None),
        "encoded_bytes": ("multiply", "largest-record-bytes", max_record_bytes, 4096, None),
        "decoded_bytes": ("multiply", "largest-record-bytes", max_record_bytes, 4096, None),
        "stdout_bytes": ("multiply", "largest-record-bytes", max_record_bytes, 128, None),
        "stderr_bytes": ("multiply", "cap:diagnostic_bytes", diagnostic_bytes, 8, None),
        "diagnostic_bytes": ("max-floor", "largest-record-bytes", max_record_bytes, 8, 8192),
        "text_bytes": ("multiply", "largest-record-bytes", max_record_bytes, 2048, None),
        "binary_bytes": ("multiply", "largest-record-bytes", max_record_bytes, 2048, None),
        "nested_depth": ("multiply", "corpus-max-nested-depth", max_depth, 8, None),
        "nested_items": ("multiply", "corpus-max-records", max_records, 2048, None),
        "retained_result_bytes": ("multiply", "fixture-corpus-bytes", fixture_bytes, 256, None),
        "recursion_limit": ("multiply", "corpus-max-nested-depth", max_depth, 64, None),
        "worker_address_space_bytes": ("multiply", "fixture-corpus-bytes", fixture_bytes, 4096, None),
    }
    caps = {
        "schema": "cycle3-experiment-caps/v1",
        "enforcement_claim": "none; static experiment-only specification, not product thresholds",
        "rationale": "finite conservative pre-execution envelope",
        "caps": [
            {
                "id": key,
                "value": value,
                "unit": unit,
                "domain": "positive integer",
                "boundary": {"accept": value, "reject": value + 1},
                "derivation": {"operation": derivations[key][0], "basis_category": derivations[key][1], "basis_value": derivations[key][2], "multiplier": derivations[key][3], "floor": derivations[key][4], "result": value},
                "rationale": (
                    f"{key}={value} {unit}: operation={derivations[key][0]}; "
                    f"basis_category={derivations[key][1]}; basis_value={derivations[key][2]}; "
                    f"multiplier={derivations[key][3]}; floor={derivations[key][4]}; "
                    f"result={value}. The stated value is the finite conservative experiment "
                    "boundary, with accept=value and reject=value+1. No macOS observation, "
                    "enforcement, or operator-approved production threshold is claimed."
                ),
                "coverage": "runner candidate must enforce later",
            }
            for key, value, unit, basis, derivation in cap_specs
        ],
    }
    return {
        "provenance.json": provenance,
        "semantic-fixtures.json": fixtures,
        "option-matrix.json": {"schema": "cycle3-option-matrix/v1", "rows": option_rows()},
        "typed-vectors.json": typed,
        "experiment-caps.json": caps,
    }


def write(check: bool) -> int:
    artifacts = build()
    manifest_items = []
    for name, value in artifacts.items():
        data = canonical(value)
        path = OUT / name
        manifest_items.append({"path": name, "sha256": hashlib.sha256(data).hexdigest()})
        if check:
            if not path.is_file() or path.read_bytes() != data:
                return 1
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    generator_digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    manifest = {
        "schema": "cycle3-fixture-manifest/v1",
        "generator": "scripts/generate_cycle3_fixtures.py",
        "generator_sha256": generator_digest,
        "artifacts": manifest_items,
    }
    data = canonical(manifest)
    path = OUT / "manifest.json"
    if check:
        return 0 if path.is_file() and path.read_bytes() == data else 1
    path.write_bytes(data)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    raise SystemExit(write(parser.parse_args().check))
