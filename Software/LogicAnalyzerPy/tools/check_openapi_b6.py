"""Dependency-free structural drift check for the additive B6 live API."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).parents[1]
PATH_METHODS = {
    "/api/v1/health": "get",
    "/api/v1/readiness": "get",
    "/api/v1/imports": "post",
    "/api/v1/device/identify": "post",
    "/api/v1/device/reconnect": "post",
    "/api/v1/device/captures": "post",
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
    "DeviceInfo",
    "LiveCaptureRequest",
}
OPENAPI_FINGERPRINT = "4d7a1646ecb404a2d2fa659beaff599bb7b633bae7be01377b41036ccaa924de"
TYPES_FINGERPRINT = "2f01d137876ebea792dbb868b37eb7044f172ee3fb395fb8cc42cca6d63179f6"


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


def _typescript_primitive(schema: dict[str, object]) -> str | None:
    enum = schema.get("enum")
    if isinstance(enum, list):
        return " | ".join("null" if value is None else f'"{value}"' for value in enum)
    value_type = schema.get("type")
    if value_type == "string":
        return "string"
    if value_type == "integer" or value_type == "number":
        return "number"
    if value_type == "boolean":
        return "boolean"
    if isinstance(value_type, list) and set(value_type) == {"integer", "null"}:
        return "number | null"
    if isinstance(value_type, list) and set(value_type) == {"string", "null"}:
        return "string | null"
    return None


def _interfaces(types: str) -> dict[str, str]:
    return dict(re.findall(r"export interface (\w+)\s*\{(.*?)\}", types, re.DOTALL))


def _typescript_fields(schema: dict[str, object], fields: str) -> None:
    for name, value in schema.get("properties", {}).items():
        assert isinstance(value, dict)
        primitive = _typescript_primitive(value)
        if primitive is not None:
            expected = f"{name}: {primitive}"
            if name == "state" and "state: OperationState" in fields:
                continue
            else:
                assert expected in fields, f"missing TypeScript field {expected}"
        if value.get("type") == "array":
            items = value.get("items")
            if isinstance(items, dict) and _typescript_primitive(items) is not None:
                assert f"{name}: {_typescript_primitive(items)}[]" in fields
        _typescript_fields(value, fields)


def validate(document: dict[str, object], types: str) -> None:
    # Updating either fingerprint requires a reviewed B4 contract regeneration/change.
    canonical = json.dumps(document, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    assert hashlib.sha256(canonical.encode("utf-8")).hexdigest() == OPENAPI_FINGERPRINT
    assert hashlib.sha256(types.encode("utf-8")).hexdigest() == TYPES_FINGERPRINT
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
    interfaces = _interfaces(types)
    for name, schema in schemas.items():
        _closed(schema)
        if name in interfaces:
            _typescript_fields(schema, interfaces[name])
    bus_decimal = schemas["BusPage"]["properties"]["rows"]["items"]["properties"]["decimal"]
    assert bus_decimal == {"type": "integer"}
    assert "decimal: number" in types
    edge = schemas["CaptureMetadata"]["properties"]["trigger_edge"]
    assert edge == {"enum": ["rising", "falling"]}
    assert 'trigger_edge: "rising" | "falling"' in types
    strobe = schemas["BusRequest"]["properties"]["strobe_channel"]
    assert strobe == {"type": ["integer", "null"]}
    assert "strobe_channel: number | null" in interfaces["BusRequest"]
    for required in TS_TYPES:
        assert f"{required}" in types
    assert "capture_id: string" in types and "sample_count: number" in types
    assert "device_id: string" in types and "timeout_seconds: number" in types


if __name__ == "__main__":
    validate(
        json.loads((ROOT / "web/openapi-b6.json").read_text()),
        (ROOT / "web/src/api.b6.generated.ts").read_text(),
    )
