"""Independent, non-decoder verification of the immutable C3-B1 runner."""

from __future__ import annotations

import ast
import hashlib
import json
import os
from pathlib import Path

import pytest

from tools.cycle3_characterize.accounting import (
    CAP_IDS,
    AccountingFailure,
    CapProfile,
    result_measurements,
    validate_result,
)
from tools.cycle3_characterize.runner import (
    CAPS_SHA256,
    FIXTURE_CANDIDATE_COMMIT,
    FIXTURE_CANDIDATE_TREE,
    RunnerFailure,
    _private_last_evidence,
    _safe_file,
    binding_payload,
    characterize,
    load_caps,
    private_test_profile,
    run_internal_probe,
    verify_launch_identity,
)
from tools.cycle3_characterize.snapshot_host import (
    DECODER_PATHS,
    SnapshotHostFailure,
    _Capture,
    validate_characterization_request,
)

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "cycle3_characterize"
REPOSITORY = ROOT.parents[1]
SUBJECT_COMMIT = "11a8ade5d828830347095bf2580766c149cb8aef"
SUBJECT_TREE = "61fa5ba18f3620188ee61dac7e3622803591aad9"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _valid_request(decoder: str = "uart") -> dict[str, object]:
    channels = {"uart": [0, 255], "spi": [0, 1, 255, 255], "i2c": [0, 1]}[decoder]
    return {
        "version": 1,
        "decoder": decoder,
        "files": list(DECODER_PATHS[decoder]),
        "samplerate": 1_000_000,
        "channels": channels,
        "samples": [0, 1],
        "options": {},
    }


def test_exact_candidate_fixture_binding_and_all_seventeen_caps() -> None:
    assert SUBJECT_COMMIT == "11a8ade5d828830347095bf2580766c149cb8aef"
    assert SUBJECT_TREE == "61fa5ba18f3620188ee61dac7e3622803591aad9"
    assert FIXTURE_CANDIDATE_COMMIT == "7c57a347bbe575e3f451383ea498f56abc362f26"
    assert FIXTURE_CANDIDATE_TREE == "02a408895dd834e6e6885218cb7323f46439e880"
    caps_file = ROOT / "testdata/decoders/cycle3/experiment-caps.json"
    assert _sha(caps_file) == CAPS_SHA256
    caps = load_caps()
    assert len(caps) == 17 and set(caps) == CAP_IDS
    for cap in CAP_IDS:
        assert private_test_profile({cap: caps[cap]})[cap] == caps[cap]
        with pytest.raises(AccountingFailure):
            private_test_profile({cap: caps[cap] + 1})


def test_binding_is_exact_closed_and_digest_complete() -> None:
    verify_launch_identity()
    committed = json.loads((TOOL / "candidate-binding.json").read_text())
    assert committed == binding_payload()
    assert set(committed["sources"]) == set(binding_payload()["sources"])
    assert all(_sha(REPOSITORY / name if name.startswith("Software/") else ROOT / name) == digest
               for name, digest in committed["sources"].items())


def test_file_symlink_shadow_environment_and_cwd_boundaries(tmp_path: Path) -> None:
    ordinary = tmp_path / "ordinary.py"
    ordinary.write_text("x = 1\n")
    link = tmp_path / "link.py"
    link.symlink_to(ordinary)
    assert _safe_file(ordinary, tmp_path)
    assert not _safe_file(link, tmp_path)
    assert not _safe_file(Path("/etc/passwd"), tmp_path)
    launch = json.loads((TOOL / "launch.json").read_text())
    assert launch["arguments"] == ["-I", "worker.py"]
    assert launch["working_directory"] == "tools/cycle3_characterize"
    assert launch["import_roots"] == ["tools/cycle3_characterize"]
    assert launch["environment"] == {
        "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": ""
    }
    assert launch["characterization_probe_mode"] == "disabled"
    assert not (TOOL / "json.py").exists()


def test_framing_nonfinite_depth_items_text_binary_and_retained_accounting() -> None:
    caps = load_caps()
    minimal = {"version": 1, "records": []}
    measures = result_measurements(minimal)
    for name in ("encoded_bytes", "decoded_bytes", "nested_depth", "nested_items",
                 "retained_result_bytes"):
        profile = CapProfile({**caps, name: measures[name]})
        assert validate_result(minimal, profile) == minimal
    with pytest.raises(AccountingFailure):
        result_measurements({"version": 1, "records": [float("nan")]})
    with pytest.raises(AccountingFailure):
        validate_result({"version": 1, "records": [], "text": "xx"},
                        CapProfile({**caps, "text_bytes": 1}))
    with pytest.raises(AccountingFailure):
        validate_result({"version": 1, "records": [], "binary": "eHg="},
                        CapProfile({**caps, "binary_bytes": 1}))


@pytest.mark.parametrize(
    "probe",
    ["partial", "extra", "nonfinite", "malformed", "deep", "items", "base64",
     "stdout_flood", "stderr_flood", "diagnostic_flood", "recursion_over"],
)
def test_each_hostile_child_is_closed_reaped_and_followed_by_recovery(probe: str) -> None:
    with pytest.raises(RunnerFailure):
        run_internal_probe(probe)
    evidence = _private_last_evidence()
    assert evidence.reaped and evidence.descriptors_closed and len(evidence.closed_fds) == 2
    assert run_internal_probe("valid").value["records"] == []
    recovered = _private_last_evidence()
    assert recovered.disposition == "completed" and recovered.reaped
    assert recovered.descriptors_closed and len(recovered.closed_fds) == 2


@pytest.mark.parametrize("probe, disposition", [("hang", "terminated-and-reaped"),
                                                  ("ignore_term", "killed-and-reaped")])
def test_graceful_termination_forced_kill_exact_reap_and_recovery(
    probe: str, disposition: str
) -> None:
    profile = private_test_profile({"wall_deadline_ms": 80, "terminate_grace_ms": 80})
    with pytest.raises(RunnerFailure):
        run_internal_probe(probe, _profile=profile)
    evidence = _private_last_evidence()
    assert evidence.disposition == disposition
    assert evidence.reaped and evidence.descriptors_closed
    assert len(evidence.closed_fds) == 2
    assert run_internal_probe("valid", _profile=profile).value["version"] == 1


def test_python312_rlimit_recursion_and_real_child_stream_boundaries() -> None:
    limits = run_internal_probe("limits")
    details = json.loads(limits.diagnostics)
    caps = load_caps()
    assert details == {
        "recursion": caps["recursion_limit"],
        "soft": caps["worker_address_space_bytes"],
        "hard": caps["worker_address_space_bytes"],
    }
    for probe, cap in (("stdout_noise", "stdout_bytes"), ("stderr", "stderr_bytes"),
                       ("text_cap", "text_bytes"), ("binary_cap", "binary_bytes"),
                       ("nested_items", "nested_items"), ("large_result", "retained_result_bytes")):
        with pytest.raises(RunnerFailure):
            run_internal_probe(probe, _profile=private_test_profile({cap: 1}))
        assert _private_last_evidence().reaped
        assert run_internal_probe("valid").value["version"] == 1


def test_public_route_disabled_private_route_present_without_invocation() -> None:
    with pytest.raises(RunnerFailure, match="disabled pending runner gate"):
        characterize(_valid_request())
    tree = ast.parse((TOOL / "runner.py").read_text())
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    private = functions["_orchestration_execute_approved_snapshot"]
    assert any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
               and node.func.id == "_run_request" for node in ast.walk(private))
    worker_tree = ast.parse((TOOL / "worker.py").read_text())
    assert any(isinstance(node, ast.Attribute) and node.attr == "execute_snapshot"
               for node in ast.walk(worker_tree))


def test_fixed_nine_source_graph_options_and_api_v3_without_decoder() -> None:
    provenance = json.loads((ROOT / "testdata/decoders/cycle3/provenance.json").read_text())
    assert len(provenance["files"]) == 9
    assert set(DECODER_PATHS) == {"uart", "spi", "i2c"}
    for decoder in DECODER_PATHS:
        assert validate_characterization_request(_valid_request(decoder))["decoder"] == decoder
    for request in (
        {**_valid_request("spi"), "options": {"wordsize": 9}},
        {**_valid_request("i2c"), "options": {"address_format": "other"}},
        {**_valid_request("uart"), "options": {"sample_point": 0}},
    ):
        with pytest.raises(SnapshotHostFailure):
            validate_characterization_request(request)
    owner = type("Owner", (), {})()
    capture = _Capture([0, 255], [0, 1, 1])
    capture.owner = owner
    assert capture.HasChannel(0) and not capture.HasChannel(1)
    assert capture.Wait({}) == (0, 255)
    assert capture.Wait([{"skip": 1}, {"0": "r"}]) == (1, 255)
    assert owner.matched == (True, True)
    output = capture.Register(2, int)
    capture.Put(0, len(capture.samples), output, b"x")
    assert capture.records[0]["end_sample"] == 3


def test_method_truth_and_no_broad_exception_suppression() -> None:
    method = (ROOT / "docs/cycle-3-characterization-method.md").read_text()
    assert "No decoder has run" in method
    assert "characterize` remains unavailable" in method
    for name in ("runner.py", "worker.py", "accounting.py", "snapshot_host.py"):
        tree = ast.parse((TOOL / name).read_text())
        assert not any(isinstance(node, ast.With) and any(
            isinstance(item.context_expr, ast.Call)
            and isinstance(item.context_expr.func, ast.Attribute)
            and item.context_expr.func.attr == "suppress"
            for item in node.items) for node in ast.walk(tree))
    assert os.environ.get("PYTHONPATH", "") != str(TOOL)
