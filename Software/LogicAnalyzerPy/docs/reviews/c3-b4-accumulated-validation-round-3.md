# C3-B4 accumulated validation, round 3

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Independently verified B4 evidence commit/tree:
  `ec805b506ef18f6fc0844d9586764d35aba021ec` /
  `2591ba20af36d3ce903de21020b62e9dddb65ff7`.
- Completed: `2026-09-01T23:22:48Z`.
- Verdict: **changes_required**. The exact local accumulated gate and hosted
  partition selection passed, but three hosted harness assumptions remained.

This failed gate authorizes no acceptance, manifest, checkpoint, publication,
or Cycle 4 work. No hosted failure is retried, waived, or represented as a
product pass.

## Fresh ignored-local clean gate

The exact candidate was cloned without shared hardlinks under the repository's
ignored `.tmp/` directory. A fresh clone-local CPython 3.12.13 environment used
the hash-locked dependency set and editable no-build-isolation/no-dependency
product installation. `pip check` passed.

The exact workflow partition (15 accepted superseded-B1 ignores and three
transparent historical deselections) completed with **1432 passed, four
classified optional physical-artifact skips, three deselected, and 149
inherited warnings in 242.75 seconds**. No mandatory Cycle 3 check skipped.

Ruff, production and strict characterization mypy, fixture/binding checks, all
accepted Cycle 2 and C3-B1 through C3-B3 manifests, installed CLI grammar,
exact Node 22.14.0 locked frontend checks, 29-module build, asset drift, and
process/prohibited-runtime audits passed.

## Exact-candidate hosted result

Root pushed exact commit `ec805b506ef18f6fc0844d9586764d35aba021ec`
to dedicated branch `cycle3-b4-ci-ec805b5`. GitHub Actions run
`33570173317`, job `100062197241`, resolved that exact SHA and concluded
`failure`. The x86_64 guard and all setup/static/type steps passed. The hosted
pytest command used the newly governed partition, closing the round-2
superseded-module defect, but still failed for three harness reasons:

1. The default shallow checkout omitted prior candidate commits consumed by
   fresh verifier history/diff assertions.
2. Hosted Python bytecode generation created `__pycache__` inside the closed
   characterization-tool inventory, correctly producing `tool inventory
   rejected`.
3. One existing forced-kill cleanup test uses a child that installs SIGTERM
   ignore after Python startup. On the hosted runner, its 50 ms test-local
   timeout can expire before that handler is installed, allowing graceful
   termination and producing `kill_to_reap_ns == 0`. The same exact test passes
   locally, but a rerun is prohibited and supplies no hosted evidence.

## Required correction

Keep all product and accepted B1-B3 evidence bytes unchanged. Correct only the
hosted harness by using full-history checkout, setting
`PYTHONDONTWRITEBYTECODE=1` job-wide before any Python command, and executing
the existing forced-kill test once in an isolated shell that inherits SIGTERM
ignore before the broad suite. The broad suite may then transparently deselect
that exact already-executed node; this preserves mandatory coverage without a
race, retry, changed test, or waiver. The combined focused-plus-broad result
must feed the existing bounded sanitized report and single status.

The correction requires a new immutable candidate, fresh independent B4
verification, complete fresh accumulated validation, and a new exact-candidate
hosted run. The B1 rights-holder/counsel limitation remains controlling. No
wheel, sdist, upload, conveyance, or publication occurred.

`changes_required`
