"""Bounded pySerial transport for the explicitly selected Cycle 1 port."""

from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from math import isfinite
from time import monotonic, sleep
from typing import Any

from .fake import TransportClosed, TransportTimeout

DEFAULT_TIMEOUT_SECONDS = 10.0
STABILIZE_SECONDS = 0.1
DRAIN_TIMEOUT_SECONDS = 0.2
DRAIN_LIMIT_BYTES = 1024


class SerialTransportError(ConnectionError):
    """A serial open/read/write failure suitable for a connection diagnostic."""


def _validate_timeout(timeout: float) -> None:
    if not isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be finite and positive")


class SerialTransport:
    """A single byte-buffered serial stream; it never creates text readers."""

    def __init__(
        self,
        port: str,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        *,
        serial_factory: Callable[..., Any] | None = None,
        sleeper: Callable[[float], None] = sleep,
        clock: Callable[[], float] = monotonic,
    ) -> None:
        if not port:
            raise ValueError("port must not be empty")
        _validate_timeout(timeout)
        self.port = port
        self.timeout = timeout
        self._serial_factory = serial_factory
        self._sleeper = sleeper
        self._clock = clock
        self._serial: Any | None = None
        self._buffer = bytearray()

    @property
    def is_open(self) -> bool:
        return self._serial is not None and bool(self._serial.is_open)

    def open(self) -> None:
        if self.is_open:
            return
        factory = self._serial_factory
        if factory is None:
            try:
                serial_module = import_module("serial")
            except ImportError as exc:  # pragma: no cover - packaging failure
                raise SerialTransportError("pySerial is not installed") from exc
            factory = serial_module.Serial
        try:
            # Configure while port=None so opening cannot inherit host defaults.
            connection = factory(
                port=None,
                baudrate=115200,
                bytesize=8,
                parity="N",
                stopbits=1,
                timeout=self.timeout,
                write_timeout=self.timeout,
                xonxoff=False,
                rtscts=False,
                dsrdtr=False,
            )
            connection.dtr = True
            connection.rts = True
            connection.port = self.port
            connection.open()
            self._serial = connection
            self._sleeper(STABILIZE_SECONDS)
            self.drain(DRAIN_TIMEOUT_SECONDS, DRAIN_LIMIT_BYTES)
        except Exception as exc:
            self.close()
            raise SerialTransportError(f"cannot open {self.port}: {exc}") from exc

    def read_exact(self, size: int, timeout: float) -> bytes:
        if size < 0:
            raise ValueError("size must not be negative")
        _validate_timeout(timeout)
        if not self.is_open:
            raise TransportClosed("serial transport closed")
        connection = self._serial
        if connection is None:  # narrow the optional transport state for mypy
            raise TransportClosed("serial transport closed")
        deadline = self._clock() + timeout
        result = bytearray()
        while len(result) < size:
            if self._buffer:
                take = min(size - len(result), len(self._buffer))
                result.extend(self._buffer[:take])
                del self._buffer[:take]
                continue
            remaining = deadline - self._clock()
            if remaining <= 0:
                raise TransportTimeout(f"timed out reading {size} bytes from {self.port}")
            try:
                connection.timeout = remaining
                chunk = connection.read(size - len(result))
            except Exception as exc:
                self.close()
                raise SerialTransportError(f"serial read failed on {self.port}: {exc}") from exc
            if not chunk:
                raise TransportTimeout(f"timed out reading {size} bytes from {self.port}")
            result.extend(chunk)
        return bytes(result)

    def read_line(self, timeout: float, limit: int = 128) -> str:
        _validate_timeout(timeout)
        if limit < 1:
            raise ValueError("line limit must be positive")
        if not self.is_open:
            raise TransportClosed("serial transport closed")
        connection = self._serial
        if connection is None:
            raise TransportClosed("serial transport closed")
        deadline = self._clock() + timeout
        while True:
            try:
                end = self._buffer.index(10) + 1
            except ValueError:
                if len(self._buffer) >= limit:
                    raise SerialTransportError("overlong or unterminated identity field")
                remaining = deadline - self._clock()
                if remaining <= 0:
                    raise TransportTimeout(f"timed out reading identity from {self.port}")
                try:
                    connection.timeout = remaining
                    chunk = connection.read(1)
                except Exception as exc:
                    self.close()
                    raise SerialTransportError(f"serial read failed on {self.port}: {exc}") from exc
                if not chunk:
                    raise TransportTimeout(f"timed out reading identity from {self.port}")
                self._buffer.extend(chunk)
                continue
            if end > limit:
                raise SerialTransportError("overlong identity field")
            raw = bytes(self._buffer[:end])
            del self._buffer[:end]
            try:
                return raw[:-1].decode("ascii")
            except UnicodeDecodeError as exc:
                raise SerialTransportError("non-ASCII identity field") from exc

    def write(self, data: bytes, timeout: float) -> None:
        _validate_timeout(timeout)
        if not self.is_open:
            raise TransportClosed("serial transport closed")
        connection = self._serial
        if connection is None:
            raise TransportClosed("serial transport closed")
        try:
            connection.write_timeout = timeout
            written = connection.write(data)
            if written != len(data):
                raise SerialTransportError(f"short serial write to {self.port}")
            connection.flush()
        except SerialTransportError:
            raise
        except Exception as exc:
            self.close()
            raise SerialTransportError(f"serial write failed on {self.port}: {exc}") from exc

    def drain(self, timeout: float, limit: int) -> int:
        _validate_timeout(timeout)
        if limit < 0:
            raise ValueError("drain limit must not be negative")
        if not self.is_open:
            return 0
        connection = self._serial
        if connection is None:
            return 0
        self._buffer.clear()
        deadline = self._clock() + timeout
        drained = 0
        while drained < limit and self._clock() < deadline:
            try:
                waiting = int(getattr(connection, "in_waiting", 0))
                if waiting <= 0:
                    break
                connection.timeout = max(0.001, deadline - self._clock())
                chunk = connection.read(min(waiting, limit - drained))
            except Exception as exc:
                self.close()
                raise SerialTransportError(f"serial drain failed on {self.port}: {exc}") from exc
            if not chunk:
                break
            drained += len(chunk)
        return drained

    def close(self) -> None:
        connection, self._serial = self._serial, None
        self._buffer.clear()
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass
