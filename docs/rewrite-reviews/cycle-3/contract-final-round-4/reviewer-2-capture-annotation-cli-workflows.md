# Cycle 3 final contract review — capture, annotations, library, and CLI

- Gate and round: `contract`; `contract-final-round-4`
- Reviewer: `/root/c3_final_r4_workflows` (capture, annotation, CLI, and workflows)
- Reviewed commit: `59390b75a406eebd6660d52381c68325ebd5fbdc`
- Reviewed tree: `cabb1fc44372be99f504384ff08985e169e07109`
- UTC timestamp: `2026-08-26T15:26:03Z`
- Verdict: `pass`

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
inspected the accepted capture, replay, CSV, CLI, public-type, test, OpenAPI,
and web-boundary sources needed to assess the workflow seams, using content
from the reviewed commit only. No decoder, reference runtime, C#, .NET,
pythonnet, libsigrokdecode, or `sigrok-cli` code was executed, built, restored,
installed, imported, or used as an output oracle.

## Findings and dispositions

No finding remains open. The candidate continues to preserve physical channel
identity separately from packed sample position and decoder mapping; converges
validated in-memory, replay-schema-1/2, and explicit-metadata CSV inputs before
decode; freezes immutable version-1 result/error objects and byte-exact
canonical serialization; preserves request-wide emission order; and adds no
decoder browser, API, frontend, serial, or live-capture surface.

The round-3 correction also makes the B1 workflow executable without crossing
ownership boundaries. The semantic-fixture candidate now contains only the
complete finite experiment-cap specification, exact values and schema,
boundaries, coverage, and independently derived rationale. Its verification,
accumulated gate, and acceptance perform static declarative review and
explicitly neither contain nor claim executable enforcement. The actual
runner, launch/import configuration, cap plumbing, and cleanup paths first
appear in a separate immutable runner candidate owned by a distinct
implementor. Its separate verifier and acceptance identity exclusively prove
every cap and termination/close/reap path with inert or hostile non-decoder
probes before the unchanged runner may execute an approved snapshot. No pass
transfers between the two candidates.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R2-001` — resolved

- Earlier record:
  `contract-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  preserved by reviewed commit
  `59390b75a406eebd6660d52381c68325ebd5fbdc`.
- Evidence: discovery's “Public library and installed CLI only” and
  orchestration's “Inputs, outputs, library, and CLI” freeze mutually exclusive
  replay/CSV input; ordered physical CSV `--channels`; legacy-inference-only
  optional `--sample-rate`; required `--trigger-channel` and `--edge`; exact
  precedence, presence, exclusion, and pre-launch validation; and separation
  from repeatable decoder `--channel` mappings. C3-B3/B4 require independent
  cross-source and installed black-box proof.
- Disposition: resolved; accepted CSV capture identity is never reconstructed
  from decoder mappings or inferred from non-legacy CSV content.

### `contract-round-1` / `C3-CR1-R2-002` — resolved

- Earlier record:
  `contract-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  preserved by reviewed commit
  `59390b75a406eebd6660d52381c68325ebd5fbdc`.
- Evidence: discovery's “Normative decode-result schema version 1” freezes the
  exact `pico-logic-analyzer.decode-result/v1` and
  `pico-logic-analyzer.decode-error/v1` roots, declarations, records, closed
  Python-value tags, immutable library classes, integer coordinates, rational
  time, padded RFC 4648 base64, Python 3.12 canonical JSON bytes, failure
  codes, diagnostics, and exits. B1 independently authors expected typed
  objects and literal CLI bytes before product result/CLI implementation;
  R9/R17/R18 and B2/B4/B5 consume those identities unchanged.
- Disposition: resolved; typed-object and byte-exact public proof has no
  implementer-selected schema interpretation.

### `contract-final-round-1` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that record passed commit
  `ed24f1badfff5200494cf2408e53c85cb44c0f02`. The reviewed candidate preserves
  its capture, result, CLI, serialization, regression, and browser-exclusion
  resolutions.
- Disposition: reconciled through this fresh complete-set review; the earlier
  pass was not transferred.

### `contract-final-round-2` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-2/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that record passed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`. Later B1 role separation and the
  directed evidence protocol leave the accepted public workflow unchanged.
- Disposition: reconciled through this fresh complete-set review; the earlier
  pass was not transferred.

### `contract-final-round-3` / `C3-CFR3-R2-001` — resolved

- Earlier record:
  `contract-final-round-3/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `59390b75a406eebd6660d52381c68325ebd5fbdc`.
- Evidence: C3-B1 steps 3-6 in `CYCLE3_BATCH_EXECUTION.md` now define the
  semantic-fixture candidate as containing no runner or executable cap
  plumbing; limit its verifier and accumulated gate to cap-set completeness,
  exact finite values, schema, boundaries, coverage, and independent
  derivation; and state that executable enforcement is absent, untested, and
  unclaimed. Fixture acceptance reviews only that static specification and
  cannot transfer its pass. Steps 7-8 exclusively assign the actual runner,
  launch/import configuration, cap/cleanup plumbing, and every executable cap,
  digest/import, termination, close, and reap test to the later immutable
  runner candidate and its separate identities. Matching language appears in
  discovery's baseline and B1 sections, orchestration's B1 ordering and role
  sections, the review README's mandatory freeze points, and the Reviewer 3
  charter.
- Disposition: resolved; no fixture-owned gate requires impossible or
  placeholder runner evidence, and executable enforcement is proved only on
  the exact candidate that contains it.

## Cross-domain reconciliation

### Reviewer 1 findings — preserved resolved

- Earlier findings: `C3-CR1-R1-F1`, `C3-CR1-R1-F2`, and `C3-CR1-R1-F3`.
- Evidence: the reviewed candidate preserves the exact conservative
  pre-characterization experiment-cap specification and later unchanged-runner
  gate; integer `0xFF` optional-pin semantics and named UART/SPI mapping
  fixtures; and the closed option-coverage matrix with B3/B5 audit ownership.
  Separating declarative cap review from executable enforcement does not change
  fixture meaning, decoder identity, API-v3 semantics, or the sole-oracle rule.
- Disposition: all remain resolved; no earlier Reviewer 1 pass was transferred.

### Reviewer 3 round-1 findings — preserved resolved

- Earlier findings: `C3-CR1-R3-001`, `C3-CR1-R3-002`, and
  `C3-CR1-R3-003`.
- Evidence: B5 acceptance remains pre-manifest and the later terminal evidence
  chain remains directed; prohibited use remains scoped to every active Cycle
  3 production and development/test path while preserved C# stays inert static
  history; and a manifest verifier remains distinct from the orchestrator and
  assembler.
- Disposition: all remain resolved.

### Reviewer 3 final-round-1 findings — preserved resolved

- Earlier findings: `C3-CFR1-R3-001` and `C3-CFR1-R3-002`.
- Evidence: the exact actual runner and all enforcement/cleanup plumbing are
  still committed and independently proved before unchanged snapshot
  execution, and B5 still uses the directed manifest/verification,
  closure-pending checkpoint, immutable completion-proof, closure-verdict, and
  terminal non-audit-input seal sequence.
- Disposition: both remain resolved.

### Reviewer 3 final-round-2 findings — preserved resolved

- Earlier findings: `C3-CFR2-R3-001` and `C3-CFR2-R3-002`.
- Evidence: the fixture and runner candidates retain different implementors,
  verifiers, and acceptance identities with reciprocal authorship exclusions;
  the immutable manifest may name its assigned verifier but no future verdict,
  record, path, or self-dependent digest; and the separate verification record
  owns the manifest digest, commands, results, findings, and verdict before the
  later checkpoint references both.
- Disposition: both remain resolved.

## Final disposition

The complete common-commit contract set is internally consistent and
objectively testable in the capture, annotation, deterministic-data, library,
CLI, and cross-domain workflow seams. Every earlier finding in this domain has
a durable disposition, including the corrected split between declarative
fixture-cap review and later exact-runner enforcement proof. No finding remains
open. Verdict: `pass`.
