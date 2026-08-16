"""Hostile provisional-replay tests built independently in temporary storage."""

from __future__ import annotations

import io
import json
import struct
import zipfile
from pathlib import Path

import numpy as np
import pytest

import pico_logic_analyzer.formats.replay as replay_module
from pico_logic_analyzer.formats import load_replay
from pico_logic_analyzer.model import ProtocolError

_REQUIRED_METADATA: dict[str, object] = {
    "schema_version": 1,
    "provisional": True,
    "sample_rate_hz": 100,
    "requested_count": 3,
    "actual_count": 3,
    "pre_trigger_samples": 2,
    "post_trigger_samples": 1,
    "trigger_index": 2,
    "trigger_channel": 0,
    "trigger_edge": "rising",
    "channel_ids": list(range(8)),
    "channel_labels": [f"D{i}" for i in range(8)],
    "channel_mapping": [f"D{i}" for i in range(8)],
    "device": {
        "identity": "LOGIC_ANALYZER_TEST_BOARD_V6_0",
        "capabilities": {
            "max_frequency_hz": 100,
            "blast_frequency_hz": 100,
            "buffer_size": 131_072,
            "channel_count": 8,
        },
    },
}


def _npy_bytes(array: np.ndarray[object]) -> bytes:
    buffer = io.BytesIO()
    np.save(buffer, array, allow_pickle=True)
    return buffer.getvalue()


def _write_archive(
    path: Path,
    samples: np.ndarray[object],
    metadata: np.ndarray[object],
    compression: int = zipfile.ZIP_DEFLATED,
) -> None:
    with zipfile.ZipFile(path, "w", compression=compression) as archive:
        archive.writestr("samples.npy", _npy_bytes(samples))
        archive.writestr("metadata.npy", _npy_bytes(metadata))


def _metadata_array(metadata: dict[str, object] | None = None) -> np.ndarray[object]:
    payload = _REQUIRED_METADATA if metadata is None else metadata
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return np.frombuffer(encoded, dtype=np.uint8)


def _normal_archive(path: Path) -> None:
    _write_archive(path, np.array([1, 0, 1], dtype=np.uint8), _metadata_array())


def _patch_central_directory_u32(path: Path, member: str, offset: int, value: int) -> None:
    """Change only ZIP central-directory metadata; never allocate the claimed member."""
    contents = bytearray(path.read_bytes())
    position = 0
    while True:
        position = contents.index(b"PK\x01\x02", position)
        name_length = struct.unpack_from("<H", contents, position + 28)[0]
        extra_length = struct.unpack_from("<H", contents, position + 30)[0]
        name = bytes(contents[position + 46 : position + 46 + name_length]).decode()
        if name == member:
            struct.pack_into("<I", contents, position + offset, value)
            path.write_bytes(contents)
            return
        position += 46 + name_length + extra_length


def _oversized_count_npy() -> bytes:
    """A valid uint8 NPY header declaring 16,777,217 values but no payload."""
    buffer = io.BytesIO()
    np.lib.format.write_array_header_1_0(
        buffer,
        {"descr": "|u1", "fortran_order": False, "shape": (16_777_217,)},
    )
    return buffer.getvalue()


def _header_only_npy(descr: str, shape: tuple[int, ...]) -> bytes:
    buffer = io.BytesIO()
    np.lib.format.write_array_header_1_0(
        buffer,
        {"descr": descr, "fortran_order": False, "shape": shape},
    )
    return buffer.getvalue()


def test_replay_control_archive_loads_without_pickle(tmp_path: Path) -> None:
    path = tmp_path / "control.npz"
    _normal_archive(path)
    samples, metadata = load_replay(path)
    assert samples.dtype == np.dtype("uint8")
    assert samples.tolist() == [1, 0, 1]
    assert metadata == _REQUIRED_METADATA


@pytest.mark.parametrize(
    ("samples", "metadata"),
    [
        (np.array([1.0, 0.0, 1.0], dtype=np.float64), _metadata_array()),
        (np.array([[1, 0, 1]], dtype=np.uint8), _metadata_array()),
        (np.array([object()], dtype=object), _metadata_array()),
        (np.array([1, 0, 1], dtype=np.uint8), np.array([[1, 2]], dtype=np.uint8)),
    ],
)
def test_replay_rejects_unsafe_dtype_or_shape(
    tmp_path: Path, samples: np.ndarray[object], metadata: np.ndarray[object]
) -> None:
    path = tmp_path / "bad-dtype-or-shape.npz"
    _write_archive(path, samples, metadata)
    with pytest.raises(ProtocolError):
        load_replay(path)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda metadata: {**metadata, "unknown": True},
        lambda metadata: {key: value for key, value in metadata.items() if key != "device"},
        lambda metadata: {**metadata, "sample_rate_hz": 0},
        lambda metadata: {**metadata, "trigger_channel": 8},
        lambda metadata: {**metadata, "trigger_edge": "sideways"},
        lambda metadata: {**metadata, "channel_ids": list(range(7))},
        lambda metadata: {**metadata, "post_trigger_samples": 0},
        lambda metadata: {**metadata, "actual_count": 2},
    ],
)
def test_replay_rejects_schema_and_semantic_metadata(
    tmp_path: Path, mutate: object
) -> None:
    path = tmp_path / "bad-metadata.npz"
    changed = mutate(dict(_REQUIRED_METADATA))  # type: ignore[operator]
    _write_archive(path, np.array([1, 0, 1], dtype=np.uint8), _metadata_array(changed))
    with pytest.raises(ProtocolError):
        load_replay(path)


@pytest.mark.parametrize(
    "member_names",
    [
        ["samples.npy"],
        ["samples.npy", "metadata.npy", "extra.npy"],
        ["dir/samples.npy", "metadata.npy"],
        ["samples.npy", "samples.npy"],
    ],
)
def test_replay_rejects_missing_extra_path_or_duplicate_members(
    tmp_path: Path, member_names: list[str]
) -> None:
    path = tmp_path / "bad-members.npz"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in member_names:
            array = np.array([1, 0, 1], dtype=np.uint8) if "samples" in name else _metadata_array()
            archive.writestr(name, _npy_bytes(array))
    with pytest.raises(ProtocolError):
        load_replay(path)


def test_replay_rejects_unsupported_zip_compression(tmp_path: Path) -> None:
    path = tmp_path / "bzip2.npz"
    _write_archive(
        path,
        np.array([1, 0, 1], dtype=np.uint8),
        _metadata_array(),
        compression=zipfile.ZIP_BZIP2,
    )
    with pytest.raises(ProtocolError):
        load_replay(path)


def test_replay_rejects_invalid_utf8_json(tmp_path: Path) -> None:
    path = tmp_path / "bad-json.npz"
    _write_archive(path, np.array([1, 0, 1], dtype=np.uint8), np.array([0xFF], dtype=np.uint8))
    with pytest.raises(ProtocolError):
        load_replay(path)


@pytest.mark.parametrize(
    ("member", "offset", "value"),
    [
        ("metadata.npy", 24, 64 * 1024 + 1),
        ("samples.npy", 24, 17 * 1024 * 1024 + 1),
        ("samples.npy", 8, 1),
    ],
)
def test_replay_rejects_oversized_or_encrypted_central_directory_claim(
    tmp_path: Path, member: str, offset: int, value: int
) -> None:
    path = tmp_path / "central-directory-claim.npz"
    _normal_archive(path)
    _patch_central_directory_u32(path, member, offset, value)
    with pytest.raises(ProtocolError):
        load_replay(path)


def test_replay_rejects_archive_larger_than_32_mib_before_zip_open(tmp_path: Path) -> None:
    path = tmp_path / "oversized-archive.npz"
    _normal_archive(path)
    with path.open("r+b") as archive:
        archive.truncate(32 * 1024 * 1024 + 1)
    with pytest.raises(ProtocolError):
        load_replay(path)


def test_replay_rejects_safe_header_declaring_over_16m_samples(tmp_path: Path) -> None:
    path = tmp_path / "oversized-count.npz"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
        archive.writestr("samples.npy", _oversized_count_npy())
        archive.writestr("metadata.npy", _npy_bytes(_metadata_array()))
    with pytest.raises(ProtocolError):
        load_replay(path)


@pytest.mark.parametrize(
    ("descr", "shape"),
    [("|u1", (16_777_217,)), ("|O", (3,)), ("|u1", (1, 3))],
)
def test_replay_rejects_unsafe_sample_header_before_np_load(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, descr: str, shape: tuple[int, ...]
) -> None:
    path = tmp_path / "unsafe-header.npz"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
        archive.writestr("samples.npy", _header_only_npy(descr, shape))
        archive.writestr("metadata.npy", _npy_bytes(_metadata_array()))

    def fail_load(*args: object, **kwargs: object) -> object:
        raise AssertionError("np.load must not run for an unsafe NPY header")

    monkeypatch.setattr(replay_module.np, "load", fail_load)
    with pytest.raises(ProtocolError):
        load_replay(path)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda metadata: {
            **metadata,
            "device": {"identity": "X" * 129, "capabilities": metadata["device"]["capabilities"]},
        },
        lambda metadata: {
            **metadata,
            "device": {"identity": "not-v2", "capabilities": metadata["device"]["capabilities"]},
        },
        lambda metadata: {
            **metadata,
            "device": {
                "identity": metadata["device"]["identity"],
                "capabilities": {"buffer_size": 0},
            },
        },
        lambda metadata: {**metadata, "channel_labels": ["X" * 129] * 8},
        lambda metadata: {**metadata, "channel_mapping": [1] * 8},
        lambda metadata: {**metadata, "pre_trigger_samples": 1, "trigger_index": 2},
        lambda metadata: {**metadata, "requested_count": 4},
    ],
)
def test_replay_rejects_bounded_device_and_all_count_relations(
    tmp_path: Path, mutate: object
) -> None:
    path = tmp_path / "bad-device-or-count.npz"
    changed = mutate(dict(_REQUIRED_METADATA))  # type: ignore[operator,index]
    _write_archive(path, np.array([1, 0, 1], dtype=np.uint8), _metadata_array(changed))
    with pytest.raises(ProtocolError):
        load_replay(path)


def test_replay_rejects_noncanonical_json_bytes(tmp_path: Path) -> None:
    path = tmp_path / "noncanonical-json.npz"
    noncanonical = json.dumps(_REQUIRED_METADATA, indent=2).encode()
    metadata = np.frombuffer(noncanonical, dtype=np.uint8)
    _write_archive(path, np.array([1, 0, 1], dtype=np.uint8), metadata)
    with pytest.raises(ProtocolError):
        load_replay(path)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda metadata: {**metadata, "pre_trigger_samples": -1, "trigger_index": -1},
        lambda metadata: {**metadata, "trigger_index": 2**32},
        lambda metadata: {**metadata, "sample_rate_hz": 101},
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "capabilities": {**metadata["device"]["capabilities"], "buffer_size": 2},
            },
        },
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "capabilities": {
                    **metadata["device"]["capabilities"],
                    "buffer_size": True,
                },
            },
        },
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "capabilities": {
                    **metadata["device"]["capabilities"],
                    "buffer_size": 1.5,
                },
            },
        },
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "capabilities": {**metadata["device"]["capabilities"], "extra": 1},
            },
        },
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "capabilities": {"buffer_size": 131_072},
            },
        },
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "identity": "LOGIC_ANALYZER_" + "A" * 110 + "_V6_0",
            },
        },
        lambda metadata: {
            **metadata,
            "device": {
                **metadata["device"],
                "capabilities": {**metadata["device"]["capabilities"], "channel_count": 7},
            },
        },
    ],
)
def test_replay_rejects_remaining_numeric_and_capability_bounds(
    tmp_path: Path, mutate: object
) -> None:
    path = tmp_path / "remaining-bounds.npz"
    changed = mutate(dict(_REQUIRED_METADATA))  # type: ignore[operator,index]
    _write_archive(path, np.array([1, 0, 1], dtype=np.uint8), _metadata_array(changed))
    with pytest.raises(ProtocolError):
        load_replay(path)
