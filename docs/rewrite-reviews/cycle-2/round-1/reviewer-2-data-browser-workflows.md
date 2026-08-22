# Cycle 2 Review — Capture Data and Browser Workflows

- **Reviewer:** `/root/cycle2_review_data_web` — Reviewer 2, capture data and browser workflow boundary
- **Reviewed commit:** `61bf35dc5cf3a95a1513cbb13f182635bd3b8461`
- **Reviewed tree:** `f1e2ee2d571e5e1a0077872f694f82198a743186`
- **UTC timestamp:** `2026-08-22T01:45:46Z`
- **Verdict:** `changes_required`

## Findings

1. **Standalone self-timed CSV has no defined metadata handoff.**

   - **Severity:** high
   - **Evidence:** `CYCLE2_BATCH_EXECUTION.md` requires CSV columns after the
     fixed prefix to use display labels, while import requires "explicit channel
     metadata supplied by the schema or import command." The same document makes
     C2-B5 open a self-timed CSV through the browser API. A CSV header containing
     labels cannot recover physical IDs, packed positions, trigger channel/edge,
     or the mapping needed to preserve ordered-channel semantics. Neither contract
     defines an import-sidecar/schema, an API request object, browser controls, or
     a deterministic default that supplies those fields.
   - **Requested resolution:** Freeze one exact standalone CSV-import handoff
     before C2-B2: identify every required metadata field, its serialized or API
     source, validation/bounds, and the browser workflow for supplying it. Prove
     a reordered/noncontiguous capture round-trip preserves physical ID versus
     packed position, while the accepted D0-D7 export stays byte-identical.
   - **Disposition:** open

2. **The sampled-bus rule is ambiguous at sample index zero.**

   - **Severity:** medium
   - **Evidence:** The parallel-bus contract says sampled mode emits on a strobe
     rising/falling transition and separately requires explicit tests for an
     "edge at index zero." It never specifies an initial predecessor strobe
     level, nor whether index zero is categorically not an edge. Therefore the
     same one-sample/initial-high fixture can legitimately produce different rows
     in Python, API export, and the browser table.
   - **Requested resolution:** Define the sample-zero convention in the C2-B4
     contract (for example, no edge at zero, or a stated synthetic prior level),
     then add independent fixtures for both polarities at zero and at later
     indexes. Keep the Python analysis result as the sole table/export authority.
   - **Disposition:** open

3. **CSV time validation is not precise enough to guarantee the required
   deterministic import/export round trip.**

   - **Severity:** medium
   - **Evidence:** The CSV contract requires timing to be "constant ... consistent
     with the declared/inferred sample rate" but does not define numeric grammar,
     sample-rate declaration/inference algorithm, or rounding/tolerance. Accepted
     Cycle 1 export formats each time independently with `.12g`; for many rates,
     decimal rounding makes adjacent textual differences non-identical. The C2-B2
     acceptance gate nevertheless requires deterministic import/export for all
     widths/subsets.
   - **Requested resolution:** Freeze the accepted numeric syntax and a
     deterministic inference/validation rule that accepts the existing D0-D7
     bytes, including its rounding behavior, rejects materially irregular times,
     and specifies whether re-export is byte-identical or canonicalized for all
     generalized CSV imports. Cover a non-terminating sample period and a
     reordered subset independently.
   - **Disposition:** open

## Reviewed no-change observations

- The contracts consistently keep ordered physical channel IDs distinct from
  packed request positions and require vectorized extraction by packed position.
- Replay schema 2 remains an inert bounded NPZ/JSON format, schema 1 remains
  read-only compatible, and the explicit no-pickle, no-`.lac`, and no-.NET
  decisions are unambiguous.
- The bus scope is appropriately useful for an 8-bit SBC while deferring CPU
  decoding, decoder plugins, capture editing, and annotations.
- Python retains capture/replay/export/bus authority; React consumes bounded,
  windowed and transition-reduced data, Canvas owns pixels, and DOM growth is
  constrained to controls and channels. The C2-B5 baseline-before-threshold
  procedure is appropriately explicit.
