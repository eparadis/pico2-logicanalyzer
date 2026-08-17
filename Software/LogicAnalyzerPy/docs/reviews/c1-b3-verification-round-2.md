# C1-B3 serial line-boundary verification — round 2

## Interim result — 2026-08-17T00:24:00Z

Verdict: **changes_required** on base candidate
`3b7f1af3c80f7797514b866c39243a610f9d6f4d`.

The physical observation that the identity-only wire fields end in CRLF is
**orchestrator-reported provenance**, not independently reproduced hardware
evidence. No hardware or network access was used here. The verifier therefore
uses literal fake serial bytes at the `SerialTransport.read_line` boundary:
`IDENTITY\n` and `IDENTITY\r\n` must both yield exactly `IDENTITY`; lone CR,
CR followed by a non-LF byte, and leading/trailing space or tab must fail as
line-format errors.

New verifier-owned additions in
`tests/verification/test_c1_b3_serial_blackbox.py` establish those cases
without production encoders. Command run from `Software/LogicAnalyzerPy`:

`rtk .venv/bin/python -m ruff check tests/verification/test_c1_b3_serial_blackbox.py && rtk .venv/bin/python -m pytest tests/verification/test_c1_b3_serial_blackbox.py -q`

Ruff passed; pytest reported **4 failed, 18 passed**. The LF and CRLF
acceptance cases pass. The required failures are:

- `IDENTITY\r` raises `TransportTimeout` rather than `SerialTransportError`.
- ` IDENTITY\n` is accepted.
- `IDENTITY \n` is accepted.
- `IDENTITY\t\n` is accepted.

`IDENTITY\rX\n` already rejects. The implementation owner must make invalid
line framing and boundary whitespace deterministic `SerialTransportError`
failures while retaining exact LF/CRLF normalization. This verifier will be
rerun after that production change; no production files were edited here.

## Final result — 2026-08-17T03:01:34Z

Verdict: **pass for the C1-B3 round-two non-hardware evidence surface**.
The interim description above is retained as history, with the following
layering correction requested during review: lone CR is a bounded
`TransportTimeout` or `SerialTransportError` rejection; the transport line
boundary owns exact LF/CRLF normalization and embedded-CR rejection; identity
grammar owns acceptance of fields. The identity service test therefore accepts
either `ProtocolError` or connection failure for smuggled leading/trailing/tab
whitespace. The settled implementation rejects all such inputs and closes the
fake port.

The focused C1-B3 verifier now has **22 passed** cases. It independently uses
literal bytes and covers both `IDENTITY\n` and `IDENTITY\r\n` yielding exactly
`IDENTITY`, lone CR, embedded CR, and whitespace-smuggling failure paths,
alongside the prior serial/open/identity/discovery/CLI cases. CRLF device
behavior remains orchestrator-reported provenance only; this agent performed
no hardware or network access.

Commands from `Software/LogicAnalyzerPy` and outcomes:

- `rtk .venv/bin/python -m ruff check tests/verification/test_c1_b3_serial_blackbox.py` — pass.
- `rtk .venv/bin/python -m pytest tests/verification/test_c1_b3_serial_blackbox.py -q` — 22 passed.
- `rtk .venv/bin/python -m pytest tests/verification -q` — 130 passed, one existing duplicate-ZIP-fixture warning.
- `rtk .venv/bin/python -m pytest -m 'not hardware' -q` — 159 passed, the same expected warning.
- `rtk .venv/bin/python -m ruff check .`, `rtk .venv/bin/python -m mypy src`, `rtk .venv/bin/python -m pico_logic_analyzer --help`, `rtk .venv/bin/python -m pip check`, and `rtk git diff --check` — pass. Pip emitted only its local cache-permission warning and found no broken requirements.

Worktree qualification: base `HEAD`
`3b7f1af3c80f7797514b866c39243a610f9d6f4d`, tree
`a80bde46a66537a5e3048af46233ebc5fad4283c`; deterministic binary tracked
diff digest for `HEAD -- Software/LogicAnalyzerPy`:
`575f2d1021fffeab2f22aa67671dab8fd894311428d539141f7df0e53b74aa7b`.
The uncommitted production serial input was separately SHA-256 qualified as
`d32f60a7dae3a073ec48df99b727bb5d75d51b9db242be96cbeefc3b368b2634`;
the final verifier test before this documentation-only update was
`f60f72981f82efd0a6499b52caf67f92016d23ffc0a8f7cde37d72517412ac79`.
