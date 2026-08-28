# C3-B1 pre-execution runner rebinding accumulated validation — round 2

## Subject and verdict

- Owner: primary Cycle 3 orchestrator (`/root`).
- Candidate commit/tree:
  `55d22640334ef05176568f275c3e4e7ec63c3336` /
  `b96790c572f2fceda4445f55d8373b9a21e2cd9d`.
- Fresh verification: `pass`; commit
  `570cfe8a0977d8d3e9d5198d671cd157ce1b6696`; verifier
  `c3-b1-pre-execution-runner-rebinding-verifier-2`.
- Completed: `2026-08-28T16:26:58Z`.
- Finding: `C3B1-RA001`, pre-acceptance downstream raw-module execution risk.
- Verdict: **changes_required**. This candidate must not receive acceptance,
  raw, threshold, final-B1, manifest, checkpoint, or B2 authority.

## Ordering failure

After the focused 194-test verifier/runner matrix passed, root mistakenly
started an unfiltered non-hardware pytest command in clean clone
`/private/tmp/c3-runner-if002`. At the prior fixture stage this shape failed
closed before raw execution because the runner binding was stale. At this
stage the binding was valid, so the same command progressed into
`tests/verification/test_c3_b1_raw_baseline_candidate.py`, whose complete
reproduction may launch approved decoder snapshots.

Root recognized the ordering violation while the command was still running,
interrupted it with SIGINT, and accepted no exit result, raw output, digest,
count, timing, or pass evidence. Because the command had spent sufficient time
inside the downstream portion that snapshot execution cannot be disproved,
this record conservatively treats a pre-acceptance decoder launch as having
occurred. The governing sequence permits no such launch before exact runner
acceptance. The violation cannot be relabeled as inert runner validation or
repaired merely by rerunning a filtered command.

Immediate process inspection found no surviving clone process,
characterization runner, snapshot host, worker, decoder, browser, or
prohibited runtime. The main repository and candidate bytes remained
unchanged. No generated raw artifact was copied, committed, cited, or used to
adjust a fixture, cap, threshold, product behavior, or later gate.

## Non-transferring diagnostic reruns

Root then proved that the byte candidate itself remained technically sound,
but these results do not rescue its invalid sequence:

- a second fresh clone `/private/tmp/c3-runner-if002-clean` passed the exact
  runner-applicable partition: 598 passed, 6 classified inherited skips, and
  106 warnings;
- pip check, whole-project Ruff, strict mypy over 21 product plus seven runner
  modules, binding check, generator check, installed CLI help, and all six
  Cycle 2 evidence validators passed;
- exact Node 22 lint, typecheck, three-file/five-test unit suite, 29-module
  build, asset check, isolated one-test maximum-width browser run, three-test
  live/shell run, and B6 performance run passed; the retained performance
  report SHA-256 was
  `f2d904cf4e20ccb40232b4f0d13376542252bf72a8574ca84331027058592b8b`;
- final process inspection found no relevant survivor.

The runner-applicable partition deliberately excluded only superseded exact-
candidate fixture/runner verifier modules and all raw/threshold/final modules.
Unlike the interrupted command, it could not enter a decoder execution path.
These diagnostics may inform the replacement candidate but transfer no
accumulated verdict.

## Required disposition

1. Preserve candidate `55d2264`, verifier commit `570cfe8`, this
   `changes_required` record, and `C3B1-RA001` as immutable history.
2. The same assigned runner-rebinding implementation lane may create a fresh
   replacement candidate record binding the unchanged reviewed runner bytes
   and explicitly excluding every downstream execution module from the
   pre-acceptance matrix. It may not change behavior, caps, fixture identity,
   or use the interrupted raw attempt as evidence.
3. Assign a fresh runner verifier identity. Then root must run a fresh
   accumulated gate in a new clean clone using only the pre-acceptance-safe
   command partition, followed by fresh acceptance.
4. Only that accepted replacement runner may execute fresh raw
   characterization. Nothing from the interrupted attempt transfers.

Open candidate finding: `C3B1-RA001`.

`changes_required`
