# C3-B3 cross-source verification round 1

Date: 2026-08-31

Verdict: **PASS** for R16 cross-source equivalence. No candidate correction is
required. This review makes no accumulated-validation, acceptance, manifest,
checkpoint, or progress claim.

## Identity and scope audit

- Candidate commit: `970f9a79169733d20bc06db60e2c736a8234b7eb`.
- Candidate tree: `beffab143acd64eeb776c48f3138df17828a8079`.
- Candidate test SHA-256:
  `90754fb7a3d32da70c1526bde29dcc359d2a9e17ac21ea0a97273650f5bd1159`.
- Accepted semantic corpus SHA-256:
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`.
- Accepted option matrix SHA-256:
  `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`.
- The frozen B1 evidence contains reference
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`.
- B2 evidence-manifest SHA-256:
  `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`.
- `git diff-tree --no-commit-id --name-only -r <candidate>` reported only the
  R16 implementation test and its implementation review. There are no product,
  fixture, contract, or evidence changes in the candidate.

## Independent construction and challenge

The verifier does not import or copy the candidate test. It reads only the
accepted B1 transition corpus, independently interprets logical transitions,
and materializes packed eight-wire words. For every representative it then
crosses four production boundaries: direct `CaptureResult`, hand-built schema
1 replay import, separately hand-built schema 2 replay import, and hand-built
non-legacy CSV import with explicit ordered physical IDs, rate, trigger channel,
and edge. Neither replay uses the production replay serializer, and the CSV is
not emitted by the production CSV serializer. All four captures must have exact
rate, ordered IDs, trigger index, sample words, labels, and mapping before decode;
their private-decoder canonical JSON bytes must then be identical.

The six representatives are justified as the smallest channel-requirement
matrix, not as a substitute for semantic conformance:

1. UART RX optional direction.
2. UART TX optional direction.
3. SPI clock plus MOSI.
4. SPI clock plus MISO.
5. SPI clock plus CS plus data, including CS polarity/bit-order/word-width.
6. I2C's required SCL/SDA pair.

All three protocols and all four source forms are therefore exercised. Schema
1 fixes physical identity to D0-D7. The accepted UART TX witness is on D9, so
the verifier deliberately translates that logical TX transition stream to D4
for every source and freezes both the original `{tx: 9}` and R16 `{tx: 4}`
facts. This is a semantic wire remap, not truncation or a claim that D9 can be
represented by schema 1.

Hostile controls prove visibility of distinct schema-1/schema-2/CSV bytes;
sample mutation; logical-to-physical mapping; ordered channel IDs; rate;
trigger index; labels/mapping metadata; missing explicit CSV IDs; missing or
incorrect CSV rate; duplicate CSV triggers; and attempted serial/live capture.
The serial constructor is a fail-fast trap. Decode output changes are required
where the mutation is semantically decode-relevant; identity changes are
required for metadata/order changes that need not change decoded protocol data.

The six rows prove source materialization, while the other 57 of 63 accepted
timelines remain covered by the authoritative R13-R15 UART/SPI/I2C
implementation and independent verification conformance suites. Their semantic
coverage is not transferred to R16 or claimed from representative sampling.

## Commands and results

Commands were run from `Software/LogicAnalyzerPy`; each shell invocation used
the required `rtk` prefix.

- `.venv/bin/python -m pytest -q tests/verification/test_c3_b3_cross_source_equivalence.py`
  — 9 passed in 4.45s.
- `.venv/bin/python -m pytest -q tests/implementation/test_c3_b3_cross_source_equivalence.py tests/verification/test_c3_b3_cross_source_equivalence.py`
  — 17 passed in 8.56s.
- `.venv/bin/python -m pytest -q` over all six UART/SPI/I2C implementation and
  verification conformance modules — 404 passed in 50.93s.
- One combined `.venv/bin/python -m pytest -q` invocation over the candidate,
  verifier, all six conformance modules, implementation and black-box capture
  artifacts, wider-capture formats, B2 private host implementation, and all five
  B2 verifier generations — 801 passed in 100.97s.
- `.venv/bin/ruff check tests/verification/test_c3_b3_cross_source_equivalence.py`
  — all checks passed.
- `git diff --check` — exit 0, no whitespace errors.
- `sha256sum` reproduced the candidate, semantic, matrix, and B2 hashes above.

One verifier-local Ruff import-group finding was corrected before the final
run. No candidate/product finding was observed. The only round-1 additions are
this review and the independent verifier test; no approval or external
capability was needed.
