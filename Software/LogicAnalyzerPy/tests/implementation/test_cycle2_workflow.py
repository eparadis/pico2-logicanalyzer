from __future__ import annotations

import re
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[4]
WORKFLOWS = REPOSITORY / ".github" / "workflows"
WORKFLOW = WORKFLOWS / "logic-analyzer-python-cycle2.yml"
ANNOTATION_PREFIX = "::error title=Cycle 3 non-hardware pytest failure::"
FORCED_KILL_NODE = (
    "tests/implementation/test_c3_b2_private_host.py::"
    "test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure"
)
SECOND_SIGTERM_NODE = (
    "tests/verification/test_c3_b2_private_host_round3.py::"
    "test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation"
)
SETUP_UV_COMMIT = "c771a70e6277c0a99b617c7a806ffedaca235ff9"
EXPECTED_PYTHON_VERSION = (
    "3.12.13 (main, Jun 23 2026, 15:54:40) [Clang 22.1.3 ]"
)

SUPERSEDED_B1_IGNORES = (
    "tests/verification/test_c3_b1_threshold_proposal_round2.py",
    "tests/verification/test_c3_b1_final_candidate.py",
    "tests/verification/test_c3_b1_raw_baseline_candidate.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding.py",
    "tests/verification/test_c3_b1_semantic_fixture_candidate.py",
    "tests/verification/test_c3_b1_threshold_proposal_round3.py",
    "tests/verification/test_c3_b1_preexecution_runner_candidate.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py",
    "tests/verification/test_c3_b1_final_candidate_round3.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py",
    "tests/verification/test_c3_b1_semantic_fixture_correction_round2.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round2.py",
    "tests/verification/test_c3_b1_runner_fixture_rebinding_round3.py",
    "tests/verification/test_c3_b1_threshold_proposal.py",
    "tests/verification/test_c3_b1_semantic_fixture_correction.py",
)
ACCEPTED_DESELECTS = (
    (
        "tests/implementation/test_cycle3_fixtures.py::"
        "test_cycle3_fixture_surface_is_present_and_rebuildable"
    ),
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_candidate_binding_and_exact_workflow_digest"
    ),
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order"
    ),
    FORCED_KILL_NODE,
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_candidate_binding_and_exact_workflow_digest"
    ),
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_partition_has_exact_ordered_unique_ignores_and_deselections"
    ),
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_every_candidate_b2_b3_b4_module_is_retained"
    ),
    (
        "tests/verification/test_c3_b4_public_round5.py::"
        "test_partition_is_the_only_workflow_change_from_round4"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_candidate_tree_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_runner_guard_and_every_other_gate_byte_are_preserved"
    ),
    SECOND_SIGTERM_NODE,
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_candidate_tree_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_redaction_log_status_and_no_retry_are_byte_preserved"
    ),
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases"
    ),
    (
        "tests/verification/test_c3_b4_public_round7.py::"
        "test_second_sigterm_node_remains_selected_and_passes"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_focused_gate_is_once_no_retry_and_broad_only_on_success"
    ),
    (
        "tests/verification/test_c3_b4_public_round8.py::"
        "test_candidate_tree_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round8.py::"
        "test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged"
    ),
    (
        "tests/verification/test_c3_b4_public_round8.py::"
        "test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases"
    ),
    (
        "tests/verification/test_c3_b4_public_round4.py::"
        "test_official_intel_label_and_guard_are_first_and_prebootstrap"
    ),
    (
        "tests/verification/test_c3_b4_public_round6.py::"
        "test_full_history_checkout_and_job_wide_no_bytecode_precede_python_steps"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_candidate_tree_failed_evidence_and_workflow_digest_are_exact"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_setup_python_is_exact_31213_once_before_both_clean_environments"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_only_python_pin_and_three_round8_selectors_change_workflow_bytes"
    ),
    (
        "tests/verification/test_c3_b4_public_round9.py::"
        "test_partition_is_exact_ordered_twenty_selectors_twenty_one_cases"
    ),
)
MANDATORY_CURRENT_MODULES = (
    "tests/implementation/test_c3_b2_private_host.py",
    "tests/verification/test_c3_b2_private_host.py",
    "tests/verification/test_c3_b2_private_host_round2.py",
    "tests/verification/test_c3_b2_private_host_round3.py",
    "tests/verification/test_c3_b2_private_host_round4.py",
    "tests/implementation/test_c3_b3_cross_source_equivalence.py",
    "tests/implementation/test_c3_b3_uart_conformance.py",
    "tests/implementation/test_c3_b3_spi_conformance.py",
    "tests/implementation/test_c3_b3_i2c_conformance.py",
    "tests/verification/test_c3_b3_cross_source_equivalence.py",
    "tests/verification/test_c3_b3_uart_conformance.py",
    "tests/verification/test_c3_b3_spi_conformance.py",
    "tests/verification/test_c3_b3_i2c_conformance.py",
    "tests/implementation/test_c3_b4_public.py",
    "tests/verification/test_c3_b4_public_round1.py",
    "tests/verification/test_c3_b4_public_round2.py",
    "tests/verification/test_c3_b4_public_round3.py",
    "tests/verification/test_c3_b4_public_round4.py",
    "tests/verification/test_c3_b4_public_round5.py",
    "tests/verification/test_c3_b4_public_round6.py",
    "tests/verification/test_c3_b4_public_round7.py",
    "tests/verification/test_c3_b4_public_round8.py",
    "tests/verification/test_c3_b4_public_round9.py",
)


def _github_escape(value: str) -> str:
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def test_failure_annotation_is_bounded_and_retains_the_final_summary() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count('LC_ALL=C tail -c 1300 "$1"') == 1
    assert "tail -c 12000" not in text

    worst_case_report = "%" * 1300
    worst_case_command = f"{ANNOTATION_PREFIX}{_github_escape(worst_case_report)}\n"
    assert len(worst_case_command.encode("ascii")) == 3952
    assert len(worst_case_command.encode("ascii")) <= 4096

    summary = (
        "FAILED tests/verification/test_hidden.py::test_exact_hidden_failure - "
        "AssertionError\n1 failed in 360.00s\n"
    )
    captured_log = ("discarded progress line\n" * 200) + summary
    bounded_report = captured_log.encode("ascii")[-1300:].decode("ascii")
    assert bounded_report.endswith(summary)
    assert summary in bounded_report


def test_cycle2_workflow_is_single_macos_dispatchable_and_complete() -> None:
    active = sorted(
        path for path in WORKFLOWS.iterdir() if path.is_file() and path.suffix in {".yml", ".yaml"}
    )
    assert active == [WORKFLOW]
    text = WORKFLOW.read_text(encoding="utf-8")
    lines = text.splitlines()

    assert "  workflow_dispatch:\n" in text
    assert text.count("  push:\n") == 1 and text.count("  pull_request:\n") == 1
    expected_paths = (
        '    paths: ["Software/LogicAnalyzerPy/**", '
        '".github/workflows/logic-analyzer-python-cycle2.yml"]\n'
    )
    assert text.count(expected_paths) == 2
    top_level = [line.removesuffix(":") for line in lines if line and not line.startswith(" ")]
    assert top_level == ["name: Logic analyzer Python Cycle 2", "on", "permissions", "jobs"]
    on_block = lines[lines.index("on:") + 1 : lines.index("permissions:")]
    assert [line.strip() for line in on_block if line.strip().endswith(":")] == [
        "workflow_dispatch:",
        "push:",
        "pull_request:",
    ]
    assert text.count("runs-on: macos-15-intel") == 1
    assert "runs-on: macos-latest" not in text
    assert "runs-on: ubuntu" not in text and "runs-on: windows" not in text

    architecture_check = "Verify governed macOS x86_64 runner"
    assert text.count(architecture_check) == 1
    assert text.count('architecture="$(uname -m)"') == 1
    assert text.count('if [ "$architecture" != "x86_64" ]; then') == 1
    assert text.index(architecture_check) < text.index("actions/checkout@v4")

    checkout = (
        "      - uses: actions/checkout@v4\n"
        "        with:\n"
        "          fetch-depth: 0\n"
    )
    assert text.count(checkout) == 1

    job_environment = (
        "    env:\n"
        '      PYTHONDONTWRITEBYTECODE: "1"\n'
        "      UV_CACHE_DIR: ${{ github.workspace }}/.tmp/c3-b4-ci/uv-cache\n"
        "      UV_PYTHON_INSTALL_DIR: ${{ github.workspace }}/.tmp/c3-b4-ci/uv-python\n"
        "      PICO_LA_PYTHON: ${{ github.workspace }}/.tmp/c3-b4-ci/uv-python/"
        "cpython-3.12.13-macos-x86_64-none/bin/python3.12\n"
        f'      PICO_LA_EXPECTED_PYTHON: "{EXPECTED_PYTHON_VERSION}"\n'
        "    steps:\n"
    )
    assert text.count(job_environment) == 1

    exact_uv = (
        f"      - uses: astral-sh/setup-uv@{SETUP_UV_COMMIT} # v9.0.0\n"
        "        with:\n"
        '          version: "0.12.6"\n'
        "          enable-cache: false\n"
    )
    install_and_guard = (
        "      - name: Install and verify accepted managed CPython 3.12.13\n"
        "        shell: bash\n"
        "        run: |\n"
        "          uv python install 3.12.13 --no-bin\n"
        "          \"$PICO_LA_PYTHON\" -c 'import os, platform, sys; from pathlib import Path; "
        'assert sys.version == os.environ["PICO_LA_EXPECTED_PYTHON"]; '
        'assert platform.machine() == "x86_64"; '
        'assert sys.base_prefix.endswith("/cpython-3.12.13-macos-x86_64-none"); '
        'assert (Path(sys.base_prefix) / "BUILD").read_text() == "20260623"\'\n'
    )
    core_venv = (
        "      - name: Create clean core Python 3.12 environment\n"
        "        working-directory: Software/LogicAnalyzerPy\n"
        "        run: |\n"
        '          "$PICO_LA_PYTHON" -m venv .venv\n'
        "          .venv/bin/python -c 'import os, platform, sys; "
        'assert sys.version == os.environ["PICO_LA_EXPECTED_PYTHON"]; '
        'assert platform.machine() == "x86_64"\'\n'
    )
    web_venv = core_venv.replace("core", "web-runtime").replace(".venv", ".venv-web")
    assert text.count(exact_uv) == 1
    assert text.count(install_and_guard) == 1
    assert text.count(core_venv) == 1
    assert text.count(web_venv) == 1
    assert "actions/setup-python" not in text
    assert "python-version:" not in text
    assert "run: python -m venv" not in text
    assert text.index(job_environment) < text.index(exact_uv)
    assert text.index("actions/checkout@v4") < text.index(exact_uv)
    assert text.index(exact_uv) < text.index(install_and_guard)
    assert text.index(install_and_guard) < text.index("actions/setup-node@v4")
    assert text.index(core_venv) < text.index("requirements-dev.lock")
    assert text.index(web_venv) < text.index("requirements-web.lock")

    assert "permissions:\n  contents: read\n" in text
    assert "write-all" not in text and "contents: write" not in text
    assert "secrets." not in text and "pull_request_target:" not in text

    required = (
        "actions/checkout@v4",
        f"astral-sh/setup-uv@{SETUP_UV_COMMIT}",
        "actions/setup-node@v4",
        "pip install --require-hashes -r requirements-dev.lock",
        "pip install --no-build-isolation --no-deps -e .",
        "python -m pip check",
        "python -m ruff check .",
        "python -m mypy src",
        'python -m pytest -m "not hardware" --tb=short --disable-warnings',
        "workflow sanitizer self-test failed",
        "requirements-web.lock",
        "npm ci --no-audit --no-fund",
        "npm run lint",
        "npm run typecheck",
        "npm test -- --run",
        "npm run build",
        "scripts/check_web_assets.py",
        "npx playwright install chromium",
        "npm run test:browser",
    )
    assert all(fragment in text for fragment in required)
    assert text.count("--tb=short --disable-warnings") == 2

    focused_command = (
        "            .venv/bin/python -m pytest -q \\\n"
        f"              {FORCED_KILL_NODE} \\\n"
        f"              {SECOND_SIGTERM_NODE} \\\n"
        "              --tb=short --disable-warnings\n"
    )
    focused_gate = (
        "          set +e\n"
        '          : >"$log_file"\n'
        "          (\n"
        "            trap '' TERM\n"
        f"{focused_command}"
        '          ) >>"$log_file" 2>&1\n'
        "          focused_status=$?\n"
        '          if [ "$focused_status" -eq 0 ]; then\n'
    )
    assert text.count(focused_gate) == 1
    assert text.count("focused_status=$?") == 1
    assert text.count("status=$focused_status") == 1
    assert text.index(focused_gate) < text.index(
        '.venv/bin/python -m pytest -m "not hardware" --tb=short --disable-warnings'
    )
    assert text.count(FORCED_KILL_NODE) == 2
    assert text.count(SECOND_SIGTERM_NODE) == 2
    assert text.count(".venv/bin/python -m pytest -q") == 1
    assert 2 + 1 == 3
    assert text.count('>>"$log_file" 2>&1') == 2
    assert text.count('>"$log_file" 2>&1') == 2
    assert text.count(" -m pytest ") == 2
    assert "retry:" not in text.lower()
    assert "for attempt" not in text.lower()
    assert "while " not in text.lower()

    ignores = tuple(re.findall(r"--ignore ([^\s\\]+)", text))
    deselections = tuple(re.findall(r"--deselect ([^\s\\]+)", text))
    assert ignores == SUPERSEDED_B1_IGNORES
    assert deselections == ACCEPTED_DESELECTS
    assert len(set(ignores)) == len(ignores) == 15
    assert len(set(deselections)) == len(deselections) == 26
    assert 25 + 2 == 27
    for relative in MANDATORY_CURRENT_MODULES:
        assert (REPOSITORY / "Software/LogicAnalyzerPy" / relative).is_file()
        assert relative not in ignores
    round4 = "tests/verification/test_c3_b4_public_round4.py"
    assert sum(item.startswith(f"{round4}::") for item in deselections) == 3
    round5 = "tests/verification/test_c3_b4_public_round5.py"
    assert sum(item.startswith(f"{round5}::") for item in deselections) == 4
    round6 = "tests/verification/test_c3_b4_public_round6.py"
    round6_disposed = {
        item.split("::", maxsplit=1)[1]
        for item in deselections
        if item.startswith(f"{round6}::")
    }
    assert round6_disposed == {
        "test_candidate_tree_and_workflow_digest_are_exact",
        "test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases",
        "test_focused_gate_is_once_no_retry_and_broad_only_on_success",
        "test_full_history_checkout_and_job_wide_no_bytecode_precede_python_steps",
        "test_runner_guard_and_every_other_gate_byte_are_preserved",
    }
    round6_source = (REPOSITORY / "Software/LogicAnalyzerPy" / round6).read_text(
        encoding="utf-8"
    )
    round6_nodes = set(re.findall(r"^def (test_[^(]+)\(", round6_source, re.MULTILINE))
    assert len(round6_nodes) == 10
    assert len(round6_nodes - round6_disposed) == 5
    round7 = "tests/verification/test_c3_b4_public_round7.py"
    round7_disposed = {
        item.split("::", maxsplit=1)[1]
        for item in deselections
        if item.startswith(f"{round7}::")
    }
    assert round7_disposed == {
        "test_candidate_tree_and_workflow_digest_are_exact",
        "test_redaction_log_status_and_no_retry_are_byte_preserved",
        "test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases",
        "test_second_sigterm_node_remains_selected_and_passes",
    }
    round7_source = (REPOSITORY / "Software/LogicAnalyzerPy" / round7).read_text(
        encoding="utf-8"
    )
    round7_nodes = set(re.findall(r"^def (test_[^(]+)\(", round7_source, re.MULTILINE))
    assert len(round7_nodes) == 10
    assert len(round7_nodes - round7_disposed) == 6
    round8 = "tests/verification/test_c3_b4_public_round8.py"
    round8_disposed = {
        item.split("::", maxsplit=1)[1]
        for item in deselections
        if item.startswith(f"{round8}::")
    }
    assert round8_disposed == {
        "test_candidate_tree_and_workflow_digest_are_exact",
        "test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged",
        "test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases",
    }
    round8_source = (REPOSITORY / "Software/LogicAnalyzerPy" / round8).read_text(
        encoding="utf-8"
    )
    round8_nodes = set(re.findall(r"^def (test_[^(]+)\(", round8_source, re.MULTILINE))
    assert len(round8_nodes) == 9
    assert len(round8_nodes - round8_disposed) == 6
    round9 = "tests/verification/test_c3_b4_public_round9.py"
    round9_disposed = {
        item.split("::", maxsplit=1)[1]
        for item in deselections
        if item.startswith(f"{round9}::")
    }
    assert round9_disposed == {
        "test_candidate_tree_failed_evidence_and_workflow_digest_are_exact",
        "test_setup_python_is_exact_31213_once_before_both_clean_environments",
        "test_only_python_pin_and_three_round8_selectors_change_workflow_bytes",
        "test_partition_is_exact_ordered_twenty_selectors_twenty_one_cases",
    }
    round9_source = (REPOSITORY / "Software/LogicAnalyzerPy" / round9).read_text(
        encoding="utf-8"
    )
    round9_nodes = set(re.findall(r"^def (test_[^(]+)\(", round9_source, re.MULTILINE))
    assert len(round9_nodes) == 9
    assert len(round9_nodes - round9_disposed) == 5
    assert FORCED_KILL_NODE in deselections
    assert SECOND_SIGTERM_NODE in deselections
    assert FORCED_KILL_NODE.split("::", maxsplit=1)[0] not in ignores
