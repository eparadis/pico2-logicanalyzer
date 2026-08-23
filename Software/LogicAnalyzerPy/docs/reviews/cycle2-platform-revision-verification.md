# Cycle 2 macOS-only contract revision verification

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `e266d88815b0dabdd1397cbfcf3e1187bf8dfc24`
- Reviewed candidate tree: `9ec8c3ef73e47c940fd686656708cfaa212d9058`
- Operator directive: remove Linux from active Cycle 2 requirements and workflow;
  preserve immutable historical Linux records for possible future provenance
- Review date: 2026-08-22 America/Los_Angeles
- Verdict: `pass`

## Authorized changed-path audit

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. The revision commit modifies exactly the six authorized
active files:

- `CYCLE2_GOAL.md`;
- `CYCLE2_ORCHESTRATION.md`;
- `CYCLE2_BATCH_EXECUTION.md`;
- `.github/workflows/logic-analyzer-python-cycle2.yml`;
- `Software/LogicAnalyzerPy/README.md`; and
- append-only `Software/LogicAnalyzerPy/docs/cycle-2-orchestration-progress.md`.

It does not modify historical discovery, preparatory reviews, implementation or
verification reviews, acceptance records, CI evidence, checkpoint evidence,
firmware, C# applications, or product implementation.

## Active platform requirement audit

The goal now requires hosted macOS CI, native macOS browser work, physical
captures, and performance thresholds. Its completion handoff requires a
macOS-only support qualification.

The orchestration contract now states that macOS is the only accepted and
supported platform and that other operating systems are outside Cycle 2 scope.
Stopping condition 3 requires the complete Python/frontend/API/headless-browser
suite on exact-candidate macOS CI. Conditions 1 through 14 all remain present;
no non-platform behavior, evidence, security, hardware, performance, rollback,
or prohibition condition was removed.

The batch contract retains all six C2-B1 through C2-B6 sections and the same
ownership/order. Platform references were consistently narrowed in B1 clean
probes/workflow/acceptance, B5 headless acceptance, B6 final CI and support
claim, stopping-condition ownership, and final evidence packet. Hardware and
native browser acceptance remain macOS requirements; unsupported-platform
hardware claims remain out of scope. No later batch, physical gate, security
boundary, or Cycle 3 exclusion was weakened.

Searches of the active goal, orchestration contract, batch contract, workflow,
and README found no remaining Linux or Ubuntu requirement/reference. The only
Linux references among the six revised files are in the append-only progress
log: one pre-revision historical B1 evidence statement and the new revision
entry that explicitly says historical Linux records are not current support
claims and future Linux support requires a new approved revision.

## Workflow audit

The single Cycle 2 workflow now uses `runs-on: macos-latest` directly. The prior
matrix strategy, `${{ matrix.os }}`, Ubuntu runner, Linux browser-dependency
step, and `runner.os` conditions are absent. The macOS Chromium provisioning
step is unconditional within the macOS job.

All canonical gates remain coherent and ordered: Python 3.12 and Node 22.14.0;
clean core/web environments; hash-locked installs; no-build-isolation/no-deps
source installs; both `pip check` gates; Ruff, mypy, exact non-hardware pytest
with bounded sanitized diagnostics, CLI help; locked npm install, lint,
typecheck, unit tests, production build, asset-drift check, Chromium
provisioning, and real production-browser smoke. Removing the Linux job did not
remove a macOS command or create a stale conditional skip.

## Progress/history audit

The new progress section is append-only and records the operator authority,
macOS-only current scope, exact revised artifact categories, preservation and
historical meaning of old Linux records, discarded uncommitted B1 manifest,
required re-verification/reacceptance, and the rule that future Linux support
needs a separately approved revision. This correctly distinguishes historical
truth from the current support claim.

## Bounded checks

- Exact commit/tree and clean starting status: pass.
- Revision-commit changed paths: exactly six authorized active files.
- Active Linux/Ubuntu and stale workflow matrix search: none outside explicitly
  historical/current-scope progress text.
- Stopping-condition audit: all 14 remain with only approved platform narrowing.
- Batch audit: all six remain with original non-platform semantics.
- Historical-record mutation audit: pass; revision commit changes none.
- `git diff --check`: pass.
- C2-B1 verifier foundation regression: 7 passed in 0.58 seconds, exit 0.

## Final finding state

No finding is open. The candidate faithfully implements the operator-approved
macOS-only Cycle 2 contract revision without unrelated scope or Cycle 3 work.
