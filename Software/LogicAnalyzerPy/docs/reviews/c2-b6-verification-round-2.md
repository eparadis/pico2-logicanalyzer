# C2-B6 verification round 2

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T21:56:22Z`.
- Correction candidate: `04988050711869307a1a136cf5686cd88ef895d7`;
  tree `1254a119aaae532a1181058f4f48527c8ba5d47c`.
- Implementation record: commit `a5ef6b1`, SHA-256
  `5fd8e9293cfef445cb520e463242169bb84c283658ce49fdbba1dc0b74896792`, evidence only.
- Verdict: `changes_required`.

## Findings and dispositions

1. `C2B6-V001` — open. The correction rejects all five prior mutation classes and chains the
   checker automatically after `benchmark:b6`, but it silently weakens one operator-approved
   deterministic resource ceiling. The approved B5 record requires every waveform request to
   span at most 100,000 samples. The B6 benchmark report, benchmark producer, and checker all
   freeze `waveform_request_max_span_samples` as `393216`. The checker therefore accepts a
   declared bound almost four times the approved maximum and rejects correction back to the
   approved value. The current viewer still happens to request at most 100,000; the defect is
   that B6 enforcement attests and enforces the wrong ceiling. Restore exactly 100,000 and bind
   it to observed requests without rebasing the approved threshold.
2. `C2B6-V002` — closed by deterministic correction audit. The strengthened native test now
   asserts trigger and cursor sample/time, applicable high values on D0/D8/D16/D23 across all
   widths, explicit LSB-first channel selection, ordered transition rows restricted to expected
   0/15 encodings, exact exported CSV header/value bytes, 31 distinct-D23-strobe rows with the
   expected three-bit value, reopen, second capture, nondisclosure, and shutdown. These checks
   match the independently inspected round-one physical artifacts. A further device/browser
   rerun was intentionally not performed after the surviving V001 failure; it remains required
   on the next corrected candidate.
3. `C2B6-V003` — closed. The durable evidence now binds the exact physically exercised product
   commit/tree and the six independently verified capture artifact digests plus recovery digest.
   It records exact dtypes, masks/projections, edge counts, high-bit zero, CSV/NPZ equivalence,
   measured recovery frequency, reidentify/close/reopen/second capture, and nondisclosure. The
   correction changes only enforcement/tests/evidence metadata, not driver/API/viewer/assets,
   so reuse of the immutable physical artifacts is valid.

## Independent falsification and validation

- Five fresh mutations—viewport, fixture digest, raw interaction timing, required load role,
  and production asset manifest digest—were rejected 5/5. Canonical enforcement passed.
- Focused threshold/evidence/native-harness/OpenAPI tests: 16 passed.
- Fresh automatic `benchmark:b6` ran Playwright and its chained checker successfully. Independent
  recomputation gave p95 load `444.4`, interaction `331.3`, representative bus `146.0`/`67.4`,
  and worst bus `406.2`/`153.8` ms, all within approved timing ceilings. Generated report
  SHA-256 was `5261ca1651202680bc9f29f6d6b4a94c3e450e7d57df7522789008ac6e750633`;
  residue was removed. Its bound object reproduced the incorrect 393,216 value, confirming the
  finding on the actual automatic path.
- Clean accumulated nonhardware Python: 378 passed, 2 documented sandbox-loopback skips,
  106 warnings. Ruff, strict mypy over 21 source files, dependency, B4/B6 OpenAPI, production
  assets, and diff checks passed.
- Node 22 lint/typecheck passed; Vitest 3 files/5 tests passed; production build transformed
  29 modules and reproduced committed assets.

Corrected durable identities match the candidate: enforcement checker
`4e1748a3ef5ae9f463a089a5faa1c8d856c07d7c9c96d4e9318ab968afba759d`, report
`9d2d360dd86ce75c7f89005f7bc3e4de21ec0d52ecb956f1abc955a42c632f54`, implementation evidence
`dfe1e7504e3289e21a556a423d1c5d417e3072bdf5be3156557e279567864a6a`, native test
`7783e48969366651bc54b339f3dcfa20d037c2e253cad531037a3b01a69e1bd9`, B6 benchmark
`68dd480c3e8df3cc0409053c81834cb082e64243d22e08d2217a675d63e18265`, and package manifest
`edc8456f4503c272d0aa49b7282d79ed45a3745e250dd0388a7140f758434d00`.

## Scope

No product file, prior evidence, threshold approval, contract, progress, manifest, firmware,
wiring, persistent device state, public service, packaging, .NET surface, acceptance,
completion record, or Cycle 3 work was changed. No threshold was rebased or newly proposed.

Open findings: `C2B6-V001`. Closed findings: `C2B6-V002`, `C2B6-V003`. Deferred findings: none.
