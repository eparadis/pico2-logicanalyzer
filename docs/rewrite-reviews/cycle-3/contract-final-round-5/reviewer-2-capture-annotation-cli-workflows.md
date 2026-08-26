# Cycle 3 final contract review — capture, annotations, library, and CLI

- Gate and round: `contract`; `contract-final-round-5`
- Reviewer: `/root/c3_final_r5_workflows` (capture, annotation, CLI, and workflows)
- Reviewed commit: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`
- Reviewed tree: `d9fb09345ab85580cd8c877745262d1b481e366f`
- UTC timestamp: `2026-08-26T15:52:08Z`
- Verdict: `pass`

## Set-completeness declaration

I inspected every path in the exact six-file Step 8 contract-review set at the
commit and tree above, using commit content only and substituting no worktree
file:

1. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`;
2. `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`;
3. `CYCLE3_ORCHESTRATION.md`;
4. `CYCLE3_BATCH_EXECUTION.md`;
5. `docs/rewrite-reviews/cycle-3/README.md`; and
6. `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`.

I also inspected every earlier contract-gate review record, the Step 10
preflight context, the cited Cycle 2 evidence validator, and the accepted
capture/replay/CSV/CLI/public-type and unchanged web-boundary seams required by
this charter. Inspection was static. I did not execute, build, restore,
install, import, or load a decoder, C#, .NET, pythonnet, libsigrokdecode,
`sigrok-cli`, or another external/reference runtime, and none supplied expected
output or corroborating evidence.

## Findings and dispositions

No finding remains open. The sole contract-set delta from the previously
approved round-4 candidate is a factual correction in the Cycle 3 discovery
record. It preserves the originally attempted aggregate command and now records
its actual Exit 2 instead of falsely claiming Exit 0. Static inspection of
`scripts/validate_cycle2_evidence.py` confirms `main()` returns 2 unless its
argument vector contains exactly the program name, one schema, and one
manifest; the recorded aggregate invocation supplies one schema and six
manifests and therefore cannot be a successful validation invocation.

The correction separately records six Step 10 invocations, each containing the
schema and exactly one C2-B1 through C2-B6 manifest, with Exit 0. Git comparison
confirms that the validator, Cycle 2 schema, and all six named manifest bytes
are identical between cited original inspection commit
`c163a8353550e0b80dd7f001b21147659ad307ff` and cited Step 10 inspection commit
`64af244bf95572b147246a412c33fed13ed34afd`, whose tree is correctly recorded as
`1bb01eefaf5c94c932ecaf434917cf19033e1ddf`. Thus the per-manifest checks repair
the command record without changing the accepted evidence inputs or claiming
that the invalid aggregate command passed.

The correction explicitly requires fresh contract and goal reviews before
launch. It neither transfers the earlier approval nor weakens any capture,
decoder mapping, result schema, canonical-byte, CLI, regression, browser/API
exclusion, authority, candidate-order, or evidence requirement. Physical
channel IDs remain separate from packed positions and decoder mappings;
validated in-memory, replay-schema-1/2, and explicit-metadata CSV inputs still
converge before decode; and equivalent inputs still require byte-identical
canonical results.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R2-001` — remains resolved

- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  resolution preserved at the reviewed commit.
- Evidence: discovery and orchestration still freeze mutually exclusive
  replay/CSV input; ordered physical CSV `--channels`; legacy-inference-only
  optional `--sample-rate`; required `--trigger-channel` and `--edge`; exact
  presence, exclusion, precedence, and pre-launch validation; and strict
  separation from repeatable decoder `--channel` mappings. C3-B3/B4 retain
  independent cross-source and installed black-box proof.
- Disposition: resolved; the factual validator correction does not alter CSV
  capture identity or decoder mapping.

### `contract-round-1` / `C3-CR1-R2-002` — remains resolved

- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`;
  resolution preserved at the reviewed commit.
- Evidence: the separately versioned result/error schemas, immutable objects,
  declarations, closed value tags, rational time, padded base64, canonical
  Python 3.12 JSON bytes, failure classes, stderr, and exits are unchanged.
  B1 still owns independent expected objects and literal CLI bytes; R9/R17/R18
  and C3-B2/B4/B5 consume their immutable identities.
- Disposition: resolved; public object and byte semantics remain exact.

### `contract-final-round-1` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-1/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that review passed commit
  `ed24f1badfff5200494cf2408e53c85cb44c0f02`. The present complete-set review
  confirms its capture, result, CLI, serialization, regression, and browser-
  exclusion resolutions remain intact.
- Disposition: reconciled through fresh review; no pass was transferred.

### `contract-final-round-2` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-2/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that review passed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`; later role and evidence repairs
  and the present factual correction leave its public workflow conclusions
  unchanged.
- Disposition: reconciled through fresh review; no pass was transferred.

### `contract-final-round-3` / `C3-CFR3-R2-001` — remains resolved

- Resolving commit: `59390b75a406eebd6660d52381c68325ebd5fbdc`;
  resolution preserved at the reviewed commit.
- Evidence: the B1 semantic-fixture candidate still contains only the finite
  experiment-cap specification, exact values/schema/boundaries/coverage, and
  independent rationale, with executable enforcement absent and unclaimed.
  The distinct immutable runner candidate and its separate verifier and
  acceptance identities exclusively own inert/hostile proof of every cap,
  digest/import, termination, close, and reap path before unchanged snapshot
  execution.
- Disposition: resolved; no fixture-gate pass substitutes for runner proof.

### `contract-final-round-4` / Reviewer 2 pass — reconciled

- Earlier record:
  `contract-final-round-4/reviewer-2-capture-annotation-cli-workflows.md`.
- Evidence: that record passed commit
  `59390b75a406eebd6660d52381c68325ebd5fbdc`. A direct set diff shows the
  reviewed candidate changes only the discovery validator-result correction
  audited above; every public workflow and cross-domain contract clause is
  otherwise unchanged.
- Disposition: reconciled through fresh complete-set review; no earlier pass
  was transferred to the new commit.

## Cross-domain reconciliation

### Reviewer 1 findings and passes — preserved resolved

- Earlier findings: `C3-CR1-R1-F1`, `C3-CR1-R1-F2`, and `C3-CR1-R1-F3`;
  later Reviewer 1 passes in contract final rounds 1 through 4.
- Evidence: the reviewed set retains the exact conservative experiment-cap
  specification and separately qualified unchanged runner; integer `0xFF`
  optional-pin semantics and named UART/SPI mapping fixtures; the closed option
  matrix; independent fixture authority; the hash/import boundary; and the
  focused API-v3/result-emission seam. The evidence-validator correction does
  not touch any of these clauses.
- Disposition: all remain resolved and independently reconciled; no pass was
  transferred.

### Reviewer 3 findings and passes — preserved resolved

- Earlier findings: `C3-CR1-R3-001`, `C3-CR1-R3-002`, `C3-CR1-R3-003`,
  `C3-CFR1-R3-001`, `C3-CFR1-R3-002`, `C3-CFR2-R3-001`, and
  `C3-CFR2-R3-002`; later Reviewer 3 passes in contract final rounds 3 and 4.
- Evidence: B5 acceptance remains pre-manifest and the terminal chain remains
  directed; prohibited use still covers every active production and
  development/test path while preserved C# stays inert; manifest verification
  remains independent and acyclic; the exact actual runner remains qualified
  before execution; and B1 retains distinct fixture/runner implementors,
  verifiers, and acceptance identities with no transferred pass. The corrected
  historical command result strengthens rather than weakens evidence accuracy.
- Disposition: all remain resolved and independently reconciled; no pass was
  transferred.

## Final disposition

The corrected discovery record now truthfully distinguishes the invalid
aggregate Exit 2 from the six successful per-manifest Exit 0 checks and binds
that correction to byte-identical validator/schema/manifest inputs. The exact
six-file candidate remains internally consistent and objectively testable in
the capture, annotation, deterministic-data, library, CLI, and cross-domain
workflow seams. Every earlier contract finding has a durable disposition. No
finding remains open. Verdict: `pass`.
