from __future__ import annotations

import struct
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.formats import csv_bytes, import_csv_bytes, load_replay, replay_bytes
from pico_logic_analyzer.model import (
    CaptureConfig,
    CaptureResult,
    DeviceInfo,
    ProtocolError,
    ValidationError,
)
from pico_logic_analyzer.protocol import ByteParser, encode_capture_request, parse_capture_response


def _device() -> DeviceInfo:
    return DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 1_000_000, 2_000_000, 4096, 24)


@pytest.mark.parametrize(
    ("channels", "mode", "dtype"),
    [((7, 0), 0, np.uint8), ((15, 0, 8), 1, np.uint16), ((23, 0, 16), 2, np.uint32)],
)
def test_wider_config_preserves_request_order_and_mode(
    channels: tuple[int, ...], mode: int, dtype: type[np.generic]
) -> None:
    config = CaptureConfig(100, 1, 2, channels[0], "rising", channels)
    assert config.firmware_mode == mode and config.sample_dtype == np.dtype(dtype)
    payload = encode_capture_request(config)[3:-2]
    assert len(payload) == 48 and payload[6 : 6 + len(channels)] == bytes(channels)
    assert payload[6 + len(channels) : 30] == bytes(24 - len(channels))
    assert payload[30] == len(channels) and payload[31] == 0 and payload[46] == mode


@pytest.mark.parametrize(
    ("channels", "words", "dtype"),
    [
        ((0,), [1, 0, 1], np.uint8),
        ((8, 0), [0x0101, 0x0001, 0x0100], np.uint16),
        ((16, 0), [0x010001, 1, 0x010000], np.uint32),
    ],
)
def test_wider_response_uses_little_endian_mode_words(
    channels: tuple[int, ...], words: list[int], dtype: type[np.generic]
) -> None:
    config = CaptureConfig(100, 1, 2, channels[0], "rising", channels)
    raw = np.asarray(words, dtype=dtype).astype(np.dtype(dtype).newbyteorder("<")).tobytes()
    parser = ByteParser(b"CAPTURE_STARTED\n" + struct.pack("<I", 3) + raw + b"\0")
    samples, _ = parse_capture_response(parser, config, _device())
    assert samples.dtype == np.dtype(dtype) and samples.tolist() == words


def test_wider_model_rejects_duplicates_and_nonzero_24bit_padding() -> None:
    with pytest.raises(ValidationError):
        CaptureConfig(1, 0, 1, 0, "rising", (0, 0))
    config = CaptureConfig(1, 0, 1, 16, "rising", (16,))
    with pytest.raises(ValidationError):
        CaptureResult(config, np.array([0xFF000001], dtype=np.uint32), _device())
    parser = ByteParser(b"CAPTURE_STARTED\n\x01\0\0\0\x01\0\0\xff\0")
    with pytest.raises(ProtocolError):
        parse_capture_response(parser, config, _device())


def test_timestamp_contamination_invalidates_receive_owner() -> None:
    config = CaptureConfig(1, 0, 1, 0, "rising", (0,))
    parser = ByteParser(b"CAPTURE_STARTED\n\x01\0\0\0\x01\x01\0\0\0\0")
    with pytest.raises(ProtocolError):
        parse_capture_response(parser, config, _device())
    with pytest.raises(ProtocolError):
        parser.feed(b"CAPTURE_STARTED\n")


def test_wider_csv_uses_ordered_packed_positions() -> None:
    config = CaptureConfig(100, 0, 2, 8, "rising", (8, 0))
    result = CaptureResult(
        config,
        np.array([1, 2], dtype=np.uint16),
        _device(),
        ("D8", "D0"),
        ("D8", "D0"),
    )
    assert csv_bytes(result) == (
        b"sample_index,time_seconds,trigger,D8,D0\n0,0,1,1,0\n1,0.01,0,0,1\n"
    )


def test_wider_csv_import_reconstructs_ordered_packed_positions() -> None:
    data = b"sample_index,time_seconds,trigger,D8,D0\n0,0,1,1,0\n1,0.01,0,0,1\n"
    result = import_csv_bytes(
        data,
        channel_ids=(8, 0),
        sample_rate_hz=100,
        trigger_channel=8,
        trigger_edge="rising",
    )
    assert result.config.channel_ids == (8, 0)
    assert result.samples.dtype == np.dtype("uint16") and result.samples.tolist() == [1, 2]
    assert csv_bytes(result) == data


def test_general_csv_never_infers_ids_from_labels() -> None:
    data = b"sample_index,time_seconds,trigger,D8\n0,0,1,1\n"
    with pytest.raises(ProtocolError):
        import_csv_bytes(
            data,
            channel_ids=None,
            sample_rate_hz=100,
            trigger_channel=8,
            trigger_edge="rising",
        )


def test_schema2_replay_round_trips_wider_words(tmp_path: Path) -> None:
    config = CaptureConfig(100, 0, 2, 16, "rising", (16, 0))
    result = CaptureResult(
        config, np.array([1, 2], dtype=np.uint32), _device(), ("D16", "D0"), ("D16", "D0")
    )
    path = tmp_path / "capture.npz"
    path.write_bytes(replay_bytes(result))
    samples, metadata = load_replay(path)
    assert samples.dtype == np.dtype("uint32") and metadata["schema_version"] == 2
