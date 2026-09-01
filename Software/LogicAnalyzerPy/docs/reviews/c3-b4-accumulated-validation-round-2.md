# C3-B4 accumulated validation, round 2

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Independently verified B4 evidence commit/tree:
  `e3b169f8744c6f4ff80d6a06172d86b14cd49085` /
  `4567fdae34e1a0d37b0e7d5b1fd277f56a2f5737`.
- Completed: `2026-09-01T22:49:41Z`.
- Verdict: **changes_required**. The fresh local accumulated gate passed and
  hosted x86_64 selection passed, but hosted pytest did not use the governed
  applicable-test partition.

This failed gate authorizes no acceptance, manifest, checkpoint, publication,
or Cycle 4 work. Neither the previous arm64 failure nor this new failure is
retried, waived, or represented as success.

## Fresh ignored-local clean gate

All temporary clone, environment, Node, and downloaded CI metadata paths were
created below the repository's ignored `.tmp/` directory. The exact candidate
was cloned without shared hardlinks. A fresh clone-local `.venv` used CPython
3.12.13; hash-locked dependencies were installed from the already verified
wheelhouse, followed by the editable product with `--no-build-isolation
--no-deps`. `pip check` passed.

The exact governed applicable non-hardware partition used the accepted 15
superseded-B1 ignores and one frozen historical fixture-surface deselection. It
completed with **1427 passed, four classified optional physical-artifact skips,
one historical deselection, and 149 inherited warnings in 238.75 seconds**.
No mandatory Cycle 3 check skipped.

Ruff, production mypy over 31 source files, strict characterization mypy,
fixture generator and binding checks, all six Cycle 2 manifests, C3-B1 through
C3-B3 manifests, installed CLI help and decode grammar, process cleanup, and
prohibited runtime searches passed. Exact official Node 22.14.0 archive
SHA-256
`6698587713ab565a94a360e091df9f6d91c8fadda6d00f0cf6526e9b40bed250`
matched the governed value. The locked 215-package install, ESLint, TypeScript,
three Vitest files/five tests, 29-module Vite build, and production asset check
all passed.

## Exact-candidate hosted result

Root pushed exact commit `e3b169f8744c6f4ff80d6a06172d86b14cd49085`
to dedicated branch `cycle3-b4-ci-e3b169f`. GitHub Actions run
`33567808584`, job `100054884701`, resolved that same SHA and concluded
`failure`. The new first architecture step passed on exact x86_64, closing the
round-1 arm64 environment-class defect. Checkout, Python 3.12, Node 22.14.0,
clean dependency installs, Ruff, production mypy, and strict installed public
consumer checking also passed.

The non-hardware pytest step failed because its workflow command remained the
unfiltered `pytest -m "not hardware"`. Hosted annotations show failures in
the exact superseded modules governed out of the accepted partition, including
`test_c3_b1_runner_fixture_rebinding_round5.py` and
`test_c3_b1_semantic_fixture_correction.py`. They attempt historical Git
revisions unavailable in Actions' shallow checkout and assert intentionally
superseded fixture/import digests. The candidate's clean local governed
partition passes; that local result cannot waive the wrong hosted command.

## Required correction

Make the hosted pytest invocation byte-explicitly use the same accepted 15
superseded-B1 `--ignore` entries and the one frozen fixture-surface
`--deselect` used by the B2/B3 and current B4 accumulated gates. Add workflow
regression coverage that fails if any entry is missing, duplicated, or if a
mandatory current B2/B3/B4 module is excluded. Preserve the x86_64 runner
selection, all other workflow steps, all product bytes, and all governed
fixtures, limits, thresholds, locks, and manifests.

The correction requires a new immutable candidate, fresh independent B4
verification, complete fresh accumulated validation, and a new exact-candidate
hosted run. The B1 rights-holder/counsel limitation remains controlling. No
wheel, sdist, upload, conveyance, or publication occurred.

`changes_required`
