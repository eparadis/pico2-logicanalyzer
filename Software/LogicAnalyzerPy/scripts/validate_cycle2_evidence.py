#!/usr/bin/env python3
"""Strict, dependency-free validator for Cycle 2 checkpoint evidence."""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
CHECKPOINT = re.compile(r"^C2-B[1-6]$")
SECRET = re.compile(
    r"/dev/(?:tty|cu\.|serial/)|https?://(?:localhost|127\.0\.0\.1|\[)|/(?:Users|home)/"
    r"|authorization\s*(?::|=)?\s*(?:bearer|basic)\s+[^\s,;]+"
    r"|(?:cookie|set-cookie)\s*:\s*[^\s,;]+"
    r"|(?:pico_la_capability|token|api[_-]?key|password)\s*(?:=|:)\s*[^\s,;]+"
    r"|(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{43}(?![A-Za-z0-9_-])",
    re.I,
)
REQUIRED = {
    "schema_version", "checkpoint", "tested_commit", "tested_tree", "timestamp_utc",
    "worktree_state", "environment", "locks", "roles", "commands", "sources",
    "stopping_conditions", "findings", "decisions", "limitations", "deferred_work",
}
OPTIONAL = {"performance_threshold_sha256"}


def _string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or SECRET.search(value):
        raise ValueError(f"invalid or secret-bearing {label}")
    return value


def _object(value: object, required: set[str], allowed: set[str], label: str) -> dict[str, object]:
    if not isinstance(value, dict) or set(value) - allowed or required - set(value):
        raise ValueError(f"invalid fields in {label}")
    return value


def _digest(value: object, label: str) -> None:
    if value != "not-applicable" and (not isinstance(value, str) or not HEX64.fullmatch(value)):
        raise ValueError(f"invalid {label} digest")


def _strings(value: object, label: str) -> None:
    """Reject prohibited values in every free-text leaf, not just typed fields."""
    if isinstance(value, str):
        _string(value, label)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _strings(item, f"{label}[{index}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"invalid key in {label}")
            _strings(item, f"{label}.{key}")


def validate(value: object) -> None:
    data = _object(value, REQUIRED, REQUIRED | OPTIONAL, "manifest")
    checkpoint = _string(data["checkpoint"], "checkpoint")
    if data["schema_version"] != 2 or not CHECKPOINT.fullmatch(checkpoint):
        raise ValueError("invalid schema version or checkpoint")
    for key in ("tested_commit", "tested_tree"):
        if not HEX40.fullmatch(_string(data[key], key)):
            raise ValueError(f"invalid {key}")
    timestamp = _string(data["timestamp_utc"], "timestamp_utc")
    try:
        if not timestamp.endswith("Z"):
            raise ValueError
        datetime.fromisoformat(timestamp.removesuffix("Z") + "+00:00")
    except ValueError as exc:
        raise ValueError("invalid timestamp_utc") from exc
    worktree_state = _string(data["worktree_state"], "worktree_state")
    if len(worktree_state) > 2048:
        raise ValueError("worktree_state is too long")
    environment = _object(
        data["environment"],
        {"os", "architecture", "python", "node"},
        {"os", "architecture", "python", "node", "browser", "automation"},
        "environment",
    )
    for key, item in environment.items():
        _string(item, f"environment.{key}")
    lock_keys = {"requirements_dev", "requirements_web", "package_lock", "assets"}
    locks = _object(data["locks"], lock_keys, lock_keys, "locks")
    for key, item in locks.items():
        _digest(item, f"locks.{key}")
    role_keys = {"implementation", "verification", "acceptance"}
    roles = _object(data["roles"], role_keys, role_keys, "roles")
    if len({_string(item, f"roles.{key}") for key, item in roles.items()}) != 3:
        raise ValueError("role identities must be distinct")
    list_keys = (
        "commands", "sources", "stopping_conditions", "findings", "decisions", "limitations",
        "deferred_work",
    )
    for key in list_keys:
        if not isinstance(data[key], list):
            raise ValueError(f"{key} must be an array")
    for command in data["commands"]:
        item = _object(
            command, {"command", "exit_status", "verifier"},
            {"command", "exit_status", "verifier", "ci"}, "command",
        )
        _string(item["command"], "command")
        _string(item["verifier"], "verifier")
        if not isinstance(item["exit_status"], int) or not 0 <= item["exit_status"] <= 255:
            raise ValueError("invalid command exit status")
    for source in data["sources"]:
        source_keys = {"category", "revision", "artifact", "sha256"}
        item = _object(source, source_keys, source_keys, "source")
        categories = {
            "firmware-source", "cycle1-accepted", "synthetic", "hardware-observation",
            "browser-observation", "generated-fixture",
        }
        if item["category"] not in categories:
            raise ValueError("invalid source category")
        _string(item["revision"], "revision")
        _string(item["artifact"], "artifact")
        _digest(item["sha256"], "source")
    for condition in data["stopping_conditions"]:
        item = _object(condition, {"id", "artifacts"}, {"id", "artifacts"}, "condition")
        if type(item["id"]) is not int or not 1 <= item["id"] <= 14:
            raise ValueError("invalid stopping condition id")
        if not isinstance(item["artifacts"], list):
            raise ValueError("condition artifacts must be an array")
        for artifact in item["artifacts"]:
            proof = _object(artifact, {"path", "sha256"}, {"path", "sha256"}, "artifact")
            _string(proof["path"], "artifact path")
            _digest(proof["sha256"], "artifact")
    for key in ("findings", "decisions", "limitations", "deferred_work"):
        _strings(data[key], key)
    if "performance_threshold_sha256" in data:
        _digest(data["performance_threshold_sha256"], "performance threshold")


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        return 2
    try:
        schema, manifest = map(Path, argv[1:])
        if json.loads(schema.read_text(encoding="utf-8")).get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            raise ValueError("schema is not draft 2020-12")
        validate(json.loads(manifest.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"cycle2-evidence: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
