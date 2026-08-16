# Round 1 Review: Device Protocol and Hardware Boundary

- Reviewer: `/root/review_protocol_hardware` — Reviewer 1, Device Protocol and Hardware Boundary
- Reviewed commit: `1a6fb5aed5f0714368f3bf97af04c1789b8f9dc9`
- UTC timestamp: `2026-08-16T15:00:44Z`
- Verdict: changes_required
- Resolving commit: `7d04ed1a2a2f9c90a6017b90e41b9df61ba620c7`

## Scope

This review covers architectural domains 1–3 as defined in
`docs/rewrite-reviews/ARCHITECTURAL_DOMAINS.md`: the V2 firmware and wire
protocol, serial transport and device lifecycle, and capture validation through
a validated in-memory raw-word result. It reviewed the three rewrite/process
documents at the commit above, `Firmware/LogicAnalyzer_V2/`,
`Software/LogicAnalyzer/SharedDriver/`, and capture validation in the current
CLI, terminal, and GUI front ends. The review prioritizes a working Cycle 1
physical serial path and explicit deferral of later complexity.

## Findings and disposition

### 1. Close-only cancellation is inconsistent with the promised recovery contract

- Severity: high
- Evidence: `ORCHESTRATION.md:65-66,89-92` requires finite timeouts, cleanup,
  close/reopen recovery, and a second physical capture. `BATCH_EXECUTION.md:240-241`
  defines cancellation by closing, while `BATCH_EXECUTION.md:309-311` explicitly
  excludes graceful firmware abort and `BATCH_EXECUTION.md:337-339` requires
  timeout/Ctrl-C and close/reopen verification. In the V2 firmware,
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c:606-610,731-743` remains in its
  capture loop until capture completion or received input; any received byte is
  consumed as cancellation by `processCancel()` via
  `LogicAnalyzer.c:423-437,533-545`. Merely closing the host port does not itself
  send that byte. The current C# client sends `0xff` before reopening
  (`Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:628-661`).
- Finding: An implementation following the documents can time out, close the
  serial device, reopen it, and still find the analyzer waiting for its old
  trigger. Its next framed identity/capture request may instead be consumed as
  cancellation, so the documented recovery and reusable-state proof are not
  implementable deterministically by close alone.
- Requested resolution: Choose and state one Cycle 1 contract. Recommended:
  characterize the minimal V2 cancellation exchange (including timing, drain,
  close, reopen, and re-identification) and bring only that bounded recovery
  primitive into C1-B1/B2/B5; continue to defer a richer public abort workflow.
  Add fake and physical tests for timeout and Ctrl-C while the trigger is absent,
  followed by successful identity and capture without a power cycle. Alternative:
  explicitly limit close/reopen recovery to completed captures, state that an
  in-flight timeout may require trigger completion or a power cycle, and remove
  reusable-after-failure implications from the stopping condition.
- Disposition: resolved — the resolving commit requires the bounded V2 `0xFF`
  cancellation exchange, byte/timing/drain/reopen/re-identification contract,
  and fake plus physical no-trigger recovery evidence while keeping a general
  public abort workflow deferred.

### 2. The hardware preflight does not define a safe electrical boundary for a likely 5 V SBC

- Severity: high
- Evidence: `ORCHESTRATION.md:118-128` asks only for a “safe” periodic source and
  safely connected grounds; `BATCH_EXECUTION.md:90,295-307` delegates wiring
  assumptions to preflight/operator input without required voltage or front-end
  fields. The repository warns that a bare Pico supports only 3.3 V and needs a
  level shifter for 5 V signals (`README.md:673-675,700-706`), that level-shifter
  VRef is limited to 5.5 V with no overvoltage protection (`README.md:558-567`),
  and that mismatching analyzer and shifter board revisions can create fatal
  shorts (`README.md:539-544`). The intended simple 8-bit SBC is plausibly a 5 V
  target.
- Finding: “Safe wiring” is not a verifiable authority gate. An agent/operator
  could connect a 5 V bus directly to Pico GPIO or use an incompatible shifter
  revision while still believing the precondition is satisfied.
- Requested resolution: Make the C1-B1 operator template and every physical
  batch gate require recorded, operator-confirmed analyzer board variant,
  firmware identity/build, input-front-end or level-shifter revision, target
  logic voltage/VRef, permitted input range, common-ground point, and logical
  channel-to-header/GPIO map. State that bare Pico inputs must not receive 5 V,
  and require a compatible level shifter/probe for a 5 V SBC. Unknown voltage,
  board revision, VRef, or pin mapping must block the physical path. Preserve
  generic periodic-generator testing as the simpler alternative when the SBC
  electrical boundary is not yet characterized.
- Disposition: resolved — the resolving commit makes board/front-end revisions,
  target voltage, VRef, input range, ground, and pin map required operator
  evidence; it forbids 5 V on bare Pico GPIO and blocks unknown wiring.

### 3. “8-channel capture” does not settle the legal channel set or packed-bit mapping

- Severity: medium
- Evidence: `ORCHESTRATION.md:37,83-85` and
  `BATCH_EXECUTION.md:292-303` require a normal 8-channel/8-bit result but do not
  say whether that means exactly channels 0–7, any unique subset of up to eight
  of the 24 inputs, or merely firmware capture mode 0. Firmware accepts a channel
  list and packs requested channel position `i` into result bit `i`
  (`Firmware/LogicAnalyzer_V2/LogicAnalyzer_Capture.c:1034-1065,1079-1085,1323-1351`).
  Board builds map logical channels to different GPIO arrays
  (`LogicAnalyzer_Capture.c:61-69`). The C# request sends channel numbers in list
  order (`Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:511-533`)
  and later interprets returned bits by list position
  (`LogicAnalyzerDriver.cs:501-508`).
- Finding: Without an explicit invariant, implementations can disagree about
  uniqueness, ordering, maximum selected channel, whether the trigger must also
  be captured, and whether raw bit 3 means logical channel 3 or the fourth
  requested channel. That ambiguity reaches the in-memory handoff and can make
  an apparently valid 8-bit bus capture misleading.
- Requested resolution: In C1-B1 settle and fixture-test the narrow validation
  and mapping contract: legal logical channel IDs, non-empty and unique channel
  list, maximum count eight, deterministic request order, capture mode value,
  trigger range/membership rule, and the rule that raw bit position maps to
  request-list position (with separate retained physical/logical channel
  metadata). Recommended Cycle 1 default is exactly logical channels 0–7 in
  ascending order for an 8-bit bus, while permitting a documented unique subset
  only if it does not complicate the slice. Add a hardware bit-position check on
  more than the trigger bit when safe; otherwise record that wider physical
  mapping proof is deferred.
- Disposition: resolved — the resolving commit fixes Cycle 1 to logical D0–D7
  in ascending request order, mode 0, captured trigger membership, and ordinal
  raw-bit mapping with separately retained channel metadata.

### 4. The serial configuration and reopen behavior are not acceptance criteria

- Severity: medium
- Evidence: C1-B1 says only to document “relevant serial settings”
  (`BATCH_EXECUTION.md:198-200`), while C1-B3 accepts pySerial generally
  (`BATCH_EXECUTION.md:259-287`). The current working client opens at 115200,
  asserts RTS and DTR, uses newline `\n`, and sets large buffers before the
  identity request (`Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:83-104`).
  These settings and their open/reopen ordering are not required by any golden
  fixture or acceptance item.
- Finding: Different agents can choose pySerial defaults, toggle control lines
  at different times, leave flow control enabled, or fail to drain stale bytes.
  Such differences often appear only on one host and undermine the Linux/macOS
  physical gate and deterministic close/reopen proof.
- Requested resolution: Require `docs/device-protocol.md` to state and justify
  baud, data bits, parity, stop bits, software/hardware flow control, read/write
  timeout semantics, DTR/RTS values and ordering, open stabilization/drain
  policy, and reopen behavior. Add pySerial contract tests that assert the
  constructor/configuration and cleanup sequence, plus one physical identity
  and close/reopen check on the supported host. Mark settings that USB CDC
  ignores as compatibility settings rather than silently omitting them.
- Disposition: resolved — the resolving commit specifies 115200 8N1, disabled
  flow control, asserted DTR/RTS, finite timeouts, documented open/drain/reopen
  ordering, contract tests, and physical reopen evidence.

### 5. The ASCII-to-binary response boundary can lose bytes or grow without a bound

- Severity: medium
- Evidence: V2 identity is five newline-terminated ASCII lines
  (`Firmware/LogicAnalyzer_V2/LogicAnalyzer.c:246-264`); capture first returns
  `CAPTURE_STARTED\n`, then a native-endian 32-bit sample count, sample bytes,
  and a timestamp-count byte (`LogicAnalyzer.c:267-304,606-640,714-725`). The
  current C# client uses a buffered `StreamReader` for lines and a separate
  `BinaryReader` on the same stream (`Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:83-104,273-323`),
  a pattern that can read ahead across the text/binary boundary. C1-B2 requires
  fragmentation and allocation limits (`BATCH_EXECUTION.md:230-255`) but does not
  explicitly bound ASCII lines or require a coalesced start-line-plus-binary
  test.
- Finding: A Python port can reproduce the split-buffer defect, drop binary
  bytes already buffered by a text wrapper, or accept an unbounded unterminated
  identity/status line before any 32-bit payload bound is applied.
- Requested resolution: Define one byte-oriented receive buffer/parser with
  maximum line lengths, ASCII/newline grammar, exactly five bounded identity
  fields, and a lossless transition from `CAPTURE_STARTED\n` to the four-byte
  little-endian count and raw payload. B2 tests must cover one-byte
  fragmentation, all response bytes arriving in one read, delimiter splits,
  overlong/unterminated lines, extra identity fields, and a coalesced status line
  plus binary payload. The sample count must equal the validated Cycle 1 request
  and remain within the negotiated buffer before allocation/read; consume and
  validate the trailing zero timestamp-count byte for the non-burst slice.
- Disposition: resolved — the resolving commit assigns all ASCII/binary input to
  one bounded byte buffer, limits five identity fields/status lines, defines the
  lossless binary transition and trailing zero timestamp byte, and requires
  fragmentation/coalescing/overlong-field tests.
