# C3-B1 operator-approved decoder limits

## Decision and immutable subject

- Operator decision: `approved`.
- Approved at: `2026-08-27T16:48:28Z`.
- Operator statement: `I approve the exact round-2 threshold value`.
- Exact proposal commit/tree:
  `395646fa1172382928581d7266723f5b044cf8f2` /
  `6857f9a67ff70220e6d6b2a11f9ca450005c8321`.
- Proposal path:
  `testdata/decoders/cycle3/threshold-proposal-round-2.json`.
- Proposal SHA-256:
  `94882b710f2d569c0ea0535366a0c1c3df3514aa20a18e4cd35f652177458ec2`.
- Rationale SHA-256:
  `18a6b58a2b05f7dd7aa302a6e1bb4d074621440648a2e735a1d16d9708b209b0`.
- Fresh verification pass: `1cdedcae57e6233010410172196b23f6167ee675`.
- Accumulated-validation pass: `0d00fe4b88a1192b893afbf8e32c39bd6493b2fd`.
- Fresh acceptance pass: `91de257667fa819dd1c183d4ec112f106ed6742a`.

The operator explicitly approved the complete exact round-2 proposal presented
as 29 committed threshold values. The singular wording `threshold value` does
not select one entry: it directly answered the request to approve the exact
round-2 threshold values as a whole. No value is amended, omitted, inferred,
or rebased by this record.

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
| `successful_parent_total_ns` | 900,000,000 ns | 900,000,001 |
| `launch_ns` | 100,000,000 ns | 100,000,001 |
| `reap_ns` | 50,000,000 ns | 50,000,001 |
| `child_load_ns` | 100,000,000 ns | 100,000,001 |
| `child_import_ns` | 100,000,000 ns | 100,000,001 |
| `child_decode_ns` | 100,000,000 ns | 100,000,001 |
| `timeout_cleanup_total_ns` | 5,500,000,000 ns | 5,500,000,001 |
| `terminate_to_reap_ns` | 300,000,000 ns | 300,000,001 |
| `kill_to_reap_ns` | 50,000,000 ns | 50,000,001 |

## Authority and limitations

This decision freezes the exact proposal as an input to the final C3-B1
candidate and later B2/B3/B5 enforcement and regression proof. It does not by
itself create product enforcement, accept a B1 final candidate, authorize a
silent increase, broaden the macOS-only claim, authorize a distributable
artifact, or start Cycle 4. Any amendment requires a new immutable proposal,
fresh independent verification, complete accumulated validation, independent
acceptance, and renewed explicit operator approval.
