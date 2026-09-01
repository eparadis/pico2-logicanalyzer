# Decoder snapshot attribution

The private installed decoder snapshot is copied byte-for-byte from import
commit `407b5ef039aa0474c400c0721749baa126e53270`. Its predecessor gitlink was
`Software/SigrokDecode` at `0235970293590f673a253950e6c61017cefa97df`.
The source headers are retained verbatim. The snapshot derives from the
[libsigrokdecode project](https://sigrok.org/wiki/Libsigrokdecode), except for
the compatibility shim whose file contains no notice and whose project-history
and rights confirmation remains required before conveyance.

| Installed path beneath `_decoder_snapshots/407b5ef039aa0474c400c0721749baa126e53270/` | Original repository path | SHA-256 | Observed attribution/license |
| --- | --- | --- | --- |
| `sigrokdecode.py` | `Software/decoders/sigrokdecode.py` | `385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a` | Notice not present in file; project-history/rights confirmation required |
| `uart/__init__.py` | `Software/decoders/uart/__init__.py` | `351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f` | Uwe Hermann, 2012; GPL-2.0-or-later |
| `uart/pd.py` | `Software/decoders/uart/pd.py` | `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc` | Uwe Hermann, 2011-2014; GPL-2.0-or-later |
| `spi/__init__.py` | `Software/decoders/spi/__init__.py` | `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c` | Uwe Hermann, 2012; GPL-2.0-or-later |
| `spi/pd.py` | `Software/decoders/spi/pd.py` | `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d` | Gareth McMullin, 2011; Uwe Hermann, 2012-2014; GPL-2.0-or-later |
| `i2c/__init__.py` | `Software/decoders/i2c/__init__.py` | `37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f` | Uwe Hermann, 2012; GPL-2.0-or-later |
| `i2c/pd.py` | `Software/decoders/i2c/pd.py` | `b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305` | Uwe Hermann, 2010-2016; GPL-2.0-or-later |
| `common/srdhelper/__init__.py` | `Software/decoders/common/srdhelper/__init__.py` | `125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1` | Uwe Hermann, 2012-2014; GPL-2.0-or-later |
| `common/srdhelper/mod.py` | `Software/decoders/common/srdhelper/mod.py` | `602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6` | Uwe Hermann, 2012-2020; GPL-2.0-or-later |

The distribution-level license expression is `GPL-3.0-only`. See [LICENSE](LICENSE)
for GPL version 3, [LICENSES/GPL-2.0-or-later.txt](LICENSES/GPL-2.0-or-later.txt)
for the retained snapshot notices, and [LICENSES/MIT.txt](LICENSES/MIT.txt) for
the pre-existing Python-package portions. This engineering attribution is not
legal advice, a warranty, or a certification of rights.
