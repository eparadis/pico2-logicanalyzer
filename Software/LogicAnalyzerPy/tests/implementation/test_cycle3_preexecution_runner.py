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
    deep_size,
    result_measurements,
    validate_result,
)
from tools.cycle3_characterize.probes import PROBES
from tools.cycle3_characterize.runner import (
    BINDING,
    CAPS_SHA256,
    FIXTURE_CANDIDATE_COMMIT,
    FIXTURE_CANDIDATE_TREE,
    FIXTURE_MANIFEST_SHA256,
    SEMANTIC_FIXTURE_SHA256,
    STDLIB_ALLOWLIST,
    RunnerFailure,
    _child_environment,
    _frame,
    _parse_result,
    _popen_spec,
    _private_last_evidence,
    _request_for_characterization,
    _run_request,
    _safe_file,
    _validate_launch_document,
    _verify_tool_inventory,
    characterize,
    load_caps,
    private_test_profile,
    run_internal_probe,
    verify_launch_identity,
)
from tools.cycle3_characterize.snapshot_host import (
    DECODER_PATHS,
    DECODER_SET_SHA256,
    SOURCE_SHA256,
    SnapshotHostFailure,
    _Capture,
    canonical_value,
    format_metrics,
    load_pinned_bytes,
    validate_characterization_request,
)

ROOT = Path(__file__).parents[2]
TOOL = ROOT / "tools" / "cycle3_characterize"


def test_snapshot_host_constants_exactly_match_provenance() -> None:
    provenance = json.loads((ROOT / "testdata/decoders/cycle3/provenance.json").read_text())
    assert SOURCE_SHA256 == {item["path"]: item["sha256"] for item in provenance["files"]}
    assert set().union(*map(set, DECODER_PATHS.values())) == set(SOURCE_SHA256)
    assert DECODER_SET_SHA256 == {
        item["decoder"]: item["sha256"] for item in provenance["decoder_file_sets"]
    }


def test_snapshot_import_graph_is_closed_by_the_launch_allowlist() -> None:
    imported: set[str] = set()
    for relative in SOURCE_SHA256:
        tree = ast.parse((ROOT.parents[1] / relative).read_bytes())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(name.name.split(".")[0] for name in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                imported.add(node.module.split(".")[0])
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "__import__"
            ):
                pytest.fail(f"dynamic snapshot import in {relative}")
    assert imported == {
        "collections",
        "common",
        "enum",
        "itertools",
        "math",
        "re",
        "sigrokdecode",
    }
    assert imported - {"common", "sigrokdecode"} <= set(STDLIB_ALLOWLIST)


def test_snapshot_host_loader_rejects_containment_and_digest_mismatch(tmp_path: Path) -> None:
    source = tmp_path / "ok.py"
    source.write_bytes(b"ok")
    digest = hashlib.sha256(b"ok").hexdigest()
    assert load_pinned_bytes(tmp_path, "ok.py", digest) == b"ok"
    for name in ("../ok.py", str(source)):
        with pytest.raises(SnapshotHostFailure):
            load_pinned_bytes(tmp_path, name, digest)
    with pytest.raises(SnapshotHostFailure):
        load_pinned_bytes(tmp_path, "ok.py", "0" * 64)


def test_snapshot_host_canonical_values_fail_closed() -> None:
    assert canonical_value({"bytes": b"x", "items": [1, None]}) == {
        "bytes": {"$cycle3_bytes": "eA==", "length": 1},
        "items": [1, None],
    }
    with pytest.raises(SnapshotHostFailure):
        canonical_value(object())


def test_accepted_profile_is_the_exact_immutable_seventeen_cap_input() -> None:
    caps_path = ROOT / "testdata" / "decoders" / "cycle3" / "experiment-caps.json"
    assert hashlib.sha256(caps_path.read_bytes()).hexdigest() == CAPS_SHA256
    assert set(load_caps()) == CAP_IDS


def test_corrected_semantic_fixture_digest_is_immutable() -> None:
    fixture_path = ROOT / "testdata" / "decoders" / "cycle3" / "semantic-fixtures.json"
    assert hashlib.sha256(fixture_path.read_bytes()).hexdigest() == SEMANTIC_FIXTURE_SHA256


CAP_BOUNDARY_MATRIX = (
    "wall_deadline_ms",
    "terminate_grace_ms",
    "input_samples",
    "request_bytes",
    "output_records",
    "encoded_bytes",
    "decoded_bytes",
    "stdout_bytes",
    "stderr_bytes",
    "diagnostic_bytes",
    "text_bytes",
    "binary_bytes",
    "nested_depth",
    "nested_items",
    "retained_result_bytes",
    "recursion_limit",
    "worker_address_space_bytes",
)


@pytest.mark.parametrize("cap", CAP_BOUNDARY_MATRIX)
def test_every_immutable_cap_accepts_its_value_and_rejects_value_plus_one(cap: str) -> None:
    """The test-only derivation cannot expand any production boundary."""
    production = load_caps()
    profile = private_test_profile({cap: production[cap]})
    assert profile[cap] == production[cap]
    with pytest.raises(AccountingFailure):
        private_test_profile({cap: production[cap] + 1})


def _profile_with(cap: str, value: int) -> CapProfile:
    return private_test_profile({cap: value})


@pytest.mark.parametrize("count", [1, 2])
def test_output_records_boundary_fixture(count: int) -> None:
    value = {"version": 1, "records": list(range(count))}
    assert validate_result(value, _profile_with("output_records", count)) == value
    if count == 2:
        with pytest.raises(AccountingFailure):
            validate_result(value, _profile_with("output_records", count - 1))


@pytest.mark.parametrize(
    ("field", "cap"), [("text", "text_bytes"), ("diagnostics", "diagnostic_bytes")]
)
def test_textual_boundary_fixture(field: str, cap: str) -> None:
    accepted = {"version": 1, "records": [], field: "x" * 8}
    assert validate_result(accepted, _profile_with(cap, 8)) == accepted
    rejected = {"version": 1, "records": [], field: "x" * 9}
    with pytest.raises(AccountingFailure):
        validate_result(rejected, _profile_with(cap, 8))


def test_binary_boundary_fixture() -> None:
    accepted = {"version": 1, "records": [], "binary": "eHh4eHh4eHg="}
    assert validate_result(accepted, _profile_with("binary_bytes", 8)) == accepted
    rejected = {"version": 1, "records": [], "binary": "eHh4eHh4eHh4"}
    with pytest.raises(AccountingFailure):
        validate_result(rejected, _profile_with("binary_bytes", 8))


def test_request_byte_boundary_is_pre_spawn() -> None:
    accepted = {"payload": "x"}
    size = len(_frame(accepted, 1 << 20)) - 4
    assert _frame(accepted, size)
    with pytest.raises(RunnerFailure):
        _frame(accepted, size - 1)


def test_overlimit_request_never_opens_pipe_or_launches(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe", lambda: calls.__setitem__("pipe", 1)
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: calls.__setitem__("popen", 1),
    )
    with pytest.raises(RunnerFailure):
        _run_request(
            {"version": 1, "kind": "valid", "token": "x" * 64, "probe": True},
            _profile_with("request_bytes", 1),
        )
    assert calls == {"pipe": 0, "popen": 0}


def test_missing_private_token_never_opens_pipe_or_launches(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe", lambda: calls.__setitem__("pipe", 1)
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: calls.__setitem__("popen", 1),
    )
    with pytest.raises(RunnerFailure, match="request token rejected"):
        _run_request({"version": 1, "kind": "valid", "probe": True})
    assert calls == {"pipe": 0, "popen": 0}


def test_launch_failure_closes_both_raw_pipe_descriptors(monkeypatch: pytest.MonkeyPatch) -> None:
    import tools.cycle3_characterize.runner as runner

    real_pipe = runner.os.pipe
    descriptors: tuple[int, int] | None = None

    def record_pipe() -> tuple[int, int]:
        nonlocal descriptors
        descriptors = real_pipe()
        return descriptors

    monkeypatch.setattr(runner.os, "pipe", record_pipe)
    monkeypatch.setattr(
        runner.subprocess, "Popen", lambda *a, **k: (_ for _ in ()).throw(OSError("blocked"))
    )
    with pytest.raises(RunnerFailure, match="worker launch rejected"):
        _run_request({"version": 1, "kind": "valid", "token": "x" * 64, "probe": True})
    assert descriptors is not None
    for descriptor in descriptors:
        with pytest.raises(OSError):
            os.fstat(descriptor)


def test_malformed_binding_forms_are_stable_runner_failures(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    with pytest.raises(RunnerFailure):
        verify_launch_identity(_binding_data=[])
    real_read_text = Path.read_text

    def malformed_read_text(path: Path, *args: object, **kwargs: object) -> str:
        if path == BINDING:
            return "{"
        return real_read_text(path, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", malformed_read_text)
    with pytest.raises(RunnerFailure):
        verify_launch_identity()


def test_input_sample_boundary_is_rejected_before_any_spawn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from tools.cycle3_characterize.runner import _verify_provenance

    files = list(_verify_provenance()["uart"])
    request = {
        "version": 1,
        "decoder": "uart",
        "files": files,
        "samplerate": 1,
        "channels": [0, 255],
        "options": {},
    }
    spawned = 0
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("spawned")),
    )
    request["samples"] = [0] * load_caps()["input_samples"]
    assert _request_for_characterization(request)["samples"] == request["samples"]
    request["samples"] = [0] * (load_caps()["input_samples"] + 1)
    with pytest.raises(RunnerFailure):
        _request_for_characterization(request)
    assert spawned == 0


def test_encoded_protocol_boundary_is_parent_framed_limit() -> None:
    value = {"version": 1, "records": [], "text": "x"}
    raw = _frame(value, 1 << 20)
    profile = _profile_with("encoded_bytes", len(raw) - 4)
    assert _parse_result(raw, profile) == value
    with pytest.raises(RunnerFailure):
        _parse_result(raw, _profile_with("encoded_bytes", len(raw) - 5))


def test_decoded_and_retained_boundaries_have_no_partial_result() -> None:
    value = {"version": 1, "records": [], "text": "x" * 32}
    encoded = len(json.dumps(value, separators=(",", ":")).encode())
    assert validate_result(value, _profile_with("decoded_bytes", encoded)) == value
    with pytest.raises(AccountingFailure):
        validate_result(value, _profile_with("decoded_bytes", encoded - 1))
    retained = deep_size(value)
    assert validate_result(value, _profile_with("retained_result_bytes", retained)) == value
    with pytest.raises(AccountingFailure):
        validate_result(value, _profile_with("retained_result_bytes", retained - 1))


def test_nested_item_boundary_fixture() -> None:
    accepted = {"version": 1, "records": [0]}
    items = 4
    assert validate_result(accepted, _profile_with("nested_items", items)) == accepted
    with pytest.raises(AccountingFailure):
        validate_result(accepted, _profile_with("nested_items", items - 1))


def test_binding_covers_closed_source_set() -> None:
    verify_launch_identity()
    binding = json.loads(BINDING.read_text(encoding="utf-8"))
    assert binding["accepted_fixture"] == {
        "candidate_commit": FIXTURE_CANDIDATE_COMMIT,
        "candidate_tree": FIXTURE_CANDIDATE_TREE,
        "caps_sha256": CAPS_SHA256,
        "semantic_fixture_sha256": SEMANTIC_FIXTURE_SHA256,
        "manifest_sha256": FIXTURE_MANIFEST_SHA256,
    }


@pytest.mark.parametrize(
    "variant",
    [
        "missing",
        "extra",
        "digest",
        "schema",
        "fixture_candidate",
        "fixture_caps",
        "fixture_manifest",
        "fixture_semantic",
        "traversal",
        "ordinary",
    ],
)
def test_hostile_binding_path_is_rejected_pre_spawn(
    monkeypatch: pytest.MonkeyPatch, variant: str
) -> None:
    payload = json.loads(BINDING.read_text(encoding="utf-8"))
    sources = payload["sources"]
    first = next(iter(sources))
    if variant == "missing":
        sources.pop(first)
    elif variant == "extra":
        sources["unexpected.py"] = "0" * 64
    elif variant == "digest":
        sources[first] = "0" * 64
    elif variant == "schema":
        payload["schema"] = "bad"
    elif variant == "fixture_candidate":
        payload["accepted_fixture"]["candidate_commit"] = "0" * 40
    elif variant == "fixture_caps":
        payload["accepted_fixture"]["caps_sha256"] = "0" * 64
    elif variant == "fixture_manifest":
        payload["accepted_fixture"]["manifest_sha256"] = "0" * 64
    elif variant == "fixture_semantic":
        payload["accepted_fixture"]["semantic_fixture_sha256"] = "0" * 64
    elif variant == "traversal":
        sources["../escape.py"] = "0" * 64
    elif variant == "ordinary":
        payload["sources"] = "not-a-dict"
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe", lambda: calls.__setitem__("pipe", 1)
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: calls.__setitem__("popen", 1),
    )
    with pytest.raises(RunnerFailure):
        verify_launch_identity(_binding_data=payload)
    assert calls == {"pipe": 0, "popen": 0}


@pytest.mark.parametrize(
    "hostile", ["shadow.py", "shadow.pyc", "__pycache__", "package", "module.so"]
)
def test_tool_inventory_rejects_importable_shadow_before_spawn(
    tmp_path: Path, hostile: str
) -> None:
    allowed = {
        "__init__.py",
        "accounting.py",
        "binding.py",
        "candidate-binding.json",
        "launch.json",
        "probes.py",
        "runner.py",
        "worker.py",
    }
    for name in allowed:
        (tmp_path / name).write_text("", encoding="utf-8")
    target = tmp_path / hostile
    if "." in hostile:
        target.write_text("", encoding="utf-8")
    else:
        target.mkdir()
    with pytest.raises(RunnerFailure):
        _verify_tool_inventory(tmp_path)


def test_safe_file_rejects_outside_and_symlink_variants(tmp_path: Path) -> None:
    root = tmp_path / "root"
    root.mkdir()
    outside = tmp_path / "outside.py"
    outside.write_text("", encoding="utf-8")
    assert not _safe_file(outside, root)
    linked = root / "linked.py"
    linked.symlink_to(outside)
    assert not _safe_file(linked, root)
    directory = root / "dir"
    directory.symlink_to(tmp_path, target_is_directory=True)
    assert not _safe_file(directory / "outside.py", root)


def test_child_environment_does_not_forward_hostile_ambient_values(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in ("PYTHONPATH", "PYTHONHOME", "PYTHONUSERBASE", "CUSTOM_HOSTILE"):
        monkeypatch.setenv(name, "hostile")
    caps = private_test_profile({"request_bytes": 1})
    environment = _child_environment(19, caps, "token")
    assert environment == {
        "PATH": os.defpath,
        "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONPATH": "",
        "CYCLE3_PROTOCOL_FD": "19",
        "CYCLE3_ADDRESS_SPACE": str(caps["worker_address_space_bytes"]),
        "CYCLE3_RECURSION": str(caps["recursion_limit"]),
        "CYCLE3_INTERNAL_PROBE_TOKEN": "token",
    }


def test_popen_spec_is_fixed_independent_of_caller_cwd(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    caps = private_test_profile({"request_bytes": 1})
    spec = _popen_spec(23, caps, "token")
    assert spec["args"] == [os.sys.executable, "-I", "-B", "worker.py"]
    assert spec["cwd"] == TOOL
    assert spec["env"] == _child_environment(23, caps, "token")
    assert spec["pass_fds"] == (23,)
    assert spec["close_fds"] is True and spec["shell"] is False


def test_two_isolated_bytecode_probe_launches_leave_inventory_clean() -> None:
    first = run_internal_probe("bytecode")
    second = run_internal_probe("bytecode")
    expected = {"dont_write_bytecode": True, "probes": True}
    assert json.loads(first.diagnostics) == expected
    assert json.loads(second.diagnostics) == expected
    _verify_tool_inventory()


@pytest.mark.parametrize(
    "field",
    [
        "schema",
        "executable",
        "arguments",
        "environment",
        "working_directory",
        "import_roots",
        "stdlib_allowlist",
        "request_version",
        "protocol_fd",
        "characterization_probe_mode",
        "source_allowlist",
    ],
)
def test_each_launch_field_mutation_is_rejected_pre_spawn(
    field: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    launch = json.loads((TOOL / "launch.json").read_text(encoding="utf-8"))
    launch[field] = None
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe", lambda: calls.__setitem__("pipe", 1)
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: calls.__setitem__("popen", 1),
    )
    with pytest.raises(RunnerFailure):
        _validate_launch_document(launch)
    assert calls == {"pipe": 0, "popen": 0}


@pytest.mark.parametrize("mutation", ["missing", "extra", "non_dict"])
def test_launch_shape_mutations_are_rejected_pre_spawn(
    mutation: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    launch: object = json.loads((TOOL / "launch.json").read_text(encoding="utf-8"))
    if mutation == "missing":
        launch.pop("schema")
    elif mutation == "extra":
        launch["extra"] = True
    else:
        launch = []
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe", lambda: calls.__setitem__("pipe", 1)
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: calls.__setitem__("popen", 1),
    )
    with pytest.raises(RunnerFailure):
        _validate_launch_document(launch)
    assert calls == {"pipe": 0, "popen": 0}


def test_valid_inert_child_uses_separate_protocol_and_reaps() -> None:
    result = run_internal_probe("valid")
    assert result.value["records"] == []
    assert result.stdout == result.stderr == result.diagnostics == b""
    assert result.launch_ns >= 0 and result.reap_ns >= 0 and result.total_ns >= result.launch_ns
    assert result.counts == {
        **result_measurements(result.value),
        "input_samples": 0,
        "request_bytes": result.counts["request_bytes"],
        "stdout_bytes": 0,
        "stderr_bytes": 0,
    }
    evidence = _private_last_evidence()
    assert evidence.disposition == "completed"
    assert evidence.reaped and evidence.descriptors_closed and len(evidence.closed_fds) == 2


def test_worker_reads_back_exact_recursion_and_address_space_limits() -> None:
    result = run_internal_probe("limits")
    limits = json.loads(result.diagnostics)
    caps = load_caps()
    assert limits == {
        "recursion": caps["recursion_limit"],
        "soft": caps["worker_address_space_bytes"],
        "hard": caps["worker_address_space_bytes"],
    }


def test_worker_cannot_raise_the_exact_address_space_hard_cap() -> None:
    result = run_internal_probe("raise_address_space")
    assert json.loads(result.diagnostics) == {"rejected": True}


def test_exact_address_space_overreservation_is_rejected_without_touching_pages() -> None:
    result = run_internal_probe("address_space_over")
    assert result.stdout == b"address-space-start\n"
    assert result.diagnostics in {b"OSError", b"ValueError", b"MemoryError"}
    assert run_internal_probe("valid").value["version"] == 1


def test_worker_recursion_overrun_is_rejected_and_recovery_is_clean() -> None:
    with pytest.raises(RunnerFailure):
        run_internal_probe("recursion_over")
    assert run_internal_probe("valid").value["version"] == 1


@pytest.mark.parametrize("probe", ["hang", "ignore_term"])
def test_deadline_cleanup_then_recovery_for_graceful_and_forced_termination(probe: str) -> None:
    with pytest.raises(RunnerFailure):
        run_internal_probe(probe)
    evidence = _private_last_evidence()
    assert evidence.reaped and evidence.descriptors_closed
    assert len(evidence.closed_fds) == 2
    expected = "killed-and-reaped" if probe == "ignore_term" else "terminated-and-reaped"
    assert evidence.disposition == expected
    assert evidence.total_ns > 0 and evidence.terminate_to_reap_ns > 0
    if probe == "ignore_term":
        assert evidence.kill_to_reap_ns > 0
    else:
        assert evidence.kill_to_reap_ns == 0
    with pytest.raises(ProcessLookupError):
        os.kill(evidence.pid, 0)
    assert run_internal_probe("valid").value["records"] == []


def test_small_private_deadline_is_enforced_by_an_actual_child() -> None:
    profile = private_test_profile({"wall_deadline_ms": 200, "terminate_grace_ms": 20})
    with pytest.raises(RunnerFailure):
        run_internal_probe("hang", _profile=profile)
    assert run_internal_probe("valid", _profile=profile).value["version"] == 1


@pytest.mark.parametrize(
    ("probe", "cap", "limit"),
    [
        ("stdout_flood", "stdout_bytes", 1),
        ("stderr_flood", "stderr_bytes", 1),
        ("diagnostic_flood", "diagnostic_bytes", 1),
        ("text_cap", "text_bytes", 1),
        ("binary_cap", "binary_bytes", 1),
        ("deep", "nested_depth", 4),
        ("items", "output_records", 1),
        ("nested_items", "nested_items", 6),
    ],
)
def test_small_private_profile_enforces_child_output_cap(probe: str, cap: str, limit: int) -> None:
    profile = private_test_profile({cap: limit})
    with pytest.raises(RunnerFailure):
        run_internal_probe(probe, _profile=profile)
    assert run_internal_probe("valid", _profile=profile).value["records"] == []


_MINIMAL_RESULT = {
    "version": 1,
    "records": [],
    "text": "",
    "binary": "",
    "diagnostics": "",
}


@pytest.mark.parametrize(
    ("cap", "limit"),
    [
        ("encoded_bytes", len(json.dumps(_MINIMAL_RESULT, separators=(",", ":")).encode())),
        ("decoded_bytes", len(json.dumps(_MINIMAL_RESULT, separators=(",", ":")).encode())),
        ("retained_result_bytes", deep_size(_MINIMAL_RESULT)),
    ],
)
def test_actual_child_enforces_result_size_caps_and_recovers(cap: str, limit: int) -> None:
    profile = private_test_profile({cap: limit})
    with pytest.raises(RunnerFailure):
        run_internal_probe("large_result", _profile=profile)
    evidence = _private_last_evidence()
    assert evidence.reaped and evidence.descriptors_closed
    assert run_internal_probe("valid", _profile=profile).value == _MINIMAL_RESULT


@pytest.mark.parametrize("cap", sorted(CAP_IDS))
def test_private_profile_rejects_unknown_or_nonpositive_caps(cap: str) -> None:
    values = load_caps()
    values[cap] = 0
    with pytest.raises(AccountingFailure):
        CapProfile(values)


@pytest.mark.parametrize(
    "probe",
    [
        "partial",
        "extra",
        "nonfinite",
        "malformed",
        "hang",
        "ignore_term",
        "stdout_flood",
        "stderr_flood",
        "diagnostic_flood",
        "deep",
        "items",
        "unknown",
        "base64",
    ],
)
def test_hostile_inventory_is_closed(probe: str) -> None:
    assert probe in PROBES


@pytest.mark.parametrize("probe", ["text_cap", "binary_cap", "nested_items", "large_result"])
def test_boundary_probe_inventory_is_closed(probe: str) -> None:
    assert probe in PROBES


@pytest.mark.parametrize(
    "probe",
    [
        "partial",
        "extra",
        "nonfinite",
        "malformed",
        "stdout_flood",
        "stderr_flood",
        "diagnostic_flood",
        "deep",
        "items",
        "unknown",
        "base64",
    ],
)
def test_hostile_child_is_discarded_and_next_child_recovers(probe: str) -> None:
    with pytest.raises(RunnerFailure):
        run_internal_probe(probe)
    evidence = _private_last_evidence()
    assert evidence.reaped and evidence.descriptors_closed and len(evidence.closed_fds) == 2
    assert run_internal_probe("valid").value["version"] == 1


def test_bounded_stdout_and_stderr_are_separate_from_protocol() -> None:
    stdout = run_internal_probe("stdout_noise")
    assert stdout.stdout == b"unexpected" and stdout.stderr == stdout.diagnostics == b""
    stderr = run_internal_probe("stderr")
    assert stderr.stderr == b"unexpected" and stderr.stdout == stderr.diagnostics == b""


def test_real_characterization_is_structurally_bound_and_disabled() -> None:
    with pytest.raises(RunnerFailure, match="disabled pending runner gate"):
        characterize(_closed_request())


def test_result_rejects_invalid_base64_without_partial_value() -> None:
    profile = CapProfile(load_caps())
    with pytest.raises(AccountingFailure):
        validate_result({"version": 1, "records": [], "binary": "*"}, profile)


def test_tool_imports_no_decoder_surface() -> None:
    forbidden = {"sigrokdecode", "semantic_fixtures", "typed_vectors", "generate_cycle3_fixtures"}
    for path in TOOL.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        imported = {
            name.name.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for name in node.names
        }
        imported.update(
            node.module.split(".")[0]
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom) and node.module
        )
        assert not imported & forbidden
        dynamic_imports = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "__import__"
        ]
        if dynamic_imports:
            assert path.name == "worker.py"
            assert len(dynamic_imports) == 2
            arguments = [call.args[0] for call in dynamic_imports]
            assert all(isinstance(argument, ast.Constant) for argument in arguments)
            assert [argument.value for argument in arguments] == ["snapshot_host", "probes"]


def _closed_request(decoder: str = "uart") -> dict[str, object]:
    return {
        "version": 1,
        "decoder": decoder,
        "files": list(DECODER_PATHS[decoder]),
        "samplerate": 1,
        "channels": {"uart": [0, 255], "spi": [0, 1, 255, 255], "i2c": [0, 1]}[decoder],
        "samples": [0],
        "options": {},
    }


@pytest.mark.parametrize("decoder", ["uart", "spi", "i2c"])
def test_closed_validator_accepts_minimal_each_decoder(decoder: str) -> None:
    assert validate_characterization_request(_closed_request(decoder))["decoder"] == decoder


@pytest.mark.parametrize(
    "field,value",
    [("version", 2), ("files", []), ("samplerate", 0), ("samples", []), ("samples", [True])],
)
def test_closed_validator_rejects_shape_and_sample_families(field: str, value: object) -> None:
    request = _closed_request()
    request[field] = value
    with pytest.raises(SnapshotHostFailure):
        validate_characterization_request(request)


@pytest.mark.parametrize("channels", [[0], [0, 0], [255, 255], [0, 256]])
def test_closed_validator_rejects_uart_mapping_families(channels: list[int]) -> None:
    request = _closed_request()
    request["channels"] = channels
    with pytest.raises(SnapshotHostFailure):
        validate_characterization_request(request)


@pytest.mark.parametrize(
    "options",
    [
        {"baudrate": 0},
        {"data_bits": 4},
        {"parity": "bad"},
        {"stop_bits": 3.0},
        {"sample_point": 100},
        {"rx_packet_delim": 256},
        {"rx_packet_len": 0},
        {"invert_rx": True},
    ],
)
def test_closed_validator_rejects_uart_option_families(options: dict[str, object]) -> None:
    request = _closed_request()
    request["options"] = options
    with pytest.raises(SnapshotHostFailure):
        validate_characterization_request(request)


@pytest.mark.parametrize(
    "decoder,options",
    [
        ("spi", {"wordsize": 9}),
        ("spi", {"cpol": True}),
        ("spi", {"bitorder": "bad"}),
        ("i2c", {"address_format": "bad"}),
    ],
)
def test_closed_validator_rejects_spi_i2c_option_families(
    decoder: str, options: dict[str, object]
) -> None:
    request = _closed_request(decoder)
    request["options"] = options
    with pytest.raises(SnapshotHostFailure):
        validate_characterization_request(request)


def test_closed_validator_matches_every_accepted_option_matrix_row() -> None:
    matrix = json.loads(
        (ROOT / "testdata/decoders/cycle3/option-matrix.json").read_text(encoding="utf-8")
    )
    accepted = [row for row in matrix["rows"] if row["disposition"] == "direct-fixture"]
    assert len(accepted) == 62
    for row in accepted:
        request = _closed_request(row["decoder"])
        options = dict(row.get("selected_width_context") or {})
        options[row["option"]] = row["value"]
        request["options"] = options
        assert validate_characterization_request(request)["options"] == options, row["id"]


def test_closed_validator_rejects_every_unsupported_option_matrix_row() -> None:
    matrix = json.loads(
        (ROOT / "testdata/decoders/cycle3/option-matrix.json").read_text(encoding="utf-8")
    )
    unsupported = [row for row in matrix["rows"] if row["disposition"] == "unsupported"]
    assert len(unsupported) == 103
    for row in unsupported:
        request = _closed_request(row["decoder"])
        options = dict(row.get("selected_width_context") or {})
        options[row["option"]] = row["value"]
        request["options"] = options
        with pytest.raises(SnapshotHostFailure, match="options rejected"):
            validate_characterization_request(request)


def test_parent_rejects_invalid_request_before_pipe_or_popen(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = {"pipe": 0, "popen": 0}
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.os.pipe", lambda: calls.__setitem__("pipe", 1)
    )
    monkeypatch.setattr(
        "tools.cycle3_characterize.runner.subprocess.Popen",
        lambda *a, **k: calls.__setitem__("popen", 1),
    )
    with pytest.raises(RunnerFailure):
        _request_for_characterization({**_closed_request(), "probe": True})
    assert calls == {"pipe": 0, "popen": 0}


def test_nested_tagged_binary_is_bounded_and_not_text() -> None:
    value = {"version": 1, "records": [{"$cycle3_bytes": "eHg=", "length": 2}]}
    assert validate_result(value, _profile_with("binary_bytes", 2)) == value
    assert validate_result(value, _profile_with("text_bytes", 1)) == value
    assert (
        validate_result(
            {"version": 1, "records": [], "binary": "eHg="}, _profile_with("text_bytes", 1)
        )["binary"]
        == "eHg="
    )
    with pytest.raises(AccountingFailure):
        validate_result(
            {"version": 1, "records": [{"$cycle3_bytes": "eHg=", "length": 2}]},
            _profile_with("binary_bytes", 1),
        )
    for bad in ({"$cycle3_bytes": "*", "length": 1}, {"$cycle3_bytes": "eA==", "length": 2}):
        with pytest.raises(AccountingFailure):
            validate_result({"version": 1, "records": [bad]}, _profile_with("binary_bytes", 8))


def test_binary_usage_is_aggregate_and_only_transport_base64_is_not_text() -> None:
    combined = {
        "version": 1,
        "records": [{"$cycle3_bytes": "eA==", "length": 1}],
        "binary": "eA==",
    }
    assert result_measurements(combined)["binary_bytes"] == 2
    with pytest.raises(AccountingFailure):
        validate_result(combined, _profile_with("binary_bytes", 1))
    semantic_key = {"version": 1, "records": [{"binary": "xx"}]}
    assert result_measurements(semantic_key)["text_bytes"] == 2


def test_capture_api_is_deterministic_without_decoder() -> None:
    capture = _Capture([0, 255], [0, 1, 1])
    capture.owner = type("Owner", (), {})()
    assert capture.HasChannel(0) and not capture.HasChannel(1)
    assert capture.Wait({}) == (0, 255) and capture.owner.samplenum == 0
    assert capture.Wait({"skip": 0}) == (0, 255)
    assert capture.Wait({"0": "r"}) == (1, 255) and capture.owner.matched == (True,)
    assert capture.Wait({"0": "f"}) is None
    output = capture.Register(2, int)
    capture.Put(0, 1, output, b"x")
    assert capture.records[0]["output"]["meta"] == {"$cycle3_type": "int"}
    with pytest.raises(SnapshotHostFailure):
        capture.Put(0, 1, 99, [])


def test_capture_mixed_skip_edge_and_terminal_semantics_without_decoder() -> None:
    owner = type("Owner", (), {})()
    capture = _Capture([0, 1], [0b10, 0b10, 0b11, 0b11, 0b10])
    capture.owner = owner
    assert capture.Wait({}) == (0, 1)
    assert capture.Wait([{"skip": 3}, {"0": "r"}]) == (1, 1)
    assert owner.samplenum == 2 and owner.matched == (False, True)
    assert capture.Wait([{"skip": 2}, {"0": "f"}]) == (0, 1)
    assert owner.samplenum == 4 and owner.matched == (True, True)
    assert capture.Wait({"0": "r"}) is None
    assert owner.samplenum == 5 and owner.matched == (False,)


def test_capture_empty_wait_advances_and_put_uses_half_open_capture_end() -> None:
    owner = type("Owner", (), {})()
    capture = _Capture([0], [0, 1])
    capture.owner = owner
    assert capture.Wait({}) == (0,)
    assert capture.Wait({}) == (1,)
    output = capture.Register(1, None)
    capture.Put(0, len(capture.samples), output, ["complete"])
    assert capture.records == [
        {
            "start_sample": 0,
            "end_sample": 2,
            "output_id": 0,
            "output": {"type": 1, "meta": None},
            "value": ["complete"],
        }
    ]
    for interval in ((-1, 0), (1, 0), (0, 3)):
        with pytest.raises(SnapshotHostFailure):
            capture.Put(*interval, output, [])


def test_metric_formatter_is_deterministic_for_inert_records() -> None:
    rendered = format_metrics(
        input_samples=2,
        registrations={0: {"type": 2}},
        records=[{"output": {"type": 2}}],
        load_ns=1,
        import_ns=2,
        decode_ns=3,
        maxrss=4,
        address_space=(5, 6),
        recursion=7,
    )
    assert json.loads(rendered) == {
        "address_space": [5, 6],
        "decode_ns": 3,
        "import_ns": 2,
        "input_samples": 2,
        "load_ns": 1,
        "maxrss": 4,
        "output_type_counts": {"2": 1},
        "record_count": 1,
        "recursion": 7,
        "registration_count": 1,
    }
