# C3-B1 threshold-proposal acceptance — round 4

## Identity, subject, and verdict

- Acceptance identity: `c3-b1-threshold-acceptance-replacement-1`
  (`/root/c3_b1_threshold_accept_r4`), acting only in the independent
  acceptance lane.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact round-4 proposal candidate/tree:
  `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` /
  `e8661f094ba0423ca08055ea785bbfcde8554d71`.
- Fresh verification descendant/tree:
  `46d57e482c330fca945c0e2bb3ca35cc1a95d3a1` /
  `4dc95bc35142c920cc162550e27511279fbbe828`.
- Accumulated-validation descendant/tree:
  `62b67fe03da96a7baae89c66859e6b67d66664ee` /
  `82a009d7bc89518f784787adaa74abf1306de6a8`.
- Verdict: `pass`.

This was a static acceptance audit. I did not reproduce the raw baseline,
execute a decoder or runner, enforce a threshold, amend any input, or make an
operator decision. I wrote only this record.

## Acceptance findings

1. **Pass — ancestry, candidate scope, ordering, and role separation.** The
   accepted corrected-fixture raw chain is ordered exactly as raw candidate
   `d0d9dbe87f7841f09f261556de0909475e048b95`, independent verification
   `17397360770f3aab7d79a479a53499b50a1245cd`, root accumulation
   `7295e4d9472632f92bb22e6a06e001609b2590e6`, and independent acceptance
   `72168f4ca0f90e16e99a72537e159818a434dea1`. The proposal candidate follows
   that chain and adds exactly the round-4 proposal JSON and rationale. The
   fresh verifier and accumulated record then follow in the required order.
   Proposal author `c3-b1-threshold-proposer-replacement-1`, verifier
   `c3-b1-threshold-verifier-replacement-1`, the primary orchestrator as
   accumulated-validation owner, and this acceptance identity are distinct.
   No product, raw, fixture, runner, approved-limit, final-B1, manifest,
   checkpoint, B2, or downstream path is part of the proposal delta.

2. **Pass — artifact and evidence identity is closed.** Independently
   recomputed SHA-256 values are:

   - proposal:
     `98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`;
   - rationale:
     `58ef6451033603989617b195ab2d0184c75e243cbcad3ec99df3b2d41027242c`;
   - verifier test:
     `719acc7d4e474958d36bfc8d08c63f7dcce7dc97faf41b9d188e801bd33e54d6`;
   - verification record:
     `2a5d8ee0ca91b713bbd21f5dbffe39ebeed953d7eb411ce96d97540066c57433`;
   - accumulated record:
     `5e1261261f7ae673cf2dc8a8ae056fadf06deb756cf6289c609e32f565d9390b`.

   The machine-readable proposal is canonical newline-terminated JSON with
   exact schema `cycle3-threshold-proposal/v1`, round 4, and status
   `proposal-not-approved`. It binds accepted fixture `3af6b9f...`, accepted
   runner `380d5dd...`, runner acceptance `01f059c...`, the complete corrected
   raw chain, the exact macOS 15.7.7 build 24G720 / x86_64 / Macmini8,1 /
   Python 3.12.13 environment, and all six raw/cap digests.

3. **Pass — all 29 exact values, formulas, boundaries, and caps recompute.**
   There are exactly 29 unique IDs with no missing, extra, or duplicate ID.
   Every proposed value is a positive non-boolean integer, every `accept`
   equals its value, and every `reject` is value plus one. The exact inclusive
   values are:

   | ID | Proposed value |
   | --- | ---: |
   | `input_samples` | 65,536 |
   | `request_bytes` | 4,194,304 |
   | `wall_deadline_ms` | 5,000 |
   | `terminate_grace_ms` | 250 |
   | `worker_address_space_bytes` | 68,719,476,736 |
   | `worker_peak_rss_bytes` | 134,217,728 |
   | `parent_retained_growth_bytes` | 33,554,432 |
   | `recursion_limit` | 320 |
   | `output_records` | 16,384 |
   | `encoded_bytes` | 2,097,152 |
   | `decoded_bytes` | 2,097,152 |
   | `stdout_bytes` | 65,536 |
   | `stderr_bytes` | 65,536 |
   | `diagnostic_bytes` | 8,192 |
   | `text_bytes` | 524,288 |
   | `binary_bytes` | 262,144 |
   | `nested_depth` | 32 |
   | `nested_items` | 16,384 |
   | `retained_result_bytes` | 8,388,608 |
   | `successful_parent_total_ns` | 1,300,000,000 |
   | `launch_ns` | 50,000,000 |
   | `reap_ns` | 50,000,000 |
   | `child_load_ns` | 100,000,000 |
   | `child_import_ns` | 100,000,000 |
   | `child_decode_ns` | 100,000,000 |
   | `timeout_cleanup_total_ns` | 5,500,000,000 |
   | `terminate_to_reap_ns` | 300,000,000 |
   | `kill_to_reap_ns` | 50,000,000 |
   | `spi_max_word_size_bits` | 8 |

   Recomputed maxima cover all 315 retained successful snapshot rows and all
   50 retained hostile primary rows, never medians or selected cases. All
   exact derivation strings, raw maxima, kinds, units, experiment-cap
   identities, and hard-cap relations match. The parent-success ceiling fits
   inside the wall deadline; timeout cleanup fits deadline plus grace plus
   250 ms; terminate-to-reap fits grace plus 50 ms; and SPI 8 is accepted
   while 9 is the first rejected value.

4. **Pass — the exact 26 unchanged / three changed comparison is truthful.**
   Direct ID-to-value comparison with round 3 finds exactly 26 unchanged
   values and three changes:

   - `parent_retained_growth_bytes`: 16,777,216 to 33,554,432;
   - `successful_parent_total_ns`: 1,000,000,000 to 1,300,000,000; and
   - `launch_ns`: 100,000,000 to 50,000,000.

   The two increases and one decrease follow exactly from the accepted raw
   maxima and unchanged formulas:

   ```text
   next_power_of_two(1,757,184 * 16) = 33,554,432
   ceil_to_100ms(156,549,612 * 8) = 1,300,000,000
   ceil_to_50ms(6,008,633 * 8) = 50,000,000
   ```

5. **Pass — prior proposal and operator approval transfer no authority.** The
   proposal binds superseded round-3 proposal
   `b260d9ecc0e74ed2502dda89beebb851ddfedb77` and superseded operator record
   `63fdfee87159251cdf525eb608340e6bc08ad010`. The accepted replacement fixture
   and runner invalidated their chain. Numerically unchanged entries and the
   prior explicit decision are historical comparison evidence only. Both the
   proposal and rationale require a new explicit operator decision on this
   exact committed round-4 proposal.

6. **Pass — independent verification is complete and non-vacuous.** The
   verifier statically recomputes the closed schema, canonical status, exact
   evidence identities and digests, all retained-row maxima, all 29 formulas,
   kinds, units, boundaries, cap relationships, cross-limit constraints, and
   the exact 26/3 prior-round comparison. Its 30 cases comprise one complete
   positive audit, 24 proposal mutations, and five direct cross-limit
   mutations. They reject missing, extra, and duplicate IDs; booleans,
   floats, zero, and negatives; changed maxima, formulas, caps, units, kinds,
   and boundaries; weakened hard caps; approved status; evidence, commit, or
   environment substitution; a false comparison; and deadline, cleanup,
   terminate, or SPI contradictions. My focused static rerun passed all 30
   tests in 0.50 seconds.

7. **Pass — accumulated validation is complete and candid.** The exact
   41-module Python gate collected 608 tests and completed with 602 passed,
   six inherited classified skips, and 106 warnings. It included the complete
   486-launch raw reproduction and all 30 proposal-verifier cases, while
   excluding superseded routes and all threshold-enforcement, product,
   final-candidate, B2, and downstream work. Dependency consistency,
   whole-project Ruff, strict mypy over 28 source files, fixture and binding
   checks, six Cycle-2 validators, CLI help, Node lint/type/test/build/assets,
   and isolated browser/performance gates also passed. Reproduction-report
   SHA-256 is
   `41c6b6f84306ebe6a3e468b8b3f66af37c6efe5073fa44c6792840c8926cd6b1`;
   performance-report SHA-256 is
   `641e62cc1722461dcbf5195ac19174851b82dd292c3de6592eb4f54ad44141d8`.

8. **Pass — the invalid combined-browser attempt is disclosed and contributes
   no accepted result.** The exploratory command concurrently combined the
   maximum-width, live, and shell files against shared server state. Although
   three tests passed, maximum-width observed `error`; that command shape is
   explicitly rejected as a gate and transfers nothing. The established
   isolated reruns subsequently passed maximum-width 1/1 and live/shell 3/3,
   followed by the isolated B6 performance test and accepted B5 checker. Only
   those isolated reruns support the accumulated browser result.

9. **Pass — scope and cleanup remain bounded.** This acceptance used only Git,
   SHA-256, static document/JSON inspection, and the focused verifier suite.
   It did not execute raw reproduction, a decoder, runner/worker request,
   threshold enforcement, product/final behavior, browser, hardware, network,
   external runtime, publication, B2, or downstream work. No finding remains
   open.

## Authority and next gate

This pass makes the exact committed round-4 proposal eligible for an explicit
operator decision. It does **not** approve or enforce any numeric value. The
next required gate is explicit operator approval or amendment of the exact
committed round-4 values. An amendment creates another immutable proposal and
repeats verification, accumulated validation, and acceptance. No final-B1,
manifest, checkpoint, B2, downstream, or Cycle 4 authority is granted here.

Open findings: none.

## Verdict

`pass`
