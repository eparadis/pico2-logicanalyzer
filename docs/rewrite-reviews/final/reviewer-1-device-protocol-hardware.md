# Final Review: Device Protocol and Hardware Boundary

- Reviewer: `/root/review_protocol_hardware` — Reviewer 1, Device Protocol and Hardware Boundary
- Reviewed commit: `de93d47dabb64cfc0e014ce9eed807877b9f5b69`
- UTC timestamp: `2026-08-16T17:14:59Z`
- Verdict: pass

## Scope

This final review applies the Reviewer 1 charter in
`docs/rewrite-reviews/ARCHITECTURAL_DOMAINS.md` to the exact commit above. It
reviewed the resolved `ORCHESTRATION.md`, `BATCH_EXECUTION.md`, technical
roadmap, Round 1 Reviewer 1 record and dispositions, and the authoritative V2
firmware/C# evidence. It covers framing through a validated in-memory D0–D7
capture, serial lifecycle and recovery, electrical safety, and physical proof.
Working-tree changes were not considered.

## Findings and disposition

### 1. Prior finding: close-only cancellation versus recovery

- Status: resolved
- Evidence: `ORCHESTRATION.md:34-41,68-72,97-102` now requires the bounded V2
  `0xFF` cancellation primitive, documented drain/timing/reopen and
  re-identification, and board reuse without a power cycle. It explicitly keeps
  the broader public abort workflow deferred at `ORCHESTRATION.md:106-114`.
  `BATCH_EXECUTION.md:279-297` settles the serial/recovery contract;
  `BATCH_EXECUTION.md:369-395` requires fake recovery followed by identity; and
  `BATCH_EXECUTION.md:472-488` requires a physical no-trigger timeout or Ctrl-C
  recovery followed by capture. This matches firmware behavior at
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c:423-437,533-545,606-610,731-743`
  and the existing client’s `0xFF` behavior at
  `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:628-661`.
- Disposition: accepted/no change — Cycle 1 includes only the minimum recovery
  exchange needed to make timeout and close/reopen deterministic.

### 2. Prior finding: unsafe or unverifiable electrical preflight

- Status: resolved
- Evidence: `ORCHESTRATION.md:127-148` requires operator-confirmed board and
  front-end/shifter revisions, target voltage, VRef, permitted input range,
  common ground, and D0–D7 pin map before wiring. It explicitly prohibits 5 V
  on bare Pico GPIO, requires a compatible referenced shifter/probe for a 5 V
  SBC, and blocks unknown electrical inputs. `BATCH_EXECUTION.md:319-329`
  assigns those fields to the C1-B1 operator template and requires unknowns to
  block hardware. This resolves the repository warnings at
  `README.md:539-544,558-567,673-675,700-706`.
- Disposition: accepted/no change — the physical gate is now objective and safe
  for either a known 3.3 V generator or a characterized SBC/front end.

### 3. Prior finding: ambiguous 8-channel selection and packed-bit identity

- Status: resolved
- Evidence: `ORCHESTRATION.md:86-93` fixes Cycle 1 to logical D0–D7 in ascending
  request order, constrains the trigger to a captured D0–D7 channel, and defines
  raw bit `i` as request-list position `i`. `BATCH_EXECUTION.md:199-217` further
  requires exact `uint8` raw words, rejects duplicates/subsets, fixes capture
  mode 0, retains physical/logical metadata separately, and settles sample and
  trigger metadata. C1-B2 and C1-B4 must enforce and test that contract at
  `BATCH_EXECUTION.md:367-382,443-468`. This is consistent with firmware packing
  in `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Capture.c:1323-1351`.
- Disposition: accepted/no change — the validated raw-word handoff has one
  unambiguous channel and bit-order interpretation.

### 4. Prior finding: unspecified pySerial configuration and reopen sequence

- Status: resolved
- Evidence: `BATCH_EXECUTION.md:279-284` fixes 115200 baud, 8N1, no flow control,
  finite read/write timeouts, asserted DTR/RTS, and requires exact
  configure/open/stabilize/drain documentation. C1-B3 requires configuration-
  sequence tests plus physical close/reopen identity at
  `BATCH_EXECUTION.md:400-432`. The resulting contract preserves the relevant
  current-client settings from
  `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:83-104` while
  requiring USB CDC exceptions to be documented.
- Disposition: accepted/no change — serial configuration is a testable batch
  interface rather than an implementation default.

### 5. Prior finding: lossy or unbounded ASCII-to-binary transition

- Status: resolved
- Evidence: `BATCH_EXECUTION.md:285-293` gives one byte-oriented buffer ownership
  of text and binary phases, bounds the exact five identity lines and status
  line, requires a lossless coalesced status/count/payload transition, bounds and
  checks the little-endian count before allocation/read, and validates the final
  zero timestamp-count byte. C1-B2 requires one-byte fragmentation, single-read
  coalescing, overlong/unterminated/extra-field, malformed-length, and trailing-
  byte tests at `BATCH_EXECUTION.md:369-395`. This removes the separate buffered
  readers risk present in
  `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:83-104,273-323`.
- Disposition: accepted/no change — parser ownership, bounds, response grammar,
  and adverse-read proof are explicit.

### 6. New protocol or hardware-boundary findings

- Status: none
- Disposition: accepted/no change — the resolutions introduce no new open
  ambiguity in Reviewer 1’s domain. Exact native request offsets/padding and
  rising/falling golden bytes remain a C1-B1 gate; bounded parsing and recovery
  remain C1-B2 gates; serial identity is a C1-B3 physical gate; and capture plus
  lifecycle proof remains confined to C1-B4/B5. Later widths, modes, transports,
  public abort behavior, and device-management commands remain explicitly
  deferred.

No open Reviewer 1 findings remain for commit
`de93d47dabb64cfc0e014ce9eed807877b9f5b69`.
