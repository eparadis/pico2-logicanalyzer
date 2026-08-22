# Cycle 2 Final Review — Capture Data and Browser Workflows

- **Reviewer:** `/root/cycle2_review_data_web` — Reviewer 2, capture data and browser workflow boundary
- **Reviewed commit:** `f115bff194c812eb1d55f5adfcf2afabd8b54589`
- **Reviewed tree:** `a0db51794c29e2b88dd14254dc8da74b0ccaced3`
- **UTC timestamp:** `2026-08-22T20:03:41Z`
- **Verdict:** `pass`

## Round-1 finding dispositions

1. **Standalone self-timed CSV metadata handoff — resolved.**

   - **Evidence:** `CYCLE2_BATCH_EXECUTION.md`, “Self-timed CSV,” now defines
     an exact four-field import-metadata object (`channel_ids`,
     `sample_rate_hz`, `trigger_channel`, and `trigger_edge`), derives packed
     positions and capture fields deterministically, and prohibits inferring
     physical identity from labels or filenames. It also requires both the
     browser confirmation flow to display the physical-ID-to-packed-position
     mapping and equivalent CLI options. The legacy D0-D7 exception is bounded
     to its exact header.
   - **Disposition:** resolved by reviewed commit

2. **Sampled-bus edge at sample zero — resolved.**

   - **Evidence:** The “Parallel-bus analysis” contract now states that sample
     zero is never an edge, assumes no synthetic prior strobe level, and compares
     only `i-1` and `i` for `i >= 1`. Required fixtures cover initial high and
     low for both polarities as well as later rising/falling edges. Python remains
     the sole analysis, API-export, and browser-table authority.
   - **Disposition:** resolved by reviewed commit

3. **CSV timing inference and rounding — resolved.**

   - **Evidence:** The CSV contract now fixes ASCII decimal grammar, finite-value
     validation, exact Decimal comparison against Cycle 1’s `.12g` values for a
     supplied rate, the legacy integer-rate candidate algorithm, and the
     canonicalization/re-export rule. It explicitly covers non-terminating sample
     periods and preserves byte-identical accepted D0-D7 export.
   - **Disposition:** resolved by reviewed commit

## Final review result

No findings remain. The reviewed contracts retain strict physical-ID versus
packed-position separation; bounded inert schema-1/schema-2 replay handling;
the explicit no-pickle, no-`.lac`, and no-.NET boundary; Python ownership of
capture/replay/export/bus semantics; bounded windowed and transition-reduced
Canvas work; and the practical 8-bit-SBC bus workflow without decoder or
editing scope expansion. The C2-B5 baseline-before-threshold procedure and its
cross-domain API/browser evidence requirements remain intact.
