"""Private, versioned, length-framed IPC primitives."""

from __future__ import annotations

import json
import struct
from collections.abc import Callable, Mapping

from .model import HARD_LIMITS, WorkerFailure

VERSION = 1
REQUEST = "decode-request"
RESULT = "decode-result"
FAILURE = "decode-failure"
_SCHEMAS = {
    REQUEST: frozenset(
        {
            "decoder",
            "file_set_sha256",
            "samplerate_hz",
            "channel_ids",
            "mapping",
            "samples",
            "trigger_index",
            "options",
        }
    ),
    RESULT: frozenset({"result", "metrics"}),
    FAILURE: frozenset({"code", "message"}),
}


def encode_frame(message_type: str, fields: Mapping[str, object], limit: int) -> bytes:
    if (
        type(message_type) is not str
        or message_type not in _SCHEMAS
        or type(limit) is not int
        or limit < 1
        or set(fields) != _SCHEMAS[message_type]
        or any(type(key) is not str for key in fields)
    ):
        raise WorkerFailure("ipc rejected")
    raw = json.dumps(
        {"version": VERSION, "type": message_type, **dict(fields)},
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode()
    if len(raw) > limit:
        raise WorkerFailure("ipc rejected")
    return struct.pack(">I", len(raw)) + raw


def read_frame(read: Callable[[int], bytes], limit: int) -> Mapping[str, object]:
    if type(limit) is not int or not 1 <= limit <= HARD_LIMITS["request_bytes"]:
        raise WorkerFailure("ipc rejected")
    header = _read_exact(read, 4)
    size = struct.unpack(">I", header)[0]
    if size > limit:
        raise WorkerFailure("ipc rejected")
    raw = _read_exact(read, size)
    try:
        value = json.loads(raw, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except (UnicodeDecodeError, ValueError):
        raise WorkerFailure("ipc rejected") from None
    if (
        not isinstance(value, dict)
        or value.get("version") != VERSION
        or type(value.get("type")) is not str
        or value["type"] not in _SCHEMAS
        or set(value) != {"version", "type", *_SCHEMAS[value["type"]]}
    ):
        raise WorkerFailure("ipc rejected")
    if read(1):
        raise WorkerFailure("ipc rejected")
    return value


def _read_exact(read: Callable[[int], bytes], count: int) -> bytes:
    chunks: list[bytes] = []
    remaining = count
    while remaining:
        chunk = read(remaining)
        if type(chunk) is not bytes or not chunk:
            raise WorkerFailure("ipc truncated")
        chunks.append(chunk)
        remaining -= len(chunk)
    return b"".join(chunks)


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


def _reject_constant(_value: str) -> object:
    raise ValueError("non-finite value")
