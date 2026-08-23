"""Independent C2-B1 boundary checks derived from the governing contracts."""

from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import time
import tomllib
import urllib.error
import urllib.request
from http.cookies import SimpleCookie
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[2]
VALIDATOR = ROOT / "scripts" / "validate_cycle2_evidence.py"


def _validator_module() -> object:
    spec = importlib.util.spec_from_file_location("cycle2_validator", VALIDATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _manifest() -> dict[str, object]:
    digest = "a" * 64
    return {
        "schema_version": 2,
        "checkpoint": "C2-B1",
        "tested_commit": "b" * 40,
        "tested_tree": "c" * 40,
        "timestamp_utc": "2026-08-22T00:00:00Z",
        "worktree_state": "clean",
        "environment": {"os": "test", "architecture": "x86_64", "python": "3.12", "node": "22.14.0"},
        "locks": {"requirements_dev": digest, "requirements_web": digest, "package_lock": digest, "assets": digest},
        "roles": {"implementation": "implementor", "verification": "verifier", "acceptance": "acceptance"},
        "commands": [{"command": "check", "exit_status": 0, "verifier": "verifier"}],
        "sources": [{"category": "synthetic", "revision": "literal", "artifact": "fixture", "sha256": digest}],
        "stopping_conditions": [{"id": 1, "artifacts": [{"path": "proof.json", "sha256": digest}]}],
        "findings": [],
        "decisions": [],
        "limitations": [],
        "deferred_work": [],
    }


def test_validator_rejects_unknown_nested_stopping_condition_field() -> None:
    validator = _validator_module()
    manifest = _manifest()
    condition = manifest["stopping_conditions"][0]  # type: ignore[index]
    condition["unexpected"] = "must be rejected"  # type: ignore[index]
    try:
        validator.validate(manifest)  # type: ignore[attr-defined]
    except ValueError:
        return
    raise AssertionError("recursive no-extra-properties policy was not enforced")


def test_validator_rejects_secret_in_free_text_arrays() -> None:
    validator = _validator_module()
    manifest = _manifest()
    manifest["findings"] = ["browser URL was http://[::1]:4173"]
    try:
        validator.validate(manifest)  # type: ignore[attr-defined]
    except ValueError:
        return
    raise AssertionError("secret-bearing finding was accepted")


def _free_port() -> int:
    try:
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            return int(sock.getsockname()[1])
    except PermissionError:
        pytest.skip("sandbox prohibits loopback socket verification")


def _open(request: urllib.request.Request, timeout: float = 0.5) -> object:
    return urllib.request.urlopen(request, timeout=timeout)


def test_orderly_shutdown_stops_production_process() -> None:
    port = _free_port()
    process = subprocess.Popen(
        [sys.executable, "-m", "pico_logic_analyzer", "web", "--port", str(port)],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    origin = f"http://127.0.0.1:{port}"
    try:
        response = None
        for _ in range(40):
            try:
                response = _open(urllib.request.Request(origin + "/"))
                break
            except (urllib.error.URLError, TimeoutError):
                time.sleep(0.05)
        assert response is not None, "production server never became reachable"
        cookie = SimpleCookie()
        cookie.load(response.headers["Set-Cookie"])
        capability = cookie["pico_la_capability"].value
        shutdown = urllib.request.Request(
            origin + "/api/v1/shutdown",
            data=b"",
            method="POST",
            headers={"Origin": origin, "Cookie": f"pico_la_capability={capability}"},
        )
        assert _open(shutdown).status == 204
        try:
            process.wait(timeout=1.0)
        except subprocess.TimeoutExpired as exc:
            raise AssertionError("successful orderly shutdown did not stop the server") from exc
        assert process.returncode == 0
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=2)


def test_evidence_json_schema_is_recursively_strict() -> None:
    schema = json.loads((ROOT / "docs/evidence-manifest/cycle2-schema.json").read_text())
    condition = schema["$defs"]["condition"]
    artifact = condition["properties"]["artifacts"]["items"]
    assert condition["additionalProperties"] is False
    assert artifact["additionalProperties"] is False


def test_web_runtime_lock_contains_core_runtime_dependencies() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    lock = (ROOT / "requirements-web.lock").read_text(encoding="utf-8")
    locked_names = {
        line.split("==", 1)[0].strip().lower()
        for line in lock.splitlines()
        if line and not line.startswith((" ", "#")) and "==" in line
    }
    required_names = {
        requirement.split("==", 1)[0].strip().lower()
        for requirement in project["project"]["dependencies"]
    }
    assert required_names <= locked_names, "web lock is not a complete application runtime closure"


def test_package_data_rule_covers_nested_production_assets() -> None:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    patterns = project["tool"]["setuptools"]["package-data"]["pico_logic_analyzer"]
    assert "web/assets/assets/*" in patterns, "built wheel omits hashed JavaScript/CSS assets"


def test_cli_accepts_os_assigned_loopback_port() -> None:
    from pico_logic_analyzer.web.server import create_app

    app = create_app("127.0.0.1", 0)
    assert app["canonical_port"] == 0
