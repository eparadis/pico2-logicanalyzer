# C2-B5 rendering-threshold proposal — round 1

- Proposer: Cycle 2 root orchestrator
- Proposed: 2026-08-23 (America/Los_Angeles)
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`
- Product tree: `06d6498f010f9cf230697aa922c2a550f8cca24c`
- Passing verification evidence commit: `d6b366b`
- Baseline: `docs/performance/c2-b5-baseline-round-1.json`
- Baseline SHA-256: `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`
- Fixture manifest SHA-256: `dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`
- Production asset manifest SHA-256: `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`
- Status: proposed; not approved and not yet an acceptance criterion

## Frozen measurement method

Use the exact baseline method `c2-b5-playwright-production-v2`: production
assets, loopback-only Python server, Chromium `133.0.6943.16`, Playwright
`1.50.1`, Node `22.14.0`, macOS x86_64 primary host, viewport 1280 by 900,
device-pixel ratio 1, three warmups, two initial ready/paint observations for
each of the eight required roles, 30 response-complete pan/zoom observations,
and two observations for every representative/worst transition and
distinct-strobe bus group. Statistics use ascending raw samples and nearest
rank `max(0, ceil(p * n) - 1)` with no rounding.

The frozen fixture, generator, benchmark-script, browser, host, asset, timing,
iteration, payload, sample-count, transition-count, row-count, and raw-sample
identity fields must match the approved baseline before timing is evaluated.
Shared-CI timings are informational only unless this exact primary-host method
is reproduced.

## Proposed timing acceptance rule

Every metric below must satisfy both its absolute usability ceiling and its
regression ceiling. The regression ceiling is the frozen baseline p95 multiplied
by `1.75`; comparison uses the unrounded IEEE-754 millisecond values.

| Metric | Frozen p95 (ms) | Absolute ceiling (ms) | Regression ceiling (ms) |
| --- | ---: | ---: | ---: |
| All required initial ready/paint loads | 441.19999999925494 | 1000 | 772.0999999986961 |
| Response-complete pan/zoom | 331.6000000014901 | 750 | 580.3000000026077 |
| Representative transition bus table | 149.39999999850988 | 500 | 261.4499999973923 |
| Representative distinct-strobe bus table | 66.70000000298023 | 300 | 116.7250000052154 |
| Worst-case transition bus table | 405.79999999701977 | 900 | 710.1499999947846 |
| Worst-case distinct-strobe bus table | 150.39999999850988 | 500 | 263.1999999973923 |

A run fails if any p95 exceeds either ceiling. No metric may be omitted,
substituted, averaged with another group, or silently rebased. C2-B6 may repeat
an invalid run only for a documented environmental invalidation such as a
background interruption; it may not discard a valid slow observation.

## Proposed deterministic resource ceilings

The same run must also prove:

- every waveform request spans at most 100,000 samples and declares
  `pixel_width <= 960`;
- the rendered document remains below 1,000 DOM nodes for the frozen maximum
  24-channel case;
- each bus page renders at most 100 rows;
- Canvas planning remains bounded by the returned reduced transitions and the
  visible 960-pixel viewport rather than raw capture sample count;
- all nine frozen fixture roles remain present with unchanged digests; and
- capability values and machine-local paths remain absent from URL, Referer,
  storage, DOM, console/network logs, errors, snapshots, and durable reports.

Heap usage remains recorded as `null` with `memory_reliable: false`; no memory
threshold is proposed until a reliable cross-run collection method exists.

## Rationale and limitations

The 75-percent regression allowance is intentionally wider than normal local
run noise while still rejecting a visibly slower interaction path. Independent
verification reproduced the method, raw samples, statistics, bus roles, and
fixture generator before this proposal. Absolute ceilings prevent a future
fast baseline from making harmless noise the only criterion and preserve a
human-usable upper bound.

These thresholds apply only to the frozen primary-macOS production method and
the accepted B5 fixture corpus. They make no support or timing claim for other
operating systems, remote serving, development builds, live serial capture, or
unfrozen hardware. Intentional method, fixture, browser, viewport, or asset
changes require a new reviewed proposal and explicit operator approval; they
must not silently update this record.
