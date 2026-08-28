# C3-B1 threshold-proposal verification — round 4

Verdict: `pass`.

## Identity and scope

Independent verifier `c3-b1-threshold-verifier-replacement-1` statically
verified proposal candidate commit
`b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0`, tree
`e8661f094ba0423ca08055ea785bbfcde8554d71`. The candidate adds exactly:

- `testdata/decoders/cycle3/threshold-proposal-round-4.json`, SHA-256
  `98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`;
- `docs/reviews/c3-b1-threshold-proposal-rationale-round-4.md`, SHA-256
  `58ef6451033603989617b195ab2d0184c75e243cbcad3ec99df3b2d41027242c`.

The accepted raw candidate `d0d9dbe87f7841f09f261556de0909475e048b95`,
raw verification `17397360770f3aab7d79a479a53499b50a1245cd`, raw
accumulation `7295e4d9472632f92bb22e6a06e001609b2590e6`, and raw
acceptance `72168f4ca0f90e16e99a72537e159818a434dea1` are exact
ancestors. This verification was static: no decoder, runner, snapshot, raw
reproduction, threshold enforcement, browser, product, final-candidate, B2,
downstream, hardware, network, or external runtime action occurred. The
untracked B2 paths were neither inspected nor modified.

## Evidence identity and retained-row maxima

The proposal is compact canonical newline-terminated JSON with a closed schema,
round 4, and exact status `proposal-not-approved`. Its environment is exactly
macOS 15.7.7 build 24G720, x86_64, `Macmini8,1`, Python 3.12.13. Its accepted
fixture, accepted runner, runner acceptance, raw candidate, raw verification,
raw accumulation, raw acceptance, superseded proposal, superseded operator
approval, and six digest fields are closed exact-equality checks.

The six artifact SHA-256 values independently match environment
`d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f`,
requests `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`,
observations `ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee`,
hostile observations
`af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91`,
raw manifest `5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8`,
and experiment caps
`6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.

I independently recomputed maxima over all 315 retained successful snapshot
rows and all 50 retained hostile primary rows, never from medians or selected
cases. The complete 29 raw maxima are:

| ID | Raw maximum |
| --- | ---: |
| `input_samples` | 372 |
| `request_bytes` | 1,286 |
| `wall_deadline_ms` | 157 |
| `terminate_grace_ms` | 250 |
| `worker_address_space_bytes` | not an RSS maximum |
| `worker_peak_rss_bytes` | 20,713,472 |
| `parent_retained_growth_bytes` | 1,757,184 |
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
| `successful_parent_total_ns` | 156,549,612 |
| `launch_ns` | 6,008,633 |
| `reap_ns` | 171,050 |
| `child_load_ns` | 1,982,562 |
| `child_import_ns` | 10,056,019 |
| `child_decode_ns` | 1,505,821 |
| `timeout_cleanup_total_ns` | 5,283,467,874 |
| `terminate_to_reap_ns` | 257,173,170 |
| `kill_to_reap_ns` | 1,581,889 |
| `spi_max_word_size_bits` | 8 |

## Formulae, boundaries, feasibility, and comparison

All 29 independently calculated values and exact derivation strings match.
Every entry has the expected kind and unit, positive non-boolean integer value,
inclusive `accept == value`, first rejection `reject == value + 1`, exact raw
maximum, and exact experiment-cap identity. Every hard value is equal to or
stricter than its cap. The cross-limit checks prove parent total fits within
the wall deadline, timeout cleanup fits deadline plus grace plus 250 ms,
terminate-to-reap fits grace plus 50 ms, and SPI 8 is accepted while 9 is the
first rejected value.

The three changed calculations independently give:

```text
next_power_of_two(1,757,184 * 16) = 33,554,432
ceil_to_100ms(156,549,612 * 8) = 1,300,000,000
ceil_to_50ms(6,008,633 * 8) = 50,000,000
```

An exact ID-to-value comparison with round 3 finds exactly 26 unchanged values
and three changed values: `parent_retained_growth_bytes` from 16,777,216 to
33,554,432, `successful_parent_total_ns` from 1,000,000,000 to 1,300,000,000,
and `launch_ns` from 100,000,000 to 50,000,000. Thus the rationale's two
increases and one decrease are exact formula results.

The proposal and rationale bind superseded proposal
`b260d9ecc0e74ed2502dda89beebb851ddfedb77` and superseded operator approval
`63fdfee87159251cdf525eb608340e6bc08ad010`. The rationale truthfully states
that neither transfers authority and that no value becomes authoritative
without fresh remaining gates and a new explicit operator decision.

## Negative coverage and commands

The verifier-owned test has 30 passing cases: one complete positive audit, 24
proposal mutations, and five direct cross-limit mutations. It non-vacuously
rejects missing, extra, and duplicate IDs; boolean, float, zero, and negative
values; changed raw maxima or formulae; weakened or substituted caps; wrong
units or kinds; changed accept/reject boundaries; deadline, cleanup,
terminate-to-reap, and SPI contradictions; approved status; evidence digest,
commit, and environment substitutions; and a false 26/3 prior-round
comparison. The five direct tests reach the named feasibility guard rather
than failing an earlier exact-value assertion.

All commands were prefixed with `rtk` and the focused tests used
`PYTHONDONTWRITEBYTECODE=1`.

- candidate commit/tree and exact two-path diff — passed;
- raw-chain ancestry and evidence digests — passed;
- focused verifier — 30 passed in 0.47 seconds;
- Ruff over the verifier — passed;
- `git diff --check` over the verifier — passed.

Verifier test:
`tests/verification/test_c3_b1_threshold_proposal_round4.py`, SHA-256
`719acc7d4e474958d36bfc8d08c63f7dcce7dc97faf41b9d188e801bd33e54d6`.

No finding remains open. The exact round-4 proposal candidate passes fresh
independent static verification. This verdict is not accumulated validation,
acceptance, operator approval, product enforcement, or permission to transfer
the superseded approval.
