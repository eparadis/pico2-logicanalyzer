# C3-B1 threshold-proposal accumulated validation — round 4

## Subject and verdict

- Owner: primary Cycle 3 orchestrator (`/root`).
- Proposal candidate commit/tree:
  `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` /
  `e8661f094ba0423ca08055ea785bbfcde8554d71`.
- Fresh verifier commit/tree:
  `46d57e482c330fca945c0e2bb3ca35cc1a95d3a1` /
  `4dc95bc35142c920cc162550e27511279fbbe828`.
- Clean clone: `/private/tmp/c3-threshold-r4-final`.
- Completed: `2026-08-28T18:26:22Z`.
- Verdict: **pass**. The exact proposal is eligible for fresh independent
  acceptance, but remains `proposal-not-approved`.

Proposal and rationale SHA-256 values are respectively
`98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`
and
`58ef6451033603989617b195ab2d0184c75e243cbcad3ec99df3b2d41027242c`.
Verifier test/review SHA-256 values are respectively
`719acc7d4e474958d36bfc8d08c63f7dcce7dc97faf41b9d188e801bd33e54d6`
and
`2a5d8ee0ca91b713bbd21f5dbffe39ebeed953d7eb411ce96d97540066c57433`.

## Exact accumulated Python gate

Root derived the inventory from the immutable proposal candidate and added
only verifier-4. The resulting **56 modules** partitioned into **41 included**
and **15 excluded** modules. The included set contains the current fixture and
runner implementation tests, replacement raw verifier, and round-4 proposal
verifier. Every superseded raw/runner/proposal/final C3 module was excluded;
optional B2 was absent and was not copied, read, imported, or executed.

The exact 41 paths collected **608 tests** and completed with **602 passed**,
**6 inherited classified skips**, and **106 warnings** in 120.99 seconds. This
included a complete 486-launch raw reproduction and all 30 proposal tests.
Accumulated reproduction report SHA-256:
`41c6b6f84306ebe6a3e468b8b3f66af37c6efe5073fa44c6792840c8926cd6b1`.
No threshold enforcement, product, final-candidate, B2, or superseded C3 route
ran.

The proposal remained canonical round-4 `proposal-not-approved` evidence with
29 unique positive integer limits, exact inclusive/exclusive boundaries, six
raw/cap digests, all retained-row maxima and formulas, hard-cap and cross-limit
relationships, and the exact 26 unchanged / three changed comparison. The
superseded round-3 proposal and operator approval transfer no authority.

## Static and inherited regressions

The clean descendant also passed dependency consistency, whole-project Ruff,
strict mypy over 28 source files, binding and fixture checks, six Cycle-2
evidence validators, CLI help, Node lint/typecheck, five Vitest tests, the
29-module production build, and asset drift check.

One exploratory combined Playwright command ran the maximum-width, live, and
shell files concurrently against shared server state. Three tests passed and
maximum-width observed `error`; that combined shape is not an accepted gate
and transfers no result. Root then used the established isolated shapes:
maximum-width **1 passed**, followed separately by live/shell **3 passed**.
The isolated B6 performance test passed and the accepted B5 checker passed;
performance-report SHA-256 is
`641e62cc1722461dcbf5195ac19174851b82dd292c3de6592eb4f54ad44141d8`.

Final process and inventory audits found no characterization, worker, browser,
Vite, or web-server survivor and no runner bytecode cache. `git diff --check`
passed. The three preserved untracked B2 paths remained untouched.

This pass grants no operator, final-B1, manifest, checkpoint, B2, product, or
Cycle 4 authority.

Findings: none.

`pass`
