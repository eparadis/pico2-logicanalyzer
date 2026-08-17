# C1-B4 independent acceptance

- Reviewer: `/root/c1_b1_acceptance`
- Reviewed commit: `53bfc2184c825296da20a644777729096cff3c1f`
- Reviewed tree: `7b5828208fbe72839fee2f59fd41652d5abee073`
- UTC timestamp: `2026-08-17T03:51:09Z`
- Verdict: **pass**

## Candidate and scope

`HEAD` and `git rev-parse <commit>^{tree}` matched the exact candidate. `git diff --check` passed and the C1-B4 delta contains no changes under `Firmware/` or `Software/LogicAnalyzer/`. It is confined to the authorized normal 8-channel capture, deterministic CSV/provisional replay artifacts, transactional output behavior, hardware-smoke procedure/evidence, tests, and related documentation. No GUI, wider mode, TCP, persistent-device operation, firmware change, or public recovery feature was introduced.

## Physical artifact audit

I read the current raw evidence-only artifacts under `testdata/evidence/c1-b4-runtime/` without opening a serial port:

| Artifact | SHA-256 | Independent result |
| --- | --- | --- |
| `capture.csv` | `34bf6599024c0110659c1733a152c06573e7e76b0d861c0707544d5900fb2a54` | 6,144 sample rows; exact settled header, LF rows, one trigger flag at index 2048, D0 transition data |
| `capture.npz` | `6cd69a8b26c2463a1168824777f6726e9d4651224fd007906deb17ede1a73d46` | loads with the production secure loader; rank-one contiguous `uint8` samples, exact count and canonical provisional metadata |
| `hardware-smoke.json` | `c747cd8f881e24273562a8fe82a21e79ac70ca91bd026caed3267b98ba15df5f` | sanitized port, identity/capabilities, 1 kHz measurement, requested edge/counts, and no persistent change |

The replay metadata identifies `LOGIC_ANALYZER_PICO_2_V6_0`, 200 MHz normal / 400 MHz blast limit, 393216-byte buffer, 24 channels, D0-GPIO2 mapping, rising D0 trigger, 100000 Sa/s, pre/post 2048/4096, requested/actual 6144, and trigger index 2048. The independent secure replay load succeeded with pickling disabled. Reconstructing a `CaptureResult` from that metadata produced CSV bytes exactly equal to the checked raw CSV (`190739` bytes).

The smoke evidence is sanitized (`"port":"<PORT_SUPPLIED>"`), records `persistent_device_change:false`, and contains no raw path. It reports a nonconstant D0 trace, 41 requested rising transitions, a 4000-sample first/last rising-edge span, measured 1000.0 Hz, 0.0005 endpoint quantization allowance, named 0.02 source allowance, and total 0.0205 tolerance. The physical 1 kHz rising-D0 gate therefore passes exactly.

## Trigger-index observation

- **Disposition: recorded limitation; not a C1-B4 blocker.** Independent CSV parsing found the first physical rising transition at sample 2047 (D0 `0` to `1`), while the settled logical `trigger_index` and sole CSV trigger flag are 2048. Sample 2047 and 2048 both hold D0 high.
- The settled contract defines `trigger_index = pre_trigger_samples`, the pre/post region boundary, time zero, and the CSV trigger flag. It does not require the sampled electrical transition itself to be stored at that exact index. The C1-B4 physical gate requires a nonconstant channel containing the requested polarity, which this trace supplies. The artifact correctly preserves the contractual logical boundary rather than falsely relocating it.
- This one-sample device sequencing/alignment observation must remain documented for later physical lifecycle/compatibility review; it must not be represented as proof that the physical transition is exactly the time-zero sample.

## Non-hardware acceptance dispositions

- **Pass — literal capture requests and bounds.** Independent black-box coverage validates rising/falling golden request bytes, identity/capture count validation before payload read/allocation, exact 8-bit words, cleanup, and explicit-port behavior.
- **Pass — deterministic safe artifacts.** CSV is exact self-timed UTF-8/LF; replay has the fixed two safe members, canonical metadata, exact samples, and no pickle. Transaction tests cover collisions, force, fsync, aliases, rollback/backup failures, and evidence-output failure.
- **Pass — smoke calculation and evidence.** The independent fake smoke tests verify first/last same-polarity calculation, rising/falling paths, fewer-than-two-edge rejection, quantization-plus-named-source tolerance, sanitized port replacement, and atomic evidence failure behavior.
- **Pass — accumulated gate.** Python 3.12.13 `pip check`, focused C1-B4 verifier, full verifier, Ruff, mypy, all non-hardware pytest, and module help passed. The only warning is the known C1-B2 verifier fixture warning while intentionally constructing a duplicate ZIP entry; the loader rejects that hostile archive.

## Commands and outcomes

| Command | Result |
| --- | --- |
| `.venv/bin/python -m pip check` | pass — no broken requirements |
| `.venv/bin/python -m pytest tests/verification/test_c1_b4_capture_artifacts_blackbox.py -q` | pass — 22 passed |
| `.venv/bin/python -m pytest tests/verification -q` | pass — 152 passed; one expected duplicate-ZIP fixture warning |
| `.venv/bin/python -m ruff check .` | pass |
| `.venv/bin/python -m mypy src` | pass — no issues in 17 source files |
| `.venv/bin/python -m pytest -m "not hardware" -q` | pass — 188 passed; same expected warning only |
| `.venv/bin/python -m pico_logic_analyzer --help` | pass |
| secure replay load plus independent CSV reconstruction of physical NPZ | pass — exact CSV byte match |
| independent CSV transition scan | pass — 41 rises, all 100 samples apart; first at 2047 |
| `git diff --check <candidate>^ <candidate>` | pass |

## Limitations and deferrals

This C1-B4 acceptance does not claim fixed-high/fixed-low wire checks, physical no-trigger cancellation, Ctrl-C/timeout recovery, or a second physical capture after recovery; those are C1-B5 work. The runtime artifacts are evidence-only and must be archived through the checkpoint evidence process with the candidate/tree provenance; this review did not alter them. No hardware or network operation was performed by this reviewer.

## New findings

None blocking C1-B4.
