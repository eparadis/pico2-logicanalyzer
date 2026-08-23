# C2-B5 rendering-threshold proposal — round 2

- Proposer: Cycle 2 root orchestrator
- Proposed: 2026-08-23 (America/Los_Angeles)
- Supersedes: `c2-b5-threshold-proposal-round-1.md`
- Round-1 verification: `docs/reviews/c2-b5-threshold-verification-round-1.md`
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`
- Product tree: `06d6498f010f9cf230697aa922c2a550f8cca24c`
- Passing product verification evidence commit: `d6b366b`
- Baseline SHA-256: `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`
- Fixture manifest SHA-256: `dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`
- Production asset manifest SHA-256: `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`
- Status: proposed; not approved and not yet an acceptance criterion

## Frozen method and identity

Use baseline method `c2-b5-playwright-production-v2`: production assets,
loopback-only Python server, Chromium `133.0.6943.16`, Playwright `1.50.1`,
Node `22.14.0`, macOS x86_64 primary host, viewport 1280 by 900, DPR 1, three
warmups, two initial ready/paint observations for every required role, 30
response-complete pan/zoom observations, and two observations for each
representative/worst transition and distinct-strobe bus group. Statistics use
ascending raw samples and nearest rank `max(0, ceil(p * n) - 1)` without
rounding.

The fixture bytes/digests, role assignments, generator, benchmark script,
browser/version, host/OS/architecture, assets, viewport, DPR, timing boundaries,
iteration counts, payload bytes, sample/transition counts, and expected bounded
row groups are frozen capture and method identities and must match before timing
is evaluated. Each enforcement run must collect and retain its own fresh raw
timing arrays. Those fresh values are expected to differ from the baseline and
are compared by the rules below; they must never be required to equal baseline
raw timing arrays. Shared-CI timing remains informational unless this exact
primary-host method is reproduced.

## Timing acceptance rule

Every fresh p95 must satisfy both the absolute usability ceiling and the
regression ceiling. The regression ceiling is the frozen baseline p95 times
`1.75`, compared using unrounded IEEE-754 millisecond values.

| Metric | Frozen p95 (ms) | Absolute ceiling (ms) | Regression ceiling (ms) |
| --- | ---: | ---: | ---: |
| All required initial ready/paint loads | 441.19999999925494 | 1000 | 772.0999999986961 |
| Response-complete pan/zoom | 331.6000000014901 | 750 | 580.3000000026077 |
| Representative transition bus table | 149.39999999850988 | 500 | 261.4499999973923 |
| Representative distinct-strobe bus table | 66.70000000298023 | 300 | 116.7250000052154 |
| Worst-case transition bus table | 405.79999999701977 | 900 | 710.1499999947846 |
| Worst-case distinct-strobe bus table | 150.39999999850988 | 500 | 263.1999999973923 |

Any omitted/substituted group or any p95 above either applicable ceiling fails.
No result may be averaged with another group or silently rebased. C2-B6 may
repeat an invalid run only for a documented environmental invalidation such as
a background interruption; it may not discard a valid slow observation.

## Deterministic resource ceilings

The same run must prove all of the following:

- waveform request span is at most 100,000 samples and `pixel_width <= 960`;
- maximum 24-channel document size is below 1,000 DOM nodes;
- each rendered bus page contains at most 100 rows;
- total Canvas planned commands for the frozen maximum-width viewport are at
  most `24 * (2 * 960 + 2) + 1 = 46,129`, including the trigger marker;
- every individual channel command plan is bounded by
  `2 * pixel_width + 2`, and the aggregate plan is the sum for visible channels
  plus at most one trigger-marker command;
- all nine frozen fixture roles retain their approved digests; and
- capability values and machine-local paths remain absent from URL, Referer,
  storage, DOM, console/network logs, errors, snapshots, and durable reports.

The Canvas formula is an upper bound, not a target: implementations remain
required to use reduced transitions and visible-window work. Heap usage remains
`null` with `memory_reliable: false`; no memory threshold is proposed without a
reliable collection method.

## Rationale and limitations

The 75-percent regression allowance is wider than normal local noise while
still rejecting visibly slower interaction. Absolute ceilings preserve a
human-usable upper bound. Independent product verification reproduced fixtures,
raw statistics, both bus modes, and the measurement method before proposal.

These thresholds apply only to the frozen primary-macOS production method and
B5 corpus. They claim nothing for other operating systems, development builds,
remote serving, live serial capture, or unfrozen hardware. Intentional method,
fixture, browser, viewport, or asset changes require a new reviewed proposal
and explicit operator approval; they may not silently revise this record.
