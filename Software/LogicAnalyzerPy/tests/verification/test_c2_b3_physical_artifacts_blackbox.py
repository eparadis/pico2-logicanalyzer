"""Independent offline verification of the C2-B3 physical artifacts."""

from __future__ import annotations

import hashlib
import io
import json
import os
import zipfile
from pathlib import Path

import numpy as np
import pytest

RUNTIME = Path(os.environ.get("PICO_LA_C2_B3_RUNTIME", "/private/tmp/cycle2-b3-corrected-runtime"))
EXPECTED_DIGESTS = {
    "recovery.json": "40745b7e3be4e53d8b9957f72efd310fcd5c1a309395213b36fbf392da482ad1",
    "capture-8.csv": "fc4c4759394b4fc5180440d09dfe6a0082ca6401b93f18a38782ce3012fa37a3",
    "capture-8.npz": "b1401639e128f78f964552f8e0c613bb3e70ff86b17c015382547d96ad031ad6",
    "capture-16.csv": "ee1e2bf48400c520c6e3a6aa25ce5917303bf720bd3cddf713e1cececfdb2b9f",
    "capture-16.npz": "614765cd3f1385153e348d91a49d75bc47e214640b3532aba8418adb89ff58a1",
    "capture-24.csv": "c6255f31621b1a366dc839af3f94240a2b897760ed2433a43e6f33495866efe5",
    "capture-24.npz": "af3b61f1081f7e272e0d429bae004ddccdc11363cff2061dd25228ddebae41bd",
}


def _artifacts_available(runtime: Path, *, explicitly_supplied: bool) -> bool:
    present = {name for name in EXPECTED_DIGESTS if (runtime / name).is_file()}
    if not present and not explicitly_supplied:
        return False
    missing = sorted(set(EXPECTED_DIGESTS) - present)
    if missing:
        source = "explicitly supplied" if explicitly_supplied else "default"
        raise AssertionError(f"{source} C2-B3 artifact set is incomplete: {', '.join(missing)}")
    return True


@pytest.fixture(scope="module", autouse=True)
def require_complete_physical_artifacts() -> None:
    explicitly_supplied = "PICO_LA_C2_B3_RUNTIME" in os.environ
    if not _artifacts_available(RUNTIME, explicitly_supplied=explicitly_supplied):
        pytest.skip(
            "C2-B3 machine-local physical artifacts were not supplied; checked-in sanitized "
            "evidence remains covered by mandatory nonhardware validation"
        )


def _bytes(name: str) -> bytes:
    data = (RUNTIME / name).read_bytes()
    assert hashlib.sha256(data).hexdigest() == EXPECTED_DIGESTS[name]
    return data


def _read_npy(member: bytes) -> np.ndarray:
    return np.lib.format.read_array(io.BytesIO(member), allow_pickle=False)


def _read_replay(width: int) -> tuple[np.ndarray, dict[str, object]]:
    archive_bytes = _bytes(f"capture-{width}.npz")
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        assert archive.namelist() == ["samples.npy", "metadata.npy"]
        assert all(info.flag_bits & 1 == 0 for info in archive.infolist())
        assert all(info.compress_type == zipfile.ZIP_STORED for info in archive.infolist())
        samples = _read_npy(archive.read("samples.npy"))
        metadata_array = _read_npy(archive.read("metadata.npy"))
    assert metadata_array.dtype == np.dtype("uint8") and metadata_array.ndim == 1
    metadata_bytes = metadata_array.tobytes()
    metadata = json.loads(metadata_bytes.decode("utf-8"))
    assert (
        metadata_bytes
        == json.dumps(metadata, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    )
    return samples, metadata


def _independent_csv(samples: np.ndarray, metadata: dict[str, object]) -> bytes:
    labels = metadata["channel_labels"]
    assert isinstance(labels, list)
    trigger_index = metadata["trigger_index"]
    rate = metadata["sample_rate_hz"]
    assert isinstance(trigger_index, int) and isinstance(rate, int)
    rows = [",".join(["sample_index", "time_seconds", "trigger", *labels])]
    for index, raw_word in enumerate(samples):
        word = int(raw_word)
        cells = [
            str(index),
            format((index - trigger_index) / rate, ".12g"),
            str(int(index == trigger_index)),
            *(str((word >> bit) & 1) for bit in range(len(labels))),
        ]
        rows.append(",".join(cells))
    return ("\n".join(rows) + "\n").encode()


@pytest.mark.parametrize(
    ("width", "dtype", "mode", "driven_mask"),
    [
        (8, np.dtype("uint8"), 0, 0x01),
        (16, np.dtype("uint16"), 1, 0x0101),
        (24, np.dtype("uint32"), 2, 0x810101),
    ],
)
def test_physical_capture_width_mask_frequency_and_csv(
    width: int, dtype: np.dtype[np.generic], mode: int, driven_mask: int
) -> None:
    samples, metadata = _read_replay(width)
    channels = list(range(width))
    assert metadata["schema_version"] == 2
    assert metadata["channel_ids"] == channels
    assert metadata["channel_labels"] == [f"D{i}" for i in channels]
    assert metadata["channel_mapping"] == [f"GPIO{i + 2}" for i in channels]
    assert metadata["sample_dtype"] == dtype.name
    assert metadata["firmware_mode"] == mode
    assert metadata["sample_rate_hz"] == 100_000
    assert metadata["pre_trigger_samples"] == metadata["trigger_index"] == 2048
    assert metadata["post_trigger_samples"] == 4096
    assert metadata["requested_count"] == metadata["actual_count"] == 6144
    assert metadata["trigger_channel"] == 0 and metadata["trigger_edge"] == "rising"
    assert samples.dtype == dtype and samples.shape == (6144,) and samples.flags.c_contiguous
    if width == 24:
        assert not np.any(samples & np.uint32(0xFF000000))

    projected = samples.astype(np.uint32, copy=False) & np.uint32(driven_mask)
    assert np.any(projected == 0)
    assert np.any(projected == driven_mask)
    rises = np.flatnonzero((projected[:-1] != driven_mask) & (projected[1:] == driven_mask)) + 1
    assert len(rises) >= 2
    span = int(rises[-1] - rises[0])
    measured_hz = 100_000 * (len(rises) - 1) / span
    tolerance = 0.02 + 2 / span
    assert abs(measured_hz - 1000) / 1000 <= tolerance

    assert _independent_csv(samples, metadata) == _bytes(f"capture-{width}.csv")


def test_recovery_summary_matches_accepted_bounded_lifecycle() -> None:
    recovery = json.loads(_bytes("recovery.json"))
    assert recovery == {
        "actual_count": 6144,
        "cancel_after_seconds": 0.25,
        "cancel_byte": "ff",
        "device_identity": "LOGIC_ANALYZER_PICO_2_V6_0",
        "edge": "rising",
        "idle_channel": 1,
        "idle_level": "0",
        "measured_frequency_hz": 1000.0,
        "persistent_device_change": False,
        "port": "<PORT_SUPPLIED>",
        "post_trigger_samples": 4096,
        "pre_trigger_samples": 2048,
        "quantization_tolerance_fraction": 0.0005,
        "reidentified": True,
        "sample_rate_hz": 100000,
        "signal_channel": 0,
        "signal_hz": 1000,
        "source_tolerance_fraction": 0.02,
        "span_samples": 4000,
        "tolerance_fraction": 0.0205,
        "transition_count": 41,
    }
    independently_measured = 100_000 * (41 - 1) / 4000
    assert independently_measured == recovery["measured_frequency_hz"]
    assert abs(independently_measured - 1000) / 1000 <= recovery["tolerance_fraction"]
