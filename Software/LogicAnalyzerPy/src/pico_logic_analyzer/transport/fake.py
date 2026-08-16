from __future__ import annotations

from collections import deque
from math import isfinite
from typing import Protocol


class TransportTimeout(TimeoutError):
    pass


class TransportClosed(ConnectionError):
    pass


class ByteTransport(Protocol):
    def read_exact(self, size: int, timeout: float) -> bytes: ...
    def write(self, data: bytes, timeout: float) -> None: ...
    def close(self) -> None: ...


class FakeTransport:
    def __init__(self, reads: list[bytes] | None = None) -> None:
        self._reads: deque[bytes] = deque(reads or [])
        self.writes: list[bytes] = []
        self.closed = False

    def read_exact(self, size: int, timeout: float) -> bytes:
        if not isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be finite and positive")
        if self.closed:
            raise TransportClosed("transport closed")
        out = bytearray()
        while len(out) < size:
            if not self._reads:
                raise TransportTimeout("script exhausted")
            chunk = self._reads.popleft()
            needed = size - len(out)
            out.extend(chunk[:needed])
            if len(chunk) > needed:
                self._reads.appendleft(chunk[needed:])
        return bytes(out)

    def write(self, data: bytes, timeout: float) -> None:
        if not isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be finite and positive")
        if self.closed:
            raise TransportClosed("transport closed")
        self.writes.append(bytes(data))

    def cancel_recovery(self, timeout: float) -> None:
        self.write(b"\xff", timeout)

    def close(self) -> None:
        self.closed = True
