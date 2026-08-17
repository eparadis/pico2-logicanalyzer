# C1-B3 independent verification matrix

Status: final non-hardware verifier pass recorded below. No serial device,
network, or hardware access was used.

| Surface | Independent fake input | Required result |
|---|---|---|
| Explicit port | `info --port /dev/fake` | Opens only that exact path; no discovery choice or fallback. |
| Serial settings | Recording fake serial constructor | 115200, 8 data bits, no parity, one stop bit, no software/hardware flow control, finite read/write timeouts, DTR and RTS asserted. |
| Ordering | Recording fake serial | Configure before open; bounded stabilize/drain after open; identity request/read; close; reopen repeats configuration/identity. |
| Identity | Five-field V6 response, including one-byte fragments | Sends literal `55 aa 00 aa 55`; parses source-derived identity/capabilities. |
| Cleanup failures | Permission, disconnect, read timeout, malformed/missing identity | Exit 3, actionable stderr, no stdout contamination, port cleanup. |
| Discovery | Linux/macOS-like port records plus missing VID/PID/serial/location fields | Lists only VID `0x1209` / PID `0x3020` candidates, tolerates absent optional metadata, never opens a listed port. |
| Devices CLI | text and `--json` | Machine data on stdout only; valid deterministic JSON with no diagnostics. |
| Info CLI | text and `--json` with explicit port | Success 0; valid identity/capabilities, JSON stdout only. |
| No implicit selection | zero/one/multiple discovered candidates and missing `--port` | No auto-open; usage/configuration failure is exit 2. |
| Reopen | Two valid scripted identities | Explicit close/reopen separates two identity operations. |
| Scope | `capture`, bootloader/network/persistent paths | B3 `devices`/`info` introduce none; no persistent device mutation. |

## Provenance and deferrals

The VID/PID comes from C# `DeviceDetector.cs` (`1209:3020`). C#
`LogicAnalyzerDriver.InitSerialPort` supplies 115200, DTR/RTS, LF, and identity
ordering reference. The Cycle 1 contracts supersede C#'s unsafe paired readers:
the Python implementation must retain its single byte-oriented buffer.

Physical identity, exact USB CDC line-setting behavior, real-port permissions,
and actual board identity are C1-B3 hardware evidence; they cannot be claimed
by these fake tests.

## Final independent verifier result — 2026-08-17T00:22:54Z

Verdict: **pass for the C1-B3 non-hardware evidence surface**. The physical
serial/board confirmation remains explicitly deferred: this verifier used only
recording fakes and did not access hardware or the network.

The independent black-box fixture
`tests/verification/test_c1_b3_serial_blackbox.py` has 14 passing cases. Its
expectations are literal/source-derived rather than using production encoders:
the literal identity request is `55 aa 00 aa 55`, response input is fragmented
one byte at a time, and discovery accepts exactly VID `0x1209`, PID `0x3020`.
It covers exact serial configuration (115200/8N1, all flow control disabled,
finite read/write timeouts), DTR/RTS and configure/open/stabilize/drain order,
close/reopen, cleanup on open/read/malformed failures, explicit-port-only
identity, deterministic candidate sorting with absent metadata, and text/JSON
stdout/stderr/exit contracts. It also proves that `info` cannot omit `--port`
and that a fully formed `capture` command is rejected without opening a port.

Commands and outcomes, run from `Software/LogicAnalyzerPy`:

- `rtk .venv/bin/python -m ruff check tests/verification/test_c1_b3_serial_blackbox.py` — pass.
- `rtk .venv/bin/python -m pytest tests/verification/test_c1_b3_serial_blackbox.py -q` — 14 passed.
- `rtk .venv/bin/python -m pytest tests/verification -q` — 122 passed, one expected duplicate-ZIP fixture warning.
- `rtk .venv/bin/python -m pytest -m 'not hardware' -q` — 145 passed, the same expected warning.
- `rtk .venv/bin/python -m ruff check .` and `rtk .venv/bin/python -m mypy src` — pass.
- `rtk .venv/bin/python -m pico_logic_analyzer --help`, `rtk .venv/bin/python -m pip check`, and `rtk git diff --check` — pass; pip reported no broken requirements (with only a local cache-permission warning).

Worktree qualification: base `HEAD`
`f27a9f43b4a62946b43f9ae57b370210ebd1667d`, tree
`14cd2573308d1dfe192ceaa5f03707f53a4932fe`; the deterministic binary tracked
diff digest for `HEAD -- Software/LogicAnalyzerPy` was
`bf09c782735e5dd127b038ac8744c4d0b105f030ae8bddb772d2138f10443002`.
Untracked B3 production inputs were separately qualified as
`device.py` `9e90994bd86d14bebf890b1914a051c7a85577752c626cb1d78b231702b46d74`
and `serial.py` `f67cae5f60afa2006d262af913c342f039698349e9059bda5d8c9e7741765a4c`.
The verifier file at this result was
`0360e92898ac77bb51822e1c689f3286bb39ea328557969c3549967fdccc1dcf`.

## Post-review correction — 2026-08-17T00:23:44Z

Root review requested an explicit malformed-identity CLI assertion because
`ProtocolError` is a `ValueError`. The verifier now injects a literal
`ProtocolError("malformed identity")` from the explicit-port identity service
and requires exit `3`, empty stdout, and the exact connection/protocol
diagnostic. It passes: the qualified implementation catches `ProtocolError`
before generic `ValueError`. No finding remains.

Final verdict: **pass for C1-B3 non-hardware verification**, with the physical
USB CDC/board evidence still deferred as stated above. The updated focused
verifier has 15 passing cases; `tests/verification` has 123 passing cases and
the full non-hardware selection has 147 passing cases, each with the existing
expected duplicate-ZIP-fixture warning. Ruff, mypy, CLI help, pip check, and
`git diff --check` also pass. Exact commands were the same as the final-result
commands above, with the focused pytest command rerun after this added case.

Qualified base `HEAD` and tree remain
`f27a9f43b4a62946b43f9ae57b370210ebd1667d` and
`14cd2573308d1dfe192ceaa5f03707f53a4932fe`. The updated deterministic tracked
diff digest is
`b913d3836a57c527e4099051968924566de66194891c54a6d90e594b91291376`;
separate untracked production hashes remain `device.py`
`9e90994bd86d14bebf890b1914a051c7a85577752c626cb1d78b231702b46d74` and
`serial.py` `f67cae5f60afa2006d262af913c342f039698349e9059bda5d8c9e7741765a4c`.
The final verifier hash before this review-note-only documentation update was
`f303641b003acbb756f3fa057678c79d5dc18e70bb1d39e6d70a7516f5e34b28`.
