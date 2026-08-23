from __future__ import annotations

import importlib.util
import json
import threading
from pathlib import Path

import numpy as np

from pico_logic_analyzer.model import CaptureConfig, CaptureResult, DeviceInfo

ROOT = Path(__file__).parents[2]
SPEC = importlib.util.spec_from_file_location(
    "c2_b6_native_acceptance", ROOT / "scripts/c2_b6_native_acceptance.py"
)
assert SPEC is not None and SPEC.loader is not None
HARNESS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HARNESS)

DEVICE = DeviceInfo("LOGIC_ANALYZER_PRIVATE_SERIAL_V6_0", 100_000_000, 125_000_000, 393_216, 24)


class FakeService:
    def __init__(self) -> None:
        self.ports: list[str] = []

    def identify_after_reopen(self, port: str, timeout: float) -> tuple[DeviceInfo, DeviceInfo]:
        self.ports.extend((port, port))
        return DEVICE, DEVICE

    def capture_cancellable(
        self, port: str, config: CaptureConfig, cancelled: threading.Event, timeout: float
    ) -> CaptureResult:
        assert not cancelled.is_set() and timeout == 10.0
        self.ports.append(port)
        indices = np.arange(config.requested_count, dtype=np.uint32)
        words = np.zeros(config.requested_count, dtype=np.uint32)
        for position, channel in enumerate(config.channel_ids):
            if channel in (0, 8, 16, 23):
                words |= ((indices // 50) & 1) << position
        return CaptureResult(config, words.astype(config.sample_dtype), DEVICE)


def test_native_harness_is_bounded_and_records_no_raw_port_or_identity(tmp_path: Path) -> None:
    port = "/machine/local/private-port"
    evidence = tmp_path / "acceptance.json"
    service = FakeService()
    HARNESS.run(port, evidence, service)
    serialized = evidence.read_text(encoding="utf-8")
    report = json.loads(serialized)
    assert report["port"] == "<PORT_SUPPLIED>"
    assert port not in serialized and DEVICE.identity not in serialized
    assert [item["width"] for item in report["captures"]] == [8, 16, 24]
    assert report["captures"][2]["observed_signal_channels"] == [0, 8, 16, 23]
    assert report["second_capture_sample_count"] == 4096
    assert report["reidentified_after_reopen"] is True
    assert len(service.ports) == 6 and set(service.ports) == {port}
