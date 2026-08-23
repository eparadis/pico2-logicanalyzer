#!/usr/bin/env python3
"""Check that committed production assets match their deterministic manifest."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
ASSETS = ROOT / "src" / "pico_logic_analyzer" / "web" / "assets"
MANIFEST = ROOT / "web" / (
    "production-assets-b6.json" if (ROOT / "web" / "production-assets-b6.json").exists()
    else "production-assets.json"
)


def main() -> int:
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    actual = {
        path.relative_to(ASSETS).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(ASSETS.rglob("*"))
        if path.is_file()
    }
    if expected != actual:
        print("web production assets differ from web/production-assets.json", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
