from __future__ import annotations

from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[4]
WORKFLOWS = REPOSITORY / ".github" / "workflows"
WORKFLOW = WORKFLOWS / "logic-analyzer-python-cycle2.yml"


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
    assert text.count("runs-on: macos-latest") == 1
    assert "runs-on: ubuntu" not in text and "runs-on: windows" not in text

    assert "permissions:\n  contents: read\n" in text
    assert "write-all" not in text and "contents: write" not in text
    assert "secrets." not in text and "pull_request_target:" not in text

    required = (
        "actions/checkout@v4",
        "actions/setup-python@v5",
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
    assert text.count("--tb=short --disable-warnings") == 1
