# C2-B1 independent verification, round 9

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `152eb26c9f7ff8ed0abdfae6a26f12e85cc5ddbf`
- Reviewed candidate tree: `65fb4d288779b0e95ada76f2e9f265c96319506a`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `pass`

## Candidate and finding audit

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. Relative to candidate `cf34845788a64b958919dfacbe9bc77d303fe02b`,
the only executable delta is the verifier-owned lifecycle test. The other added
paths are immutable round-8 verification and macOS CI diagnosis records. No
product, workflow, lock, governing contract, firmware, C# application, or
excluded Cycle 3 path changed.

### C2B1-CI-MAC-001 — closed

The correction consumes and closes the initial HTML response before sending
shutdown, retaining only its `Set-Cookie` header. It consumes and closes the
shutdown response after asserting status 204. This removes open keep-alive
connections from aiohttp runner cleanup.

The process wait changes from one to five seconds. Five seconds remains a finite
and strict verification deadline; timeout still raises the same failed
assertion, and the `finally` block still terminates then kills the subprocess
under separate two-second bounds if necessary. The startup loop remains finite
and the server still must become reachable.

No security or lifecycle expectation was removed: the test still obtains the
server-generated capability cookie, supplies the exact canonical Origin and
cookie, requires shutdown 204, requires bounded process exit, and requires exit
status 0. The complete seven-check file retains evidence-validator, secret,
lock-closure, nested-package-data, recursive-schema, and OS-assigned-port
coverage.

Disposition: closed.

## Independent command evidence

- Ruff on the complete verifier-owned test: pass — all checks passed, exit 0.
- `Software/LogicAnalyzerPy/.venv/bin/python -m pytest
  Software/LogicAnalyzerPy/tests/verification/test_c2_b1_foundation_blackbox.py
  -q`: pass — 7 passed, 0 failed, 0.73 seconds, exit 0.
- `PATH=/private/tmp/node-v22.14.0-darwin-x64/bin:/usr/local/bin:/usr/bin:/bin
  npm run test:browser`: pass — installed Chromium production smoke 1 passed,
  0 failed, 1.4 seconds, exit 0.

## Hosted CI qualification

This record verifies the corrected test semantics and local exact-candidate
behavior. A fresh hosted macOS/Linux run remains orchestration-owned
accumulated-validation evidence and is not fabricated here.

## Final finding state

C2B1-CI-MAC-001 is closed. No verifier finding is open for the exact candidate.
