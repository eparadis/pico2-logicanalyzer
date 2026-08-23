from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[2]
VALIDATOR = ROOT / "scripts" / "validate_cycle2_evidence.py"
SCHEMA = ROOT / "docs" / "evidence-manifest" / "cycle2-schema.json"


def test_cycle2_validator_rejects_extra_and_secret_fields(tmp_path: Path) -> None:
    manifest = {
        "schema_version": 2,
        "checkpoint": "C2-B1",
        "tested_commit": "0" * 40,
        "tested_tree": "1" * 40,
        "timestamp_utc": "2026-08-22T00:00:00Z",
        "worktree_state": "clean",
        "environment": {"os": "test", "architecture": "test", "python": "3.12", "node": "22"},
        "locks": {
            "requirements_dev": "0" * 64, "requirements_web": "1" * 64,
            "package_lock": "2" * 64, "assets": "3" * 64,
        },
        "roles": {
            "implementation": "implementor", "verification": "verifier", "acceptance": "acceptance",
        },
        "commands": [{"command": "test", "exit_status": 0, "verifier": "test"}],
        "sources": [
            {"category": "synthetic", "revision": "test", "artifact": "x", "sha256": "4" * 64}
        ],
        "stopping_conditions": [{"id": 1, "artifacts": [{"path": "x", "sha256": "5" * 64}]}],
        "findings": [], "decisions": [], "limitations": [], "deferred_work": [],
    }
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    command = [sys.executable, str(VALIDATOR), str(SCHEMA), str(path)]
    assert subprocess.run(command, check=False).returncode == 0
    manifest["machine_url"] = "http://127.0.0.1:1234"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    assert subprocess.run(command, check=False).returncode == 1


@pytest.mark.parametrize(
    ("location", "secret"),
    [
        ("findings", "AbCdEfGhIjKlMnOpQrStUvWxYz0123456789_-abcde"),
        ("artifact", "Authorization: Bearer fixed-hostile-credential"),
        ("findings", "Cookie: pico_la_capability=fixed-hostile-cookie"),
        ("artifact", "api_key=fixed-hostile-credential"),
        ("findings", "password: fixed-hostile-credential"),
    ],
)
def test_cycle2_validator_rejects_literal_secrets_in_nested_and_free_text(
    tmp_path: Path, location: str, secret: str
) -> None:
    manifest = {
        "schema_version": 2,
        "checkpoint": "C2-B1",
        "tested_commit": "0" * 40,
        "tested_tree": "1" * 40,
        "timestamp_utc": "2026-08-22T00:00:00Z",
        "worktree_state": "clean",
        "environment": {"os": "test", "architecture": "test", "python": "3.12", "node": "22"},
        "locks": {
            "requirements_dev": "0" * 64, "requirements_web": "1" * 64,
            "package_lock": "2" * 64, "assets": "3" * 64,
        },
        "roles": {
            "implementation": "implementor", "verification": "verifier", "acceptance": "acceptance",
        },
        "commands": [{"command": "test", "exit_status": 0, "verifier": "test"}],
        "sources": [
            {"category": "synthetic", "revision": "test", "artifact": "fixture", "sha256": "4" * 64}
        ],
        "stopping_conditions": [{"id": 1, "artifacts": [{"path": "x", "sha256": "5" * 64}]}],
        "findings": [], "decisions": [], "limitations": [], "deferred_work": [],
    }
    if location == "artifact":
        manifest["sources"][0]["artifact"] = secret
    else:
        manifest["findings"] = [secret]
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    command = [sys.executable, str(VALIDATOR), str(SCHEMA), str(path)]
    assert subprocess.run(command, check=False).returncode == 1


@pytest.mark.parametrize(
    "prose",
    [
        "Capability token redaction verified with fixed hostile fixtures",
        "authorization required before shutdown",
        "password handling verified",
    ],
)
def test_cycle2_validator_accepts_benign_security_prose(tmp_path: Path, prose: str) -> None:
    manifest = {
        "schema_version": 2,
        "checkpoint": "C2-B1",
        "tested_commit": "0" * 40,
        "tested_tree": "1" * 40,
        "timestamp_utc": "2026-08-22T00:00:00Z",
        "worktree_state": "clean",
        "environment": {"os": "test", "architecture": "test", "python": "3.12", "node": "22"},
        "locks": {
            "requirements_dev": "0" * 64, "requirements_web": "1" * 64,
            "package_lock": "2" * 64, "assets": "3" * 64,
        },
        "roles": {
            "implementation": "implementor", "verification": "verifier", "acceptance": "acceptance",
        },
        "commands": [{"command": "test", "exit_status": 0, "verifier": "test"}],
        "sources": [
            {"category": "synthetic", "revision": "test", "artifact": "fixture", "sha256": "4" * 64}
        ],
        "stopping_conditions": [{"id": 1, "artifacts": [{"path": "x", "sha256": "5" * 64}]}],
        "findings": [prose], "decisions": [], "limitations": [], "deferred_work": [],
    }
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    command = [sys.executable, str(VALIDATOR), str(SCHEMA), str(path)]
    assert subprocess.run(command, check=False).returncode == 0
