"""Fresh round-3 adversarial verification of the private C3-B2 host."""

from __future__ import annotations

import copy
import os
import subprocess
import sys
from collections.abc import Callable
from dataclasses import fields

import pytest

from pico_logic_analyzer._decode.host import (
    _decode_with_factory,
    _RegressionObservation,
    _validate_regression_observation,
    decode_private,
)
from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
from pico_logic_analyzer._decode.model import (
    HARD_LIMITS,
    REGRESSION_LIMITS,
    DecodeRequest,
    HostFailure,
)


def _request(decoder: str = "uart") -> DecodeRequest:
    mappings = {
        "uart": {"rx": 7, "tx": 2},
        "spi": {"clk": 7, "miso": 2},
        "i2c": {"scl": 7, "sda": 2},
    }
    return DecodeRequest(decoder, 1, (7, 2), mappings[decoder], (0, 0), 1, {})


def _frame(result: dict[str, object], metrics: object | None = None) -> bytes:
    return encode_frame(
        RESULT,
        {
            "result": result,
            "metrics": metrics
            if metrics is not None
            else {
                "child_import_ns": 0,
                "child_load_ns": 0,
                "child_decode_ns": 0,
                "worker_peak_rss_bytes": 0,
            },
        },
        HARD_LIMITS["encoded_bytes"],
    )


def _factory(frame: bytes) -> Callable[..., subprocess.Popen[bytes]]:
    def factory(args: list[str], **kwargs: object) -> subprocess.Popen[bytes]:
        source = "import os,sys;os.write(int(sys.argv[1]),bytes.fromhex(sys.argv[2]))"
        return subprocess.Popen(
            [sys.executable, "-I", "-B", "-c", source, args[-1], frame.hex()], **kwargs
        )

    return factory


def _hostile(result: dict[str, object], request: DecodeRequest | None = None) -> None:
    selected = request or _request()
    before = set(os.listdir("/dev/fd"))
    with pytest.raises(HostFailure, match="^ipc$"):
        _decode_with_factory(selected, _factory(_frame(result)))
    assert set(os.listdir("/dev/fd")) == before
    assert decode_private(selected).decoder == selected.decoder


def _annotation_record(index: int, sample: int) -> dict[str, object]:
    return {
        "emission_index": index,
        "start_sample": sample,
        "end_sample": sample,
        "output_id": 2,
        "kind": "annotation",
        "value": {"class_index": 0, "texts": ["independent"]},
        "start_time": {
            "absolute": {"numerator": sample, "denominator": 1},
            "trigger_relative": {"numerator": sample - 1, "denominator": 1},
        },
        "end_time": {
            "absolute": {"numerator": sample, "denominator": 1},
            "trigger_relative": {"numerator": sample - 1, "denominator": 1},
        },
    }


@pytest.mark.parametrize("name", sorted(REGRESSION_LIMITS))
def test_separate_regression_gate_has_exact_inclusive_ceiling(name: str) -> None:
    values = dict(REGRESSION_LIMITS)
    exact = _RegressionObservation(**values)
    _validate_regression_observation(exact)
    values[name] += 1
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_regression_observation(_RegressionObservation(**values))


@pytest.mark.parametrize("bad", [-1, True, 1.0, "1", None])
def test_regression_gate_rejects_every_noncanonical_field_value(bad: object) -> None:
    values: dict[str, object] = dict(REGRESSION_LIMITS)
    values[fields(_RegressionObservation)[0].name] = bad
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_regression_observation(_RegressionObservation(**values))  # type: ignore[arg-type]


def test_over_ceiling_worker_metrics_remain_observable_product_success() -> None:
    request = _request()
    result = decode_private(request).to_dict()
    observed: list[_RegressionObservation] = []
    metrics = {
        "child_import_ns": REGRESSION_LIMITS["child_import_ns"] + 1,
        "child_load_ns": REGRESSION_LIMITS["child_load_ns"] + 1,
        "child_decode_ns": REGRESSION_LIMITS["child_decode_ns"] + 1,
        "worker_peak_rss_bytes": REGRESSION_LIMITS["worker_peak_rss_bytes"] + 1,
    }
    assert (
        _decode_with_factory(
            request, _factory(_frame(result, metrics)), regression_observer=observed.append
        ).to_dict()
        == result
    )
    assert len(observed) == 1
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_regression_observation(observed[0])


@pytest.mark.parametrize(
    "metrics",
    [
        {},
        {"child_import_ns": 0, "child_load_ns": 0, "child_decode_ns": 0},
        {
            "child_import_ns": 0,
            "child_load_ns": 0,
            "child_decode_ns": 0,
            "worker_peak_rss_bytes": 0,
            "extra": 0,
        },
        {
            "child_import_ns": False,
            "child_load_ns": 0,
            "child_decode_ns": 0,
            "worker_peak_rss_bytes": 0,
        },
        {
            "child_import_ns": -1,
            "child_load_ns": 0,
            "child_decode_ns": 0,
            "worker_peak_rss_bytes": 0,
        },
    ],
)
def test_hostile_metric_shape_is_atomic_and_does_not_poison(metrics: object) -> None:
    request = _request()
    result = decode_private(request).to_dict()
    before = set(os.listdir("/dev/fd"))
    with pytest.raises(HostFailure, match="^ipc$"):
        _decode_with_factory(request, _factory(_frame(result, metrics)))
    assert set(os.listdir("/dev/fd")) == before
    assert decode_private(request).to_dict() == result


@pytest.mark.parametrize(
    ("section", "mutation"),
    [
        ("annotations", "empty-id"),
        ("annotations", "empty-description"),
        ("annotations", "duplicate-id"),
        ("annotation_rows", "empty-id"),
        ("annotation_rows", "empty-description"),
        ("binary", "duplicate-id"),
    ],
)
def test_declaration_identity_and_description_invariants(section: str, mutation: str) -> None:
    result = copy.deepcopy(decode_private(_request()).to_dict())
    declarations = result["declarations"]
    assert isinstance(declarations, dict)
    collection = declarations[section]
    assert isinstance(collection, list) and collection
    if mutation == "empty-id":
        collection[0]["id"] = ""
    elif mutation == "empty-description":
        collection[0]["description"] = ""
    else:
        assert len(collection) > 1
        collection[1]["id"] = collection[0]["id"]
    _hostile(result)


def test_emission_indices_are_contiguous_and_ordered() -> None:
    result = copy.deepcopy(decode_private(_request()).to_dict())
    result["records"] = [_annotation_record(0, 0), _annotation_record(0, 1)]
    _hostile(result)


def test_terminal_capture_endpoint_with_exact_rational_times_is_valid() -> None:
    request = _request()
    result = copy.deepcopy(decode_private(request).to_dict())
    result["records"] = [_annotation_record(0, 2)]
    assert _decode_with_factory(request, _factory(_frame(result))).records[0].end_sample == 2


def test_product_source_never_invokes_regression_validator() -> None:
    import inspect

    import pico_logic_analyzer._decode.host as host

    source = inspect.getsource(host)
    assert source.count("_validate_regression_observation(") == 1
    assert "REGRESSION_LIMITS" not in inspect.getsource(host._decode_with_factory)


def test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import pico_logic_analyzer._decode.host as host

    limits = dict(HARD_LIMITS)
    limits["wall_deadline_ms"] = 50
    limits["terminate_grace_ms"] = 10
    monkeypatch.setattr(host, "HARD_LIMITS", limits)
    observed: list[_RegressionObservation] = []

    def ignoring_factory(args: list[str], **kwargs: object) -> subprocess.Popen[bytes]:
        source = "import signal,time;signal.signal(signal.SIGTERM,signal.SIG_IGN);time.sleep(60)"
        return subprocess.Popen([sys.executable, "-I", "-B", "-c", source], **kwargs)

    before = set(os.listdir("/dev/fd"))
    with pytest.raises(HostFailure, match="^timeout$"):
        host._decode_with_factory(_request(), ignoring_factory, regression_observer=observed.append)
    assert set(os.listdir("/dev/fd")) == before
    assert len(observed) == 1
    cleanup = observed[0]
    assert cleanup.timeout_cleanup_total_ns > 0
    assert cleanup.terminate_to_reap_ns > 0
    assert cleanup.kill_to_reap_ns > 0
    _validate_regression_observation(cleanup)
