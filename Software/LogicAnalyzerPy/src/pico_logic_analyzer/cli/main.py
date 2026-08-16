"""CLI surface declaration; hardware operations arrive in later Cycle 1 batches."""

from __future__ import annotations

import argparse
from collections.abc import Sequence


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


def main(argv: Sequence[str] | None = None) -> int:
    """Parse the declared contract; operational commands are intentionally deferred."""
    parser = _parser()
    arguments = parser.parse_args(argv)
    parser.error(f"{arguments.command} is not implemented until its owning Cycle 1 batch")
    return 2
