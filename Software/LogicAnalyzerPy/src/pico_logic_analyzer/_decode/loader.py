"""Pinned in-memory frozen decoder module loader; it never creates a decoder instance."""

from __future__ import annotations

import builtins
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from types import ModuleType

from .identity import ROOT, DecoderIdentity, verify_decoder
from .model import WorkerFailure

_MODULES = (
    "sigrokdecode", "uart", "uart.pd", "spi", "spi.pd", "i2c", "i2c.pd", "common",
    "common.srdhelper", "common.srdhelper.mod",
)
_STDLIB = frozenset({"collections", "math", "enum", "itertools", "re"})


@dataclass(frozen=True)
class FrozenDescriptor:
    identity: DecoderIdentity
    decoder_class: type[object]
    shim_class: type[object]
    spi_data_type: type[object] | None


def load_frozen_decoder(decoder: str) -> FrozenDescriptor:
    identity = verify_decoder(decoder)
    _clear_modules()
    original_import = builtins.__import__

    def guarded_import(
        name: str,
        globals: Mapping[str, object] | None = None,
        locals: Mapping[str, object] | None = None,
        fromlist: Sequence[str] = (),
        level: int = 0,
    ) -> ModuleType:
        root = name.split(".", 1)[0]
        if level == 0 and root not in _STDLIB and root not in {"sigrokdecode", "common", decoder}:
            raise WorkerFailure("frozen import rejected")
        return original_import(name, globals, locals, fromlist, level)

    builtins.__import__ = guarded_import
    try:
        shim = _load_module("sigrokdecode", "Software/decoders/sigrokdecode.py")
        if decoder in {"uart", "i2c"}:
            _package("common")
            _package("common.srdhelper")
            _load_module("common.srdhelper.mod", "Software/decoders/common/srdhelper/mod.py")
            _exec_into(
                sys.modules["common.srdhelper"], "Software/decoders/common/srdhelper/__init__.py"
            )
        _package(decoder)
        module = _load_module(f"{decoder}.pd", f"Software/decoders/{decoder}/pd.py")
        _exec_into(sys.modules[decoder], f"Software/decoders/{decoder}/__init__.py")
    except BaseException:
        _clear_modules()
        raise
    finally:
        builtins.__import__ = original_import
    decoder_class = getattr(module, "Decoder", None)
    shim_class = getattr(shim, "Decoder", None)
    data = getattr(module, "Data", None) if decoder == "spi" else None
    if (
        type(decoder_class) is not type
        or type(shim_class) is not type
        or (data is not None and type(data) is not type)
    ):
        _clear_modules()
        raise WorkerFailure("frozen descriptor rejected")
    return FrozenDescriptor(identity, decoder_class, shim_class, data)


def _package(name: str) -> None:
    module = ModuleType(name)
    module.__package__ = name
    module.__path__ = []
    sys.modules[name] = module


def _load_module(name: str, relative: str) -> ModuleType:
    module = ModuleType(name)
    module.__file__ = str(ROOT / relative)
    module.__package__ = name.rpartition(".")[0]
    sys.modules[name] = module
    _exec_into(module, relative)
    return module


def _exec_into(module: ModuleType, relative: str) -> None:
    path = ROOT / relative
    if path != path.resolve() or not path.is_file() or path.suffix != ".py":
        raise WorkerFailure("frozen import rejected")
    code = compile(path.read_bytes(), str(path), "exec", dont_inherit=True)
    exec(code, module.__dict__)


def _clear_modules() -> None:
    for name in _MODULES:
        sys.modules.pop(name, None)
