# Cycle 3 final contract review — decoder API, runtime, and fixtures

- Gate and round: `contract`; `contract-final-round-4`
- Reviewer: `/root/c3_final_r4_decoder` (decoder API, runtime, fixtures, and provenance)
- Reviewed commit: `59390b75a406eebd6660d52381c68325ebd5fbdc`
- Reviewed tree: `cabb1fc44372be99f504384ff08985e169e07109`
- UTC timestamp: `2026-08-26T15:26:29Z`
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
inspected the focused checked-in decoder, shim, and helper sources, their inert
provenance/license evidence, and the accepted capture/result seams required by
this charter. I did not execute, build, restore, install, import, or load a
decoder, C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or an
external/reference runtime, and none supplied expected output or corroborating
evidence.

## Findings and dispositions

No finding remains open. The candidate preserves the exact snapshot and import
allowlist, host-owned decoder identity, closed API-v3 behavior, integer `0xFF`
optional-pin contract, closed option-coverage matrix, independent fixture and
version-1 golden authority, complete typed-emission seam, and immutable staged
pre-execution safety gate.

The round-4 correction is complete at the fixture/runner seam. The
semantic-fixture candidate specifies the complete finite experiment-cap set,
exact values and schema, boundary cases, coverage, and independently derived
rationale, but contains no runner or executable enforcement plumbing. Its
verifier, accumulated gate, and acceptance identity review only that static cap
specification and expressly make no enforcement claim. Only after those gates
pass does a different implementor create the immutable actual-runner candidate.
That later candidate alone receives inert/hostile non-decoder enforcement,
digest/import, termination, close, reap, accumulated-validation, and acceptance
proof before its unchanged bytes may execute an approved snapshot. No fixture
pass transfers to the runner candidate.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R1-F1` — resolved

- Resolving commits and evidence: exact conservative experiment caps first
  appeared in `ed24f1badfff5200494cf2408e53c85cb44c0f02`; the immutable actual-
  runner gate appeared in `4d094b6d9a71e44387a386c85a586b1ecf5230fb`;
  distinct fixture/runner ownership appeared in
  `6621d0881a102586f32de0b8cd2b1579a369a6cd`; and reviewed commit
  `59390b75a406eebd6660d52381c68325ebd5fbdc` now makes the split between
  static cap-specification review and later executable enforcement proof exact.
  Discovery's “Baseline-first thresholds,” orchestration's validation contract,
  and B1 steps 3-9 require the accepted cap specification and complete
  non-decoder proof on the immutable runner before its unchanged bytes execute
  a snapshot. A limit termination is not a passing baseline and caps cannot be
  weakened.
- Disposition: resolved; no characterization can begin unbounded, through an
  unqualified runner, or on enforcement evidence transferred from a fixture
  candidate.

### `contract-round-1` / `C3-CR1-R1-F2` — resolved

- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains unchanged in reviewed
  commit `59390b75a406eebd6660d52381c68325ebd5fbdc`. Discovery and orchestration
  freeze full required-then-optional tuple order, built-in integer values,
  exact absent optional sentinel `0xFF` (`255`), and `has_channel()` false
  exactly for such an absent optional slot. B1/B3 require UART RX-only/TX-only
  and SPI MISO-only/MOSI-only/no-CS fixtures.
- Disposition: resolved; absent-pin and mapping behavior remains exact and
  testable.

### `contract-round-1` / `C3-CR1-R1-F3` — resolved

- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains unchanged in reviewed
  commit `59390b75a406eebd6660d52381c68325ebd5fbdc`. Before characterization, the
  closed matrix classifies every default, enumeration, numeric boundary, and
  sentinel only as a named direct fixture, a named source-justified static
  equivalent, or unsupported pre-launch rejection; B3 and B5 audit every row
  against accepted fixture digests.
- Disposition: resolved; subjective “material options” sampling remains
  forbidden.

### `contract-round-1` / `C3-CR1-R2-001` and `C3-CR1-R2-002` — resolved at the decoder-consumer seam

- Resolving commit and evidence: `ed24f1badfff5200494cf2408e53c85cb44c0f02`
  froze explicit CSV capture metadata separately from decoder mappings and the
  complete version-1 result/error models and canonical bytes. Those contracts,
  R9/R16-R18 ownership, and B1/B3/B4/B5 proof remain unchanged in the reviewed
  candidate.
- Disposition: resolved; decoder inputs retain capture authority and emitted
  records have one independently fixed public representation.

### `contract-round-1` / `C3-CR1-R3-001`, `C3-CR1-R3-002`, and `C3-CR1-R3-003` — resolved

- Resolving commits and evidence: `ed24f1badfff5200494cf2408e53c85cb44c0f02`
  separated B5 pre-manifest acceptance, scoped prohibited use to every active
  production and non-production Cycle 3 path while keeping C# metadata inert,
  and assigned a manifest verifier independent of the orchestrator/assembler.
  Commit `4d094b6d9a71e44387a386c85a586b1ecf5230fb` made the B5 terminal chain
  directed. All clauses remain in the reviewed candidate.
- Disposition: resolved; fixture/runtime evidence can flow into acceptance and
  completion without prohibited execution or circular B5 acceptance.

### `contract-final-round-1` / `C3-CFR1-R3-001` — resolved

- Resolving commits and evidence: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
  introduced the immutable actual-runner candidate and independent non-decoder
  cap/import/termination/close/reap gate;
  `6621d0881a102586f32de0b8cd2b1579a369a6cd` assigned its implementor,
  verifier, and acceptance identities separately from fixture ownership; and
  reviewed commit `59390b75a406eebd6660d52381c68325ebd5fbdc` confines all executable
  enforcement proof to this runner candidate.
- Disposition: resolved; the qualified execution path and expected-output
  oracle are separately owned and separately proved.

### `contract-final-round-1` / `C3-CFR1-R3-002` — resolved

- Resolving commit and evidence: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
  froze the directed B5 manifest/verification-record commit, closure-pending
  checkpoint, immutable completion proof with no future reference, committed
  closure verdict, and terminal non-audit-input seal. The reviewed candidate
  preserves that order.
- Disposition: resolved; no decoder evidence is amended after its closure
  audit.

### `contract-final-round-2` / `C3-CFR2-R3-001` — resolved

- Resolving commit and evidence: `6621d0881a102586f32de0b8cd2b1579a369a6cd`
  assigned semantic fixtures and the pre-execution runner to different
  implementors with reciprocal exclusions, separate verifier and acceptance
  identities for each internal candidate, no transferred pass, and a durable
  six-identity map in downstream evidence. The reviewed candidate preserves
  those rules.
- Disposition: resolved; actual-runner authorship remains independent of
  authoritative expected-output authorship.

### `contract-final-round-2` / `C3-CFR2-R3-002` — resolved

- Resolving commit and evidence: `6621d0881a102586f32de0b8cd2b1579a369a6cd`
  applies one directed manifest protocol to B1-B5. A proposed manifest may name
  its assigned verifier identity but no future verdict, record identity/path,
  or self-dependent digest; the separate verifier record names and hashes the
  unchanged manifest and owns its commands, findings, and verdict.
- Disposition: resolved; manifest verification is acyclic and independently
  attributable.

### `contract-final-round-3` / `C3-CFR3-R2-001` — resolved

- Resolving commit and evidence: reviewed commit
  `59390b75a406eebd6660d52381c68325ebd5fbdc` changes discovery's B1 gate,
  orchestration's role/validation clauses, the batch procedure's B1 steps 3-8
  and ownership/proof text, and both review-framework documents. The fixture
  candidate has only a declarative finite cap specification. Its verifier,
  accumulated gate, and acceptance identity review completeness, exact values,
  schema, boundaries, coverage, and independent derivation while explicitly
  stating that executable enforcement is absent and unclaimed. The actual
  runner and every executable cap/digest/import/termination/close/reap proof
  remain exclusive to the later immutable runner candidate and its distinct
  verifier and acceptance identity.
- Disposition: resolved; the workflow no longer requires proof against a
  nonexistent, placeholder, or fixture-owned runner, and no static fixture pass
  can be transferred as runner-enforcement evidence.

### Earlier Reviewer 1 final-round passes — reconciled by fresh review

- Earlier records: `contract-final-round-1/reviewer-1-decoder-api-runtime-fixtures.md`,
  `contract-final-round-2/reviewer-1-decoder-api-runtime-fixtures.md`, and
  `contract-final-round-3/reviewer-1-decoder-api-runtime-fixtures.md`.
- Evidence: I performed a fresh complete-set review of the substantive round-4
  candidate. Its correction narrows the fixture cap gate to declarative review
  and leaves executable enforcement on the already required immutable runner;
  it does not weaken decoder identities, API-v3 semantics, fixtures, mappings,
  options, result schemas, public-consumer seams, limits, or exclusions.
- Disposition: reconciled on the new commit; no earlier pass was transferred.

No earlier contract-gate finding lacks a durable disposition, and no new
decoder/API/runtime/fixture or cross-domain finding was identified. Verdict:
`pass`.
