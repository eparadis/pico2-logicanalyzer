#!/usr/bin/env python3
"""Strict, dependency-free validator for Cycle 3 checkpoint evidence."""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any, cast

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
CHECKPOINT = re.compile(r"^C3-B([1-5])$")
REQUIREMENT = re.compile(r"^R(?:[1-9]|1[0-9]|2[0-6])$")
PYTHON_312 = re.compile(r"^3\.12(?:\.|$)")
SAFE_ID = re.compile(r"^[A-Za-z0-9._-]+$")
SAFE_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
SECRET = re.compile(
    r"/dev/(?:tty|cu\.|serial/)|https?://(?:localhost|127\.0\.0\.1|\[)|/(?:Users|home)/"
    r"|authorization\s*(?::|=)?\s*(?:bearer|basic)\s+[^\s,;]+"
    r"|(?:cookie|set-cookie)\s*:\s*[^\s,;]+"
    r"|(?:pico_la_capability|token|api[_-]?key|password)\s*(?:=|:)\s*[^\s,;]+"
    r"|(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{43}(?![A-Za-z0-9_-])",
    re.I,
)

ROOT_REQUIRED = {
    "schema_version", "checkpoint", "tested_commit", "tested_tree", "timestamp_utc",
    "worktree_state", "environment", "locks", "roles", "commands", "artifacts",
    "requirements", "stopping_conditions", "findings", "decisions", "limitations",
    "deferred_work", "audits",
}
ROOT_OPTIONAL = {"hosted_ci", "b1_evidence", "final_measurements"}


def fail(message: str) -> None:
    raise ValueError(message)


def obj(value: object, required: set[str], optional: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    raw = cast(dict[Any, Any], value)
    if any(not isinstance(key, str) for key in raw):
        fail(f"{label} has a non-string key")
    result = cast(dict[str, Any], raw)
    keys = set(result)
    if missing := required - keys:
        fail(f"missing fields in {label}: {', '.join(sorted(missing))}")
    if extra := keys - required - optional:
        fail(f"unexpected fields in {label}: {', '.join(sorted(extra))}")
    return result


def array(value: object, label: str, *, nonempty: bool = False) -> list[Any]:
    if not isinstance(value, list) or (nonempty and not value):
        fail(f"{label} must be {'a non-empty' if nonempty else 'an'} array")
    return cast(list[Any], value)


def string(value: object, label: str, *, max_length: int | None = None) -> str:
    if not isinstance(value, str) or not value or SECRET.search(value):
        fail(f"invalid or sensitive {label}")
    result = cast(str, value)
    if max_length is not None and len(result) > max_length:
        fail(f"{label} is too long")
    return result


def digest(value: object, label: str) -> str:
    result = string(value, label)
    if not HEX64.fullmatch(result):
        fail(f"invalid {label} digest")
    return result


def commit(value: object, label: str) -> str:
    result = string(value, label)
    if not HEX40.fullmatch(result):
        fail(f"invalid {label}")
    return result


def path(value: object, label: str) -> str:
    result = string(value, label)
    pure = PurePosixPath(result)
    if pure.is_absolute() or "\\" in result or ".." in pure.parts:
        fail(f"{label} must be a repository-relative path")
    return result


def reference(value: object, label: str) -> None:
    item = obj(value, {"path", "sha256"}, set(), label)
    path(item["path"], f"{label}.path")
    digest(item["sha256"], f"{label}.sha256")


def references(value: object, label: str) -> None:
    for index, item in enumerate(array(value, label, nonempty=True)):
        reference(item, f"{label}[{index}]")


def free_text(value: object, label: str) -> None:
    if isinstance(value, str):
        string(value, label)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            free_text(item, f"{label}[{index}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                fail(f"invalid key in {label}")
            free_text(item, f"{label}.{key}")


def validate_environment(value: object) -> None:
    item = obj(
        value,
        {"os", "architecture", "python", "environment_class"},
        {"resource_observation"},
        "environment",
    )
    if not string(item["os"], "environment.os").startswith("macOS "):
        fail("Cycle 3 environment must be macOS")
    if item["architecture"] not in {"arm64", "x86_64"}:
        fail("invalid environment.architecture")
    if not PYTHON_312.match(string(item["python"], "environment.python")):
        fail("Cycle 3 Python must be 3.12")
    string(item["environment_class"], "environment.environment_class")
    if "resource_observation" in item:
        string(item["resource_observation"], "environment.resource_observation")


def validate_roles(value: object, checkpoint: str) -> None:
    item = obj(
        value,
        {"implementation", "verification", "acceptance", "manifest_verifier"},
        {"b1_internal"},
        "roles",
    )
    identities = [string(item[key], f"roles.{key}") for key in (
        "implementation", "verification", "acceptance", "manifest_verifier"
    )]
    if len(set(identities)) != len(identities):
        fail("primary role identities must be distinct")
    if checkpoint == "C3-B1":
        if "b1_internal" not in item:
            fail("C3-B1 requires roles.b1_internal")
        keys = {
            "semantic_fixture_implementation", "semantic_fixture_verification",
            "semantic_fixture_acceptance", "runner_implementation",
            "runner_verification", "runner_acceptance",
        }
        internal = obj(item["b1_internal"], keys, set(), "roles.b1_internal")
        internal_ids = [string(internal[key], f"roles.b1_internal.{key}") for key in sorted(keys)]
        if len(set(internal_ids)) != 6:
            fail("all six C3-B1 internal identities must be distinct")
        if set(internal_ids) & set(identities[1:]):
            fail("C3-B1 internal identities must be distinct from final evidence roles")
    elif "b1_internal" in item:
        fail("roles.b1_internal is permitted only for C3-B1")


def validate_commands(value: object, tested_commit: str) -> None:
    required = {
        "name", "command", "exit_status", "verifier", "candidate_commit", "result", "skipped"
    }
    for index, raw in enumerate(array(value, "commands", nonempty=True)):
        item = obj(raw, required, {"evidence"}, f"commands[{index}]")
        for key in ("name", "command", "verifier", "result"):
            string(item[key], f"commands[{index}].{key}")
        if type(item["exit_status"]) is not int or not 0 <= item["exit_status"] <= 255:
            fail(f"invalid commands[{index}].exit_status")
        if item["skipped"] is not False:
            fail(f"commands[{index}] may not represent a skipped mandatory gate")
        if commit(item["candidate_commit"], f"commands[{index}].candidate_commit") != tested_commit:
            fail(f"commands[{index}] is bound to a different candidate")
        if "evidence" in item:
            references(item["evidence"], f"commands[{index}].evidence")


def validate_artifacts(value: object) -> None:
    categories = {
        "accepted-baseline", "decoder-snapshot", "fixture-source", "generated-fixture",
        "method", "raw-observation", "threshold", "review", "operator-decision",
        "project-legal", "test", "workflow", "process-audit", "scope-audit",
        "rollback", "checkpoint",
    }
    required = {"category", "provenance", "revision", "path", "sha256"}
    seen_paths: set[str] = set()
    for index, raw in enumerate(array(value, "artifacts", nonempty=True)):
        item = obj(raw, required, {"counts"}, f"artifacts[{index}]")
        if item["category"] not in categories:
            fail(f"invalid artifacts[{index}].category")
        string(item["provenance"], f"artifacts[{index}].provenance")
        string(item["revision"], f"artifacts[{index}].revision")
        artifact_path = path(item["path"], f"artifacts[{index}].path")
        if artifact_path in seen_paths:
            fail(f"duplicate artifact path: {artifact_path}")
        seen_paths.add(artifact_path)
        digest(item["sha256"], f"artifacts[{index}].sha256")
        if "counts" in item:
            count_names: set[str] = set()
            counts = array(item["counts"], f"artifacts[{index}].counts")
            for count_index, raw_count in enumerate(counts):
                count_item = obj(
                    raw_count, {"name", "value"}, set(),
                    f"artifacts[{index}].counts[{count_index}]",
                )
                count_name = string(
                    count_item["name"], f"artifacts[{index}].counts[{count_index}].name"
                )
                if not SAFE_NAME.fullmatch(count_name) or count_name in count_names:
                    fail(f"invalid or duplicate artifact count name: {count_name}")
                count_names.add(count_name)
                if type(count_item["value"]) is not int or count_item["value"] < 0:
                    fail(f"invalid artifacts[{index}].counts[{count_index}].value")


def validate_mappings(data: dict[str, Any]) -> None:
    requirement_ids: list[str] = []
    for index, raw in enumerate(array(data["requirements"], "requirements", nonempty=True)):
        item = obj(raw, {"id", "status", "evidence"}, set(), f"requirements[{index}]")
        req_id = string(item["id"], f"requirements[{index}].id")
        if not REQUIREMENT.fullmatch(req_id) or item["status"] != "pass":
            fail(f"invalid requirements[{index}]")
        references(item["evidence"], f"requirements[{index}].evidence")
        requirement_ids.append(req_id)
    if len(set(requirement_ids)) != len(requirement_ids):
        fail("duplicate requirement id")

    condition_ids: list[int] = []
    conditions = array(data["stopping_conditions"], "stopping_conditions", nonempty=True)
    for index, raw in enumerate(conditions):
        item = obj(raw, {"id", "status", "evidence"}, set(), f"stopping_conditions[{index}]")
        if type(item["id"]) is not int or not 1 <= item["id"] <= 18 or item["status"] != "pass":
            fail(f"invalid stopping_conditions[{index}]")
        references(item["evidence"], f"stopping_conditions[{index}].evidence")
        condition_ids.append(item["id"])
    if len(set(condition_ids)) != len(condition_ids):
        fail("duplicate stopping condition id")
    if data["checkpoint"] == "C3-B5":
        if set(requirement_ids) != {f"R{number}" for number in range(1, 27)}:
            fail("C3-B5 must map every requirement R1-R26")
        if set(condition_ids) != set(range(1, 18)):
            fail(
                "pre-manifest C3-B5 may map exactly stopping conditions 1-17; "
                "condition 18 closes later"
            )


def validate_findings_decisions(data: dict[str, Any]) -> None:
    finding_ids: set[str] = set()
    for index, raw in enumerate(array(data["findings"], "findings")):
        item = obj(raw, {"id", "status", "disposition", "evidence"}, set(), f"findings[{index}]")
        finding_id = string(item["id"], f"findings[{index}].id")
        if finding_id in finding_ids or item["status"] not in {"closed", "accepted-limitation"}:
            fail(f"invalid findings[{index}]")
        finding_ids.add(finding_id)
        string(item["disposition"], f"findings[{index}].disposition")
        references(item["evidence"], f"findings[{index}].evidence")
    for index, raw in enumerate(array(data["decisions"], "decisions")):
        item = obj(raw, {"authority", "decision", "evidence"}, set(), f"decisions[{index}]")
        string(item["authority"], f"decisions[{index}].authority")
        string(item["decision"], f"decisions[{index}].decision")
        references(item["evidence"], f"decisions[{index}].evidence")
    for key in ("limitations", "deferred_work"):
        for index, value in enumerate(array(data[key], key)):
            string(value, f"{key}[{index}]")


def validate_audits(value: object) -> None:
    categories = {
        "prohibited-runtime", "dependency", "process", "import", "scope", "license",
        "rollback", "repository",
    }
    for index, raw in enumerate(array(value, "audits", nonempty=True)):
        item = obj(raw, {"category", "verdict", "scope", "evidence"}, set(), f"audits[{index}]")
        if item["category"] not in categories or item["verdict"] != "pass":
            fail(f"invalid audits[{index}]")
        string(item["scope"], f"audits[{index}].scope")
        references(item["evidence"], f"audits[{index}].evidence")


def validate_optional(data: dict[str, Any], tested_commit: str) -> None:
    checkpoint = data["checkpoint"]
    if checkpoint in {"C3-B4", "C3-B5"} and "hosted_ci" not in data:
        fail(f"{checkpoint} requires exact-candidate hosted_ci")
    if "hosted_ci" in data:
        ci_keys = {"provider", "run_id", "job_id", "candidate_commit", "platform", "result"}
        item = obj(data["hosted_ci"], ci_keys, set(), "hosted_ci")
        string(item["provider"], "hosted_ci.provider")
        for key in ("run_id", "job_id"):
            if not SAFE_ID.fullmatch(string(item[key], f"hosted_ci.{key}")):
                fail(f"invalid hosted_ci.{key}")
        if commit(item["candidate_commit"], "hosted_ci.candidate_commit") != tested_commit:
            fail("hosted_ci is bound to a different candidate")
        if item["platform"] != "macOS" or item["result"] != "success":
            fail("hosted_ci must be a successful macOS job")
    if checkpoint == "C3-B1" and "b1_evidence" not in data:
        fail("C3-B1 requires b1_evidence")
    if "b1_evidence" in data:
        keys = {
            "fixture_candidate", "runner_candidate", "raw_candidate", "threshold_candidate",
            "project_legal", "operator_decision",
        }
        item = obj(data["b1_evidence"], keys, set(), "b1_evidence")
        for key in sorted(keys):
            reference(item[key], f"b1_evidence.{key}")
    if checkpoint == "C3-B5" and "final_measurements" not in data:
        fail("C3-B5 requires final_measurements")
    if "final_measurements" in data:
        measurements = array(data["final_measurements"], "final_measurements", nonempty=True)
        measurement_keys = {"name", "observed", "ceiling", "unit", "status", "evidence"}
        for index, raw in enumerate(measurements):
            item = obj(
                raw, measurement_keys, set(), f"final_measurements[{index}]"
            )
            string(item["name"], f"final_measurements[{index}].name")
            string(item["unit"], f"final_measurements[{index}].unit")
            for key in ("observed", "ceiling"):
                number = item[key]
                if (
                    isinstance(number, bool)
                    or not isinstance(number, int | float)
                    or not math.isfinite(number)
                ):
                    fail(f"invalid final_measurements[{index}].{key}")
            if item["observed"] < 0 or item["ceiling"] <= 0 or item["status"] != "pass":
                fail(f"invalid final_measurements[{index}]")
            reference(item["evidence"], f"final_measurements[{index}].evidence")


def validate(value: object) -> None:
    data = obj(value, ROOT_REQUIRED, ROOT_OPTIONAL, "manifest")
    if data["schema_version"] != 3:
        fail("invalid schema_version")
    checkpoint = string(data["checkpoint"], "checkpoint")
    if not CHECKPOINT.fullmatch(checkpoint):
        fail("invalid checkpoint")
    tested_commit = commit(data["tested_commit"], "tested_commit")
    commit(data["tested_tree"], "tested_tree")
    timestamp = string(data["timestamp_utc"], "timestamp_utc")
    try:
        if not timestamp.endswith("Z"):
            raise ValueError
        datetime.fromisoformat(timestamp.removesuffix("Z") + "+00:00")
    except ValueError as exc:
        raise ValueError("invalid timestamp_utc") from exc
    string(data["worktree_state"], "worktree_state", max_length=2048)
    validate_environment(data["environment"])
    for index, raw in enumerate(array(data["locks"], "locks", nonempty=True)):
        item = obj(raw, {"name", "path", "sha256"}, set(), f"locks[{index}]")
        string(item["name"], f"locks[{index}].name")
        path(item["path"], f"locks[{index}].path")
        digest(item["sha256"], f"locks[{index}].sha256")
    validate_roles(data["roles"], checkpoint)
    validate_commands(data["commands"], tested_commit)
    validate_artifacts(data["artifacts"])
    validate_mappings(data)
    validate_findings_decisions(data)
    validate_audits(data["audits"])
    validate_optional(data, tested_commit)
    free_text(data, "manifest")


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: validate_cycle3_evidence.py SCHEMA MANIFEST", file=sys.stderr)
        return 2
    try:
        schema_path, manifest_path = map(Path, argv[1:])
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            fail("schema is not draft 2020-12")
        if schema.get("additionalProperties") is not False:
            fail("schema root is not strict")
        validate(json.loads(manifest_path.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"cycle3-evidence: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
