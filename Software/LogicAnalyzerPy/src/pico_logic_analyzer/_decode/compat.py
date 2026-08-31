"""Closed, inert API-v3 compatibility surface for the private decoder worker."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal, cast

from .model import (
    AnnotationValue,
    BinaryValue,
    DecodeRecord,
    MetadataValue,
    RationalTime,
    RecordTime,
    ResultFailure,
    SpiData,
    TaggedValue,
    tagged_value,
)

SRD_CONF_SAMPLERATE = 0
OUTPUT_ANN = 0
OUTPUT_PYTHON = 1
OUTPUT_BINARY = 2
OUTPUT_META = 4
_OUTPUT_TYPES = frozenset({OUTPUT_ANN, OUTPUT_PYTHON, OUTPUT_BINARY, OUTPUT_META})


class EndOfInput(BaseException):
    """Host-owned normal termination; decoder ``except Exception`` cannot catch it."""


@dataclass(frozen=True)
class Registration:
    output_type: int
    proto_id: str | None
    meta: object | None


class ApiV3Host:
    """Stateful request-local shim; it contains no decoder import or process operation."""

    def __init__(
        self,
        channel_names: tuple[str, ...],
        mapping: Mapping[str, int],
        channel_ids: tuple[int, ...],
        samples: tuple[int, ...],
        samplerate_hz: int,
        trigger_index: int,
        options: Mapping[str, object],
        spi_data_type: type[object] | None = None,
    ) -> None:
        if (
            type(channel_names) is not tuple
            or not channel_names
            or any(type(name) is not str for name in channel_names)
            or len(set(channel_names)) != len(channel_names)
            or type(channel_ids) is not tuple
            or not channel_ids
            or len(set(channel_ids)) != len(channel_ids)
            or any(
                type(identifier) is not int or not 0 <= identifier <= 23
                for identifier in channel_ids
            )
            or type(samples) is not tuple
            or not samples
            or any(
                type(sample) is not int or sample < 0 or sample >> len(channel_ids)
                for sample in samples
            )
            or type(samplerate_hz) is not int
            or samplerate_hz <= 0
            or type(trigger_index) is not int
            or not 0 <= trigger_index < len(samples)
        ):
            raise ResultFailure("compatibility capture rejected")
        if not isinstance(mapping, Mapping) or set(mapping) - set(channel_names):
            raise ResultFailure("compatibility mapping rejected")
        if any(
            type(key) is not str or type(value) is not int or value not in channel_ids
            for key, value in mapping.items()
        ):
            raise ResultFailure("compatibility mapping rejected")
        self.options = MappingProxyType(dict(options))
        self.samplenum = -1
        self.matched: tuple[bool, ...] = ()
        self._channel_names = channel_names
        self._mapping = MappingProxyType(dict(mapping))
        self._channel_ids = channel_ids
        self._samples = samples
        self._samplerate_hz = samplerate_hz
        self._trigger_index = trigger_index
        self._registrations: list[Registration] = []
        self._records: list[DecodeRecord] = []
        self._metadata_calls: list[tuple[int, int]] = []
        self._wait_calls = 0
        self._spi_data_type = spi_data_type
        self._spi_transfer_absent = (
            "mosi" not in self._mapping,
            "miso" not in self._mapping,
        )

    @property
    def records(self) -> tuple[DecodeRecord, ...]:
        return tuple(self._records)

    @property
    def registrations(self) -> tuple[Registration, ...]:
        return tuple(self._registrations)

    @property
    def metadata_calls(self) -> tuple[tuple[int, int], ...]:
        return tuple(self._metadata_calls)

    def has_channel(self, index: int) -> bool:
        if type(index) is not int or not 0 <= index < len(self._channel_names):
            raise ResultFailure("channel rejected")
        return self._channel_names[index] in self._mapping

    def metadata(self, key: int, value: int) -> None:
        if (
            key != SRD_CONF_SAMPLERATE
            or type(value) is not int
            or value != self._samplerate_hz
            or self._metadata_calls
        ):
            raise ResultFailure("metadata rejected")
        self._metadata_calls.append((key, value))

    def register(
        self, output_type: int, proto_id: str | None = None, meta: object | None = None
    ) -> int:
        if (
            type(output_type) is not int
            or output_type not in _OUTPUT_TYPES
            or (proto_id is not None and type(proto_id) is not str)
            or (output_type == OUTPUT_META and not _metadata_declaration(meta))
        ):
            raise ResultFailure("registration rejected")
        output_id = len(self._registrations)
        self._registrations.append(Registration(output_type, proto_id, meta))
        return output_id

    def put(self, ss: int, es: int, output_id: int, value: object) -> None:
        if (
            type(ss) is not int
            or type(es) is not int
            or type(output_id) is not int
            or not 0 <= ss <= es <= len(self._samples)
            or not 0 <= output_id < len(self._registrations)
        ):
            raise ResultFailure("put rejected")
        registration = self._registrations[output_id]
        kind, normalized = self._normalize(registration.output_type, value)
        self._records.append(
            DecodeRecord(
                len(self._records),
                ss,
                es,
                output_id,
                kind,
                normalized,
                self._time(ss),
                self._time(es),
            )
        )

    def wait(self, condition: object = None) -> tuple[int, ...]:
        self._wait_calls += 1
        if self._wait_calls > len(self._samples) * 4:
            raise ResultFailure("wait limit")
        alternatives, empty = self._conditions(condition)
        if empty:
            start = 0 if self.samplenum < 0 else self.samplenum + 1
            return self._return_at(start, (True,))
        start = max(self.samplenum, 0)
        for index in range(start, len(self._samples)):
            matches = tuple(self._matches(part, index) for part in alternatives)
            if any(matches):
                return self._return_at(index, matches)
        self.samplenum = len(self._samples)
        self.matched = tuple(False for _ in alternatives)
        raise EndOfInput()

    def _conditions(self, condition: object) -> tuple[tuple[Mapping[object, object], ...], bool]:
        if condition == {}:
            return (), True
        raw = (condition,) if isinstance(condition, Mapping) else condition
        if type(raw) is not tuple and type(raw) is not list:
            raise ResultFailure("wait rejected")
        if not raw:
            raise ResultFailure("wait rejected")
        alternatives = tuple(self._condition_dict(part) for part in raw)
        return alternatives, False

    def _condition_dict(self, condition: object) -> Mapping[object, object]:
        if not isinstance(condition, Mapping) or not condition:
            raise ResultFailure("wait rejected")
        if "skip" in condition:
            if len(condition) != 1 or type(condition["skip"]) is not int or condition["skip"] < 0:
                raise ResultFailure("wait rejected")
            return MappingProxyType(dict(condition))
        normalized: dict[object, object] = {}
        for key, predicate in condition.items():
            index = self._channel_index(key)
            if index in normalized or predicate not in {"r", "f", "e", "h"}:
                raise ResultFailure("wait rejected")
            normalized[index] = predicate
        return MappingProxyType(normalized)

    def _channel_index(self, key: object) -> int:
        if type(key) is int:
            index = key
        else:
            raise ResultFailure("wait rejected")
        if not 0 <= index < len(self._channel_names):
            raise ResultFailure("wait rejected")
        return index

    def _matches(self, condition: Mapping[object, object], index: int) -> bool:
        if "skip" in condition:
            skip = condition["skip"]
            if type(skip) is not int:
                raise ResultFailure("wait rejected")
            return index == max(self.samplenum, 0) + skip
        if self.samplenum >= 0 and index <= self.samplenum:
            return False
        return all(self._predicate(index, key, predicate) for key, predicate in condition.items())

    def _predicate(self, index: int, key: object, predicate: object) -> bool:
        channel = self._channel_index(key)
        current = self._pin(index, channel)
        if current == 255:
            return False
        if predicate == "h":
            return current == 1
        if index == 0:
            return False
        previous = self._pin(index - 1, channel)
        if previous == 255:
            return False
        return (
            (predicate == "r" and previous == 0 and current == 1)
            or (predicate == "f" and previous == 1 and current == 0)
            or (predicate == "e" and previous != current)
        )

    def _return_at(self, index: int, matches: tuple[bool, ...]) -> tuple[int, ...]:
        if not 0 <= index < len(self._samples):
            self.samplenum = len(self._samples)
            self.matched = matches
            raise EndOfInput()
        self.samplenum = index
        self.matched = matches
        return tuple(self._pin(index, channel) for channel in range(len(self._channel_names)))

    def _pin(self, sample: int, decoder_channel: int) -> int:
        name = self._channel_names[decoder_channel]
        physical = self._mapping.get(name)
        if physical is None:
            return 255
        position = self._channel_ids.index(physical)
        return (self._samples[sample] >> position) & 1

    def _time(self, sample: int) -> RecordTime:
        return RecordTime(
            RationalTime(sample, self._samplerate_hz),
            RationalTime(sample - self._trigger_index, self._samplerate_hz),
        )

    def _normalize(
        self, output_type: int, value: object
    ) -> tuple[
        Literal["annotation", "python", "binary", "metadata"],
        TaggedValue | AnnotationValue | BinaryValue | MetadataValue,
    ]:
        if output_type == OUTPUT_ANN:
            sequence = _sequence(value)
            texts = _string_sequence(sequence[1]) if len(sequence) == 2 else ()
            if (
                len(sequence) != 2
                or type(sequence[0]) is not int
                or sequence[0] < 0
                or not texts
            ):
                raise ResultFailure("annotation rejected")
            return "annotation", AnnotationValue(sequence[0], texts)
        if output_type == OUTPUT_PYTHON:
            return "python", _normalize_python_value(
                value,
                spi_data_type=self._spi_data_type,
                spi_transfer_absent=self._spi_transfer_absent,
            )
        if output_type == OUTPUT_BINARY:
            sequence = _sequence(value)
            if (
                len(sequence) != 2
                or type(sequence[0]) is not int
                or sequence[0] < 0
                or type(sequence[1]) is not bytes
            ):
                raise ResultFailure("binary rejected")
            return "binary", BinaryValue(sequence[0], sequence[1])
        if type(value) is not int:
            raise ResultFailure("metadata rejected")
        return "metadata", MetadataValue("integer", value)


class ShimAdapter:
    """Exact uppercase bridge consumed by the frozen local ``sigrokdecode.py`` shim."""

    def __init__(self, host: ApiV3Host) -> None:
        self._host = host
        self._decoder: object | None = None

    def bind_decoder(self, decoder: object) -> None:
        """Bind the one trusted frozen instance so wait state mirrors API-v3."""
        self._decoder = decoder

    def HasChannel(self, channel: int) -> bool:
        return self._host.has_channel(channel)

    def Wait(self, conditions: object = None) -> tuple[int, ...]:
        values = self._host.wait(conditions)
        if self._decoder is not None:
            setattr(self._decoder, "samplenum", self._host.samplenum)
            setattr(self._decoder, "matched", self._host.matched)
        return values

    def Put(self, ss: int, es: int, output_id: int, value: object) -> None:
        self._host.put(ss, es, output_id, value)

    def Register(self, output_type: int, meta: object | None = None) -> int:
        return self._host.register(output_type, meta=meta)


def _sequence(value: object) -> tuple[object, ...]:
    if type(value) is list or type(value) is tuple:
        return tuple(value)
    raise ResultFailure("value rejected")


def _string_sequence(value: object) -> tuple[str, ...]:
    sequence = _sequence(value)
    if any(type(item) is not str for item in sequence):
        raise ResultFailure("annotation rejected")
    return tuple(cast(str, item) for item in sequence)


def _metadata_declaration(value: object | None) -> bool:
    return (
        type(value) is tuple
        and len(value) == 3
        and value[0] is int
        and type(value[1]) is str
        and type(value[2]) is str
    )


def _normalize_python_value(
    value: object,
    seen: set[int] | None = None,
    depth: int = 1,
    spi_data_type: type[object] | None = None,
    spi_transfer_absent: tuple[bool, bool] = (False, False),
) -> TaggedValue:
    if depth > 32:
        raise ResultFailure("python value rejected")
    if value is None or type(value) in {bool, int, float, str, bytes}:
        tagged_value(value)
        return cast(TaggedValue, value)
    if spi_data_type is not None and type(value) is spi_data_type:
        data_ss, data_es, data_val = cast(tuple[object, object, object], value)
        if type(data_ss) is not int or type(data_es) is not int or type(data_val) is not int:
            raise ResultFailure("python value rejected")
        return SpiData(data_ss, data_es, data_val)
    if type(value) is not list and type(value) is not tuple:
        raise ResultFailure("python value rejected")
    active = set() if seen is None else seen
    marker = id(value)
    if marker in active:
        raise ResultFailure("python value rejected")
    active.add(marker)
    try:
        if _is_spi_bits_packet(value, spi_data_type):
            normalized = _normalize_spi_bits_packet(value)
        elif _is_spi_transfer_packet(value, spi_data_type):
            normalized = _normalize_spi_transfer_packet(
                value, spi_data_type, spi_transfer_absent
            )
        elif _is_uart_signal_packet(value):
            normalized = _normalize_uart_signal_packet(value)
        elif _is_uart_data_packet(value):
            normalized = _normalize_uart_data_packet(value)
        else:
            normalized = [
                _normalize_python_value(
                    item,
                    active,
                    depth + 1,
                    spi_data_type,
                    spi_transfer_absent,
                )
                for item in value
            ]
    finally:
        active.remove(marker)
    return normalized if type(value) is list else tuple(normalized)


def _is_spi_bits_packet(value: object, spi_data_type: type[object] | None) -> bool:
    """Recognize SPI's documented BITS packet without widening generic lists."""
    return (
        spi_data_type is not None
        and type(value) is list
        and len(value) == 3
        and value[0] == "BITS"
    )


def _normalize_spi_bits_packet(value: list[object] | tuple[object, ...]) -> list[TaggedValue]:
    normalized: list[TaggedValue] = ["BITS"]
    for bits in value[1:]:
        if bits is None:
            normalized.append(None)
            continue
        if type(bits) is not list:
            raise ResultFailure("python value rejected")
        normalized_bits: list[TaggedValue] = []
        for bit in bits:
            if (
                type(bit) is not list
                or len(bit) != 3
                or any(type(item) is not int for item in bit)
            ):
                raise ResultFailure("python value rejected")
            bit_value, start_sample, end_sample = bit
            if start_sample < 0 or end_sample < start_sample:
                raise ResultFailure("python value rejected")
            normalized_bits.append(SpiData(start_sample, end_sample, bit_value))
        normalized.append(normalized_bits)
    return normalized


def _is_spi_transfer_packet(value: object, spi_data_type: type[object] | None) -> bool:
    return (
        spi_data_type is not None
        and type(value) is list
        and len(value) == 3
        and value[0] == "TRANSFER"
    )


def _normalize_spi_transfer_packet(
    value: list[object] | tuple[object, ...],
    spi_data_type: type[object] | None,
    absent: tuple[bool, bool],
) -> list[TaggedValue]:
    normalized: list[TaggedValue] = ["TRANSFER"]
    for payload, is_absent in zip(value[1:], absent, strict=True):
        if is_absent:
            if type(payload) is not list or payload:
                raise ResultFailure("python value rejected")
            normalized.append(None)
            continue
        normalized.append(_normalize_python_value(payload, spi_data_type=spi_data_type))
    return normalized


_UART_SIGNAL_PACKETS = frozenset(
    {"STARTBIT", "INVALID STARTBIT", "PARITYBIT", "INVALID STOPBIT", "STOPBIT"}
)


def _is_uart_signal_packet(value: object) -> bool:
    return (
        type(value) is list
        and len(value) == 3
        and type(value[0]) is str
        and value[0] in _UART_SIGNAL_PACKETS
        and type(value[1]) is int
        and type(value[2]) is bool
    )


def _normalize_uart_signal_packet(value: list[object] | tuple[object, ...]) -> list[TaggedValue]:
    return [cast(str, value[0]), cast(int, value[1]), int(cast(bool, value[2]))]


def _is_uart_data_packet(value: object) -> bool:
    return (
        type(value) is list
        and len(value) == 3
        and value[0] == "DATA"
        and type(value[1]) is int
        and type(value[2]) is tuple
        and len(value[2]) == 2
        and type(value[2][0]) is int
        and type(value[2][1]) is list
    )


def _normalize_uart_data_packet(value: list[object] | tuple[object, ...]) -> list[TaggedValue]:
    data = cast(tuple[object, object], value[2])
    data_value = data[0]
    if type(data_value) is not int:
        raise ResultFailure("python value rejected")
    bit_rows = cast(list[object], data[1])
    normalized_rows: list[TaggedValue] = []
    for row in bit_rows:
        if type(row) is not list or len(row) != 3:
            raise ResultFailure("python value rejected")
        bit, start_sample, end_sample = row
        if type(bit) is bool:
            bit = int(bit)
        if (
            type(bit) is not int
            or type(start_sample) is not int
            or type(end_sample) is not int
        ):
            raise ResultFailure("python value rejected")
        normalized_rows.append([bit, start_sample, end_sample])
    return ["DATA", cast(int, value[1]), (data_value, normalized_rows)]
