# Cycle 1 completion proof

## Accepted candidate

- Tested implementation commit: `aeba415939d2f3d3f6d21852d3b446c4b6fef69b`
- Tested implementation tree: `ec839c5646c09fbab5403ddde62304a2049eac0a`
- Environment: macOS 15.7.7 (24G720), x86_64, Python 3.12.13
- Dependency identity: `requirements-dev.lock` SHA-256
  `931e790473b3ca014c248cdd3b665389ddb3f24425c4320124c40f1a608ab726`
- Independent final verdict: `pass` in
  `docs/reviews/c1-b5-acceptance.md`

The implementation candidate had a clean tracked worktree during the physical
recovery proof. Raw physical evidence was untracked and was inspected by the
acceptance agent before being summarized. Subsequent changes are evidence and
checkpoint records only; no implementation changed after the proof.

## Stopping-condition checklist

| # | Condition | Evidence | Result |
| --- | --- | --- | --- |
| 1 | Python 3.12 installation and CLI help | Fresh venv; hash-required lock install; `--no-build-isolation --no-deps -e .`; `pip check`; module help | Pass |
| 2 | Static and all non-hardware validation | Ruff; mypy over 17 source files; 201 non-hardware tests | Pass |
| 3 | Provenance-tagged V2 fixtures | C1-B1/B2 identity and literal rising/falling normal-request fixtures and provenance review | Pass |
| 4 | Adverse fake/replay behavior | 162 independent verifier tests cover fragmentation, malformed data, finite timeouts, disconnect, cleanup, hostile archives, and recovery | Pass |
| 5 | Real V2 identity and periodic capture | C1-B3 reports `LOGIC_ANALYZER_PICO_2_V6_0`; C1-B4 captures 6144 samples from rising D0 and measures 1000.0 Hz | Pass |
| 6 | Deterministic CSV and safe replay | C1-B4 acceptance securely reloads NPZ and reconstructs the 190739-byte CSV byte-for-byte | Pass |
| 7 | Timeout/cancellation recovery and second capture | C1-B5 fixed-low D1 no-trigger attempt; exact one-`ff` tested path; bounded drain; close/reopen/re-identify; recovered 6144-sample D0 capture at 1001.710236989983 Hz | Pass |
| 8 | Final evidence and progress record | Five checkpoint manifests, independent reviews, sanitized hardware observations, this record, and `docs/orchestration-progress.md` | Pass |
| 9 | C# and firmware rollback paths preserved | Existing `Software/LogicAnalyzer/` and `Firmware/LogicAnalyzer_V2/` remain present; no Cycle 1 product commit modifies them | Pass |

## Validation results

The final clean Python 3.12 environment passed:

```text
python -m pip install --require-hashes -r requirements-dev.lock
python -m pip install --no-build-isolation --no-deps -e .
python -m pip check                                      pass
python -m ruff check .                                  pass
python -m mypy src                                      pass (17 files)
python -m pytest tests/verification/test_c1_b5_recovery_blackbox.py -q
                                                         pass (10 tests)
python -m pytest tests/verification -q                  pass (162 tests)
python -m pytest -m "not hardware" -q                  pass (201 tests)
python -m pico_logic_analyzer --help                    pass
git diff --check                                        pass
```

The only warning is intentionally emitted while a verifier constructs a
duplicate-member ZIP attack fixture. The production replay loader rejects that
archive.

## Physical results

- Board/front end: Raspberry Pi Pico 2 in the integrated checked-in
  LogicAnalyzerV2 protection design, VRef 3.3 V, common analyzer ground.
- Firmware identity: `LOGIC_ANALYZER_PICO_2_V6_0`; latest checked-in V2 firmware
  built with `BOARD_TYPE=BOARD_PICO_2`.
- Periodic input: labeled input `1`, logical D0, GPIO2, protected 3.3 V 1 kHz.
- Idle input: labeled input `2`, logical D1, GPIO3, directly connected to
  analyzer `GND` and operator-confirmed fixed low.
- C1-B4: 100000 samples/s, rising D0, 2048 pre/4096 post, 6144 samples,
  nonconstant waveform, 41 rising transitions, measured 1000.0 Hz.
- C1-B5: wait 0.25 s on fixed-low D1, recover with the single characterized
  `0xFF` path under a 3 s/4096-byte bound, close/reopen/re-identify, then capture
  rising D0 without a power cycle. Result: 6144 samples, 42 rising transitions
  over 4093 samples, 1001.710236989983 Hz within 2.0488639% tolerance.
- The committed port value is always `<PORT_SUPPLIED>`.
- No firmware flash, bootloader entry, Wi-Fi change, power cycle, or persistent
  device-management action occurred during Cycle 1 execution.

## Evidence manifests

| Checkpoint | Tested commit | Manifest SHA-256 |
| --- | --- | --- |
| C1-B1 | `476c075891e50e5525b3aa3acc3430415ff018d3` | `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc` |
| C1-B2 | `37bdd50da4c85f32eb0055ca2a34be92e7edb2f0` | `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af` |
| C1-B3 | `c71db28f17bd2ba8b68542b8514c383610bb7635` | `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598` |
| C1-B4 | `53bfc2184c825296da20a644777729096cff3c1f` | `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead` |
| C1-B5 | `aeba415939d2f3d3f6d21852d3b446c4b6fef69b` | `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d` |

The final evidence audit removed one mutable C1-B3 test path from that
checkpoint's artifact list after C1-B4 legitimately replaced its obsolete
"capture unimplemented" assertion. C1-B3 retains its immutable physical
observation and independent review artifacts; its tested commit/tree and
verdict are unchanged.

The C1-B5 physical summary is
`testdata/evidence/c1-b5-recovery-observation.json` (SHA-256
`252125b3c7daf504e3cd53222bf8fa48a26000014af39dfeb26902bf0585d8d0`)
and its sanitized command result is
`testdata/evidence/c1-b5-recovery-smoke.json` (SHA-256
`44a7bffc0bcc7c415ba8fa09efb26624853dce26833216d78d408b9c45907815`).

## Known limitations and deferred work

- Cycle 1 supports only normal eight-channel D0-D7 captures and a narrow CLI;
  no GUI, decoders, wider modes, TCP/Wi-Fi, `.lac`, or release packaging.
- The replay schema is explicitly provisional.
- C1-B4 observed the physical rising transition one sample before the settled
  logical trigger marker/time-zero sample. This alignment issue is recorded for
  later protocol/firmware investigation and is not represented as exact
  electrical-edge timing.
- The physical recovery artifact is a sanitized result, not a timestamped raw
  serial trace. Independent literal fake-transport tests prove exact one-byte
  ordering against the same frozen command path.
- Firmware performance or protocol improvements require a separately reviewed
  later cycle. Firmware remained fixed throughout Cycle 1.

Cycle 2 has not begun.
