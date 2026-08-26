#!/usr/bin/env python3
"""Build inert Cycle 3 B1 fixture data from literals authored in this file.

This is deliberately stdlib-only and never imports/executes a host or decoder.
"""

from __future__ import annotations

import argparse
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
                    ("uart", "parity", "even"): "uart-parity-invalid-stop-break-idle-packet",
                    ("uart", "data_bits", 9): "uart-msb-9bit-boundary-incomplete",
                    ("uart", "bit_order", "msb-first"): "uart-msb-9bit-boundary-incomplete",
                    ("uart", "sample_point", 99): "uart-msb-9bit-boundary-incomplete",
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
                direct_fixture = direct_cases.get((decoder, option, value))
                fixture_by_decoder = {
                    "uart": "uart-tx-valid-default"
                    if option == "invert_tx"
                    else "uart-rx-valid-default",
                    "spi": "spi-cs-active-high-lsb-word1"
                    if option == "cs_polarity"
                    else "spi-mosi-mode0-word8",
                    "i2c": "i2c-shifted-start-address-ack-data-nack-stop",
                }
                rows.append(
                    {
                        "id": f"{decoder}-{option}-{value_id}",
                        "decoder": decoder,
                        "option": option,
                        "value": value,
                        "classification": "default"
                        if value == defaults[option]
                        else "accepted-enumeration-or-inclusive-boundary",
                        "disposition": "direct-fixture" if direct_fixture else "static-equivalence",
                        "fixture": (direct_fixture or fixture_by_decoder[decoder]),
                        "equivalence_argument": (
                            None
                            if direct_fixture
                            else {
                                "uart": (
                                    "The UART source only reads this option in format_value/packet "
                                    "rendering or selects a sampled-frame branch; the named finite "
                                    "frame fixes the same register order and frame boundary, while "
                                    "its distinct rendering is asserted "
                                    "by the named source option."
                                ),
                                "spi": (
                                    "The SPI source reads this option only when selecting a clock "
                                    "edge, CS assertion, or bit accumulation direction; the "
                                    "named completed "
                                    "word has the same putdata register/output sequence."
                                ),
                                "i2c": (
                                    "The I2C source reads address_format only when shifting the "
                                    "collected address value; named START/address/ACK/STOP "
                                    "fixture covers the same "
                                    "handlers and output registrations."
                                ),
                            }[decoder]
                        ),
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
    for row in rows:
        if row["disposition"] == "static-equivalence":
            row["equivalence_argument"] += (
                f" Option {row['option']} value {row['value']!r} is the reviewed source branch."
            )
    return rows


def record(
    index: int,
    kind: str,
    value: dict[str, object],
    start: int = 0,
    end: int = 1,
    output_id: int = 0,
    samplerate: int = 1_000_000,
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
        "samplerate_hz": 1_000_000,
        "trigger_index": trigger,
        "sample_count": 256,
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
        typed_value = {
            "annotation": {"class_index": 0, "texts": ["A"]},
            "python": value,
            "binary": {"class_index": 0, "data_base64": "AA=="},
            "metadata": {"value_type": "integer", "value": 1},
        }[kind]
        return {
            "schema": "pico-logic-analyzer.decode-result/v1",
            "decoder": {"id": "uart", "file_set_sha256": "0" * 64},
            "samplerate_hz": 1000000,
            "channels": [{"decoder_channel": "rx", "physical_channel": 4}],
            "options": {"baudrate": 115200},
            "capture": {"sample_count": 2, "trigger_index": 0},
            "declarations": {
                "annotations": [{"index": 0, "id": "a", "description": "A"}],
                "annotation_rows": [
                    {"index": 0, "id": "r", "description": "R", "annotation_indices": [0]}
                ],
                "binary": [{"index": 0, "id": "b", "description": "B"}],
                "metadata": [
                    {"output_id": 3, "value_type": "integer", "name": "M", "description": "M"}
                ],
            },
            "records": [
                record(
                    0,
                    kind,
                    typed_value,
                    start=1,
                    end=2,
                    output_id={"annotation": 0, "python": 1, "binary": 2, "metadata": 3}[kind],
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
                "rationale": (
                    f"{value} {unit} is the conservative finite experiment ceiling for {key}; "
                    "it is independently bounded against related byte, record, depth, retention, "
                    "and deadline caps."
                ),
                "coverage": "runner candidate must enforce later",
            }
            for key, value, unit in [
                ("wall_deadline_ms", 5000, "milliseconds"),
                ("terminate_grace_ms", 250, "milliseconds"),
                ("input_samples", 100000, "samples"),
                ("request_bytes", 4000000, "bytes"),
                ("output_records", 100000, "records"),
                ("encoded_bytes", 16000000, "bytes"),
                ("decoded_bytes", 16000000, "bytes"),
                ("stdout_bytes", 65536, "bytes"),
                ("stderr_bytes", 65536, "bytes"),
                ("diagnostic_bytes", 8192, "bytes"),
                ("text_bytes", 1048576, "bytes"),
                ("binary_bytes", 1048576, "bytes"),
                ("nested_depth", 32, "levels"),
                ("nested_items", 100000, "items"),
                ("retained_result_bytes", 16000000, "bytes"),
                ("recursion_limit", 512, "frames"),
                ("worker_address_space_bytes", 536870912, "bytes"),
            ]
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
