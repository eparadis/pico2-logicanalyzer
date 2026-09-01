# C3-B3 SPI verification — round 1

## Verdict and scope

**PASS — independently verified, SPI-only.** Frozen candidate commit
`3e6124ab68d1bcea7df628c520741add93658350` and tree
`c4d88ada4bc6c0869b53b5f19f7c325c27697112` satisfy the bounded R14 SPI
conformance claim. This verdict does not claim C3-B3 accumulation or acceptance,
checkpoint advancement, UART/R13, I2C/R15, or cross-source/R16 coverage.

The candidate commit changes exactly two paths: the SPI implementation test and
its implementation review. The verification worktree adds only
`tests/verification/test_c3_b3_spi_conformance.py` and this review. No product,
decoder snapshot, fixture, contract, progress, or checkpoint path was modified.
No unrelated concurrent changes were observed.

## Independent oracle and coverage

The verifier independently reconstructs packed captures and complete expected
decode results from only the accepted B1 semantic corpus, option matrix, and
provenance evidence. It does not import the candidate test or use production
decoder values/defaults as an oracle. AST checks additionally close the
candidate's import roots and confirm its default helper exists; the verifier's
five defaults are selected from the matrix's unique default-classification rows
and asserted literally.

Coverage includes all 6 accepted timelines and their full typed/canonical
results; all 10 direct rows and fixture bindings; all 20 unsupported rows with a
spawn trap; all five defaults; annotation, binary, metadata, Python, SPI DATA,
and tagged `spi-data` semantics; CPOL/CPHA 0/1, MSB/LSB order, active-low/high
CS, word sizes 1 and 8, and rejection at 9; incomplete traffic; exact MISO-only,
MOSI-only, and no-CS `0xFF` sentinels plus complete `has_channel` arrays;
noncontiguous/reordered physical mappings; repeat determinism; and closed
snapshot import roots/hashes.

Hostile checks independently mutate declarations, record values and order,
Python tags, nested `spi-data` tags, binary bytes, metadata, channel mappings,
options, defaults, and the word-size boundary. Every mutation is distinguished
from the accepted observed result or rejected as required.

Accepted identities were rechecked exactly:

- semantic corpus: `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`
- option matrix: `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`
- B1 fixture-manifest reference: `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`
- accepted B2 manifest: `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`
- SPI file set: `96bbaf9f3325196e9a4cea856194355a1b788022ed7457781371cdd4de38c193`
- `sigrokdecode.py`: `385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a`
- `spi/__init__.py`: `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c`
- `spi/pd.py`: `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d`
- frozen candidate test: `e35c8d2ac472a7ae4c557daaba54521696971f871ef158d794c3d754cfdc0250`

## Validation evidence

Commands were run from `Software/LogicAnalyzerPy` unless noted. The mandatory
`rtk` prefix was used for every shell command.

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pytest tests/verification/test_c3_b3_spi_conformance.py -q` | `52 passed in 4.89s` |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b3_spi_conformance.py -q` | `20 passed in 2.67s` |
| `.venv/bin/python -m pytest tests/implementation/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host_round2.py tests/verification/test_c3_b2_private_host_round3.py tests/verification/test_c3_b2_private_host_round4.py -q -k 'spi or option_type_and_boundary or tagged_value'` | `15 passed, 298 deselected in 1.04s` |
| `.venv/bin/ruff check tests/verification/test_c3_b3_spi_conformance.py tests/implementation/test_c3_b3_spi_conformance.py` | `All checks passed!` |
| `git diff --check` | clean |

An earlier verifier-only run produced `51 passed, 1 failed`: the new test had
incorrectly assumed incomplete no-CS traffic emitted no records. The accepted
corpus specifies one initial tagged `CS-CHANGE` record. The verifier was fixed
to assert that exact record, after which all validation passed. This was not a
candidate or product defect.

## Findings and disposition

No candidate or product defect was found. No approval, network, external
reference decoder, hardware, serial, browser, or fixture/product mutation was
needed. Disposition: **PASS for the bounded R14 SPI candidate verification**.
