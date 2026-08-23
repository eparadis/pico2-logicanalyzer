from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tests.verification import test_c2_b3_physical_artifacts_blackbox as physical

ROOT = Path(__file__).parents[2]


def test_default_absence_skips_but_partial_and_explicit_absence_fail(tmp_path: Path) -> None:
    assert physical._artifacts_available(tmp_path, explicitly_supplied=False) is False

    (tmp_path / next(iter(physical.EXPECTED_DIGESTS))).write_bytes(b"partial")
    with pytest.raises(AssertionError, match="default C2-B3 artifact set is incomplete"):
        physical._artifacts_available(tmp_path, explicitly_supplied=False)

    empty = tmp_path / "explicit-empty"
    empty.mkdir()
    with pytest.raises(
        AssertionError, match="explicitly supplied C2-B3 artifact set is incomplete"
    ):
        physical._artifacts_available(empty, explicitly_supplied=True)


def test_complete_availability_does_not_waive_digest_validation(tmp_path: Path) -> None:
    for name in physical.EXPECTED_DIGESTS:
        (tmp_path / name).write_bytes(b"deliberately-corrupt")
    assert physical._artifacts_available(tmp_path, explicitly_supplied=True) is True
    original = physical.RUNTIME
    try:
        physical.RUNTIME = tmp_path
        with pytest.raises(AssertionError):
            physical._bytes("capture-8.npz")
    finally:
        physical.RUNTIME = original


def test_checked_in_c2_b3_sanitized_evidence_remains_mandatory() -> None:
    command = [
        sys.executable,
        str(ROOT / "scripts/validate_cycle2_evidence.py"),
        str(ROOT / "docs/evidence-manifest/cycle2-schema.json"),
        str(ROOT / "testdata/evidence/c2-b3.json"),
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    evidence = json.loads((ROOT / "testdata/evidence/c2-b3.json").read_text(encoding="utf-8"))
    assert evidence["checkpoint"] == "C2-B3"
