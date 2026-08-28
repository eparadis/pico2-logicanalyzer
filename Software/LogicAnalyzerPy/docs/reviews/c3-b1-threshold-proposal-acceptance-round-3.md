# C3-B1 threshold-proposal acceptance — round 3

## Identity, subject, and verdict

- Acceptance identity:
  `c3-b1-pre-execution-runner-rebinding-acceptance-1`
  (`/root/c3_b1_runner_rebind_accept_r1`), acting only in the independent
  acceptance lane.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact round-3 proposal candidate/tree:
  `b260d9ecc0e74ed2502dda89beebb851ddfedb77` /
  `8a65628df5ba63727e8305e901b9954fe0bec7e5`.
- Fresh verification descendant/tree:
  `92de4e6c9c57ba258f2991c92c3e1569cf659ad4` /
  `1317567a736035e8123da1b5a50ab8a3c1250da7`.
- Accumulated-validation descendant/tree:
  `c3cc27417fdf324723f6643deb863a4933b29537` /
  `61b3826b1ddad280f9e25935b97f0ce330b905f2`.
- Verdict: `pass`.

This is a static acceptance audit. I did not amend the proposal, execute a
threshold, or make an operator decision. I wrote only this record.

## Acceptance findings

1. **Pass — ancestry, candidate scope, and role separation.** The proposal is
   a direct descendant of accepted raw-baseline commit `115e2d0...`; the
   verifier and accumulated commits are direct descendants in the required
   order. The candidate adds exactly the round-3 rationale and machine-readable
   proposal. The verifier adds only its record and verifier-owned test; the
   orchestrator adds only the accumulated record. The primary orchestrator is
   proposal author and accumulated-validation owner, the independent verifier
   is `c3-b1-pre-execution-runner-rebinding-verifier-1`, and this identity is
   the independent acceptance auditor. No product, raw, fixture, runner,
   manifest, checkpoint, or B2 path is part of the proposal delta.

2. **Pass — artifact and evidence closure.** Independently recomputed SHA-256
   values are:

   - proposal:
     `7fb9e88aaa5888e1a3133ff2234253bdfbbc4bd7151fc3a3be3c387dd619f510`;
   - rationale:
     `8ea67712009a8a730c6eba8834e063179b709f07dfcdc5ffd7e9a55f6a93c58b`;
   - verifier test:
     `60068a4cc155b9661a5a558c4ca07a0766b0b581ecd86dcc246eccc2c311953d`;
   - verification record:
     `2209b61e8460e77a6118a9c934315d4bd89c150d46e5645436e52c9df304338c`;
   - accumulated record:
     `d96ad923d95b2004e7a5e2d3b935bde9008f7afef9688d852f2ab3944e83c975`.

   The proposal is canonical newline-terminated JSON with exact schema
   `cycle3-threshold-proposal/v1`, round 3, and status
   `proposal-not-approved`. It binds the corrected fixture, accepted runner and
   runner acceptance, exact raw candidate, corrected raw verification,
   accumulation and acceptance, five raw artifact hashes, corrected experiment
   cap hash, and the exact macOS 15.7.7 build 24G720 / x86_64 / Macmini8,1 /
   Python 3.12.13 environment class.

3. **Pass — all 29 exact proposed values and boundaries recompute.** There are
   exactly 29 unique IDs, no missing or extra ID, every value is a positive
   integer, every `accept` equals its value, and every `reject` equals value
   plus one. The exact inclusive values are:

   | ID | Proposed value |
   | --- | ---: |
   | `input_samples` | 65,536 |
   | `request_bytes` | 4,194,304 |
   | `wall_deadline_ms` | 5,000 |
   | `terminate_grace_ms` | 250 |
   | `worker_address_space_bytes` | 68,719,476,736 |
   | `worker_peak_rss_bytes` | 134,217,728 |
   | `parent_retained_growth_bytes` | 16,777,216 |
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
   | `successful_parent_total_ns` | 1,000,000,000 |
   | `launch_ns` | 100,000,000 |
   | `reap_ns` | 50,000,000 |
   | `child_load_ns` | 100,000,000 |
   | `child_import_ns` | 100,000,000 |
   | `child_decode_ns` | 100,000,000 |
   | `timeout_cleanup_total_ns` | 5,500,000,000 |
   | `terminate_to_reap_ns` | 300,000,000 |
   | `kill_to_reap_ns` | 50,000,000 |
   | `spi_max_word_size_bits` | 8 |

   Recomputed maxima cover all 315 retained snapshot rows and 50 retained
   hostile primary rows, never medians or selected cases. All derivations,
   units, kinds, raw maxima, cap relations, and cross-limit constraints match.
   Hard-enforcement values are equal to or stricter than the corrected
   experiment caps. Successful execution remains below the wall deadline;
   cleanup and terminate ceilings fit their composed budgets; SPI 8 is the
   largest reproduced and accepted word size and 9 is the first rejection.

4. **Pass — the exact 28 unchanged / one changed comparison is truthful.** A
   direct ID-to-value comparison with round 2 gives 28 unchanged values and
   exactly one change: `successful_parent_total_ns`, from 900,000,000 to
   1,000,000,000 ns. The new accepted raw maximum is 123,103,531 ns:

   ```text
   123,103,531 * 8 = 984,828,248
   ceil to 100,000,000-ns quantum = 1,000,000,000
   first rejected integer = 1,000,000,001
   ```

   The new value is approximately 8.12 times the raw maximum and exactly one
   fifth of the five-second deadline. No other value differs.

5. **Pass — superseded approval transfers no authority.** The proposal
   explicitly names round-2 proposal
   `395646fa1172382928581d7266723f5b044cf8f2` and operator-approval record
   `b6d904064ab7b9e195eedded1c55efc306eeb925` as superseded. The fixture/raw
   correction invalidated both. Their 28 numerically unchanged entries are
   historical comparison data only; neither the old record nor earlier
   conversational approval authorizes any round-3 value. The proposal and
   rationale consistently require a new explicit operator decision after the
   fresh gates.

6. **Pass — independent verification is complete and non-vacuous.** The
   verifier statically recomputed all raw maxima, formulas, identities,
   boundaries, kinds, units, cap relationships, cross-limit rules, and the
   exact prior-round comparison. Its 29-test matrix includes one complete
   positive audit, 23 proposal mutations, and five direct cross-limit
   mutations, rejecting missing/extra/duplicate IDs, bad types or values,
   evidence substitutions, weakened caps, inconsistent units or boundaries,
   false approval status, false 28/1 comparison, and deadline/cleanup/
   terminate/SPI contradictions. My independent static rerun passed all 29
   tests in 0.48 seconds. No decoder or raw reproduction was invoked.

7. **Pass — accumulated evidence is sufficient and candid.** The repository-
   local Python 3.12.13 gate passed dependency consistency, whole-project Ruff,
   strict mypy over 21 product files and seven runner modules, deterministic
   fixture and binding checks, CLI help, six Cycle 2 validators, and 635
   applicable tests with exactly two historical deselections. The suite
   included the complete 486-launch raw reproduction and reported exact reap,
   descriptor closure, semantic/count equality, classified failures, and
   successful recovery. Exact repository-local Node 22.14.0 passed ESLint,
   TypeScript, five Vitest tests, Vite/assets, four browser tests, and frozen B6
   performance/threshold validation; performance report SHA-256 is
   `387eaeb878960aa7239f7f0a265cb7e435576665fd8537e10579557c481a8979`.
   One reusable loopback/browser approval class covered recurring process
   families without per-child prompts.

8. **Pass — applicability exclusions are precise, not waivers.** The two
   deselected historical assertions are:

   - `tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`;
   - `tests/verification/test_c3_b1_semantic_fixture_correction.py::test_historical_inventory_failure_and_broad_mypy_non_gate_are_not_weakened`.

   Both freeze an earlier JSON namespace and necessarily reject the later
   required round-3 proposal artifact. The four ignored modules are the old
   final-candidate verifier, superseded runner-candidate verifier, round-1
   proposal verifier, and round-2 proposal verifier. A targeted audit reported
   the exact expected 44 failures and 45 passes: the two historical inventory
   assertions, 18 final assertions, one old runner assertion, 22 round-1
   proposal assertions, and one round-2 proposal assertion failed; remaining
   negative coverage passed. These modules must be rebound by their owning
   downstream gates.

9. **Pass — scope and cleanup remain bounded.** This acceptance used only Git,
   SHA-256, JSON, and static verifier checks. It did not execute a decoder, raw
   reproduction, runner/worker request, threshold, product host, browser,
   hardware, network, external runtime, publication, or B2 behavior. The two
   preserved untracked B2 paths were neither inspected nor modified. The
   accumulated clean clone was unchanged, and final audits found no retained
   test, browser, runner, worker, or decoder process.

## Authority and next gate

This pass accepts the exact proposal as suitable for an operator decision; it
does **not** itself approve or enforce any numeric value. The next required gate
is renewed explicit operator approval or amendment of the exact committed
round-3 values. An amendment creates another proposal candidate and repeats
verification, accumulated validation, and acceptance before renewed approval.
Only explicit approval of this exact committed proposal permits preparation of
the replacement final B1 binder. No final-binder, manifest, checkpoint, B2, or
Cycle 4 authority is granted here.

Open findings: none.

## Verdict

`pass`
