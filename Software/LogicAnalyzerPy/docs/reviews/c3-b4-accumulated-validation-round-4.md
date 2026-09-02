# C3-B4 accumulated validation, round 4

- Orchestrator role: root accumulated-validation and hosted-dispatch owner
- Timestamp: `2026-09-02T00:18:00Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Round-6 implementation candidate/tree: `db94d6b4a63aefbd1ec185a6492344be3df98842` /
  `26f3afe065e0202d9289e7ccb4a8fb47a9329a31`
- Independently verified evidence commit/tree exercised by this gate:
  `a75874236e1d15dfa3abe969aafa27140a78253c` /
  `7e099b2a92ea6776f38409143e025dec749736aa`
- Local clean clone: repository-ignored
  `.tmp/c3-b4-accumulated-r5.zzHPMA/repo`

## Exact local accumulated result

The exact evidence commit was cloned without local-object sharing into the ignored
repository `.tmp/` tree. A fresh Python 3.12.13 environment was created there and
populated from the exact development lock. `PYTHONDONTWRITEBYTECODE=1` and a
repository-local temporary directory were used for verification commands.

The focused forced-kill function was executed once in a bash child inheriting ignored
SIGTERM and passed both parameters: `2 passed in 0.23s`. The subsequent exact broad
partition collected 1,449 items, selected 1,440, and transparently deselected nine
cases through the workflow's eight exact node selectors. It completed with `1,434
passed, 6 skipped, 9 deselected, 106 warnings in 248.33s`. The six skips were exactly
the two sandbox-loopback checks and four optional machine-local physical-artifact
checks; no mandatory Cycle 3 or B2/B3/B4 check skipped.

Additional exact-clone gates passed:

- Python 3.12.13, development-lock `pip check`, Ruff, production mypy over 31 source
  files, and strict installed-consumer mypy.
- Fresh web-runtime lock installation and `pip check`.
- Exact Node 22.14.0 archive SHA-256
  `6698587713ab565a94a360e091df9f6d91c8fadda6d00f0cf6526e9b40bed250`;
  lockfile installation of 215 packages; ESLint; TypeScript; three Vitest files/five
  tests; and the 29-module Vite production build.
- Production asset drift, top-level and decode CLI help, and strict validation of
  accepted `c3-b1.json`, `c3-b2.json`, and `c3-b3.json` manifests.
- Closed characterization-tool inventory contained no bytecode. The prohibited
  process audit found no active .NET, pythonnet, `sigrok-cli`, or external
  libsigrokdecode process. The exact clone remained clean after validation.

An initial supplementary clone was accidentally bootstrapped with system Python 3.14.7
and is not governing evidence. It correctly failed the contract's Python 3.12 gates.
It also provided diagnostic-only stress evidence that the immutable
`test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation` can observe
the same startup race as the already isolated forced-kill function: under concurrent
load its child exited on SIGTERM before installing its own ignored disposition, so
`kill_to_reap_ns` was zero. The node passed when independently executed under inherited
ignored SIGTERM. This observation is not used to convert the hosted failure into a
pass.

## Exact hosted dispatch and failure

The exact evidence commit was pushed to dedicated branch
`cycle3-b4-ci-a758742`. GitHub Actions run
[`33573907523`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33573907523),
job
[`100073568756`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33573907523/job/100073568756),
resolved exact head `a75874236e1d15dfa3abe969aafa27140a78253c` on the governed
`macos-15-intel` runner and concluded `failure`.

The architecture guard, full-history checkout, Python and Node setup, hash-locked core
installation, editable source installation, dependency check, Ruff, production mypy,
and strict installed-consumer type check all passed. The non-hardware step's focused
inherited-SIGTERM proof also passed both parameters in 0.45 seconds. The broad suite
then collected the exact 1,449/1,440/9 partition and failed after approximately six
minutes. All later CLI, web, frontend, asset, and browser steps were skipped by normal
fail-fast behavior.

The exact failing pytest node is not visible in the preserved public annotation. The
workflow sanitizes the last 12,000 bytes, but GitHub retained only the first 4,096
characters of that annotation. Those characters end at 56 percent of the broad run,
before the failure report. The separate annotation says only that the step exited 1.
The unauthenticated full-job-log API returns HTTP 403. Consequently this record does
not guess the hidden node, waive the failure, or claim the locally observed timing race
is proven to be the hosted cause.

Status polling used one reusable read-only `rtk curl` command class to write JSON under
the repository's ignored `.tmp/` directory, followed by separate sandbox-local `jq`
parsing. One transient DNS failure was retried with the same saved class. No repeated
approval class, workflow rerun, artifact publication, or conveyance occurred.

## Disposition

Local accumulated validation passes, but the mandatory exact-candidate hosted gate
fails and its bounded diagnostic annotation is insufficient to identify the failing
node. B4 is not accepted. A fresh bounded correction and independent verification are
required before another exact-candidate dispatch.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, publication, or conveyance
was performed.

Verdict: `fail`. `APPROVAL_NEEDED`: none.
