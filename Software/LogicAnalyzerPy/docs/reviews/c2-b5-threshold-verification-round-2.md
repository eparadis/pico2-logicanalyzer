# C2-B5 threshold-proposal verification round 2

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T20:47:56Z`.
- Proposal commit: `c5eb657`; proposal SHA-256:
  `d314eea0979b567086eed7b346162eef76865507f9d8a111c736c94f62bbc597`.
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`;
  tree `06d6498f010f9cf230697aa922c2a550f8cca24c`.
- Passing B5 verification evidence commit: `d6b366bd81ff19dc6ce982941efabb9f00742c53`.
- Baseline SHA-256: `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`.
- Verdict: `pass`.

## Findings and dispositions

1. `C2B5-TV001` — closed. The proposal now unambiguously freezes capture/fixture/method
   identities before timing evaluation while requiring each enforcement run to retain its own
   fresh raw timing arrays. It explicitly states that fresh timings are expected to differ and
   must not equal the baseline arrays.
2. `C2B5-TV002` — closed. The proposal freezes both executable Canvas bounds: at most
   `2 * pixel_width + 2` planned commands per visible channel, and the visible-channel sum plus
   at most one trigger-marker command. At 24 channels and 960 pixels this is exactly
   `24 * 1,922 + 1 = 46,129`, consistent with the product planning function and existing
   verifier/browser assertions. Reduced-transition and visible-window proportionality remains
   mandatory, so the numeric ceiling cannot legitimize raw-sample-scaled work.

## Independent arithmetic and identity verification

Nearest-rank p95 was freshly recomputed from the durable raw arrays without rounding:

| Metric | Recomputed baseline p95 (ms) | Exact × 1.75 (ms) | Absolute (ms) |
| --- | ---: | ---: | ---: |
| Initial ready/paint | 441.19999999925494 | 772.0999999986961 | 1000 |
| Pan/zoom | 331.6000000014901 | 580.3000000026077 | 750 |
| Representative transition | 149.39999999850988 | 261.4499999973923 | 500 |
| Representative distinct strobe | 66.70000000298023 | 116.7250000052154 | 300 |
| Worst transition | 405.79999999701977 | 710.1499999947846 | 900 |
| Worst distinct strobe | 150.39999999850988 | 263.1999999973923 | 500 |

Every table value matches the proposal. “Satisfy both” is executable as comparison against
both listed ceilings; for this baseline each regression ceiling is the tighter value. The
proposal correctly rejects omitted/substituted/averaged groups and preserves unrounded
IEEE-754 comparison.

Candidate, tree, verification, baseline, fixture manifest
`dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`, and production asset
manifest `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9` identities match the
accepted B5 evidence. The method freezes Chromium/Playwright/Node/macOS x64, viewport/DPR,
warmups, iteration counts, timing boundaries, generator/script/assets, fixture bytes/roles,
payload/sample/transition/row identities, and fresh raw timing retention before evaluation.

## Enforceability, usability, and governance

The timing limits are 75% above frozen p95, above the independent reproduction, and retain
sub-second absolute usability ceilings. They are evidence-based and sufficiently tolerant of
observed primary-host variation without becoming weaker than the required initial, interaction,
representative-bus, or worst-bus scope. Resource limits for request span/pixels, DOM nodes, bus
rows, Canvas planning, fixtures, nondisclosure, and reliable-memory exclusion are deterministic
at B6.

Only documented environmental invalidation permits a retry; a valid slow observation cannot be
discarded. Shared-CI timing remains informational outside the exact primary-host method.
Intentional method/fixture/browser/viewport/asset changes require a new reviewed proposal and
explicit operator approval, so silent rebasing is prohibited.

This verdict verifies the corrected proposal only. It does not grant operator approval, make
the proposal an acceptance criterion, edit product/proposal, perform acceptance, or begin B6.

Open findings: none. Deferred findings: none.
