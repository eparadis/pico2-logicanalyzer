"""Fresh round-2 black-box verification of the private C3-B2 host."""

from __future__ import annotations

import copy
import os
import subprocess
import sys
from collections.abc import Callable

import pytest

from pico_logic_analyzer._decode.host import (
    _decode_with_factory,
    _enforce_result_limits,
    _validate_cleanup_times,
    _validate_parent_growth,
    _validate_worker_metrics,
    decode_private,
)
from pico_logic_analyzer._decode.ipc import RESULT, encode_frame
from pico_logic_analyzer._decode.model import (
    HARD_LIMITS,
    REGRESSION_LIMITS,
    DecodeFailure,
    DecodeRequest,
    HostFailure,
)


def _request() -> DecodeRequest:
    return DecodeRequest("uart", 1, (7, 2), {"rx": 7, "tx": 2}, (0, 0), 1, {})


def _valid_result() -> dict[str, object]:
    return decode_private(_request()).to_dict()


def _frame(result: dict[str, object], **extra: object) -> bytes:
    payload: dict[str, object] = {
        "result": result,
        "metrics": {
            "child_import_ns": 0,
            "child_load_ns": 0,
            "child_decode_ns": 0,
            "worker_peak_rss_bytes": 0,
        },
    }
    payload.update(extra)
    return encode_frame(RESULT, payload, HARD_LIMITS["encoded_bytes"])


def _factory(frame: bytes) -> Callable[..., subprocess.Popen[bytes]]:
    def factory(args: list[str], **kwargs: object) -> subprocess.Popen[bytes]:
        response_fd = int(args[-1])
        source = "import os,sys;os.write(int(sys.argv[1]),bytes.fromhex(sys.argv[2]))"
        return subprocess.Popen(
            [sys.executable, "-I", "-B", "-c", source, str(response_fd), frame.hex()],
            **kwargs,
        )

    return factory


def _reject_and_recover(result: dict[str, object]) -> None:
    before = set(os.listdir("/dev/fd"))
    with pytest.raises(HostFailure, match="^ipc$"):
        _decode_with_factory(_request(), _factory(_frame(result)))
    assert set(os.listdir("/dev/fd")) == before
    recovered = decode_private(_request())
    assert recovered.to_dict() == _valid_result()


def _set_nested(result: dict[str, object], path: tuple[object, ...], value: object) -> None:
    target: object = result
    for part in path[:-1]:
        target = target[part]  # type: ignore[index]
    target[path[-1]] = value  # type: ignore[index]


@pytest.mark.parametrize(
    ("path", "value"),
    [
        (("decoder", "id"), "i2c"),
        (("decoder", "file_set_sha256"), "f" * 64),
        (("samplerate_hz",), 2),
        (("capture", "sample_count"), 3),
        (("capture", "trigger_index"), 0),
        (("channels", 0, "decoder_channel"), "tx"),
        (("channels", 0, "physical_channel"), 2),
    ],
    ids=("decoder", "hash", "rate", "samples", "trigger", "channel-name", "physical"),
)
def test_every_scalar_projection_is_bound_to_pre_spawn_facts(
    path: tuple[object, ...], value: object
) -> None:
    result = copy.deepcopy(_valid_result())
    _set_nested(result, path, value)
    _reject_and_recover(result)


@pytest.mark.parametrize("variant", ["reordered", "locally-valid", "duplicate"])
def test_mapping_identity_and_order_cannot_be_replaced(variant: str) -> None:
    result = copy.deepcopy(_valid_result())
    channels = result["channels"]
    assert isinstance(channels, list)
    if variant == "reordered":
        channels.reverse()
    elif variant == "locally-valid":
        result["channels"] = [
            {"decoder_channel": "rx", "physical_channel": 0},
            {"decoder_channel": "tx", "physical_channel": 1},
        ]
    else:
        channels[1] = copy.deepcopy(channels[0])
    _reject_and_recover(result)


@pytest.mark.parametrize("variant", ["missing-default", "extra", "value", "type"])
def test_full_materialized_option_set_value_type_and_order_are_bound(variant: str) -> None:
    result = copy.deepcopy(_valid_result())
    options = result["options"]
    assert isinstance(options, dict)
    if variant == "missing-default":
        options.pop("baudrate")
    elif variant == "extra":
        options["unapproved"] = 1
    elif variant == "value":
        options["baudrate"] = 9600
    elif variant == "type":
        options["stop_bits"] = 1
    _reject_and_recover(result)


def test_option_key_order_is_canonicalized_without_changing_projection() -> None:
    result = copy.deepcopy(_valid_result())
    options = result["options"]
    assert isinstance(options, dict)
    result["options"] = dict(reversed(list(options.items())))
    actual = _decode_with_factory(_request(), _factory(_frame(result)))
    assert actual.to_dict() == _valid_result()


@pytest.mark.parametrize("section", ["declarations", "records"])
def test_adjacent_result_content_inconsistency_is_atomic_ipc(section: str) -> None:
    result = copy.deepcopy(_valid_result())
    if section == "declarations":
        declarations = result["declarations"]
        assert isinstance(declarations, dict)
        annotations = declarations["annotations"]
        assert isinstance(annotations, list)
        annotations[0]["index"] = 99
    else:
        # A locally shaped record may not name an undeclared output.
        result["records"] = [{
            "emission_index": 0, "start_sample": 0, "end_sample": 0,
            "output_id": 999, "kind": "annotation",
            "value": {"class_index": 0, "texts": ["x"]},
            "start_time": {"absolute": {"numerator": 0, "denominator": 1},
                           "trigger_relative": {"numerator": -1, "denominator": 1}},
            "end_time": {"absolute": {"numerator": 0, "denominator": 1},
                         "trigger_relative": {"numerator": -1, "denominator": 1}},
        }]
    _reject_and_recover(result)


def test_exact_unmodified_projection_is_accepted() -> None:
    expected = _valid_result()
    actual = _decode_with_factory(_request(), _factory(_frame(copy.deepcopy(expected))))
    assert actual.to_dict() == expected


@pytest.mark.parametrize("name", sorted(REGRESSION_LIMITS))
def test_independently_rederived_numeric_boundary_is_inclusive(name: str) -> None:
    limit = REGRESSION_LIMITS[name]
    assert type(limit) is int and limit > 0
    if name in {"child_import_ns", "child_load_ns", "child_decode_ns", "worker_peak_rss_bytes"}:
        metrics = {key: 0 for key in (
            "child_import_ns", "child_load_ns", "child_decode_ns", "worker_peak_rss_bytes"
        )}
        metrics[name] = limit
        _validate_worker_metrics(metrics)
        metrics[name] = limit + 1
        with pytest.raises(HostFailure, match="^process-exit$"):
            _validate_worker_metrics(metrics)


def test_decoded_retained_and_parent_growth_exact_boundary_plus_one() -> None:
    _enforce_result_limits(
        {},
        lambda _: HARD_LIMITS["decoded_bytes"],
        lambda _: HARD_LIMITS["retained_result_bytes"],
    )
    with pytest.raises(HostFailure, match="^output-limit$"):
        _enforce_result_limits({}, lambda _: HARD_LIMITS["decoded_bytes"] + 1, lambda _: 0)
    _validate_parent_growth(10, 10 + REGRESSION_LIMITS["parent_retained_growth_bytes"])
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_parent_growth(10, 11 + REGRESSION_LIMITS["parent_retained_growth_bytes"])


def test_cleanup_caps_are_inclusive_and_first_overrun_is_typed() -> None:
    _validate_cleanup_times(
        REGRESSION_LIMITS["timeout_cleanup_total_ns"],
        REGRESSION_LIMITS["terminate_to_reap_ns"],
        REGRESSION_LIMITS["kill_to_reap_ns"],
    )
    with pytest.raises(HostFailure, match="^process-exit$"):
        _validate_cleanup_times(REGRESSION_LIMITS["timeout_cleanup_total_ns"] + 1, 0, 0)


@pytest.mark.parametrize("message", ["Traceback: boom", "/private/tmp/secret.py", "C:\\secret.py"])
def test_failure_diagnostic_cannot_disclose_traceback_or_path(message: str) -> None:
    with pytest.raises(HostFailure):
        DecodeFailure("decoder", message)


def test_private_host_has_no_public_or_request_selected_execution_surface() -> None:
    import pico_logic_analyzer
    import pico_logic_analyzer._decode.host as host

    assert not hasattr(pico_logic_analyzer, "decode_private")
    assert not hasattr(pico_logic_analyzer, "decode_capture")
    source = open(host.__file__, encoding="utf-8").read()
    assert "shell=True" not in source
    assert "PYTHONPATH" not in source
    assert "request.decoder" not in source[source.index("def _spawn_fixed_worker") :]
