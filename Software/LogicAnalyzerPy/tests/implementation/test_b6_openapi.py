from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).parents[2]


def _checker() -> object:
    specification = importlib.util.spec_from_file_location(
        "check_openapi_b6", ROOT / "tools/check_openapi_b6.py"
    )
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def test_b6_openapi_is_fingerprinted_additive_and_never_accepts_a_port() -> None:
    b4 = json.loads((ROOT / "web/openapi.json").read_text(encoding="utf-8"))
    b6 = json.loads((ROOT / "web/openapi-b6.json").read_text(encoding="utf-8"))
    types = (ROOT / "web/src/api.b6.generated.ts").read_text(encoding="utf-8")
    checker = _checker()
    checker.validate(b6, types)
    assert set(b4["paths"]) < set(b6["paths"])
    assert set(b6["paths"]) - set(b4["paths"]) == {
        "/api/v1/device/identify",
        "/api/v1/device/reconnect",
        "/api/v1/device/captures",
    }
    request = b6["components"]["schemas"]["LiveCaptureRequest"]
    assert "port" not in request["properties"]
    assert "DeviceInfo" in types and "LiveCaptureRequest" in types
