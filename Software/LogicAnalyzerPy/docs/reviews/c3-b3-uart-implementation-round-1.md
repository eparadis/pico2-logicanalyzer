# C3-B3 UART implementation — round 1

## Scope and verdict

Status: **candidate-not-accepted**. This bounded C3-B3 implementation adds
only independent UART conformance evidence in
`tests/implementation/test_c3_b3_uart_conformance.py`; it does not alter a
decoder snapshot, product source, fixture, host, or public surface. No SPI,
I2C, R16, B4, or later work was begun. No product defect was found, so no
product change is proposed.

The checks derive expected output solely from the checked-in accepted UART
semantic fixture content and accepted option matrix. A timeline's selected
options are completed only from the matrix's 13 unique UART
`classification=default` rows; the module asserts that exact closed key set
and direct-fixture disposition. The test module does not hardcode fixture
output or inspect production host defaults.

## Candidate checks

- 54 UART timelines are each reconstructed from their declared transitions
  and mapping, decoded through a fresh private worker, and compared as full
  `DecodeResult` values (including declarations and all emission-ordered typed
  records). The corresponding canonical JSON bytes also compare exactly.
- 50 direct UART option rows each resolve to and independently run their
  accepted fixture. The corpus contains 77 unsupported UART rows; an
  independent `_spawn_fixed_worker` counter proves every one is rejected by
  `DecodeRequest` before a worker can be created.
- RX-only and TX-only compatibility pin sequences are exact, including
  `[1, 255]` and `[255, 0]`; an additional host check proves noncontiguous,
  reordered physical mappings (`rx=19`, `tx=7`, capture order `(7, 19)`).
- The accepted timelines cover start/end, parity, stop, BREAK, IDLE, packet,
  nine-bit, malformed/incomplete, and repeated byte identity behavior.
- Static source-as-data checks reproduce the exact UART initializer, decoder,
  and `srdhelper` digests and limit their direct import roots to the frozen
  closed set.

## Fixture and source identity

Observed SHA-256 values:

| Artifact | SHA-256 |
| --- | --- |
| accepted B1 manifest | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| semantic fixtures | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| option matrix | `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209` |
| UART test candidate | `6ebad5ba914a41904fc6965dbc592e201e0d1bee8211efb030e2bd18a6d5bd16` |

The test asserts UART source digests: initializer
`351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f`,
decoder `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc`,
srdhelper initializer
`125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1`, and
module `602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6`.
It also checks the accepted UART file-set hash
`eb9ee54a167e01c1a40830804912c18f8ebe700e41d9b1ee27707afd4c50d3f3`.

## Validation

All commands were run from `Software/LogicAnalyzerPy` except the final
repository-wide diff and hash command.

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b3_uart_conformance.py -q` | `107 passed in 16.91s` |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b2_private_host.py -q -k 'test_every_corrected_semantic_timeline_matches_the_closed_private_host and uart'` | `54 passed, 178 deselected in 8.46s` |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b2_private_host.py -q -k 'test_uart_option_rejections or test_option_matrix_rejects_every_unsupported_row or test_option_matrix_materializes_supported_direct_rows'` | `6 passed, 226 deselected in 0.08s` |
| `.venv/bin/ruff check tests/implementation/test_c3_b3_uart_conformance.py` | `All checks passed!` |
| `git diff --check` | clean |

No approval, network, external decoder, .NET/C#, libsigrokdecode, sigrok-cli,
hardware, serial, browser path, or fixture/product mutation was used.
