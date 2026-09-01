"""Closed decoder identities for the B2 private host."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType

from .model import HostFailure

# ``ROOT`` remains the read-only repository identity used by the accepted B2/B3
# evidence.  Product execution uses only the exact package-owned snapshot root.
ROOT = Path(__file__).resolve().parents[5]
SNAPSHOT_COMMIT = "407b5ef039aa0474c400c0721749baa126e53270"
SNAPSHOT_ROOT = Path(__file__).resolve().parents[1] / "_decoder_snapshots" / SNAPSHOT_COMMIT
SOURCE_SHA256 = {
    "Software/decoders/sigrokdecode.py": (
        "385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a"
    ),
    "Software/decoders/uart/__init__.py": (
        "351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f"
    ),
    "Software/decoders/uart/pd.py": (
        "67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc"
    ),
    "Software/decoders/spi/__init__.py": (
        "91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c"
    ),
    "Software/decoders/spi/pd.py": (
        "ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d"
    ),
    "Software/decoders/i2c/__init__.py": (
        "37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f"
    ),
    "Software/decoders/i2c/pd.py": (
        "b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305"
    ),
    "Software/decoders/common/srdhelper/__init__.py": (
        "125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1"
    ),
    "Software/decoders/common/srdhelper/mod.py": (
        "602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6"
    ),
}
PATHS = MappingProxyType(
    {
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
)
FILE_SET_SHA256 = MappingProxyType(
    {
        "uart": "eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3",
        "spi": "96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193",
        "i2c": "dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae",
    }
)


@dataclass(frozen=True)
class DecoderIdentity:
    decoder: str
    paths: tuple[str, ...]
    file_set_sha256: str


def verify_decoder(request_decoder: str) -> DecoderIdentity:
    if (
        type(request_decoder) is not str
        or SNAPSHOT_ROOT != SNAPSHOT_ROOT.resolve()
        or SNAPSHOT_ROOT.is_symlink()
    ):
        raise HostFailure("decode identity rejected")
    paths = PATHS.get(request_decoder)
    if paths is None:
        raise HostFailure("decode identity rejected")
    expected_resources = {
        relative.removeprefix("Software/decoders/") for relative in SOURCE_SHA256
    }
    try:
        actual_resources = {
            str(path.relative_to(SNAPSHOT_ROOT))
            for path in SNAPSHOT_ROOT.rglob("*")
            if path.is_file()
        }
    except OSError:
        raise HostFailure("decode identity rejected") from None
    if actual_resources != expected_resources:
        raise HostFailure("decode identity rejected")
    digest_input = bytearray()
    for relative in paths:
        path = SNAPSHOT_ROOT / relative.removeprefix("Software/decoders/")
        try:
            invalid = (
                path != path.resolve()
                or any(
                    component.is_symlink()
                    for component in path.parents
                    if component != SNAPSHOT_ROOT.parent
                )
                or path.is_symlink()
                or not path.is_file()
                or hashlib.sha256(path.read_bytes()).hexdigest() != SOURCE_SHA256[relative]
            )
        except OSError:
            invalid = True
        if invalid:
            raise HostFailure("decode identity rejected")
        digest_input.extend(relative.encode())
        digest_input.extend(b"\0")
        digest_input.extend(SOURCE_SHA256[relative].encode())
        digest_input.extend(b"\n")
    digest = hashlib.sha256(digest_input).hexdigest()
    if digest != FILE_SET_SHA256[request_decoder]:
        raise HostFailure("decode identity rejected")
    return DecoderIdentity(request_decoder, paths, digest)
