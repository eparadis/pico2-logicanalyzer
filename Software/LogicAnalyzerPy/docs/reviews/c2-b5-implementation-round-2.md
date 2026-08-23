# C2-B5 implementation review — round 2

## Identity and immutable candidate

- Lane: implementation.
- Stable identity: `cycle2-b5-implementor-replacement-1`.
- Corrected product candidate commit:
  `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`.
- Candidate tree: `06d6498f010f9cf230697aa922c2a550f8cca24c`.
- SHA-256 of the candidate's canonical Git commit object bytes:
  `c7268df0c586f13be7ac3d86e0264e33f4510f4f64a6869afec47cb4646b1594`.
- Parent verifier record: `ab336c9e5815ed7a4e638d6c8497f64e995c8255`.
- Candidate state before this record: clean worktree. This review is a separate
  descendant artifact and is not part of the corrected product candidate.

## C2B5-V001 correction

Round-1 verification found that the benchmark did not exercise actual bus
table rendering, recorded only one initial observation for several required
roles, and discarded the raw interaction timings needed to recompute its
statistics. The corrected candidate resolves that finding without changing
the viewer or B4 API behavior:

- every required initial ready/paint role has two observations: empty,
  constant-8, sparse-16, dense-24, maximum-8, maximum-16, maximum-24, and
  bus-representative-8, for 16 observations total;
- the representative and worst bus fixtures each exercise the real table in
  transition and distinct-strobe modes twice, through the production B4 API;
- the representative fixture now contains independently changing lower data
  bits and an edge-producing D7 strobe, so distinct-strobe analysis is real;
- all initial ready/paint, response-complete pan/zoom, and bus-render timings
  remain in the durable sanitized baseline as raw arrays; and
- implementation tests recompute each median and p95 from those arrays and
  require the exact role, mode, iteration, row, payload, and digest evidence.

The browser test runner starts a fresh server for the immutable verifier before
running the shell workflows. This prevents the shell's intentional shutdown
test from terminating the verifier's server. It changes test orchestration
only; React viewer code, production assets, B4 routes, OpenAPI, and generated
API types are unchanged.

## Frozen method and raw evidence

The method identifier is `c2-b5-playwright-production-v2`. It freezes a
1280-by-900 viewport at device-pixel ratio 1, Chromium `133.0.6943.16`,
Playwright `1.50.1`, Node `22.14.0`, macOS `24.6.0` x86_64, three warm-up
interactions, two load iterations per role, 30 response-complete pan/zoom
iterations, two bus iterations per role and mode, fixture counts and payloads,
production asset identity, and reliable-memory availability.

Timing uses `performance.now()` around the UI action through B4 response
completion, rendered Canvas or table DOM, and the next animation frame. Empty
navigation/load/paint uses Node's monotonic `performance.now()`. Statistics use
nearest-rank selection on the ascending raw array at index
`max(0, ceil(p * n) - 1)`. No rounding is applied; JSON retains the raw
IEEE-754 millisecond values.

Measured aggregate results:

- initial ready/paint median: `410.3999999985099 ms`;
- initial ready/paint p95: `441.19999999925494 ms`;
- repeated pan/zoom median: `310.6000000014901 ms`;
- repeated pan/zoom p95: `331.6000000014901 ms`;
- representative transition bus median/p95:
  `148.30000000074506 / 149.39999999850988 ms`;
- representative distinct-strobe bus median/p95:
  `66.5 / 66.70000000298023 ms`;
- worst transition bus median/p95:
  `398.80000000074506 / 405.79999999701977 ms`; and
- worst distinct-strobe bus median/p95:
  `144.80000000074506 / 150.39999999850988 ms`.

Every bus observation rendered 100 bounded rows in each iteration. Reliable
memory remains unavailable and is recorded as `null` with
`memory_reliable: false`; no imprecise legacy heap value is promoted to
evidence.

Frozen SHA-256 identities:

- durable baseline:
  `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`;
- fixture manifest:
  `dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`;
- representative bus fixture:
  `6cbd86b4346e7922d1685c08e8c49ed49bb7e820a5714bea1ba5e10c266328c3`;
- fixture generator:
  `3e0be8f90e6dc846803a28bb278b21f797ddc0576f5371149beb9ad185fb29c4`;
- benchmark script:
  `2efeca32fcac6eb8c98480d49d02b304b9985121d9f2fe3f85e8ffe47e1c930b`;
- implementation benchmark tests:
  `0d50c0f641b0d4a6a1bcf283357a655ffdd45af7d7556a7b37f69afd81c9059e`;
- benchmark README:
  `9860a3108ef2f0909ba0bf17280217af8ac7083caafac1811ab1af26b3f19ac1`;
- browser package manifest:
  `335004662e73f3b1ec5992ea4573f27a5f5fa152d00b4b1a50d421965df2ce55`;
  and
- unchanged production asset manifest:
  `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

These are measurements and identities only. This record proposes no
performance threshold, approves no threshold, and does not convert any timing
observation into an acceptance ceiling.

## Validation and audit

Validation against the corrected candidate produced:

- immutable round-1 verifier plus implementation benchmark checks: 6 passed;
- complete nonhardware Python suite: 350 passed and 2 documented
  sandbox-loopback skips;
- Ruff, strict mypy over 21 source files, `pip check`, OpenAPI, packaged assets,
  CLI, and `git diff --check`: pass;
- ESLint, TypeScript, and Vitest: 3 files and 5 tests passed;
- deterministic production build: 29 modules, with the production asset
  manifest unchanged;
- independent DPR/request/DOM/secret browser verifier: 1 passed;
- production browser workflows: 2 passed; and
- final production benchmark reproduction: 1 passed in 23.9 seconds.

The durable report contains no user-home path, device path, loopback URL,
capability name or value, token, or secret. Request, DOM, Canvas, bus-page,
fixture-payload, and sample-count bounds remain explicit. No governing
contract, verifier evidence, threshold artifact, B4 API, OpenAPI artifact,
generated TypeScript type, viewer behavior, or production asset changed.

## Residual risks and scope

- Shared-host timing remains informational. A separately reviewed method and
  operator-approved threshold record are still required before any ceiling can
  be accepted.
- Reliable browser memory is unavailable on this Chromium build and is
  explicitly unclaimed.
- The two full-suite loopback skips remain covered by the separately exercised
  production Playwright workflows; they are not hidden or counted as passes.
- No serial/hardware work, persistent-device action, publication, B6 work, or
  Cycle 3 work occurred.

## Implementation verdict and Git handoff

Focused implementation verdict: `pass` for corrected immutable candidate
`b5d502b5ded71fdf03b38058cb4fd6438d9110ad`, tree
`06d6498f010f9cf230697aa922c2a550f8cca24c`.

The root orchestrator should stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b5-implementation-round-2.md` as a
separate descendant record, calculate that record's SHA-256, and submit the
exact corrected candidate—not the descendant record commit—to a fresh
independent B5 verification round. No round-1 verdict transfers to the
corrected candidate.
