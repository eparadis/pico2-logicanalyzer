# C2-B1 independent verification — round 18

- Verifier identity: `cycle2-verifier`
- Product candidate commit: `e266d88815b0dabdd1397cbfcf3e1187bf8dfc24`
- Product candidate tree: `9ec8c3ef73e47c940fd686656708cfaa212d9058`
- Verification date: 2026-08-23
- Verdict: **pass**
- Open findings: none

## Candidate and scope

The working HEAD used for execution contained only two later immutable platform-revision review records beyond the exact candidate. Its product tree and active contracts were otherwise identical to the candidate. The revision delta was limited to the authorized active contracts, workflow, README, and append-only progress entry. Firmware, C# applications, excluded Cycle 3 surfaces, and historical discovery/review/acceptance/evidence records were unchanged.

The current governing contracts consistently require macOS only. The workflow uses `macos-latest`, has no stale OS matrix or Linux-specific condition, and retains the canonical B1 gates, exact Python/Node versions, hash installs, and failure semantics. All fourteen stopping conditions and B1–B6 batch semantics remain present apart from the authorized platform narrowing. Historical Linux references remain identifiable as history rather than current claims.

## Independent evidence

Fresh Python 3.12 environments were created outside the repository for the core and web installs.

- Core lock install used `pip install --require-hashes -r requirements-dev.lock`; source install used `pip install --no-build-isolation --no-deps -e .`; `pip check` passed.
- Web lock install used `pip install --require-hashes -r requirements-web.lock`; source install used `pip install --no-build-isolation --no-deps -e '.[web]'`; `pip check` passed.
- Lock/artifact SHA-256 values were: `requirements-dev.lock` and `requirements-web.lock` `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`; `web/package-lock.json` `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`; `web/production-assets.json` `1d1b44794eed6f288f1140e67c1520d847fb3263718672cf743ff70b9da0ece9`.
- Ruff passed for the complete Python project; mypy passed for 19 source files.
- `pytest -m 'not hardware' -q` passed: 232 passed, 94 warnings, 3.65 seconds.
- The CLI help gate passed and exposed the expected command set, including `web`.
- A focused verifier run covering the one-overall-deadline recovery behavior and the C2-B1 foundation passed: 8 passed in 0.74 seconds. The test still proves one total timeout budget, not a renewed per-byte timeout.
- An independently constructed evidence-validator probe rejected 10/10 hostile samples, including a standalone 43-character capability value, Bearer and Basic authorization, capability cookies, token/API-key/password assignments, serial-device paths, and a loopback URL in nested and free-text locations. It accepted 4/4 benign security-prose samples and the baseline valid manifest.
- With pinned Node 22.14.0, `npm ci --no-audit --no-fund` installed 215 packages; lint and typecheck passed; Vitest passed 1 test; the production build completed with 26 modules; the production-asset checker passed.
- The installed Playwright Chromium production smoke passed: 1 passed in 2.1 seconds. This exercised local built assets, readiness, HttpOnly/SameSite=Strict capability cookie handling, protected shutdown, and console token non-disclosure without a Node development server or serial dependency.
- The complete and focused suites cover loopback-only binding, canonical Host, exact Origin/capability requirements, malformed/missing/duplicate/expired credentials, WebSocket upgrade behavior, absent CORS/OPTIONS surface, request bounds, ownership, deterministic shutdown/cookie expiry, schema recursive strictness, missing-web-extra behavior, and Cycle 1 regressions.
- Diff and path audits found no prohibited firmware, C#, or Cycle 3 change and no corruption of immutable historical records.

One optional defense-in-depth command ran a single production-process test under an artificial minimal `PATH`. It emitted no result before external interruption after 945.4 seconds. It is not credited as evidence and does not replace or qualify any required gate above; the required bounded full suite, focused suite, and real-browser production smoke all completed successfully.

## Disposition and handoff

No product or contract finding is open. C2-B1 satisfies the current macOS-only governing contracts on this exact product candidate. Accumulated validation should commit this immutable record, remove the browser-generated untracked `web/test-results/` artifact without committing it, run the exact-candidate hosted macOS workflow, and then submit the candidate for acceptance.
