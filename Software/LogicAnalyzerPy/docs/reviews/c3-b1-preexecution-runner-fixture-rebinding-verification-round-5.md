# C3-B1 pre-execution runner fixture rebinding — verification round 5

## Subject and verdict

- Verifier: `c3-b1-pre-execution-runner-rebinding-verifier-5`.
- Implementor: `c3-b1-pre-execution-runner-implementor-replacement-4`.
- Finding dispositions: `C3B1-RA001` replacement candidate and portable
  corrections for `C3B1-RV002` and `C3B1-RV003`.
- Candidate commit/tree:
  `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` /
  `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Completed: `2026-08-28T16:50:27Z` on Darwin `24.6.0` x86_64 with
  repository-local Python `3.12.13`.
- Verdict: `pass`.

This verdict is fresh static/inert verification of only the exact replacement
runner candidate. It makes no accumulated-validation, acceptance, raw-baseline,
threshold, final-B1, manifest, checkpoint, B2, product, decoder-execution, or
future claim and grants no snapshot-execution authority.

## Exact candidate and unchanged-byte proof

The diff from immutable RA001 record commit
`91ee8f818ce6bb26196d673cdf6975e9a7248d6a` to the candidate is exactly one new
path:
`docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-implementation-round-3.md`.
Its independently recomputed SHA-256 is
`bbf2cb087ec97790c2403b7406560656d84ebb4f600190a3a881c7143fa8bf0e`.
The record keeps the candidate not accepted, preserves RA001's conservative
possible-launch classification, transfers no result or authority from the
interrupted command or later diagnostics, and requires fresh verification,
safe accumulation, and acceptance.

The method, runner, canonical binding, implementation test, semantic fixture,
fixture manifest, and cap hashes independently recomputed as:

| Artifact | SHA-256 |
| --- | --- |
| `docs/cycle-3-characterization-method.md` | `f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341` |
| `tools/cycle3_characterize/runner.py` | `0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80` |
| `tools/cycle3_characterize/candidate-binding.json` | `4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7` |
| `tests/implementation/test_cycle3_preexecution_runner.py` | `1511083a3254a44bd95f33f75d9cf5adb022162b20a9e0c274929f4f9325ad19` |
| `testdata/decoders/cycle3/semantic-fixtures.json` | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| `testdata/decoders/cycle3/manifest.json` | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| `testdata/decoders/cycle3/experiment-caps.json` | `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d` |
| round-5 verifier test | `f84f123e6f8bbc1c3bcb1063faa11d0177438012db8b6ec314248b8c1d0984b1` |

Git-object comparison proves every bound artifact is byte-identical between
superseded candidate `55d22640334ef05176568f275c3e4e7ec63c3336` and the
subject candidate. The binding closes all 24 source paths and exact digests.
Its accepted fixture remains commit/tree
`3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
`14c010153ea5542617e601e4126047c561a48483`, and the cap document still
contains exactly 17 uniquely identified positive integer values.

## Portable include-only boundary and finding dispositions

The inventory begins with `git ls-tree` over the immutable candidate, never a
worktree glob. The candidate contains exactly **51 tracked test modules**.
Adding only verifier-5 produces the clean evidence-descendant inventory of
**52 modules**: **40 included** and **12 excluded**. The sets are disjoint and
exhaustive. Neither optional B2 nor superseded verifier-3/verifier-4 is in that
clean input, and none is required.

The same partition was then tested against a synthetic pathname-only state
formed by adding optional
`tests/implementation/test_c3_b2_private_host.py` and both superseded verifier
pathnames. The resulting **55-module** inventory retains exactly the same
**40 included** paths and has **15 excluded** paths. The optional B2 pathname
and both superseded verifiers are in the excluded set. No optional path was
looked up in the live filesystem; in particular, B2 content was not opened,
read, copied, imported, collected, or executed. A synthetic unknown future C3
pathname also fails closed.

Every `test_c3_*` module is excluded unless it is exactly the current fixture
implementation, current runner implementation, or verifier-5. The candidate's
excluded set independently covers the known raw-baseline, threshold-proposal,
final-candidate, prior runner-candidate, prior runner-verifier, and semantic
fixture candidate classes. Static import inspection of every ordinary included
module proves none directly imports the decoder product, snapshot host, raw
candidate, or B2 host. The explicitly permitted inert runner suite imports
snapshot-host validation helpers but does not launch characterization.

This closes the portability correction required by `C3B1-RV003` without
transferring either verifier-4's pass or verifier-3's pass. It also preserves
the independent `C3B1-RV002` no-authority disposition. `C3B1-RA001` remains
preserved and requires the next fresh safe accumulation and acceptance.

Before any execution, the verifier named the exact include-only paths: the
candidate's 39 tracked non-`test_c3_*` modules plus verifier-5. The explicit
40-path `pytest --collect-only -q` command collected exactly **585 tests**. It
used no directory, glob, marker expression, superseded verifier, raw,
threshold, final, manifest/checkpoint, B2, or downstream module. Only verifier-5
and the complete 177-test inert runner implementation suite were executed.

## Commands and exact results

All pytest and generator commands used `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONPATH=src`, and the repository-local Python 3.12 environment where
applicable.

- Exact 40-path collection-only audit: **585 tests collected**, exit 0; no
  tests executed.
- Static verifier-5 plus complete inert/hostile runner implementation suite:
  **188 passed** (**11 verifier + 177 runner**), exit 0.
- Canonical binding
  `.venv/bin/python -m tools.cycle3_characterize.binding --check`: exit 0.
- Deterministic fixture generator
  `.venv/bin/python scripts/generate_cycle3_fixtures.py --check`: exit 0.
- Scoped Ruff over all runner tool modules, the runner implementation suite,
  and verifier-5: `All checks passed!`, exit 0.
- Strict mypy over all seven runner modules:
  `Success: no issues found in 7 source files`, exit 0.
- Candidate/tree, one-record delta, Git-object equality, 24-source digest
  closure, accepted fixture identity, 17-cap uniqueness/positivity, portable
  inventory partitions, unknown-module fail-closed behavior, and
  `git diff --check`: passed.

Only this verifier's two assigned evidence paths are new and uncommitted.
Pre-existing untracked B2-owned product, test, and implementation-record paths
were preserved and not modified. No decoder, raw reproduction, snapshot
characterization, B2 route, external/reference runtime, prohibited dependency,
hardware, network, or approval-gated operation executed.

Findings: none.

`pass`
