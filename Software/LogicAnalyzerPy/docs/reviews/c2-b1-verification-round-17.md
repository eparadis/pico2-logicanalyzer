# C2-B1 independent verification, round 17

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `47575f54230965a3f1772aac53064323aea3f119`
- Reviewed candidate tree: `6cbec99662323b5d530def6cb8dfc5cb092ee927`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `pass`

## Candidate and delta audit

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. Relative to candidate `41eeec1e81e61b030bda87168da2331e87468799`,
the only executable delta is the verifier-owned deterministic-clock correction
in `test_protocol_blackbox.py`; the other added paths are immutable round-15
and round-16 verifier records. The round-16 record digest independently matches
`e7852460fb92f7d4923175177c1a4c9afc5ebfadfe9cae08e2c9fa26aa9b9b74`.

No implementation, workflow, lock, governing contract, firmware, C#
application, or excluded Cycle 3 path changed.

## Finding disposition

### C2B1-CI-MAC-002 — closed

The test replaces host scheduling with an injected monotonic clock starting at
100 seconds. Recovery establishes one 20-millisecond deadline. The first
scripted transport read records its supplied timeout, advances the same clock by
exactly five milliseconds, and returns one byte. Production recomputes the
remaining time from the original deadline, so the second read receives a
positive timeout strictly smaller than the first and raises the scripted drain
timeout.

The assertions still require exactly two reads and require
`0 < second_timeout < first_timeout`. A defective per-byte implementation that
passed a fresh 20-millisecond timeout on every read would fail the strict-
decrease assertion. A defective unbounded drain would fail the scripted timeout
and cleanup behavior. The test therefore continues to prove one shared overall
budget without depending on real sleep, scheduler latency, or platform load.

Disposition: closed.

## Independent accumulated evidence

- Exact corrected timeout-budget test: 1 passed in 0.08 seconds, exit 0.
- Protocol plus C2-B1 foundation verifier suites: 65 passed in 0.57 seconds,
  exit 0.
- Ruff over `Software/LogicAnalyzerPy`: pass, exit 0.
- mypy: pass over 19 source files, exit 0.
- Full non-hardware pytest: 232 passed in 1.56 seconds, exit 0.
- Pinned Node v22.14.0 installed-Chromium production smoke: 1 passed in 1.5
  seconds, exit 0.

## Hosted CI qualification

This record verifies the deterministic fixture and local exact-candidate
accumulated gates. Fresh exact-candidate hosted macOS/Linux results remain
orchestration-owned accumulated-validation evidence and are not fabricated.

## Final finding state

C2B1-CI-MAC-002 is closed. No verifier finding remains open for the exact
candidate.
