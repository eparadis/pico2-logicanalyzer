"""Mutation regressions for the Python-owned OpenAPI structural checker."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[2]
SPEC = importlib.util.spec_from_file_location("openapi_check", ROOT / "tools/check_openapi.py")
assert SPEC is not None and SPEC.loader is not None
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def _contract() -> tuple[dict[str, object], str]:
    return (
        json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8")),
        (ROOT / "web/src/api.generated.ts").read_text(encoding="utf-8"),
    )


def _fails(change: object, types: str | None = None) -> None:
    document, canonical_types = _contract()
    mutated = copy.deepcopy(document)
    assert isinstance(change, type(lambda: None))
    change(mutated)
    with pytest.raises(AssertionError):
        checker.validate(mutated, canonical_types if types is None else types)


def test_checker_rejects_route_method_and_status_drift() -> None:
    _fails(lambda document: document["paths"].pop("/api/v1/health"))
    _fails(lambda document: document["paths"]["/api/v1/health"].update({"post": {}}))
    _fails(lambda document: document["paths"]["/api/v1/imports"]["post"]["responses"].pop("413"))


@pytest.mark.parametrize("key", ["name", "required", "schema"])
def test_checker_rejects_path_parameter_drift(key: str) -> None:
    def change(document: dict[str, object]) -> None:
        parameter = document["paths"]["/api/v1/captures/{capture_id}"]["get"]["parameters"][0]
        parameter[key] = False if key == "required" else "wrong"

    _fails(change)


def test_checker_rejects_nested_closure_and_upload_drift() -> None:
    _fails(
        lambda document: document["components"]["schemas"]["BusPage"]["properties"]["rows"][
            "items"
        ]["properties"].pop("decimal")
    )


def test_checker_rejects_primitive_and_enum_wire_drift() -> None:
    _fails(
        lambda document: document["components"]["schemas"]["BusPage"]["properties"][
            "rows"
        ]["items"]["properties"]["decimal"].update({"type": "string"})
    )
    _fails(
        lambda document: document["components"]["schemas"]["CaptureMetadata"][
            "properties"
        ]["trigger_edge"].update({"enum": ["rising"]})
    )
    _fails(
        lambda document: document["components"]["schemas"]["WaveformWindow"]["properties"][
            "channels"
        ]["items"].update({"additionalProperties": True})
    )
    _fails(
        lambda document: document["paths"]["/api/v1/imports"]["post"]["requestBody"]["content"][
            "multipart/form-data"
        ]["schema"]["properties"]["artifact"].update({"maxLength": 1})
    )


def test_checker_rejects_generated_type_structure_drift() -> None:
    document, types = _contract()
    with pytest.raises(AssertionError):
        checker.validate(document, types.replace("capture_id: string", "capture_id: number"))
    with pytest.raises(AssertionError):
        checker.validate(document, types.replace("decimal: number", "decimal: string"))
