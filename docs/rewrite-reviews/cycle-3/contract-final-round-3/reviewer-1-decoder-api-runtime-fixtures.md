# Cycle 3 final contract review — decoder API, runtime, and fixtures

- Gate and round: `contract`; `contract-final-round-3`
- Reviewer: `/root/c3_final_r3_decoder` (decoder API, runtime, fixtures, and provenance)
- Reviewed commit: `6621d0881a102586f32de0b8cd2b1579a369a6cd`
- Reviewed tree: `1b8b9b3f1ce3c73f095610d24b082e510129b9ad`
- UTC timestamp: `2026-08-26T15:18:30Z`
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
provenance/license evidence, and the capture/result seams required by this
charter. I did not execute, build, restore, install, import, or load any decoder,
C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or external/reference
runtime, and none supplied expected output or corroborating evidence.

## Findings and dispositions

No finding remains open. The candidate retains the exact hash/import allowlist,
host-owned decoder identity, closed API-v3 behavior, integer `0xFF` optional-pin
contract, closed option-coverage matrix, independent fixture and version-1
golden authority, complete typed-emission seam, and staged pre-execution safety
gate.

The round-3 ownership repair is complete at the decoder/runtime seam. B1 now
assigns semantic fixtures and the pre-execution runner to different
implementation identities with reciprocal exclusions. Each internal candidate
has its own verifier and acceptance identities; no pass transfers; and the full
six-identity map is required in progress, assignments, handoffs, the final B1
candidate, manifest, checkpoint, and completion proof. The directed B1-B5
manifest protocol also leaves authoritative fixture, candidate, and proof
identities immutable: the manifest may name only the assigned verifier identity,
while the separate verifier record names and hashes the unchanged manifest and
exclusively owns verification commands, results, findings, and verdict.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R1-F1` — resolved

- Resolving commits and evidence: the exact conservative experiment caps first
  appeared in `ed24f1badfff5200494cf2408e53c85cb44c0f02`; the actual-runner gate
  appeared in `4d094b6d9a71e44387a386c85a586b1ecf5230fb`; both remain in reviewed
  commit `6621d0881a102586f32de0b8cd2b1579a369a6cd`. Discovery's
  “Baseline-first thresholds,” orchestration's validation contract, and B1
  steps 3-9 require exact experiment-only caps and inert/hostile non-decoder
  proof on the immutable actual runner before its unchanged bytes execute a
  snapshot. Limit termination is not a passing baseline and caps cannot weaken.
- Disposition: resolved; no characterization can start unbounded or through an
  unqualified runner.

### `contract-round-1` / `C3-CR1-R1-F2` — resolved

- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains in the reviewed
  candidate. Discovery and orchestration freeze full declared tuple order,
  built-in integer values, exact absent optional sentinel `0xFF` (`255`), and
  `has_channel()` false exactly for such an absent optional slot. B1/B3 require
  UART RX-only/TX-only and SPI MISO-only/MOSI-only/no-CS fixtures.
- Disposition: resolved; absent-pin and mapping behavior is exact and testable.

### `contract-round-1` / `C3-CR1-R1-F3` — resolved

- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains in the reviewed
  candidate. The closed B1 matrix classifies every default, enumeration,
  numeric boundary, and sentinel only as a named direct fixture, a named
  source-justified static equivalent, or unsupported pre-launch rejection; B3
  and B5 audit every row against accepted fixture digests.
- Disposition: resolved; subjective “material options” sampling is forbidden.

### `contract-round-1` / `C3-CR1-R2-001` and `C3-CR1-R2-002` — resolved at the decoder-consumer seam

- Resolving commit and evidence: `ed24f1badfff5200494cf2408e53c85cb44c0f02`
  froze explicit CSV capture metadata separately from decoder mappings and the
  complete version-1 result/error models and canonical bytes. Those contracts,
  the R9/R16-R18 ownership, and B1/B3/B4/B5 proof remain unchanged in the
  reviewed candidate.
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

- Resolving commit and evidence: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
  introduced the immutable actual-runner candidate and independent non-decoder
  cap/import/termination/close/reap gate. Reviewed commit
  `6621d0881a102586f32de0b8cd2b1579a369a6cd` additionally assigns that runner
  to an implementor who cannot own authoritative expected fixtures.
- Disposition: resolved; the qualified execution path and expected-output oracle
  are separately owned.

### `contract-final-round-1` / `C3-CFR1-R3-002` — resolved

- Resolving commit and evidence: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
  froze the directed B5 manifest/verification-record commit, closure-pending
  checkpoint, immutable completion proof with no future reference, committed
  closure verdict, and terminal non-audit-input seal. The reviewed candidate
  preserves that order.
- Disposition: resolved; no decoder evidence is amended after its closure audit.

### `contract-final-round-2` / `C3-CFR2-R3-001` — resolved

- Resolving commit and evidence: `6621d0881a102586f32de0b8cd2b1579a369a6cd`
  updates discovery's common mechanics and B1 ownership, orchestration's B1
  sequence/roles/evidence schema, the complete batch identity/assignment/
  handoff/path/candidate/checkpoint protocol, and both review-framework files.
  The semantic-fixture implementor cannot author runner/method/probe content;
  the runner implementor cannot author expected fixtures. Each internal
  candidate has a different verifier and acceptance identity and transfers no
  pass. The final B1 candidate and all durable downstream records preserve the
  six-identity map.
- Disposition: resolved; B1 can now assign an actual runner independently of
  authoritative expected-output authorship without ambiguity.

### `contract-final-round-2` / `C3-CFR2-R3-002` — resolved

- Resolving commit and evidence: `6621d0881a102586f32de0b8cd2b1579a369a6cd`
  applies one directed manifest protocol to B1-B5. A proposed manifest may name
  its assigned verifier identity but no future verdict, record identity/path,
  or self-dependent digest. The distinct verifier record names and hashes the
  unchanged manifest and exclusively owns its commands, results, findings, and
  verdict. Both commit together before the later checkpoint references them and
  the `pass`.
- Disposition: resolved; manifest verification no longer predicts or mutates
  the artifact it verifies.

### Earlier Reviewer 1 final-round passes — preserved by fresh review

- Earlier records: `contract-final-round-1/reviewer-1-decoder-api-runtime-fixtures.md`
  and `contract-final-round-2/reviewer-1-decoder-api-runtime-fixtures.md`.
- Evidence: I performed a fresh complete-set review of the substantive
  round-3 candidate. Its changes add role and evidence separation without
  weakening the decoder identities, API-v3 semantics, fixtures, mappings,
  options, result schema, public-consumer seam, limits, or exclusions accepted
  by those records.
- Disposition: reconciled on the new commit; no earlier pass was transferred.

No earlier contract-gate finding lacks a durable disposition, and no new
decoder/API/runtime/fixture or cross-domain finding was identified. Verdict:
`pass`.
