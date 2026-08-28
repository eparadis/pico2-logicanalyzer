# C3-B1 pre-execution runner fixture rebinding — verification round 4

## Subject and verdict

- Verifier: `c3-b1-pre-execution-runner-rebinding-verifier-4`.
- Implementor: `c3-b1-pre-execution-runner-implementor-replacement-4`.
- Finding dispositions: `C3B1-RA001` replacement candidate and
  `C3B1-RV002` portable-inventory correction.
- Candidate commit/tree:
  `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` /
  `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Completed: `2026-08-28T16:41:16Z` on Darwin `24.6.0` x86_64 with
  repository-local Python `3.12.13`.
- Verdict: `pass`.

This verdict is only fresh static/inert verification of the exact replacement
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
The record labels the candidate not accepted, preserves RA001's conservative
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
| round-4 verifier test | `c05cc1290cf0ba4d0e6023a2d13ddc3e7ac016af2256419c70541d8a5373fb18` |

Git-object comparison proves every bound artifact is byte-identical between
superseded candidate `55d22640334ef05176568f275c3e4e7ec63c3336` and the
subject candidate. The binding closes all 24 source paths and exact digests.
Its accepted fixture remains commit/tree
`3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
`14c010153ea5542617e601e4126047c561a48483`, and the cap document still
contains exactly 17 uniquely identified positive integer values.

## Portable include-only boundary and RV002 disposition

The portable inventory begins with `git ls-tree` over the immutable candidate,
not a worktree glob. The candidate contains exactly **51 tracked test modules**.
Adding only the current round-4 verifier produces the clean evidence-descendant
inventory of **52 modules**: **40 included** and **12 excluded**. The sets are
disjoint and exhaustive. The optional B2 path and superseded verifier-3 are
both absent in that clean state and neither is required.

The separately checked main-worktree pathname inventory contains **54 modules**:
the same **40 included** plus **14 excluded**, including both inherited
superseded verifier-3 and optional preserved
`tests/implementation/test_c3_b2_private_host.py`. The optional B2 file was
classified by pathname only; it was not copied, materialized, opened, imported,
or executed. Both states apply the same fail-closed rule: every `test_c3_*`
module is excluded unless it is exactly the current fixture implementation,
current runner implementation, or round-4 verifier module. A synthetic unknown
future C3 pathname was proved excluded.

This closes `C3B1-RV002`: verifier-3 commit `14c5bdc` and its non-portable pass
remain immutable history and transfer no authority. The new proof neither
requires nor consumes untracked B2 content.

Before any test execution, the verifier named the exact include-only paths:
the candidate's 39 tracked non-`test_c3_*` test modules plus only
`tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py`. The explicit
40-path `pytest --collect-only -q` command collected exactly **584 tests**. It
used no directory, glob, marker expression, superseded verifier, raw,
threshold, final, manifest/checkpoint, B2, or downstream module. Only the
round-4 static verifier and current 177-test inert runner module were then run.

## Commands and exact results

All pytest/generator commands used `PYTHONDONTWRITEBYTECODE=1` and the
repository-local Python 3.12 environment.

- Exact 40-path collection-only audit: **584 tests collected**, exit 0; no
  tests executed.
- Static round-4 verifier only: **10 passed**, exit 0.
- Complete inert/hostile current runner implementation suite: **177 passed**,
  exit 0.
- Canonical binding
  `.venv/bin/python -m tools.cycle3_characterize.binding --check`: exit 0.
- Deterministic fixture generator
  `.venv/bin/python scripts/generate_cycle3_fixtures.py --check`: exit 0.
- Scoped Ruff over all runner tool modules, the runner implementation suite,
  and verifier-4: `All checks passed!`, exit 0.
- Strict mypy over all seven runner modules:
  `Success: no issues found in 7 source files`, exit 0.
- Candidate/tree, one-record delta, git-object equality, 24-source digest
  closure, accepted fixture identity, 17-cap uniqueness/positivity, both
  inventory partitions, unknown-module fail-closed behavior, worktree scope,
  and `git diff --check`: passed.

Only this verifier's two assigned evidence paths are new and uncommitted.
Pre-existing untracked B2-owned product, test, and implementation-record paths
were preserved and not modified. No decoder, raw reproduction, snapshot
characterization, B2 route, external/reference runtime, prohibited dependency,
hardware, network, or approval-gated operation executed.

Findings: none. `C3B1-RA001` is correctly preserved and requires the next fresh
safe accumulation and acceptance; `C3B1-RV002` is closed by this portable proof.

`pass`
