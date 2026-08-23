"""Independent C2-B2 regression for the reopened 24-channel metadata boundary."""

from __future__ import annotations

import numpy as np
import pytest

from pico_logic_analyzer.cli.main import _capture_config, _parser
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo, ValidationError
from pico_logic_analyzer.protocol import encode_capture_request


def _device(*, channels: int = 24, buffer_size: int = 393_216) -> DeviceInfo:
    return DeviceInfo(
        "LOGIC_ANALYZER_PICO_2_V6_0",
        200_000_000,
        400_000_000,
        buffer_size,
        channels,
    )


def _cli_config(channel_ids: tuple[int, ...]) -> CaptureConfig:
    arguments = _parser().parse_args(
        [
            "capture",
            "--port",
            "never-opened",
            "--sample-rate",
            "100000",
            "--trigger-channel",
            str(channel_ids[0]),
            "--edge",
            "rising",
            "--pre-samples",
            "2",
            "--post-samples",
            "2",
            "--channels",
            ",".join(str(channel) for channel in channel_ids),
            "--csv",
            "unused.csv",
            "--replay",
            "unused.npz",
        ]
    )
    return _capture_config(arguments)


def test_full_d0_through_d23_cli_defaults_are_complete_and_ordered() -> None:
    channels = tuple(range(24))
    config = _cli_config(channels)
    result = CaptureResult(config, np.array([0, 1, 0x810101, 0], dtype=np.uint32), _device())

    assert config.channel_ids == channels
    assert config.firmware_mode == 2
    assert config.bytes_per_word == 4
    assert result.channel_labels == tuple(f"D{channel}" for channel in channels)
    assert result.channel_mapping == tuple(f"D{channel}" for channel in channels)
    assert [result.channel_samples(channel).tolist() for channel in (0, 8, 16, 23)] == [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
    ]

    payload = encode_capture_request(config)[3:-2]
    assert payload[6:30] == bytes(range(24))
    assert payload[30:32] == b"\x18\x00"
    assert payload[46] == 2


def test_default_metadata_follows_reordered_physical_ids_not_packed_indices() -> None:
    channels = (23, 0, 16, 8)
    config = _cli_config(channels)
    result = CaptureResult(config, np.zeros(4, dtype=np.uint32), _device())
    assert result.channel_labels == ("D23", "D0", "D16", "D8")
    assert result.channel_mapping == ("D23", "D0", "D16", "D8")


@pytest.mark.parametrize(
    ("labels", "mappings"),
    [
        (("D0",) * 23, tuple(f"D{i}" for i in range(24))),
        (tuple(f"D{i}" for i in range(24)), ("D0",) * 23),
        (("same",) * 24, tuple(f"D{i}" for i in range(24))),
        (("",) + tuple(f"D{i}" for i in range(1, 24)), tuple(f"D{i}" for i in range(24))),
        (("X" * 129,) + tuple(f"D{i}" for i in range(1, 24)), tuple(f"D{i}" for i in range(24))),
        (tuple(f"D{i}" for i in range(24)), (1,) + tuple(f"D{i}" for i in range(1, 24))),
    ],
)
def test_malformed_duplicate_or_unsafe_metadata_rejects_before_transport(
    labels: tuple[object, ...], mappings: tuple[object, ...]
) -> None:
    config = _cli_config(tuple(range(24)))
    with pytest.raises(ValidationError):
        CaptureResult(
            config,
            np.zeros(4, dtype=np.uint32),
            _device(),
            labels,  # type: ignore[arg-type]
            mappings,  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    "config,device",
    [
        (CaptureConfig(100_000, 2, 2, 0, "rising", tuple(range(24))), _device(channels=23)),
        (CaptureConfig(100_000, 2, 2, 0, "rising", tuple(range(24))), _device(buffer_size=15)),
    ],
)
def test_existing_negotiated_channel_and_byte_buffer_bounds_remain_pre_io(
    config: CaptureConfig, device: DeviceInfo
) -> None:
    with pytest.raises(ValidationError):
        CaptureResult(config, np.zeros(4, dtype=np.uint32), device)
