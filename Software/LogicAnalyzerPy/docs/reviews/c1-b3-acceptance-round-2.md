# C1-B3 independent acceptance — round 2

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed commit: `c71db28f17bd2ba8b68542b8514c383610bb7635`
- Reviewed tree: `bc724c1f071062c4cfd397aac016c3af3083415d`
- UTC timestamp: `2026-08-17T03:11:51Z`
- Verdict: **pass**

## Candidate and evidence scope

`HEAD` and `git rev-parse <commit>^{tree}` matched the exact candidate. The code delta from the first C1-B3 candidate is limited to the serial line-boundary correction, focused tests, procedure/operator updates, and review records; `git diff --check` passes and there are no firmware or C# changes. I also reviewed the current evidence-only operator record (SHA-256 `d82b9e9b192ba976eb5ad9ee7ec84025cb02138a7fdfb653aceea186ca607c51`) and sanitized observation (SHA-256 `2bdba98556f6dbe20150e85b433b19fe839b0aaa6535611ff71467b291db9148`). Those post-candidate files are explicitly treated as physical evidence, not as files included in the tested tree.

## Finding dispositions

### 1. Prior physical-identity blocker

- **Status: resolved.** The operator record now confirms the installed integrated checked-in LogicAnalyzerV2 protection design and its permitted input range, a 3.3 V 1 kHz source, 3.3 V VRef, common ground at the labeled GND point, and direct circuit inspection that labeled input 1 reaches Pico 2 GPIO2/logical D0. This clears the safety/mapping prerequisite for identity-only I/O.
- The sanitized C1-B3 observation records two identity requests separated by close/reopen, request bytes `55aa00aa55`, observed CRLF line endings, exit status 0, equal identities, and no persistent device changes. The serial path is sanitized as `<PORT_SUPPLIED>`.
- Both observations report `LOGIC_ANALYZER_PICO_2_V6_0`, normal frequency 200000000 Hz, blast frequency 400000000 Hz, buffer 393216 bytes, and 24 channels. These are consistent with the checked-in `BOARD_PICO_2`/turbo source definitions: board name `PICO_2`, V6_0, `MAX_FREQ` 200000000, `MAX_BLAST_FREQ` 400000000, `CAPTURE_BUFFER_SIZE` `128 * 3 * 1024`, and `MAX_CHANNELS` 24.

### 2. CRLF identity compatibility correction

- **Status: resolved.** The original physical diagnostic found CRLF fields. `SerialTransport.read_line` now accepts exactly LF or CRLF, strips only the final CR before LF, and rejects lone/embedded CR plus leading/trailing/tab whitespace. This preserves the one-byte buffer and does not broaden the identity grammar.
- Independent literal fake-wire tests cover LF and CRLF acceptance, lone/embedded CR rejection, whitespace-smuggling rejection, fragmented identity, exact request bytes, cleanup, explicit-port-only behavior, and two fake close/reopen identities.

### 3. Non-hardware and scope gate

- **Status: resolved.** The pySerial configuration/lifecycle, discovery filtering, stdout/stderr/JSON/exit-code contracts, and close-on-service paths remain covered. No auto-selection, capture/export, TCP, persistent device management, firmware mutation, or later-cycle feature is introduced. The existing C# and firmware paths remain unchanged.

## Independent commands and outcomes

Run from `Software/LogicAnalyzerPy` using Python 3.12.13; no serial device or network was accessed by this reviewer:

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pip check` | pass — no broken requirements |
| `.venv/bin/python -m pytest tests/verification/test_c1_b3_serial_blackbox.py -q` | pass — 22 passed |
| `.venv/bin/python -m pytest tests/verification -q` | pass — 130 passed; one expected C1-B2 duplicate-ZIP fixture-construction warning |
| `.venv/bin/python -m ruff check .` | pass |
| `.venv/bin/python -m mypy src` | pass — no issues in 16 source files |
| `.venv/bin/python -m pytest -m "not hardware" -q` | pass — 159 passed; same expected warning only |
| `.venv/bin/python -m pico_logic_analyzer --help` | pass |
| `git diff --check <candidate>^ <candidate>` | pass |
| changed-path check under `Firmware/` and `Software/LogicAnalyzer/` | pass — no paths |

## Limitations and deferrals

This acceptance proves only C1-B3's identity/reopen gate. It does not claim capture success, edge polarity, CSV/NPZ output, physical timeout cancellation, or a second physical capture; those remain C1-B4/C1-B5 acceptance work. The checked-in source establishes consistency, while the sanitized physical observation is the evidence for the deployed board; no raw port path or unsanitized trace is stored.

## New findings

None.
