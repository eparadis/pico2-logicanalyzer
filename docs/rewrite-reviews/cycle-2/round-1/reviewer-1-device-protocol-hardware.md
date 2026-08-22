# Cycle 2 review — device protocol and hardware boundary

- **Reviewer:** `/root/cycle2_review_protocol` — Reviewer 1, device protocol and hardware boundary
- **Reviewed commit:** `61bf35dc5cf3a95a1513cbb13f182635bd3b8461`
- **UTC timestamp:** `2026-08-22T01:45:55Z`
- **Verdict:** changes_required

## Findings

1. **The normal-mode trailing timestamp-count rule is underspecified.**
   - **Severity:** high
   - **Evidence:** `CYCLE2_BATCH_EXECUTION.md` calls for a four-byte count, word payload, and an “accepted trailing non-burst timestamp-count byte,” but does not require that byte to be zero or state how a nonzero value is rejected/consumed. The accepted Cycle 1 protocol contract, `Software/LogicAnalyzerPy/docs/device-protocol.md`, requires a trailing timestamp count of zero for normal capture, and the current parser rejects any nonzero byte. In fixed firmware, `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c` sends `stampsLength` followed by `stampsLength * 4` timestamp bytes whenever it is nonzero. Permitting a nonzero byte while consuming only one byte would leave binary data in the shared receive owner and corrupt the next exchange.
   - **Requested resolution:** Freeze the normal edge-trigger request as `loopCount = 0` and `measure = 0`, require the trailing timestamp-count byte to be exactly `0`, and require rejection before a subsequent request for a nonzero count or any trailing bytes. Include literal adverse fixtures for a nonzero count and its would-be timestamp payload at every word width. Keep timestamped/burst handling deferred with the other excluded modes.
   - **Disposition:** open

2. **The contract incorrectly labels unused channel-slot and padding values as source-derived.**
   - **Severity:** medium
   - **Evidence:** The wire-codec contract requires unused channel slots and padding to use “exact source-derived values.” The checked-in firmware source fixes the 48-byte field layout, but `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c` passes only `channels[0..channelCount-1]` to capture setup; `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Capture.c` reads only that many entries. The explicit alignment/padding bytes and unused entries have no firmware-required value. Cycle 1 used zeroes as a host convention, not a value imposed by firmware.
   - **Requested resolution:** State that all otherwise-unused channel slots and explicit padding are canonical host-defined zero bytes, with literal fixtures proving that convention and its escaping. Cite firmware only for offsets, field widths, and the fact that unused slots are ignored. This preserves the fixed ABI while avoiding an unprovable source-provenance claim.
   - **Disposition:** open

## Reviewed no-change observations

1. The contracts correctly preserve the fixed checked-in V2 Pico 2 firmware, explicit port selection, and the Cycle 1 one-`0xFF` in-flight recovery sequence with bounded drain, close, reopen, and re-identification.
2. Ordered channel IDs are correctly separated from packed returned bit positions; mode selection by highest physical ID, little-endian `uint8`/`uint16`/`uint32`, byte-based buffer bounds, and zero bits 24–31 for mode 2 are all explicit.
3. The C2-B3 gate appropriately requires operator confirmation of 3.3 V protection, common ground, input direction, D0/D8/D16/D23 mapping, source-drive safety, and fixed D1 recovery input. Its simultaneous-pattern masks (`0x01`, `0x0101`, `0x810101`) give useful byte-boundary and 24-bit upper-byte evidence without treating floating channels as controlled.
4. The physical proof remains correctly non-substitutable by fake tests and requires independent raw schema-2 artifact validation, exact count/dtype/mask evidence, and reuse without a power cycle.
