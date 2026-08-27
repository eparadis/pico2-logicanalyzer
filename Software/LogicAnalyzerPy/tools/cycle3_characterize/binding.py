"""Deterministically refresh or check the non-self candidate binding."""

from __future__ import annotations

import argparse
import json

from .runner import BINDING, binding_payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = json.dumps(binding_payload(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.check:
        return 0 if BINDING.read_text(encoding="utf-8") == payload else 1
    BINDING.write_text(payload, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
