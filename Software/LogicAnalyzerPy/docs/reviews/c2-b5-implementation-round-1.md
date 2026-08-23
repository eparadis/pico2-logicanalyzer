# C2-B5 implementation review — round 1

## Identity and immutable candidate

- Lane: implementation.
- Stable identity: `cycle2-b5-implementor-replacement-1`.
- Candidate commit:
  `5e1a4cc87325e0c1f39df6b0f3c5757f900d1504`.
- Candidate tree: `9c2b786680c4d30941f06fd9fc5eaf4d448bf484`.
- Candidate state before this record: clean worktree; this review is a separate
  descendant artifact and is not part of the product candidate.
- Prerequisite: accepted C2-B4 candidate and manifest. No B4 production,
  OpenAPI, generated-TypeScript, or fingerprint surface changed.

## Product outcome

The candidate completes the bounded offline C2-B5 product outcome:

- schema-1/schema-2 replay and explicit-metadata self-timed CSV import use the
  accepted asynchronous B4 import, polling, cancellation, capture, channels,
  waveform, bus, export, readiness, and shutdown API;
- 8-, 16-, and 24-channel labels, physical/packed mappings, visibility
  controls, digital Canvas waveforms, trigger marker, exact cursor sample/time
  and per-channel values are visible;
- pointer drag and keyboard pan, cursor-centered wheel and keyboard zoom, and
  the 100,000-sample API window limit are deterministic and clamped;
- ordered LSB-first transition and distinct-strobe bus controls drive the
  Python-owned results, a bounded 100-row table, pagination, and deterministic
  safe download;
- loading, ready, empty, error, disconnected, cancelling, and shutdown are
  explicit. Cancellation polls to terminal cleanup and restores the prior
  ready/empty state; reconnect and component cleanup abort stale requests;
- DOM nodes scale with controls/channels, while waveform requests and Canvas
  commands scale with visible channels, pixels, and reduced transitions rather
  than raw capture length; and
- production uses committed Vite assets without a CDN, Node runtime, serial
  open, development server, persistent server file, or user-controlled server
  path.

## Changed surfaces

- React/API/viewer: `web/src/api.ts`, `web/src/main.tsx`, `web/src/style.css`.
- Pure geometry/Canvas plus unit/component tests: `web/src/geometry.ts`,
  `web/src/waveform.ts`, and their tests plus `web/src/shell.test.ts`.
- Production browser coverage: `web/tests/shell.spec.ts` and
  `web/playwright.config.ts`.
- Frozen benchmark method/corpus: `web/tests/performance.spec.ts`,
  `web/benchmarks/`, and
  `tests/implementation/test_b5_performance_fixtures.py`.
- Baseline evidence: `docs/performance/c2-b5-baseline-round-1.json` and its
  README.
- Deterministic production assets and manifest under
  `src/pico_logic_analyzer/web/assets/` and `web/production-assets.json`.
- Node scripts only in `web/package.json`; dependency locks did not change.

## Clean bootstrap and validation

The root approval broker installed `requirements-dev.lock` into the fresh
Python 3.12.13 environment `/private/tmp/cycle2-clean-b5-312`; the command
exited 0. The implementation lane then ran the following against the candidate:

| Command | Result |
| --- | --- |
| `python -m pip install --no-build-isolation --no-deps -e .` | pass; editable source wheel installed |
| `python -m pip check` | pass; no broken requirements |
| `python -m ruff check .` | pass |
| `python -m mypy src` | pass; 21 source files |
| `python -m pytest -m 'not hardware' -q` | pass; 346 passed, 2 sandbox-loopback skips |
| `python -m pytest tests/implementation/test_web_api.py -q` using the approved loopback command shape | pass; 1 passed |
| `python -m pytest tests/implementation/test_b5_performance_fixtures.py -q` | pass; 2 passed in the clean environment |
| `python -m pico_logic_analyzer --help` | pass; accepted CLI commands present |
| `python tools/check_openapi.py` | pass; accepted B4 schema/types unchanged |
| `python scripts/check_web_assets.py` | pass |
| clean `npm ci --ignore-scripts --no-audit --no-fund` | pass; 215 locked packages |
| `npm run lint` | pass |
| `npm run typecheck` | pass |
| `npm test -- --run` | pass; 3 files, 5 tests |
| `npm run build` | pass; 29 modules; deterministic production assets |
| `npm run test:browser` | pass; 2 production-browser tests |
| `npm run test:browser -- tests/performance.spec.ts` | pass; 1 production benchmark test |
| `git diff --check` | pass |

The two full-suite skips are the pre-existing tests that intentionally report
when the command sandbox prohibits loopback binding. They are not omitted
product evidence: the separately approved real-loopback API test passed, and
the production Playwright server/browser workflows also passed on loopback.

## Browser, bounds, and security proof

The production browser suite exercised CSV at 8/16/24 widths, schema-1 and
schema-2 replay, mapping preview, labels/toggles, exact cursor values, trigger,
keyboard/pointer/wheel navigation, both bus modes, pagination, download,
oversize rejection, export failure, cancellation, disconnect, reconnect, and
shutdown. It observed these bounds:

- Canvas planning at most `channels * (2 * 960 + 2) + 1` commands;
- a 100,000-sample maximum waveform request window;
- a 100-row bus page; and
- fewer than 1,000 DOM nodes for the tested maximum-width workflow (the
  baseline maximum was 186).

The browser recorded only canonical loopback requests and proved that the
launch capability value did not appear in the location, Referer, browser
storage, DOM, console messages, or recorded request URLs. Checked-in baseline
evidence was separately scanned for user-home paths, device paths, local URLs,
and capability material. Safe downloads use the fixed B4 response and a
client-created object URL that is revoked; no server path or persistent file is
introduced.

## Frozen benchmark and measurements

- Method: production Playwright through the real bounded B4 API at viewport
  1280 by 900 and device-pixel ratio 1, Chromium `133.0.6943.16`, Playwright
  `1.50.1`, Node `22.14.0`, macOS `24.6.0` x86_64.
- Corpus: empty, schema-1, constant, sparse, dense, maximum 8/16/24, and
  representative/worst bus roles.
- Iterations: 15 initial load/paint observations, 3 warm-up interactions, and
  30 response-complete repeated pan/zoom observations.
- Timing: `performance.now()` around the UI action through bounded API
  completion, Canvas dataset update, and the next animation frame.
- Results: initial median `408.30000000074506 ms`, initial p95
  `446.5999999977648 ms`; repeated pan/zoom median
  `347.8999999985099 ms`, p95 `365.30000000074506 ms`.
- Reliable memory: unavailable; the record explicitly stores `null` and
  `memory_reliable: false` rather than treating Chromium's imprecise legacy
  heap value as evidence.

Frozen SHA-256 identities:

- baseline record:
  `1a692cfe7a3b0cec0c4b30b9f8e496d67a8ca50ec1b418f25ffda6deba4a5888`;
- fixture manifest:
  `9e2372ac1861b2b47bdaaf5cedab9a9b1faf671e459f640753ccf1124408e496`;
- fixture generator:
  `6b66f9a994084c650a385ba44e76bed8900be6a33338e2dace476c3774455440`;
- benchmark script:
  `3f15d8e6820b8ec7b2e937566db13aabd3871cee6cbbc158f9aa9171cab246f2`;
- production asset manifest:
  `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`;
- Python development and web locks, each:
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
- Node lock:
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`.

These values are measurements and identities only. This implementation record
proposes no performance threshold, approves no threshold, and cannot satisfy
the required independent verification, acceptance, orchestrator proposal, or
operator approval steps.

## Scope and residual risks

- No serial or hardware operation, firmware/C#/.NET change, persistent-device
  action, public serving, packaging, publication, unsupported-platform claim,
  B6 implementation, or Cycle 3 work occurred.
- No governing contract, accepted manifest, B4 API implementation, OpenAPI
  artifact, generated TypeScript API type, or B4 fingerprint changed.
- Shared-CI timing remains informational under the governing contract. Only an
  independently reproduced method and later operator-approved threshold record
  may create B5 acceptance ceilings.
- Memory is intentionally unavailable rather than weakly inferred.
- Live serial capture and native installed-browser hardware workflow remain B6
  work and are not claimed here.

## Implementation verdict and Git handoff

Focused implementation verdict: `pass` for immutable product candidate
`5e1a4cc87325e0c1f39df6b0f3c5757f900d1504`, tree
`9c2b786680c4d30941f06fd9fc5eaf4d448bf484`.

The root orchestrator should stage and commit only this review record as a
separate descendant, calculate its SHA-256, then submit the exact candidate—not
the descendant record commit—to the independent B5 verification lane. No
earlier verifier or acceptance result transfers to this new candidate.
