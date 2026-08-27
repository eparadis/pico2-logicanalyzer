# C3-B1 numeric threshold proposal rationale — round 2

## Status and authority

This is an immutable **proposal**, not approved limits. It was prepared by the
primary orchestrator only after raw candidate
`397981adf0f89115647203e749db1b1e5b3384cf` passed independent reproduction,
complete accumulated validation, and independent acceptance. The machine-
readable proposal is
`testdata/decoders/cycle3/threshold-proposal-round-2.json`.

Round 2 supersedes only the failed round-1 proposal candidate `e3a1d7c`. Fresh
verification at `e47dc30` found `C3B1-TPV001`: the round-1 successful-parent
value did not equal its stated ceiling formula. Correction assignment
`b663d76` authorizes the exact 900-ms formula result below. No round-1 pass or
approval transfers, and all other proposed limits and accepted evidence remain
byte-for-byte equivalent in meaning.

No product host exists, no product enforcement is claimed, and no numeric value
becomes authoritative until proposal verification, accumulated validation,
acceptance, and explicit operator approval all pass in that order.

## Evidence and method

The proposal binds accepted fixture `7c57a347`, corrected runner `48d139f`, raw
candidate `397981a`, reproduction `9ac10d7`, accumulated result `b49bd49`, raw
acceptance `7baa53b`, original proposal assignment `29ac784`, failed proposal
`e3a1d7c`, failed verification assignment `8762de1`, failed verification
`e47dc30`, and correction assignment `b663d76`. Its five raw-file digests and
experiment-cap digest are literal machine-checkable inputs.

Root recomputed maxima over every retained row, not medians or selected cases:

- 63 timelines × five successful repetitions;
- ten hostile cases × five repetitions, with recovery after every failure;
- input 372 samples and request 1,286 bytes;
- 34 records, 4,222 encoded/decoded bytes, 426 text bytes, four binary bytes,
  depth eight, 447 nested items, 244 diagnostic bytes, and 24,389 retained
  result bytes;
- successful parent total 105,815,301 ns, launch 6,464,224 ns, reap 164,802 ns,
  child load/import/decode 2,524,751 / 9,337,765 / 1,715,444 ns;
- child peak RSS 20,856,832 bytes and maximum per-call parent max-RSS growth
  884,736 bytes; and
- timeout cleanup 5,283,148,328 ns, terminate-to-reap 254,508,892 ns, and
  kill-to-reap 2,054,776 ns.

The verifier's timing discrepancy is retained: 61/63 reproduction ranges were
lower and non-overlapping, two overlapped; RSS overlapped for 58 cases and was
lower for five, never higher/non-overlapping. Therefore the proposal uses the
slower committed raw maxima and broad explicit regression headroom. It does not
average the two runs, discard slower rows, or infer platform guarantees.

## Proposed hard ceilings

| Limit | Proposed inclusive maximum | Raw maximum | Experiment cap | Derivation |
| --- | ---: | ---: | ---: | --- |
| Input samples | 65,536 | 372 | 100,000 | next power of two above raw × 128 |
| Request bytes | 4 MiB | 1,286 | 46,354,688 | next power of two above raw × 2,048 |
| Wall deadline | 5,000 ms | 105.816 ms successful | 5,000 ms | unchanged proven deadline |
| Termination grace | 250 ms | 250 ms exercised | 250 ms | unchanged proven grace |
| Worker address space | 64 GiB | not an RSS observation | 64 GiB | verified macOS x86_64 RLIMIT_AS floor |
| Recursion | 320 frames | 320 reported | 320 | unchanged proven boundary |
| Output records | 16,384 | 34 | 69,632 | next power of two above raw × 256 |
| Encoded / decoded | 2 MiB each | 4,222 each | 6,180,864 | next power of two above raw × 256 |
| Stdout / stderr | 64 KiB each | zero each | 193,152 / 96,576 | defensive bounded-channel floor |
| Diagnostics | 8 KiB | 244 | 12,072 | next power of two above raw × 32 |
| Text / binary | 512 / 256 KiB | 426 / 4 | 3,090,432 each | explicit powers-of-two headroom |
| Nested depth / items | 32 / 16,384 | 8 / 447 | 40 / 69,632 | raw × 4; next power above raw × 32 |
| Retained result | 8 MiB | 24,389 | 185,418,752 | next power of two above raw × 256 |
| SPI maximum word size | 8 bits | 8 | n/a | largest directly reproduced size |

Every product hard ceiling is equal to or stricter than the accepted experiment
envelope. “Stricter” means a smaller accepted value; no experiment cap was
increased or weakened. Request headroom is deliberately larger relative to raw
than sample headroom so a full accepted sample vector remains representable.

The SPI maximum is evidence-driven, not a default of convenience: word sizes 1
and 8 were directly characterized, 8 is the largest reproduced value, and the
governing discovery record explicitly leaves values above 8 ineligible until
positive evidence and operator approval exist. This proposal supplies no such
evidence, so 9 is the first rejected value.

## Proposed regression ceilings

| Observation | Proposed inclusive maximum | Accepted raw maximum | Rationale |
| --- | ---: | ---: | --- |
| Worker peak RSS | 128 MiB | 20,856,832 B | next power above raw × 4; 6.4× actual |
| Parent retained growth | 16 MiB | 884,736 B | next power above raw × 16 |
| Successful parent total | 900 ms | 105,815,301 ns | ceiling to 100 ms above raw × 8 |
| Launch | 100 ms | 6,464,224 ns | rounded ceiling above raw × 8 |
| Reap | 50 ms | 164,802 ns | scheduler floor above raw × 64 |
| Child load / import / decode | 100 ms each | 2,524,751 / 9,337,765 / 1,715,444 ns | bounded phase-specific headroom |
| Timeout cleanup total | 5.5 s | 5,283,148,328 ns | deadline + grace + 250 ms cleanup |
| Terminate-to-reap | 300 ms | 254,508,892 ns | grace + 50 ms cleanup |
| Kill-to-reap | 50 ms | 2,054,776 ns | scheduler floor above raw × 16 |

These are exact-candidate regression ceilings on the characterized macOS
environment class. They are not real-time promises. The wall deadline and
grace are enforced process limits; phase timings and RSS are observed
regression gates. Address-space and peak-RSS values remain separate because a
Python process can reserve virtual address space without retaining that amount
of resident memory.

## Boundaries and limitations

Every proposal entry repeats `accept == value` and `reject == value + 1`.
Verification must independently recompute every raw maximum, formula, boundary,
digest, and cap relationship. It must specifically reject duplicate/missing
IDs, booleans masquerading as integers, non-positive or non-integral values,
changed raw evidence, a performance ceiling above the wall/cleanup policy, an
SPI maximum above characterized evidence, and any hard limit weaker than the
experiment cap.

The corpus is focused and macOS-only; it does not prove throughput scaling to
every hard maximum. B2 must independently enforce every accepted boundary, and
B3/B5 must prove representative, stress, and exact-candidate performance
without rebasing. Any later need to increase a value is a B1 amendment: new
proposal, independent verification, accumulated validation, acceptance, and
renewed explicit operator approval.

No finding is hidden. No value is operator-approved by this document.
