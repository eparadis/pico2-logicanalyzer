# Cycle 3 final contract review — decoder API, runtime, and fixtures

- Gate and round: `contract`; `contract-final-round-1`
- Reviewer: `/root/c3_final_r1_decoder` (decoder API, runtime, fixtures, and provenance)
- Reviewed commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`
- Reviewed tree: `511de8bc4f7ccc6219c81e61fe55a3722b96a20b`
- UTC timestamp: `2026-08-26T14:55:01Z`
- Verdict: `pass`

## Set-completeness declaration

I inspected every path in the exact six-file Step 8 contract-review set at the
commit and tree above, with no worktree file substituted: the roadmap,
discovery review, orchestration contract, batch procedure, Cycle 3 review
README, and architectural-domain charters. I also statically inspected the
focused checked-in decoder/shim/helper sources, their provenance and license
headers, and the accepted capture/replay/CSV seams required by the Reviewer 1
charter. No decoder, C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or
external/reference runtime was executed, installed, imported, or used as an
oracle.

## Findings and dispositions

No finding remains open. The exact snapshot and import boundary, focused
API-v3 behavior, independent-fixture authority, optional-channel behavior,
closed option coverage, typed emission seam, staged resource gate, and B1/B3/B5
proof ownership are explicit, internally consistent, and objectively testable.
The lower-authority roadmap's historical and later-parity references do not
authorize Cycle 3 execution or proof and are expressly subordinated to the
Cycle 3 contracts.

## Prior-round reconciliation

### C3-CR1-R1-F1 — resolved

- Earlier record: `contract-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`.
- Evidence: `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` freezes,
  before the first characterization runner or snapshot execution, exact
  conservative experiment-only wall deadline, terminate/force-kill grace,
  input, output/diagnostic, nesting, recursion, and memory/address-space caps;
  independent verification and acceptance must pass before execution, a capped
  termination is not a passing baseline, caps cannot be weakened, and later
  operator-approved product thresholds replace them. `CYCLE3_BATCH_EXECUTION.md`
  makes this a committed semantic-fixture candidate and orders verifier,
  accumulated, and acceptance gates before characterization.
- Disposition: resolved; no decoder characterization can begin unbounded or
  treat an experiment-cap failure as success.

### C3-CR1-R1-F2 — resolved

- Earlier record: `contract-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`.
- Evidence: `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` freezes
  every pin tuple element as an exact built-in integer, mapped values as `0` or
  `1`, absent optional values as integer `0xFF` (`255`), full declared
  required-then-optional tuple order, required-channel presence, and
  `has_channel()` false exactly for an optional `0xFF` slot. The discovery,
  orchestration, and batch contracts require UART RX-only/TX-only and SPI
  MISO-only/MOSI-only/no-CS fixtures and prevent the sentinel from becoming a
  capture level or public result.
- Disposition: resolved; the sentinel, tuple behavior, `has_channel()` seam,
  and named mapping fixtures are exact.

### C3-CR1-R1-F3 — resolved

- Earlier record: `contract-round-1/reviewer-1-decoder-api-runtime-fixtures.md`.
- Resolving commit: `ed24f1badfff5200494cf2408e53c85cb44c0f02`.
- Evidence: `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` requires
  a closed matrix before characterization that classifies every checked-in
  default, enumerated choice, inclusive/exclusive numeric boundary, and
  sentinel as exactly `direct-fixture` with a named fixture,
  `static-equivalence` with a named directly covered fixture and source-based
  argument, or `unsupported` with pre-launch rejection. It explicitly includes
  UART packet and sample-point boundaries/enumerations, every SPI enumeration
  and word-size boundary, and both I2C choices. B3 audits every accepted row
  against fixture digests and B5 repeats that audit; “material options” is not
  an allowed disposition.
- Disposition: resolved; option conformance is closed and auditable rather than
  subjective sampling.
