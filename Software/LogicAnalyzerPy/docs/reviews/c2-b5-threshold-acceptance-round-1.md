# C2-B5 threshold-proposal acceptance — round 1

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-3`
- Proposal commit: `c5eb6575625158d05b12fdd16b1c35167af385d5`
- Proposal SHA-256:
  `d314eea0979b567086eed7b346162eef76865507f9d8a111c736c94f62bbc597`
- Threshold verification commit: `62e49d98da2af1151af4c021fae4bf6e69c234aa`
- Threshold verification SHA-256:
  `7e77999b30650ab19f3b623def7f11b4e1c72b666e1c6f5791b984881eb79b71`
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`
- Product tree: `06d6498f010f9cf230697aa922c2a550f8cca24c`
- Passing product verification evidence commit:
  `d6b366bd81ff19dc6ce982941efabb9f00742c53`
- Baseline SHA-256:
  `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`
- Accepted at: `2026-08-23T20:51:21Z`
- Prior-result transfer: none
- Verdict: `pass`

## Audit boundary and immutable inputs

Acceptance independently audited the C2-B5 performance-threshold procedure in
the macOS-only governing contracts; the exact B5 candidate and passing product
verification; the frozen fixture corpus, generator, benchmark implementation,
production assets, raw baseline, method and identity fields; immutable failed
proposal round 1 and threshold-verification round 1; corrected proposal round
2; and passing independent threshold-verification round 2.

The corrected proposal commit and verification commit exist in the required
order and their file digests exactly match the assigned SHA-256 values. The
product candidate resolves to the assigned tree. Passing product verification
record `docs/reviews/c2-b5-verification-round-2.md` has SHA-256
`ebcf3d9aac7dd1e9b3817f6567ab997cc90cf537f11cb4f5b3344a7949fc0541`,
names the exact candidate/tree, and reports no open or deferred product finding.
No product, proposal, prior evidence, or governing contract was edited by this
acceptance.

## Evidence basis, arithmetic, and fresh reproduction

The baseline retains raw arrays for 16 initial ready/paint observations, 30
response-complete pan/zoom observations, and two observations for every
representative/worst transition and distinct-strobe bus group. Nearest-rank p95
is unambiguously `max(0, ceil(0.95 * n) - 1)` on ascending raw values with no
rounding. Independent recomputation confirmed every frozen p95 and its exact
IEEE-754 multiplication by `1.75`:

| Metric | Baseline p95 (ms) | Regression ceiling (ms) | Absolute ceiling (ms) |
| --- | ---: | ---: | ---: |
| Initial ready/paint | 441.19999999925494 | 772.0999999986961 | 1000 |
| Pan/zoom | 331.6000000014901 | 580.3000000026077 | 750 |
| Representative transition | 149.39999999850988 | 261.4499999973923 | 500 |
| Representative distinct strobe | 66.70000000298023 | 116.7250000052154 | 300 |
| Worst transition | 405.79999999701977 | 710.1499999947846 | 900 |
| Worst distinct strobe | 150.39999999850988 | 263.1999999973923 | 500 |

A fresh acceptance-owned production benchmark reproduced the exact method in
24.8 seconds and passed one Playwright test. Its sanitized transient report had
SHA-256
`917ce63315486a7c014cda87799b61c0129a3120d9f4b5c0626d2025065636a8`.
Fresh p95 values were respectively `421.6000000014901`,
`334.8999999985099`, `150.30000000074506`, `67`,
`404.19999999925494`, and `146.39999999850988` milliseconds. Each satisfies
both its regression and absolute ceiling without averaging, substitution,
omission, rounding, or baseline replacement.

The fresh run matched method `c2-b5-playwright-production-v2`, viewport
1280x900, DPR 1, Chromium `133.0.6943.16`, Playwright `1.50.1`, Node
`22.14.0`, macOS x86_64 host identity, fixtures/roles, generator, benchmark
script, production assets, warmups, iterations, timing boundaries, payloads,
sample counts, and row groups. Its raw timing arrays differed from the baseline
as expected and were retained through evaluation. Generated transient output
was removed after digest and arithmetic checks; the worktree returned clean.

## Usability, flakiness, resources, and B6 enforceability

The proposed 75-percent regression allowance is wider than the independently
observed primary-host variation while all absolute ceilings remain sub-second.
Because every regression ceiling is currently tighter than its corresponding
absolute ceiling, the requirement to satisfy both is conservative and directly
executable. Two samples per load/bus case are a small statistical corpus, but
nearest-rank makes p95 equal the slower observation and the dual ceilings,
fresh-reproduction evidence, and no-discard rule prevent the proposal from
hiding a valid regression. This is an acknowledged method limitation rather
than an open acceptance defect.

Resource gates are deterministic at B6: waveform span at most 100,000 samples;
`pixel_width <= 960`; fewer than 1,000 DOM nodes for maximum 24-channel input;
at most 100 rendered bus rows; at most `2 * pixel_width + 2` Canvas commands per
visible channel; and at most the visible-channel sum plus one trigger marker,
which is exactly `46,129` commands at 24 channels and 960 pixels. The fresh run
observed maxima of 12,755 commands, 216 DOM nodes, and 100 bus rows. The numeric
Canvas ceiling remains subordinate to reduced-transition and visible-window
proportionality and therefore cannot legitimize raw-sample-scaled rendering.

Fixture and method enforceability is anchored by fixture-manifest SHA-256
`dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`,
fixture-generator SHA-256
`3e0be8f90e6dc846803a28bb278b21f797ddc0576f5371149beb9ad185fb29c4`,
benchmark-script SHA-256
`2efeca32fcac6eb8c98480d49d02b304b9985121d9f2fe3f85e8ffe47e1c930b`,
and production-asset-manifest SHA-256
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
Reliable heap measurement is unavailable, explicitly recorded as `null` with
`memory_reliable: false`, and correctly excluded rather than inferred.

## Findings and dispositions

1. `C2B5-TV001`: closed. Round 2 freezes fixture/raw-capture and method
   identities while explicitly requiring every enforcement run to collect and
   retain new raw timing arrays that are expected to differ from baseline.
2. `C2B5-TV002`: closed. Round 2 supplies exact per-channel and aggregate Canvas
   formulas, including the trigger marker, while retaining reduced-transition
   and visible-window proportionality.
3. `C2B5-TA001`: no new threshold-acceptance finding; closed by this verdict.

No finding is open or deferred. Round-1 proposal and verification remain
immutable failed history and are not silently rewritten or treated as passing.

## Governance, scope, and decision

A valid slow observation cannot be discarded. A retry is allowed only after a
documented environmental invalidation, and an invalid run cannot replace a
valid slow run without that record. Shared-CI timing remains informational
unless it reproduces the exact frozen primary-host method. Any intentional
fixture, generator, benchmark, browser, viewport, DPR, asset, timing-boundary,
iteration, or host-method change requires a new reviewed proposal and explicit
operator approval. These rules prevent hidden threshold rebasing at B6.

The proposal is limited to the frozen primary macOS production method and makes
no claim for other operating systems, development builds, remote serving,
serial capture, or unfrozen hardware. This audit performed no serial/hardware,
firmware, C#/.NET, persistent-device, public-server, packaging/publication, B6,
or Cycle 3 action.

Verdict is `pass` for the corrected threshold proposal only. This acceptance
does **not** grant operator approval, activate the thresholds, complete overall
C2-B5 product acceptance, authorize a C2-B5 manifest/checkpoint, or begin B6.
Exact Git handoff: the root orchestrator may stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b5-threshold-acceptance-round-1.md`,
record its SHA-256, and then present the unchanged round-2 proposal plus this
verification/acceptance packet to the operator for explicit approval or
amendment. Overall B5 acceptance follows only after that operator decision.
