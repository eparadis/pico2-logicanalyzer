"""Private immutable B2 host models and exact validation materialization."""

from __future__ import annotations

import base64
import json
import math
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal


class HostFailure(RuntimeError):
    """Stable private failure category, intentionally without implementation detail."""


class RequestFailure(HostFailure):
    pass


class ResultFailure(HostFailure):
    pass


class WorkerFailure(HostFailure):
    pass


HARD_LIMITS: Mapping[str, int] = MappingProxyType(
    {
        "input_samples": 65536,
        "request_bytes": 4194304,
        "wall_deadline_ms": 5000,
        "terminate_grace_ms": 250,
        "worker_address_space_bytes": 68719476736,
        "recursion_limit": 320,
        "output_records": 16384,
        "encoded_bytes": 2097152,
        "decoded_bytes": 2097152,
        "stdout_bytes": 65536,
        "stderr_bytes": 65536,
        "diagnostic_bytes": 8192,
        "text_bytes": 524288,
        "binary_bytes": 262144,
        "nested_depth": 32,
        "nested_items": 16384,
        "retained_result_bytes": 8388608,
        "spi_max_word_size_bits": 8,
    }
)
REGRESSION_LIMITS: Mapping[str, int] = MappingProxyType(
    {
        "worker_peak_rss_bytes": 134217728,
        "parent_retained_growth_bytes": 33554432,
        "successful_parent_total_ns": 1300000000,
        "launch_ns": 50000000,
        "reap_ns": 50000000,
        "child_load_ns": 100000000,
        "child_import_ns": 100000000,
        "child_decode_ns": 100000000,
        "timeout_cleanup_total_ns": 5500000000,
        "terminate_to_reap_ns": 300000000,
        "kill_to_reap_ns": 50000000,
    }
)
LIMITS = HARD_LIMITS
@dataclass(frozen=True)
class SpiData:
    ss: int
    es: int
    value: int

    def __post_init__(self) -> None:
        if any(type(item) is not int or item < 0 for item in (self.ss, self.es, self.value)):
            raise ResultFailure("spi data rejected")


type TaggedValue = (
    None | bool | int | float | str | bytes | tuple[TaggedValue, ...] | list[TaggedValue] | SpiData
)

FAILURE_CODES = frozenset(
    {
        "snapshot",
        "import",
        "ipc",
        "decoder",
        "recursion",
        "memory",
        "process-exit",
        "timeout",
        "cancelled",
        "output-limit",
    }
)


@dataclass(frozen=True)
class DecodeFailure:
    code: str
    message: str
    schema: Literal["pico-logic-analyzer.decode-error/v1"] = "pico-logic-analyzer.decode-error/v1"

    def __post_init__(self) -> None:
        if (
            self.code not in FAILURE_CODES
            or type(self.message) is not str
            or not self.message
            or len(self.message.encode()) > HARD_LIMITS["diagnostic_bytes"]
            or "/" in self.message
            or "\\" in self.message
            or "traceback" in self.message.lower()
        ):
            raise RequestFailure("failure rejected")

    def to_dict(self) -> dict[str, str]:
        return {"schema": self.schema, "code": self.code, "message": self.message}


@dataclass(frozen=True)
class CaptureIdentity:
    sample_count: int
    trigger_index: int
    channel_ids: tuple[int, ...]

    def __post_init__(self) -> None:
        if (
            type(self.sample_count) is not int
            or self.sample_count <= 0
            or type(self.trigger_index) is not int
            or not 0 <= self.trigger_index < self.sample_count
            or not self.channel_ids
            or any(type(value) is not int or not 0 <= value <= 23 for value in self.channel_ids)
            or len(set(self.channel_ids)) != len(self.channel_ids)
        ):
            raise RequestFailure("capture rejected")


def tagged_value(value: object) -> dict[str, object]:
    if value is None:
        return {"tag": "null"}
    if type(value) is bool:
        return {"tag": "bool", "value": value}
    if type(value) is int:
        return {"tag": "integer", "value": value}
    if type(value) is float:
        if not math.isfinite(value):
            raise ResultFailure("value rejected")
        return {"tag": "float", "value": value}
    if isinstance(value, str):
        return {"tag": "string", "value": value}
    if isinstance(value, bytes):
        return {"tag": "bytes", "value": base64.b64encode(value).decode("ascii")}
    if type(value) is SpiData:
        return {"tag": "spi-data", "ss": value.ss, "es": value.es, "val": value.value}
    if type(value) is tuple:
        return {"tag": "tuple", "value": [tagged_value(item) for item in value]}
    if type(value) is list:
        return {"tag": "list", "value": [tagged_value(item) for item in value]}
    raise ResultFailure("value rejected")


@dataclass(frozen=True)
class RationalTime:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        if (
            type(self.numerator) is not int
            or type(self.denominator) is not int
            or self.denominator <= 0
        ):
            raise RequestFailure("time rejected")

    def to_dict(self) -> dict[str, int]:
        return {"numerator": self.numerator, "denominator": self.denominator}


@dataclass(frozen=True)
class RecordTime:
    absolute: RationalTime
    trigger_relative: RationalTime

    def to_dict(self) -> dict[str, dict[str, int]]:
        return {
            "absolute": self.absolute.to_dict(),
            "trigger_relative": self.trigger_relative.to_dict(),
        }


@dataclass(frozen=True)
class AnnotationDeclaration:
    identifier: str
    index: int
    description: str

    def __post_init__(self) -> None:
        if (
            not isinstance(self.identifier, str)
            or type(self.index) is not int
            or self.index < 0
            or not isinstance(self.description, str)
        ):
            raise ResultFailure("declaration rejected")

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.identifier,
            "index": self.index,
            "description": self.description,
        }


@dataclass(frozen=True)
class AnnotationRowDeclaration:
    identifier: str
    index: int
    description: str
    annotation_indices: tuple[int, ...]

    def __post_init__(self) -> None:
        if (
            not isinstance(self.identifier, str)
            or type(self.index) is not int
            or self.index < 0
            or not isinstance(self.description, str)
            or type(self.annotation_indices) is not tuple
            or any(type(item) is not int or item < 0 for item in self.annotation_indices)
        ):
            raise ResultFailure("declaration rejected")

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.identifier,
            "index": self.index,
            "description": self.description,
            "annotation_indices": list(self.annotation_indices),
        }


@dataclass(frozen=True)
class BinaryDeclaration(AnnotationDeclaration):
    pass


@dataclass(frozen=True)
class MetadataDeclaration:
    output_id: int
    value_type: Literal["integer"]
    name: str
    description: str

    def __post_init__(self) -> None:
        if (
            type(self.output_id) is not int
            or self.output_id < 0
            or self.value_type != "integer"
            or not isinstance(self.name, str)
            or not isinstance(self.description, str)
        ):
            raise ResultFailure("declaration rejected")

    def to_dict(self) -> dict[str, object]:
        return {
            "output_id": self.output_id,
            "value_type": self.value_type,
            "name": self.name,
            "description": self.description,
        }


type Declaration = (
    AnnotationDeclaration | AnnotationRowDeclaration | BinaryDeclaration | MetadataDeclaration
)


@dataclass(frozen=True)
class AnnotationValue:
    class_index: int
    texts: tuple[str, ...]

    def __post_init__(self) -> None:
        if (
            type(self.class_index) is not int
            or self.class_index < 0
            or type(self.texts) is not tuple
            or not self.texts
            or any(not isinstance(text, str) for text in self.texts)
        ):
            raise ResultFailure("annotation rejected")

    def to_dict(self) -> dict[str, object]:
        return {"class_index": self.class_index, "texts": list(self.texts)}


@dataclass(frozen=True)
class BinaryValue:
    class_index: int
    data: bytes

    def __post_init__(self) -> None:
        if (
            type(self.class_index) is not int
            or self.class_index < 0
            or type(self.data) is not bytes
        ):
            raise ResultFailure("binary rejected")

    def to_dict(self) -> dict[str, object]:
        return {
            "class_index": self.class_index,
            "data_base64": base64.b64encode(self.data).decode("ascii"),
        }


@dataclass(frozen=True)
class MetadataValue:
    value_type: Literal["integer"]
    value: int

    def __post_init__(self) -> None:
        if self.value_type != "integer" or type(self.value) is not int:
            raise ResultFailure("metadata rejected")

    def to_dict(self) -> dict[str, object]:
        return {"value_type": self.value_type, "value": self.value}


@dataclass(frozen=True)
class DecodeRecord:
    emission_index: int
    start_sample: int
    end_sample: int
    output_id: int
    kind: Literal["annotation", "python", "binary", "metadata"]
    value: TaggedValue | AnnotationValue | BinaryValue | MetadataValue
    start_time: RecordTime
    end_time: RecordTime

    def __post_init__(self) -> None:
        if (
            type(self.emission_index) is not int
            or self.emission_index < 0
            or type(self.start_sample) is not int
            or type(self.end_sample) is not int
            or self.start_sample < 0
            or self.end_sample < self.start_sample
            or type(self.output_id) is not int
            or self.output_id < 0
            or self.kind not in {"annotation", "python", "binary", "metadata"}
            or (self.kind == "annotation" and type(self.value) is not AnnotationValue)
            or (self.kind == "binary" and type(self.value) is not BinaryValue)
            or (self.kind == "metadata" and type(self.value) is not MetadataValue)
            or (
                self.kind == "python"
                and type(self.value) in {AnnotationValue, BinaryValue, MetadataValue}
            )
        ):
            raise ResultFailure("record rejected")

    def to_dict(self) -> dict[str, object]:
        return {
            "emission_index": self.emission_index,
            "start_sample": self.start_sample,
            "end_sample": self.end_sample,
            "start_time": self.start_time.to_dict(),
            "end_time": self.end_time.to_dict(),
            "output_id": self.output_id,
            "kind": self.kind,
            "value": self._value_dict(),
        }

    def _value_dict(self) -> dict[str, object]:
        if self.kind == "python":
            value = self.value
            if type(value) in {AnnotationValue, BinaryValue, MetadataValue}:
                raise ResultFailure("record rejected")
            return tagged_value(value)
        if isinstance(self.value, AnnotationValue | BinaryValue | MetadataValue):
            return self.value.to_dict()
        raise ResultFailure("record rejected")


@dataclass(frozen=True)
class DecodeResult:
    decoder: str
    file_set_sha256: str
    samplerate_hz: int
    capture: CaptureIdentity
    channels: Mapping[str, int]
    options: Mapping[str, object]
    declarations: tuple[Declaration, ...]
    records: tuple[DecodeRecord, ...]
    schema: Literal["pico-logic-analyzer.decode-result/v1"] = "pico-logic-analyzer.decode-result/v1"

    def __post_init__(self) -> None:
        if (
            self.decoder not in _CHANNELS
            or not isinstance(self.file_set_sha256, str)
            or len(self.file_set_sha256) != 64
            or any(character not in "0123456789abcdef" for character in self.file_set_sha256)
            or type(self.samplerate_hz) is not int
            or self.samplerate_hz <= 0
            or type(self.declarations) is not tuple
            or type(self.records) is not tuple
            or tuple(record.emission_index for record in self.records)
            != tuple(range(len(self.records)))
        ):
            raise ResultFailure("result rejected")
        frozen_channels = _freeze_mapping(self.channels, ResultFailure)
        if any(
            type(key) is not str or type(value) is not int
            for key, value in frozen_channels.items()
        ):
            raise ResultFailure("result rejected")
        if any(not _option_scalar(value) for value in self.options.values()):
            raise ResultFailure("result rejected")
        _validate_result_limits(self.declarations, self.records)
        object.__setattr__(self, "channels", frozen_channels)
        object.__setattr__(self, "options", _freeze_mapping(self.options, ResultFailure))

    def to_dict(self) -> dict[str, object]:
        declarations: dict[str, list[dict[str, object]]] = {
            "annotations": [],
            "annotation_rows": [],
            "binary": [],
            "metadata": [],
        }
        for declaration in self.declarations:
            key = (
                "annotations"
                if type(declaration) is AnnotationDeclaration
                else "annotation_rows"
                if type(declaration) is AnnotationRowDeclaration
                else "binary"
                if type(declaration) is BinaryDeclaration
                else "metadata"
            )
            declarations[key].append(declaration.to_dict())
        return {
            "schema": self.schema,
            "decoder": {"id": self.decoder, "file_set_sha256": self.file_set_sha256},
            "samplerate_hz": self.samplerate_hz,
            "capture": {
                "sample_count": self.capture.sample_count,
                "trigger_index": self.capture.trigger_index,
            },
            "channels": [
                {"decoder_channel": key, "physical_channel": value}
                for key, value in self.channels.items()
            ],
            "options": dict(sorted(self.options.items())),
            "declarations": declarations,
            "records": [record.to_dict() for record in self.records],
        }


def canonical_json(value: Mapping[str, object]) -> bytes:
    return json.dumps(
        value, allow_nan=False, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode() + b"\n"


def _dict(value: object) -> Mapping[str, object]:
    if not isinstance(value, Mapping) or any(type(key) is not str for key in value):
        raise ResultFailure("result rejected")
    return value


def _int(value: object) -> int:
    if type(value) is not int:
        raise ResultFailure("result rejected")
    return value


def _str(value: object) -> str:
    if type(value) is not str:
        raise ResultFailure("result rejected")
    return value


def _list(value: object) -> list[object]:
    if type(value) is not list:
        raise ResultFailure("result rejected")
    return value


def _metadata_type(value: object) -> Literal["integer"]:
    if value != "integer":
        raise ResultFailure("result rejected")
    return "integer"


def _record_kind(value: object) -> Literal["annotation", "python", "binary", "metadata"]:
    if value == "annotation":
        return "annotation"
    if value == "python":
        return "python"
    if value == "binary":
        return "binary"
    if value == "metadata":
        return "metadata"
    raise ResultFailure("result rejected")


def _schema(value: object) -> Literal["pico-logic-analyzer.decode-result/v1"]:
    if value != "pico-logic-analyzer.decode-result/v1":
        raise ResultFailure("result rejected")
    return "pico-logic-analyzer.decode-result/v1"


def _tagged_from_dict(value: object) -> TaggedValue:
    item = _dict(value)
    tag = item.get("tag")
    if tag == "null" and set(item) == {"tag"}:
        return None
    raw = item.get("value")
    if tag == "bool" and type(raw) is bool:
        return raw
    if tag == "integer" and type(raw) is int:
        return raw
    if tag == "float" and type(raw) is float and math.isfinite(raw):
        return raw
    if tag == "string" and type(raw) is str:
        return raw
    if tag == "bytes" and type(raw) is str:
        try:
            return base64.b64decode(raw, validate=True)
        except (ValueError, TypeError):
            raise ResultFailure("value rejected") from None
    if tag in {"list", "tuple"} and type(raw) is list:
        values = [_tagged_from_dict(part) for part in raw]
        return values if tag == "list" else tuple(values)
    if (
        tag == "spi-data"
        and set(item) == {"tag", "ss", "es", "val"}
        and type(item.get("ss")) is int
        and type(item.get("es")) is int
        and type(item.get("val")) is int
    ):
        return SpiData(_int(item["ss"]), _int(item["es"]), _int(item["val"]))
    raise ResultFailure("value rejected")


def _time_from_dict(value: object) -> RecordTime:
    item = _dict(value)
    absolute = _dict(item.get("absolute"))
    relative = _dict(item.get("trigger_relative"))
    return RecordTime(
        RationalTime(_int(absolute.get("numerator")), _int(absolute.get("denominator"))),
        RationalTime(_int(relative.get("numerator")), _int(relative.get("denominator"))),
    )


def decode_result_from_dict(value: Mapping[str, object]) -> DecodeResult:
    item = _dict(value)
    decoder = _dict(item.get("decoder"))
    capture = _dict(item.get("capture"))
    channels_data = item.get("channels")
    declarations_data = _dict(item.get("declarations"))
    records_data = item.get("records")
    if type(channels_data) is not list or type(records_data) is not list:
        raise ResultFailure("result rejected")
    channels: dict[str, int] = {}
    for channel in _list(channels_data):
        channel_data = _dict(channel)
        name = channel_data.get("decoder_channel")
        physical = channel_data.get("physical_channel")
        if type(name) is not str or type(physical) is not int or name in channels:
            raise ResultFailure("result rejected")
        channels[_str(name)] = _int(physical)
    declarations: list[Declaration] = []
    for raw in _list(declarations_data.get("annotations", [])):
        part = _dict(raw)
        declarations.append(
            AnnotationDeclaration(
                _str(part.get("id")), _int(part.get("index")), _str(part.get("description"))
            )
        )
    for raw in _list(declarations_data.get("annotation_rows", [])):
        part = _dict(raw)
        indices = part.get("annotation_indices")
        declarations.append(
            AnnotationRowDeclaration(
                _str(part.get("id")),
                _int(part.get("index")),
                _str(part.get("description")),
                tuple(_int(index) for index in _list(indices)),
            )
        )
    for raw in _list(declarations_data.get("binary", [])):
        part = _dict(raw)
        declarations.append(
            BinaryDeclaration(
                _str(part.get("id")), _int(part.get("index")), _str(part.get("description"))
            )
        )
    for raw in _list(declarations_data.get("metadata", [])):
        part = _dict(raw)
        declarations.append(
            MetadataDeclaration(
                _int(part.get("output_id")),
                _metadata_type(part.get("value_type")),
                _str(part.get("name")),
                _str(part.get("description")),
            )
        )
    records: list[DecodeRecord] = []
    for raw in _list(records_data):
        part = _dict(raw)
        kind = part.get("kind")
        raw_value = _dict(part.get("value"))
        if kind == "annotation":
            payload: TaggedValue | AnnotationValue | BinaryValue | MetadataValue = AnnotationValue(
                _int(raw_value.get("class_index")),
                tuple(_str(text) for text in _list(raw_value.get("texts"))),
            )
        elif kind == "python":
            payload = _tagged_from_dict(raw_value)
        elif kind == "binary":
            try:
                decoded = base64.b64decode(_str(raw_value.get("data_base64")), validate=True)
            except (ValueError, TypeError):
                raise ResultFailure("binary rejected") from None
            payload = BinaryValue(_int(raw_value.get("class_index")), decoded)
        elif kind == "metadata":
            payload = MetadataValue(
                _metadata_type(raw_value.get("value_type")), _int(raw_value.get("value"))
            )
        else:
            raise ResultFailure("record rejected")
        records.append(
            DecodeRecord(
                _int(part.get("emission_index")),
                _int(part.get("start_sample")),
                _int(part.get("end_sample")),
                _int(part.get("output_id")),
                _record_kind(kind),
                payload,
                _time_from_dict(part.get("start_time")),
                _time_from_dict(part.get("end_time")),
            )
        )
    return DecodeResult(
        _str(decoder.get("id")),
        _str(decoder.get("file_set_sha256")),
        _int(item.get("samplerate_hz")),
        CaptureIdentity(
            _int(capture.get("sample_count")),
            _int(capture.get("trigger_index")),
            tuple(channels.values()),
        ),
        channels,
        _dict(item.get("options")),
        tuple(declarations),
        tuple(records),
        _schema(item.get("schema")),
    )


_CHANNELS = {"uart": 2, "spi": 4, "i2c": 2}
_MAPPING_NAMES = {
    "uart": frozenset({"rx", "tx"}),
    "spi": frozenset({"clk", "miso", "mosi", "cs"}),
    "i2c": frozenset({"scl", "sda"}),
}


def _freeze_mapping(
    value: Mapping[str, object], failure: type[HostFailure]
) -> Mapping[str, object]:
    if not isinstance(value, Mapping) or any(type(key) is not str for key in value):
        raise failure("mapping rejected")
    return MappingProxyType(dict(value))


def _option_scalar(value: object) -> bool:
    return (
        type(value) is int
        or (type(value) is float and math.isfinite(value))
        or type(value) is str
    )


def _measure_tagged(value: object, depth: int = 1) -> tuple[int, int, int, int]:
    if depth > HARD_LIMITS["nested_depth"]:
        raise ResultFailure("result limit exceeded")
    if isinstance(value, str):
        return len(value.encode()), 0, 1, depth
    if type(value) is bytes:
        return 0, len(value), 1, depth
    if type(value) is list or type(value) is tuple:
        measurements = [_measure_tagged(item, depth + 1) for item in value]
        return (
            sum(item[0] for item in measurements),
            sum(item[1] for item in measurements),
            1 + sum(item[2] for item in measurements),
            max([depth, *(item[3] for item in measurements)]),
        )
    return 0, 0, 1, depth


def _validate_result_limits(
    declarations: tuple[Declaration, ...], records: tuple[DecodeRecord, ...]
) -> None:
    text_bytes = 0
    binary_bytes = 0
    items = 0
    maximum_depth = 0
    for declaration in declarations:
        text_bytes += len(declaration.to_dict().__str__().encode())
        items += 1
    for record in records:
        items += 1
        if record.kind == "python":
            text, binary, nested_items, depth = _measure_tagged(record.value)
            text_bytes += text
            binary_bytes += binary
            items += nested_items
            maximum_depth = max(maximum_depth, depth)
        elif record.kind == "annotation":
            if not isinstance(record.value, AnnotationValue):
                raise ResultFailure("record rejected")
            text_bytes += sum(len(text.encode()) for text in record.value.texts)
        elif record.kind == "binary":
            if not isinstance(record.value, BinaryValue):
                raise ResultFailure("record rejected")
            binary_bytes += len(record.value.data)
    if (
        len(records) > HARD_LIMITS["output_records"]
        or text_bytes > HARD_LIMITS["text_bytes"]
        or binary_bytes > HARD_LIMITS["binary_bytes"]
        or items > HARD_LIMITS["nested_items"]
        or maximum_depth > HARD_LIMITS["nested_depth"]
    ):
        raise ResultFailure("result limit exceeded")


def _integer(value: object) -> int:
    if type(value) is not int:
        raise RequestFailure("options rejected")
    return value


def _string(value: object) -> str:
    if not isinstance(value, str):
        raise RequestFailure("options rejected")
    return value


def materialize_options(decoder: str, options: Mapping[str, object]) -> Mapping[str, object]:
    defaults: dict[str, dict[str, object]] = {
        "uart": {
            "baudrate": 115200,
            "data_bits": 8,
            "parity": "none",
            "stop_bits": 1.0,
            "bit_order": "lsb-first",
            "format": "hex",
            "invert_rx": "no",
            "invert_tx": "no",
            "sample_point": 50,
            "rx_packet_delim": -1,
            "tx_packet_delim": -1,
            "rx_packet_len": -1,
            "tx_packet_len": -1,
        },
        "spi": {
            "cs_polarity": "active-low",
            "cpol": 0,
            "cpha": 0,
            "bitorder": "msb-first",
            "wordsize": 8,
        },
        "i2c": {"address_format": "shifted"},
    }
    if (
        decoder not in defaults
        or not isinstance(options, Mapping)
        or any(type(k) is not str for k in options)
    ):
        raise RequestFailure("options rejected")
    safe_options: dict[str, object] = {}
    for raw_key, value in options.items():
        if type(raw_key) is str:
            safe_options[raw_key] = value
    if set(safe_options) - set(defaults[decoder]):
        raise RequestFailure("options rejected")
    result = {**defaults[decoder], **safe_options}
    if decoder == "uart":
        baud, bits, point = (_integer(result[k]) for k in ("baudrate", "data_bits", "sample_point"))
        stop = result["stop_bits"]
        if (
            baud <= 0
            or bits not in {5, 6, 7, 8, 9}
            or point not in range(1, 100)
            or type(stop) not in {int, float}
            or stop not in {0.0, 0.5, 1.0, 1.5, 2.0}
            or _string(result["parity"]) not in {"none", "odd", "even", "zero", "one", "ignore"}
            or _string(result["bit_order"]) not in {"lsb-first", "msb-first"}
            or _string(result["format"]) not in {"ascii", "dec", "hex", "oct", "bin"}
            or _string(result["invert_rx"]) not in {"yes", "no"}
            or _string(result["invert_tx"]) not in {"yes", "no"}
        ):
            raise RequestFailure("options rejected")
        maximum = (1 << bits) - 1
        for key in ("rx_packet_delim", "tx_packet_delim"):
            value = _integer(result[key])
            if value != -1 and not 0 <= value <= maximum:
                raise RequestFailure("options rejected")
        for key in ("rx_packet_len", "tx_packet_len"):
            value = _integer(result[key])
            if value != -1 and value <= 0:
                raise RequestFailure("options rejected")
    elif decoder == "spi":
        if (
            _string(result["cs_polarity"]) not in {"active-low", "active-high"}
            or _integer(result["cpol"]) not in {0, 1}
            or _integer(result["cpha"]) not in {0, 1}
            or _string(result["bitorder"]) not in {"msb-first", "lsb-first"}
            or not 1 <= _integer(result["wordsize"]) <= 8
        ):
            raise RequestFailure("options rejected")
    elif _string(result["address_format"]) not in {"shifted", "unshifted"}:
        raise RequestFailure("options rejected")
    return MappingProxyType(result)


@dataclass(frozen=True)
class DecodeRequest:
    decoder: str
    samplerate: int
    channel_ids: tuple[int, ...]
    mapping: Mapping[str, int]
    samples: tuple[int, ...]
    trigger_index: int
    options: Mapping[str, object]

    def __post_init__(self) -> None:
        if (
            self.decoder not in _CHANNELS
            or type(self.samplerate) is not int
            or self.samplerate <= 0
            or type(self.channel_ids) is not tuple
            or type(self.samples) is not tuple
            or not self.samples
            or len(self.samples) > HARD_LIMITS["input_samples"]
            or type(self.trigger_index) is not int
            or not 0 <= self.trigger_index < len(self.samples)
        ):
            raise RequestFailure("capture rejected")
        if (
            not self.channel_ids
            or any(type(x) is not int or not 0 <= x <= 23 for x in self.channel_ids)
            or len(set(self.channel_ids)) != len(self.channel_ids)
            or any(type(x) is not int or x < 0 for x in self.samples)
        ):
            raise RequestFailure("capture rejected")
        frozen_mapping = _freeze_mapping(self.mapping, RequestFailure)
        if set(frozen_mapping) - _MAPPING_NAMES[self.decoder]:
            raise RequestFailure("mapping rejected")
        if any(
            type(value) is not int or value not in self.channel_ids
            for value in frozen_mapping.values()
        ):
            raise RequestFailure("mapping rejected")
        present = tuple(frozen_mapping.values())
        if (
            len(present) != len(set(present))
            or (self.decoder == "uart" and not present)
            or (
                self.decoder == "spi"
                and ("clk" not in frozen_mapping or not {"miso", "mosi"} & set(frozen_mapping))
            )
            or (self.decoder == "i2c" and set(frozen_mapping) != {"scl", "sda"})
        ):
            raise RequestFailure("mapping rejected")
        if any(sample >> len(self.channel_ids) for sample in self.samples):
            raise RequestFailure("capture rejected")
        object.__setattr__(self, "mapping", frozen_mapping)
        object.__setattr__(self, "options", materialize_options(self.decoder, self.options))

    @property
    def channel_positions(self) -> Mapping[str, int]:
        return MappingProxyType(
            {key: self.channel_ids.index(value) for key, value in self.mapping.items()}
        )
