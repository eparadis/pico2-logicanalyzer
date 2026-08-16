# Final Round 2 Review: Delivery, Verification, and Orchestration Contract

- **Reviewer:** `/root/review_delivery_contract` — Reviewer 3, Delivery,
  Verification, and Orchestration Contract
- **Reviewed commit:** `134a4b69d1a6d0f81bb0fab37d355254d2b440ba`
- **UTC timestamp:** `2026-08-16T17:21:44Z`
- **Verdict:** `changes_required`

## Scope

I reviewed only the immutable commit named above under the Reviewer 3 charter,
including all three process documents, the review framework, Round 1 records,
the attempted `final/` records, and the dispositions leading to this candidate.
Working-tree changes were not used as evidence.

The Cycle 1 objective remains bounded, hardware-first, and objectively stopped.
The nine stopping items remain assigned as follows:

| Stop item | Batch and proof |
| --- | --- |
| 1. Python 3.12 install and CLI help | C1-B1 clean locked bootstrap plus Linux/macOS CI and CLI-help evidence. |
| 2. Static and non-hardware checks | C1-B1 establishes the exact suite; every batch accumulates it; C1-B5 reruns it clean against the candidate revision. |
| 3. Provenance-tagged V2 fixtures | C1-B1 schema/goldens, C1-B2 protocol tests, and C1-B3/B4 observed hardware confirmation. |
| 4. Fake/replay adverse behavior | C1-B2 fragmentation, malformed input, bounds, timeout, disconnect, cleanup, and cancellation/re-identification tests. |
| 5. Physical identity and capture | C1-B3 identity, C1-B4 selected-polarity signal capture, and C1-B5 final hardware smoke. |
| 6. Deterministic CSV/replay | C1-B4 bounded independent reload/determinism tests and C1-B5 final evidence. |
| 7. Cleanup, cancellation, and second capture | C1-B2 fake recovery, C1-B3 reopen, C1-B4 close, and C1-B5 non-interactive physical recovery plus two real captures. |
| 8. Final progress/evidence record | Per-checkpoint manifests and C1-B5 final packet, all tied to one candidate commit/tree. |
| 9. C#/firmware rollback | Explicit non-modification throughout and C1-B5 rollback confirmation. |

No stopping item is circular or lacks a batch/proof owner. The remaining finding
is in the pre-goal review-approval gate itself.

## Prior Reviewer 3 finding dispositions

### 1. Hash-pinned PEP 517 build dependencies

- **Severity:** none
- **Evidence:** `ORCHESTRATION.md:286-302` now requires runtime, development,
  PEP 517 build requirements, and all transitives in the hashed lock, installs
  that lock first, and performs the editable install with both
  `--no-build-isolation` and `--no-deps`. `BATCH_EXECUTION.md:163-181` repeats
  the identical local/CI sequence and its no-outside-resolution invariant;
  C1-B1 acceptance checks it at `BATCH_EXECUTION.md:372-373`.
- **Disposition:** resolved — the editable build must consume the already
  installed, hash-verified build requirements and cannot ask pip to resolve an
  isolated build environment.

### 2. Exact `0xFF` hardware authority

- **Severity:** none
- **Evidence:** `ORCHESTRATION.md:238-240` authorizes exactly one characterized
  V2 `0xFF` byte only for an in-flight Cycle 1 normal-capture recovery and binds
  it to drain/close/reopen/re-identification. The batch authority checklist at
  `BATCH_EXECUTION.md:612-615` repeats that exact restriction. General/public
  abort behavior remains excluded.
- **Disposition:** resolved — required recovery and permitted hardware actions
  are now consistent and narrowly scoped.

### 3. Stable non-interactive physical recovery proof

- **Severity:** none
- **Evidence:** `ORCHESTRATION.md:321-343` defines
  `hardware-recovery-smoke` with explicit idle-level/channel, cancellation
  delay, known-signal, sampling, trigger, count, and evidence-path inputs. It
  requires one cancellation byte, the settled recovery sequence, a known-signal
  follow-up capture without power cycling, atomic sanitized evidence, and a
  deterministic exit code. The public CLI contract repeats the interface and
  behavior at `BATCH_EXECUTION.md:272-299`; C1-B5 makes that command part of the
  physical gate at `BATCH_EXECUTION.md:520-528`.
- **Disposition:** resolved — stop item 7 now has a stable, non-interactive,
  provenance-recorded physical proof rather than an ad hoc Ctrl-C observation.

### 4. Earlier Round 1 governance findings

- **Severity:** none
- **Evidence:** The narrow CI workflow authority remains explicit; three
  distinct implementation/verification/acceptance identities remain mandatory
  (`BATCH_EXECUTION.md:112-122`); checkpoint evidence remains commit/tree and
  manifest anchored; exact firmware identity is resolved only at C1-B3
  (`BATCH_EXECUTION.md:461-462`); and both edge polarities remain fake-tested
  (`BATCH_EXECUTION.md:494`) with the physical selection recorded.
- **Disposition:** resolved — none of the current corrections regresses the six
  original Reviewer 3 findings.

## Findings and disposition

### 1. The approval checklist still points to the preserved failed final round

- **Severity:** high
- **Evidence:** The revised review protocol says a `final/` directory containing
  any `changes_required` verdict is a preserved attempted final round and that
  the next common-commit review uses `final-round-N/`
  (`docs/rewrite-reviews/README.md:31-34`). The immutable candidate indeed
  contains `changes_required` records in `docs/rewrite-reviews/final/`. However,
  the authoritative pre-goal checklist still requires all three passes to be in
  exactly `docs/rewrite-reviews/final/` (`ORCHESTRATION.md:421-422`). It does not
  recognize `final-round-2/` or the latest common-commit final review directory.
- **Impact:** Even if all three current reviewers pass this exact commit in
  `final-round-2/`, the literal authoritative approval checklist remains false
  because the preserved `final/` records are not all passes. An orchestrator
  must either ignore the higher-authority checklist or incorrectly rewrite
  immutable review history before creating `/goal`.
- **Requested resolution:** Mechanically update the checklist to require all
  three `pass` records from the latest complete common-commit final-review
  directory defined by `docs/rewrite-reviews/README.md`, with no pass taken from
  an earlier/failed round. Prefer naming the current directory explicitly as
  `docs/rewrite-reviews/final-round-2/` while also stating the general rule for
  later rounds. Preserve `docs/rewrite-reviews/final/` unchanged as history.
- **Disposition:** open — the approval gate cannot currently be satisfied.
  Because any correction creates a new candidate commit, the all-three
  same-commit rule requires all three reviewers to review that new commit.

## Same-commit rule

This record reviews exactly
`134a4b69d1a6d0f81bb0fab37d355254d2b440ba`. The required common-commit rule is
not satisfied because this verdict is `changes_required`, regardless of the
other two reviewer verdicts. No findings other than Finding 1 remain in Reviewer
3's domain.
