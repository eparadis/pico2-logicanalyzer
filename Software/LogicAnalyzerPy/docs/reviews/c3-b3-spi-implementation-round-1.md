# C3-B3 SPI implementation — round 1

## Scope and verdict

Status: **candidate-not-accepted**. This bounded C3-B3 implementation adds
only independent SPI conformance evidence in
`tests/implementation/test_c3_b3_spi_conformance.py`. It does not alter a
decoder snapshot, product source, fixture, host, governing contract, progress
record, or public surface. No UART, I2C, R16/cross-source, accumulated,
acceptance, or checkpoint claim is made.

The oracle is independent: expected results come only from the accepted C3-B1
semantic corpus, closed option matrix, and provenance fixture. The test does
not import frozen decoder sources to manufacture expected behavior or defaults.
It obtains the five default options exclusively from the matrix's unique SPI
`classification=default` direct rows and asserts their closed key set.

## Coverage accounting

- All 6 accepted SPI timelines are reconstructed from literal fixture
  transitions and decoded: `spi-mosi-mode0-word8`, `spi-miso-mode3-word8`,
  `spi-cs-active-high-lsb-word1`, `spi-incomplete-no-cs`,
  `direct-spi-cs_polarity-activeneglow`, and
  `direct-spi-bitorder-msbnegfirst`.
- Each timeline compares the full typed result and canonical JSON bytes:
  declarations plus every emission-ordered annotation, binary, metadata, and
  Python record, including SPI `DATA` tagged semantics.
- All 10 direct SPI matrix rows resolve to an accepted timeline and rerun it.
  All 20 unsupported rows reject before `_spawn_fixed_worker` can be called.
- The fixture cases span CPOL/CPHA modes, MSB/LSB order, active-low/high CS,
  word sizes 1 and accepted maximum 8, MISO-only/MOSI-only/no-CS, incomplete
  traffic, and the direct default-option witnesses. Explicit compatibility
  probes verify all three accepted optional shapes: MISO-only
  `[0, 1, 255, 255]`/`[true, true, false, false]`, MOSI-only
  `[0, 255, 1, 255]`/`[true, false, true, false]`, and no-CS
  `[0, 1, 0, 255]`/`[true, true, true, false]`, where each pair is its
  `wait({})` pin vector and complete `has_channel` vector. They also verify a
  noncontiguous reordered `clk=19,miso=7,mosi=12,cs=3` capture mapping.
- A repeat decode compares canonical bytes twice. Static source-as-data checks
  close the exact snapshot digests and direct import roots.

## Fixture and source identity

| Artifact | SHA-256 |
| --- | --- |
| accepted B1 fixture manifest reference | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| semantic corpus | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| option matrix | `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209` |
| accepted B2 manifest | `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602` |
| SPI test candidate | `e35c8d2ac472a7ae4c557daaba54521696971f871ef158d794c3d754cfdc0250` |

The test asserts `Software/decoders/sigrokdecode.py`
`385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a`,
`Software/decoders/spi/__init__.py`
`91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c`,
and `Software/decoders/spi/pd.py`
`ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d`.
It also asserts the SPI provenance file-set SHA-256
`96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193`
and closed direct import roots: empty shim, `pd` initializer, and
`collections`/`sigrokdecode` decoder.

## Worktree and validation

- Assigned base HEAD/tree: `25d4849459ff238a28a41a4d72156b64f5fc8251` /
  `a12706a97298b53ec08854d43ddd9c3936352f9a`.
- Base worktree was clean. Candidate worktree contains only this SPI test and
  this review record; unrelated concurrent changes were not observed or
  modified.

All commands ran from `Software/LogicAnalyzerPy` except base identity checks.

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b3_spi_conformance.py -q` | `20 passed in 2.73s` |
| `.venv/bin/ruff check tests/implementation/test_c3_b3_spi_conformance.py` | `All checks passed!` |
| `git diff --check` | clean |

No approval, network, external/reference decoder, .NET/C#, libsigrokdecode,
sigrok-cli, hardware, serial, browser path, or fixture/product mutation was
used. No product defect was found, so no product change is proposed.
