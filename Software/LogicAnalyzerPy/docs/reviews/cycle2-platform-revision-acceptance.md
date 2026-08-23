# Cycle 2 macOS-only contract revision acceptance

- Lane / identity: acceptance / `cycle2-acceptance`
- Verifier identity: `cycle2-verifier`
- Reviewed candidate commit: `e266d88815b0dabdd1397cbfcf3e1187bf8dfc24`
- Reviewed candidate tree: `9ec8c3ef73e47c940fd686656708cfaa212d9058`
- Operator authority: remove Linux from active Cycle 2 requirements and
  workflows while preserving immutable historical records for possible future
  provenance
- Review date: 2026-08-22 America/Los_Angeles
- Verdict: `pass`

## Candidate and scope audit

The assigned commit exists and resolves to the assigned tree. Its revision
delta modifies exactly the six authorized active files:

- `CYCLE2_GOAL.md`;
- `CYCLE2_ORCHESTRATION.md`;
- `CYCLE2_BATCH_EXECUTION.md`;
- `.github/workflows/logic-analyzer-python-cycle2.yml`;
- `Software/LogicAnalyzerPy/README.md`; and
- append-only `Software/LogicAnalyzerPy/docs/cycle-2-orchestration-progress.md`.

The revision does not modify discovery evidence, preparatory reviews,
implementation/verifier/acceptance records, prior hosted-CI evidence, firmware,
C# applications, Python product implementation, tests, locks, built assets, or
excluded Cycle 3 surfaces. The progress-log change appends a new authority and
reopening record; it does not rewrite its earlier Linux-requirement statements.

Independent verification record
`Software/LogicAnalyzerPy/docs/reviews/cycle2-platform-revision-verification.md`
has SHA-256
`e4c94cfac3810300aa7c813f564d57a7af4e5225bcc4349f417038b2e501ea00`, names the
same candidate and tree, reports `pass`, and has no open finding.

## Contract coherence

The active goal, orchestration contract, batch procedure, workflow, and README
now consistently identify macOS as the only accepted and supported Cycle 2
platform. Other operating systems are outside current scope and carry no
support claim. The completion packet is required to state that macOS-only
qualification precisely. Historical Linux and Ubuntu results remain truthful
records of requirements and observations in force when they were created; the
new progress entry explicitly prevents them from being interpreted as current
support and requires a separately approved future revision before Linux support
could be claimed again.

All fourteen stopping conditions remain present. Only the authorized platform
portion of conditions 3 and 13 is narrowed. Python and frontend clean installs,
Cycle 1 regression, protocol fixtures, hostile-input and lifecycle coverage,
replay/CSV, bus analysis, physical masks and recovery, offline and native
browser workflows, rendering thresholds, final evidence, rollback paths, and
the prohibited-action audit remain mandatory.

All six C2-B1 through C2-B6 batches retain their order, ownership, acceptance
gates, hardware gates, performance checkpoint, evidence lifecycle, and Cycle 3
exclusions. Platform-specific B1, B5, and B6 language is consistently narrowed
to macOS without removing unrelated requirements.

## Workflow and support-boundary audit

The single Cycle 2 workflow now runs directly on `macos-latest`. Removal is
limited to the matrix wrapper, Ubuntu runner, Linux-only Chromium dependency
installation, and now-redundant platform conditions. The macOS Chromium install
is unconditional. Python 3.12, Node 22.14.0, both clean locked Python installs,
both `pip check` gates, Ruff, mypy, bounded sanitized non-hardware pytest, CLI
help, locked npm install, lint, typecheck, unit tests, production build, asset
drift, Chromium provisioning, and production browser smoke remain ordered and
active. No stale matrix expression or conditional platform skip remains.

The README's macOS-only statement agrees with the governing objective and does
not imply partial support for another operating system. The contracts likewise
distinguish unsupported platforms from deferred features without weakening the
macOS native browser, physical hardware, or hosted-CI proof.

## Findings

No acceptance finding is open. The candidate faithfully implements the
operator-authorized platform narrowing without rewriting history, dropping an
unrelated gate, creating support ambiguity, or beginning Cycle 3.

## C2-B1 reopening handoff

This verdict accepts the contract revision only; it does not transfer the prior
C2-B1 verification or acceptance verdict to the revised governing candidate.
The progress log correctly records that the prior uncommitted B1 manifest was
discarded. C2-B1 is reopened and must receive fresh independent verification,
complete accumulated macOS validation including exact-candidate hosted CI, and
fresh independent acceptance under this revision. Only after those gates pass
may the orchestrator atomically create and validate the C2-B1 manifest, commit
it, append the checkpoint record, and mark B1 complete. Historical Linux
evidence may remain as provenance but must not be used as a current support
claim or active checkpoint requirement.

## Final state

The exact revision candidate is accepted as the authoritative macOS-only Cycle
2 contract baseline. No finding remains open; C2-B1 remains reopened pending
its revised-contract gate sequence.
