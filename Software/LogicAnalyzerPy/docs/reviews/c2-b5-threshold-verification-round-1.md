# C2-B5 threshold-proposal verification round 1

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T20:45:46Z`.
- Proposal commit: `1376708`; proposal SHA-256:
  `40f3d89526bf0a9662dc0e2b5964c934ad38c9bad17264c2940a8366107644fe`.
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`;
  tree `06d6498f010f9cf230697aa922c2a550f8cca24c`.
- Passing B5 verification evidence commit: `d6b366bd81ff19dc6ce982941efabb9f00742c53`.
- Baseline SHA-256: `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`.
- Verdict: `changes_required`.

## Findings and dispositions

1. `C2B5-TV001` — open. The precondition says that “raw-sample identity fields” must match the
   approved baseline before timing is evaluated. The durable baseline contains both capture
   sample identities and raw timing samples. Requiring a new run's raw timing samples to match
   is impossible and conflicts with evaluating a fresh run; requiring only capture fixture
   bytes/counts is sensible. B6 needs the proposal to say explicitly that frozen fixture/raw
   capture identities must match, while fresh raw timing arrays must have the frozen shape and
   method but are expected to differ.
2. `C2B5-TV002` — open. Five deterministic resource limits are directly enforceable, but the
   Canvas bullet only says work is “bounded” by transitions and 960 visible pixels. It supplies
   neither the already evidenced numeric ceiling (`24 * (2 * 960 + 2) + 1 = 46,129` planned
   commands including the marker) nor another exact per-visible-channel/transition formula.
   B6 cannot deterministically decide that bullet from the proposal alone. Freeze an explicit
   command-count rule without weakening the visible-window/reduced-transition requirement.

## Independent calculations and identity checks

Nearest-rank p95 values were recomputed from the baseline raw arrays using ascending samples
at `max(0, ceil(0.95 * n) - 1)` with no rounding. Every proposed p95 matches. IEEE-754
multiplication by `1.75` also matches exactly:

| Metric | Baseline p95 | p95 × 1.75 | Absolute | Effective `min` |
| --- | ---: | ---: | ---: | ---: |
| Initial ready/paint | 441.19999999925494 | 772.0999999986961 | 1000 | 772.0999999986961 |
| Pan/zoom | 331.6000000014901 | 580.3000000026077 | 750 | 580.3000000026077 |
| Representative transition | 149.39999999850988 | 261.4499999973923 | 500 | 261.4499999973923 |
| Representative distinct strobe | 66.70000000298023 | 116.7250000052154 | 300 | 116.7250000052154 |
| Worst transition | 405.79999999701977 | 710.1499999947846 | 900 | 710.1499999947846 |
| Worst distinct strobe | 150.39999999850988 | 263.1999999973923 | 500 | 263.1999999973923 |

Because every regression ceiling is lower than its absolute ceiling, “must satisfy both” is
unambiguous and equivalent to the effective values above. The limits are 75% above frozen p95,
are above the fresh reproduced observations, retain sub-second absolute usability bounds, and
are neither scope-weak nor facially flaky for the frozen primary-host method.

The referenced baseline/candidate/verification identities match. Baseline method
`c2-b5-playwright-production-v2`, viewport 1280x900, DPR 1, Chromium/Playwright/Node/macOS x64,
warmups, iterations, timing boundary, payload/sample/transition/row/DOM data, memory-unavailable
declaration, nine fixture roles, and raw arrays are present. Frozen fixture manifest SHA-256 is
`dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`; production asset
manifest SHA-256 is `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

## Governance and scope

The dual timing rule, nearest-rank/no-rounding semantics, no omitted/substituted/averaged
metric rule, valid-slow-run retention, documented environmental invalidation retry rule,
shared-CI informational boundary, reliable-memory exclusion, explicit new-review/operator
approval for method changes, and prohibition on silent rebasing are sound.

This is verification of a proposal only. It does not approve thresholds for the operator,
change product/proposal/baseline, perform acceptance, or begin B6/Cycle 3.

Open findings: `C2B5-TV001`, `C2B5-TV002`.
