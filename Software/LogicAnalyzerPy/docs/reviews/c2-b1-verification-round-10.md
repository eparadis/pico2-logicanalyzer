# C2-B1 independent verification, round 10

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `629d4f3a96784eda36561db13ea95f4e5f2349ba`
- Reviewed candidate tree: `ef11c1eaeccdb808f14008780853a185a1fbcc65`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `changes_required`

## Candidate and semantic audit

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. Relative to candidate `152eb26c9f7ff8ed0abdfae6a26f12e85cc5ddbf`,
the only product delta is the Cycle 2 workflow; the other added path is the
immutable round-9 verifier record.

The wrapper still invokes exactly `.venv/bin/python -m pytest -m "not hardware"`
with no added exclusion, deselection, skip, retry, or changed pytest option. It
captures the original status immediately, disables fail-fast shell behavior
only around pytest, restores it afterward, and exits the captured status. There
is no `continue-on-error`; downstream steps remain blocked on failure. The
temporary log is deleted by an EXIT trap.

Output selection is finite: the report takes only the final 12,000 input bytes,
filters to ASCII horizontal-tab/newline/carriage-return/printable characters,
and GitHub-escapes percent, carriage return, and newline for its annotation.
The annotation remains bounded by the finite source report even after escaping.

## Finding

### C2B1-V010 — Failure annotation can disclose raw capability tokens and Linux serial paths

The sanitizer redacts capability values only when rendered as
`pico_la_capability=<value>`. Pytest assertion rewriting can render the
server-generated capability as an unlabeled expected/actual Python string—for
example if a token non-disclosure assertion fails—so the unpredictable launch
value can reach the printed report and annotation without the cookie-name
prefix. The token's URL-safe random representation is not otherwise redacted.

The serial-port rule covers `/dev/tty...` and `/dev/cu....` but not Linux's
normal `/dev/serial/...` paths. The matrix explicitly includes Linux, and the
Cycle 2 evidence boundary prohibits serial ports rather than only those two
device-name prefixes.

An independent literal passed through the exact four `sed` expressions retained
both an unlabeled URL-safe token-like value and `/dev/serial/by-id/device`
unchanged. URL and `/Users`/`/home` path rules, cookie-labelled capability,
printable filtering, finite tailing, annotation escaping, temporary cleanup,
and exit-status preservation are otherwise structurally sound.

Requested resolution: extend the bounded sanitizer and independent workflow
tests to redact standalone capability-token representations that can be emitted
by the C2-B1 tests and all supported serial-device path forms, including
`/dev/serial/...`, without removing the exact pytest gate or altering its exit
status. Use fixed hostile diagnostic literals to prove the redaction before
printing; do not expose a real launch token in evidence.

Disposition: open; workflow/product owner correction required.

## Independent runtime evidence

- Verifier suite: 7 passed, 0 failed in 0.44 seconds, exit 0.
- Pinned Node v22.14.0 installed-Chromium production smoke: 1 passed, 0 failed
  in 1.2 seconds, exit 0.
- Literal sanitizer probe: exit 0 and reproduced both unredacted prohibited
  classes described in C2B1-V010.

## Final finding state

C2B1-V010 remains open. No runtime product failure was observed, but the exact
candidate does not yet satisfy the committed-evidence secret-redaction boundary
on a failing hosted test.
