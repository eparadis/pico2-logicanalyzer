# C3-B3 UART independent verification — round 1

## Verdict

`pass`

The exact UART-only candidate commit
`e5ac88ef7425bfab75a7901d1ca6552cc587fec0`, tree
`b6fc418cb6ed907d78a03061b47c63da7a390a8d`, conforms to R13 under governing
contract `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree
`d9fb09345ab85580cd8c877745262d1b481e366f` and accepted B2 checkpoint
`18614cc812edda68598e19d200f7bb4c87861ebd`. No finding remains open.

## Identity and scope

The candidate diff contains the UART implementation test, its review record,
and a root-owned orchestration-progress evidence update; it contains no product
code. Recomputed SHA-256 values are:

| Artifact | SHA-256 |
| --- | --- |
| implementation test | `6ebad5ba914a41904fc6965dbc592e201e0d1bee8211efb030e2bd18a6d5bd16` |
| implementation review | `bf7ffcd8e147139a7f02436f324858408e414937dac0a0140ee33432debbe56c` |
| accepted semantic fixture | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| accepted option matrix | `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209` |
| accepted UART file set | `eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3` |

No product, fixture, snapshot, implementation evidence, progress, contract, or
dependency was changed by verification. No SPI, I2C, R16, public API, CLI,
Cycle 4, runtime/reference decoder, hardware, serial, browser, network, C#,
.NET, pythonnet, libsigrokdecode, or sigrok-cli action occurred.

## Independent hostile evidence

The verifier reconstructs packed samples directly from accepted declarative
transitions and physical mapping order. Expected fully materialized options
come exclusively from the 13 unique accepted B1 matrix default rows plus the
timeline override; no production default table is read.

- All 54 distinct UART timelines pass as full v1 objects and exact canonical
  bytes, with complete declarations and request-wide contiguous
  emission-ordered annotation, Python, and binary records. Each request is run
  twice and produces byte-identical results.
- The 54 accepted timelines include RX/TX start/end, parity choices and errors,
  every stop width and invalid stop, BREAK, IDLE, packet delimiters and lengths,
  5–9 data bits, MSB/LSB order, formatting, inversion, sample-point boundaries,
  malformed stop/parity and incomplete traffic.
- All 50 direct option rows bind to an existing accepted UART timeline and
  reproduce its entire result. All 77 unsupported rows raise stable
  `options rejected` during `DecodeRequest` construction; a patched spawn path
  would fail immediately if reached.
- RX-only and TX-only missing pins are exactly integer `0xFF`. A separate
  `rx=17`, `tx=3`, capture order `(3, 17)` case proves noncontiguous reordered
  mapping is resolved by capture position rather than physical ID.
- Hostile mutations of a declaration, record coordinate, emission order, and
  annotation text/canonical bytes all make the comparator fail. Rebinding a
  direct matrix row to a different valid fixture also fails, demonstrating
  non-vacuous fixture binding.
- UART initializer, decoder, and both `common.srdhelper` snapshot digests are
  recomputed. Candidate imports remain closed to stdlib, pytest, and the
  private product host/model/compat surface; no decoder snapshot is imported
  into the test process.

## Commands and results

Commands ran from `Software/LogicAnalyzerPy` unless stated otherwise.

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pytest tests/verification/test_c3_b3_uart_conformance.py -q` | `190 passed in 25.59s` (final repeat) |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b3_uart_conformance.py -q` | `107 passed in 18.47s` |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b2_private_host.py -q -k 'test_every_corrected_semantic_timeline_matches_the_closed_private_host and uart'` | `54 passed, 178 deselected in 9.99s` |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b2_private_host.py -q -k 'test_uart_option_rejections or test_option_matrix_rejects_every_unsupported_row or test_option_matrix_materializes_supported_direct_rows'` | `6 passed, 226 deselected in 0.11s` |
| `.venv/bin/ruff check tests/verification/test_c3_b3_uart_conformance.py tests/implementation/test_c3_b3_uart_conformance.py` | `All checks passed!` |
| `git diff --check` (repository root) | clean |

Verification identity: `/root/c3_b3_uart_verify_r1` (`c3-b3-uart-verifier-1`).
No files were staged or committed.
