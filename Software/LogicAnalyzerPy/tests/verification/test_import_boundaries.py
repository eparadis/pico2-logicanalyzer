"""Cycle 1 core package must not gain hardware/UI/CLI dependencies in B2."""

from __future__ import annotations

import ast
from pathlib import Path

_PROJECT_ROOT = Path(__file__).parents[2]
_CORE = _PROJECT_ROOT / "src" / "pico_logic_analyzer"
_FORBIDDEN_ROOTS = {"serial", "PySide6", "PyQt6", "qtpy"}


def test_core_modules_do_not_import_serial_qt_or_cli() -> None:
    violations: list[str] = []
    for path in _CORE.rglob("*.py"):
        if path.name == "__main__.py" or "cli" in path.relative_to(_CORE).parts:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            module = None
            if isinstance(node, ast.Import):
                module = node.names[0].name
            elif isinstance(node, ast.ImportFrom):
                module = node.module
            if module is not None and module.split(".", maxsplit=1)[0] in _FORBIDDEN_ROOTS:
                violations.append(f"{path.relative_to(_PROJECT_ROOT)}:{module}")
            if module is not None and module.startswith("pico_logic_analyzer.cli"):
                violations.append(f"{path.relative_to(_PROJECT_ROOT)}:{module}")
    assert violations == []
