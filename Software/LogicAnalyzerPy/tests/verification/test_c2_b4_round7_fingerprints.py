"""Independent round-seven exhaustive artifact fingerprint verification."""

from __future__ import annotations

import copy
import importlib.util
import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).parents[2]


def _checker() -> object:
    spec = importlib.util.spec_from_file_location("round7_openapi", ROOT / "tools/check_openapi.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _raw_contract() -> tuple[str, str]:
    return (
        (ROOT / "web/openapi.json").read_text(encoding="utf-8"),
        (ROOT / "web/src/api.generated.ts").read_text(encoding="utf-8"),
    )


def _contract() -> tuple[dict[str, Any], str]:
    raw, types = _raw_contract()
    return json.loads(raw), types


def _reversed_mappings(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _reversed_mappings(item) for key, item in reversed(value.items())}
    if isinstance(value, list):
        return [_reversed_mappings(item) for item in value]
    return value


def test_openapi_fingerprint_normalizes_json_format_and_mapping_order() -> None:
    raw, types = _raw_contract()
    canonical = json.loads(raw)
    checker = _checker()
    checker.validate(canonical, types)
    checker.validate(_reversed_mappings(canonical), types)
    checker.validate(json.loads(json.dumps(canonical, indent=None)), types)
    checker.validate(json.loads("\n\t" + json.dumps(canonical, indent=4) + "\n"), types)


def _scalar_paths(value: Any, path: tuple[object, ...] = ()) -> Iterator[tuple[object, ...]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from _scalar_paths(item, (*path, key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _scalar_paths(item, (*path, index))
    else:
        yield path


def _replace_scalar(document: dict[str, Any], path: tuple[object, ...]) -> None:
    target: Any = document
    for part in path[:-1]:
        target = target[part]
    old = target[path[-1]]
    if isinstance(old, bool):
        new: Any = not old
    elif isinstance(old, int):
        new = old + 1
    elif old is None:
        new = "mutated"
    else:
        new = f"{old}__mutated"
    target[path[-1]] = new


def test_checker_rejects_mutation_of_every_openapi_scalar_leaf() -> None:
    document, types = _contract()
    checker = _checker()
    paths = list(_scalar_paths(document))
    assert len(paths) > 100
    for path in paths:
        mutated = copy.deepcopy(document)
        _replace_scalar(mutated, path)
        with pytest.raises(AssertionError):
            checker.validate(mutated, types)


def test_checker_rejects_openapi_container_key_and_shape_mutations() -> None:
    document, types = _contract()
    mutations = []
    added = copy.deepcopy(document)
    added["x-unapproved"] = True
    mutations.append(added)
    removed = copy.deepcopy(document)
    removed["paths"].pop("/api/v1/health")
    mutations.append(removed)
    reordered_array = copy.deepcopy(document)
    required = reordered_array["components"]["schemas"]["BusRequest"]["required"]
    required.reverse()
    mutations.append(reordered_array)
    for mutated in mutations:
        with pytest.raises(AssertionError):
            _checker().validate(mutated, types)


def test_checker_rejects_every_single_typescript_byte_replacement() -> None:
    document, types = _contract()
    checker = _checker()
    for index, character in enumerate(types):
        replacement = "X" if character != "X" else "Y"
        mutated = f"{types[:index]}{replacement}{types[index + 1:]}"
        with pytest.raises(AssertionError):
            checker.validate(document, mutated)


@pytest.mark.parametrize(
    ("old", "new"),
    [
        ("BusPage", "BusPageShadow"),
        ("rows: BusRow[]", "rows: Channel[]"),
        ("decimal: number", "decimal: string"),
        ("number | null", "number"),
        ("OperationState", "OperationStatus"),
        ('"failed" | "cancelled"', '"cancelled"'),
        ("sample_index: number", "sample_index?: number"),
    ],
    ids=["interface", "reference", "primitive", "nullability", "identifier", "enum", "field"],
)
def test_checker_rejects_named_typescript_mutations(old: str, new: str) -> None:
    document, types = _contract()
    mutated = types.replace(old, new, 1)
    assert mutated != types
    with pytest.raises(AssertionError):
        _checker().validate(document, mutated)
