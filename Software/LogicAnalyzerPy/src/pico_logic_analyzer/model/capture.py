from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

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
        if self.channel_count < 8 or any(
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
            or any(type(value) is not int for value in self.channel_ids)
            or self.channel_ids != tuple(range(8))
        ):
            raise ValidationError("Cycle 1 requires exactly D0-D7 in ascending order")
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
        if self.requested_count > device.buffer_size:
            raise ValidationError("sample count exceeds device buffer")
        if any(
            value > 0xFFFFFFFF
            for value in (self.sample_rate_hz, self.pre_trigger_samples, self.post_trigger_samples)
        ):
            raise ValidationError("capture field exceeds uint32")


@dataclass(frozen=True, slots=True)
class CaptureResult:
    config: CaptureConfig
    samples: NDArray[np.uint8]
    device: DeviceInfo
    channel_labels: tuple[str, ...] = tuple(f"D{i}" for i in range(8))
    channel_mapping: tuple[str, ...] = tuple(f"D{i}" for i in range(8))

    def __post_init__(self) -> None:
        if (
            not isinstance(self.samples, np.ndarray)
            or self.samples.dtype != np.dtype("uint8")
            or self.samples.ndim != 1
        ):
            raise ValidationError("samples must be a rank-one uint8 array")
        if not self.samples.flags.c_contiguous or len(self.samples) != self.config.requested_count:
            raise ValidationError("sample count or memory layout is invalid")
        self.config.validate_for(self.device)
        metadata = (self.channel_labels, self.channel_mapping)
        if any(
            type(values) is not tuple
            or len(values) != 8
            or any(type(value) is not str or len(value) > 128 for value in values)
            for values in metadata
        ):
            raise ValidationError("Cycle 1 requires eight labels and mappings")

    @property
    def trigger_index(self) -> int:
        return self.config.pre_trigger_samples

    def time_seconds(self, index: int) -> float:
        if not 0 <= index < len(self.samples):
            raise IndexError(index)
        return (index - self.trigger_index) / self.config.sample_rate_hz
