"""Small dependency-free guard for the reviewed Python-owned API contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
document = json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8"))
assert document["openapi"] == "3.1.0"
paths = document["paths"]
required = {"/api/v1/health", "/api/v1/readiness", "/api/v1/imports", "/api/v1/shutdown"}
assert required <= set(paths)
schemas = document["components"]["schemas"]
assert all(value.get("additionalProperties") is False for value in schemas.values())
assert set(schemas["Operation"]["properties"]["state"]["enum"]) == {
    "pending", "running", "cancelling", "succeeded", "failed", "cancelled"
}
