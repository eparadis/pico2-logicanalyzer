"""Strict-mypy-only external-style consumer of the public Cycle 3 API."""

from collections.abc import Mapping

from pico_logic_analyzer.decode import DecodeResult, PythonRecord, decode_capture
from pico_logic_analyzer.model import CaptureResult


def consume(
    capture: CaptureResult,
    decoder: str,
    channels: Mapping[str, int],
    options: Mapping[str, object],
) -> tuple[str, int]:
    result: DecodeResult = decode_capture(capture, decoder, channels, options)
    python_records: tuple[PythonRecord, ...] = tuple(
        record for record in result.records if isinstance(record, PythonRecord)
    )
    return result.decoder.id, len(python_records)
