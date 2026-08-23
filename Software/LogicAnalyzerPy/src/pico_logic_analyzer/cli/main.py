"""Cycle 2 command line retaining the accepted Cycle 1 commands."""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import tempfile
from collections.abc import Sequence
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from pico_logic_analyzer.driver import V2DeviceService, list_candidates
from pico_logic_analyzer.formats import (
    MAX_CSV_INPUT_BYTES,
    OutputError,
    import_csv_bytes,
    load_replay,
    write_capture_outputs,
)
from pico_logic_analyzer.model import CaptureConfig, ProtocolError

EXIT_USAGE = 2
EXIT_CONNECTION = 3
EXIT_CAPTURE = 4
EXIT_VALIDATION = 5
EXIT_OUTPUT = 6
UNCALIBRATED_SOURCE_TOLERANCE_FRACTION = 0.02


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pico-la", description="Pico logic analyzer")
    subcommands = parser.add_subparsers(dest="command", required=True)

    devices = subcommands.add_parser("devices", help="list candidate serial ports")
    devices.add_argument("--json", action="store_true", help="write machine-readable output")

    info = subcommands.add_parser("info", help="read V2 analyzer identity")
    info.add_argument("--port", required=True, metavar="PORT")
    info.add_argument("--json", action="store_true")
    info.add_argument("--timeout", type=float, metavar="SECONDS")

    capture = subcommands.add_parser("capture", help="perform an ordered normal capture")
    capture.add_argument("--port", required=True, metavar="PORT")
    capture.add_argument("--sample-rate", required=True, type=int, metavar="HZ")
    capture.add_argument("--trigger-channel", required=True, type=int, metavar="CHANNEL")
    capture.add_argument("--edge", required=True, choices=("rising", "falling"))
    capture.add_argument("--pre-samples", required=True, type=int, metavar="N")
    capture.add_argument("--post-samples", required=True, type=int, metavar="N")
    capture.add_argument(
        "--channels",
        metavar="D0,D1,...",
        help="ordered physical channels (default: D0,D1,D2,D3,D4,D5,D6,D7)",
    )
    capture.add_argument("--csv", required=True, metavar="PATH")
    capture.add_argument("--replay", required=True, metavar="PATH")
    capture.add_argument("--timeout", type=float, metavar="SECONDS")
    capture.add_argument("--force", action="store_true")

    replay = subcommands.add_parser("replay-validate", help="validate a replay artifact")
    replay.add_argument("path", metavar="PATH")
    replay.add_argument("--json", action="store_true")

    csv_import = subcommands.add_parser("csv-import", help="import bounded self-timed CSV")
    csv_import.add_argument("path", metavar="PATH")
    csv_import.add_argument("--channels", metavar="D0,D1,...")
    csv_import.add_argument("--sample-rate", type=int, metavar="HZ")
    csv_import.add_argument("--trigger-channel", required=True, type=int, metavar="CHANNEL")
    csv_import.add_argument("--edge", required=True, choices=("rising", "falling"))
    csv_import.add_argument("--csv", required=True, metavar="PATH")
    csv_import.add_argument("--replay", required=True, metavar="PATH")
    csv_import.add_argument("--force", action="store_true")

    smoke = subcommands.add_parser(
        "hardware-smoke", help="run the opt-in capture hardware procedure"
    )
    smoke.add_argument("--port", required=True, metavar="PORT")
    smoke.add_argument("--signal-hz", required=True, type=int, metavar="HZ")
    smoke.add_argument("--sample-rate", required=True, type=int, metavar="HZ")
    smoke.add_argument("--trigger-channel", required=True, type=int, metavar="CHANNEL")
    smoke.add_argument("--edge", required=True, choices=("rising", "falling"))
    smoke.add_argument("--pre-samples", required=True, type=int, metavar="N")
    smoke.add_argument("--post-samples", required=True, type=int, metavar="N")
    smoke.add_argument("--evidence", required=True, metavar="PATH")
    smoke.add_argument("--timeout", type=float, metavar="SECONDS")

    recovery = subcommands.add_parser(
        "hardware-recovery-smoke", help="run the opt-in recovery hardware procedure"
    )
    recovery.add_argument("--port", required=True, metavar="PORT")
    recovery.add_argument("--idle-channel", required=True, type=int, metavar="CHANNEL")
    recovery.add_argument("--idle-level", required=True, choices=("0", "1"))
    recovery.add_argument("--cancel-after", required=True, type=float, metavar="SECONDS")
    recovery.add_argument("--signal-channel", required=True, type=int, metavar="CHANNEL")
    recovery.add_argument("--signal-hz", required=True, type=int, metavar="HZ")
    recovery.add_argument("--sample-rate", required=True, type=int, metavar="HZ")
    recovery.add_argument("--edge", required=True, choices=("rising", "falling"))
    recovery.add_argument("--pre-samples", required=True, type=int, metavar="N")
    recovery.add_argument("--post-samples", required=True, type=int, metavar="N")
    recovery.add_argument("--evidence", required=True, metavar="PATH")
    recovery.add_argument("--timeout", type=float, metavar="SECONDS")
    web = subcommands.add_parser("web", help="start the loopback-only offline web shell")
    web.add_argument("--host", default="127.0.0.1", metavar="LOOPBACK_ADDRESS")
    web.add_argument("--port", default=4173, type=int, metavar="PORT")
    web.add_argument(
        "--device-port",
        metavar="PORT",
        help="explicit serial port for live capture (never exposed to the browser)",
    )
    return parser


def _timeout(value: float | None) -> float:
    timeout = 10.0 if value is None else value
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("--timeout must be a finite positive number")
    return timeout


def _write_json(value: object) -> None:
    print(json.dumps(value, sort_keys=True, separators=(",", ":")))


def _devices(arguments: argparse.Namespace) -> int:
    candidates = list_candidates()
    if arguments.json:
        _write_json({"devices": [candidate.json_object() for candidate in candidates]})
    elif not candidates:
        print("No supported Pico logic analyzer serial ports found.")
    else:
        for candidate in candidates:
            metadata = []
            if candidate.serial_number is not None:
                metadata.append(f"serial={candidate.serial_number}")
            if candidate.location is not None:
                metadata.append(f"location={candidate.location}")
            suffix = "" if not metadata else " " + " ".join(metadata)
            print(f"{candidate.device} VID=1209 PID=3020{suffix}")
    return 0


def _info(arguments: argparse.Namespace) -> int:
    device = V2DeviceService().identify(arguments.port, _timeout(arguments.timeout))
    if arguments.json:
        _write_json(
            {
                "blast_frequency_hz": device.blast_frequency_hz,
                "buffer_size": device.buffer_size,
                "channel_count": device.channel_count,
                "identity": device.identity,
                "max_frequency_hz": device.max_frequency_hz,
            }
        )
    else:
        print(device.identity)
        print(f"FREQ:{device.max_frequency_hz}")
        print(f"BLASTFREQ:{device.blast_frequency_hz}")
        print(f"BUFFER:{device.buffer_size}")
        print(f"CHANNELS:{device.channel_count}")
    return 0


def _channel_ids(value: str | None) -> tuple[int, ...] | None:
    if value is None:
        return None
    try:
        return tuple(int(channel) for channel in value.split(","))
    except ValueError as exc:
        raise ValueError("--channels must be comma-separated integer IDs") from exc


def _capture_config(arguments: argparse.Namespace) -> CaptureConfig:
    channel_ids = tuple(range(8))
    if getattr(arguments, "channels", None) is not None:
        try:
            channel_ids = tuple(int(value) for value in arguments.channels.split(","))
        except ValueError as exc:
            raise ValueError("--channels must be comma-separated integer IDs") from exc
    return CaptureConfig(
        arguments.sample_rate,
        arguments.pre_samples,
        arguments.post_samples,
        arguments.trigger_channel,
        arguments.edge,
        channel_ids,
    )


def _capture(arguments: argparse.Namespace) -> int:
    result = V2DeviceService().capture(
        arguments.port, _capture_config(arguments), _timeout(arguments.timeout)
    )
    write_capture_outputs(
        result, Path(arguments.csv), Path(arguments.replay), force=arguments.force
    )
    return 0


def _csv_import(arguments: argparse.Namespace) -> int:
    source_path = Path(arguments.path)
    try:
        if source_path.stat().st_size > MAX_CSV_INPUT_BYTES:
            raise ProtocolError("CSV input is too large")
        with source_path.open("rb") as file:
            source = file.read(MAX_CSV_INPUT_BYTES + 1)
    except OSError as exc:
        raise OutputError(f"could not read CSV input: {exc}") from exc
    result = import_csv_bytes(
        source,
        channel_ids=_channel_ids(arguments.channels),
        sample_rate_hz=arguments.sample_rate,
        trigger_channel=arguments.trigger_channel,
        trigger_edge=arguments.edge,
    )
    write_capture_outputs(
        result, Path(arguments.csv), Path(arguments.replay), force=arguments.force
    )
    return 0


def _atomic_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    temp = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as file:
            json.dump(value, file, sort_keys=True, separators=(",", ":"))
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())
        os.replace(temp, path)
    except Exception as exc:
        temp.unlink(missing_ok=True)
        raise OutputError(f"could not write hardware evidence: {exc}") from exc


def _frequency_measurement(
    samples: NDArray[np.generic], channel: int, edge: str, sample_rate: int
) -> tuple[float, int, int, float]:
    values = [((int(word) >> channel) & 1) for word in samples]  # bounded by negotiated buffer
    transitions = [
        index
        for index in range(1, len(values))
        if values[index - 1] != values[index] and values[index] == (1 if edge == "rising" else 0)
    ]
    if len(transitions) < 2:
        raise ProtocolError("periodic input has fewer than two requested-polarity edges")
    span_samples = transitions[-1] - transitions[0]
    if span_samples <= 0:
        raise ProtocolError("invalid periodic edge spacing")
    transition_count = len(transitions)
    measured = sample_rate * (transition_count - 1) / span_samples
    # First and last transition locations can each be quantized by one sample.
    return measured, transition_count, span_samples, 2 / span_samples


def _measured_frequency(
    samples: NDArray[np.uint8], channel: int, edge: str, sample_rate: int
) -> float:
    """Compatibility helper for callers that require only the measured frequency."""
    return _frequency_measurement(samples, channel, edge, sample_rate)[0]


def _hardware_smoke(arguments: argparse.Namespace) -> int:
    result = V2DeviceService().capture(
        arguments.port, _capture_config(arguments), _timeout(arguments.timeout)
    )
    measured, transition_count, span_samples, quantization_tolerance = _frequency_measurement(
        result.samples,
        result.config.trigger_channel,
        result.config.trigger_edge,
        result.config.sample_rate_hz,
    )
    source_tolerance = UNCALIBRATED_SOURCE_TOLERANCE_FRACTION
    tolerance = source_tolerance + quantization_tolerance
    if quantization_tolerance >= 1:
        raise ProtocolError("periodic waveform span is too short for frequency validation")
    if abs(measured - arguments.signal_hz) / arguments.signal_hz > tolerance:
        raise ProtocolError("measured frequency is outside hardware-smoke tolerance")
    _atomic_json(
        Path(arguments.evidence),
        {
            "actual_count": len(result.samples),
            "channel_mapping": list(result.channel_mapping),
            "device": {
                "capabilities": {
                    "blast_frequency_hz": result.device.blast_frequency_hz,
                    "buffer_size": result.device.buffer_size,
                    "channel_count": result.device.channel_count,
                    "max_frequency_hz": result.device.max_frequency_hz,
                },
                "identity": result.device.identity,
            },
            "edge": result.config.trigger_edge,
            "edge_observed": True,
            "measured_frequency_hz": measured,
            "persistent_device_change": False,
            "port": "<PORT_SUPPLIED>",
            "post_trigger_samples": result.config.post_trigger_samples,
            "pre_trigger_samples": result.config.pre_trigger_samples,
            "requested_count": result.config.requested_count,
            "sample_rate_hz": result.config.sample_rate_hz,
            "signal_hz": arguments.signal_hz,
            "source_tolerance_fraction": source_tolerance,
            "tolerance_fraction": tolerance,
            "quantization_tolerance_fraction": quantization_tolerance,
            "span_samples": span_samples,
            "transition_count": transition_count,
            "trigger_channel": result.config.trigger_channel,
            "waveform_nonconstant": True,
        },
    )
    return 0


def _hardware_recovery_smoke(arguments: argparse.Namespace) -> int:
    timeout = _timeout(arguments.timeout)
    idle = CaptureConfig(
        arguments.sample_rate,
        arguments.pre_samples,
        arguments.post_samples,
        arguments.idle_channel,
        arguments.edge,
    )
    signal = CaptureConfig(
        arguments.sample_rate,
        arguments.pre_samples,
        arguments.post_samples,
        arguments.signal_channel,
        arguments.edge,
    )
    result = V2DeviceService().recovery_capture(
        arguments.port, idle, signal, arguments.cancel_after, timeout
    )
    measured, transitions, span, quantization = _frequency_measurement(
        result.samples, signal.trigger_channel, signal.trigger_edge, signal.sample_rate_hz
    )
    tolerance = UNCALIBRATED_SOURCE_TOLERANCE_FRACTION + quantization
    if abs(measured - arguments.signal_hz) / arguments.signal_hz > tolerance:
        raise ProtocolError("recovered periodic waveform is outside validation tolerance")
    _atomic_json(
        Path(arguments.evidence),
        {
            "actual_count": len(result.samples),
            "cancel_after_seconds": arguments.cancel_after,
            "cancel_byte": "ff",
            "device_identity": result.device.identity,
            "edge": signal.trigger_edge,
            "idle_channel": arguments.idle_channel,
            "idle_level": arguments.idle_level,
            "measured_frequency_hz": measured,
            "persistent_device_change": False,
            "port": "<PORT_SUPPLIED>",
            "post_trigger_samples": signal.post_trigger_samples,
            "pre_trigger_samples": signal.pre_trigger_samples,
            "quantization_tolerance_fraction": quantization,
            "reidentified": True,
            "sample_rate_hz": signal.sample_rate_hz,
            "signal_channel": arguments.signal_channel,
            "signal_hz": arguments.signal_hz,
            "source_tolerance_fraction": UNCALIBRATED_SOURCE_TOLERANCE_FRACTION,
            "span_samples": span,
            "tolerance_fraction": tolerance,
            "transition_count": transitions,
        },
    )
    return 0


def _replay_validate(arguments: argparse.Namespace) -> int:
    samples, metadata = load_replay(Path(arguments.path))
    if arguments.json:
        _write_json(
            {
                "actual_count": len(samples),
                "schema_version": metadata["schema_version"],
                "valid": True,
            }
        )
    return 0


def _web(arguments: argparse.Namespace) -> int:
    try:
        from pico_logic_analyzer.web.server import run
    except ModuleNotFoundError as exc:
        if exc.name in {"aiohttp", "pico_logic_analyzer.web"}:
            print(
                "pico-la: web support is not installed; run "
                "pip install 'pico-logic-analyzer[web]'",
                file=sys.stderr,
            )
            return EXIT_USAGE
        raise
    environment_port = os.environ.get("PICO_LA_DEVICE_PORT")
    if arguments.device_port and environment_port and arguments.device_port != environment_port:
        raise ValueError("conflicting explicit device ports")
    return run(
        arguments.host,
        arguments.port,
        device_port=arguments.device_port or environment_port,
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Run the bounded CLI without ever selecting a port implicitly."""
    parser = _parser()
    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "devices":
            return _devices(arguments)
        if arguments.command == "info":
            return _info(arguments)
        if arguments.command == "capture":
            return _capture(arguments)
        if arguments.command == "csv-import":
            return _csv_import(arguments)
        if arguments.command == "replay-validate":
            return _replay_validate(arguments)
        if arguments.command == "web":
            return _web(arguments)
        if arguments.command == "hardware-smoke":
            return _hardware_smoke(arguments)
        if arguments.command == "hardware-recovery-smoke":
            return _hardware_recovery_smoke(arguments)
        print(
            f"pico-la: {arguments.command} is not implemented until its owning batch",
            file=sys.stderr,
        )
        return EXIT_USAGE
    except TimeoutError as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return (
            EXIT_CAPTURE
            if arguments.command in {"capture", "hardware-smoke", "hardware-recovery-smoke"}
            else EXIT_CONNECTION
        )
    except ProtocolError as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return (
            EXIT_VALIDATION
            if arguments.command
            in {"csv-import", "replay-validate", "hardware-smoke", "hardware-recovery-smoke"}
            else EXIT_CONNECTION
        )
    except ConnectionError as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return EXIT_CONNECTION
    except ValueError as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return EXIT_USAGE
    except OutputError as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return EXIT_OUTPUT
    except KeyboardInterrupt:
        print("pico-la: capture cancelled", file=sys.stderr)
        return EXIT_CAPTURE
