# C3-B4 immutable candidate collection implementation, round 14

- Identity and role: `c3-b4-public-implementor-1`; bounded verifier-durability
  correction implementor
- Blocked implementation candidate commit/tree:
  `d6cc54afa991f2d6ffed4d9e91cb7d6ebecb9511` /
  `ddb4112a3090229f90684881d21b11cfbfbe8cad`
- Immutable collection candidate commit/tree:
  `c7650876544e477c277200c4f2fcbd23c67fe245` /
  `87e36568aae7fe0cc55cfc1f584cc8b025c52769`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Timestamp: `2026-09-02T08:12:37Z`

## Blocked verifier evidence

Independent round-13 verification correctly blocked before commit because
round 12's `test_candidate_qualified_collection_is_exact` collected the
mutable descendant worktree while excluding only its own module. With the
ignored draft round-13 verifier present it observed `1468/1506` rather than the
literal `1460/1498`. A descendant worktree cannot provide immutable evidence
for candidate `c7650876544e477c277200c4f2fcbd23c67fe245`.

## Implementation and validation

Round 12 now obtains both the workflow partition and test tree from immutable
candidate `c7650876544e477c277200c4f2fcbd23c67fe245`. It reads the candidate
workflow with `git show`, then uses `git archive` on
`c765087…:Software/LogicAnalyzerPy` with an explicit
`Software/LogicAnalyzerPy/` prefix. It does not create a git worktree or mutate
`.git`.

Every tar member is checked to be relative, free of `..`, and rooted beneath
`Software/LogicAnalyzerPy/`. Extraction additionally uses tarfile's `data`
filter. The unique destination is created under ignored repository
`.tmp/c3-b4-ci/`; collection runs from the extracted
`Software/LogicAnalyzerPy` with `PYTHONPATH` bound to its extracted `src`, a
candidate-local temporary directory, bytecode disabled, and pytest's cache
provider disabled. The directory is removed in `finally`, including on failure.

The immutable candidate arithmetic is exactly `1459/1497 tests collected (38
deselected)`. Descendant tests, tracked or untracked, cannot enter that
collection. An implementation regression requires candidate `git show` and
`git archive`, safe member validation and extraction, extracted cwd and
PYTHONPATH, cleanup, and the candidate arithmetic; it rejects collection from
the mutable `ROOT` and the old self-module exclusion.

The preserved ignored draft
`.tmp/c3-b4-ci/r13-verifier-draft/test_c3_b4_public_round13.py` was present
during focused proof. The durability regression and round-12 immutable
collection node passed `2 passed in 2.62s`; the draft did not affect candidate
counts. No `r12-c765-*` directory remained afterward.

Ruff on the changed Python files, `git diff --check`, and the explicit
unchanged-workflow check passed. The final full partition collected 1,509
items, deselected the unchanged 38 cases, and selected 1,471; result was `1464
passed, 7 skipped, 38 deselected, 106 warnings in 237.48s`. The skips remain
classified loopback, optional physical artifacts, and local absence of hosted
artifact paths.

Changed paths and pre-commit hashes:

- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `bbad162e00ae46a7f290593e6509dd42d47e780a7be519bc7be2b2b439312c57`;
- `Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round12.py` —
  `e52f86cbfb32c2980980a11bac8c83c72b1d2ef8b4f2c70152c74dbdecbe39a0`;
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-14.md` —
  this implementation record.

The workflow is unchanged at SHA-256
`12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`
and retains exactly 15 ignores / 37 selector strings / 38 cases. No product,
decoder, threshold, limit, B1/B2/B3 fixture, lock, manifest, contract, or prior
evidence byte changed. No network, hosted dispatch, or external mutation was
performed.

## Verdict and boundary

Candidate-qualified collection is now independent of all descendant worktree
state, and the unchanged full partition is green. Fresh independent
verification and root-owned hosted dispatch remain required, so the verdict is
`candidate-not-accepted`.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.
