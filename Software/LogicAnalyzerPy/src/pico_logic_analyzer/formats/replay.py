from __future__ import annotations

import json
import zipfile
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from pico_logic_analyzer.model.capture import DeviceInfo, ProtocolError, ValidationError

_NAMES = {"samples.npy", "metadata.npy"}


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
    if len(shape) != 1 or dtype != np.dtype("uint8"):
        raise ProtocolError("invalid replay NPY dtype or rank")
    count = shape[0]
    if not isinstance(count, int) or count < 0 or (name == "samples.npy" and count > 16_777_216):
        raise ProtocolError("invalid replay NPY count")


def load_replay(path: Path) -> tuple[NDArray[np.uint8], dict[str, object]]:
    try:
        archive_size = path.stat().st_size
    except OSError as exc:
        raise ProtocolError("cannot read replay archive") from exc
    if archive_size > 32 * 1024 * 1024:
        raise ProtocolError("replay archive too large")
    try:
        archive = zipfile.ZipFile(path)
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
        limits = {"samples.npy": 17 * 1024 * 1024, "metadata.npy": 64 * 1024}
        if any(
            item.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED)
            or item.file_size > limits[item.filename]
            for item in infos
        ):
            raise ProtocolError("invalid replay member size or compression")
        _validate_npy_header(archive, "samples.npy")
        _validate_npy_header(archive, "metadata.npy")
        try:
            with np.load(path, allow_pickle=False) as payload:
                samples = payload["samples"]
                metadata_bytes = payload["metadata"]
        except (ValueError, TypeError, KeyError, OSError) as exc:
            raise ProtocolError("invalid replay NumPy members") from exc
    if samples.dtype != np.dtype("uint8") or samples.ndim != 1 or len(samples) > 16_777_216:
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
