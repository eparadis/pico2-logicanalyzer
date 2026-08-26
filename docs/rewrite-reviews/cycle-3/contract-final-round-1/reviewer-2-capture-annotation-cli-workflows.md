# Cycle 3 final contract review — capture, annotations, library, and CLI

- Gate and round: `contract`; `contract-final-round-1`
- Reviewer: `/root/c3_final_r1_workflows` (capture, annotation, CLI, and workflows)
- Reviewed commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`
- Reviewed tree: `511de8bc4f7ccc6219c81e61fe55a3722b96a20b`
- UTC timestamp: `2026-08-26T14:54:08Z`
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

I also statically inspected the accepted capture, replay, CSV, CLI, public type,
and web-boundary sources needed to test the proposed seams. No decoder,
reference runtime, C#, .NET, pythonnet, libsigrokdecode, or `sigrok-cli` code
was executed, built, restored, installed, imported, or used as an output oracle.

## Findings and dispositions

No finding remains open. The exact candidate consistently preserves physical
channel identity separately from packed position and decoder mapping; converges
validated in-memory, replay-schema-1/2, and explicit-metadata CSV inputs before
decode; freezes deterministic typed records and canonical serialization; and
keeps Cycle 3 decoder behavior out of the browser/API/frontend surface.

## Prior-round reconciliation

### C3-CR1-R2-001 — resolved

- Earlier record: `contract-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`.
- Evidence: `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`,
  “Public library and installed CLI only,” freezes the mutually exclusive
  replay/CSV grammar. CSV capture metadata consists of ordered physical
  `--channels`, legacy-inference-only optional `--sample-rate`, required
  `--trigger-channel`, and required `--edge`; it is explicitly separate from
  repeatable decoder `--channel` mappings. Presence, replay exclusion,
  precedence, label/identity validation, failure classification, and
  pre-launch ordering are explicit. `CYCLE3_ORCHESTRATION.md`, “Inputs,
  outputs, library, and CLI,” repeats the same machine contract, and
  `CYCLE3_BATCH_EXECUTION.md`, C3-B4, assigns installed black-box presence,
  precedence, separation, and cross-source-equivalence proof.
- Disposition: resolved; no capture identity must be reconstructed from a
  decoder mapping or inferred from non-legacy CSV content.

### C3-CR1-R2-002 — resolved

- Earlier record: `contract-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`.
- Evidence: `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`,
  “Normative decode-result schema version 1,” separately freezes
  `pico-logic-analyzer.decode-result/v1` and
  `pico-logic-analyzer.decode-error/v1`: exact root fields and scalar types,
  declaration and record shapes, closed tags, request-wide order, immutable
  library classes, rational-time numerators/denominators, padded RFC 4648
  base64, Python 3.12 canonical JSON bytes, host failure codes, stderr and exit
  behavior. The same section requires independently authored expected immutable
  objects and literal CLI UTF-8 bytes for every tag before product result/CLI
  implementation. The R9, R17, and R18 rows bind those B1 identities to private
  result, installed library, and installed CLI proof; C3-B2, C3-B4, and C3-B5
  in `CYCLE3_BATCH_EXECUTION.md` consume them unchanged.
- Disposition: resolved; independent typed-object and byte-exact public proof
  no longer depends on implementer-selected prose interpretation.

## Final disposition

The capture/annotation/library/CLI contract is internally consistent with the
accepted Cycle 1/2 formats and public boundaries, objectively testable, and
complete enough for the later goal gate. Verdict: `pass`.
