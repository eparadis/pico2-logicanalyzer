"""Independent inert verification of the C3-B1 runner fixture rebinding."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from tools.cycle3_characterize.accounting import CAP_IDS, AccountingFailure
from tools.cycle3_characterize.runner import (
    BINDING,
    CAPS_SHA256,
    FIXTURE_CANDIDATE_COMMIT,
    FIXTURE_CANDIDATE_TREE,
    FIXTURE_MANIFEST_SHA256,
    SEMANTIC_FIXTURE_SHA256,
    RunnerFailure,
    binding_payload,
    load_caps,
    private_test_profile,
    verify_launch_identity,
)

ROOT = Path(__file__).resolve().parents[2]
SUBJECT_COMMIT = "ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a"
SUBJECT_TREE = "457240c481afcdf20ef41a74208749e112efa9b6"
BINDING_SHA256 = "144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_exact_corrected_fixture_and_binding_identities() -> None:
    assert SUBJECT_COMMIT == "ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a"
    assert SUBJECT_TREE == "457240c481afcdf20ef41a74208749e112efa9b6"
    assert FIXTURE_CANDIDATE_COMMIT == "a98d328aab92f3dad66988fb70cc567946dc89d0"
    assert FIXTURE_CANDIDATE_TREE == "450aadcf26bd6c74860872bfbf0a0a1b32d94f3b"
    assert CAPS_SHA256 == "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d"
    assert SEMANTIC_FIXTURE_SHA256 == (
        "1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329"
    )
    assert FIXTURE_MANIFEST_SHA256 == (
        "ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f"
    )
    assert _sha256(BINDING) == BINDING_SHA256
    assert json.loads(BINDING.read_text(encoding="utf-8")) == binding_payload()


def test_all_seventeen_caps_have_exact_accept_reject_boundaries() -> None:
    caps = load_caps()
    assert len(caps) == 17
    assert set(caps) == CAP_IDS
    for cap, value in caps.items():
        assert private_test_profile({cap: value})[cap] == value
        with pytest.raises(AccountingFailure):
            private_test_profile({cap: value + 1})


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        ("candidate_commit", "0" * 40),
        ("candidate_tree", "0" * 40),
        ("caps_sha256", "0" * 64),
        ("manifest_sha256", "0" * 64),
        ("semantic_fixture_sha256", "0" * 64),
    ],
)
def test_each_stale_fixture_identity_fails_before_process_setup(
    monkeypatch: pytest.MonkeyPatch, field: str, replacement: str
) -> None:
    payload = json.loads(BINDING.read_text(encoding="utf-8"))
    payload["accepted_fixture"][field] = replacement
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe",
        lambda: calls.__setitem__("pipe", calls["pipe"] + 1),
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *args, **kwargs: calls.__setitem__("popen", calls["popen"] + 1),
    )
    with pytest.raises(RunnerFailure, match="accepted fixture binding rejected"):
        verify_launch_identity(_binding_data=payload)
    assert calls == {"pipe": 0, "popen": 0}


def test_closed_binding_and_fixture_files_match_their_digests() -> None:
    accepted = json.loads(BINDING.read_text(encoding="utf-8"))["accepted_fixture"]
    data = ROOT / "testdata" / "decoders" / "cycle3"
    assert _sha256(data / "experiment-caps.json") == accepted["caps_sha256"]
    assert _sha256(data / "semantic-fixtures.json") == accepted["semantic_fixture_sha256"]
    assert _sha256(data / "manifest.json") == accepted["manifest_sha256"]
    verify_launch_identity()
