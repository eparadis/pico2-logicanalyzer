# C3-B1 raw-baseline collection replacement — round 1

## Subject and verdict

- Collection identity: `c3-b1-raw-baseline-reproducer-replacement-1`.
- Accepted runner candidate: `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` / `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Accepted runner-chain commit/tree: `01f059cb5f60e885c7d19e8bf5376bdb27dcca19` / `1c15252a26e5a4af571228dbf37999e385026f87`.
- Accepted runner-chain record SHA-256: `f1963a6cfe7de8c62c2f3de150f0bbb7ffe0e3c93998d2dc352ffdbe4b3eb5bd`.
- Accepted corrected semantic fixture: `3af6b9f80dd52611e14acca407707d1da7b8d9ac` / `14c010153ea5542617e601e4126047c561a48483`.
- Verdict: **pass**.

## Fresh serialized collection

One collector process performed the single complete serialized evidence collection using repository-local CPython 3.12. Four earlier pre-write attempts transferred no observation or evidence: the first stopped during inert machine-model precomputation and launched zero children; the second stopped at the first timeline's deliberately strict stability audit after six child launches; the third completed all 378 snapshot launches and the first designed-success hostile case's six launches, then stopped while auditing optional hostile diagnostic fields; the fourth completed 378 snapshot launches, 43 hostile launches, and 36 required recovery launches through `recursion_over`, then stopped after the `address_space_over` warm-up because that probe's intentionally plain-text diagnostic was incorrectly treated as JSON. All 847 child results from those attempts were discarded. Every environment, identity, source digest, provenance file set, request, and cap input for the complete collection was precomputed before its first warm-up. The exact 63 requests were derived only from timeline transitions, mapping, sample count, samplerate, options, and provenance source sets; expected calls, records, waits, typed vectors, goldens, historical observations, and historical timings were not execution oracles.

Each of 63 timelines received one unrecorded status-only warm-up and five retained repetitions. All five retained semantic outputs and the eight semantically deterministic count fields (`input_samples`, `request_bytes`, `output_records`, `binary_bytes`, `nested_depth`, `nested_items`, `stdout_bytes`, and `stderr_bytes`) were stable within every timeline. The five size-accounting fields that necessarily include volatile diagnostic timing digits (`encoded_bytes`, `decoded_bytes`, `diagnostic_bytes`, `text_bytes`, and `retained_result_bytes`) remain exact per repetition and are summarized by min/median/max rather than falsely required to be identical. The full ten-kind hostile production profile received one warm-up and five retained repetitions per kind. Eight expected-failure kinds received a valid recovery after every failure, including warm-ups; both designed-success kinds completed. All failures were discarded by the runner, all recoveries succeeded, every child was reaped, both protocol descriptors were closed, and `ignore_term` used kill-and-reap evidence.

Exact complete-collection launch accounting: 378 snapshot launches (63 warm-ups + 315 retained), 60 hostile launches (10 warm-ups + 50 retained), and 48 recovery launches (8 warm-ups + 40 retained), for **486 complete-collection child launches**. Including the 847 explicitly discarded pre-write attempt launches, the replacement chain launched 1,333 children in total. Timing and RSS values are retained transparently in the canonical observations as min/median/max summaries and per-repetition raw measurements; no prior timing transferred.

## Identity and artifacts

- Binding SHA-256: `4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7`.
- Semantic fixture SHA-256: `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`.
- Fixture manifest SHA-256: `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`.
- Caps SHA-256: `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`; all 17 exact production caps were preserved without adjustment.
- `environment.json`: `d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f`.
- `requests.json`: `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`.
- `observations.json`: `ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee`.
- `hostile-observations.json`: `af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91`.
- `manifest.json`: `5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8`.
- Temporary collector SHA-256: `df825cddebffe7268fdfe61ae21846d6a6556d1bfb0f3fecfb6b7549ad43b70d`; it remained under `/private/tmp` and did not enter the repository.

The five canonical JSON documents were constructed in temporary storage, parsed back, checked for canonical encoding, full closed schemas, summary arithmetic, stable semantics/counts, exact identity and digest closure, and only then replaced as one closed write-at-end set.

## Scope and cleanup

Only the five canonical `cycle3-raw` JSON files and this review record were changed. No fixture, runner, threshold, product, contract, progress, test, manifest outside the raw set, later evidence, B2 path, hardware, network, or Cycle 4 action was touched. The collector ran no expected-output comparison and made no threshold proposal or acceptance claim. No runner worker or bytecode cache survived the collection boundary.

`pass`
