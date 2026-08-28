# C3-B1 operator-approved decoder limits — round 3

## Decision and immutable subject

- Operator decision: `approved`.
- Approved at: `2026-08-28T12:57:17Z`.
- Operator statement:
  `I approve the exact committed round-3 threshold values in proposal b260d9e`.
- Exact proposal commit/tree:
  `b260d9ecc0e74ed2502dda89beebb851ddfedb77` /
  `8a65628df5ba63727e8305e901b9954fe0bec7e5`.
- Proposal path:
  `testdata/decoders/cycle3/threshold-proposal-round-3.json`.
- Proposal SHA-256:
  `7fb9e88aaa5888e1a3133ff2234253bdfbbc4bd7151fc3a3be3c387dd619f510`.
- Rationale SHA-256:
  `8ea67712009a8a730c6eba8834e063179b709f07dfcdc5ffd7e9a55f6a93c58b`.
- Fresh verification pass:
  `92de4e6c9c57ba258f2991c92c3e1569cf659ad4`.
- Accumulated-validation pass:
  `c3cc27417fdf324723f6643deb863a4933b29537`.
- Fresh acceptance pass:
  `d922ba33ba81714417f5ce18eb7267bd7c5850a3`.
- Acceptance-record SHA-256:
  `ec16e5549b4c150582a773cfd18c6b0012c72999733a824cddd3d4bf06de26c7`.

The operator explicitly approved the complete exact round-3 proposal presented
as 29 committed threshold values. No value is amended, omitted, inferred, or
rebased by this record. The proposal remains immutable with status
`proposal-not-approved`; this separate record owns the operator decision.

The corrected fixture and raw-baseline chain superseded round-2 proposal
`395646fa1172382928581d7266723f5b044cf8f2` and approval commit
`b6d904064ab7b9e195eedded1c55efc306eeb925`. That earlier approval transfers
no authority. This decision applies only to exact round-3 proposal `b260d9e`.

## Approved hard-enforcement limits

Each value is an inclusive maximum; the first rejected integer is value + 1.

| ID | Inclusive maximum | First rejected |
| --- | ---: | ---: |
| `input_samples` | 65,536 samples | 65,537 |
| `request_bytes` | 4,194,304 bytes | 4,194,305 |
| `wall_deadline_ms` | 5,000 ms | 5,001 |
| `terminate_grace_ms` | 250 ms | 251 |
| `worker_address_space_bytes` | 68,719,476,736 bytes | 68,719,476,737 |
| `recursion_limit` | 320 frames | 321 |
| `output_records` | 16,384 records | 16,385 |
| `encoded_bytes` | 2,097,152 bytes | 2,097,153 |
| `decoded_bytes` | 2,097,152 bytes | 2,097,153 |
| `stdout_bytes` | 65,536 bytes | 65,537 |
| `stderr_bytes` | 65,536 bytes | 65,537 |
| `diagnostic_bytes` | 8,192 bytes | 8,193 |
| `text_bytes` | 524,288 bytes | 524,289 |
| `binary_bytes` | 262,144 bytes | 262,145 |
| `nested_depth` | 32 levels | 33 |
| `nested_items` | 16,384 items | 16,385 |
| `retained_result_bytes` | 8,388,608 bytes | 8,388,609 |
| `spi_max_word_size_bits` | 8 bits | 9 |

## Approved exact-candidate regression ceilings

These ceilings apply to the characterized macOS 15.7.7 build 24G720, x86_64,
Python 3.12.13 environment class. They are regression gates, not real-time or
cross-platform guarantees.

| ID | Inclusive maximum | First rejected |
| --- | ---: | ---: |
| `worker_peak_rss_bytes` | 134,217,728 bytes | 134,217,729 |
| `parent_retained_growth_bytes` | 16,777,216 bytes | 16,777,217 |
| `successful_parent_total_ns` | 1,000,000,000 ns | 1,000,000,001 |
| `launch_ns` | 100,000,000 ns | 100,000,001 |
| `reap_ns` | 50,000,000 ns | 50,000,001 |
| `child_load_ns` | 100,000,000 ns | 100,000,001 |
| `child_import_ns` | 100,000,000 ns | 100,000,001 |
| `child_decode_ns` | 100,000,000 ns | 100,000,001 |
| `timeout_cleanup_total_ns` | 5,500,000,000 ns | 5,500,000,001 |
| `terminate_to_reap_ns` | 300,000,000 ns | 300,000,001 |
| `kill_to_reap_ns` | 50,000,000 ns | 50,000,001 |

Exactly 28 numeric values are unchanged from round 2. The only changed value is
`successful_parent_total_ns`, from 900,000,000 to 1,000,000,000 ns, derived as
the accepted raw maximum 123,103,531 ns multiplied by eight and rounded upward
to the next 100,000,000-ns quantum.

## Authority and limitations

This decision freezes the exact proposal as an input to the replacement final
C3-B1 candidate and later B2/B3/B5 enforcement and regression proof. It does
not by itself create product enforcement, accept a final B1 candidate, create
a B1 manifest or checkpoint, authorize a silent increase, broaden the
macOS-only claim, authorize a distributable artifact, or start Cycle 4.

Any amendment requires a new immutable proposal, fresh independent
verification, complete accumulated validation, independent acceptance, and
renewed explicit operator approval.
