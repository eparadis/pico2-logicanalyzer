from __future__ import annotations

import numpy as np
import pytest

from pico_logic_analyzer.analysis import bus_csv_bytes, sampled_rows, transition_rows
from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo, ValidationError


def _result() -> CaptureResult:
    config = CaptureConfig(100, 1, 4, 8, "rising", (8, 0, 5))
    # Packed positions: D8 is bit 0, D0 bit 1, D5 strobe bit 2.
    return CaptureResult(config, np.array([0, 3, 7, 5, 1], dtype=np.uint16), _device())


def _device() -> DeviceInfo:
    return DeviceInfo("LOGIC_ANALYZER_TEST_V6_0", 1000, 1000, 4096, 24)


def test_transition_bus_uses_ordered_lsb_positions_and_intervals() -> None:
    rows = transition_rows(_result(), (0, 8))
    assert [(row.sample_index, row.binary, row.hexadecimal, row.decimal) for row in rows] == [
        (0, "00", "0x0", 0), (1, "11", "0x3", 3), (3, "10", "0x2", 2)
    ]
    assert rows[0].end_sample_index == 1 and rows[-1].duration_seconds is None
    assert bus_csv_bytes(rows).startswith(b"sample_index,time_seconds,binary,hexadecimal,decimal,")


def test_sampled_bus_uses_only_real_distinct_strobe_edges() -> None:
    result = _result()
    rising = sampled_rows(result, (0, 8), 5, "rising")
    falling = sampled_rows(result, (0, 8), 5, "falling")
    assert [(row.sample_index, row.decimal) for row in rising] == [(2, 3)]
    assert [(row.sample_index, row.decimal) for row in falling] == [(4, 2)]
    assert all(row.end_sample_index is None for row in rising + falling)


def test_bus_rejects_invalid_distinctness_and_empty_capture() -> None:
    result = _result()
    with pytest.raises(ValidationError):
        transition_rows(result, ())
    with pytest.raises(ValidationError):
        sampled_rows(result, (0,), 0, "rising")
    empty = CaptureResult(
        CaptureConfig(100, 0, 1, 0, "rising", (0,)), np.array([0], dtype=np.uint8), _device()
    )
    assert transition_rows(empty, (0,))[0].sample_index == 0
