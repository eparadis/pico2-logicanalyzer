"""Literal source-derived V2 vectors; never call production encoders here."""

from __future__ import annotations

IDENTITY_REQUEST = bytes.fromhex("55 aa 00 aa 55")

RISING_REQUEST_PAYLOAD = bytes.fromhex(
    "01 00 00 00 00 00 00 00 01 02 03 04 05 06 07 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "08 00 40 42 0f 00 aa 00 00 00 55 00 00 00 00 00 00 00"
)
RISING_REQUEST = bytes.fromhex(
    "55 aa 01 00 00 00 00 00 00 00 01 02 03 04 05 06 07 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "08 00 40 42 0f 00 f0 5a 00 00 00 f0 a5 00 00 00 00 00 00 00 aa 55"
)

FALLING_REQUEST_PAYLOAD = bytes.fromhex(
    "01 00 00 01 00 00 00 00 01 02 03 04 05 06 07 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "08 00 40 42 0f 00 aa 00 00 00 55 00 00 00 00 00 00 00"
)
FALLING_REQUEST = bytes.fromhex(
    "55 aa 01 00 00 01 00 00 00 00 01 02 03 04 05 06 07 "
    "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 "
    "08 00 40 42 0f 00 f0 5a 00 00 00 f0 a5 00 00 00 00 00 00 00 aa 55"
)

IDENTITY_RESPONSE = (
    b"LOGIC_ANALYZER_TEST_BOARD_V6_0\n"
    b"FREQ:1000000\n"
    b"BLASTFREQ:1000000\n"
    b"BUFFER:131072\n"
    b"CHANNELS:24\n"
)

CAPTURE_RESPONSE = b"CAPTURE_STARTED\n" + (3).to_bytes(4, "little") + b"\x01\x00\x01\x00"
