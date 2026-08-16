"""Verifier-owned literal checks that do not depend on the implementation API."""

from __future__ import annotations

import json
from pathlib import Path

from .golden import (
    FALLING_REQUEST,
    FALLING_REQUEST_PAYLOAD,
    IDENTITY_REQUEST,
    RISING_REQUEST,
    RISING_REQUEST_PAYLOAD,
)

_PROJECT_ROOT = Path(__file__).parents[2]
_PROTOCOL_DATA = _PROJECT_ROOT / "testdata" / "protocol"


def _fixture_bytes(name: str, field: str) -> bytes:
    contents = json.loads((_PROTOCOL_DATA / name).read_text(encoding="utf-8"))
    return bytes.fromhex(contents[field])


def test_identity_literal_matches_accepted_source_fixture() -> None:
    assert IDENTITY_REQUEST == _fixture_bytes("v2_identity_request.source.json", "framed_hex")


def test_rising_literal_matches_accepted_source_fixture() -> None:
    assert RISING_REQUEST_PAYLOAD == _fixture_bytes(
        "v2_normal_8ch_rising.source.json", "unescaped_payload_hex"
    )
    assert RISING_REQUEST == _fixture_bytes("v2_normal_8ch_rising.source.json", "framed_hex")


def test_falling_literal_matches_accepted_source_fixture() -> None:
    assert FALLING_REQUEST_PAYLOAD == _fixture_bytes(
        "v2_normal_8ch_falling.source.json", "unescaped_payload_hex"
    )
    assert FALLING_REQUEST == _fixture_bytes("v2_normal_8ch_falling.source.json", "framed_hex")


def test_literal_rising_falling_delta_is_only_inverted_byte() -> None:
    differences = [
        index
        for index, (rising, falling) in enumerate(
            zip(RISING_REQUEST_PAYLOAD, FALLING_REQUEST_PAYLOAD)
        )
        if rising != falling
    ]
    assert differences == [3]  # command at payload offset 0; native struct offset 2 follows.
    assert RISING_REQUEST_PAYLOAD[3] == 0
    assert FALLING_REQUEST_PAYLOAD[3] == 1
