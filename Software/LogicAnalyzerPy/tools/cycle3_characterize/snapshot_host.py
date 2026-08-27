"""Fixed-snapshot loader primitives; no decoder lifecycle is invoked here."""

from __future__ import annotations

import base64
import hashlib
import json
import resource
import sys
import time
import types
from pathlib import Path
from typing import Any

DECODERS = frozenset({"uart", "spi", "i2c"})
SOURCE_SHA256 = dict(
    [
        (
            "Software/decoders/common/srdhelper/__init__.py",
            "125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1",
        ),
        (
            "Software/decoders/common/srdhelper/mod.py",
            "602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6",
        ),
        (
            "Software/decoders/i2c/__init__.py",
            "37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f",
        ),
        (
            "Software/decoders/i2c/pd.py",
            "b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305",
        ),
        (
            "Software/decoders/sigrokdecode.py",
            "385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a",
        ),
        (
            "Software/decoders/spi/__init__.py",
            "91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c",
        ),
        (
            "Software/decoders/spi/pd.py",
            "ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d",
        ),
        (
            "Software/decoders/uart/__init__.py",
            "351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f",
        ),
        (
            "Software/decoders/uart/pd.py",
            "67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc",
        ),
    ]
)
DECODER_PATHS = {
    "uart": (
        "Software/decoders/sigrokdecode.py",
        "Software/decoders/uart/__init__.py",
        "Software/decoders/uart/pd.py",
        "Software/decoders/common/srdhelper/__init__.py",
        "Software/decoders/common/srdhelper/mod.py",
    ),
    "spi": (
        "Software/decoders/sigrokdecode.py",
        "Software/decoders/spi/__init__.py",
        "Software/decoders/spi/pd.py",
    ),
    "i2c": (
        "Software/decoders/sigrokdecode.py",
        "Software/decoders/i2c/__init__.py",
        "Software/decoders/i2c/pd.py",
        "Software/decoders/common/srdhelper/__init__.py",
        "Software/decoders/common/srdhelper/mod.py",
    ),
}
DECODER_SET_SHA256 = {
    "uart": "eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3",
    "spi": "96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193",
    "i2c": "dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae",
}
if set().union(*map(set, DECODER_PATHS.values())) - set(SOURCE_SHA256):
    raise RuntimeError("fixed source set rejected")


class SnapshotHostFailure(RuntimeError):
    """A fixed snapshot byte or containment check failed."""


def _require_int(options: dict[object, object], key: str, default: int) -> int:
    value = options.get(key, default)
    if type(value) is not int:
        raise SnapshotHostFailure("options rejected")
    return value


def _require_str(options: dict[object, object], key: str, default: str) -> str:
    value = options.get(key, default)
    if not isinstance(value, str):
        raise SnapshotHostFailure("options rejected")
    return value


def _require_number(options: dict[object, object], key: str, default: float) -> int | float:
    value = options.get(key, default)
    if type(value) is int or type(value) is float:
        return value
    else:
        raise SnapshotHostFailure("options rejected")


def load_pinned_bytes(root: Path, relative: str, digest: str) -> bytes:
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise SnapshotHostFailure("snapshot path rejected")
    path = root / relative
    try:
        path.relative_to(root)
    except ValueError as error:
        raise SnapshotHostFailure("snapshot path rejected") from error
    current = root
    for part in Path(relative).parts:
        current /= part
        if current.is_symlink():
            raise SnapshotHostFailure("snapshot path rejected")
    if path.is_symlink() or not path.is_file():
        raise SnapshotHostFailure("snapshot path rejected")
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise SnapshotHostFailure("snapshot digest rejected")
    return data


def canonical_value(value: object) -> object:
    if value is int:
        return {"$cycle3_type": "int"}
    if value is None or type(value) in {bool, int, str}:
        return value
    if isinstance(value, bytes):
        return {"$cycle3_bytes": base64.b64encode(value).decode("ascii"), "length": len(value)}
    if isinstance(value, list | tuple):
        return [canonical_value(item) for item in value]
    if isinstance(value, dict):
        if any(type(key) is not str for key in value):
            raise SnapshotHostFailure("unsupported canonical key")
        return {key: canonical_value(item) for key, item in value.items()}
    raise SnapshotHostFailure("unsupported canonical value")


def format_metrics(
    *,
    input_samples: int,
    registrations: dict[int, dict[str, object]],
    records: list[dict[str, object]],
    load_ns: int,
    import_ns: int,
    decode_ns: int,
    maxrss: int,
    address_space: tuple[int, int],
    recursion: int,
) -> str:
    types_count: dict[str, int] = {}
    for record in records:
        output = record.get("output")
        if isinstance(output, dict) and type(output.get("type")) is int:
            key = str(output["type"])
            types_count[key] = types_count.get(key, 0) + 1
    return json.dumps(
        {
            "address_space": list(address_space),
            "decode_ns": decode_ns,
            "input_samples": input_samples,
            "load_ns": load_ns,
            "maxrss": maxrss,
            "output_type_counts": types_count,
            "record_count": len(records),
            "recursion": recursion,
            "registration_count": len(registrations),
            "import_ns": import_ns,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def validate_characterization_request(request: object) -> dict[str, object]:
    required = {"version", "decoder", "files", "samplerate", "channels", "samples", "options"}
    if not isinstance(request, dict) or set(request) != required or request.get("version") != 1:
        raise SnapshotHostFailure("request rejected")
    decoder = request["decoder"]
    channels, samples, samplerate, options = (
        request["channels"],
        request["samples"],
        request["samplerate"],
        request["options"],
    )
    if (
        not isinstance(decoder, str)
        or decoder not in DECODERS
        or request["files"] != list(DECODER_PATHS[decoder])
        or type(samplerate) is not int
        or samplerate <= 0
    ):
        raise SnapshotHostFailure("request rejected")
    if (
        not isinstance(channels, list)
        or not isinstance(samples, list)
        or not samples
        or not all(type(x) is int and x >= 0 for x in samples)
    ):
        raise SnapshotHostFailure("capture rejected")
    lengths = {"uart": 2, "spi": 4, "i2c": 2}
    if len(channels) != lengths[decoder] or not all(
        type(x) is int and 0 <= x <= 255 for x in channels
    ):
        raise SnapshotHostFailure("mapping rejected")
    mapped = [x for x in channels if x != 255]
    if (
        len(mapped) != len(set(mapped))
        or (decoder == "uart" and not mapped)
        or (decoder == "spi" and (channels[0] == 255 or channels[1] == channels[2] == 255))
        or (decoder == "i2c" and 255 in channels)
    ):
        raise SnapshotHostFailure("mapping rejected")
    if not isinstance(options, dict):
        raise SnapshotHostFailure("options rejected")
    allowed = {
        "uart": {
            "baudrate",
            "data_bits",
            "parity",
            "stop_bits",
            "bit_order",
            "format",
            "invert_rx",
            "invert_tx",
            "sample_point",
            "rx_packet_delim",
            "tx_packet_delim",
            "rx_packet_len",
            "tx_packet_len",
        },
        "spi": {"cs_polarity", "cpol", "cpha", "bitorder", "wordsize"},
        "i2c": {"address_format"},
    }[decoder]
    if set(options) - allowed or any(type(key) is not str for key in options):
        raise SnapshotHostFailure("options rejected")
    if decoder == "uart":
        baudrate, data_bits, sample_point = (
            _require_int(options, "baudrate", 115200),
            _require_int(options, "data_bits", 8),
            _require_int(options, "sample_point", 50),
        )
        parity, bit_order, display = (
            _require_str(options, "parity", "none"),
            _require_str(options, "bit_order", "lsb-first"),
            _require_str(options, "format", "hex"),
        )
        invert_rx, invert_tx = (
            _require_str(options, "invert_rx", "no"),
            _require_str(options, "invert_tx", "no"),
        )
        stop_bits = _require_number(options, "stop_bits", 1.0)
        delimiters = (
            _require_int(options, "rx_packet_delim", -1),
            _require_int(options, "tx_packet_delim", -1),
        )
        packet_lengths = (
            _require_int(options, "rx_packet_len", -1),
            _require_int(options, "tx_packet_len", -1),
        )
        if (
            baudrate <= 0
            or parity not in {"none", "odd", "even", "zero", "one", "ignore"}
            or stop_bits not in {0.0, 0.5, 1.0, 1.5, 2.0}
            or bit_order not in {"lsb-first", "msb-first"}
            or display not in {"ascii", "dec", "hex", "oct", "bin"}
            or invert_rx not in {"yes", "no"}
            or invert_tx not in {"yes", "no"}
            or not 1 <= sample_point <= 99
        ):
            raise SnapshotHostFailure("options rejected")
        if data_bits not in {5, 6, 7, 8, 9}:
            raise SnapshotHostFailure("options rejected")
        maximum = (1 << data_bits) - 1
        if any(value != -1 and not 0 <= value <= maximum for value in delimiters) or any(
            value != -1 and value <= 0 for value in packet_lengths
        ):
            raise SnapshotHostFailure("options rejected")
    if decoder == "spi" and (
        _require_str(options, "cs_polarity", "active-low") not in {"active-low", "active-high"}
        or _require_int(options, "cpol", 0) not in {0, 1}
        or _require_int(options, "cpha", 0) not in {0, 1}
        or _require_str(options, "bitorder", "msb-first") not in {"msb-first", "lsb-first"}
        or not 1 <= _require_int(options, "wordsize", 8) <= 8
    ):
        raise SnapshotHostFailure("options rejected")
    if decoder == "i2c" and _require_str(options, "address_format", "shifted") not in {
        "shifted",
        "unshifted",
    }:
        raise SnapshotHostFailure("options rejected")
    return dict(request)


class _Capture:
    """Small, closed API-v3 compatibility object for one pinned snapshot."""

    def __init__(self, channels: list[int], samples: list[int]) -> None:
        self.channels = channels
        self.samples = samples
        self.index = -1
        self.records: list[dict[str, object]] = []
        self.next_output = 0
        self.outputs: dict[int, dict[str, object]] = {}
        self.owner: Any = None

    def HasChannel(self, channel: int) -> bool:  # noqa: N802 - pinned API spelling
        return (
            type(channel) is int
            and 0 <= channel < len(self.channels)
            and self.channels[channel] != 255
        )

    def _pins(self, sample: int) -> tuple[int, ...]:
        packed = self.samples[sample]
        return tuple(
            (packed >> physical) & 1 if physical != 255 else 255 for physical in self.channels
        )

    def _matches(
        self,
        sample: int,
        pins: tuple[int, ...],
        alternatives: list[dict[object, object]],
        previous: tuple[int, ...] | None,
        wait_origin: int,
    ) -> list[bool]:
        matched: list[bool] = []
        for condition in alternatives:
            if "skip" in condition:
                if set(condition) != {"skip"} or type(condition["skip"]) is not int:
                    raise SnapshotHostFailure("wait skip rejected")
                skip = condition["skip"]
                if skip < 0:
                    raise SnapshotHostFailure("wait skip rejected")
                matched.append(sample == max(0, wait_origin + skip))
                continue
            ok = True
            for raw_channel, wanted in condition.items():
                if type(raw_channel) is int:
                    channel = raw_channel
                elif isinstance(raw_channel, str):
                    try:
                        channel = int(raw_channel)
                    except ValueError as error:
                        raise SnapshotHostFailure("wait channel rejected") from error
                else:
                    raise SnapshotHostFailure("wait channel rejected")
                if not self.HasChannel(channel) or wanted not in {"r", "f", "e", "h", "l"}:
                    raise SnapshotHostFailure("wait condition rejected")
                current = pins[channel]
                prior = previous[channel] if previous is not None else None
                ok = ok and (
                    (wanted == "h" and current == 1)
                    or (wanted == "l" and current == 0)
                    or (wanted == "r" and prior == 0 and current == 1)
                    or (wanted == "f" and prior == 1 and current == 0)
                    or (wanted == "e" and prior is not None and prior != current)
                )
            matched.append(ok)
        return matched

    def Wait(self, conditions: object = None) -> tuple[int, ...] | None:  # noqa: N802
        raw_alternatives = conditions if isinstance(conditions, list) else [conditions or {}]
        if not raw_alternatives or any(not isinstance(item, dict) for item in raw_alternatives):
            raise SnapshotHostFailure("wait condition rejected")
        alternatives: list[dict[object, object]] = raw_alternatives
        wait_origin = self.index
        zero_skip = any(item.get("skip") == 0 for item in alternatives)
        start = max(0, self.index if zero_skip else self.index + 1)
        for sample in range(start, len(self.samples)):
            pins = self._pins(sample)
            previous = self._pins(sample - 1) if sample else None
            matched = self._matches(sample, pins, alternatives, previous, wait_origin)
            if any(matched):
                self.index = sample
                self.owner.samplenum = sample
                self.owner.matched = tuple(matched)
                return pins
        self.index = len(self.samples)
        self.owner.samplenum = len(self.samples)
        self.owner.matched = tuple(False for _ in alternatives)
        return None

    def Register(self, output_type: int, meta: object = None) -> int:  # noqa: N802
        if type(output_type) is not int:
            raise SnapshotHostFailure("register rejected")
        output = self.next_output
        self.next_output += 1
        self.outputs[output] = {"type": output_type, "meta": canonical_value(meta)}
        return output

    def Put(self, start: int, end: int, output: int, value: object) -> None:  # noqa: N802
        if (
            any(type(item) is not int for item in (start, end, output))
            or output not in self.outputs
            or not 0 <= start <= end <= len(self.samples)
        ):
            raise SnapshotHostFailure("put interval rejected")
        self.records.append(
            {
                "start_sample": start,
                "end_sample": end,
                "output_id": output,
                "output": self.outputs[output],
                "value": canonical_value(value),
            }
        )


def _module(name: str, source: bytes = b"", package: bool = False) -> types.ModuleType:
    module = types.ModuleType(name)
    module.__file__ = "<pinned-snapshot>"
    if package:
        module.__path__ = []
    sys.modules[name] = module
    exec(compile(source, "<pinned-snapshot>", "exec"), module.__dict__)  # noqa: S102 - exact verified bytes
    return module


def _exec_module(module: types.ModuleType, source: bytes) -> None:
    exec(compile(source, "<pinned-snapshot>", "exec"), module.__dict__)  # noqa: S102 - exact verified bytes


def execute_snapshot(root: Path, request: dict[str, object]) -> dict[str, object]:
    """Execute exactly one already-verified decoder graph after the external gate."""
    request = validate_characterization_request(request)
    decoder_id = request["decoder"]
    if not isinstance(decoder_id, str) or decoder_id not in DECODERS:
        raise SnapshotHostFailure("decoder rejected")
    expected = DECODER_PATHS[decoder_id]
    if request.get("files") != list(expected):
        raise SnapshotHostFailure("decoder source set rejected")
    channels = request.get("channels")
    samples = request.get("samples")
    samplerate = request.get("samplerate")
    if (
        type(samplerate) is not int
        or samplerate <= 0
        or not isinstance(channels, list)
        or not isinstance(samples, list)
        or not all(type(x) is int and x >= 0 for x in samples)
    ):
        raise SnapshotHostFailure("capture rejected")
    required_channels = {"uart": 2, "spi": 4, "i2c": 2}[decoder_id]
    if len(channels) != required_channels or not all(
        type(x) is int and 0 <= x <= 255 for x in channels
    ):
        raise SnapshotHostFailure("logical mapping rejected")
    before_load = time.monotonic_ns()
    loaded = {path: load_pinned_bytes(root, path, SOURCE_SHA256[path]) for path in expected}
    load_ns = time.monotonic_ns() - before_load
    names = (
        "sigrokdecode",
        "common",
        "common.srdhelper",
        "common.srdhelper.mod",
        decoder_id,
        f"{decoder_id}.pd",
    )
    prior = {name: sys.modules.get(name) for name in names}
    try:
        before_import = time.monotonic_ns()
        _module("sigrokdecode", loaded["Software/decoders/sigrokdecode.py"])
        if any("common/srdhelper" in path for path in expected):
            _module("common", b"", package=True)
            _module("common.srdhelper.mod", loaded["Software/decoders/common/srdhelper/mod.py"])
            _module(
                "common.srdhelper",
                loaded["Software/decoders/common/srdhelper/__init__.py"],
                package=True,
            )
        package = _module(decoder_id, package=True)
        module = _module(f"{decoder_id}.pd", loaded[f"Software/decoders/{decoder_id}/pd.py"])
        _exec_module(package, loaded[f"Software/decoders/{decoder_id}/__init__.py"])
        import_ns = time.monotonic_ns() - before_import
        decoder = module.Decoder()
        options = request.get("options")
        if not isinstance(options, dict):
            raise SnapshotHostFailure("options rejected")
        defaults = {item["id"]: item["default"] for item in decoder.options}
        if set(options) - set(defaults):
            raise SnapshotHostFailure("options rejected")
        for spec in decoder.options:
            key = spec["id"]
            if key not in options:
                continue
            value = options[key]
            if "values" in spec and value not in spec["values"]:
                raise SnapshotHostFailure("options rejected")
            if key == "wordsize" and (type(value) is not int or not 1 <= value <= 8):
                raise SnapshotHostFailure("options rejected")
        decoder.options = {**defaults, **options}
        capture = _Capture(channels, samples)
        capture.owner = decoder
        decoder.cObj = capture
        decoder.metadata(sys.modules["sigrokdecode"].SRD_CONF_SAMPLERATE, samplerate)
        decoder.start()
        before_decode = time.monotonic_ns()
        try:
            decoder.decode()
        except Exception as error:
            if error.args != ("Terminated",):
                raise
        decode_ns = time.monotonic_ns() - before_decode
        counts = format_metrics(
            input_samples=len(samples),
            registrations=capture.outputs,
            records=capture.records,
            load_ns=load_ns,
            import_ns=import_ns,
            decode_ns=decode_ns,
            maxrss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            address_space=resource.getrlimit(resource.RLIMIT_AS),
            recursion=sys.getrecursionlimit(),
        )
        return {
            "version": 1,
            "records": capture.records,
            "text": "",
            "binary": "",
            "diagnostics": counts,
        }
    finally:
        for name, old in prior.items():
            if old is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = old
