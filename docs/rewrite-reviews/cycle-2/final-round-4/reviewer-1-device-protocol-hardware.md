# Cycle 2 final review — device protocol and hardware boundary

- **Reviewer:** `/root/cycle2_review_protocol` — Reviewer 1, device protocol and hardware boundary
- **Reviewed commit:** `9ce6abff934c6164791edb2adb2099a5b7b0bc90`
- **Reviewed tree:** `46b4861911afe69d79829e01b1d933fac0b6b3eb`
- **UTC timestamp:** `2026-08-22T23:29:47Z`
- **Verdict:** pass

## Prior finding status

1. **Normal-mode timestamp-count framing** (round 1, high) remains resolved: normal `loopCount`/`measure` are fixed to zero; a nonzero trailer and would-be timestamp bytes are rejected and recover the transport; C2-B2 retains literal adverse fixtures for every word width.
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589`; retained without regression through final rounds 2 and 3 and verified at this commit.

2. **Unused channel-slot/padding provenance** (round 1, medium) remains resolved: zeroes are canonical host-defined request bytes, not asserted firmware-required values; firmware remains authoritative for ABI layout, widths, and ignored slots.
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589`; retained without regression through final rounds 2 and 3 and verified at this commit.

## Exact-candidate ordering analysis

1. The corrected per-batch sequence requires passing focused checks before the immutable candidate, then independent verification of that exact candidate, then every active-batch accumulated gate against that same verified candidate, then acceptance with the verifier record and exact gate results. This preserves a single auditable candidate for all device/protocol/hardware results.
2. Every focused failure, accumulated-gate failure, verification finding, acceptance finding, or implementation correction requires a new immutable candidate. That candidate repeats independent verification and complete accumulated validation before acceptance; no earlier protocol, physical, recovery, or browser/API pass can transfer to it.
3. Evidence manifests are created only after implementation, verification, accumulated validation, and acceptance evidence exist for the same candidate, and are validated and committed before the checkpoint. Therefore C2-B3's D0/D8/D16/D23 masks, word widths/dtypes, upper-byte, recovery, close/reopen, and second-capture proof retain an exact candidate/tree and cannot be supplied by placeholder or stale evidence. C2-B6 retains final live-proof ownership.

## Final observation

1. No findings remain. The common-commit set still preserves fixed firmware, explicit port and operator/electrical gates, normal-only protocol/recovery boundaries, ordered packing, mode/dtype/endianness/upper-byte and byte-buffer invariants, and non-substitutable physical proof.
