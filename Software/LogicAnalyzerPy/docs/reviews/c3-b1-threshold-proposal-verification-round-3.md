# C3-B1 threshold-proposal verification — round 3

Verdict: `pass`.

## Identity and scope

Independent verifier
`c3-b1-pre-execution-runner-rebinding-verifier-1` statically verified proposal
candidate commit `b260d9ecc0e74ed2502dda89beebb851ddfedb77`, tree
`8a65628df5ba63727e8305e901b9954fe0bec7e5`, against governing contract commit
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`.

The candidate adds exactly:

- `testdata/decoders/cycle3/threshold-proposal-round-3.json`, SHA-256
  `7fb9e88aaa5888e1a3133ff2234253bdfbbc4bd7151fc3a3be3c387dd619f510`;
- `docs/reviews/c3-b1-threshold-proposal-rationale-round-3.md`, SHA-256
  `8ea67712009a8a730c6eba8834e063179b709f07dfcdc5ffd7e9a55f6a93c58b`.

The accepted raw candidate `2ae1e4335c38a5cf717491c7936f857292f71498`,
corrected raw verification `10a6a1f72fc4973c112bd1da0877ffdc2590f3f8`,
raw accumulation `68242a9b2a173432ad465b514dac9369821c3723`, and
raw acceptance `115e2d022f26dbd211616dea05ed91bdb1a2cb62` are exact
ancestors. This verification was static: no decoder, runner, snapshot, raw
reproduction, threshold execution, browser, product, hardware, external
runtime, or network action occurred. The two untracked B2 paths were neither
inspected nor modified.

## Evidence identity and maxima

The proposal is compact canonical newline-terminated JSON with a closed schema,
round 3, and exact status `proposal-not-approved`. Its environment is exactly
macOS 15.7.7 build 24G720, x86_64, `Macmini8,1`, Python 3.12.13. Its fixture,
runner, runner-acceptance, raw candidate, corrected verification, accumulation,
acceptance, superseded proposal, superseded approval, and six digest fields are
an exact closed equality check.

The five raw artifact SHA-256 values independently remain environment
`fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34`,
requests `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`,
observations `28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd`,
hostile `d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080`,
and manifest `7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e`.
Corrected cap SHA-256 remains
`6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.

I recomputed maxima over all 315 retained snapshot rows and all 50 retained
hostile primary rows, never from a median or selected case. The complete 29
raw maxima are:

| ID | Raw maximum |
| --- | ---: |
| `input_samples` | 372 |
| `request_bytes` | 1,286 |
| `wall_deadline_ms` | 124 |
| `terminate_grace_ms` | 250 |
| `worker_address_space_bytes` | not an RSS maximum |
| `worker_peak_rss_bytes` | 20,692,992 |
| `parent_retained_growth_bytes` | 933,888 |
| `recursion_limit` | 320 |
| `output_records` | 34 |
| `encoded_bytes` | 4,222 |
| `decoded_bytes` | 4,222 |
| `stdout_bytes` | 0 |
| `stderr_bytes` | 0 |
| `diagnostic_bytes` | 244 |
| `text_bytes` | 426 |
| `binary_bytes` | 4 |
| `nested_depth` | 8 |
| `nested_items` | 447 |
| `retained_result_bytes` | 24,389 |
| `successful_parent_total_ns` | 123,103,531 |
| `launch_ns` | 7,277,866 |
| `reap_ns` | 121,658 |
| `child_load_ns` | 2,520,499 |
| `child_import_ns` | 12,202,717 |
| `child_decode_ns` | 1,342,863 |
| `timeout_cleanup_total_ns` | 5,282,160,866 |
| `terminate_to_reap_ns` | 253,029,590 |
| `kill_to_reap_ns` | 1,456,856 |
| `spi_max_word_size_bits` | 8 |

## Formulae, boundaries, and comparison

All 29 derivation strings and independently calculated values match. Every
entry has the exact expected kind and unit, positive integer `value`, inclusive
`accept == value`, first rejection `reject == value + 1`, exact raw maximum,
and exact experiment-cap identity. Every hard value is equal to or stricter
than its corrected experiment cap. Cross-limit checks prove the successful
ceiling fits the wall deadline; timeout cleanup fits deadline plus grace plus
250 ms; terminate-to-reap fits grace plus 50 ms; and SPI 8 is accepted while 9
is rejected.

The changed formula independently gives:

```text
123,103,531 * 8 = 984,828,248
ceil(984,828,248 / 100,000,000) * 100,000,000 = 1,000,000,000
accept = 1,000,000,000
reject = 1,000,000,001
```

`1,000,000,000 / 123,103,531` rounds to 8.12, so the proposal's approximate
ratio statement is accurate. One second is exactly one fifth of, and remains
below, the five-second wall deadline.

An exact ID-to-value comparison with the superseded round-2 proposal finds 28
unchanged values and one changed value only:
`successful_parent_total_ns`, from 900,000,000 to 1,000,000,000. Proposal
`395646fa1172382928581d7266723f5b044cf8f2` and operator-approval record
`b6d904064ab7b9e195eedded1c55efc306eeb925` are explicitly named as
superseded. The rationale states that neither transfers authority and that no
round-3 value becomes authoritative without the fresh remaining gates and a new
explicit operator decision.

## Negative coverage and commands

The verifier-owned test has 29 passing cases: one complete positive audit, 23
proposal mutations, and five direct cross-limit mutations. It non-vacuously
rejects missing, extra, and duplicate IDs; boolean, float, zero, and negative
values; changed raw maxima and formula strings; weakened or substituted caps;
wrong units and accept/reject boundaries; deadline, cleanup, terminate, and SPI
feasibility violations; approved status; digest, commit, and environment
substitutions; and a false 28/1 prior-round comparison. The direct cross-limit
tests reach their specific guard rather than merely failing an earlier exact
value assertion.

All commands were prefixed with `rtk` and tests used the clean Python 3.12
environment with `PYTHONDONTWRITEBYTECODE=1`.

- candidate commit/tree and exact two-path diff — passed;
- raw/fixture hashes and candidate ancestry — passed;
- focused verifier — 29 passed in 0.45 seconds;
- Ruff over the verifier — passed;
- `git diff --check` — passed.

Verifier test:
`tests/verification/test_c3_b1_threshold_proposal_round3.py`, SHA-256
`60068a4cc155b9661a5a558c4ca07a0766b0b581ecd86dcc246eccc2c311953d`.

No finding remains open. The exact proposal candidate passes fresh independent
static verification. This is not accumulated validation, acceptance, operator
approval, product enforcement, or permission to transfer the superseded
approval.
