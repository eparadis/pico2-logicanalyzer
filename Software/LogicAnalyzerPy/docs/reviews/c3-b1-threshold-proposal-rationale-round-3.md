# C3-B1 numeric threshold proposal rationale — round 3

## Status and authority

This is an immutable **proposal**, not an approval or product-enforcement
change. It was prepared by the primary orchestrator only after raw candidate
`2ae1e4335c38a5cf717491c7936f857292f71498` passed corrected independent
verification at `10a6a1f...`, accumulated validation at `68242a9...`, and
independent acceptance at `115e2d0...`. The machine-readable proposal is
`testdata/decoders/cycle3/threshold-proposal-round-3.json`.

The fixture correction invalidated the old raw evidence and therefore the
round-2 proposal and operator approval even where numeric values remain useful.
Round 3 supersedes proposal `395646f...` and operator-approval record
`b6d9040...`; neither transfers authority. No numeric value becomes
authoritative until this exact proposal receives fresh independent
verification, complete accumulated validation, independent acceptance, and a
new explicit operator decision.

## Evidence and method

The proposal binds corrected fixture `a98d328...`, accepted runner
`ca0ee751...`, runner acceptance `bf1fc5e...`, raw candidate `2ae1e43...`,
corrected raw verification `10a6a1f...`, raw accumulation `68242a9...`, and raw
acceptance `115e2d0...`. Its five raw-file digests and corrected experiment-cap
digest are literal machine-checkable inputs.

Root recomputed maxima over every retained row, never medians or selected
cases:

- 63 timelines × five successful retained repetitions;
- ten hostile cases × five retained repetitions, with recovery after every
  classified failure;
- input 372 samples and request 1,286 bytes;
- 34 records, 4,222 encoded/decoded bytes, 426 text bytes, four binary bytes,
  depth eight, 447 nested items, 244 diagnostic bytes, and 24,389 retained
  result bytes;
- successful parent total 123,103,531 ns, launch 7,277,866 ns, reap 121,658
  ns, and child load/import/decode 2,520,499 / 12,202,717 / 1,342,863 ns;
- child peak RSS 20,692,992 bytes and maximum per-call parent max-RSS growth
  933,888 bytes; and
- timeout cleanup 5,282,160,866 ns, terminate-to-reap 253,029,590 ns, and
  kill-to-reap 1,456,856 ns.

Independent reproductions preserve complete timing and RSS discrepancies as
observations. They do not average runs, replace the committed raw maxima, or
turn runtime variation into approval.

## Numeric relationship to round 2

Exactly 28 of 29 proposed inclusive values remain unchanged. One value changes
because the accepted raw maximum changed:

- `successful_parent_total_ns`: raw maximum `123,103,531`; multiplying by
  eight gives `984,828,248`; ceiling to the required `100,000,000-ns` quantum
  gives exactly `1,000,000,000`; inclusive accept is `1,000,000,000` and the
  first rejected integer is `1,000,000,001`.

The prior value was 900,000,000 ns, derived from the invalidated earlier raw
maximum. It is not silently retained or treated as approved. The new 1-second
proposal is approximately 8.12 times the slowest accepted parent observation
and remains one fifth of the enforced 5-second wall deadline.

## Proposed hard ceilings

| Limit | Proposed inclusive maximum | Raw maximum | Experiment cap | Derivation |
| --- | ---: | ---: | ---: | --- |
| Input samples | 65,536 | 372 | 100,000 | next power of two above raw × 128 |
| Request bytes | 4 MiB | 1,286 | 46,456,256 | next power of two above raw × 2,048 |
| Wall deadline | 5,000 ms | 123.104 ms successful | 5,000 ms | unchanged proven deadline |
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

Every hard ceiling is equal to or stricter than its corrected experiment cap.
The SPI maximum remains evidence-driven: 8 is the largest directly reproduced
word size and 9 remains the first rejected value.

## Proposed regression ceilings

| Observation | Proposed inclusive maximum | Accepted raw maximum | Rationale |
| --- | ---: | ---: | --- |
| Worker peak RSS | 128 MiB | 20,692,992 B | next power above raw × 4; approximately 6.5× actual |
| Parent retained growth | 16 MiB | 933,888 B | next power above raw × 16 |
| Successful parent total | 1,000 ms | 123,103,531 ns | ceiling to 100 ms above raw × 8 |
| Launch | 100 ms | 7,277,866 ns | rounded ceiling above raw × 8 |
| Reap | 50 ms | 121,658 ns | scheduler floor above raw × 64 |
| Child load / import / decode | 100 ms each | 2,520,499 / 12,202,717 / 1,342,863 ns | bounded phase-specific headroom |
| Timeout cleanup total | 5.5 s | 5,282,160,866 ns | deadline + grace + 250 ms cleanup |
| Terminate-to-reap | 300 ms | 253,029,590 ns | grace + 50 ms cleanup |
| Kill-to-reap | 50 ms | 1,456,856 ns | scheduler floor above raw × 16 |

These are exact-candidate regression ceilings for the characterized macOS
15.7.7 build 24G720, x86_64, Python 3.12.13 environment class. They are not
real-time or cross-platform guarantees. Address space and peak RSS remain
separate measurements.

## Boundaries and limitations

Every entry repeats `accept == value` and `reject == value + 1`. Verification
must independently recompute all raw maxima, formulae, boundaries, digests,
cap relationships, the exact 1-second arithmetic, and the 28-unchanged/one-
changed comparison. It must reject missing, extra, or duplicate IDs; booleans
or non-positive/non-integral values; weakened hard caps; inconsistent units or
boundaries; timing-policy contradictions; an SPI maximum above eight; changed
evidence; and any approved status.

The focused corpus does not prove throughput scaling to every hard maximum.
Later product batches must independently enforce accepted boundaries and prove
representative, stress, and exact-candidate performance without rebasing. Any
later increase requires another B1 amendment and renewed explicit operator
approval.

No product host exists, no product enforcement is claimed, and no value is
operator-approved by this document.
