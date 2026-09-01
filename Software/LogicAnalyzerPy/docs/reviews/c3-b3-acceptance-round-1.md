# C3-B3 independent acceptance — round 1

## Identity, environment, and verdict

- Acceptor: `c3-b3-independent-acceptor-1`
  (`/root/c3_b3_accept_r1`), fresh and distinct from every B3 implementor,
  verifier, and accumulated validator.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Accepted B2 checkpoint prerequisite:
  `18614cc812edda68598e19d200f7bb4c87861ebd`.
- Product/evidence candidate commit/tree:
  `0e1f619c8c744c16a96119c0834ed2f7d2518d0e` /
  `d22ecdd374446cef9e4b1e941b0937ae6389a1cb`.
- Assigned acceptance HEAD/tree, containing only the later accumulated-review
  commit: `6eeb43d660eeb9d7e9b55b320921aa108becf068` /
  `a06aa94a23b7fbf4e887816d9c21f31bb3e0466f`.
- Environment: macOS 15.7.9 build 24G830, x86_64, CPython 3.12.13.
- Verdict: **pass**.

This is independent acceptance of the exact ordered B3 record. It does not
transfer the accumulated validator's pass and does not create, precompute,
predict, or verify a B3 manifest or claim a B3 checkpoint.

## Ordered record and role audit

`git rev-list --ancestry-path --reverse 18614cc..6eeb43d` reproduced this exact
linear history: `2507057` preflight, `1811c31` UART baseline, `e5ac88e` UART
implementation, `25d4849` UART verification, `3e6124a` SPI implementation,
`db825ef` SPI verification, `844d69d` I2C implementation, `30b020a` I2C
verification, `970f9a7` R16 implementation, `0e1f619` R16 verification/final
candidate, then `6eeb43d` accumulated validation. Candidate and assigned trees
recomputed exactly as stated above.

The four implementation identities, four fresh verifier identities,
`c3-b3-accumulated-validator-1`, and this acceptor are distinct. The eight test
and eight review hashes in the accumulated record were critically checked
against their frozen commits; their candidate/tree ordering and reviewed scope
agree with Git history. No pass was applied across a correction or different
candidate.

Preserved correction history is coherent and precedes each immutable pass:
UART moved defaults from production to the accepted matrix; SPI separated its
no-CS probe and corrected a verifier-only incomplete-CS expectation; I2C fixed
packed channel order and a verifier-only read-surface/emitted-write
expectation; R16 fixed an inert identity, added the missing packed-sample
hostile control and refreshed command evidence; its verifier fixed Ruff import
grouping. None is an unresolved product finding.

`git diff --name-status 18614cc..6eeb43d` contains exactly the eight B3 tests,
eight B3 implementation/verification reviews, the accumulated-validation
review, and the root-owned orchestration-progress update. No product decoder,
API, CLI, fixture, dependency/lock, workflow, browser/frontend, hardware,
firmware, serial/live-capture, contract, manifest, or checkpoint path changed.

## Independent coverage audit

The accepted artifacts recomputed as follows:

- semantic corpus: 63 timelines and SHA-256
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`;
- option matrix: 165 unique rows and SHA-256
  `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`;
- accepted B1 fixture manifest:
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`;
- accepted C3-B1 evidence:
  `3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`;
- accepted C3-B2 evidence:
  `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`.

The 63 timelines are exactly UART 54, SPI 6, and I2C 3. The 165 option rows are
exactly UART 127 (50 accepted direct/default, 77 unsupported), SPI 30 (10
accepted direct/default, 20 unsupported), and I2C 8 (2 accepted direct/default,
6 unsupported). Thus the earlier assignment typo suggesting 215 rows is
corrected to the immutable accepted count 165; no rows were invented or
duplicated.

R13-R15 cover every timeline and every real matrix row with fixture/matrix-only
expected values, complete typed declarations and emission-ordered records,
canonical bytes, applicable annotation/Python/binary/metadata outputs,
malformed/incomplete and boundary behavior, integer `0xFF` optional-pin
sentinels, noncontiguous/reordered mappings, rejection before spawn, hostile
oracle checks, and repeat determinism. Source hashes/import roots are closed.

R16 independently constructs four sources—direct memory, hand-built schema 1,
independently built schema 2, and explicit-metadata CSV—for six complete
integration mapping classes: UART RX, UART TX, SPI MOSI, SPI MISO, SPI data
with CS, and I2C SCL/SDA. Its 24 private decodes have exact capture identity and
byte-identical canonical results. Schema 1's D0-D7 limit is handled by the
explicit, consistent UART TX D9-to-D4 semantic wire remap. Serial/live capture
is fail-fast trapped. The other 57 timelines remain authoritatively owned by
R13-R15; no semantic pass is transferred from representative R16 sampling.

## Commands and results

Every shell command used the required `rtk` prefix. Commands ran from
`Software/LogicAnalyzerPy` except repository identity, history, scope, and
process checks.

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pytest -q` plus all eight B3 implementation/verifier modules | `421 passed in 58.06s` |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python scripts/generate_cycle3_fixtures.py --check` | exit 0; no drift |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m tools.cycle3_characterize.binding --check` | exit 0; no drift |
| `.venv/bin/python scripts/validate_cycle3_evidence.py docs/evidence-manifest/cycle3-schema.json testdata/evidence/c3-b1.json` | exit 0 |
| same validator/schema over `testdata/evidence/c3-b2.json` | exit 0 |
| `.venv/bin/python -m ruff check` over all eight B3 modules | `All checks passed!` |
| `git diff --check` | exit 0, no output |
| `jq` timeline and row grouping plus `shasum -a 256` over accepted inputs | 54/6/3 timelines; 127/30/8 rows; hashes above |
| prohibited-runtime `rg` over `src`, `tools`, `pyproject.toml`, and `requirements-dev.lock` | exit 1, zero matches |
| `git diff --name-status 18614cc..6eeb43d` and ordered ancestry/log audit | only the allowed B3 evidence/progress paths; order above |
| eight separate already-approved `rtk proxy pgrep -fl PATTERN` checks | all exit 1/empty; no worker, pytest, vite, playwright, characterization, dotnet, sigrok-cli, or libsigrokdecode process |

An initial direct-file invocation of `tools/cycle3_characterize/binding.py
--check` failed with the expected relative-import error because the tool is a
package module. The authoritative invocation used `python -m
tools.cycle3_characterize.binding --check` and passed. This is command-shape
correction only, not candidate drift or a product finding.

The accumulated validator's broader `1359 passed, 4 skipped, 1 deselected`
non-hardware run was audited rather than adopted as this verdict. The four
skips are optional C2-B3 machine-local physical-artifact reruns and the one
deselection is the established superseded B1 inventory assertion; no mandatory
Cycle 3 gate was skipped. The fresh 421-test complete B3 rerun and inherited
B1/B2 manifest/drift checks provide a proportionate decisive independent
subset.

## Requirements, stopping conditions, findings, and limits

- R13-R15 / stopping condition 9: pass for all 63 timelines, all 165 accepted
  matrix rows, mappings, boundaries, output kinds, sentinels, and repeatability.
- R16 / condition 10: pass for four inert source representations across all six
  integration mapping classes, without physical I/O.
- R21 / condition 13: pass continuously for B3. Static dependency/import/lock/
  command scope and the final process inventory show no prohibited runtime use.
- R23 / condition 14: pass continuously for B3. Accepted B1/B2 manifests,
  fixture binding/generation, inherited behavior and macOS-only qualification
  remain intact; the broader accumulated regression evidence is credible and
  internally consistent.
- R24 / applicable condition-16 portion: pass. Candidate, role, correction,
  finding, review, accumulated-validation, and deferred-manifest ordering is
  auditable. The final five-checkpoint condition is not claimed at B3.
- R25 / condition 17: pass continuously for B3. No excluded browser/API/
  frontend decoder, hardware, firmware, serial/live capture, dynamic discovery,
  stacking, `.lac`, packaging/publication, platform, lock, or workflow scope
  expanded.

Findings: no candidate or product finding. The 215-to-165 count correction and
the package-module command correction above are fully disposed evidence notes.
No external decoder, C#/.NET, pythonnet, libsigrokdecode, sigrok-cli, hardware,
serial device, browser, hosted CI, network, packaging, or publication action was
performed or relied upon. Physical reruns and broader platform claims remain
out of scope. No approval was needed.

This pass authorizes only the root orchestrator to create the post-acceptance
B3 manifest for this exact unchanged ordered record. It does not authorize a
changed candidate, predict manifest verification, or claim checkpoint status.

`pass`
