# C3-B2 independent verification — round 4

Identity: `c3-b2-private-host-verifier-replacement-4`.

Verdict: `pass`.

## Immutable subject

This hostile verification is bound only to governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`; corrected B1 checkpoint
`d4f984d`; approved round-4 limits proposal/decision `b680aa5` / `afd4585`;
and exact candidate `959edf77945176b26c7cec86bcdd806d7e5769ea`, tree
`bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`. Verification completed at
`2026-08-31T14:45:43Z` from descendant `c9f2db1` with candidate product bytes
unchanged.

The candidate SHA-256 identities were independently confirmed as:

- host: `8a555fb08a88badf59bdabe2f558bcd9f7918ccebd52d3c2539013bff733c990`;
- implementation tests:
  `77116dab6279a2e6bb579f14d72a2be59a02725cba2ef1f888b69492ae6954b5`;
- implementation review:
  `c0d5b2573a21c80a9d8e89c5c81e22412642ecd42eda7acf0d7a0fa459d88dbf`.

No verdict transfers from predecessor `d8e14bb`, verifier `5178a63`,
accumulation `bba6662`, or failed acceptance. Finding `C3B2-A001` remains
preserved at `6825e88`; this record verifies its correction without modifying
the finding or implementation.

## Independent audit

The corrected parent control flow launches without writing, places the request
descriptor in nonblocking mode, and registers request writes together with
response, stdout, and stderr reads in one selector lifecycle. Cancellation and
the five-second inclusive deadline are checked while delivery is incomplete.
Partial writes retain the unwritten suffix; completion unregisters and closes
the request descriptor. Broken/zero writes, early close/exit/signal, malformed
or excessive output, cancellation, and deadline paths converge on stable
failure translation and exact-child terminate/kill, descriptor close, and
reap. Result parsing occurs only after every registered stream reaches its
terminal state, preventing an early response from becoming partial success.

The new independent suite uses real fresh subprocesses and assertions outside
implementation counters. It proves successful delivery well beyond pipe
atomic-write capacity to a deliberately slow reader; a complete valid response
sent before a never-read request cannot succeed and instead times out; partial
delivery cancellation wins while the child concurrently writes stdout and
stderr; close, clean exit, and fatal signal during delivery map stably to
`process-exit`; and repeated empty selector readiness remains deadline bounded.
Every failure assertion proves the exact child is reaped and both captured
pipes are closed, then performs a real fresh decoder success. The tests are
bounded and left no owned child.

Static inspection plus the complete current and prior B2 suites retained full
R6-R12/R22 coverage: host-owned closed decoder ID/digest/import selection;
prelaunch mapping/options/sample validation; frozen compatibility lifecycle;
versioned framed IPC and hostile frame/output/diagnostic/resource rejection;
request/result projection binding and declaration/record graph validation from
`C3B2-V001`/`C3B2-V002`; atomic failure and recovery; all 18 exact hard product
limits; and the separate 11 evidence-only macOS regression gates. No public
decode API or CLI was added.

## Validation

- New verifier suite: `6 passed in 1.81s`.
- Current implementation plus all four B2 verifier suites: `313 passed in
  47.37s`.
- Ruff over the owned verifier and current implementation test: passed.
- `mypy --strict Software/LogicAnalyzerPy/src/pico_logic_analyzer/_decode`:
  success, 9 source files.
- `git diff --check`: passed.

Owned verifier-test SHA-256 before this record:
`a77b4e6081da5dead4e4f9d3e7b3761a28efa765c24fd9a1c88016b114408607`.
Only this test and review record were created; neither was staged or committed.

The sandbox denied the final bounded process-list command. All spawned test
children were nevertheless asserted reaped in-suite; root must perform the
already-authorized repository-wide process confirmation. No external/reference
decoder, C#/.NET, prohibited runtime or dependency, hardware, USB/serial, live
capture, publication, browser product work, B3+, or Cycle 4 action occurred.

`pass`
