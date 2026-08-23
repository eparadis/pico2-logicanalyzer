"""Independent round-six mutation audit for the B4 contract checker."""

from __future__ import annotations

import copy
import importlib.util
import json
from collections.abc import Callable
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[2]


def _checker() -> object:
    spec = importlib.util.spec_from_file_location("round6_openapi", ROOT / "tools/check_openapi.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _contract() -> tuple[dict[str, object], str]:
    return (
        json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8")),
        (ROOT / "web/src/api.generated.ts").read_text(encoding="utf-8"),
    )


def test_checker_accepts_only_canonical_baseline() -> None:
    document, types = _contract()
    _checker().validate(document, types)


def _reject_openapi(change: Callable[[dict[str, object]], None]) -> None:
    document, types = _contract()
    mutated = copy.deepcopy(document)
    change(mutated)
    with pytest.raises(AssertionError):
        _checker().validate(mutated, types)


@pytest.mark.parametrize(
    "change",
    [
        lambda doc: doc["components"]["schemas"]["CaptureMetadata"]["properties"]
        ["sample_count"].update({"type": "string"}),
        lambda doc: doc["components"]["schemas"]["CaptureMetadata"]["properties"]
        ["trigger_edge"].update({"enum": ["rising"]}),
        lambda doc: doc["components"]["schemas"]["BusRequest"]["properties"]
        ["strobe_channel"].update({"type": "integer"}),
        lambda doc: doc["components"]["schemas"]["BusRequest"]["properties"]
        ["channel_ids"]["items"].update({"type": "string"}),
        lambda doc: doc["components"]["schemas"]["BusPage"]["properties"]["rows"]
        ["items"]["properties"]["decimal"].update({"type": "string"}),
        lambda doc: doc["components"]["schemas"]["WaveformWindow"]["properties"]
        ["channels"]["items"]["properties"]["transitions"]["items"]["properties"]
        ["value"].update({"type": "string"}),
    ],
    ids=["primitive", "enum", "nullability", "array-item", "nested-decimal", "deep-primitive"],
)
def test_checker_rejects_openapi_mutations(change: Callable[[dict[str, object]], None]) -> None:
    _reject_openapi(change)


@pytest.mark.parametrize(
    ("old", "new"),
    [
        ("decimal: number", "decimal: string"),
        ("sample_count: number", "sample_count: string"),
        ("offset: number; limit: number", "offset: string; limit: number"),
        ("channel_ids: number[]", "channel_ids: string[]"),
        ("strobe_channel: number | null", "strobe_channel: number"),
        ("rows: BusRow[]", "rows: Channel[]"),
        ("export interface BusPage", "export interface BusPageShadow"),
        (
            '"pending" | "running" | "cancelling" | "succeeded" | "failed" | "cancelled"',
            '"pending" | "succeeded"',
        ),
        (
            "channels: { channel_id: number; transitions:",
            "channels: { channel_id: string; transitions: { channel_id: number; marker:",
        ),
    ],
    ids=[
        "nested-model",
        "response-primitive",
        "interface-collision",
        "primitive-array",
        "nullability",
        "referenced-array-model",
        "interface-rename",
        "named-enum",
        "nested-field-collision",
    ],
)
def test_checker_rejects_typescript_mutations(old: str, new: str) -> None:
    document, types = _contract()
    mutated = types.replace(old, new, 1)
    assert mutated != types
    with pytest.raises(AssertionError):
        _checker().validate(document, mutated)
