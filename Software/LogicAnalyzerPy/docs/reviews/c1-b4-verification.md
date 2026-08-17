# C1-B4 independent verification

- Verifier: `/root/c1_b4_verification`
- Verdict: **changes_required**
- Scope reviewed: normal D0--D7 capture request/receive, deterministic CSV and
  provisional replay artifacts, transactional output behavior, CLI stream/exit
  behavior, and the physical-smoke acceptance procedure. No serial port or
  physical hardware was accessed by this verifier.

## Provenance and independent expectations

The literal rising/falling requests are the accepted source-derived vectors in
`tests/verification/golden.py`; the response grammar/bounds are from the
settled BATCH_EXECUTION capture and receive contracts. CSV expectations are a
separately written five-sample capture (`00 01 81 02 ff`) with pre=2,
post=3, rate=100 Hz, and D0 trigger. The expected artifact bytes, trigger-row,
time-zero, last-pre-trigger time, and D0/D7 values are hard-coded in
`tests/verification/test_c1_b4_capture_artifacts_blackbox.py`, rather than
being calculated through production exporters.

The safe physical setup is limited to the C1-B3 operator record: integrated
LogicAnalyzerV2 protection board, 3.3 V VRef and source, common labelled GND,
and labelled input `1` confirmed as logical D0/Pico 2 GPIO2. This review does
not treat that record as a C1-B4 waveform observation.

## Passing non-hardware evidence

- The independent verifier suite passes 17 tests. It covers literal rising and
  falling request bytes; count-first rejection before a payload read; exact
  `uint8` width/count; exact CSV bytes/LF/self-timing; `allow_pickle=False`
  NPY reload; canonical metadata; exact samples; replay member restrictions;
  collision, force, fsync, path alias, partial-backup, rename rollback, and
  post-commit backup-cleanup behavior; explicit-port-only CLI behavior; and
  stderr-only validation failures.
- The accumulated gate passes: Ruff, mypy, `pytest -m "not hardware"` (181
  passed; one expected duplicate-ZIP construction warning), module CLI help,
  and `git diff --check`.
- Post-commit backup cleanup is intentionally best-effort: if deletion of a
  backup fails after *both* new final files are atomically installed, the
  command remains successful and preserves the two new finals; an orphaned
  `.bak` is safer than an unsafe rollback. Normal success removes backups.

## Findings requiring disposition before acceptance

1. **Physical C1-B4 evidence is absent.** The required opt-in capture has not
   yet shown 6144 returned 8-bit samples, a nonconstant D0 trace, an observed
   rising transition, acceptable measured frequency, artifact validation, and
   port closure. Run the documented explicit command and retain a sanitized
   evidence file before marking the batch complete.

2. **The documented 2% frequency tolerance is not defensibly derived from
   this fixture.** At 100,000 sample/s and 1,000 Hz there are 100 samples per
   period. The 2,048+4,096=6,144-sample window is 61.44 ms, roughly 61.44
   periods. Using first/last same-polarity D0 transitions spans about 6,000
   samples (about 60 periods); even a conservative two-sample endpoint error
   is at most 2/6000 = 0.0334%. A tolerance must state a source-stability
   allowance supplied by the operator and add its bounded quantization term
   (for example, source allowance + 0.05%), rather than accepting the
   unexplained 2% floor. The sanitized evidence should also record the number
   of requested-polarity D0 transitions used by the estimate, not only a
   boolean `edge_observed`.

No scope expansion is recommended: recovery/cancellation, fixed-level wires,
and a second post-recovery capture remain C1-B5.
