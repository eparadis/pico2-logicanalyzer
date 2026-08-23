# C2-B5 verification round 2

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T20:42:49Z`.
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`;
  tree `06d6498f010f9cf230697aa922c2a550f8cca24c`.
- Implementation record reviewed as evidence only: `819a9760c763802cc135c0f9d27f88a39b71fd33`.
- Verdict: `pass`.

## Findings and dispositions

1. `C2B5-V001` — closed. The durable schema-2 record contains two raw ready/paint
   observations for every required case; 30 raw response-complete pan/zoom observations; and
   two raw observations for each transition/distinct-strobe and representative/worst bus
   combination. An independent nearest-rank implementation reproduced every per-case and
   aggregate median/p95 exactly. Real bus tables were rendered with 100 bounded rows, fixture
   payload identities, roles, modes, and counts attached.

## Independent fixture and baseline validation

- Inert ZIP/NPY readers verified the complete empty/schema-1/constant/sparse/dense/maximum
  8/16/24/representative-bus/worst-bus corpus, exact payload digests/sizes/counts/dtypes, a
  genuinely changing lower-bit representative bus with D7 edge-producing strobe, and a
  transition-dense worst bus.
- The generator reproduced the manifest and every fixture byte-for-byte in an isolated
  `/private/tmp` directory. Frozen identities:
  - baseline: `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`;
  - manifest: `dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`;
  - generator: `3e0be8f90e6dc846803a28bb278b21f797ddc0576f5371149beb9ad185fb29c4`;
  - benchmark: `2efeca32fcac6eb8c98480d49d02b304b9985121d9f2fe3f85e8ffe47e1c930b`;
  - production asset manifest:
    `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
- Method identity, 1280x900 viewport, DPR 1, browser/Playwright/Node/macOS host identity,
  warmups, iteration counts, timing boundary, nearest-rank formula, payload/sample/transition/
  Canvas/DOM/row counts, and unavailable-memory declaration were complete and sanitized.
  `threshold` remains `null`.
- Fresh reproduction produced schema 2, all 9 roles, 16 loads, 30 interactions, and 4 bus
  observations with the frozen counts. Its report SHA-256 was
  `1c83af36e62b0d62540f093310f829daa2702ec89339915fec24e48fefb6dad9`;
  generated residue was removed. Timing differences from the frozen observation are expected
  shared-host measurements and no threshold was applied.

## Product and accumulated gates

- Fresh independent baseline suites, including the immutable round-one checks: 8 passed.
- Clean accumulated non-hardware Python: 354 passed, 2 documented sandbox-loopback skips,
  44 warnings. Ruff, strict mypy over 21 source files, dependency, OpenAPI, asset, CLI-help,
  and diff checks passed.
- Node 22 lint/typecheck passed; Vitest 3 files/5 tests passed; production build transformed
  29 modules and reproduced committed assets.
- Root-brokered real-loopback API: 1 passed. Production browser workflows: 2 passed.
  Independent DPR-2 maximum-width/request/DOM/capability test: 1 passed. Performance benchmark:
  1 passed in 23.8 seconds test time / 24.8 seconds total.
- Full B5 source and black-box audit rechecked schema-1/schema-2/CSV offline imports; ordered
  8/16/24 labels and visibility; pan, cursor-centered zoom, trigger/cursor readout; bounded
  transition Canvas/DPR/DOM work; both bus modes/pagination/export; all lifecycle/failure/
  cancellation/reconnect/shutdown states; safe downloads; production runtime isolation; and
  capability non-disclosure. No new product finding was identified.

## Scope and authority

No threshold was evaluated or proposed. No product, prior evidence, governing contract,
manifest, or progress file was modified. No serial/hardware, firmware, C#/.NET, persistent
service, public server, packaging, acceptance, B6, or Cycle 3 action occurred.

Open findings: none. Deferred findings: none.
