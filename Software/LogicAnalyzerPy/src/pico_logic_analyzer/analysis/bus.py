"""Parallel-bus extraction from packed capture words."""

from __future__ import annotations

import csv
import io
from dataclasses import asdict, dataclass

import numpy as np
from numpy.typing import NDArray

from pico_logic_analyzer.model import CaptureResult, ValidationError

MAX_BUS_ROWS = 100_000


@dataclass(frozen=True, slots=True)
class BusRow:
    sample_index: int
    time_seconds: str
    binary: str
    hexadecimal: str
    decimal: int
    end_sample_index: int | None
    end_time_seconds: str | None
    duration_seconds: str | None

    def json_object(self) -> dict[str, object]:
        return asdict(self)


def _validate(result: CaptureResult, channels: tuple[int, ...], strobe: int | None) -> None:
    if type(channels) is not tuple or not channels or len(set(channels)) != len(channels):
        raise ValidationError("bus channels must be a nonempty unique tuple")
    if any(
        type(channel) is not int or channel not in result.config.channel_ids for channel in channels
    ):
        raise ValidationError("bus channel is not captured")
    if strobe is not None and (
        type(strobe) is not int or strobe not in result.config.channel_ids or strobe in channels
    ):
        raise ValidationError("strobe must be a distinct captured channel")


def _values(result: CaptureResult, channels: tuple[int, ...]) -> NDArray[np.uint32]:
    values = np.zeros(len(result.samples), dtype=np.uint32)
    words = result.samples.astype(np.uint32, copy=False)
    for output_bit, channel in enumerate(channels):
        packed_bit = result.config.channel_ids.index(channel)
        values |= (((words >> packed_bit) & 1) << output_bit).astype(np.uint32, copy=False)
    return values


def _format(value: int, width: int) -> tuple[str, str]:
    digits = max(1, (width + 3) // 4)
    return f"{value:0{width}b}", f"0x{value:0{digits}X}"


def _time(result: CaptureResult, index: int) -> str:
    return format(result.time_seconds(index), ".12g")


def _row(
    result: CaptureResult, values: NDArray[np.uint32], width: int, index: int, end: int | None
) -> BusRow:
    value = int(values[index])
    binary, hexadecimal = _format(value, width)
    return BusRow(
        index,
        _time(result, index),
        binary,
        hexadecimal,
        value,
        end,
        None if end is None else _time(result, end),
        None if end is None else format((end - index) / result.config.sample_rate_hz, ".12g"),
    )


def transition_rows(result: CaptureResult, channels: tuple[int, ...]) -> list[BusRow]:
    """Emit sample-zero and value-change intervals for ordered LSB-first channels."""
    _validate(result, channels, None)
    values = _values(result, channels)
    if not len(values):
        return []
    starts = np.concatenate((np.array([0]), np.flatnonzero(values[1:] != values[:-1]) + 1))
    if len(starts) > MAX_BUS_ROWS:
        raise ValidationError("bus row limit exceeded")
    return [
        _row(
            result,
            values,
            len(channels),
            int(start),
            None if pos + 1 == len(starts) else int(starts[pos + 1]),
        )
        for pos, start in enumerate(starts)
    ]


def sampled_rows(
    result: CaptureResult, channels: tuple[int, ...], strobe: int, edge: str
) -> list[BusRow]:
    """Emit rows only for actual i-1 to i transitions of a distinct strobe."""
    _validate(result, channels, strobe)
    if edge not in ("rising", "falling"):
        raise ValidationError("strobe edge must be rising or falling")
    values = _values(result, channels)
    strobe_values = result.channel_samples(strobe)
    target = 1 if edge == "rising" else 0
    indexes = (
        np.flatnonzero((strobe_values[1:] != strobe_values[:-1]) & (strobe_values[1:] == target))
        + 1
    )
    if len(indexes) > MAX_BUS_ROWS:
        raise ValidationError("bus row limit exceeded")
    return [_row(result, values, len(channels), int(index), None) for index in indexes]


def bus_csv_bytes(rows: list[BusRow]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(BusRow.__dataclass_fields__.keys())
    for row in rows:
        writer.writerow(
            "" if value is None else value
            for value in (
                row.sample_index,
                row.time_seconds,
                row.binary,
                row.hexadecimal,
                row.decimal,
                row.end_sample_index,
                row.end_time_seconds,
                row.duration_seconds,
            )
        )
    return output.getvalue().encode("utf-8")
