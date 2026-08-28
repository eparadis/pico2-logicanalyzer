# C3-B1 pre-execution runner rebinding accumulated validation — round 3

## Subject and verdict

- Owner: primary Cycle 3 orchestrator (`/root`).
- Candidate commit/tree:
  `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` /
  `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Fresh verifier-5 pass commit/tree:
  `e95706f10a8a5a2f955e29b23cda25e157bf373e` /
  `19412221641fe361afc8bbbe119a2e8c24f039a2`.
- Completed: `2026-08-28T17:30:07Z`.
- Clean Python clone: `/private/tmp/c3-runner-if002-final`.
- Stable web-validation clone: `/private/tmp/c3-fixture-if002`.
- Verdict: **pass**. The exact replacement runner candidate is eligible for
  fresh independent acceptance. This record grants no raw, threshold,
  final-B1, manifest, checkpoint, B2, product, or Cycle 4 authority.

## Portable verifier and immutable subject

Verifier-5 owns only its new test and review. Their independently recomputed
SHA-256 values are respectively
`f84f123e6f8bbc1c3bcb1063faa11d0177438012db8b6ec314248b8c1d0984b1`
and
`027d0109336f3f5160a0dc609d2c79cf37722b845d9a050406463d921e4b28c2`.
Root reran verifier-5 with the complete inert/hostile runner implementation
suite: **188 passed** (11 verifier plus 177 runner).

The immutable candidate still differs from the RA001 finding commit only by
the round-3 implementation record. The reviewed method, runner, binding,
runner implementation test, accepted semantic fixture, fixture manifest, all
24 bound source digests, and all 17 positive caps remain unchanged. Verifier-5
preserves `C3B1-RA001` and proves that the invalid verifier-3 and verifier-4
passes transfer no authority under `C3B1-RV002` and `C3B1-RV003`.

## Exact pre-acceptance Python partition

Before execution, root derived paths only from the immutable candidate tree
and added verifier-5. The inventory was exactly **52 modules**, partitioned
into **40 included** and **12 excluded** modules. The explicit included set
contains the ordinary inherited tests, current fixture implementation test,
current inert runner implementation test, and verifier-5. Every other
`test_c3_*` module fails closed into the excluded set.

The same exact 40 paths collected **585 tests**. Executing those paths in the
clean clone produced **579 passed**, **6 inherited classified skips**, and
**106 warnings**. The skips were the two sandbox-prohibited loopback checks
and four optional Cycle-2 physical-artifact cases. No directory, glob, broad
marker selection, raw candidate, threshold candidate, final candidate,
manifest/checkpoint, superseded verifier, B2 path, snapshot characterization,
or decoder execution path was collected or executed.

Optional untracked B2 was neither copied into the clone nor read from the main
worktree. Verifier-5 handles its possible presence only as a synthetic
pathname and proves it would remain excluded. The three pre-existing B2-owned
untracked paths in the main worktree remained untouched.

## Static, contract, CLI, and web accumulation

Against the exact clean descendant, all of the following passed:

- `pip check`: no broken requirements.
- whole-project Ruff: all checks passed.
- strict mypy over `src` and all seven `tools/cycle3_characterize` modules:
  no issues in **28 source files**.
- canonical runner binding `--check` and deterministic fixture generator
  `--check`.
- all six accepted Cycle-2 evidence manifests, each validated separately
  against the Cycle-2 schema.
- installed `pico-la --help`, including the expected bounded command surface.
- Node 22 lint and typecheck.
- Vitest: **3 files / 5 tests passed**.
- deterministic Vite production build: **29 modules transformed**; committed
  asset check passed.
- isolated maximum-width Playwright gate: **1 passed**.
- separate live/shell Playwright gate: **3 passed**.
- isolated B6 performance Playwright gate: **1 passed**; the accepted B5
  threshold checker passed. Retained report SHA-256:
  `0934fbf638eaa61e64ea71b15bbd5e629383fc4f605dac070f4da570d327c25f`.

The first performance launcher attempt was rejected before test execution by
the filesystem/network sandbox's loopback readiness probe (`EPERM`). Root
retried once outside that sandbox using the already approved stable
Playwright prefix, as required by the approval-broker policy; the test and
threshold check then passed. This was one existing command class, not a new or
per-action authorization.

A final process audit found no characterization, snapshot host, decoder,
Playwright, Vite, or web-server survivor. `git diff --check` passed. No raw
artifact, timing, result, or authority from the interrupted RA001 command or
either invalid verifier was used.

Findings: none.

`pass`
