"""Independent round-4 verification of request streaming containment."""

from __future__ import annotations

import os
import subprocess
import sys
from collections.abc import Callable

import pytest

from pico_logic_analyzer._decode.host import CancellationToken, _decode_with_factory, decode_private
from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
from pico_logic_analyzer._decode.model import HARD_LIMITS, DecodeRequest, HostFailure


def _request(samples: int = 2) -> DecodeRequest:
    return DecodeRequest("uart", 1, (7,), {"rx": 7}, (0,) * samples, 0, {})


def _large_request() -> DecodeRequest:
    # The encoded frame is independently shown to exceed this machine's pipe capacity.
    request = _request(40_000)
    read_fd, write_fd = os.pipe()
    try:
        capacity = os.fpathconf(write_fd, "PC_PIPE_BUF")
    finally:
        os.close(read_fd)
        os.close(write_fd)
    assert 40_000 > capacity
    return request


def _frame(request: DecodeRequest) -> bytes:
    result = decode_private(request).to_dict()
    return encode_frame(
        RESULT,
        {
            "result": result,
            "metrics": {
                "child_import_ns": 0,
                "child_load_ns": 0,
                "child_decode_ns": 0,
                "worker_peak_rss_bytes": 0,
            },
        },
        HARD_LIMITS["encoded_bytes"],
    )


def _factory(
    script: str, *arguments: str
) -> tuple[Callable[..., subprocess.Popen[bytes]], list[subprocess.Popen[bytes]]]:
    children: list[subprocess.Popen[bytes]] = []

    def launch(command: list[str], **kwargs: object) -> subprocess.Popen[bytes]:
        child = subprocess.Popen(
            [sys.executable, "-I", "-B", "-c", script, command[-2], command[-1], *arguments],
            **kwargs,
        )
        children.append(child)
        return child

    return launch, children


def _closed_and_reaped(children: list[subprocess.Popen[bytes]]) -> None:
    assert len(children) == 1
    child = children[0]
    assert child.poll() is not None
    assert child.stdout is not None and child.stdout.closed
    assert child.stderr is not None and child.stderr.closed


def _recovery() -> None:
    assert decode_private(_request()).decoder == "uart"


def test_complete_large_request_is_streamed_to_slow_reader() -> None:
    script = """
import os, sys, time
r, w = map(int, sys.argv[1:3])
minimum = int(sys.argv[3]); total = 0
while True:
    chunk = os.read(r, 1024)
    if not chunk: break
    total += len(chunk); time.sleep(0.0001)
assert total > minimum
os.write(w, bytes.fromhex(sys.argv[4]))
"""
    request = _large_request()
    frame = _frame(request)
    read_fd, write_fd = os.pipe()
    try:
        pipe_buf = os.fpathconf(write_fd, "PC_PIPE_BUF")
    finally:
        os.close(read_fd)
        os.close(write_fd)
    factory, children = _factory(script, str(pipe_buf), frame.hex())
    assert _decode_with_factory(request, factory).decoder == "uart"
    _closed_and_reaped(children)


def test_response_before_request_completion_cannot_be_partial_success(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host

    request = _large_request()
    script = """
import os, sys, time
r, w = map(int, sys.argv[1:3])
os.write(w, bytes.fromhex(sys.argv[3]))
time.sleep(10)
"""
    factory, children = _factory(script, _frame(request).hex())
    monkeypatch.setattr(host, "HARD_LIMITS", {**HARD_LIMITS, "wall_deadline_ms": 30})
    with pytest.raises(HostFailure, match="^timeout$"):
        host._decode_with_factory(request, factory)
    _closed_and_reaped(children)
    monkeypatch.undo()
    _recovery()


def test_cancel_after_partial_delivery_wins_over_hostile_output_and_reaps(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host

    token = CancellationToken()
    real_write = os.write
    calls = 0

    def write_then_cancel(fd: int, data: object) -> int:
        nonlocal calls
        written = real_write(fd, data)  # type: ignore[arg-type]
        calls += 1
        if calls == 1:
            assert written < len(data)  # type: ignore[arg-type]
            token.cancel()
        return written

    script = """
import os, sys, time
r, w = map(int, sys.argv[1:3])
os.write(1, b'o' * 4096); os.write(2, b'e' * 4096)
time.sleep(10)
"""
    factory, children = _factory(script)
    monkeypatch.setattr(host.os, "write", write_then_cancel)
    with pytest.raises(HostFailure, match="^cancelled$"):
        host._decode_with_factory(_large_request(), factory, token)
    assert calls and token.cancelled
    _closed_and_reaped(children)
    monkeypatch.undo()
    _recovery()


@pytest.mark.parametrize(
    ("termination", "expected"),
    [
        ("raise SystemExit(0)", "process-exit"),
        ("os.kill(os.getpid(), signal.SIGKILL)", "process-exit"),
    ],
)
def test_close_exit_or_signal_during_delivery_is_stable_and_recovers(
    termination: str, expected: str
) -> None:
    script = f"""
import os, signal, sys
r, w = map(int, sys.argv[1:3]); os.close(r); os.close(w)
{termination}
"""
    factory, children = _factory(script)
    with pytest.raises(HostFailure, match=f"^{expected}$"):
        _decode_with_factory(_large_request(), factory)
    _closed_and_reaped(children)
    _recovery()


def test_selector_readiness_anomaly_remains_deadline_bounded(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host

    real_selector = host.selectors.DefaultSelector

    class EmptySelector:
        def __init__(self) -> None:
            self.inner = real_selector()

        def __getattr__(self, name: str) -> object:
            return getattr(self.inner, name)

        def select(self, timeout: float | None = None) -> list[tuple[object, int]]:
            return []

    factory, children = _factory("import time; time.sleep(10)")
    monkeypatch.setattr(host.selectors, "DefaultSelector", EmptySelector)
    monkeypatch.setattr(host, "HARD_LIMITS", {**HARD_LIMITS, "wall_deadline_ms": 20})
    with pytest.raises(HostFailure, match="^timeout$"):
        host._decode_with_factory(_large_request(), factory)
    _closed_and_reaped(children)
    monkeypatch.undo()
    _recovery()
