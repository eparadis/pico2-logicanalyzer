from importlib import import_module

from .fake import ByteTransport, FakeTransport, TransportClosed, TransportTimeout

__all__ = [
    "ByteTransport",
    "FakeTransport",
    "SerialTransport",
    "SerialTransportError",
    "TransportClosed",
    "TransportTimeout",
]


def __getattr__(name: str) -> object:
    if name in {"SerialTransport", "SerialTransportError"}:
        return getattr(import_module("pico_logic_analyzer.transport.serial"), name)
    raise AttributeError(name)
