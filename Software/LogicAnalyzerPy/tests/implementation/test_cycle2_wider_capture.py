from __future__ import annotations

import struct
from argparse import Namespace
from pathlib import Path

import numpy as np
import pytest

from pico_logic_analyzer.cli import main as cli
from pico_logic_analyzer.driver import V2DeviceService
from pico_logic_analyzer.formats import csv_bytes, import_csv_bytes, load_replay, replay_bytes
from pico_logic_analyzer.formats.capture import MAX_CSV_INPUT_BYTES
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


def test_24_channel_result_uses_ordered_default_labels_and_rejects_invalid_metadata() -> None:
    config = cli._capture_config(
        Namespace(
            sample_rate=100,
            pre_samples=1,
            post_samples=2,
            trigger_channel=0,
            edge="rising",
            channels=",".join(str(channel) for channel in range(24)),
        )
    )
    result = CaptureResult(config, np.zeros(3, dtype=np.uint32), _device())
    assert result.channel_labels == tuple(f"D{channel}" for channel in range(24))
    assert result.channel_mapping == tuple(f"D{channel}" for channel in range(24))
    with pytest.raises(ValidationError, match="invalid channel labels or mappings"):
        CaptureResult(
            config,
            np.zeros(3, dtype=np.uint32),
            _device(),
            tuple(f"D{channel}" for channel in range(23)),
            tuple(f"D{channel}" for channel in range(24)),
        )
    with pytest.raises(ValidationError, match="channel labels must be unique"):
        CaptureResult(
            config,
            np.zeros(3, dtype=np.uint32),
            _device(),
            ("same",) * 24,
            tuple(f"D{channel}" for channel in range(24)),
        )


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
    assert result.channel_samples(8).tolist() == [1, 0]
    assert result.channel_samples(0).tolist() == [0, 1]


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


def test_legacy_csv_infers_unique_integer_rate() -> None:
    data = (
        b"sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7\n"
        b"0,-0.01,0,0,0,0,0,0,0,0,0\n"
        b"1,0,1,1,0,0,0,0,0,0,0\n"
        b"2,0.01,0,0,0,0,0,0,0,0,0\n"
    )
    result = import_csv_bytes(
        data,
        channel_ids=None,
        sample_rate_hz=None,
        trigger_channel=0,
        trigger_edge="rising",
    )
    assert result.config.sample_rate_hz == 100 and csv_bytes(result) == data


def test_legacy_csv_rejects_ambiguous_or_missing_rate() -> None:
    header = b"sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7\n"
    ambiguous = (
        header
        + b"0,-0.01,0,0,0,0,0,0,0,0,0\n"
        + b"1,0,1,0,0,0,0,0,0,0,0\n"
        + b"2,0.009,0,0,0,0,0,0,0,0,0\n"
    )
    one_row = header + b"0,0,1,0,0,0,0,0,0,0,0\n"
    for data in (ambiguous, one_row):
        with pytest.raises(ProtocolError):
            import_csv_bytes(
                data,
                channel_ids=None,
                sample_rate_hz=None,
                trigger_channel=0,
                trigger_edge="rising",
            )


def test_legacy_csv_rate_inference_uses_exact_decimal_canonical_times() -> None:
    data = (
        b"sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7\n"
        b"0,-0.333333333333,0,0,0,0,0,0,0,0,0\n"
        b"1,0,1,0,0,0,0,0,0,0,0\n"
        b"2,0.333333333333,0,0,0,0,0,0,0,0,0\n"
    )
    result = import_csv_bytes(
        data,
        channel_ids=None,
        sample_rate_hz=None,
        trigger_channel=0,
        trigger_edge="rising",
    )
    assert result.config.sample_rate_hz == 3


def test_cli_csv_import_preserves_explicit_paths(tmp_path: Path) -> None:
    source = tmp_path / "input.csv"
    output, replay = tmp_path / "output.csv", tmp_path / "output.npz"
    source.write_bytes(
        b"sample_index,time_seconds,trigger,D8,D0\n0,0,1,1,0\n1,0.01,0,0,1\n"
    )
    assert cli.main(
        [
            "csv-import", str(source), "--channels", "8,0", "--sample-rate", "100",
            "--trigger-channel", "8", "--edge", "rising", "--csv", str(output),
            "--replay", str(replay),
        ]
    ) == 0
    assert output.read_bytes() == source.read_bytes() and load_replay(replay)[0].tolist() == [1, 2]


def test_cli_csv_import_maps_invalid_metadata_to_validation_exit(tmp_path: Path) -> None:
    source = tmp_path / "input.csv"
    source.write_bytes(b"sample_index,time_seconds,trigger,D8\n0,0,1,1\n")
    assert cli.main(
        [
            "csv-import", str(source), "--sample-rate", "100", "--trigger-channel", "8",
            "--edge", "rising", "--csv", str(tmp_path / "output.csv"), "--replay",
            str(tmp_path / "output.npz"),
        ]
    ) == 5


@pytest.mark.parametrize("rate", (0, -1, 0x1_0000_0000, True, 1.5))
def test_csv_import_validates_explicit_rate_before_timing(rate: object) -> None:
    with pytest.raises(ProtocolError, match="invalid CSV capture"):
        import_csv_bytes(
            b"sample_index,time_seconds,trigger,D8\n0,0,1,1\n",
            channel_ids=(8,),
            sample_rate_hz=rate,  # type: ignore[arg-type]
            trigger_channel=8,
            trigger_edge="rising",
        )


@pytest.mark.parametrize("rate", ("0", "-1", "4294967296"))
def test_cli_csv_import_rejects_invalid_rate_with_validation_exit(
    tmp_path: Path, rate: str
) -> None:
    source = tmp_path / "input.csv"
    output, replay = tmp_path / "output.csv", tmp_path / "output.npz"
    source.write_bytes(b"sample_index,time_seconds,trigger,D8\n0,0,1,1\n")
    assert cli.main(
        [
            "csv-import", str(source), "--channels", "8", "--sample-rate", rate,
            "--trigger-channel", "8", "--edge", "rising", "--csv", str(output),
            "--replay", str(replay),
        ]
    ) == 5
    assert not output.exists() and not replay.exists()


def test_cli_csv_import_bounds_sparse_input_before_full_read(tmp_path: Path) -> None:
    source = tmp_path / "large.csv"
    with source.open("wb") as file:
        file.truncate(MAX_CSV_INPUT_BYTES + 1)
    output, replay = tmp_path / "output.csv", tmp_path / "output.npz"
    assert cli.main(
        [
            "csv-import", str(source), "--channels", "8", "--sample-rate", "100",
            "--trigger-channel", "8", "--edge", "rising", "--csv", str(output),
            "--replay", str(replay),
        ]
    ) == 5
    assert not output.exists() and not replay.exists()


def test_cli_csv_import_reads_exact_limit_and_maps_read_failure(
    tmp_path: Path,
) -> None:
    source = tmp_path / "input.csv"
    source.write_bytes(b"x" * MAX_CSV_INPUT_BYTES)
    output, replay = tmp_path / "output.csv", tmp_path / "output.npz"
    assert cli.main(
        [
            "csv-import", str(source), "--channels", "8", "--sample-rate", "100",
            "--trigger-channel", "8", "--edge", "rising", "--csv", str(output),
            "--replay", str(replay),
        ]
    ) == 5
    assert cli.main(
        [
            "csv-import", str(tmp_path / "missing.csv"), "--channels", "8", "--sample-rate", "100",
            "--trigger-channel", "8", "--edge", "rising", "--csv", str(output),
            "--replay", str(replay),
        ]
    ) == 6
    assert not output.exists() and not replay.exists()


def test_schema2_replay_round_trips_wider_words(tmp_path: Path) -> None:
    config = CaptureConfig(100, 0, 2, 16, "rising", (16, 0))
    result = CaptureResult(
        config, np.array([1, 2], dtype=np.uint32), _device(), ("D16", "D0"), ("D16", "D0")
    )
    path = tmp_path / "capture.npz"
    path.write_bytes(replay_bytes(result))
    samples, metadata = load_replay(path)
    assert samples.dtype == np.dtype("uint32") and metadata["schema_version"] == 2


@pytest.mark.parametrize(
    ("channels", "golden"),
    [
        ((0, 7), "55aa010000010000000007000000000000000000000000000000000000000000"
         "00020078563412040302010807060500000000aa55"),
        ((8, 0), "55aa010008010000000800000000000000000000000000000000000000000000"
         "00020078563412040302010807060500000100aa55"),
        ((16, 3, 23), "55aa010010010000001003170000000000000000000000000000000000000000"
         "00030078563412040302010807060500000200aa55"),
    ],
)
def test_literal_normal_request_golden_packets_all_widths(
    channels: tuple[int, ...], golden: str
) -> None:
    request = encode_capture_request(
        CaptureConfig(0x12345678, 0x01020304, 0x05060708, channels[0], "falling", channels)
    )
    assert request == bytes.fromhex(golden)


@pytest.mark.parametrize(
    ("channels", "dtype", "words"),
    [
        ((0,), np.uint8, [0, 1, 0]),
        ((8, 0), np.uint16, [0x101, 2, 0]),
        ((16, 0), np.uint32, [0x10001, 2, 0]),
    ],
)
def test_literal_response_fragmentation_and_adverses_all_widths(
    channels: tuple[int, ...], dtype: type[np.generic], words: list[int]
) -> None:
    config = CaptureConfig(100, 1, 2, channels[0], "rising", channels)
    response = (
        b"CAPTURE_STARTED\n"
        + struct.pack("<I", len(words))
        + np.asarray(words, dtype=dtype).astype(np.dtype(dtype).newbyteorder("<")).tobytes()
        + b"\0"
    )
    fragmented = ByteParser()
    for byte in response:
        fragmented.feed(bytes((byte,)))
    samples, _ = parse_capture_response(fragmented, config, _device())
    assert samples.tolist() == words
    for bad in (
        response.replace(b"CAPTURE_STARTED", b"NOPE", 1),
        response[:-1],
        response + b"extra",
    ):
        with pytest.raises(ProtocolError):
            parse_capture_response(ByteParser(bad), config, _device())
    contaminated = ByteParser(response[:-1] + b"\x01\xde\xad\xbe\xef")
    with pytest.raises(ProtocolError):
        parse_capture_response(contaminated, config, _device())
    with pytest.raises(ProtocolError):
        contaminated.feed(b"CAPTURE_STARTED\n")


def test_capture_service_closes_transport_after_timeout() -> None:
    class TimeoutTransport:
        closed = False

        def open(self) -> None:
            pass

        def write(self, _: bytes, __: float) -> None:
            pass

        def read_line(self, _: float) -> str:
            raise TimeoutError("deliberate timeout")

        def read_exact(self, _: int, __: float) -> bytes:
            raise AssertionError("not reached")

        def close(self) -> None:
            self.closed = True

    transport = TimeoutTransport()
    with pytest.raises(TimeoutError):
        V2DeviceService(lambda *_: transport).capture(
            "/dev/fake", CaptureConfig(1, 0, 1, 0, "rising"), 1
        )
    assert transport.closed
