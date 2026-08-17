# C1-B5 and final Cycle 1 independent acceptance

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed candidate: `aeba415939d2f3d3f6d21852d3b446c4b6fef69b`
- Reviewed tree: `ec839c5646c09fbab5403ddde62304a2049eac0a`
- UTC timestamp: `2026-08-17T04:59:24Z`
- Verdict: **pass**

## C1-B5 recovery disposition

- **Pass — bounded internal recovery.** `V2DeviceService.recovery_capture` validates a finite, positive, non-Boolean `cancel_after < timeout` before transport construction; identifies; sends a normal fixed-level request; marks it in-flight; then recovers. `CaptureRecovery` writes literal `b"\xff"` exactly once, drains at most 4096 one-byte reads under one monotonic deadline, closes, reopens and identifies. The service then performs a separate normal periodic capture. Setup failures close without cancellation; write/drain/close/re-identification failures become `RecoveryError`; Ctrl-C/timeout after the request take the same recovery path.
- **Pass — independent observable ordering.** The ten C1-B5 black-box cases use literal V2 inputs and recording transports to prove one `ff` only after the initial capture request, drain/close/re-identify before second capture, Ctrl-C cleanup, no cancellation for malformed setup, strict pre-I/O delay validation, explicit port requirement, and sanitized atomic evidence. The accumulated protocol verifier proves the 4096 cap, decreasing shared deadline, and close on recovery failure.
- **Pass — CLI/scope.** `hardware-recovery-smoke` requires explicit inputs and deterministic errors. It sanitizes the port and declares no persistent change. The reviewed Python surface introduces no GUI/Qt, pythonnet/Roslyn, TCP/Wi-Fi, wider capture, decoder, bootloader, or public general-abort feature.

## Physical recovery evidence

I inspected pre-archive evidence-only `testdata/evidence/c1-b5-runtime/recovery-smoke.json` without opening a serial port. SHA-256: `44a7bffc0bcc7c415ba8fa09efb26624853dce26833216d78d408b9c45907815`.

- **Pass — configuration and recovery.** Operator-confirmed wiring is the integrated V2 protection board, 3.3 V VRef/common labelled ground, D0/GPIO2 protected 3.3 V 1 kHz input, and D1/GPIO3 directly grounded/fixed low. The sanitized result reports `cancel_after_seconds: 0.25`, `cancel_byte: "ff"`, `reidentified: true`, `persistent_device_change: false`, and `LOGIC_ANALYZER_PICO_2_V6_0`.
- **Pass — second capture without power cycle.** The recovered D0 capture has exactly 6144 samples (`2048 + 4096`), rising edge, 100000 Sa/s, 42 rises over 4093 samples, and 1001.710236989983 Hz. Independent calculation `100000 * (42 - 1) / 4093` matches; about 0.171% error is within the recorded 2.0488639% source-plus-quantization tolerance.
- **Evidence-strength limitation, accepted.** The sanitized JSON is a physical command result, not a raw serial trace, so it does not itself timestamp each event or count wire bytes. In combination with independently exercised literal fake ordering and the inspected command path, it credibly records the required physical cancel semantic, re-identification, and valid second capture. I did not perform physical I/O.

## ORCHESTRATION.md stopping conditions

| Condition | Disposition and linked evidence |
| --- | --- |
| 1. Python 3.12 install/help | **Pass.** Retained clean `/private/tmp/pico-la-c1-b5-clean` is Python 3.12.13, passes `pip check`, has locked numpy/pyserial/pytest/ruff/mypy/setuptools/wheel versions, and editable `direct_url.json`. Checked workflow uses hash lock then `--no-build-isolation --no-deps -e .`; help passed. |
| 2. Static/non-hardware gate | **Pass.** Ruff, mypy, and 201 non-hardware tests passed. |
| 3. Provenance fixtures | **Pass.** Accepted C1-B1/C1-B2 fixture/provenance records retain literal V2 identity and normal rising/falling 8-channel request/response evidence. |
| 4. Fake/replay errors/cleanup | **Pass.** Accepted C1-B2 matrix and current 162-test verifier cover fragmentation, malformed data, finite timeout, disconnect, hostile replay, and cleanup. |
| 5. Physical identity/capture | **Pass.** C1-B3 identity and C1-B4 rising-D0 capture are accepted; this recovered second rising-D0 capture retains count/polarity/frequency evidence. Both polarities are fake-tested. |
| 6. Deterministic safe output | **Pass.** C1-B4 independently secure-loaded replay and exactly regenerated physical CSV; current hostile replay tests pass. |
| 7. Close/recovery/second physical capture | **Pass.** C1-B5 ordering/bounds tests plus fixed-low cancel/re-identify/recovered-D0 artifact prove this gate without power cycle. |
| 8. Final handoff evidence | **Pass.** B1--B4 progress/reviews identify commands, hashes, artifacts, limits, and deferrals; this review records B5 artifact/hash and exact supplied candidate/tree. Orchestrator owns the subsequent archive checkpoint. |
| 9. C#/firmware rollback | **Pass.** B1--B4 accepted changed-path audits preserve C#/firmware; C1-B5 scope is Python recovery/CLI/tests/docs, with no firmware, bootloader, or persistent-device action. |

The C1-B4 one-sample physical-edge/logical-marker offset remains a documented later-cycle alignment limitation; it does not invalidate periodic rising-polarity or recovery proof.

## Commands and outcomes

Run without hardware or network access:

| Command | Outcome |
| --- | --- |
| `.venv/bin/python --version` | pass — Python 3.12.13 |
| `.venv/bin/python -m pip check` | pass — no broken requirements |
| `.venv/bin/python -m ruff check .` | pass |
| `.venv/bin/python -m mypy src` | pass — no issues in 17 source files |
| `.venv/bin/python -m pytest tests/verification/test_c1_b5_recovery_blackbox.py -q` | pass — 10 passed |
| `.venv/bin/python -m pytest tests/verification -q` | pass — 162 passed; one expected duplicate-ZIP fixture-construction warning |
| `.venv/bin/python -m pytest -m "not hardware" -q` | pass — 201 passed; same warning |
| `.venv/bin/python -m pico_logic_analyzer --help` | pass |
| clean venv Python/pip/version/direct-url/help inspection | pass — independently corroborates clean locked editable-install outcome; installation was not rerun because this acceptance had no network authority |
| `sha256sum testdata/evidence/c1-b5-runtime/recovery-smoke.json` | pass — hash above |

No `git` operation was run because the assignment prohibited it; the candidate/tree are the frozen identifiers supplied for review. No hardware or network access was performed.

## Limitations and deferrals

Cycle 1 remains limited to V2 normal eight-channel capture. GUI, `.lac`, wider modes, advanced triggers, decoders, TCP/Wi-Fi, packaging, and public general-abort semantics remain deferred. The physical artifact is a sanitized summary rather than a raw serial trace; the known one-sample edge/marker alignment remains documented and is not overstated.
