# C3-B5 implementation round 1 — final-packet candidate

## Scope and identity

- Implementor: `c3-b5-final-proof-implementor-1`.
- Governing contract/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Starting accepted B4 checkpoint: `9a8fc46ba4bc73cd007d678b85b6510bba0eeb87` /
  `62811eca22c8fd3de5403b5b6f853b187c938038`.
- B5 preflight HEAD/tree before this evidence-only delta:
  `2af1b177f84ec00cdc68e5c7e526be3328af022b` /
  `3dcfb3b7a565c8e0f57db22e05a7015850d75301`.
- Owned delta: this record, `tests/implementation/test_c3_b5_final_packet.py`, and
  `testdata/decoders/cycle3-raw/b5-final-measurements.json`.  No product,
  fixture, method, threshold, manifest, checkpoint, completion, or closure
  artifact was changed or created.

## Focused proof

`test_c3_b5_final_packet.py` independently validates the four accepted B1--B4
manifests with the Cycle 3 schema and their fixed SHA-256 values, checks their
checkpoint ordering and distinct role identities, and proves the union maps
R1--R25 and stopping conditions 1--14, 16, and 17.  It owns the remaining
condition-15 fresh-measurement check.  It also rejects a pre-created B5
manifest, B5 checkpoint, completion proof, or completion seal.

The accepted threshold source is exactly proposal
`b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0`, SHA-256
`98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`.
The test checks all 18 hard-enforcement identities have exact accept/reject
boundaries and that the SPI maximum remains 8 bits.  It records every raw
measurement, with no retry or outlier deletion, after exactly one unrecorded
warm-up per accepted UART, SPI, and I2C timeline, followed by five retained
repetitions each: three warm-up launches plus 15 retained launches equals 18
total launches.  The raw result binds the B1 method SHA-256
`f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341` and
semantic-fixture SHA-256
`34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`.

## Fresh observed maxima versus unchanged ceilings

| Ceiling | Observed max | Ceiling | Result |
| --- | ---: | ---: | --- |
| worker peak RSS bytes | 28,897,280 | 134,217,728 | pass |
| parent retained growth bytes | 57,344 | 33,554,432 | pass |
| successful parent total ns | 153,574,907 | 1,300,000,000 | pass |
| launch ns | 2,689,733 | 50,000,000 | pass |
| reap ns | 22,638 | 50,000,000 | pass |
| child load ns | 9,062,265 | 100,000,000 | pass |
| child import ns | 91,613,460 | 100,000,000 | pass |
| child decode ns | 2,347,729 | 100,000,000 | pass |
| timeout cleanup total ns | 0 | 5,500,000,000 | pass (success-path observation) |
| terminate-to-reap ns | 0 | 300,000,000 | pass (success-path observation) |
| kill-to-reap ns | 0 | 50,000,000 | pass (success-path observation) |

Environment was Darwin/x86_64 CPython 3.12.13, the characterized macOS
environment class.  The raw file records `warmup=3`, `retained=15`, and
`total=18`, and retains one row for every decoder/repetition pair.

## Commands and results

- `C3_B5_WRITE_MEASUREMENTS=1 .venv/bin/python -m pytest -q tests/implementation/test_c3_b5_final_packet.py` — `1 failed, 1 passed` initially; the failure correctly exposed that condition 15 has no inherited B1--B4 manifest mapping.  The test was narrowed to make condition 15 B5-owned.
- `.venv/bin/python -m pytest -q tests/implementation/test_c3_b5_final_packet.py` — `2 passed`.
- `C3_B5_WRITE_MEASUREMENTS=1 .venv/bin/python -m pytest -q tests/implementation/test_c3_b5_final_packet.py` after C3B5-V001 correction — `2 passed`; it regenerated exactly 18 launches (three unrecorded warm-ups and 15 retained observations).
- `git diff --check` — pass.

The larger inherited B2/B3/B4 focused suite was launched after this focused
gate; its final result is deliberately not claimed by this implementation
record and must be recorded by the accumulated-validation owner.

## Files and digests

- `tests/implementation/test_c3_b5_final_packet.py`:
  `8914ca125aa2ed132f7eabdff8d148045132bce447222d75ac9860b0175689f6`.
- `testdata/decoders/cycle3-raw/b5-final-measurements.json`:
  `980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e`.

## Findings and disposition

`C3B5-V001` (the original collector made five unrecorded repetitions per
protocol) is closed by the minimal loop correction and explicit raw
`warmup=3`/`retained=15`/`total=18` assertion.  No earlier-owner defect,
threshold variance, prohibited action, or authority need was found.  The three cleanup ceilings are represented by successful-path
zero observations here; their hostile timeout/terminate/kill enforcement
remains inherited B2 evidence and requires a fresh B5 verifier/accumulated
audit before any final claim.  This is an evidence candidate only: verdict
`candidate-not-accepted`.  It authorizes no manifest, checkpoint, hosted
dispatch, completion proof, closure audit, seal, publication, conveyance, or
Cycle 4 work.
