# Cycle 3 final contract review — capture, annotations, library, and CLI

- Gate and round: `contract`; `contract-final-round-2`
- Reviewer: `/root/c3_final_r2_workflows` (capture, annotation, CLI, and workflows)
- Reviewed commit: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
- Reviewed tree: `f53d0f23bb63b92e54099fbcfce5d4fb047fec70`
- UTC timestamp: `2026-08-26T15:06:28Z`
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
inspected the accepted capture, replay, CSV, CLI, public-type, and unchanged
web-boundary sources needed to assess the workflow seams. No decoder,
reference runtime, C#, .NET, pythonnet, libsigrokdecode, or `sigrok-cli` code
was executed, built, restored, installed, imported, or used as an output
oracle.

## Findings and dispositions

No finding remains open. The exact candidate preserves physical channel IDs
separately from packed positions and decoder mappings; converges validated
in-memory, replay-schema-1/2, and explicit-metadata CSV inputs before decode;
freezes deterministic immutable result objects, rational time, every output
tag, request-wide emission order, canonical CLI bytes, failure classes, and
exit behavior; and keeps Cycle 3 decoder behavior out of the browser/API/
frontend surface.

The substantive corrections since `contract-final-round-1` do not introduce a
second workflow path. The pre-execution runner remains non-installed and
private, cannot use capture or expected-output data to select code, and may run
a snapshot only after the exact runner/launch/import/cap/cleanup candidate
passes independent non-decoder verification and acceptance unchanged. The B5
completion repair is a directed evidence sequence whose closure-pending proof
cannot predict a later verdict or seal; it does not alter the public result or
capture semantics.

## Prior-round reconciliation

### C3-CR1-R2-001 — resolved

- Earlier record:
  `contract-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  preserved unchanged by reviewed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`.
- Evidence: `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`,
  “Public library and installed CLI only,” and
  `CYCLE3_ORCHESTRATION.md`, “Inputs, outputs, library, and CLI,” freeze the
  mutually exclusive replay/CSV grammar. CSV carries ordered physical
  `--channels`, legacy-inference-only optional `--sample-rate`, required
  `--trigger-channel`, and required `--edge`, separately from repeatable
  decoder `--channel` mappings. Presence, replay exclusion, precedence,
  content/metadata validation, failure classification, and pre-launch ordering
  are explicit. C3-B3 and C3-B4 require independent cross-source and installed
  black-box proof.
- Disposition: resolved; no accepted CSV capture identity is reconstructed from
  decoder mapping or inferred from non-legacy content.

### C3-CR1-R2-002 — resolved

- Earlier record:
  `contract-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  preserved unchanged by reviewed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`.
- Evidence: discovery's “Normative decode-result schema version 1” separately
  freezes `pico-logic-analyzer.decode-result/v1` and
  `pico-logic-analyzer.decode-error/v1`: exact root fields and scalar types,
  declarations and record shapes, closed Python-value tags, immutable library
  classes, rational time, padded RFC 4648 base64, Python 3.12 canonical JSON
  bytes, failure codes, stderr, and exits. It requires independently authored
  typed-object vectors and literal CLI bytes before product result/CLI
  implementation. R9, R17, and R18 and C3-B2/B4/B5 consume those identities
  unchanged.
- Disposition: resolved; typed-object and byte-exact public proof does not
  depend on implementer-selected interpretation.

### `contract-final-round-1` Reviewer 2 disposition — preserved

- Earlier record:
  `contract-final-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: the earlier reviewer recorded `pass` at commit
  `ed24f1badfff5200494cf2408e53c85cb44c0f02`. The diff to the present commit
  changes only the B1 pre-execution runner gate, the B5 terminal evidence
  sequence, and matching review invariants; it does not weaken any capture,
  result, CLI, serialization, regression, or browser-exclusion clause.
- Disposition: reconciled by a fresh complete-set review; no pass was
  transferred across commits.

## Cross-domain reconciliation

### C3-CFR1-R3-001 — resolved without a workflow regression

- Earlier record:
  `contract-final-round-1/reviewer-3-security-delivery-orchestration.md`.
- Resolving commit: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`.
- Evidence: discovery's “Baseline-first thresholds and intentionally staged
  gates,” orchestration's validation contract, and C3-B1 steps 7-9 in the batch
  procedure now require the actual non-installed runner, method, exact launch/
  import configuration, cap plumbing, and all cleanup paths in a separate
  immutable candidate. Independent inert/hostile non-decoder verification,
  accumulated validation, and acceptance must pass and state that no decoder
  ran before the unchanged runner may execute a snapshot. Expected-fixture
  ownership remains separate.
- Disposition: resolved; the later public library/CLI still consumes only the
  B2 isolated host and cannot select or weaken the B1 characterization path.

### C3-CFR1-R3-002 — resolved without a future-record cycle

- Earlier record:
  `contract-final-round-1/reviewer-3-security-delivery-orchestration.md`.
- Resolving commit: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`.
- Evidence: discovery stopping condition 18, orchestration's role/completion
  sections, and the batch procedure now agree on one direction: committed B5
  manifest and manifest-verification record; closure-pending checkpoint;
  immutable completion-proof candidate naming no future closure artifact;
  separately committed closure verdict over those unchanged inputs; and a
  terminal non-audit-input seal committed last. The checkpoint template and
  final-packet contents prohibit predicting the later auditor, verdict, record,
  or seal.
- Disposition: resolved; no artifact is amended after audit and the workflow
  has an objective terminal state.

## Final disposition

The capture/annotation/deterministic-data/library/CLI contract and both repaired
cross-domain seams are internally consistent, objectively testable, and
complete enough for the later goal gate. No finding remains open. Verdict:
`pass`.
