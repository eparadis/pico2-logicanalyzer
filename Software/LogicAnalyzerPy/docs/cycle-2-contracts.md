# Cycle 2 frozen contracts

This index freezes the C2-B1 interfaces from the approved orchestration and batch contracts. It is intentionally descriptive; production behavior is implemented only in its owning batch.

- Capture: ordered unique D0–D23 IDs, request-position bit packing, highest-ID word mode, native rank-one `uint8`/`uint16`/`uint32`, and zero upper byte for 24-channel words.
- Replay: inert two-member NPZ (`samples.npy`, `metadata.npy`), `allow_pickle=False`, canonical UTF-8 JSON, schema 1 read compatibility and schema 2 writing in C2-B2.
- CSV: UTF-8 LF self-timed CSV, leading `sample_index,time_seconds,trigger`, explicit ordered labels, and explicit import metadata except for the exact legacy D0–D7 header.
- Bus: ordered LSB-first data channels; transitions begin at sample zero; sampled rows occur only at a real distinct-strobe edge.
- API/server: `/api/v1`, loopback-only canonical origin, no CORS, bounded inert reads, capability-cookie plus exact Origin for mutations, and no serial access in the B1 shell.
- Rendering: React state plus Canvas pixels, deterministic viewport functions, and bounds by visible channels/pixels/transitions. Performance thresholds are owned by C2-B5.

The complete normative details remain in `CYCLE2_BATCH_EXECUTION.md`; changes require its governed review process.
