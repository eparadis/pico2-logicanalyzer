# Cycle 3 final contract review — capture, annotations, library, and CLI

- Gate and round: `contract`; `contract-final-round-3`
- Reviewer: `/root/c3_final_r3_workflows` (capture, annotation, CLI, and workflows)
- Reviewed commit: `6621d0881a102586f32de0b8cd2b1579a369a6cd`
- Reviewed tree: `1b8b9b3f1ce3c73f095610d24b082e510129b9ad`
- UTC timestamp: `2026-08-26T15:18:22Z`
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

I also inspected every earlier contract-gate review record and statically
inspected the accepted capture, replay, CSV, CLI, public-type, and unchanged
web-boundary sources needed to assess the workflow seams. No decoder,
reference runtime, C#, .NET, pythonnet, libsigrokdecode, or `sigrok-cli` code
was executed, built, restored, installed, imported, or used as an output
oracle.

## Findings and dispositions

### C3-CFR3-R2-001 — High — the semantic-fixture gate still requires runner cap-enforcement proof before the runner exists

- **Evidence:** `CYCLE3_BATCH_EXECUTION.md`, C3-B1 “Mandatory internal gate
  order,” step 3 defines the semantic-fixture candidate as fixture, expected-
  result, schema, safety-cap, decision, and digest material. Step 5 nevertheless
  requires its accumulated gate to include “independent cap-enforcement tests.”
  The actual runner, launch/import configuration, cap-enforcement plumbing, and
  cleanup paths are first authored and committed later in step 7, and step 8 is
  the contract's dedicated independent non-decoder enforcement gate for that
  immutable runner candidate. The orchestration validation contract and the
  review README likewise assign executable enforcement proof to that later
  exact-runner gate.
- **Violated invariant/cross-domain seam:** the fixture candidate must freeze
  conservative cap values without implementing or pretending to prove the
  future runner. Executable cap enforcement must be proved only against the
  immutable actual runner that contains all enforcement and cleanup plumbing.
  As written, step 5 either demands impossible evidence, permits proof against
  a placeholder/different implementation, or silently moves runner work into
  the fixture owner's prohibited surface. Each interpretation breaks the
  corrected fixture/runner ownership and immutable-candidate sequence.
- **Requested resolution:** replace step 5's “independent cap-enforcement
  tests” with a fixture-owned static completeness/schema/boundary review of the
  proposed experiment-cap values. State there that executable enforcement is
  absent and not claimed at the fixture gate. Keep every executable cap,
  digest/import, termination, close, and reap test exclusively in steps 7-8
  against the exact immutable runner candidate. Apply matching wording wherever
  the fixture accumulated gate is summarized so no pass can transfer from cap
  review to runner enforcement.
- **Disposition:** open.

The capture and public workflow surface itself remains coherent: physical
channel IDs stay separate from packed positions and decoder mappings;
in-memory, replay-schema-1/2, and explicit-metadata CSV converge before decode;
the version-1 immutable result/error models and canonical bytes remain exact;
and no decoder browser/API/frontend surface is introduced. The open ordering
defect above still prevents an objectively executable B1 workflow, so this
round cannot pass.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R2-001` — resolved

- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  preserved by reviewed commit
  `6621d0881a102586f32de0b8cd2b1579a369a6cd`.
- Evidence: discovery's “Public library and installed CLI only” and
  orchestration's “Inputs, outputs, library, and CLI” freeze the mutually
  exclusive replay/CSV grammar, ordered physical `--channels`, legacy-only
  optional `--sample-rate`, required `--trigger-channel` and `--edge`, their
  precedence and pre-launch validation, and their separation from decoder
  `--channel` mappings. C3-B3/B4 require independent cross-source and installed
  black-box proof.
- Disposition: resolved; CSV capture identity is never reconstructed from a
  decoder mapping or inferred from non-legacy content.

### `contract-round-1` / `C3-CR1-R2-002` — resolved

- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  preserved by reviewed commit
  `6621d0881a102586f32de0b8cd2b1579a369a6cd`.
- Evidence: discovery's “Normative decode-result schema version 1” freezes the
  exact result/error schemas, immutable objects, declarations, record/value
  tags, rational time, base64, canonical Python 3.12 JSON bytes, errors, and
  exits. B1 independently authors object and literal-byte goldens; R9/R17/R18
  and B2/B4/B5 consume those identities unchanged.
- Disposition: resolved; typed-object and byte-exact public proof has no
  implementer-selected schema interpretation.

### `contract-final-round-1` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that record passed commit
  `ed24f1badfff5200494cf2408e53c85cb44c0f02`. The later candidates preserve its
  capture, result, CLI, serialization, regression, and browser-exclusion
  resolutions.
- Disposition: reconciled through this fresh complete-set review; the earlier
  pass was not transferred.

### `contract-final-round-2` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-2/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that record passed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`. The reviewed commit changes B1
  role separation and the directed manifest protocol while preserving the
  accepted capture/result/public-workflow contract.
- Disposition: reconciled through this fresh complete-set review; no pass was
  transferred across commits. The new step-5 contradiction is recorded as
  `C3-CFR3-R2-001`.

## Cross-domain reconciliation

### `contract-final-round-2` / `C3-CFR2-R3-001` — resolved, subject to the new sequencing finding

- Resolving commit: `6621d0881a102586f32de0b8cd2b1579a369a6cd`.
- Evidence: discovery, orchestration, batch roles, progress/assignment/handoff
  templates, B1 ownership, final-candidate identity map, manifest/checkpoint,
  review README, and reviewer charter now consistently name a semantic-fixture
  implementor and a distinct pre-execution-runner implementor with reciprocal
  authorship exclusions. Each internal candidate receives separate verifier
  and acceptance identities and transfers no pass.
- Disposition: the earlier identity-assignment contradiction is resolved. The
  remaining premature enforcement-test clause is a distinct candidate-order
  defect recorded as `C3-CFR3-R2-001`.

### `contract-final-round-2` / `C3-CFR2-R3-002` — resolved

- Resolving commit: `6621d0881a102586f32de0b8cd2b1579a369a6cd`.
- Evidence: all five documents now freeze one directed protocol: the proposed
  manifest may name only the assigned verifier identity and already-existing
  reviews; the separate verifier record exclusively owns and records the
  manifest digest, verification commands/results, findings, and verdict; both
  immutable files commit together; and only a later checkpoint references
  both identities and the pass. No manifest predicts a future record or hashes
  itself.
- Disposition: resolved; the manifest/verifier-record handoff is acyclic and
  objectively verifiable.

### Earlier Reviewer 1 and Reviewer 3 findings — preserved resolved

- Evidence: the reviewed candidate preserves the exact pre-characterization
  safety envelope and unchanged-runner gate, integer `0xFF` sentinel and named
  mapping fixtures, closed option matrix, pre-manifest B5 acceptance and
  directed closure chain, exact active-path prohibited-use scope, and verifier
  independence introduced by the resolving commits recorded in the earlier
  reviews.
- Disposition: no earlier cross-domain finding is silently waived or reopened
  except for the separate fixture-versus-runner sequencing defect identified
  above.

## Final disposition

The public capture/result/library/CLI contract remains complete and
deterministic, and both round-2 findings are substantively repaired. However,
the B1 fixture gate still asks for executable enforcement proof before the only
candidate containing that enforcement exists. That contradiction must be
corrected and the complete six-file set re-reviewed at one new commit and tree.
Verdict: `changes_required`.
