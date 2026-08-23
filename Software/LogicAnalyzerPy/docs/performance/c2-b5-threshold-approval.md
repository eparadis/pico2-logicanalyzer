# C2-B5 operator-approved rendering thresholds

- Operator decision: `approved`
- Approved at: `2026-08-23T20:55:48Z`
- Approved proposal: `c2-b5-threshold-proposal-round-2.md`
- Proposal commit: `c5eb6575625158d05b12fdd16b1c35167af385d5`
- Proposal SHA-256: `d314eea0979b567086eed7b346162eef76865507f9d8a111c736c94f62bbc597`
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`
- Product tree: `06d6498f010f9cf230697aa922c2a550f8cca24c`
- Baseline SHA-256: `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`
- Product verification commit: `d6b366bd81ff19dc6ce982941efabb9f00742c53`
- Threshold verification commit: `62e49d98da2af1151af4c021fae4bf6e69c234aa`
- Threshold acceptance commit: `dbdc9ef`

The operator explicitly approved the unchanged Cycle 2 B5 rendering-threshold
proposal round 2. The full proposal, including its frozen method and identities,
fresh-run semantics, dual timing rules, resource ceilings, retry governance,
CI boundary, limitations, and no-silent-rebase rule, is incorporated by exact
commit and SHA-256 above.

The approved effective regression ceilings are:

- all required initial ready/paint loads: `772.0999999986961 ms`;
- response-complete pan/zoom: `580.3000000026077 ms`;
- representative transition bus table: `261.4499999973923 ms`;
- representative distinct-strobe bus table: `116.7250000052154 ms`;
- worst-case transition bus table: `710.1499999947846 ms`;
- worst-case distinct-strobe bus table: `263.1999999973923 ms`.

Every group remains additionally subject to the absolute ceiling in the
proposal. Approved deterministic resource ceilings are 46,129 aggregate Canvas
commands under the frozen maximum-width viewport formula, fewer than 1,000 DOM
nodes, at most 100,000 samples and 960 pixels per waveform request, and at most
100 rows per bus page. No reliable heap threshold is approved.

This approval is a subordinate Cycle 2 acceptance input for C2-B5 and C2-B6.
It does not authorize silent rebasing, a non-macOS support claim, live serial
work before C2-B6, changes to governing contracts, or Cycle 3.
