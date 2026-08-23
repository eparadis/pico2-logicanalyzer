# C2-B1 independent verification, round 11

- Lane / identity: verifier / `cycle2-verifier`
- Reviewed candidate commit: `8fd4d737be283d68a7cbe682225eb781fb58ef5a`
- Reviewed candidate tree: `fa98722af2c5992a40d54c0adc032e4e26f7ecaf`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `pass`

## Candidate and workflow delta

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. Relative to candidate `629d4f3a96784eda36561db13ea95f4e5f2349ba`,
the only product delta is the Cycle 2 workflow sanitizer; the other added path
is the immutable round-10 verifier record.

The pytest selection remains exactly `.venv/bin/python -m pytest -m "not
hardware"`. The wrapper captures its status immediately, restores shell
fail-fast behavior, and exits that exact status. There is no retry, exclusion,
skip, `continue-on-error`, or alternative success path. A sanitizer self-test
failure exits 2 before pytest and cannot turn a pytest failure into success.

## Finding disposition

### C2B1-V010 — closed

The sanitizer now covers `/dev/tty...`, `/dev/cu....`, and `/dev/serial/...`
paths and standalone 43-character URL-safe capability-token representations in
addition to cookie-labelled tokens, local URLs, and `/Users`/`/home` paths. The
43-character rule uses non-token boundaries, so it does not redact a substring
from a longer digest or identifier.

An independent probe containing a fixed hostile token, `/dev/ttyUSB0`,
`/dev/cu.usbmodem`, `/dev/serial/by-id/x`, a loopback URL, a `/Users` path, and
percent text produced only the expected token/port/URL/path markers plus benign
text. No hostile literal survived.

The checked-in self-test uses a fixed non-secret token and Linux serial path,
requires both redaction markers in order, and fails if either original survives.
It creates bounded temporary files and the EXIT trap removes both on success or
failure.

The report remains limited to the final 12,000 input bytes before sanitizing and
is filtered to tabs, newlines, carriage returns, and printable ASCII. Annotation
encoding independently transformed percent, carriage return, and newline to
`%25`, `%0D`, and `%0A`, preventing injected workflow-command line breaks. The
finite input also keeps escaped output finite.

Disposition: closed.

## Independent runtime evidence

- Hostile sanitizer probe: pass — standalone token; tty, cu, and serial paths;
  loopback URL; and machine path all redacted, exit 0.
- Annotation escaping probe: pass — percent/CR/LF encoded, exit 0.
- Verifier suite: 7 passed, 0 failed in 0.43 seconds, exit 0.
- Pinned Node v22.14.0 installed-Chromium production smoke: 1 passed, 0 failed
  in 1.2 seconds, exit 0.

## Hosted CI qualification

This record verifies sanitizer behavior, exact status semantics, and local
exact-candidate runtime gates. Fresh hosted macOS/Linux results remain
orchestration-owned accumulated-validation evidence and are not fabricated.

## Final finding state

C2B1-V010 is closed. No verifier finding remains open for the exact candidate.
