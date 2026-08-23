# C2-B1 hosted macOS pytest failure diagnosis

- Lane / identity: verifier / `cycle2-verifier`
- Diagnosed candidate commit: `cf34845788a64b958919dfacbe9bc77d303fe02b`
- Diagnosed candidate tree: `6b64606ad36289e052c3482a0216f0511b5e7e9c`
- Hosted run/job: `32617267020` / macOS `97139884132`
- Diagnosis date: 2026-08-22 America/Los_Angeles
- Owner: `cycle2-verifier`
- Verdict: `changes_required`

## Evidence boundary

Ubuntu job `97139884069` passed all 25 gates. The macOS job passed clean Python
environment creation, hash-locked install, no-deps source install, `pip check`,
Ruff, and mypy, then exited 1 during `pytest -m "not hardware"`. Detailed hosted
logs were unavailable (403), so this diagnosis did not invent a hidden test
name. The candidate's only product delta from the prior verified candidate is
post-pytest Playwright browser provisioning, which cannot affect the earlier
pytest step.

## Finding

### C2B1-CI-MAC-001 — Verifier-owned subprocess test does not close HTTP responses and uses a brittle cleanup deadline

The verifier-owned `test_orderly_shutdown_stops_production_process` retained
the initial `urllib` response while issuing shutdown and did not consume or
close either HTTP response. It then required the aiohttp production process to
complete runner cleanup within one second. On a hosted macOS runner, an open
keep-alive response can delay connection/runner cleanup; a one-second scheduling
deadline is not an application contract and makes the verifier test sensitive
to runner load.

A requested 20-iteration diagnostic command returned no completed iteration
output and was externally terminated after 311.3 seconds. That observation is
consistent with the test/runner command boundary stalling, but is not counted as
20 failed iterations. It prompted bounded source-level ownership inspection.

The verifier-only correction now:

- consumes and closes the initial HTML response before shutdown;
- stores only the `Set-Cookie` header needed for the security assertion;
- consumes and closes the shutdown response; and
- allows a still-bounded five seconds for orderly runner/process cleanup.

No expected status, cookie, Origin, process-exit, lock/package/schema, port, or
security assertion changed. No product file changed.

Disposition: corrected in the verifier-owned test; open against the exact
candidate until the correction is committed as a new immutable candidate and
hosted macOS pytest is rerun.

## Post-correction evidence

- Focused verifier suite: 7 passed, 0 failed in 0.68 seconds, exit 0.
- Full macOS non-hardware suite: 224 passed, 0 failed in 1.26 seconds, exit 0.
- Ruff on the corrected verifier file: all checks passed, exit 0.

## Required next action

Commit only the verifier test correction and this immutable diagnosis, create a
new candidate, and repeat independent verification plus the full hosted
macOS/Linux accumulated gate. The implementation/product lane does not own this
finding unless a subsequent attributable failure identifies a product defect.
