# Cycle 3 final contract review — decoder API, runtime, and fixtures

- Gate and round: `contract`; `contract-final-round-2`
- Reviewer: `/root/c3_final_r2_decoder` (decoder API, runtime, fixtures, and provenance)
- Reviewed commit: `4d094b6d9a71e44387a386c85a586b1ecf5230fb`
- Reviewed tree: `f53d0f23bb63b92e54099fbcfce5d4fb047fec70`
- UTC timestamp: `2026-08-26T15:06:17Z`
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

I also statically inspected the focused checked-in decoder, shim, and helper
sources, their inert Git provenance and license headers, every earlier
contract-gate review record, and the capture/result seams needed by this
charter. I did not execute, build, restore, install, import, or load any decoder,
C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or external/reference
runtime, and none supplied expected output or corroborating evidence.

## Findings and dispositions

No finding remains open. The candidate keeps the exact hash/import allowlist,
host-owned decoder identity, focused API-v3 behavior, integer `0xFF` optional-
pin contract, closed option-coverage matrix, independently authored fixture and
version-1 golden authority, complete typed-emission seam, and B1/B3/B5 proof
ownership explicit and objectively testable.

The corrected B1 sequence also preserves the decoder-domain trust seam: the
semantic-fixture candidate is independently accepted before the actual
characterization runner exists; the later immutable runner candidate binds the
accepted fixture/cap digests, exact executable/arguments, launch/import
configuration, probe sources, and all cap and cleanup plumbing; independent
inert/hostile non-decoder proof, accumulated validation, and distinct acceptance
must pass and state that no decoder ran; and only that unchanged runner may then
execute an approved snapshot. The fixture owner cannot author, verify, or
approve the runner candidate, and snapshot output never becomes an expected-
result oracle.

## Prior-round reconciliation

### `contract-round-1` / `C3-CR1-R1-F1` — resolved

- Earlier record:
  `contract-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains in reviewed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb`. The discovery, orchestration,
  batch, review-protocol, and charter documents require exact conservative
  experiment-only wall, kill-grace, input, output/diagnostic, nesting,
  recursion, and memory/address-space caps before snapshot execution. The
  corrected batch sequence additionally requires their enforcement on the
  immutable actual runner candidate before first execution. A cap termination
  is not a passing baseline, and caps cannot be weakened to obtain data.
- Disposition: resolved; no characterization starts unbounded or on an
  unreviewed cap-enforcement path.

### `contract-round-1` / `C3-CR1-R1-F2` — resolved

- Earlier record:
  `contract-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains unchanged in reviewed
  commit `4d094b6d9a71e44387a386c85a586b1ecf5230fb`. The discovery and execution
  contracts freeze built-in integer pin values, integer `0xFF` (`255`) for an
  absent optional slot, required-then-optional tuple order, and
  `has_channel()` false exactly for such a slot. They require UART RX-only and
  TX-only plus SPI MISO-only, MOSI-only, and no-CS fixtures and keep the sentinel
  out of capture levels and public results.
- Disposition: resolved; optional-pin representation, tuple behavior, and named
  mapping fixtures remain exact.

### `contract-round-1` / `C3-CR1-R1-F3` — resolved

- Earlier record:
  `contract-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit and evidence: resolution first appeared in
  `ed24f1badfff5200494cf2408e53c85cb44c0f02` and remains unchanged in reviewed
  commit `4d094b6d9a71e44387a386c85a586b1ecf5230fb`. Before characterization, the
  closed matrix must classify every checked-in option default, enumeration,
  numeric boundary, and sentinel as `direct-fixture` with a named fixture,
  `static-equivalence` with a named directly covered fixture and source-based
  argument, or `unsupported` with pre-launch rejection. B3 audits every row
  against accepted fixture digests and B5 repeats the audit; “material options”
  is not a valid disposition.
- Disposition: resolved; coverage remains closed, digest-bound, and auditable.

### `contract-final-round-1` / Reviewer 1 pass — preserved

- Earlier record:
  `contract-final-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit and evidence: that record passed commit
  `ed24f1badfff5200494cf2408e53c85cb44c0f02`. Reviewed commit
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb` preserves every decoder/API/
  fixture resolution and changes only the pre-execution-runner and directed-
  closure contracts plus their review invariants.
- Disposition: preserved after complete-set substantive re-review; no earlier
  Reviewer 1 finding was reopened.

## Cross-domain reconciliation

### `contract-final-round-1` / `C3-CFR1-R3-001` — resolved at the decoder/runtime seam

- Earlier record:
  `contract-final-round-1/reviewer-3-security-delivery-orchestration.md`.
- Resolving commit and evidence:
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb` places the actual non-installed
  characterization runner, method, exact launch/import configuration,
  digest/import rules, all cap plumbing, and termination/close/reap behavior in
  a separate immutable pre-execution candidate. Independent non-decoder probe
  verification, accumulated validation, and distinct acceptance all bind that
  exact candidate and precede any snapshot execution. Any relevant change
  creates a new runner candidate and repeats the gate.
- Disposition: resolved; the API/fixture inputs are consumed by one reviewed
  unchanged execution path without transferring oracle ownership.

### `contract-final-round-1` / `C3-CFR1-R3-002` — resolved with no decoder-domain regression

- Earlier record:
  `contract-final-round-1/reviewer-3-security-delivery-orchestration.md`.
- Resolving commit and evidence:
  `4d094b6d9a71e44387a386c85a586b1ecf5230fb` freezes the directed terminal order:
  committed B5 manifest and verification record, closure-pending checkpoint,
  immutable completion-proof candidate with no future closure identity,
  distinct committed closure verdict, and terminal non-audit-input seal. The
  proof and seal bind the already accepted decoder, fixture, runner, method,
  threshold, and conformance identities without amending an audited input.
- Disposition: resolved; final decoder evidence remains immutable and has no
  circular or predicted future record.

No earlier contract-gate finding relevant to this charter lacks a durable
disposition, and no new decoder/API/runtime/fixture or cross-domain finding was
identified. Verdict: `pass`.
