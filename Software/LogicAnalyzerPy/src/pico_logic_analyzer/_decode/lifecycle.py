"""Private lifecycle projection over an already pinned frozen descriptor."""

from __future__ import annotations

from types import MappingProxyType
from typing import Protocol, cast

from .compat import ApiV3Host, EndOfInput, ShimAdapter
from .loader import FrozenDescriptor
from .model import (
    AnnotationDeclaration,
    AnnotationRowDeclaration,
    BinaryDeclaration,
    CaptureIdentity,
    Declaration,
    DecodeRequest,
    DecodeResult,
    MetadataDeclaration,
    ResultFailure,
)


class LifecycleDecoder(Protocol):
    channels: tuple[tuple[str, str], ...]
    optional_channels: tuple[tuple[str, str], ...]
    annotations: tuple[tuple[str, str], ...]
    annotation_rows: tuple[tuple[str, str, tuple[int, ...]], ...]
    binary: tuple[tuple[str, str], ...]
    cObj: ShimAdapter
    options: MappingProxyType[str, object]

    def start(self) -> None: ...
    def metadata(self, key: int, value: int) -> None: ...
    def decode(self) -> None: ...


def run_lifecycle(descriptor: FrozenDescriptor, request: DecodeRequest) -> DecodeResult:
    """Run the closed lifecycle; only EndOfInput is a normal decode completion."""
    if descriptor.identity.decoder != request.decoder:
        raise ResultFailure("lifecycle identity rejected")
    channels = _channel_names(descriptor.decoder_class)
    host = ApiV3Host(
        channels,
        request.mapping,
        request.channel_ids,
        request.samples,
        request.samplerate,
        request.trigger_index,
        request.options,
        descriptor.spi_data_type,
    )
    try:
        decoder = cast(LifecycleDecoder, descriptor.decoder_class())
        adapter = ShimAdapter(host)
        decoder.cObj = adapter
        adapter.bind_decoder(decoder)
        decoder.options = MappingProxyType(dict(request.options))
        decoder.start()
        decoder.metadata(0, request.samplerate)
        host.metadata(0, request.samplerate)
        decoder.decode()
    except EndOfInput:
        pass
    except ResultFailure as error:
        raise ResultFailure(f"lifecycle decoder rejected:{error}") from None
    except BaseException as error:
        raise ResultFailure(
            f"lifecycle decoder rejected:{type(error).__name__}:{str(error)}"
        ) from None
    try:
        declarations = _declarations(decoder, host)
    except ResultFailure as error:
        raise ResultFailure(f"lifecycle-declarations:{error}") from None
    try:
        return DecodeResult(
        request.decoder,
        descriptor.identity.file_set_sha256,
        request.samplerate,
        _capture(request),
        request.mapping,
        request.options,
        declarations,
            host.records,
        )
    except ResultFailure as error:
        raise ResultFailure(f"lifecycle-result:{error}") from None


def _channel_names(decoder_class: type[object]) -> tuple[str, ...]:
    required = getattr(decoder_class, "channels", ())
    optional = getattr(decoder_class, "optional_channels", ())
    if type(required) not in {tuple, list} or type(optional) is not tuple:
        raise ResultFailure("lifecycle declaration rejected")
    names = tuple(_channel_name(item) for item in (*required, *optional))
    if not names or any(type(name) is not str for name in names):
        raise ResultFailure("lifecycle declaration rejected")
    return names


def _channel_name(value: object) -> str:
    if isinstance(value, dict):
        identifier = value.get("id")
        if type(identifier) is str:
            return identifier
    if type(value) is tuple and value and type(value[0]) is str:
        return value[0]
    raise ResultFailure("lifecycle declaration rejected")


def _capture(request: DecodeRequest) -> CaptureIdentity:
    return CaptureIdentity(len(request.samples), request.trigger_index, request.channel_ids)


def _declarations(decoder: LifecycleDecoder, host: ApiV3Host) -> tuple[Declaration, ...]:
    annotations = tuple(
        AnnotationDeclaration(identifier, index, description)
        for index, (identifier, description) in enumerate(getattr(decoder, "annotations", ()))
    )
    rows = tuple(
        AnnotationRowDeclaration(identifier, index, description, tuple(indices))
        for index, (identifier, description, indices) in enumerate(
            getattr(decoder, "annotation_rows", ())
        )
    )
    binary = tuple(
        BinaryDeclaration(identifier, index, description)
        for index, (identifier, description) in enumerate(getattr(decoder, "binary", ()))
    )
    metadata = tuple(
        MetadataDeclaration(output_id, "integer", meta[1], meta[2])
        for output_id, registration in enumerate(host.registrations)
        if registration.output_type == 4 and type(meta := registration.meta) is tuple
    )
    return (*annotations, *rows, *binary, *metadata)
