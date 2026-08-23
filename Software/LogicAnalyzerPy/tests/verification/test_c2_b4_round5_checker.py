"""Independent round-five mutation checks for the B4 wire-contract checker."""

from __future__ import annotations

import copy
import importlib.util
import json
from collections.abc import Callable
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[2]


def _checker() -> object:
    spec = importlib.util.spec_from_file_location("round5_openapi", ROOT / "tools/check_openapi.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _contract() -> tuple[dict[str, object], str]:
    return (
        json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8")),
        (ROOT / "web/src/api.generated.ts").read_text(encoding="utf-8"),
    )


def test_checker_accepts_canonical_contract() -> None:
    document, types = _contract()
    _checker().validate(document, types)


def _openapi_mutation(change: Callable[[dict[str, object]], None]) -> None:
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
    ],
    ids=["primitive", "enum", "nullability", "array-items", "nested-decimal"],
)
def test_checker_rejects_representative_openapi_drift(
    change: Callable[[dict[str, object]], None],
) -> None:
    _openapi_mutation(change)


@pytest.mark.parametrize(
    ("old", "new"),
    [
        ("decimal: number", "decimal: string"),
        ("sample_count: number", "sample_count: string"),
        ("offset: number; limit: number", "offset: string; limit: number"),
        ("channel_ids: number[]", "channel_ids: string[]"),
        ("strobe_channel: number | null", "strobe_channel: number"),
    ],
    ids=["model", "response", "request-same-name", "array", "nullability"],
)
def test_checker_rejects_representative_typescript_drift(old: str, new: str) -> None:
    document, types = _contract()
    mutated = types.replace(old, new, 1)
    assert mutated != types
    with pytest.raises(AssertionError):
        _checker().validate(document, mutated)
