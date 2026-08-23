# C2-B1 independent verification, round 8

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `cf34845788a64b958919dfacbe9bc77d303fe02b`
- Reviewed candidate tree: `6b64606ad36289e052c3482a0216f0511b5e7e9c`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `pass`

## Candidate and workflow delta

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. Relative to candidate `0983abfea92d087227b204cc0659dbd75da2fa4d`,
the only product delta is the Cycle 2 workflow; the other added path is the
immutable round-7 verifier record.

The workflow adds two mutually exclusive browser-provisioning steps after the
locked Node install and production asset build/drift gate:

- Linux runs the local Playwright CLI's `install --with-deps chromium`, which
  provisions the Chromium browser plus Linux CI system dependencies.
- macOS runs the local Playwright CLI's `install chromium`, avoiding the
  Linux-only dependency installer while provisioning the same browser family.

Because `npm ci` has already installed the lock-pinned `@playwright/test`
version, `npx playwright` resolves the project-local pinned CLI and its matching
browser revision. Browser download/system provisioning is CI development/test
tooling, not a Python application dependency or production runtime action.

The macOS/Linux matrix, Python 3.12, Node 22.14.0, hash-required Python locks,
no-build-isolation/no-deps installs, both `pip check` steps, Ruff, mypy,
non-hardware pytest, CLI help, npm lock install, lint, typecheck, Vitest,
production build, asset drift, and actual browser smoke all remain present and
unconditional for their matrix job. No gate was omitted or weakened.

The production build is still committed and checked before browser
provisioning. The shipped Python server still serves local assets without Node,
CDN, or runtime network access; the new CI provisioning commands are not
invoked by `pico-la web` or included as product behavior.

## Independent runtime evidence

- `Software/LogicAnalyzerPy/.venv/bin/python -m pytest
  Software/LogicAnalyzerPy/tests/verification/test_c2_b1_foundation_blackbox.py
  -q`: pass — 7 passed, 0 failed, 0.61 seconds, exit 0.
- `PATH=/private/tmp/node-v22.14.0-darwin-x64/bin:/usr/local/bin:/usr/bin:/bin
  npm run test:browser`: pass — installed Chromium production smoke 1 passed,
  0 failed, 1.5 seconds, exit 0.

The browser observation covers production startup, local built shell,
capability cookie, readiness, protected exact-origin shutdown, process cleanup,
and console token non-disclosure. The verifier suite independently covers the
seven C2-B1 schema, lock, package, lifecycle, and port boundaries.

## Hosted CI qualification

This record verifies complete/non-weakened cross-platform workflow semantics
and local exact-candidate behavior. Hosted macOS/Linux run identities/results
remain orchestration-owned accumulated-validation evidence and are not
fabricated.

## Final finding state

No verifier finding is open for the exact candidate.
