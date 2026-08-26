# Cycle 3 decoder provenance and license inventory

This B1 static inventory identifies the closed nine-file executable set: the
shim, UART/SPI/I2C initializers and `pd.py` files, and the helper initializer
and implementation listed in `testdata/decoders/cycle3/provenance.json`.
Their SHA-256 values, import commit
`407b5ef039aa0474c400c0721749baa126e53270`, and prior gitlink
`0235970293590f673a253950e6c61017cefa97df` are regenerated from independent
literals by `scripts/generate_cycle3_fixtures.py`.

The closed imports are the local shim/helper and the exact standard-library
symbols in the inventory. The source headers retain GPL-2.0-or-later notices.
The package is currently MIT-labelled. This inventory is proposed decision input:
before any package placement of GPL-2.0-or-later snapshot material, independent
project/legal review must decide placement, notices, attribution manifest, and
resulting package metadata. That review has not occurred and this document does
not claim it passed, reach a legal conclusion, or authorize distribution.

The generator and every test are stdlib-only static data processing; they do
not import or execute a decoder, host, C#, .NET, or reference runtime.

The inventory is file-accurate: `sigrokdecode.py`; `uart/__init__.py` and
`uart/pd.py`; `spi/__init__.py` and `spi/pd.py`; `i2c/__init__.py` and
`i2c/pd.py`; and `common/srdhelper/__init__.py` and `common/srdhelper/mod.py`.
Each digest is calculated against checked-in bytes, not an imported module.
The shim has no observed in-file copyright/GPL header; each snapshot/helper
file carries its retained GPLv2-or-later header. This is an observation, not a
legal conclusion.

The concrete review packet asks independent project/legal owners to decide
whether snapshots may enter package placement, how retained notices and an
attribution manifest should be carried, and whether present MIT metadata needs
change. Build, wheel, sdist, editable installation, distribution, and
publication remain forbidden until that separate review is complete.
