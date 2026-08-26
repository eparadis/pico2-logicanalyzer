# Cycle 3 contract final review — security, delivery, evidence, and orchestration

- Gate and round: `contract`; `contract-final-round-1`
- Reviewer: `/root/c3_final_r1_security` (security, delivery, and orchestration)
- Reviewed commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`
- Reviewed tree: `511de8bc4f7ccc6219c81e61fe55a3722b96a20b`
- UTC timestamp: `2026-08-26T14:54:55Z`
- Verdict: `changes_required`

## Set-completeness declaration

I inspected every path in the exact six-file Step 8 contract-review set at the
commit and tree above, with no worktree file substituted:

1. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`;
2. `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`;
3. `CYCLE3_ORCHESTRATION.md`;
4. `CYCLE3_BATCH_EXECUTION.md`;
5. `docs/rewrite-reviews/cycle-3/README.md`; and
6. `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`.

I also inspected the repository instructions, parent review protocol, current
Python dependency/lock and hosted-CI metadata, accepted Cycle 1/Cycle 2
evidence interfaces, performance/evidence records, and relevant preserved
source/provenance as inert text. I did not execute a decoder, C#, .NET,
pythonnet, libsigrokdecode, `sigrok-cli`, or another reference runtime.

## Findings and dispositions

### C3-CFR1-R3-001 — High — the pre-execution gate does not review the runner that applies its caps

- **Evidence:** `CYCLE3_BATCH_EXECUTION.md`, C3-B1 “Mandatory internal gate
  order” steps 3-6, puts the safety envelope in the semantic-fixture candidate
  and requires independent cap-enforcement proof, but step 7 says only after
  those gates pass may the implementation identity add the non-installed
  characterization runner and measurement method and immediately execute the
  snapshots. The same document's preflight and `CYCLE3_ORCHESTRATION.md`'s
  validation contract require cap enforcement to be independently proved
  before the first decoder execution. The reviewed candidate therefore cannot
  prove that the later, newly added executable runner actually wires every
  accepted cap, closed import/digest rule, and cleanup action into its launch.
- **Violated invariant/cross-domain seam:** the exact executable path that
  performs first characterization must itself be immutable, independently
  verified, and accepted as enforcing the experiment-only envelope before any
  approved snapshot executes. Reviewing cap values or a different probe before
  the runner exists does not establish that seam.
- **Requested resolution:** put the characterization runner, measurement
  method, exact launch/import configuration, and cap-enforcement plumbing in a
  separate immutable pre-execution candidate (or include them in the existing
  fixture candidate without running a snapshot). Independently verify and
  accept that exact candidate using inert/hostile non-decoder probes for every
  cap, digest/import boundary, termination, close, and reap path. Only after
  those passes may that unchanged runner execute an approved snapshot. Preserve
  independent expected-fixture ownership and record explicitly that no decoder
  ran during this runner gate.
- **Disposition:** open.

### C3-CFR1-R3-002 — High — completion proof and closure audit still form a future-record cycle

- **Evidence:** `CYCLE3_ORCHESTRATION.md`, “Roles, candidate sequence, and
  correction rules,” requires the completion-closure auditor to inspect the
  already committed B5 manifest, verification record, checkpoint, and
  completion proof after checkpointing. “Completion proof, rollback, and
  handoff” simultaneously requires `cycle-3-completion.md` to contain the B5
  completion-closure record. `CYCLE3_BATCH_EXECUTION.md` likewise places the
  closure audit after the B5 checkpoint, while its checkpoint template asks the
  checkpoint to record the B5 closure auditor/verdict. Thus either the proof or
  checkpoint must name a verdict that cannot yet exist, or the closure auditor
  must audit an artifact that is later changed to add its own record.
- **Violated invariant/cross-domain seam:** immutable evidence cannot contain
  or depend on the later verdict whose auditor must inspect that evidence.
  Completion ordering must have a directed, non-circular chain with no future
  record or post-audit mutation.
- **Requested resolution:** freeze one exact order, for example: commit the B5
  manifest and manifest-verification record; commit the B5 checkpoint with an
  explicit closure-pending state; commit an immutable completion-proof
  candidate that names the checkpoint but no future closure verdict; have the
  distinct closure auditor inspect those committed artifacts and commit its
  verdict; then use that verdict itself, or a separate terminal completion seal
  that is not an input to the audit, as the final stop. Update stopping
  condition 18, the completion-proof contents, and the checkpoint template to
  prohibit a future closure reference.
- **Disposition:** open.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R3-001`

- **Resolving commit and evidence:**
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` separates B5 pre-manifest
  acceptance from manifest creation/verification/checkpointing and assigns a
  later completion-closure audit in `CYCLE3_ORCHESTRATION.md`,
  `CYCLE3_BATCH_EXECUTION.md`, and the discovery B5 contract.
- **Disposition:** resolved. The distinct downstream future-record cycle is
  recorded separately as `C3-CFR1-R3-002`; it does not reopen the original
  pre-manifest-acceptance defect.

### `contract-round-1` / `C3-CR1-R3-002`

- **Resolving commit and evidence:**
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` consistently scopes prohibited
  use to every active Cycle 3 Python product, development, test, fixture,
  characterization, verification, performance, acceptance, CI, bootstrap,
  lock, distribution, import, active-process, command, and evidence path. It
  explicitly preserves C# metadata only as inert history, defines ambient
  availability as non-use, and prohibits invocation, import, linkage,
  resolution, active process, command reference, and evidence reliance.
- **Disposition:** resolved.

### `contract-round-1` / `C3-CR1-R3-003`

- **Resolving commit and evidence:**
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` adds a manifest-verifier identity
  distinct from the orchestrator/assembler throughout the role definitions,
  exact batch order, B1-B5 mechanics, manifest protocol, evidence fields, and
  checkpoint template. The verifier recomputes digests/schema and records the
  candidate, manifest digest, commands, results, findings, and verdict before
  manifest commit/checkpoint.
- **Disposition:** resolved.

No earlier Reviewer 3 contract finding remains without a durable disposition,
but the two new findings above remain open, so this round cannot pass.
