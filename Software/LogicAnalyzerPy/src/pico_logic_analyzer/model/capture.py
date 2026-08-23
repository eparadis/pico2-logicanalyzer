from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, cast

import numpy as np
from numpy.typing import NDArray

Edge = Literal["rising", "falling"]


class ValidationError(ValueError):
    pass


class ProtocolError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class DeviceInfo:
    identity: str
    max_frequency_hz: int
    blast_frequency_hz: int
    buffer_size: int
    channel_count: int

    def __post_init__(self) -> None:
        import re

        if type(self.identity) is not str:
            raise ValidationError("identity must be a string")
        match = re.fullmatch(r"LOGIC_ANALYZER_[A-Za-z0-9_-]+_V(\d+)_(\d+)", self.identity)
        if match is None:
            raise ValidationError("invalid V2 identity")
        major, minor = (int(value) for value in match.groups())
        if len(self.identity) > 128 or (major, minor) < (6, 0):
            raise ValidationError("unsupported device version; minimum is V6_0")
        if any(
            type(value) is not int
            for value in (
                self.max_frequency_hz,
                self.blast_frequency_hz,
                self.buffer_size,
                self.channel_count,
            )
        ):
            raise ValidationError("capabilities must be integers")
        if (
            min(
                self.max_frequency_hz, self.blast_frequency_hz, self.buffer_size, self.channel_count
            )
            <= 0
        ):
            raise ValidationError("capabilities must be positive")
        if not 8 <= self.channel_count <= 24 or any(
            value > 0xFFFFFFFF
            for value in (
                self.max_frequency_hz,
                self.blast_frequency_hz,
                self.buffer_size,
                self.channel_count,
            )
        ):
            raise ValidationError("invalid Cycle 1 capabilities")


@dataclass(frozen=True, slots=True)
class CaptureConfig:
    sample_rate_hz: int
    pre_trigger_samples: int
    post_trigger_samples: int
    trigger_channel: int
    trigger_edge: Edge
    channel_ids: tuple[int, ...] = tuple(range(8))

    def __post_init__(self) -> None:
        numeric_fields = (
            self.sample_rate_hz,
            self.pre_trigger_samples,
            self.post_trigger_samples,
            self.trigger_channel,
        )
        if any(type(value) is not int for value in numeric_fields):
            raise ValidationError("capture fields must be integers")
        if any(value > 0xFFFFFFFF for value in numeric_fields[:3]):
            raise ValidationError("capture field exceeds uint32")
        if (
            type(self.channel_ids) is not tuple
            or not 1 <= len(self.channel_ids) <= 24
            or any(type(value) is not int or not 0 <= value <= 23 for value in self.channel_ids)
            or len(set(self.channel_ids)) != len(self.channel_ids)
        ):
            raise ValidationError("invalid ordered channel ids")
        if (
            self.sample_rate_hz <= 0
            or self.pre_trigger_samples < 0
            or self.post_trigger_samples < 1
        ):
            raise ValidationError("invalid sample rate or trigger sample count")
        if (
            self.trigger_channel not in self.channel_ids
            or type(self.trigger_edge) is not str
            or self.trigger_edge not in ("rising", "falling")
        ):
            raise ValidationError("invalid trigger")

    @property
    def requested_count(self) -> int:
        return self.pre_trigger_samples + self.post_trigger_samples

    def validate_for(self, device: DeviceInfo) -> None:
        if self.sample_rate_hz > device.max_frequency_hz:
            raise ValidationError("sample rate exceeds device capability")
        if any(channel >= device.channel_count for channel in self.channel_ids):
            raise ValidationError("channel exceeds device capability")
        if self.requested_count * self.bytes_per_word > device.buffer_size:
            raise ValidationError("sample count exceeds device buffer")
        if any(
            value > 0xFFFFFFFF
            for value in (self.sample_rate_hz, self.pre_trigger_samples, self.post_trigger_samples)
        ):
            raise ValidationError("capture field exceeds uint32")

    @property
    def firmware_mode(self) -> int:
        return max(self.channel_ids) // 8

    @property
    def bytes_per_word(self) -> int:
        return 1 << self.firmware_mode

    @property
    def sample_dtype(self) -> np.dtype[np.generic]:
        return (np.dtype("uint8"), np.dtype("uint16"), np.dtype("uint32"))[self.firmware_mode]


@dataclass(frozen=True, slots=True)
class CaptureResult:
    config: CaptureConfig
    samples: NDArray[np.generic]
    device: DeviceInfo
    channel_labels: tuple[str, ...] = tuple(f"D{i}" for i in range(8))
    channel_mapping: tuple[str, ...] = tuple(f"D{i}" for i in range(8))

    def __post_init__(self) -> None:
        if (
            not isinstance(self.samples, np.ndarray)
            or self.samples.dtype != self.config.sample_dtype
            or self.samples.ndim != 1
        ):
            raise ValidationError("samples must be a rank-one mode-appropriate array")
        if not self.samples.flags.c_contiguous or len(self.samples) != self.config.requested_count:
            raise ValidationError("sample count or memory layout is invalid")
        self.config.validate_for(self.device)
        if self.config.firmware_mode == 2 and np.any(
            cast(NDArray[np.uint32], self.samples) & np.uint32(0xFF000000)
        ):
            raise ValidationError("24-channel samples must have a zero upper byte")
        metadata = (self.channel_labels, self.channel_mapping)
        if any(
            type(values) is not tuple
            or len(values) != len(self.config.channel_ids)
            or any(type(value) is not str or not value or len(value) > 128 for value in values)
            for values in metadata
        ):
            raise ValidationError("invalid channel labels or mappings")
        if len(set(self.channel_labels)) != len(self.channel_labels):
            raise ValidationError("channel labels must be unique")

    @property
    def trigger_index(self) -> int:
        return self.config.pre_trigger_samples

    def time_seconds(self, index: int) -> float:
        if not 0 <= index < len(self.samples):
            raise IndexError(index)
        return (index - self.trigger_index) / self.config.sample_rate_hz

    def channel_samples(self, channel_id: int) -> NDArray[np.uint8]:
        """Return one packed-request-position bit as a vectorized uint8 view."""
        if type(channel_id) is not int or channel_id not in self.config.channel_ids:
            raise ValidationError("channel is not captured")
        bit = self.config.channel_ids.index(channel_id)
        words = self.samples.astype(np.uint32, copy=False)
        return cast(NDArray[np.uint8], ((words >> bit) & 1).astype(np.uint8, copy=False))
