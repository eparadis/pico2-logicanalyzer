"""Dependency-free structural drift check for the Python-owned local API."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
PATH_METHODS = {
    "/api/v1/health": "get",
    "/api/v1/readiness": "get",
    "/api/v1/imports": "post",
    "/api/v1/captures/{capture_id}": "get",
    "/api/v1/captures/{capture_id}/channels": "get",
    "/api/v1/captures/{capture_id}/waveform": "get",
    "/api/v1/captures/{capture_id}/bus": "post",
    "/api/v1/captures/{capture_id}/exports": "post",
    "/api/v1/operations/{operation_id}": "get",
    "/api/v1/operations/{operation_id}/cancel": "post",
    "/api/v1/shutdown": "post",
}
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
STATUSES = {
    "/api/v1/imports": {"202", "400", "403", "409", "413", "422"},
    "/api/v1/shutdown": {"204", "403"},
}
TS_TYPES = {
    "ErrorEnvelope",
    "Operation",
    "CaptureMetadata",
    "Channel",
    "WaveformWindow",
    "BusRequest",
    "BusPage",
    "ExportRequest",
    "BusRow",
}


def _closed(schema: object) -> None:
    if not isinstance(schema, dict):
        raise AssertionError("schema must be an object")
    if schema.get("type") == "object":
        assert schema.get("additionalProperties") is False
        properties = schema.get("properties", {})
        assert set(schema.get("required", [])) == set(properties)
        for value in properties.values():
            _closed(value)
    if schema.get("type") == "array":
        assert "items" in schema
        _closed(schema["items"])


def validate(document: dict[str, object], types: str) -> None:
    assert document.get("openapi") == "3.1.0"
    paths = document["paths"]
    assert isinstance(paths, dict)
    assert {
        path: {name for name in item if name in HTTP_METHODS} for path, item in paths.items()
    } == {path: {method} for path, method in PATH_METHODS.items()}
    for path, method in PATH_METHODS.items():
        item = paths[path]
        assert isinstance(item, dict)
        operation = item[method]
        assert isinstance(operation, dict) and isinstance(operation.get("responses"), dict)
        if method == "post" and path != "/api/v1/shutdown":
            assert "requestBody" in operation
        assert STATUSES.get(path, set()) <= set(operation["responses"])
        parameters = [*item.get("parameters", []), *operation.get("parameters", [])]
        names = {
            parameter.get("name")
            for parameter in parameters
            if isinstance(parameter, dict)
            and parameter.get("in") == "path"
            and parameter.get("required") is True
        }
        for token in (part[1:-1] for part in path.split("/") if part.startswith("{")):
            assert token in names
            parameter = next(
                parameter for parameter in parameters if parameter.get("name") == token
            )
            assert parameter.get("schema") == {"type": "string", "maxLength": 32}
    artifact = paths["/api/v1/imports"]["post"]["requestBody"]["content"]["multipart/form-data"][
        "schema"
    ]["properties"]["artifact"]
    assert artifact.get("maxLength") == 34603008
    schemas = document["components"]["schemas"]
    assert isinstance(schemas, dict)
    for schema in schemas.values():
        _closed(schema)
    for required in TS_TYPES:
        assert f"{required}" in types
    assert "capture_id: string" in types and "sample_count: number" in types


if __name__ == "__main__":
    validate(
        json.loads((ROOT / "web/openapi.json").read_text()),
        (ROOT / "web/src/api.generated.ts").read_text(),
    )
