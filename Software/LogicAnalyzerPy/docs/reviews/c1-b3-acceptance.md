# C1-B3 independent acceptance

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed commit: `3b7f1af3c80f7797514b866c39243a610f9d6f4d`
- Reviewed tree: `a80bde46a66537a5e3048af46233ebc5fad4283c`
- UTC timestamp: `2026-08-17T00:26:03Z`
- Verdict: **changes_required**

## Candidate and scope

`HEAD` and `git rev-parse <commit>^{tree}` matched the exact candidate. The tracked worktree was clean before this acceptance record. The delta is confined to the authorized C1-B3 pySerial transport/device service, `devices`/explicit-port `info` CLI integration, pySerial lock metadata, procedure/docs, and focused fake tests. No changed path exists under `Firmware/` or `Software/LogicAnalyzer/`; capture/export, automatic selection, TCP, persistent device management, firmware mutation, and later-cycle implementation remain absent.

## Findings and dispositions

### 1. Required physical identity/reopen acceptance is unrun

- **Status: open — changes required.** C1-B3 requires real V2 identity/capabilities and two identity operations separated by explicit close/reopen. No physical port was opened, which is correct under the authority and safety gate.
- Evidence: `docs/operator-input-template.md` still marks the input-front-end/level-shifter revision, target voltage, VRef, permitted input range, exact common-ground point, and protection-board D0-D7/header mapping as pending. It also leaves reported deployed identity pending C1-B3. These unknowns explicitly block hardware I/O; no fake test can replace the required physical evidence.
- Required disposition: obtain and record the operator's complete electrical/mapping inputs, then run the documented identity-only procedure on the explicit operator port. Record sanitized exact V2 identity/capabilities and demonstrate two successful reads separated by close/reopen. A mismatch must pause the hardware path for direction rather than rewrite the baseline.

### 2. Non-hardware C1-B3 implementation surface

- **Status: pass.** `SerialTransport` creates a pySerial object with `port=None`, sets 115200/8N1/no flow control/finite read-write timeouts, asserts DTR/RTS, assigns only the caller-supplied port, opens, stabilizes for 100 ms, and performs bounded 200 ms/1024-byte drain. It uses one byte buffer rather than text/binary readers.
- **Status: pass.** Fake serial tests cover exact configure/open/stabilize/drain order, one-byte identity fragments, literal identity frame, malformed/missing response cleanup, permission/unplug errors, two fake close/reopen identities, VID `1209`/PID `3020` filtering with Linux/macOS-like absent metadata, deterministic listing, no auto-selection, stdout/stderr/JSON/exit-code behavior, and rejection of unimplemented capture without opening a port.
- **Status: pass.** The explicit-port service always closes in `finally`; CLI maps connection, timeout, and malformed-identity errors to exit 3 and retains exit 2 for invalid timeout/usage. `ProtocolError` is caught before generic `ValueError`, preserving the settled malformed-identity connection/protocol status.
- **Status: pass.** `pyserial==3.5` is runtime-pinned and hash-locked. The package lock/editable install and `pip check` pass in Python 3.12.13.

## Independent commands and outcomes

Run from `Software/LogicAnalyzerPy` with Python 3.12.13:

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pip check` | pass — no broken requirements |
| `.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock` | pass |
| `.venv/bin/python -m pip install --no-build-isolation --no-deps -e .` | pass |
| `.venv/bin/python -m pytest tests/verification/test_c1_b3_serial_blackbox.py -q` | pass — 15 passed |
| `.venv/bin/python -m pytest tests/verification -q` | pass — 123 passed; one expected duplicate-ZIP fixture-construction warning from C1-B2 coverage |
| `.venv/bin/python -m ruff check .` | pass |
| `.venv/bin/python -m mypy src` | pass — no issues in 16 source files |
| `.venv/bin/python -m pytest -m "not hardware" -q` | pass — 147 passed; same expected warning only |
| `.venv/bin/python -m pico_logic_analyzer --help` | pass |
| `git diff --check <candidate>^ <candidate>` | pass |
| changed-path check under `Firmware/` and `Software/LogicAnalyzer/` | pass — no paths |

## Limitations and deferrals

This review does not claim real USB CDC behavior, permission behavior on the operator's host, board identity/capabilities, or reopen behavior against a physical analyzer. No serial/hardware/network operation was performed. The exact deployed V2 identity and serial timing remain C1-B3 physical evidence; capture, CSV/NPZ output, and physical recovery remain C1-B4/C1-B5 work.

## New code findings

None in the non-hardware surface. The sole blocker is the mandatory, safety-gated physical C1-B3 identity proof.
