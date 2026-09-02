# C3-B4 accumulated validation, round 5

- Orchestrator role: root accumulated-validation and hosted-dispatch owner
- Timestamp: `2026-09-02T00:47:00Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Round-7 diagnostic candidate/tree: `f3565c11c1d7ea4351349d141401c6f98ba3940d` /
  `e0346acdcc6ea64369ba612237eb583e66311bf8`
- Independently verified evidence commit/tree exercised by this gate:
  `0bbc93dd722105f1080096454140c610b8843057` /
  `d943802b2913a3c67ba6c435c01ed03215dae734`
- Prior failed accumulated evidence commit: `79ee8e6b004e21d20fd3fc15bec7d6bd45bdbf12`

## Exact local verification

Fresh independent round-7 verification passed. The 1,300-byte raw sanitizer tail,
threefold maximum GitHub escaping, exact 51-byte annotation prefix, and terminating LF
produce an exact worst-case complete command of 3,952 bytes, below GitHub's observed
4,096-character retention bound. A real pytest failure suffix retained its `FAILED`
node, assertion, and final summary after a longer prefix was discarded.

The candidate-qualified collection selected 1,438 of 1,450 cases with exactly 12
deselected through 11 ordered unique selectors. The full descendant sweep completed
with `1,442 passed, 6 classified skips, 12 deselected in 230.65s`; subtracting the ten
fresh verifier cases gives candidate arithmetic of 1,432 passes, six skips, and twelve
deselections. The second SIGTERM-sensitive round-3 node remained selected and passed
locally. The focused inherited-SIGTERM proof passed its two parameters. V001 through
V004, full-history checkout, bytecode suppression, Intel runner guard, product/static,
frontend, resources, manifests, locks, metadata, CLI, licenses, and process/import
audits all passed with no governed product drift.

## Exact hosted diagnostic and identified failure

The exact evidence commit was pushed to dedicated branch
`cycle3-b4-ci-0bbc93d`. GitHub Actions run
[`33576227664`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33576227664),
job
[`100080675146`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33576227664/job/100080675146),
resolved exact head `0bbc93dd722105f1080096454140c610b8843057` on the governed
`macos-15-intel` runner and concluded `failure`.

The architecture guard, full-history checkout, Python and Node setup, hash-locked core
installation, dependency check, Ruff, production mypy, strict installed-consumer
typing, and the existing focused inherited-SIGTERM proof all passed. The broad suite
then failed in the exact previously hidden node:

`tests/verification/test_c3_b2_private_host_round3.py::test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation`

The child exited during the terminate phase before its script installed its own
SIGTERM-ignore handler, so the immutable observation contained
`terminate_to_reap_ns=1337415` and `kill_to_reap_ns=0`; the assertion requires
`kill_to_reap_ns > 0`. The test itself completed in 0.23 seconds. This is the same
startup race seen diagnostically under local concurrent load and is now proven under
the governed hosted Python 3.12 environment.

The second reported pytest failure was the fresh round-7 verifier's retained-node
subprocess assertion. That verifier deliberately executes the same round-3 node and
requires a zero return code; it therefore propagated the exact same underlying race.
It is not a second product defect. The final hosted arithmetic was `2 failed, 1442
passed, 4 skipped, 12 deselected, 149 warnings in 327.52s`.

The corrected 1,300-byte diagnostic retained the exact failing node, assertion,
observation, and final summary within the public GitHub annotation. No authenticated
log access, inference, retry, or waiver was needed. All later CLI, web, frontend,
asset, and browser steps were skipped by normal fail-fast behavior.

Status and annotation polling used the saved read-only `rtk curl` class with files
under the repository's ignored `.tmp/` directory, followed by separate local JSON
parsing. No repeated approval class, rerun, artifact publication, or conveyance
occurred.

## Disposition

The diagnostic objective passed, but the mandatory exact-candidate hosted gate failed.
B4 is not accepted. The evidence now supports adding this exact singleton to the one
focused pytest command that inherits ignored SIGTERM, followed by transparent broad
deselection so it still executes exactly once. A fresh correction, independent
verification, accumulated validation, and exact-candidate hosted dispatch remain
required.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, publication, or conveyance
was performed.

Verdict: `fail`. `APPROVAL_NEEDED`: none.
