"""Cycle 1 command line; only discovery and identity are operational in C1-B3."""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections.abc import Sequence

from pico_logic_analyzer.driver import V2DeviceService, list_candidates
from pico_logic_analyzer.model import ProtocolError

EXIT_USAGE = 2
EXIT_CONNECTION = 3


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pico-la", description="Pico logic analyzer")
    subcommands = parser.add_subparsers(dest="command", required=True)

    devices = subcommands.add_parser("devices", help="list candidate serial ports")
    devices.add_argument("--json", action="store_true", help="write machine-readable output")

    info = subcommands.add_parser("info", help="read V2 analyzer identity")
    info.add_argument("--port", required=True, metavar="PORT")
    info.add_argument("--json", action="store_true")
    info.add_argument("--timeout", type=float, metavar="SECONDS")

    capture = subcommands.add_parser("capture", help="perform an 8-channel capture")
    capture.add_argument("--port", required=True, metavar="PORT")
    capture.add_argument("--sample-rate", required=True, type=int, metavar="HZ")
    capture.add_argument("--trigger-channel", required=True, type=int, metavar="CHANNEL")
    capture.add_argument("--edge", required=True, choices=("rising", "falling"))
    capture.add_argument("--pre-samples", required=True, type=int, metavar="N")
    capture.add_argument("--post-samples", required=True, type=int, metavar="N")
    capture.add_argument("--csv", required=True, metavar="PATH")
    capture.add_argument("--replay", required=True, metavar="PATH")
    capture.add_argument("--timeout", type=float, metavar="SECONDS")
    capture.add_argument("--force", action="store_true")

    replay = subcommands.add_parser("replay-validate", help="validate a replay artifact")
    replay.add_argument("path", metavar="PATH")
    replay.add_argument("--json", action="store_true")

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


def main(argv: Sequence[str] | None = None) -> int:
    """Run C1-B3 discovery/identity without ever selecting a port implicitly."""
    parser = _parser()
    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "devices":
            return _devices(arguments)
        if arguments.command == "info":
            return _info(arguments)
        print(
            f"pico-la: {arguments.command} is not implemented until its owning Cycle 1 batch",
            file=sys.stderr,
        )
        return EXIT_USAGE
    except (ConnectionError, TimeoutError, ProtocolError) as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return EXIT_CONNECTION
    except ValueError as exc:
        print(f"pico-la: {exc}", file=sys.stderr)
        return EXIT_USAGE
