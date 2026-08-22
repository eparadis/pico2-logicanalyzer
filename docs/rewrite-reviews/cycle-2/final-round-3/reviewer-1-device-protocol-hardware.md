# Cycle 2 final review — device protocol and hardware boundary

- **Reviewer:** `/root/cycle2_review_protocol` — Reviewer 1, device protocol and hardware boundary
- **Reviewed commit:** `911c18882aecc6554ff0f49f149720c01d8cb409`
- **Reviewed tree:** `172c6e1f9332e2bcef8dc09b2cafc11deabfcc67`
- **UTC timestamp:** `2026-08-22T23:16:00Z`
- **Verdict:** pass

## Prior finding status

1. **Normal-mode timestamp-count framing** (round 1, high) remains resolved. The governing Wire codec fixes normal `loopCount`/`measure` to zero, requires a zero trailer, rejects a nonzero trailer and its would-be timestamp payload before a subsequent request, and requires recovery; C2-B2 retains literal adverse fixtures at all word widths.
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589`; retained without regression through `7a5f429db93c2164ef54334c0eb3adf48ae68ff0` and verified here.

2. **Unused-slot/padding provenance** (round 1, medium) remains resolved. The governing codec continues to call unused channel slots and explicit padding canonical host-defined zeroes while using firmware provenance only for ABI layout, widths, and ignored-slot behavior.
   - **Disposition:** resolved in `f115bff194c812eb1d55f5adfcf2afabd8b54589`; retained without regression through `7a5f429db93c2164ef54334c0eb3adf48ae68ff0` and verified here.

## Goal-specific analysis

1. The fixed implementor/verifier/acceptance pool preserves independent protocol and hardware proof: the implementor cannot approve its own work, verification and acceptance are distinct lanes, candidate correction returns to the same implementor and must re-pass verification before acceptance, and detailed durable records—not lossy handoffs—remain the source for findings.
2. The context-preserving/no-primary-content-review rule does not displace technical ownership. The verifier still performs independent black-box, boundary, protocol, and hardware verification; acceptance still examines the integrated candidate, evidence, scope, and checkpoint. Compact handoffs preserve candidate/tree, evidence paths and digests, verdict, finding identifiers, and required operator input, while the implementor reads a changes-required record directly.
3. Hardware/operator authority remains explicit and conservative: fresh confirmation of port, Pico 2 fixed V2 firmware, protection, 3.3 V VRef, ground, D0/D8/D16/D23 mapping and input direction, safe fan-out, and a fixed idle recovery input precedes C2-B3. The goal retains only identity, normal capture, and the established in-flight one-byte recovery sequence; it prohibits flash, bootloader, Wi-Fi, persistent mutation, and power-cycle demands.
4. The candidate/review and manifest loop preserves evidence integrity. C2-B3 remains owner of its physical masks/dtypes/counts/upper-byte/recovery/second-capture proof, and C2-B6 remains the final live proof owner. Each manifest is created only after owning-batch verification and acceptance evidence, then validated and committed before the checkpoint; no placeholder can satisfy a physical gate.

## Final observation

1. No findings remain. The complete common-commit set preserves ordered-channel ABI, mode/dtype/endianness and upper-byte invariants, byte-based bounds, single receive ownership, explicit port and fixed-firmware boundaries, real D0/D8/D16/D23 proof, and Cycle 1 recovery without a power cycle.
