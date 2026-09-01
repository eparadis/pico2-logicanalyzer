"""Immutable public interface for the bounded native protocol decoders."""

from __future__ import annotations

import base64
import json
import math
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal, cast

from pico_logic_analyzer._decode.host import decode_private as _decode_private
from pico_logic_analyzer._decode.model import (
    HARD_LIMITS,
    DecodeRequest,
    HostFailure,
    RequestFailure,
)
from pico_logic_analyzer._decode.model import (
    AnnotationDeclaration as _PrivateAnnotationDeclaration,
)
from pico_logic_analyzer._decode.model import (
    AnnotationRowDeclaration as _PrivateAnnotationRowDeclaration,
)
from pico_logic_analyzer._decode.model import (
    AnnotationValue as _PrivateAnnotationValue,
)
from pico_logic_analyzer._decode.model import (
    BinaryDeclaration as _PrivateBinaryDeclaration,
)
from pico_logic_analyzer._decode.model import (
    BinaryValue as _PrivateBinaryValue,
)
from pico_logic_analyzer._decode.model import (
    DecodeResult as _PrivateDecodeResult,
)
from pico_logic_analyzer._decode.model import (
    MetadataDeclaration as _PrivateMetadataDeclaration,
)
from pico_logic_analyzer._decode.model import (
    MetadataValue as _PrivateMetadataValue,
)
from pico_logic_analyzer._decode.model import (
    SpiData as _PrivateSpiData,
)
from pico_logic_analyzer.model import CaptureResult

type OptionScalar = int | float | str

_FAILURE_CODES = frozenset(
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
_MAX_STABLE_DIAGNOSTIC_BYTES = max(
    len(f"decoder failed: {code}".encode()) for code in _FAILURE_CODES
)


@dataclass(frozen=True, slots=True)
class DecoderIdentity:
    id: str
    file_set_sha256: str

    def __post_init__(self) -> None:
        if (
            self.id not in {"uart", "spi", "i2c"}
            or type(self.file_set_sha256) is not str
            or len(self.file_set_sha256) != 64
            or any(character not in "0123456789abcdef" for character in self.file_set_sha256)
        ):
            raise ValueError("invalid decoder identity")


@dataclass(frozen=True, slots=True)
class DecodeCaptureIdentity:
    sample_count: int
    trigger_index: int

    def __post_init__(self) -> None:
        if (
            type(self.sample_count) is not int
            or self.sample_count <= 0
            or type(self.trigger_index) is not int
            or not 0 <= self.trigger_index < self.sample_count
        ):
            raise ValueError("invalid capture identity")


@dataclass(frozen=True, slots=True)
class AnnotationDeclaration:
    index: int
    id: str
    description: str


@dataclass(frozen=True, slots=True)
class AnnotationRowDeclaration:
    index: int
    id: str
    description: str
    annotation_indices: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class BinaryDeclaration:
    index: int
    id: str
    description: str


@dataclass(frozen=True, slots=True)
class MetadataDeclaration:
    output_id: int
    value_type: Literal["integer"]
    name: str
    description: str


@dataclass(frozen=True, slots=True)
class DecodeDeclarations:
    annotations: tuple[AnnotationDeclaration, ...]
    annotation_rows: tuple[AnnotationRowDeclaration, ...]
    binary: tuple[BinaryDeclaration, ...]
    metadata: tuple[MetadataDeclaration, ...]


@dataclass(frozen=True, slots=True)
class RationalTime:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        if type(self.numerator) is not int or type(self.denominator) is not int:
            raise ValueError("invalid rational time")
        if self.denominator <= 0:
            raise ValueError("invalid rational time")


@dataclass(frozen=True, slots=True)
class RecordTime:
    absolute: RationalTime
    trigger_relative: RationalTime


@dataclass(frozen=True, slots=True)
class NullValue:
    tag: Literal["null"] = "null"

    def __post_init__(self) -> None:
        if self.tag != "null":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class BoolValue:
    value: bool
    tag: Literal["bool"] = "bool"

    def __post_init__(self) -> None:
        if type(self.value) is not bool or self.tag != "bool":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class IntegerValue:
    value: int
    tag: Literal["integer"] = "integer"

    def __post_init__(self) -> None:
        if type(self.value) is not int or self.tag != "integer":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class FloatValue:
    value: float
    tag: Literal["float"] = "float"

    def __post_init__(self) -> None:
        if type(self.value) is not float or not math.isfinite(self.value) or self.tag != "float":
            raise ValueError("non-finite Python value")


@dataclass(frozen=True, slots=True)
class StringValue:
    value: str
    tag: Literal["string"] = "string"

    def __post_init__(self) -> None:
        if type(self.value) is not str or self.tag != "string":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class BytesValue:
    value: bytes
    tag: Literal["bytes"] = "bytes"

    def __post_init__(self) -> None:
        if type(self.value) is not bytes or self.tag != "bytes":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class ListValue:
    value: tuple[PythonValue, ...]
    tag: Literal["list"] = "list"

    def __post_init__(self) -> None:
        if type(self.value) is not tuple or self.tag != "list":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class TupleValue:
    value: tuple[PythonValue, ...]
    tag: Literal["tuple"] = "tuple"

    def __post_init__(self) -> None:
        if type(self.value) is not tuple or self.tag != "tuple":
            raise ValueError("invalid Python value")


@dataclass(frozen=True, slots=True)
class SpiDataValue:
    ss: int
    es: int
    val: int
    tag: Literal["spi-data"] = "spi-data"

    def __post_init__(self) -> None:
        if (
            any(type(value) is not int or value < 0 for value in (self.ss, self.es, self.val))
            or self.tag != "spi-data"
        ):
            raise ValueError("invalid Python value")


type PythonValue = (
    NullValue
    | BoolValue
    | IntegerValue
    | FloatValue
    | StringValue
    | BytesValue
    | ListValue
    | TupleValue
    | SpiDataValue
)


type _AnnotationValue = Mapping[str, int | tuple[str, ...]]
type _BinaryValue = Mapping[str, int | str]
type _MetadataValue = Mapping[str, int | Literal["integer"]]


@dataclass(frozen=True, slots=True)
class AnnotationRecord:
    emission_index: int
    output_id: int
    start_sample: int
    end_sample: int
    start_time: RecordTime
    end_time: RecordTime
    value: _AnnotationValue
    kind: Literal["annotation"] = "annotation"

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _annotation_value(self.value))


@dataclass(frozen=True, slots=True)
class PythonRecord:
    emission_index: int
    output_id: int
    start_sample: int
    end_sample: int
    start_time: RecordTime
    end_time: RecordTime
    value: PythonValue
    kind: Literal["python"] = "python"


@dataclass(frozen=True, slots=True)
class BinaryRecord:
    emission_index: int
    output_id: int
    start_sample: int
    end_sample: int
    start_time: RecordTime
    end_time: RecordTime
    value: _BinaryValue
    kind: Literal["binary"] = "binary"

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _binary_value(self.value))


@dataclass(frozen=True, slots=True)
class MetadataRecord:
    emission_index: int
    output_id: int
    start_sample: int
    end_sample: int
    start_time: RecordTime
    end_time: RecordTime
    value: _MetadataValue
    kind: Literal["metadata"] = "metadata"

    def __post_init__(self) -> None:
        object.__setattr__(self, "value", _metadata_value(self.value))


def _annotation_value(value: Mapping[str, object]) -> _AnnotationValue:
    if not isinstance(value, Mapping) or set(value) != {"class_index", "texts"}:
        raise ValueError("invalid annotation value")
    class_index = value["class_index"]
    texts = value["texts"]
    if (
        type(class_index) is not int
        or class_index < 0
        or type(texts) is not tuple
        or not texts
        or any(type(text) is not str for text in texts)
    ):
        raise ValueError("invalid annotation value")
    result: dict[str, int | tuple[str, ...]] = {
        "class_index": class_index,
        "texts": texts,
    }
    return MappingProxyType(result)


def _binary_value(value: Mapping[str, object]) -> _BinaryValue:
    if not isinstance(value, Mapping) or set(value) != {"class_index", "data_base64"}:
        raise ValueError("invalid binary value")
    class_index = value["class_index"]
    data_base64 = value["data_base64"]
    if type(class_index) is not int or class_index < 0 or type(data_base64) is not str:
        raise ValueError("invalid binary value")
    try:
        decoded = base64.b64decode(data_base64, validate=True)
    except (ValueError, TypeError):
        raise ValueError("invalid binary value") from None
    if base64.b64encode(decoded).decode("ascii") != data_base64:
        raise ValueError("invalid binary value")
    result: dict[str, int | str] = {
        "class_index": class_index,
        "data_base64": data_base64,
    }
    return MappingProxyType(result)


def _metadata_value(value: Mapping[str, object]) -> _MetadataValue:
    if not isinstance(value, Mapping) or set(value) != {"value_type", "value"}:
        raise ValueError("invalid metadata value")
    value_type = value["value_type"]
    integer = value["value"]
    if value_type != "integer" or type(integer) is not int:
        raise ValueError("invalid metadata value")
    result: dict[str, int | Literal["integer"]] = {
        "value_type": "integer",
        "value": integer,
    }
    return MappingProxyType(result)


type DecodeRecord = AnnotationRecord | PythonRecord | BinaryRecord | MetadataRecord


@dataclass(frozen=True, slots=True)
class DecodeResult:
    decoder: DecoderIdentity
    samplerate_hz: int
    channels: tuple[tuple[str, int], ...]
    options: tuple[tuple[str, OptionScalar], ...]
    capture: DecodeCaptureIdentity
    declarations: DecodeDeclarations
    records: tuple[DecodeRecord, ...]
    schema: Literal["pico-logic-analyzer.decode-result/v1"] = (
        "pico-logic-analyzer.decode-result/v1"
    )

    def __post_init__(self) -> None:
        channel_names = tuple(name for name, _ in self.channels)
        physical_channels = tuple(physical for _, physical in self.channels)
        option_names = tuple(name for name, _ in self.options)
        if (
            self.schema != "pico-logic-analyzer.decode-result/v1"
            or type(self.samplerate_hz) is not int
            or self.samplerate_hz <= 0
            or type(self.channels) is not tuple
            or type(self.options) is not tuple
            or type(self.records) is not tuple
            or len(set(channel_names)) != len(channel_names)
            or len(set(physical_channels)) != len(physical_channels)
            or any(type(name) is not str or type(value) is not int for name, value in self.channels)
            or option_names != tuple(sorted(option_names))
            or len(set(option_names)) != len(option_names)
            or any(
                type(name) is not str
                or type(value) not in {int, float, str}
                or (type(value) is float and not math.isfinite(value))
                for name, value in self.options
            )
            or tuple(record.emission_index for record in self.records)
            != tuple(range(len(self.records)))
        ):
            raise ValueError("invalid decode result")

    def to_dict(self) -> dict[str, object]:
        return {
            "schema": self.schema,
            "decoder": {
                "id": self.decoder.id,
                "file_set_sha256": self.decoder.file_set_sha256,
            },
            "samplerate_hz": self.samplerate_hz,
            "channels": [
                {"decoder_channel": name, "physical_channel": physical}
                for name, physical in self.channels
            ],
            "options": dict(self.options),
            "capture": {
                "sample_count": self.capture.sample_count,
                "trigger_index": self.capture.trigger_index,
            },
            "declarations": _declarations_dict(self.declarations),
            "records": [_record_dict(record) for record in self.records],
        }

    def json_bytes(self) -> bytes:
        return canonical_json(self)


@dataclass(frozen=True, slots=True)
class DecodeError(RuntimeError):
    """Stable path- and traceback-free version-1 decoder failure."""

    code: str
    message: str
    schema: Literal["pico-logic-analyzer.decode-error/v1"] = "pico-logic-analyzer.decode-error/v1"

    def __post_init__(self) -> None:
        if (
            self.schema != "pico-logic-analyzer.decode-error/v1"
            or self.code not in _FAILURE_CODES
            or type(self.message) is not str
            or not self.message
            or len(self.message.encode("utf-8")) > HARD_LIMITS["diagnostic_bytes"]
            or "/" in self.message
            or "\\" in self.message
            or "traceback" in self.message.lower()
        ):
            raise ValueError("invalid decode failure")

    def __str__(self) -> str:
        return self.message

    def to_dict(self) -> dict[str, str]:
        return {"schema": self.schema, "code": self.code, "message": self.message}


def decode_capture(
    capture: CaptureResult,
    decoder_id: str,
    channels: Mapping[str, int],
    options: Mapping[str, object],
    limits: Mapping[str, int] | None = None,
) -> DecodeResult:
    """Synchronously decode one validated inert capture through the sole private host."""
    effective_limits = _validated_limits(limits)
    if type(capture) is not CaptureResult:
        raise ValueError("capture must be a validated CaptureResult")
    try:
        request = DecodeRequest(
            decoder_id,
            capture.config.sample_rate_hz,
            capture.config.channel_ids,
            _canonical_mapping(decoder_id, channels),
            tuple(int(word) for word in capture.samples),
            capture.trigger_index,
            options,
        )
    except RequestFailure as exc:
        raise ValueError(str(exc)) from None
    if len(request.samples) > effective_limits["input_samples"]:
        raise ValueError("capture exceeds caller limits")
    wordsize = request.options.get("wordsize")
    if (
        request.decoder == "spi"
        and type(wordsize) is int
        and wordsize > effective_limits["spi_max_word_size_bits"]
    ):
        raise ValueError("SPI word size exceeds caller limits")
    try:
        private = _decode_private(request, limits=effective_limits)
    except (HostFailure, OSError) as exc:
        code = str(exc)
        if isinstance(exc, OSError):
            code = "process-exit"
        if code not in _FAILURE_CODES:
            code = "snapshot" if "identity" in code else "ipc"
        raise DecodeError(code, f"decoder failed: {code}") from None
    return _public_result(private)


def canonical_json(result: DecodeResult) -> bytes:
    return json.dumps(
        result.to_dict(),
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


def _validated_limits(limits: Mapping[str, int] | None) -> dict[str, int]:
    if limits is None:
        return dict(HARD_LIMITS)
    if not isinstance(limits, Mapping) or any(type(key) is not str for key in limits):
        raise ValueError("limits must be a mapping")
    if set(limits) - set(HARD_LIMITS):
        raise ValueError("limits contain an unknown ceiling")
    effective = dict(HARD_LIMITS)
    for key, value in limits.items():
        if type(value) is not int or value <= 0 or value > HARD_LIMITS[key]:
            raise ValueError("limits may only tighten approved ceilings")
        effective[key] = value
    if effective["diagnostic_bytes"] < _MAX_STABLE_DIAGNOSTIC_BYTES:
        raise ValueError("diagnostic limit cannot encode stable failures")
    return effective


def _canonical_mapping(decoder: str, channels: Mapping[str, int]) -> Mapping[str, int]:
    if not isinstance(channels, Mapping):
        return channels
    order = {
        "uart": ("rx", "tx"),
        "spi": ("clk", "miso", "mosi", "cs"),
        "i2c": ("scl", "sda"),
    }.get(decoder, ())
    result = {name: channels[name] for name in order if name in channels}
    result.update((name, value) for name, value in channels.items() if name not in result)
    return result


def _public_result(value: _PrivateDecodeResult) -> DecodeResult:
    annotations: list[AnnotationDeclaration] = []
    rows: list[AnnotationRowDeclaration] = []
    binary: list[BinaryDeclaration] = []
    metadata: list[MetadataDeclaration] = []
    for item in value.declarations:
        if type(item) is _PrivateAnnotationDeclaration:
            annotations.append(AnnotationDeclaration(item.index, item.identifier, item.description))
        elif type(item) is _PrivateAnnotationRowDeclaration:
            rows.append(
                AnnotationRowDeclaration(
                    item.index, item.identifier, item.description, item.annotation_indices
                )
            )
        elif type(item) is _PrivateBinaryDeclaration:
            binary.append(BinaryDeclaration(item.index, item.identifier, item.description))
        elif type(item) is _PrivateMetadataDeclaration:
            metadata.append(
                MetadataDeclaration(item.output_id, item.value_type, item.name, item.description)
            )
        else:
            raise DecodeError("ipc", "decoder failed: ipc")
    declarations = DecodeDeclarations(
        tuple(annotations), tuple(rows), tuple(binary), tuple(metadata)
    )
    records = tuple(_public_record(item) for item in value.records)
    return DecodeResult(
        DecoderIdentity(value.decoder, value.file_set_sha256),
        value.samplerate_hz,
        tuple((name, physical) for name, physical in value.channels.items()),
        tuple((name, scalar) for name, scalar in sorted(value.options.items())),  # type: ignore[misc]
        DecodeCaptureIdentity(value.capture.sample_count, value.capture.trigger_index),
        declarations,
        records,
    )


def _public_record(value: object) -> DecodeRecord:
    from pico_logic_analyzer._decode.model import DecodeRecord as PrivateRecord

    if type(value) is not PrivateRecord:
        raise DecodeError("ipc", "decoder failed: ipc")
    start = _public_time(value.start_time)
    end = _public_time(value.end_time)
    common = (
        value.emission_index,
        value.output_id,
        value.start_sample,
        value.end_sample,
        start,
        end,
    )
    if value.kind == "annotation" and type(value.value) is _PrivateAnnotationValue:
        return AnnotationRecord(
            *common,
            {"class_index": value.value.class_index, "texts": value.value.texts},
        )
    if value.kind == "python":
        return PythonRecord(*common, _python_value(value.value))
    if value.kind == "binary" and type(value.value) is _PrivateBinaryValue:
        return BinaryRecord(
            *common,
            {
                "class_index": value.value.class_index,
                "data_base64": base64.b64encode(value.value.data).decode("ascii"),
            },
        )
    if value.kind == "metadata" and type(value.value) is _PrivateMetadataValue:
        return MetadataRecord(
            *common,
            {"value_type": value.value.value_type, "value": value.value.value},
        )
    raise DecodeError("ipc", "decoder failed: ipc")


def _public_time(value: object) -> RecordTime:
    absolute = value.absolute  # type: ignore[attr-defined]
    relative = value.trigger_relative  # type: ignore[attr-defined]
    return RecordTime(
        RationalTime(absolute.numerator, absolute.denominator),
        RationalTime(relative.numerator, relative.denominator),
    )


def _python_value(value: object) -> PythonValue:
    if value is None:
        return NullValue()
    if type(value) is bool:
        return BoolValue(value)
    if type(value) is int:
        return IntegerValue(value)
    if type(value) is float:
        return FloatValue(value)
    if type(value) is str:
        return StringValue(value)
    if type(value) is bytes:
        return BytesValue(value)
    if type(value) is list:
        return ListValue(tuple(_python_value(item) for item in value))
    if type(value) is tuple:
        return TupleValue(tuple(_python_value(item) for item in value))
    if type(value) is _PrivateSpiData:
        return SpiDataValue(value.ss, value.es, value.value)
    raise DecodeError("ipc", "decoder failed: ipc")


def _time_dict(value: RecordTime) -> dict[str, object]:
    return {
        "absolute": {
            "numerator": value.absolute.numerator,
            "denominator": value.absolute.denominator,
        },
        "trigger_relative": {
            "numerator": value.trigger_relative.numerator,
            "denominator": value.trigger_relative.denominator,
        },
    }


def _python_dict(value: PythonValue) -> dict[str, object]:
    if type(value) is NullValue:
        return {"tag": "null"}
    if type(value) is BytesValue:
        return {"tag": "bytes", "value": base64.b64encode(value.value).decode("ascii")}
    if isinstance(value, ListValue | TupleValue):
        return {"tag": value.tag, "value": [_python_dict(item) for item in value.value]}
    if type(value) is SpiDataValue:
        return {"tag": "spi-data", "ss": value.ss, "es": value.es, "val": value.val}
    if isinstance(value, BoolValue | IntegerValue | FloatValue | StringValue):
        return {"tag": value.tag, "value": value.value}
    raise DecodeError("ipc", "decoder failed: ipc")


def _record_dict(record: DecodeRecord) -> dict[str, object]:
    value: dict[str, object]
    if type(record) is AnnotationRecord:
        value = dict(record.value)
    elif type(record) is PythonRecord:
        value = _python_dict(record.value)
    elif type(record) is BinaryRecord:
        value = dict(record.value)
    else:
        metadata = cast(MetadataRecord, record)
        value = dict(metadata.value)
    return {
        "emission_index": record.emission_index,
        "output_id": record.output_id,
        "kind": record.kind,
        "start_sample": record.start_sample,
        "end_sample": record.end_sample,
        "start_time": _time_dict(record.start_time),
        "end_time": _time_dict(record.end_time),
        "value": value,
    }


def _declarations_dict(value: DecodeDeclarations) -> dict[str, object]:
    return {
        "annotations": [
            {"index": item.index, "id": item.id, "description": item.description}
            for item in value.annotations
        ],
        "annotation_rows": [
            {
                "index": item.index,
                "id": item.id,
                "description": item.description,
                "annotation_indices": list(item.annotation_indices),
            }
            for item in value.annotation_rows
        ],
        "binary": [
            {"index": item.index, "id": item.id, "description": item.description}
            for item in value.binary
        ],
        "metadata": [
            {
                "output_id": item.output_id,
                "value_type": item.value_type,
                "name": item.name,
                "description": item.description,
            }
            for item in value.metadata
        ],
    }


__all__ = (
    "AnnotationDeclaration",
    "AnnotationRecord",
    "AnnotationRowDeclaration",
    "BinaryDeclaration",
    "BinaryRecord",
    "BoolValue",
    "BytesValue",
    "DecodeCaptureIdentity",
    "DecodeDeclarations",
    "DecodeError",
    "DecodeRecord",
    "DecodeResult",
    "DecoderIdentity",
    "FloatValue",
    "IntegerValue",
    "ListValue",
    "MetadataDeclaration",
    "MetadataRecord",
    "NullValue",
    "PythonRecord",
    "PythonValue",
    "RationalTime",
    "RecordTime",
    "SpiDataValue",
    "StringValue",
    "TupleValue",
    "canonical_json",
    "decode_capture",
)
