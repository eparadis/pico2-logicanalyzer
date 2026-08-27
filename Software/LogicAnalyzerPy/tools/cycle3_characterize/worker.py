"""Single inert worker; protocol output is only the inherited descriptor."""

from __future__ import annotations

import json
import mmap
import os
import resource
import signal
import struct
import sys
import time
from pathlib import Path
from typing import Any


def _load_snapshot_host() -> Any:
    """Import the pinned sibling only after the private execution gate passes."""
    worker_directory = Path(__file__).resolve().parent
    if Path.cwd().resolve() != worker_directory:
        raise ValueError("worker directory rejected")
    sys.path.insert(0, str(worker_directory))
    try:
        snapshot_host = __import__("snapshot_host")
    finally:
        del sys.path[0]
    module_file = getattr(snapshot_host, "__file__", None)
    if not isinstance(module_file, str) or Path(module_file).resolve() != (
        worker_directory / "snapshot_host.py"
    ):
        raise ValueError("snapshot host path rejected")
    return snapshot_host


def _apply_limits() -> None:
    try:
        address_space = int(os.environ["CYCLE3_ADDRESS_SPACE"])
        recursion = int(os.environ["CYCLE3_RECURSION"])
        # Lower soft first: macOS rejects lowering hard below an unlimited soft
        # limit when both values are supplied in one call.
        _, hard = resource.getrlimit(resource.RLIMIT_AS)
        if hard != resource.RLIM_INFINITY and hard < address_space:
            raise ValueError("address-space cap unavailable")
        resource.setrlimit(resource.RLIMIT_AS, (address_space, hard))
        resource.setrlimit(resource.RLIMIT_AS, (address_space, address_space))
        sys.setrecursionlimit(recursion)
    except (KeyError, ValueError, OSError, AttributeError, RuntimeError) as error:
        raise ValueError("worker limits unavailable") from error


def _read_request() -> dict[str, Any]:
    header = sys.stdin.buffer.read(4)
    if len(header) != 4:
        raise ValueError("truncated request")
    length = struct.unpack(">I", header)[0]
    data = sys.stdin.buffer.read(length)
    if len(data) != length or sys.stdin.buffer.read(1):
        raise ValueError("invalid request framing")
    value = json.loads(data, parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
    if not isinstance(value, dict):
        raise ValueError("request object required")
    return value


def _write(value: dict[str, Any]) -> None:
    payload = json.dumps(value, allow_nan=False, separators=(",", ":")).encode("utf-8")
    fd = int(os.environ["CYCLE3_PROTOCOL_FD"])
    frame = memoryview(struct.pack(">I", len(payload)) + payload)
    try:
        while frame:
            written = os.write(fd, frame)
            if written <= 0:
                raise OSError("short protocol write")
            frame = frame[written:]
    finally:
        os.close(fd)


def main() -> int:
    _apply_limits()
    request = _read_request()
    if request.get("probe") is not True:
        if set(request) != {
            "_gate_token",
            "version",
            "decoder",
            "files",
            "samplerate",
            "channels",
            "samples",
            "options",
        }:
            raise ValueError("characterization request rejected")
        if request["_gate_token"] != os.environ.get("CYCLE3_INTERNAL_PROBE_TOKEN"):
            raise ValueError("characterization token rejected")
        snapshot_host_module = _load_snapshot_host()
        try:
            request.pop("_gate_token")
            _write(snapshot_host_module.execute_snapshot(_repository_root(), request))
        except snapshot_host_module.SnapshotHostFailure as error:
            raise ValueError("snapshot rejected") from error
        return 0
    if request.get("token") != os.environ.get("CYCLE3_INTERNAL_PROBE_TOKEN"):
        raise ValueError("probe rejected")
    if set(request) != {"version", "kind", "token", "probe"} or request["version"] != 1:
        raise ValueError("private request rejected")
    kind = request["kind"]
    if kind == "hang":
        time.sleep(60)
    if kind == "ignore_term":
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        time.sleep(60)
    if kind == "partial":
        os.write(int(os.environ["CYCLE3_PROTOCOL_FD"]), b"\0\0\0\10{}")
        return 0
    if kind == "extra":
        os.write(int(os.environ["CYCLE3_PROTOCOL_FD"]), b'\0\0\0\x1b{"version":1,"records":[]}x')
        return 0
    if kind == "stdout_flood":
        sys.stdout.write("x" * 200_000)
    if kind == "stderr_flood":
        sys.stderr.write("x" * 200_000)
    if kind == "diagnostic_flood":
        _write({"version": 1, "records": [], "diagnostics": "x" * 200_000})
        return 0
    if kind == "text_cap":
        _write({"version": 1, "records": [], "text": "xx"})
        return 0
    if kind == "binary_cap":
        _write({"version": 1, "records": [], "binary": "eHg="})
        return 0
    if kind == "large_result":
        _write({"version": 1, "records": [], "text": "x" * 100})
        return 0
    if kind == "stdout_noise":
        sys.stdout.write("unexpected")
        _write({"version": 1, "records": []})
        return 0
    if kind == "stderr":
        sys.stderr.write("unexpected")
        _write({"version": 1, "records": []})
        return 0
    if kind == "nonfinite":
        os.write(int(os.environ["CYCLE3_PROTOCOL_FD"]), b'\0\0\0\x1f{"version":1,"records":[NaN]}')
        return 0
    if kind == "malformed":
        os.write(int(os.environ["CYCLE3_PROTOCOL_FD"]), b"not-a-frame")
        return 0
    if kind == "deep":
        value: object = []
        for _ in range(400):
            value = [value]
        _write({"version": 1, "records": [value]})
        return 0
    if kind == "items":
        _write({"version": 1, "records": list(range(100_000))})
        return 0
    if kind == "nested_items":
        _write({"version": 1, "records": [[0, 1, 2]]})
        return 0
    if kind == "base64":
        _write({"version": 1, "records": [], "binary": "***"})
        return 0
    if kind == "limits":
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        details = {"recursion": sys.getrecursionlimit(), "soft": soft, "hard": hard}
        _write({"version": 1, "records": [], "diagnostics": json.dumps(details)})
        return 0
    if kind == "raise_address_space":
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        rejected = False
        try:
            resource.setrlimit(resource.RLIMIT_AS, (soft + 1, hard + 1))
        except (MemoryError, OSError, ValueError):
            rejected = True
        _write({"version": 1, "records": [], "diagnostics": json.dumps({"rejected": rejected})})
        return 0
    if kind == "address_space_over":
        sys.stdout.write("address-space-start\n")
        sys.stdout.flush()
        soft, _ = resource.getrlimit(resource.RLIMIT_AS)
        try:
            mapping = mmap.mmap(-1, soft + mmap.PAGESIZE, access=mmap.ACCESS_WRITE)
            mapping.close()
        except (MemoryError, OSError, ValueError) as error:
            _write(
                {
                    "version": 1,
                    "records": [],
                    "diagnostics": type(error).__name__,
                }
            )
            return 0
        raise ValueError("address-space cap was not enforced")
    if kind == "recursion_over":

        def recurse(depth: int) -> int:
            return recurse(depth + 1) + 1

        recurse(0)
    if kind != "valid":
        raise ValueError("unknown probe")
    _write({"version": 1, "records": [], "text": "", "binary": "", "diagnostics": ""})
    return 0


def _repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, json.JSONDecodeError, RecursionError):
        sys.stderr.write("worker failure\n")
        raise SystemExit(2)
