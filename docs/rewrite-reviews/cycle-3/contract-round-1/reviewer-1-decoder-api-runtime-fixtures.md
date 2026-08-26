# Cycle 3 contract review — decoder API, runtime, and fixtures

- Gate and round: `contract`; `contract-round-1`
- Reviewer: `/root/c3_contract_review_decoder` (decoder API, runtime, fixtures, and provenance)
- Reviewed commit: `8bd6ba06a42ea190f50c7b15789638938c8716d2`
- Reviewed tree: `19fc91d2cfaa526f2bee7ee2835423e5ccbd50ee`
- UTC timestamp: `2026-08-26T06:04:47Z`
- Verdict: `changes_required`

## Set-completeness declaration

I inspected every path in the exact six-file Step 8 contract-review set at the
commit and tree above, with no worktree file substituted: the roadmap,
discovery review, orchestration contract, batch procedure, Cycle 3 review
README, and architectural-domain charters.

## Findings and dispositions

### C3-CR1-R1-F1 — High — first decoder execution lacks a pre-threshold safety envelope

- Evidence: discovery and batch B1 allow characterization to execute the
  snapshots before product thresholds are proposed and approved, but do not
  require exact independently reviewed experiment-only limits first.
- Violated invariant: no decoder execution may be initially unbounded while
  the evidence needed to select product limits is collected.
- Requested resolution: require an independently reviewed and accepted
  pre-execution envelope with exact wall-time deadline, termination/force-kill
  grace, input, output/diagnostic byte and record, recursion, and memory/address-
  space caps. A capped run is not a passing baseline, the envelope may never be
  weakened to obtain observations, and later operator-approved product limits
  replace it.
- Disposition: open.

### C3-CR1-R1-F2 — Medium — absent optional-channel representation is not frozen

- Evidence: the contract promises a frozen absent-channel sentinel but gives
  neither its value/type nor complete `has_channel()` and pin-tuple behavior.
- Violated invariant: compatibility inputs and fixture expectations must be
  exact before host implementation.
- Requested resolution: freeze the sentinel and tuple semantics, and require
  UART RX-only/TX-only plus SPI MISO-only/MOSI-only/no-CS fixtures. The checked-
  in static C# source uses `0xFF`; choosing another value requires an explicit
  intentional-difference record.
- Disposition: open.

### C3-CR1-R1-F3 — Medium — “material options” is not a closed coverage rule

- Evidence: B1/B3 require defaults and material options without classifying
  every enumerated choice, numeric boundary, or sentinel.
- Violated invariant: decoder option proof must be objective and auditable.
- Requested resolution: require a closed B1 coverage matrix classifying every
  option choice/boundary/sentinel as directly covered, statically equivalent
  with a named fixture, or unsupported, and require B3 and B5 to audit the
  matrix and fixture digests.
- Disposition: open.

## Prior-round reconciliation

No earlier contract-review round or finding exists for this gate/domain.
