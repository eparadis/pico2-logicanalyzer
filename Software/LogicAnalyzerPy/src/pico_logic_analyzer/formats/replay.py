from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path
from typing import Any, cast

import numpy as np
from numpy.typing import NDArray

from pico_logic_analyzer.model.capture import (
    CaptureConfig,
    CaptureResult,
    DeviceInfo,
    ProtocolError,
    ValidationError,
)

_NAMES = {"samples.npy", "metadata.npy"}
_V2_BUFFER_BYTES = 384 * 1024
_SCHEMA1_SAMPLE_LIMIT = 16_777_216


def _validate_npy_header(archive: zipfile.ZipFile, name: str) -> None:
    """Reject hostile dtype/shape declarations before NumPy materializes data."""
    try:
        with archive.open(name) as member:
            version = np.lib.format.read_magic(member)  # type: ignore[no-untyped-call]
            reader = {
                (1, 0): np.lib.format.read_array_header_1_0,
                (2, 0): np.lib.format.read_array_header_2_0,
            }.get(version)
            if reader is None:
                raise ValueError("unsupported NPY version")
            shape, _, dtype = reader(member)  # type: ignore[no-untyped-call]
    except (OSError, ValueError, EOFError) as exc:
        raise ProtocolError("invalid replay NPY header") from exc
    allowed = (np.dtype("uint8"), np.dtype("uint16"), np.dtype("uint32"))
    if (
        len(shape) != 1
        or (name == "samples.npy" and dtype not in allowed)
        or (name == "metadata.npy" and dtype != np.dtype("uint8"))
    ):
        raise ProtocolError("invalid replay NPY dtype or rank")
    count = shape[0]
    if (
        not isinstance(count, int)
        or count < 0
        or (name == "samples.npy" and count > _SCHEMA1_SAMPLE_LIMIT)
    ):
        raise ProtocolError("invalid replay NPY count")


def load_replay(path: Path) -> tuple[NDArray[Any], dict[str, object]]:
    try:
        return load_replay_bytes(path.read_bytes())
    except OSError as exc:
        raise ProtocolError("cannot read replay archive") from exc


def load_replay_bytes(data: bytes) -> tuple[NDArray[Any], dict[str, object]]:
    """Load a bounded inert replay from request bytes without a temporary file."""
    archive_size = len(data)
    if archive_size > 2 * 1024 * 1024:
        raise ProtocolError("replay archive too large")
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except (OSError, zipfile.BadZipFile) as exc:
        raise ProtocolError("invalid replay archive") from exc
    with archive:
        infos = archive.infolist()
        if (
            len(infos) != 2
            or {item.filename for item in infos} != _NAMES
            or any("/" in item.filename or item.flag_bits & 1 for item in infos)
        ):
            raise ProtocolError("invalid replay members")
        limits = {"samples.npy": _V2_BUFFER_BYTES + 1024, "metadata.npy": 64 * 1024}
        if any(
            item.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)
            or item.file_size > limits[item.filename]
            for item in infos
        ):
            raise ProtocolError("invalid replay member size or compression")
        _validate_npy_header(archive, "samples.npy")
        _validate_npy_header(archive, "metadata.npy")
        try:
            with np.load(io.BytesIO(data), allow_pickle=False) as payload:
                samples = payload["samples"]
                metadata_bytes = payload["metadata"]
        except (ValueError, TypeError, KeyError, OSError) as exc:
            raise ProtocolError("invalid replay NumPy members") from exc
    if (
        samples.dtype not in (np.dtype("uint8"), np.dtype("uint16"), np.dtype("uint32"))
        or samples.ndim != 1
        or samples.nbytes > _SCHEMA1_SAMPLE_LIMIT
    ):
        raise ProtocolError("invalid replay samples")
    if metadata_bytes.dtype != np.dtype("uint8") or metadata_bytes.ndim != 1:
        raise ProtocolError("invalid replay metadata")
    try:
        metadata = json.loads(metadata_bytes.tobytes().decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ProtocolError("invalid replay JSON") from exc
    if not isinstance(metadata, dict) or (
        json.dumps(metadata, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode(
            "utf-8"
        )
        != metadata_bytes.tobytes()
    ):
        raise ProtocolError("replay metadata is not canonical JSON")
    if metadata.get("schema_version") == 2:
        return _load_schema2(samples, metadata)
    required = {
        "schema_version",
        "provisional",
        "sample_rate_hz",
        "requested_count",
        "actual_count",
        "pre_trigger_samples",
        "post_trigger_samples",
        "trigger_index",
        "trigger_channel",
        "trigger_edge",
        "channel_ids",
        "channel_labels",
        "channel_mapping",
        "device",
    }
    if (
        not isinstance(metadata, dict)
        or set(metadata) != required
        or metadata.get("schema_version") != 1
        or metadata.get("provisional") is not True
    ):
        raise ProtocolError("unsupported replay schema")
    integers = (
        "sample_rate_hz",
        "requested_count",
        "actual_count",
        "pre_trigger_samples",
        "post_trigger_samples",
        "trigger_index",
        "trigger_channel",
    )
    if any(
        not isinstance(metadata[key], int) or isinstance(metadata[key], bool) for key in integers
    ):
        raise ProtocolError("invalid replay numeric metadata")
    if (
        metadata["sample_rate_hz"] <= 0
        or metadata["post_trigger_samples"] < 1
        or not 0 <= metadata["trigger_channel"] <= 7
    ):
        raise ProtocolError("invalid replay capture metadata")
    if (
        metadata["pre_trigger_samples"] < 0
        or not 0 <= metadata["trigger_index"] < metadata["actual_count"]
    ):
        raise ProtocolError("invalid replay trigger index")
    if any(metadata[key] > 0xFFFFFFFF for key in integers):
        raise ProtocolError("replay numeric field exceeds uint32")
    if metadata["trigger_edge"] not in ("rising", "falling") or metadata["channel_ids"] != list(
        range(8)
    ):
        raise ProtocolError("invalid replay trigger or channel metadata")
    if not all(
        isinstance(metadata[key], list)
        and len(metadata[key]) == 8
        and all(isinstance(value, str) and len(value) <= 128 for value in metadata[key])
        for key in ("channel_labels", "channel_mapping")
    ):
        raise ProtocolError("invalid replay channel metadata")
    if not isinstance(metadata["device"], dict) or set(metadata["device"]) != {
        "identity",
        "capabilities",
    }:
        raise ProtocolError("invalid replay device metadata")
    try:
        capabilities = metadata["device"]["capabilities"]
        if not isinstance(capabilities, dict) or set(capabilities) != {
            "max_frequency_hz",
            "blast_frequency_hz",
            "buffer_size",
            "channel_count",
        }:
            raise ValidationError("capabilities must be an object")
        device = DeviceInfo(
            metadata["device"]["identity"],
            capabilities["max_frequency_hz"],
            capabilities["blast_frequency_hz"],
            capabilities["buffer_size"],
            capabilities["channel_count"],
        )
    except (KeyError, TypeError, ValidationError) as exc:
        raise ProtocolError("invalid replay device capabilities") from exc
    if (
        metadata["sample_rate_hz"] > device.max_frequency_hz
        or metadata["requested_count"] > device.buffer_size
    ):
        raise ProtocolError("replay capture exceeds device capabilities")
    if (
        metadata["actual_count"] != len(samples)
        or metadata["requested_count"] != len(samples)
        or metadata["trigger_index"] != metadata["pre_trigger_samples"]
        or metadata["requested_count"]
        != metadata["pre_trigger_samples"] + metadata["post_trigger_samples"]
    ):
        raise ProtocolError("inconsistent replay counts")
    return samples, metadata


def import_replay_bytes(data: bytes) -> CaptureResult:
    """Turn a validated schema-1/schema-2 container into the shared capture model."""
    samples, metadata = load_replay_bytes(data)
    try:
        values = cast(dict[str, Any], metadata)
        config = CaptureConfig(
            values["sample_rate_hz"],
            values["pre_trigger_samples"],
            values["post_trigger_samples"],
            values["trigger_channel"],
            values["trigger_edge"],
            tuple(values["channel_ids"]),
        )
        capabilities = values["device"]["capabilities"]
        device = DeviceInfo(
            values["device"]["identity"],
            capabilities["max_frequency_hz"],
            capabilities["blast_frequency_hz"],
            capabilities["buffer_size"],
            capabilities["channel_count"],
        )
        return CaptureResult(
            config,
            samples,
            device,
            tuple(values["channel_labels"]),
            tuple(values["channel_mapping"]),
        )
    except (KeyError, TypeError, ValidationError) as exc:
        raise ProtocolError("invalid replay capture") from exc


def _load_schema2(
    samples: NDArray[Any], metadata: dict[str, object]
) -> tuple[NDArray[Any], dict[str, object]]:
    required = {
        "schema_version",
        "sample_dtype",
        "firmware_mode",
        "sample_rate_hz",
        "requested_count",
        "actual_count",
        "pre_trigger_samples",
        "post_trigger_samples",
        "trigger_index",
        "trigger_channel",
        "trigger_edge",
        "channel_ids",
        "channel_labels",
        "channel_mapping",
        "device",
    }
    if set(metadata) != required:
        raise ProtocolError("invalid schema 2 metadata fields")
    try:
        values = cast(dict[str, Any], metadata)
        channel_ids = tuple(values["channel_ids"])
        config = CaptureConfig(
            values["sample_rate_hz"],
            values["pre_trigger_samples"],
            values["post_trigger_samples"],
            values["trigger_channel"],
            values["trigger_edge"],
            channel_ids,
        )
        device_data = values["device"]
        capabilities = device_data["capabilities"]
        device = DeviceInfo(
            device_data["identity"],
            capabilities["max_frequency_hz"],
            capabilities["blast_frequency_hz"],
            capabilities["buffer_size"],
            capabilities["channel_count"],
        )
    except (KeyError, TypeError, ValidationError) as exc:
        raise ProtocolError("invalid schema 2 metadata") from exc
    if metadata["firmware_mode"] != config.firmware_mode or metadata["sample_dtype"] != str(
        config.sample_dtype
    ):
        raise ProtocolError("inconsistent schema 2 word mode")
    if samples.nbytes > _V2_BUFFER_BYTES:
        raise ProtocolError("schema 2 samples exceed V2 byte buffer")
    if (
        samples.dtype != config.sample_dtype
        or metadata["requested_count"] != config.requested_count
        or metadata["actual_count"] != len(samples)
        or metadata["trigger_index"] != config.pre_trigger_samples
    ):
        raise ProtocolError("inconsistent schema 2 counts")
    try:
        from pico_logic_analyzer.model.capture import CaptureResult

        CaptureResult(
            config,
            samples,
            device,
            tuple(values["channel_labels"]),
            tuple(values["channel_mapping"]),
        )
    except (TypeError, ValidationError) as exc:
        raise ProtocolError("invalid schema 2 capture") from exc
    return samples, metadata
