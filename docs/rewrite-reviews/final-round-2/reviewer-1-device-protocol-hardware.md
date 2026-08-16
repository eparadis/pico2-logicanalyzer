# Final Round 2 Review: Device Protocol and Hardware Boundary

- Reviewer: `/root/review_protocol_hardware` — Reviewer 1, Device Protocol and Hardware Boundary
- Reviewed commit: `134a4b69d1a6d0f81bb0fab37d355254d2b440ba`
- UTC timestamp: `2026-08-16T17:21:29Z`
- Verdict: pass

## Scope

This common-commit review applies the Reviewer 1 charter from
`docs/rewrite-reviews/ARCHITECTURAL_DOMAINS.md` to the immutable commit above.
It inspected all three process documents, the Round 1 and attempted-final
records, and the authoritative V2 firmware/C# sources. It rechecked the complete
firmware-byte-to-validated-`uint8`-capture boundary, with particular attention
to the newly resolved trigger boundary, authority for recovery traffic, and the
stable physical recovery-smoke contract. Working-tree changes were excluded.

## Findings and disposition

### 1. Round 1 finding: close-only cancellation versus deterministic recovery

- Status: resolved
- Evidence: `ORCHESTRATION.md:34-41,68-72,97-102` retains the bounded V2 `0xFF`
  recovery primitive and requires drain/timing/reopen/re-identification plus a
  subsequent physical capture without a power cycle. The new authority clause
  at `ORCHESTRATION.md:223-243` permits exactly one characterized `0xFF` only for
  an in-flight Cycle 1 normal capture. The matching batch checklist at
  `BATCH_EXECUTION.md:608-622` prevents that byte from becoming general device-
  management authority. This remains consistent with firmware cancellation at
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c:423-437,533-545,606-610,731-743`
  and the existing client at
  `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:628-661`.
- Disposition: accepted/no change — product behavior and execution authority now
  agree, while a public/general abort API remains deferred.

### 2. Round 1 finding: electrical safety for a 3.3 V Pico and possible 5 V SBC

- Status: resolved
- Evidence: `ORCHESTRATION.md:127-148` still requires confirmed board,
  front-end/shifter revision, voltage, VRef, permitted input range, ground, and
  D0–D7 pin mapping before wiring. It forbids applying 5 V to bare Pico GPIO and
  blocks unknown electrical conditions. C1-B1 owns the corresponding operator
  template and blocking rules in `BATCH_EXECUTION.md:341-354`.
- Disposition: accepted/no change — the physical proof can use a characterized
  SBC/front end or the explicitly simpler known 3.3 V generator without
  weakening the safety gate.

### 3. Round 1 finding: ambiguous channel selection and packed-bit mapping

- Status: resolved
- Evidence: `ORCHESTRATION.md:86-93` and
  `BATCH_EXECUTION.md:205-228` fix Cycle 1 to exactly D0–D7 in ascending order,
  mode 0, a captured D0–D7 trigger, and raw bit position equal to request-list
  position with separate physical/header metadata. Requested and actual sample
  counts must match the validated array at `BATCH_EXECUTION.md:214-226`.
- Disposition: accepted/no change — the raw-word producer/consumer boundary is
  explicit and remains consistent with firmware repacking at
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Capture.c:1323-1351`.

### 4. Round 1 finding: unspecified serial configuration and reopen behavior

- Status: resolved
- Evidence: `BATCH_EXECUTION.md:301-319` retains 115200 8N1, disabled flow
  control, asserted DTR/RTS, finite read/write timeouts, exact open/stabilize/
  drain sequencing, and bounded recovery. C1-B3 requires configuration-sequence
  tests and physical close/reopen identity at `BATCH_EXECUTION.md:432-465`.
- Disposition: accepted/no change — serial settings and lifecycle ordering remain
  testable interfaces rather than host defaults.

### 5. Round 1 finding: bounded, lossless ASCII-to-binary response parsing

- Status: resolved
- Evidence: `BATCH_EXECUTION.md:307-315` retains a single byte-buffer owner,
  bounded five-field identity/status grammar, lossless coalesced status/count/
  payload parsing, pre-allocation count validation, and the required trailing
  zero timestamp-count byte. C1-B2 requires fragmented, coalesced, overlong,
  unterminated, extra-field, malformed-length, and trailing-byte tests at
  `BATCH_EXECUTION.md:397-430`.
- Disposition: accepted/no change — no separate buffered text reader can consume
  binary payload bytes, and all inbound lengths are bounded before allocation.

### 6. Attempted-final cross-domain finding: trigger/time boundary

- Status: resolved
- Evidence: The attempted Reviewer 2 final record identified an inconsistent
  marker at `pre_trigger_samples - 1`. The common commit now defines
  `trigger_index = pre_trigger_samples`, the preceding indices as pre-trigger,
  the first post-trigger sample as time zero, and sample-instant time as
  `(index-trigger_index)/sample_rate_hz` at
  `BATCH_EXECUTION.md:214-228`. The CSV flag follows that first-post-sample
  convention at `BATCH_EXECUTION.md:230-242`. C1-B1/B2/B4 must test D0, the last
  pre-trigger sample at `-1/sample_rate_hz`, and the first post-trigger sample at
  zero (`BATCH_EXECUTION.md:371-388,397-414,492-505`).
- Disposition: accepted/no change — the marker is explicitly a model/export
  boundary at the first post-trigger sample, not an ambiguous claim that the
  last pre-trigger row is post-trigger. The physical gate separately verifies
  that captured data contains the requested edge polarity.

### 7. Attempted-final cross-domain findings: recovery authority and runnable proof

- Status: resolved
- Evidence: In addition to the narrow authority at
  `ORCHESTRATION.md:223-243`, the stable interface at
  `ORCHESTRATION.md:306-342` and `BATCH_EXECUTION.md:264-299` defines
  `hardware-recovery-smoke` with explicit port, operator-confirmed fixed-level
  idle channel/level, bounded cancellation delay, periodic signal channel and
  frequency, sample settings, edge, and evidence path. It must start an
  intentionally non-triggering normal capture, send exactly one `0xFF`, drain,
  close/reopen, re-identify, and then capture the periodic signal. C1-B5 requires
  this non-interactive physical sequence at `BATCH_EXECUTION.md:507-527`.
- Disposition: accepted/no change — the stopping condition now has a stable,
  reproducible physical command rather than depending on interactive Ctrl-C or
  an unspecified way to suppress the trigger.

### 8. New device-protocol or hardware-boundary findings

- Status: none
- Disposition: accepted/no change — the common-commit resolutions introduce no
  new ambiguity within Reviewer 1’s domain. Request layout/golden bytes remain a
  C1-B1 gate, adverse codec and recovery behavior remains C1-B2, physical serial
  identity remains C1-B3, and useful capture plus recovery proof remains C1-B4/
  B5. Wider modes, TCP, richer abort behavior, and persistent device-management
  commands remain explicitly deferred.

No open Reviewer 1 findings remain for commit
`134a4b69d1a6d0f81bb0fab37d355254d2b440ba`.
