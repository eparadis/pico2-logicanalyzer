# C2-B1 hosted CI diagnosis, verification round 16

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `41eeec1e81e61b030bda87168da2331e87468799`
- Reviewed candidate tree: `911edca03887d30f4077c43f5844616a2a539802`
- Hosted run: `32622367446`
- Ubuntu job: `97152376335`
- macOS job: `97152376427`
- Review date: 2026-08-22 America/Los_Angeles
- Verdict: `changes_required`

## Hosted evidence

The public jobs API confirms both jobs tested the exact candidate SHA. Ubuntu
passed all 25 gates, including non-hardware pytest and production browser smoke.
macOS passed clean environment creation, both locked core install steps,
`pip check`, Ruff, and mypy, then failed non-hardware pytest; all later macOS
steps were correctly skipped.

The public sanitized macOS check annotation identifies one failure:
`test_recovery_drain_uses_one_overall_timeout_budget_not_one_per_byte` expected
two transport read calls but observed one. The first recorded timeout was
approximately 0.019999 seconds. No secret, local URL, serial port, or unsanitized
home path appears in the annotation. The non-fatal GitHub Actions Node-runtime
deprecation warning is unrelated.

## Finding

### C2B1-CI-MAC-002 — Verifier recovery test uses wall-clock sleep inside a 20 ms budget

The verifier-owned `_SlowDrainTransport.read_exact` calls real
`sleep(0.005)` on its first read. The test invokes production recovery with a
20 ms total deadline and then requires exactly two reads. On the hosted macOS
runner, scheduling around the five-millisecond sleep exhausted the remaining
deadline, so production correctly stopped after one read. Ubuntu happened to
schedule a second read and passed.

The application contract is that all drain reads share one overall finite
budget, not that a loaded host must schedule exactly two calls in 20 ms. The
test therefore mixed a correct semantic assertion with a wall-clock scheduling
assumption and produced a platform/load-sensitive failure. This is a verifier
fixture defect; no implementation change is requested.

The verifier-only correction replaces real sleep with an injected monotonic
clock. The first scripted read advances that clock by exactly five milliseconds
and returns one byte; the second read receives the deterministically reduced
remaining budget and raises the scripted timeout. The existing assertions still
require exactly two calls and prove the second timeout is positive and smaller
than the first, but no host scheduling behavior affects the result.

Disposition: corrected in the verifier-owned test; open against the exact
candidate until the correction and this record are committed as a new immutable
candidate and the complete verification/hosted matrix repeats.

## Post-correction evidence

- Complete protocol verifier file: 58 passed in 0.14 seconds, exit 0.
- Ruff on the corrected verifier file: pass, exit 0.
- Full non-hardware pytest: 232 passed in 1.63 seconds, exit 0.

## Final state

C2B1-CI-MAC-002 remains open for candidate identity/evidence purposes. Owner is
`cycle2-verifier`; the next candidate requires no product/implementor change.
