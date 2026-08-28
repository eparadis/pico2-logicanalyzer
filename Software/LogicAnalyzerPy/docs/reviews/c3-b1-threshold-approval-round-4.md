# C3-B1 operator-approved decoder limits — round 4

## Decision and immutable subject

- Operator decision: `approved`.
- Approved at: `2026-08-28T18:53:33Z`.
- Operator statement:
  `I approve the exact committed round-4 threshold values in proposal b680aa5.`
- Exact proposal commit/tree:
  `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` /
  `e8661f094ba0423ca08055ea785bbfcde8554d71`.
- Proposal path:
  `testdata/decoders/cycle3/threshold-proposal-round-4.json`.
- Proposal SHA-256:
  `98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`.
- Rationale SHA-256:
  `58ef6451033603989617b195ab2d0184c75e243cbcad3ec99df3b2d41027242c`.
- Fresh verification pass:
  `46d57e482c330fca945c0e2bb3ca35cc1a95d3a1`.
- Accumulated-validation pass:
  `62b67fe03da96a7baae89c66859e6b67d66664ee`.
- Fresh acceptance pass:
  `f28643bc69992d60fcf51d289ba5c4fb8e5dcc73`.
- Acceptance-record SHA-256:
  `3a9208b16bc2f3f3a89c8669711f1ddc0778055f1b238dcdc010c29d8e10fb2d`.

The operator explicitly approved the complete exact round-4 proposal presented
as 29 committed threshold values. No value is amended, omitted, inferred, or
rebased by this record. The proposal remains immutable with status
`proposal-not-approved`; this separate record owns the operator decision.

The accepted replacement fixture and runner invalidated round-3 proposal
`b260d9ecc0e74ed2502dda89beebb851ddfedb77` and approval commit
`63fdfee87159251cdf525eb608340e6bc08ad010`. That earlier approval transfers
no authority. This decision applies only to exact round-4 proposal `b680aa5`.

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
Macmini8,1, Python 3.12.13 environment class. They are regression gates, not
real-time or cross-platform guarantees.

| ID | Inclusive maximum | First rejected |
| --- | ---: | ---: |
| `worker_peak_rss_bytes` | 134,217,728 bytes | 134,217,729 |
| `parent_retained_growth_bytes` | 33,554,432 bytes | 33,554,433 |
| `successful_parent_total_ns` | 1,300,000,000 ns | 1,300,000,001 |
| `launch_ns` | 50,000,000 ns | 50,000,001 |
| `reap_ns` | 50,000,000 ns | 50,000,001 |
| `child_load_ns` | 100,000,000 ns | 100,000,001 |
| `child_import_ns` | 100,000,000 ns | 100,000,001 |
| `child_decode_ns` | 100,000,000 ns | 100,000,001 |
| `timeout_cleanup_total_ns` | 5,500,000,000 ns | 5,500,000,001 |
| `terminate_to_reap_ns` | 300,000,000 ns | 300,000,001 |
| `kill_to_reap_ns` | 50,000,000 ns | 50,000,001 |

Exactly 26 numeric values are unchanged from round 3. The three changed values
are:

- `parent_retained_growth_bytes`, from 16,777,216 to 33,554,432 bytes,
  derived as `next_power_of_two(1,757,184 * 16)`;
- `successful_parent_total_ns`, from 1,000,000,000 to 1,300,000,000 ns,
  derived as `ceil_to_100ms(156,549,612 * 8)`; and
- `launch_ns`, from 100,000,000 to 50,000,000 ns, derived as
  `ceil_to_50ms(6,008,633 * 8)`.

## Authority and limitations

This decision freezes the exact proposal as an input to the replacement final
C3-B1 candidate and later B2/B3/B5 enforcement and regression proof. It does
not by itself create product enforcement, accept a final B1 candidate, create
a B1 manifest or checkpoint, authorize a silent increase, broaden the
macOS-only claim, authorize a distributable artifact, or start Cycle 4.

Any amendment requires a new immutable proposal, fresh independent
verification, complete accumulated validation, independent acceptance, and
renewed explicit operator approval.
