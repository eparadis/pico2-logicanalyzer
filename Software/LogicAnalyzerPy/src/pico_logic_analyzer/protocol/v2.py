from __future__ import annotations

import struct

import numpy as np
from numpy.typing import NDArray

from pico_logic_analyzer.model.capture import (
    CaptureConfig,
    DeviceInfo,
    ProtocolError,
    ValidationError,
)

_START, _END, _ESCAPE = b"\x55\xaa", b"\xaa\x55", 0xF0


def encode_frame(command: int, payload: bytes = b"") -> bytes:
    if not 0 <= command <= 255:
        raise ValueError("command must fit in one byte")
    body = bytes((command,)) + payload
    escaped = bytes(
        byte
        for item in body
        for byte in ((_ESCAPE, item ^ _ESCAPE) if item in (0x55, 0xAA, _ESCAPE) else (item,))
    )
    return _START + escaped + _END


def encode_identity_request() -> bytes:
    return encode_frame(0)


def encode_capture_request(config: CaptureConfig, device: DeviceInfo | None = None) -> bytes:
    if device is not None:
        config.validate_for(device)
    elif any(
        value > 0xFFFFFFFF
        for value in (
            config.sample_rate_hz,
            config.pre_trigger_samples,
            config.post_trigger_samples,
        )
    ):
        raise ProtocolError("capture field exceeds uint32")
    payload = bytearray(48)
    payload[1] = config.trigger_channel
    payload[2] = 1 if config.trigger_edge == "falling" else 0
    payload[6:30] = bytes(range(8)) + bytes(16)
    payload[30] = 8
    struct.pack_into(
        "<III",
        payload,
        32,
        config.sample_rate_hz,
        config.pre_trigger_samples,
        config.post_trigger_samples,
    )
    return encode_frame(1, bytes(payload))


class ByteParser:
    def __init__(self, data: bytes = b"") -> None:
        self._data = bytearray(data)

    def feed(self, data: bytes) -> None:
        self._data.extend(data)

    def read_exact(self, size: int) -> bytes:
        if size < 0 or len(self._data) < size:
            raise ProtocolError("truncated response")
        result = bytes(self._data[:size])
        del self._data[:size]
        return result

    def read_line(self, limit: int = 128) -> str:
        try:
            end = self._data.index(10) + 1
        except ValueError as exc:
            if len(self._data) >= limit:
                raise ProtocolError("overlong or unterminated line") from exc
            raise ProtocolError("truncated line") from exc
        if end > limit:
            raise ProtocolError("overlong line")
        raw = self.read_exact(end)
        try:
            return raw[:-1].decode("ascii")
        except UnicodeDecodeError as exc:
            raise ProtocolError("non-ASCII response") from exc


def parse_identity(parser: ByteParser) -> DeviceInfo:
    fields = [parser.read_line() for _ in range(5)]
    prefixes = ("FREQ:", "BLASTFREQ:", "BUFFER:", "CHANNELS:")
    if any(
        not field.startswith(prefix) or not field[len(prefix) :].isdigit()
        for field, prefix in zip(fields[1:], prefixes, strict=True)
    ):
        raise ProtocolError("invalid identity capability field")
    if parser._data:
        raise ProtocolError("extra identity response data")
    try:
        return DeviceInfo(fields[0], *(int(field.split(":", 1)[1]) for field in fields[1:]))
    except ValueError as exc:
        raise ProtocolError("invalid identity") from exc


def parse_capture_response(
    parser: ByteParser, config: CaptureConfig, device: DeviceInfo
) -> tuple[NDArray[np.uint8], DeviceInfo]:
    try:
        config.validate_for(device)
    except ValidationError as exc:
        raise ProtocolError("capture configuration exceeds device capabilities") from exc
    if parser.read_line() != "CAPTURE_STARTED":
        raise ProtocolError("capture did not start")
    try:
        count = struct.unpack("<I", parser.read_exact(4))[0]
    except struct.error as exc:
        raise ProtocolError("truncated capture count") from exc
    if count != config.requested_count or count > device.buffer_size:
        raise ProtocolError("invalid capture count")
    samples = np.frombuffer(parser.read_exact(count), dtype=np.uint8).copy()
    if parser.read_exact(1) != b"\0":
        raise ProtocolError("unexpected timestamp data")
    if parser._data:
        raise ProtocolError("extra capture response data")
    return samples, device
