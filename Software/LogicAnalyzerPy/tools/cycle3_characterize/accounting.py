"""Strict, stdlib-only accounting used by the pre-execution boundary."""

from __future__ import annotations

import base64
import json
import math
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

CAP_IDS = frozenset(
    {
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
)


class AccountingFailure(RuntimeError):
    """The untrusted result has no usable partial value."""


@dataclass(frozen=True)
class CapProfile:
    values: Mapping[str, int]

    def __post_init__(self) -> None:
        if set(self.values) != CAP_IDS or any(
            type(v) is not int or v <= 0 for v in self.values.values()
        ):
            raise AccountingFailure("invalid cap profile")
        object.__setattr__(self, "values", dict(self.values))

    def __getitem__(self, name: str) -> int:
        return self.values[name]


def derived_test_profile(production: CapProfile, overrides: Mapping[str, int]) -> CapProfile:
    if not overrides or not set(overrides) <= CAP_IDS:
        raise AccountingFailure("invalid private profile")
    values = dict(production.values)
    for key, value in overrides.items():
        if type(value) is not int or not 0 < value <= production[key]:
            raise AccountingFailure("invalid private cap")
        values[key] = value
    return CapProfile(values)


def _measure(value: object, seen: set[int], depth: int = 1) -> tuple[int, int, int]:
    if isinstance(value, float) and not math.isfinite(value):
        raise AccountingFailure("nonfinite value")
    if isinstance(value, dict | list):
        if id(value) in seen:
            raise AccountingFailure("cyclic value")
        seen.add(id(value))
    if isinstance(value, dict):
        if any(type(key) is not str for key in value):
            raise AccountingFailure("invalid object key")
        if set(value) == {"$cycle3_bytes", "length"}:
            parts = [_measure(value["length"], seen, depth + 1)]
        else:
            parts = [_measure(item, seen, depth + 1) for item in value.values()]
        seen.remove(id(value))
    elif isinstance(value, list):
        parts = [_measure(item, seen, depth + 1) for item in value]
        seen.remove(id(value))
    elif isinstance(value, str):
        return depth, 1, len(value.encode())
    elif type(value) in (int, bool) or value is None:
        return depth, 1, 0
    else:
        raise AccountingFailure("invalid scalar")
    return (
        max([depth] + [part[0] for part in parts]),
        1 + sum(part[1] for part in parts),
        sum(part[2] for part in parts),
    )


def deep_size(value: object) -> int:
    seen: set[int] = set()

    def visit(item: object) -> int:
        if id(item) in seen:
            return 0
        seen.add(id(item))
        if isinstance(item, dict):
            return sys.getsizeof(item) + sum(
                visit(key) + visit(child) for key, child in item.items()
            )
        if isinstance(item, list | tuple):
            return sys.getsizeof(item) + sum(visit(child) for child in item)
        return sys.getsizeof(item)

    return visit(value)


def _nested_binary_total(item: object) -> int:
    if isinstance(item, list):
        return sum(_nested_binary_total(child) for child in item)
    if not isinstance(item, dict):
        return 0
    if set(item) == {"$cycle3_bytes", "length"}:
        encoded, length = item["$cycle3_bytes"], item["length"]
        if not isinstance(encoded, str) or type(length) is not int or length < 0:
            raise AccountingFailure("invalid nested binary")
        try:
            decoded = base64.b64decode(encoded, validate=True)
        except (ValueError, TypeError) as error:
            raise AccountingFailure("invalid nested binary") from error
        if len(decoded) != length:
            raise AccountingFailure("invalid nested binary")
        return length
    return sum(_nested_binary_total(child) for child in item.values())


def result_measurements(value: dict[str, Any]) -> dict[str, int]:
    """Return deterministic cap usage after validating encoded binary forms."""
    depth, items, text = _measure(value, set())
    diagnostics = value.get("diagnostics", "")
    explicit_text = value.get("text", "")
    if not isinstance(diagnostics, str) or not isinstance(explicit_text, str):
        raise AccountingFailure("invalid text field")
    binary = 0
    if "binary" in value:
        encoded_binary = value["binary"]
        if not isinstance(encoded_binary, str):
            raise AccountingFailure("invalid binary")
        try:
            binary = len(base64.b64decode(encoded_binary, validate=True))
        except (ValueError, TypeError) as error:
            raise AccountingFailure("invalid base64") from error
        text -= len(encoded_binary.encode())
    binary += _nested_binary_total(value)
    encoded = len(json.dumps(value, allow_nan=False, separators=(",", ":")).encode())
    return {
        "output_records": len(value["records"]),
        "encoded_bytes": encoded,
        "decoded_bytes": encoded,
        "diagnostic_bytes": len(diagnostics.encode()),
        "text_bytes": text,
        "binary_bytes": binary,
        "nested_depth": depth,
        "nested_items": items,
        "retained_result_bytes": deep_size(value),
    }


def validate_result(value: object, profile: CapProfile) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) - {
        "version",
        "records",
        "text",
        "binary",
        "diagnostics",
    }:
        raise AccountingFailure("unknown result field")
    if value.get("version") != 1 or not isinstance(value.get("records"), list):
        raise AccountingFailure("invalid result shape")
    if len(value["records"]) > profile["output_records"]:
        raise AccountingFailure("record cap")

    measurements = result_measurements(value)
    if (
        measurements["nested_depth"] > profile["nested_depth"]
        or measurements["nested_items"] > profile["nested_items"]
        or measurements["text_bytes"] > profile["text_bytes"]
    ):
        raise AccountingFailure("nested/text cap")
    for field, cap in (("diagnostics", "diagnostic_bytes"), ("text", "text_bytes")):
        if field in value and (
            not isinstance(value[field], str) or len(value[field].encode()) > profile[cap]
        ):
            raise AccountingFailure("text field cap")
    if measurements["binary_bytes"] > profile["binary_bytes"]:
        raise AccountingFailure("binary cap")
    if (
        measurements["decoded_bytes"] > profile["decoded_bytes"]
        or measurements["retained_result_bytes"] > profile["retained_result_bytes"]
    ):
        raise AccountingFailure("result size cap")
    return value
