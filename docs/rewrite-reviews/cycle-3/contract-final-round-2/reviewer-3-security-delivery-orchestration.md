# Cycle 3 contract final review — security, delivery, evidence, and orchestration

- Gate and round: `contract`; `contract-final-round-2`
- Reviewer: `/root/c3_final_r2_security` (security, delivery, and orchestration)
- Reviewed commit: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
- Reviewed tree: `f53d0f23bb63b92e54099fbcfce5d4fb047fec70`
- UTC timestamp: `2026-08-26T15:07:22Z`
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

I also inspected the repository instructions and parent review protocol,
current Python dependency/lock and hosted-CI metadata, accepted Cycle 1/Cycle 2
evidence interfaces, performance/evidence records, and relevant preserved
source/provenance as inert text. I did not execute a decoder, C#, .NET,
pythonnet, libsigrokdecode, `sigrok-cli`, or another reference runtime.

## Findings and dispositions

### C3-CFR2-R3-001 — High — B1 assigns expected fixtures and the runner to one implementation identity while forbidding that combination

- **Evidence:** `CYCLE3_ORCHESTRATION.md`, “Roles, candidate sequence, and
  correction rules,” defines one implementation identity per batch.
  `CYCLE3_BATCH_EXECUTION.md`, “Required identities and separation,” likewise
  defines one implementation agent, while “Global ownership and path
  boundaries” assigns the B1 fixture owner both independently expected records
  and the characterization runner/method. Its B1 “Ownership and proof” again
  assigns one implementation owner the independently calculated expected
  records, generator, characterization runner, and method. In direct conflict,
  B1 mandatory gate step 7 says the identity owning independently expected
  fixture content must not author, verify, or approve the runner candidate. The
  discovery and orchestration contracts repeat that prohibition.
- **Violated invariant/cross-domain seam:** the runner must be independent of
  authoritative expected-fixture ownership, but the identity and path-ownership
  model makes a compliant assignment impossible or ambiguous. This leaves the
  actual-runner qualification introduced for `C3-CFR1-R3-001` without a
  consistently assignable independent author.
- **Requested resolution:** split B1's internal implementation ownership into
  at least a semantic-fixture implementation identity and a different
  pre-execution-runner implementation identity. Update every role statement,
  progress/assignment/handoff template, final B1 candidate identity map,
  manifest field, and ownership paragraph so the fixture identity cannot author
  runner/method/probe content and the runner identity cannot author expected
  fixtures. Preserve separate verifier and acceptance identities for each
  internal candidate and transfer no pass.
- **Disposition:** open.

### C3-CFR2-R3-002 — High — the manifest schema requires its verifier's future verdict inside the manifest being verified

- **Evidence:** `CYCLE3_ORCHESTRATION.md`, “Progress, evidence, manifests, and
  checkpoints,” requires every manifest to record the manifest-verifier
  identity and verdict. `CYCLE3_BATCH_EXECUTION.md`, “Create the manifest
  atomically, then checkpoint,” instead orders the orchestrator to assemble the
  immutable manifest first, then has the manifest verifier validate and hash
  that manifest and create its verdict record, and only afterward commits the
  unchanged manifest and record together. The same section broadly says the
  manifest includes role identities and review records.
- **Violated invariant/cross-domain seam:** an immutable manifest cannot contain
  the later verdict or record produced by validating its own bytes. Predicting
  `pass` is a future-record reference; adding the actual verdict afterward
  changes the digest that was verified. This recreates an evidence cycle before
  every checkpoint, including the otherwise directed B5 terminal chain.
- **Requested resolution:** freeze a directed manifest protocol: the proposed
  manifest may name the assigned manifest-verifier identity but must contain no
  future manifest-verifier verdict, record identity/path, or self-dependent
  digest. The distinct verification record must name and hash the unchanged
  manifest and carry its own verdict. Commit those two immutable files together,
  then let the later checkpoint reference both and the pass verdict. Make the
  schema field ownership and “review records” wording explicit and apply the
  same rule to B1-B5.
- **Disposition:** open.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R3-001`

- **Resolving commit and evidence:**
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` separates B5 pre-manifest
  acceptance from post-acceptance manifest creation, independent manifest
  verification, checkpointing, and closure work throughout the discovery,
  orchestration, and batch contracts. Commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb` further makes the terminal chain
  directed.
- **Disposition:** resolved. The distinct manifest self-verification cycle is
  recorded as `C3-CFR2-R3-002`.

### `contract-round-1` / `C3-CR1-R3-002`

- **Resolving commit and evidence:**
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` scopes prohibited use to every
  active Cycle 3 Python product and non-production path while preserving C# only
  as inert history. The same exact rule remains present at
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`.
- **Disposition:** resolved.

### `contract-round-1` / `C3-CR1-R3-003`

- **Resolving commit and evidence:**
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` assigns a manifest-verifier
  identity distinct from the orchestrator/assembler and requires independent
  digest/schema recomputation before checkpointing; that role remains distinct
  at `4d094b6d9a71e44387a386c85a586b1ecf5230fb`.
- **Disposition:** resolved as to identity separation. The new field-ordering
  defect that prevents the role from producing non-circular immutable evidence
  is recorded as `C3-CFR2-R3-002`.

### `contract-final-round-1` / `C3-CFR1-R3-001`

- **Resolving commit and evidence:** commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb` adds a separate immutable actual-
  runner candidate and requires inert/hostile non-decoder proof of every cap,
  digest/import boundary, termination, close, reap, and post-failure path before
  the unchanged runner may execute an approved snapshot. It also requires
  accumulated validation and a distinct acceptance pass explicitly recording
  that no decoder ran.
- **Disposition:** unresolved because the cross-document identity model still
  assigns expected-fixture and runner authorship to one B1 implementation
  identity while forbidding that combination; carried as `C3-CFR2-R3-001`.

### `contract-final-round-1` / `C3-CFR1-R3-002`

- **Resolving commit and evidence:** commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb` freezes the directed order: B5
  manifest and verification-record commit; closure-pending checkpoint; immutable
  completion-proof candidate naming no future closure artifact; distinct
  committed closure verdict over unchanged inputs; and a terminal seal that is
  not an audit input. The checkpoint template and stopping condition 18 prohibit
  future references.
- **Disposition:** resolved.

The actual-runner mechanics and B5 terminal ordering are materially improved,
and the prohibited-dependency scope remains exact. The two open contradictions
above still prevent an auditable execution assignment and immutable checkpoint
evidence, so this round cannot pass.
