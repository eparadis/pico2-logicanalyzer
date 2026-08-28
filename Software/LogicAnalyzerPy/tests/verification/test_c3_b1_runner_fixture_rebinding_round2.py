"""Independent round-2 verification of the C3-B1 runner fixture rebind."""

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
    expected_sources,
    load_caps,
    private_test_profile,
    verify_launch_identity,
)

ROOT = Path(__file__).resolve().parents[2]
SUBJECT_COMMIT = "55d22640334ef05176568f275c3e4e7ec63c3336"
SUBJECT_TREE = "b96790c572f2fceda4445f55d8373b9a21e2cd9d"
BINDING_SHA256 = "4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7"

EXPECTED_FIXTURE = {
    "candidate_commit": "3af6b9f80dd52611e14acca407707d1da7b8d9ac",
    "candidate_tree": "14c010153ea5542617e601e4126047c561a48483",
    "caps_sha256": "6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d",
    "manifest_sha256": "71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9",
    "semantic_fixture_sha256": (
        "34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094"
    ),
}

OLD_FIXTURE = {
    "candidate_commit": "a98d328aab92f3dad66988fb70cc567946dc89d0",
    "candidate_tree": "450aadcf26bd6c74860872bfbf0a0a1b32d94f3b",
    "manifest_sha256": "ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f",
    "semantic_fixture_sha256": (
        "1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329"
    ),
}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _payload() -> dict[str, object]:
    return json.loads(BINDING.read_text(encoding="utf-8"))


def test_exact_subject_and_canonical_fixture_binding() -> None:
    assert SUBJECT_COMMIT == "55d22640334ef05176568f275c3e4e7ec63c3336"
    assert SUBJECT_TREE == "b96790c572f2fceda4445f55d8373b9a21e2cd9d"
    assert _sha256(BINDING) == BINDING_SHA256
    payload = _payload()
    assert payload == binding_payload()
    assert payload["accepted_fixture"] == EXPECTED_FIXTURE
    assert FIXTURE_CANDIDATE_COMMIT == EXPECTED_FIXTURE["candidate_commit"]
    assert FIXTURE_CANDIDATE_TREE == EXPECTED_FIXTURE["candidate_tree"]
    assert CAPS_SHA256 == EXPECTED_FIXTURE["caps_sha256"]
    assert FIXTURE_MANIFEST_SHA256 == EXPECTED_FIXTURE["manifest_sha256"]
    assert SEMANTIC_FIXTURE_SHA256 == EXPECTED_FIXTURE["semantic_fixture_sha256"]
    assert set(payload["sources"]) == expected_sources()
    assert len(payload["sources"]) == 24


def test_fixture_gate_lineage_is_in_accepted_order() -> None:
    method = (ROOT / "docs/cycle-3-characterization-method.md").read_text(
        encoding="utf-8"
    )
    positions = [
        method.index(identity)
        for identity in (
            "3a29e4684af6a4c8e53aa4f83f9692ddebab5670",
            "efcc7759f4af89eb438b2b8611e250d0962fc8c6",
            "972322116b737d2fcad37e46d23116b031841359",
        )
    ]
    assert positions == sorted(positions)


@pytest.mark.parametrize(
    ("field", "replacement"),
    [
        *OLD_FIXTURE.items(),
        *((field, "0" * len(value)) for field, value in EXPECTED_FIXTURE.items()),
    ],
)
def test_stale_or_substituted_fixture_identity_is_pre_spawn(
    monkeypatch: pytest.MonkeyPatch, field: str, replacement: str
) -> None:
    payload = _payload()
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


@pytest.mark.parametrize("mutation", ["missing", "extra", "digest", "traversal"])
def test_closed_source_inventory_rejects_mutations_pre_spawn(
    monkeypatch: pytest.MonkeyPatch, mutation: str
) -> None:
    payload = _payload()
    sources = payload["sources"]
    first = sorted(sources)[0]
    if mutation == "missing":
        del sources[first]
    elif mutation == "extra":
        sources["tools/cycle3_characterize/extra.py"] = "0" * 64
    elif mutation == "digest":
        sources[first] = "0" * 64
    else:
        sources["../escape.py"] = "0" * 64
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe",
        lambda: pytest.fail("pipe created before identity rejection"),
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *args, **kwargs: pytest.fail("process created before identity rejection"),
    )
    with pytest.raises(RunnerFailure, match="binding allowlist rejected|bound source rejected"):
        verify_launch_identity(_binding_data=payload)


def test_all_seventeen_caps_retain_exact_boundaries() -> None:
    caps = load_caps()
    assert len(caps) == 17
    assert set(caps) == CAP_IDS
    for cap, value in caps.items():
        assert private_test_profile({cap: value})[cap] == value
        with pytest.raises(AccountingFailure):
            private_test_profile({cap: value + 1})


def test_bound_fixture_files_and_all_sources_match_exact_digests() -> None:
    payload = _payload()
    data = ROOT / "testdata" / "decoders" / "cycle3"
    assert _sha256(data / "experiment-caps.json") == EXPECTED_FIXTURE["caps_sha256"]
    assert _sha256(data / "manifest.json") == EXPECTED_FIXTURE["manifest_sha256"]
    assert (
        _sha256(data / "semantic-fixtures.json")
        == EXPECTED_FIXTURE["semantic_fixture_sha256"]
    )
    assert payload == binding_payload()
    verify_launch_identity()
