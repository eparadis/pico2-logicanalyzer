# C3-B1 numeric threshold proposal rationale — round 4

## Status and authority

This is an immutable **proposal**, not an approval or product-enforcement
change. It was prepared by the distinct proposal-author identity
`c3-b1-threshold-proposer-replacement-1` only after raw candidate
`d0d9dbe87f7841f09f261556de0909475e048b95` passed independent verification
at `17397360770f3aab7d79a479a53499b50a1245cd`, accumulated validation at
`7295e4d`, and independent acceptance at
`72168f4ca0f90e16e99a72537e159818a434dea1`. The machine-readable proposal is
`testdata/decoders/cycle3/threshold-proposal-round-4.json`.

The accepted replacement fixture and runner invalidated the earlier raw chain
and therefore the round-3 proposal and operator approval, even where numeric
values remain useful. Round 4 supersedes proposal
`b260d9ecc0e74ed2502dda89beebb851ddfedb77` and operator-approval record
`63fdfee`; neither transfers authority. No numeric value becomes authoritative
until this exact proposal receives fresh independent verification, complete
accumulated validation, independent acceptance, and a new explicit operator
decision.

## Evidence and method

The proposal binds accepted corrected fixture `3af6b9f...`, accepted runner
candidate `380d5dd...`, runner acceptance `01f059c...`, raw candidate
`d0d9dbe...`, raw verification `1739736...`, raw accumulation `7295e4d`, and
raw acceptance `72168f4...`. Its five raw-file digests and experiment-cap digest
are literal machine-checkable inputs.

The proposal author independently recomputed maxima over every retained row,
never medians or selected cases:

- 63 timelines × five successful retained repetitions;
- ten hostile cases × five retained repetitions, with recovery after every
  classified failure;
- input 372 samples and request 1,286 bytes;
- 34 records, 4,222 encoded/decoded bytes, 426 text bytes, four binary bytes,
  depth eight, 447 nested items, 244 diagnostic bytes, and 24,389 retained
  result bytes;
- successful parent total 156,549,612 ns, launch 6,008,633 ns, reap 171,050
  ns, and child load/import/decode 1,982,562 / 10,056,019 / 1,505,821 ns;
- child peak RSS 20,713,472 bytes and maximum per-call parent max-RSS growth
  1,757,184 bytes; and
- timeout cleanup 5,283,467,874 ns, terminate-to-reap 257,173,170 ns, and
  kill-to-reap 1,581,889 ns.

Independent reproductions preserve complete timing and RSS discrepancies as
observations. They do not average runs, replace the committed raw maxima, or
turn runtime variation into approval.

## Numeric relationship to round 3

Exactly 26 of 29 proposed inclusive values remain unchanged. Three values
change because the accepted raw maxima and unchanged derivation policies yield
different exact results:

- `parent_retained_growth_bytes`: raw maximum `1,757,184`; multiplying by 16
  gives `28,114,944`; the next power of two is exactly `33,554,432`. The
  round-3 value was `16,777,216`.
- `successful_parent_total_ns`: raw maximum `156,549,612`; multiplying by
  eight gives `1,252,396,896`; ceiling to the required `100,000,000-ns`
  quantum gives exactly `1,300,000,000`. The round-3 value was
  `1,000,000,000`.
- `launch_ns`: raw maximum `6,008,633`; multiplying by eight gives
  `48,069,064`; ceiling to the required `50,000,000-ns` quantum gives exactly
  `50,000,000`. The round-3 value was `100,000,000`.

The two increases and one decrease are formula results, not discretionary
rebasing. The earlier values and operator decision are not silently retained
or treated as approved. The new 1.3-second parent-total proposal is about 8.30
times the slowest accepted parent observation and remains below the enforced
5-second wall deadline.

## Proposed hard ceilings

| Limit | Proposed inclusive maximum | Raw maximum | Experiment cap | Derivation |
| --- | ---: | ---: | ---: | --- |
| Input samples | 65,536 | 372 | 100,000 | next power of two above raw × 128 |
| Request bytes | 4 MiB | 1,286 | 46,456,256 | next power of two above raw × 2,048 |
| Wall deadline | 5,000 ms | 156.550 ms successful | 5,000 ms | unchanged proven deadline |
| Termination grace | 250 ms | 250 ms exercised | 250 ms | unchanged proven grace |
| Worker address space | 64 GiB | not an RSS observation | 64 GiB | verified macOS x86_64 `RLIMIT_AS` floor |
| Recursion | 320 frames | 320 reported | 320 | unchanged proven boundary |
| Output records | 16,384 | 34 | 69,632 | next power of two above raw × 256 |
| Encoded / decoded | 2 MiB each | 4,222 each | 6,180,864 | next power of two above raw × 256 |
| Stdout / stderr | 64 KiB each | zero each | 193,152 / 96,576 | defensive bounded-channel floor |
| Diagnostics | 8 KiB | 244 | 12,072 | next power of two above raw × 32 |
| Text / binary | 512 / 256 KiB | 426 / 4 | 3,090,432 each | explicit powers-of-two headroom |
| Nested depth / items | 32 / 16,384 | 8 / 447 | 40 / 69,632 | raw × 4; next power above raw × 32 |
| Retained result | 8 MiB | 24,389 | 185,825,024 | next power of two above raw × 256 |
| SPI maximum word size | 8 bits | 8 | n/a | largest directly reproduced size |

Every hard ceiling is equal to or stricter than its experiment cap. The SPI
maximum remains evidence-driven: 8 is the largest directly reproduced word
size and 9 remains the first rejected value.

## Proposed regression ceilings

| Observation | Proposed inclusive maximum | Accepted raw maximum | Rationale |
| --- | ---: | ---: | --- |
| Worker peak RSS | 128 MiB | 20,713,472 B | next power above raw × 4; approximately 6.48× actual |
| Parent retained growth | 32 MiB | 1,757,184 B | next power above raw × 16 |
| Successful parent total | 1,300 ms | 156,549,612 ns | ceiling to 100 ms above raw × 8 |
| Launch | 50 ms | 6,008,633 ns | ceiling to 50 ms above raw × 8 |
| Reap | 50 ms | 171,050 ns | scheduler floor above raw × 64 |
| Child load / import / decode | 100 ms each | 1,982,562 / 10,056,019 / 1,505,821 ns | bounded phase-specific headroom |
| Timeout cleanup total | 5.5 s | 5,283,467,874 ns | deadline + grace + 250 ms cleanup |
| Terminate-to-reap | 300 ms | 257,173,170 ns | grace + 50 ms cleanup |
| Kill-to-reap | 50 ms | 1,581,889 ns | scheduler floor above raw × 16 |

These are exact-candidate regression ceilings for the characterized macOS
15.7.7 build 24G720, x86_64, Python 3.12.13 environment class. They are not
real-time or cross-platform guarantees. Address space and peak RSS remain
separate measurements.

## Boundaries and limitations

Every entry repeats `accept == value` and `reject == value + 1`. Verification
must independently recompute all raw maxima, formulae, boundaries, digests,
cap relationships, the exact three changed-value calculations, and the
26-unchanged/three-changed comparison. It must reject missing, extra, or
duplicate IDs; booleans or non-positive/non-integral values; weakened hard
caps; inconsistent units or boundaries; timing-policy contradictions; an SPI
maximum above eight; changed evidence; and any approved status.

The focused corpus does not prove throughput scaling to every hard maximum.
Later product batches must independently enforce accepted boundaries and prove
representative, stress, and exact-candidate performance without rebasing. Any
later increase requires another B1 amendment and renewed explicit operator
approval.

No product host exists, no product enforcement is claimed, and no value is
operator-approved by this document.
