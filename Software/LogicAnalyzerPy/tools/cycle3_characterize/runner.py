"""Closed, non-installed pre-execution runner; it imports no decoder."""

from __future__ import annotations

import hashlib
import json
import os
import secrets
import selectors
import struct
import subprocess
import sys
import time
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .accounting import (
    AccountingFailure,
    CapProfile,
    derived_test_profile,
    result_measurements,
    validate_result,
)
from .snapshot_host import SnapshotHostFailure, validate_characterization_request

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = ROOT.parents[1]
TOOL_ROOT = Path(__file__).resolve().parent
DATA_ROOT = ROOT / "testdata" / "decoders" / "cycle3"
BINDING = TOOL_ROOT / "candidate-binding.json"
CAPS_SHA256 = "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d"
SEMANTIC_FIXTURE_SHA256 = "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
FIXTURE_MANIFEST_SHA256 = "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9"
FIXTURE_CANDIDATE_COMMIT = "3af6b9f80dd52611e14acca407707d1da7b8d9ac"
FIXTURE_CANDIDATE_TREE = "14c010153ea5542617e601e4126047c561a48483"
PROTOCOL_VERSION = 1
STDLIB_ALLOWLIST = [
    "argparse",
    "base64",
    "collections",
    "dataclasses",
    "enum",
    "hashlib",
    "itertools",
    "json",
    "math",
    "mmap",
    "os",
    "pathlib",
    "re",
    "resource",
    "secrets",
    "selectors",
    "signal",
    "struct",
    "subprocess",
    "sys",
    "time",
    "typing",
    "types",
]


class RunnerFailure(RuntimeError):
    """Stable failure with no child traceback or local path disclosure."""


@dataclass(frozen=True)
class RunResult:
    value: dict[str, Any]
    stdout: bytes
    stderr: bytes
    diagnostics: bytes
    launch_ns: int
    reap_ns: int
    total_ns: int
    counts: Mapping[str, int]


@dataclass(frozen=True)
class _PrivateRunEvidence:
    pid: int
    disposition: str
    reaped: bool
    descriptors_closed: bool
    closed_fds: tuple[int, ...]
    total_ns: int
    terminate_to_reap_ns: int
    kill_to_reap_ns: int


_LAST_PRIVATE_EVIDENCE: _PrivateRunEvidence | None = None


def _private_last_evidence() -> _PrivateRunEvidence:
    if _LAST_PRIVATE_EVIDENCE is None:
        raise RunnerFailure("no private run evidence")
    return _LAST_PRIVATE_EVIDENCE


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_file(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    current = root
    for part in path.relative_to(root).parts:
        current /= part
        if current.is_symlink():
            return False
    return path.is_file() and not path.is_symlink()


def _verify_tool_inventory(_tool_root: Path | None = None) -> None:
    root = _tool_root or TOOL_ROOT
    allowed = {
        "__init__.py",
        "accounting.py",
        "binding.py",
        "candidate-binding.json",
        "launch.json",
        "probes.py",
        "runner.py",
        "snapshot_host.py",
        "worker.py",
    }
    if root.is_symlink() or not root.is_dir():
        raise RunnerFailure("tool root rejected")
    entries = {item.name for item in root.iterdir()}
    if entries != allowed or any(item.is_symlink() for item in root.iterdir()):
        raise RunnerFailure("tool inventory rejected")


def _path(relative: str) -> Path:
    if not isinstance(relative, str) or ".." in Path(relative).parts:
        raise RunnerFailure("bound path rejected")
    root = REPOSITORY if relative.startswith("Software/") else ROOT
    path = root / relative
    if not _safe_file(path, root):
        raise RunnerFailure("bound path rejected")
    return path


def expected_sources() -> set[str]:
    provenance = json.loads((DATA_ROOT / "provenance.json").read_text(encoding="utf-8"))
    snapshots = {item["path"] for item in provenance["files"]}
    return snapshots | {
        "docs/cycle-3-characterization-method.md",
        "testdata/decoders/cycle3/experiment-caps.json",
        "testdata/decoders/cycle3/manifest.json",
        "testdata/decoders/cycle3/option-matrix.json",
        "testdata/decoders/cycle3/provenance.json",
        "testdata/decoders/cycle3/semantic-fixtures.json",
        "testdata/decoders/cycle3/typed-vectors.json",
        "tools/cycle3_characterize/__init__.py",
        "tools/cycle3_characterize/accounting.py",
        "tools/cycle3_characterize/binding.py",
        "tools/cycle3_characterize/launch.json",
        "tools/cycle3_characterize/probes.py",
        "tools/cycle3_characterize/runner.py",
        "tools/cycle3_characterize/snapshot_host.py",
        "tools/cycle3_characterize/worker.py",
    }


def binding_payload() -> dict[str, object]:
    sources = {name: _digest(_path(name)) for name in sorted(expected_sources())}
    return {
        "schema": "cycle3-characterize-binding/v3",
        "accepted_fixture": {
            "candidate_commit": FIXTURE_CANDIDATE_COMMIT,
            "candidate_tree": FIXTURE_CANDIDATE_TREE,
            "caps_sha256": CAPS_SHA256,
            "semantic_fixture_sha256": SEMANTIC_FIXTURE_SHA256,
            "manifest_sha256": FIXTURE_MANIFEST_SHA256,
        },
        "sources": sources,
    }


def load_caps() -> dict[str, int]:
    path = DATA_ROOT / "experiment-caps.json"
    if not _safe_file(path, DATA_ROOT) or _digest(path) != CAPS_SHA256:
        raise RunnerFailure("accepted caps rejected")
    caps = json.loads(path.read_text(encoding="utf-8"))["caps"]
    result = {item["id"]: item["value"] for item in caps}
    if len(result) != 17 or any(type(value) is not int or value <= 0 for value in result.values()):
        raise RunnerFailure("accepted cap profile rejected")
    return result


def production_profile() -> CapProfile:
    """The only profile reachable from a future characterization request."""
    return CapProfile(load_caps())


def private_test_profile(overrides: Mapping[str, int]) -> CapProfile:
    """Test-only profile factory; no characterization call accepts this value."""
    return derived_test_profile(production_profile(), overrides)


def _verify_provenance() -> dict[str, tuple[str, ...]]:
    provenance = json.loads((DATA_ROOT / "provenance.json").read_text(encoding="utf-8"))
    files = {item["path"]: item["sha256"] for item in provenance["files"]}
    if len(files) != 9:
        raise RunnerFailure("snapshot file set rejected")
    for name, digest in files.items():
        if _digest(_path(name)) != digest:
            raise RunnerFailure("snapshot identity rejected")
    result = {}
    for item in provenance["decoder_file_sets"]:
        names = tuple(item["paths"])
        if not names or any(name not in files for name in names):
            raise RunnerFailure("ordered source set rejected")
        encoded = b"".join(name.encode() + b"\0" + files[name].encode() + b"\n" for name in names)
        if hashlib.sha256(encoded).hexdigest() != item["sha256"]:
            raise RunnerFailure("ordered source digest rejected")
        result[item["decoder"]] = names
    if set(result) != {"uart", "spi", "i2c"}:
        raise RunnerFailure("decoder set rejected")
    return result


def verify_launch_identity(
    _binding_path: Path | None = None, _binding_data: object | None = None
) -> None:
    _verify_tool_inventory()
    binding_path = _binding_path or BINDING
    if not _safe_file(binding_path, TOOL_ROOT):
        raise RunnerFailure("binding rejected")
    binding = _binding_data
    if binding is None:
        try:
            binding = json.loads(binding_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise RunnerFailure("binding rejected") from error
    if not isinstance(binding, dict):
        raise RunnerFailure("binding rejected")
    if (
        set(binding) != {"schema", "accepted_fixture", "sources"}
        or binding.get("schema") != "cycle3-characterize-binding/v3"
    ):
        raise RunnerFailure("binding rejected")
    if binding.get("accepted_fixture") != binding_payload()["accepted_fixture"]:
        raise RunnerFailure("accepted fixture binding rejected")
    sources = binding.get("sources")
    if not isinstance(sources, dict) or set(sources) != expected_sources():
        raise RunnerFailure("binding allowlist rejected")
    for name, digest in sources.items():
        if not isinstance(digest, str) or _digest(_path(name)) != digest:
            raise RunnerFailure("bound source rejected")
    launch = json.loads((TOOL_ROOT / "launch.json").read_text(encoding="utf-8"))
    _validate_launch_document(launch)
    load_caps()
    if _digest(DATA_ROOT / "semantic-fixtures.json") != SEMANTIC_FIXTURE_SHA256:
        raise RunnerFailure("accepted semantic fixture rejected")
    if _digest(DATA_ROOT / "manifest.json") != FIXTURE_MANIFEST_SHA256:
        raise RunnerFailure("accepted fixture manifest rejected")
    _verify_provenance()


def _validate_launch_document(launch: object) -> None:
    required = {
        "schema",
        "executable",
        "arguments",
        "environment",
        "working_directory",
        "import_roots",
        "stdlib_allowlist",
        "request_version",
        "protocol_fd",
        "characterization_probe_mode",
        "source_allowlist",
    }
    if (
        not isinstance(launch, dict)
        or set(launch) != required
        or launch.get("schema") != "cycle3-characterize-launch/v3"
    ):
        raise RunnerFailure("launch configuration rejected")
    if launch["executable"] != {"major": 3, "minor": 12, "path": "sys.executable"}:
        raise RunnerFailure("launch executable rejected")
    if launch["arguments"] != ["-I", "-B", "worker.py"]:
        raise RunnerFailure("launch executable rejected")
    boundary_ok = (
        launch["environment"]
        == {"PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": ""}
        and launch["working_directory"] == "tools/cycle3_characterize"
        and launch["import_roots"] == ["tools/cycle3_characterize"]
        and launch["protocol_fd"] == "inherited-write-only"
        and launch["characterization_probe_mode"] == "disabled"
        and launch["request_version"] == PROTOCOL_VERSION
        and launch["source_allowlist"] == sorted(expected_sources())
    )
    if not boundary_ok:
        raise RunnerFailure("launch boundary rejected")
    if launch["stdlib_allowlist"] != STDLIB_ALLOWLIST:
        raise RunnerFailure("stdlib allowlist rejected")


def _frame(value: object, limit: int) -> bytes:
    payload = json.dumps(value, allow_nan=False, separators=(",", ":")).encode("utf-8")
    if len(payload) > limit:
        raise RunnerFailure("request bytes exceeded")
    return struct.pack(">I", len(payload)) + payload


def _child_environment(write_fd: int, caps: CapProfile, token: str) -> dict[str, str]:
    return {
        "PATH": os.defpath,
        "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONPATH": "",
        "CYCLE3_PROTOCOL_FD": str(write_fd),
        "CYCLE3_ADDRESS_SPACE": str(caps["worker_address_space_bytes"]),
        "CYCLE3_RECURSION": str(caps["recursion_limit"]),
        "CYCLE3_INTERNAL_PROBE_TOKEN": token,
    }


def _popen_spec(write_fd: int, caps: CapProfile, token: str) -> dict[str, Any]:
    return {
        "args": [sys.executable, "-I", "-B", "worker.py"],
        "cwd": TOOL_ROOT,
        "env": _child_environment(write_fd, caps, token),
        "stdin": subprocess.PIPE,
        "stdout": subprocess.PIPE,
        "stderr": subprocess.PIPE,
        "pass_fds": (write_fd,),
        "close_fds": True,
        "shell": False,
    }


def _parse_result(raw: bytes, caps: CapProfile) -> dict[str, Any]:
    if len(raw) < 4:
        raise RunnerFailure("truncated result")
    size = struct.unpack(">I", raw[:4])[0]
    if size > caps["encoded_bytes"] or len(raw) != size + 4:
        raise RunnerFailure("result framing rejected")
    try:
        value = json.loads(raw[4:], parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
    except (ValueError, json.JSONDecodeError, RecursionError) as error:
        raise RunnerFailure("result payload rejected") from error
    if (
        not isinstance(value, dict)
        or value.get("version") != 1
        or not isinstance(value.get("records"), list)
    ):
        raise RunnerFailure("result shape rejected")
    if set(value) - {"version", "records", "text", "binary", "diagnostics"}:
        raise RunnerFailure("unknown result field")
    try:
        return validate_result(value, caps)
    except AccountingFailure as error:
        raise RunnerFailure("result accounting rejected") from error


def _request_for_characterization(request: Mapping[str, object]) -> dict[str, object]:
    try:
        fixed = validate_characterization_request(dict(request))
    except SnapshotHostFailure as error:
        raise RunnerFailure("characterization request rejected") from error
    samples = fixed["samples"]
    if not isinstance(samples, list) or len(samples) > load_caps()["input_samples"]:
        raise RunnerFailure("characterization samples rejected")
    return fixed


def characterize(request: Mapping[str, object]) -> RunResult:
    """Intentionally unavailable public surface; the runner is not a product host."""
    _request_for_characterization(request)
    raise RunnerFailure("characterization disabled pending runner gate")


def _orchestration_execute_approved_snapshot(request: Mapping[str, object]) -> RunResult:
    """Private post-gate path. Orchestration must supply only a closed request."""
    fixed = _request_for_characterization(request)
    return _run_request({**fixed, "_gate_token": secrets.token_hex(32)})


def run_internal_probe(probe: str, *, _profile: CapProfile | None = None) -> RunResult:
    """Private inert hook retained solely for focused pre-execution tests."""
    from .probes import PROBES

    if probe not in PROBES:
        raise RunnerFailure("closed probe rejected")
    token = secrets.token_hex(32)
    return _run_request({"version": 1, "kind": probe, "token": token, "probe": True}, _profile)


def _run_request(request: dict[str, object], profile: CapProfile | None = None) -> RunResult:
    """Run one closed request with a dedicated protocol pipe and bounded drains."""
    run_started_ns = time.monotonic_ns()
    verify_launch_identity()
    caps = profile or production_profile()
    if sys.version_info[:2] != (3, 12):
        raise RunnerFailure("Python 3.12 is required")
    framed_request = _frame(request, caps["request_bytes"])
    token = request.get("token") if request.get("probe") is True else request.get("_gate_token")
    if not isinstance(token, str):
        raise RunnerFailure("request token rejected")
    read_fd, write_fd = os.pipe()
    try:
        launch_started_ns = time.monotonic_ns()
        process = subprocess.Popen(**_popen_spec(write_fd, caps, token))
        launch_ns = time.monotonic_ns() - launch_started_ns
    except OSError as error:
        os.close(read_fd)
        os.close(write_fd)
        raise RunnerFailure("worker launch rejected") from error
    os.close(write_fd)
    raw_fds = (read_fd, write_fd)
    assert process.stdin and process.stdout and process.stderr
    disposition = "completed"
    reap_ns = 0
    terminate_to_reap_ns = 0
    kill_to_reap_ns = 0
    selector: selectors.BaseSelector | None = None
    try:
        process.stdin.write(framed_request)
        process.stdin.close()
        streams = {
            read_fd: ("protocol", caps["encoded_bytes"] + 4),
            process.stdout.fileno(): ("stdout", caps["stdout_bytes"]),
            process.stderr.fileno(): ("stderr", caps["stderr_bytes"]),
        }
        values = {name: bytearray() for name, _ in streams.values()}
        selector = selectors.DefaultSelector()
        for fd, (name, _) in streams.items():
            selector.register(fd, selectors.EVENT_READ, name)
        deadline = time.monotonic() + caps["wall_deadline_ms"] / 1000
        while selector.get_map():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RunnerFailure("deadline exceeded")
            for key, _ in selector.select(remaining):
                name, limit = streams[key.fd]
                chunk = os.read(key.fd, min(8192, limit - len(values[name]) + 1))
                if not chunk:
                    selector.unregister(key.fd)
                else:
                    values[name].extend(chunk)
                    if len(values[name]) > limit:
                        raise RunnerFailure("stream bytes exceeded")
        selector.close()
        selector = None
        reap_started_ns = time.monotonic_ns()
        process.wait(caps["terminate_grace_ms"] / 1000)
        reap_ns = time.monotonic_ns() - reap_started_ns
        if process.returncode:
            raise RunnerFailure("worker failed")
        value = _parse_result(bytes(values["protocol"]), caps)
        diagnostic = value.get("diagnostics", "")
        if not isinstance(diagnostic, str) or len(diagnostic.encode()) > caps["diagnostic_bytes"]:
            raise RunnerFailure("diagnostic bytes exceeded")
        counts = result_measurements(value)
        request_samples = request.get("samples")
        counts.update(
            {
                "input_samples": len(request_samples) if isinstance(request_samples, list) else 0,
                "request_bytes": len(framed_request) - 4,
                "stdout_bytes": len(values["stdout"]),
                "stderr_bytes": len(values["stderr"]),
            }
        )
        return RunResult(
            value,
            bytes(values["stdout"]),
            bytes(values["stderr"]),
            diagnostic.encode(),
            launch_ns,
            reap_ns,
            time.monotonic_ns() - run_started_ns,
            counts,
        )
    except (OSError, subprocess.TimeoutExpired, RunnerFailure):
        if process.poll() is None:
            terminate_started_ns = time.monotonic_ns()
            process.terminate()
            try:
                process.wait(caps["terminate_grace_ms"] / 1000)
            except subprocess.TimeoutExpired:
                terminate_to_reap_ns = time.monotonic_ns() - terminate_started_ns
                disposition = "killed-and-reaped"
                kill_started_ns = time.monotonic_ns()
                process.kill()
                process.wait()
                kill_to_reap_ns = time.monotonic_ns() - kill_started_ns
            else:
                disposition = "terminated-and-reaped"
                terminate_to_reap_ns = time.monotonic_ns() - terminate_started_ns
        raise RunnerFailure("worker request discarded") from None
    finally:
        if selector is not None:
            selector.close()
        descriptors_closed = True
        for pipe in (process.stdin, process.stdout, process.stderr):
            if pipe is not None and not pipe.closed:
                pipe.close()
            if pipe is not None:
                descriptors_closed = descriptors_closed and pipe.closed
        for fd in raw_fds:
            try:
                os.close(fd)
            except OSError:
                pass
        closed_fds: list[int] = []
        for fd in raw_fds:
            try:
                os.fstat(fd)
            except OSError:
                closed_fds.append(fd)
            else:
                descriptors_closed = False
        global _LAST_PRIVATE_EVIDENCE
        _LAST_PRIVATE_EVIDENCE = _PrivateRunEvidence(
            process.pid,
            disposition,
            process.poll() is not None,
            descriptors_closed,
            tuple(closed_fds),
            time.monotonic_ns() - run_started_ns,
            terminate_to_reap_ns,
            kill_to_reap_ns,
        )
