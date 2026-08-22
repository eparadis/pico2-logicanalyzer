# Cycle 2 final review — device protocol and hardware boundary

- **Reviewer:** `/root/cycle2_review_protocol` — Reviewer 1, device protocol and hardware boundary
- **Reviewed commit:** `f115bff194c812eb1d55f5adfcf2afabd8b54589`
- **Reviewed tree:** `a0db51794c29e2b88dd14254dc8da74b0ccaced3`
- **UTC timestamp:** `2026-08-22T20:03:21Z`
- **Verdict:** pass

## Prior findings and dispositions

1. **Normal-mode trailing timestamp-count rule was underspecified** (round 1, high).
   - **Requested resolution:** Set normal `loopCount` and `measure` to zero; require a zero trailing timestamp-count byte; reject a nonzero count and its would-be timestamp payload before another request, then recover the transport; cover all widths with literal adverse fixtures.
   - **Evidence:** In `CYCLE2_BATCH_EXECUTION.md` at this commit, the Wire codec contract now fixes offsets 44 and 45 to zero for normal edge-trigger requests, requires the trailing timestamp-count byte to be exactly zero, specifies rejection and close/recovery for a nonzero count and trailing binary data, and keeps timestamped/burst responses excluded. C2-B2 acceptance requires literal nonzero-count plus four-byte-per-count payload adversarial responses at every width, receive-owner invalidation, and no subsequent request on the contaminated transport. This agrees with fixed firmware's `stampsLength` followed by timestamp bytes in `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c` and the accepted Cycle 1 zero-trailer parser contract.
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589`; verified in this final-round-1 review.

2. **Unused channel-slot and padding values were incorrectly called source-derived** (round 1, medium).
   - **Requested resolution:** Describe unused slots and explicit padding as canonical host-defined zeroes, fixture-test that convention and escaping, and cite firmware only for layout and ignored-slot behavior.
   - **Evidence:** The updated Wire codec contract states exactly that firmware establishes offsets, widths, and that slots at or above `channelCount` are ignored; it defines unused slots and explicit padding as host-defined zero bytes and requires fixtures for that convention and escaping. C2-B2 scope repeats the distinction. This matches `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c` and `LogicAnalyzer_Capture.c`, which consume only the requested channel-count prefix.
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589`; verified in this final-round-1 review.

## Final observations

1. No findings remain. The reviewed contracts retain explicit ordered-channel packing, highest-channel mode selection, little-endian mode-appropriate dtypes, byte-based count/buffer and overflow checks, zero upper byte for 24-channel words, one receive owner, and the bounded Cycle 1 recovery lifecycle.
2. The physical gate remains appropriately fixed-firmware and explicit-port only. It requires operator confirmation of protected 3.3 V, common ground, input direction, D0/D8/D16/D23 mapping, safe fan-out, and fixed D1 recovery input before proving the three masks, word widths/dtypes, frequency, upper-byte rule, re-identification, and second capture without a power cycle.
3. Cross-domain handoffs remain safe: C2-B2 owns literal byte and contaminated-receive tests before C2-B3 physical I/O; C2-B3 independently validates raw schema-2 artifacts; C2-B6 serial/API cancellation remains constrained to the accepted normal-capture recovery path.
