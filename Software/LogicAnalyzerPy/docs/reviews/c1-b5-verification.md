# C1-B5 independent recovery verification

## Prepared verification matrix

Status: source/contract-derived expectations are prepared. Binding waits for
the C1-B5 recovery service and `hardware-recovery-smoke` CLI implementation.
No hardware or network access was used.

| Surface | Independent observation | Required behavior |
| --- | --- | --- |
| Cancellation byte | Literal `ff` | Exactly one raw byte, only after an in-flight normal capture begins. |
| Bounds | Fake clock and continuous readable input | One finite deadline across the entire drain; at most 4096 drained bytes. |
| Failure cleanup | Timeout, Ctrl-C, malformed response, disconnect, write/drain/reidentify error | Close on every path; no second cancel byte or leaked transport. |
| Lifecycle | Recording transport/service factory | Cancel, bounded drain, close old transport, reopen, re-identify, then second periodic capture. |
| CLI | Fake service and temp evidence directory | No automatic port selection; exact exit/stream partition; finite typed `--cancel-after`; idle/signal channel and level validation. |
| Evidence | Fixed fake capture plus injected file failure | Atomic JSON, sanitized `<PORT_SUPPLIED>`, no machine path, no persistent-operation claim. |

## Provenance and deferrals

`Firmware/LogicAnalyzer_V2/LogicAnalyzer.c` polls cancellation during the
no-trigger loop and stops capture on received input. C#
`LogicAnalyzerDriver.StopCapture` writes one `0xFF`, waits, closes, and reopens.
The governing Python contracts refine that legacy behavior to exactly one raw
`0xFF` only while a normal capture is in flight, followed by a shared-deadline,
4096-byte bounded drain, close/reopen/re-identify. These are source-derived
and settled-contract expectations, not production-derived expected values.

The proposed fixed-low D1/GPIO3 input remains unconfirmed by the operator.
Physical recovery proof, actual timing, and the second physical D0 capture are
therefore pending and will not be claimed from fake tests.

## Interim bound result — 2026-08-17T03:02:00Z

Verdict: **changes_required**. The verifier is bound to the observable
`V2DeviceService.recovery_capture` and `hardware-recovery-smoke` interfaces.
It uses a literal five-field V2 identity, the independently held rising request
fixture, literal raw cancellation byte `ff`, and an exactly 255-sample
alternating periodic response for the `pre=170`, `post=85` configuration.

`rtk .venv/bin/python -m ruff check tests/verification/test_c1_b5_recovery_blackbox.py`
passes. The focused command
`rtk .venv/bin/python -m pytest tests/verification/test_c1_b5_recovery_blackbox.py -q`
reports **1 failed, 7 passed**. The failing case proves that `cancel_after=True`
with a valid `timeout=2.0` opens/constructs a transport rather than raising
`ValueError` before I/O. Booleans are not valid finite numeric command/service
parameters under the settled exact-type contract.

No production file was edited. The physical D1/GPIO3 setup remains
operator-unconfirmed and pending.

## Final non-hardware result — 2026-08-17T04:47:50Z

Verdict: **pass for the C1-B5 non-hardware recovery surface**. The interim
`cancel_after=True` finding is resolved: recovery now rejects a boolean,
non-real, non-finite, non-positive, or timeout-equal/greater cancellation
delay before constructing a transport. The independent test proves the factory
is untouched for each rejected value.

The focused verifier has **10 passed** cases. In addition to the exact-type
correction, it proves literal `ff` appears exactly once only after the initial
normal capture request, an exact 255-sample periodic second capture follows
close/re-identify, Ctrl-C after in-flight capture still cancels/closes/
re-identifies, malformed setup closes without cancellation, and the recovery
CLI requires an explicit port and creates sanitized atomic evidence. The
evidence assertion uses a literal supplied machine-local path and requires
only `<PORT_SUPPLIED>` to be persisted.

Commands run from `Software/LogicAnalyzerPy`:

- `rtk .venv/bin/python -m pytest tests/verification/test_c1_b5_recovery_blackbox.py -q` — 10 passed.
- `rtk .venv/bin/python -m pytest tests/verification -q` — 162 passed, one existing duplicate-ZIP-fixture warning.
- `rtk .venv/bin/python -m pytest -m 'not hardware' -q` — 201 passed, the same expected warning.
- `rtk .venv/bin/python -m ruff check .`, `rtk .venv/bin/python -m mypy src`, `rtk .venv/bin/python -m pico_logic_analyzer --help`, and `rtk git diff --check` — pass.

No hardware or network operation occurred. The C1-B5 physical stopping
condition remains pending operator confirmation of the proposed fixed-low
D1/GPIO3 wiring, followed by the authorized no-trigger recovery and second
physical D0 capture; this fake verification is not a substitute for either.
