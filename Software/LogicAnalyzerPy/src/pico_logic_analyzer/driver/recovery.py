"""Bounded internal recovery state machine; serial opening is a C1-B3 concern."""

from __future__ import annotations

from collections.abc import Callable
from math import isfinite
from time import monotonic

from pico_logic_analyzer.transport import ByteTransport


class RecoveryError(RuntimeError):
    pass


class CaptureRecovery:
    """Recover an in-flight normal capture without exposing a public abort API."""

    def __init__(self, transport: ByteTransport, reopen_and_identify: Callable[[], object]) -> None:
        self._transport = transport
        self._reopen_and_identify = reopen_and_identify
        self._recovering = False

    def timeout_or_cancel(self, timeout: float, drain_limit: int = 4096) -> None:
        if (
            not isfinite(timeout)
            or timeout <= 0
            or type(drain_limit) is not int
            or drain_limit <= 0
        ):
            raise ValueError("timeout and drain limit must be finite and positive")
        if self._recovering:
            raise RecoveryError("recovery already attempted")
        self._recovering = True
        deadline = monotonic() + timeout
        failure: Exception | None = None
        try:
            self._transport.write(b"\xff", timeout)
            # A bounded best-effort drain uses the same byte owner. Timeouts are
            # expected and do not suppress close/reopen/re-identification.
            try:
                for _ in range(drain_limit):
                    remaining = deadline - monotonic()
                    if remaining <= 0:
                        break
                    self._transport.read_exact(1, remaining)
            except (TimeoutError, ConnectionError):
                pass
        except Exception as exc:
            failure = exc
        try:
            self._transport.close()
        except Exception as exc:
            if failure is None:
                failure = exc
        if failure is None:
            try:
                self._reopen_and_identify()
            except Exception as exc:
                failure = exc
        if failure is not None:
            raise RecoveryError("capture recovery failed") from failure
