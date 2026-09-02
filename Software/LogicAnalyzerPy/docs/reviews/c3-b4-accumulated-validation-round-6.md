# C3-B4 accumulated validation, round 6

- Orchestrator role: root accumulated-validation and hosted-dispatch owner
- Timestamp: `2026-09-02T01:19:00Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Round-8 implementation candidate/tree: `fefc3307c2de0a680bf44cdcbbabf2e804495a4a` /
  `489ae588679ea4306c49304c0c1e40733b9f7938`
- Independently verified evidence commit/tree exercised by this gate:
  `68ccf70dbdfd2d1312c16a3b601847913e9d003b` /
  `2914e14ea131d20b271cd79d021cd87b9c4c6d5b`
- Prior failed diagnostic evidence commit: `b2b7fa24d0b90c96fb8da7295b861eb8021102f0`

## Exact local verification

Fresh independent round-8 verification passed. One focused pytest command under
inherited ignored SIGTERM executed the original two-parameter forced-kill function and
the evidence-backed round-3 singleton in exact order: three cases passed. The broad
command ran only on focused success and deselected both nodes so none executed twice.

Candidate-qualified collection selected 1,442 of 1,460 cases with exactly 18
deselected through 17 ordered unique selectors. The full descendant sweep completed
with `1,445 passed, 6 classified skips, 18 deselected in 232.32s`; subtracting the nine
fresh verifier cases gives candidate arithmetic of 1,436 passes, six skips, and
eighteen deselections, plus the three focused passes. All retained round-6/round-7 and
current B2/B3/B4 coverage passed. V001 through V004, full-history checkout, bytecode
suppression, Intel runner guard, bounded diagnostic, product/static, frontend,
resources, manifests, locks, metadata, CLI, licenses, and process/import audits all
passed with no governed product drift.

## Exact hosted failure

The exact evidence commit was pushed to dedicated branch
`cycle3-b4-ci-68ccf70`. GitHub Actions run
[`33578403022`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33578403022),
job
[`100087285659`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33578403022/job/100087285659),
resolved exact head `68ccf70dbdfd2d1312c16a3b601847913e9d003b` on the governed
`macos-15-intel` runner and concluded `failure`.

The architecture guard, full-history checkout, Python and Node setup, hash-locked core
installation, dependency check, Ruff, production mypy, strict installed-consumer
typing, and the three-case focused inherited-SIGTERM command passed. The broad suite
then failed exactly one accepted B1 raw-environment identity verifier:

`tests/verification/test_c3_b1_raw_baseline_candidate_replacement.py::test_candidate_identity_digest_environment_schema_and_summary_arithmetic`

The workflow requested the floating setup-python value `3.12`, and the hosted action
resolved CPython 3.12.10. Accepted raw B1 evidence binds the governed environment's
exact CPython 3.12.13 `sys.version`; therefore the immutable verifier correctly rejected
3.12.10. The bounded annotation preserved both values and the exact failing node. The
hosted result was `1 failed, 1446 passed, 4 skipped, 18 deselected, 149 warnings in
283.74s`.

This is not a decoder or B1-verifier defect. The accepted B1 reviews repeatedly bind
the qualification environment to CPython 3.12.13, while the Cycle 3 goal permits
Python 3.12. The evidence supports pinning the hosted setup action to exact 3.12.13;
it does not support ignoring or deselecting the accepted verifier.

All later CLI, web, frontend, asset, and browser steps were skipped by normal fail-fast
behavior. Status and annotation polling used the saved read-only `rtk curl` class with
files under repository-ignored `.tmp/`, followed by separate local JSON parsing. One
transient DNS failure was retried with the same saved class. No workflow rerun,
repeated approval class, artifact publication, or conveyance occurred.

## Disposition

Local verification passes, but the mandatory exact-candidate hosted gate fails because
its floating patch-level interpreter does not match the accepted B1 environment. B4 is
not accepted. A bounded exact-Python correction, fresh independent verification,
accumulated validation, and exact-candidate hosted dispatch remain required.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, publication, or conveyance
was performed.

Verdict: `fail`. `APPROVAL_NEEDED`: none.
