# C3-B1 pre-execution runner fixture rebinding — verification round 3

## Subject and verdict

- Verifier: `c3-b1-pre-execution-runner-rebinding-verifier-3`.
- Implementor: `c3-b1-pre-execution-runner-implementor-replacement-4`.
- Finding disposition: `C3B1-RA001`, replacement after the invalid
  pre-acceptance accumulated ordering at `91ee8f818ce6bb26196d673cdf6975e9a7248d6a`.
- Candidate commit/tree:
  `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` /
  `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Verdict: `pass`.

This verdict is only the fresh static/inert verification of the exact
replacement runner candidate. It makes no accumulated-validation, acceptance,
raw-baseline, threshold, final-B1, manifest, checkpoint, B2, product, or future
claim and grants no snapshot-execution authority.

## Exact candidate and unchanged-byte proof

The diff from the immutable RA001 record commit to the candidate is exactly one
new path:
`docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-implementation-round-3.md`.
Its SHA-256 is
`bbf2cb087ec97790c2403b7406560656d84ebb4f600190a3a881c7143fa8bf0e`.
The record honestly labels the candidate not accepted, preserves RA001's
conservative possible-launch classification, transfers no result or authority
from the interrupted command or later diagnostics, and requires fresh
verification, safe accumulation, and acceptance.

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
| round-3 verifier test | `6d22700759de3696838859aa87e9bb951dfe3077c3956861e1e5cd46c6a30554` |

Git object comparison proves each bound artifact is byte-identical between
superseded candidate `55d22640334ef05176568f275c3e4e7ec63c3336` and
this candidate. The binding closes all 24 source paths and exact digests. Its
accepted fixture remains commit/tree
`3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
`14c010153ea5542617e601e4126047c561a48483` with the semantic and manifest
hashes above. The cap document still contains exactly 17 unique, positive,
integer cap values. Thus the previously reviewed complete inert/hostile
containment matrix remains byte-for-byte unchanged; no earlier verdict is
transferred.

## Include-only pre-acceptance boundary

The new verifier statically enumerated all **53** `test_*.py` modules currently
present in the repository worktree before any accumulated execution. Exactly
**40** are in the include-only partition: inherited non-Cycle-3 regressions,
the accepted fixture implementation module, the current 177-test runner
implementation module, and this round-3 verifier. Exactly **13** are excluded.
The sets are disjoint and exhaustive, and an unknown future `test_c3_*` module
fails closed unless it is one of those three current gate modules.

The excluded set contains every currently present raw-baseline,
threshold-proposal, final-B1, superseded runner/fixture exact-candidate, and B2
module. No distinct Cycle 3 evidence-manifest, manifest-verification,
checkpoint, or final accumulated/acceptance test module currently exists; the
exhaustive enumeration proves none silently entered the include set. The B2
private-host module is present only as deliberately preserved untracked work
and is explicitly excluded. Direct-import auditing rejects private decoder,
raw-verifier, B2-host, or snapshot-host routes in the general included set.
The sole deliberate snapshot-host import is the contract-required current
runner implementation suite, whose unchanged tests statically inspect and
negatively exercise inert/hostile containment and disabled characterization.

The collection-only command named all 40 paths explicitly and collected
**581 tests**. It named no directory, glob, marker expression, or excluded
module and executed no test. This is the required allowlist boundary; an
unfiltered or marker-filtered broad pytest command remains forbidden before
fresh runner acceptance.

## Commands and results

All Python commands used the repository-local Python 3.12 environment with
bytecode writes disabled where pytest or generators ran.

- Static round-3 verifier only: **7 passed**.
- Complete inert/hostile current runner implementation suite: **177 passed**.
- Canonical binding check: passed.
- Deterministic fixture generator check: passed.
- Scoped Ruff over all runner tool modules, the runner implementation suite,
  and the new verifier: passed.
- Strict mypy over all seven runner Python modules: passed, seven source files.
- Explicit 40-module collection-only audit: **581 tests collected**; no tests
  executed and all 13 excluded modules absent.
- Candidate/tree, one-record delta, git-object equality, 24-source digest
  closure, accepted fixture identity, 17-cap uniqueness/positivity, worktree
  ownership, and `git diff --check`: passed.

Only the two assigned new verifier evidence paths are uncommitted. The three
pre-existing untracked B2 owned paths were preserved and not modified. No
decoder, raw reproduction, snapshot characterization, B2 route, external
runtime, hardware, network, or prohibited dependency executed. No approval
capability was needed.

Findings: none.

`pass`
