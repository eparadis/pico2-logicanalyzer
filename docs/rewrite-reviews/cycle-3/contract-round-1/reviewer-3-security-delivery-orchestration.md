# Cycle 3 contract review — security, delivery, evidence, and orchestration

- Gate and round: `contract`; `contract-round-1`
- Reviewer: `/root/c3_contract_review_security` (security, delivery, and orchestration)
- Reviewed commit: `8bd6ba06a42ea190f50c7b15789638938c8716d2`
- Reviewed tree: `19fc91d2cfaa526f2bee7ee2835423e5ccbd50ee`
- UTC timestamp: `2026-08-26T06:05:07Z`
- Verdict: `changes_required`

## Set-completeness declaration

I inspected every path in the exact six-file Step 8 contract-review set at the
commit and tree above, with no worktree file substituted: the roadmap,
discovery review, orchestration contract, batch procedure, Cycle 3 review
README, and architectural-domain charters.

## Findings and dispositions

### C3-CR1-R3-001 — High — B5 acceptance circularly requires future B5 evidence

- Evidence: B5 acceptance is asked to audit all five manifests/checkpoints
  before the post-acceptance B5 manifest and checkpoint may exist.
- Violated invariant: no acceptance decision may depend on evidence whose
  creation that decision authorizes.
- Requested resolution: split pre-manifest B5 acceptance (B1-B4 manifests plus
  B5 candidate/proposed-manifest readiness) from post-acceptance B5 manifest
  verification, checkpointing, and a separate completion-closure audit.
- Disposition: open.

### C3-CR1-R3-002 — High — prohibited-dependency audit scope conflicts with inert history

- Evidence: repository-/environment-wide “absence” language conflicts with the
  preserved C# project metadata, which may name historical prohibited
  dependencies even though it is an inert rollback source.
- Violated invariant: the prohibition must cover every active Cycle 3 path
  without pretending preserved historical source does not exist.
- Requested resolution: scope the audit to every Cycle 3 Python product,
  development, test, fixture, characterization, verification, performance,
  acceptance, CI, bootstrap, lock, distribution, import, active-process,
  command, and evidence path. Permit preserved C# metadata only as inert source
  that is never restored, built, installed, imported, or executed. Ambient
  installed availability alone is not use; invocation, import, linkage,
  resolution, active process, or evidence reliance is prohibited.
- Disposition: open.

### C3-CR1-R3-003 — Medium — manifest verification is not independent

- Evidence: the orchestrator both assembles and “independently” verifies each
  manifest.
- Violated invariant: an evidence producer cannot supply the independent
  recomputation claim for its own artifact.
- Requested resolution: assign a distinct post-acceptance manifest-verifier
  identity to recompute digests and schema validation and create an immutable
  record naming the manifest digest, candidate, commands, results, and verdict
  before manifest commit/checkpoint.
- Disposition: open.

## Prior-round reconciliation

No earlier contract-review round or finding exists for this gate/domain.
