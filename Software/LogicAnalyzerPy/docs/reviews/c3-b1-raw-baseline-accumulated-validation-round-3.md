# C3-B1 raw-baseline accumulated validation — round 3

## Subject and verdict

- Owner: primary Cycle 3 orchestrator (`/root`).
- Immutable raw candidate commit/tree:
  `d0d9dbe87f7841f09f261556de0909475e048b95` /
  `a749b4e192246afab34eb6f11438d64eaeaa4d0c`.
- Fresh verification commit/tree:
  `17397360770f3aab7d79a479a53499b50a1245cd` /
  `5760b6b003036252b44a110acb6772412ce6b312`.
- Clean clone: `/private/tmp/c3-raw-replacement-final`.
- Completed: `2026-08-28T18:04:04Z`.
- Verdict: **pass**. The exact raw candidate is eligible for fresh independent
  acceptance. This record grants no threshold, operator, final-B1, manifest,
  checkpoint, B2, product, or Cycle 4 authority.

## Immutable evidence and fresh verification

The closed raw artifact SHA-256 values are:

- environment:
  `d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f`;
- requests:
  `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`;
- observations:
  `ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee`;
- hostile observations:
  `af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91`;
- manifest:
  `5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8`.

Collection record SHA-256 is
`75822b3dd81bba77701b57628126cc643b0b96595133d094208ecc152b386e01`.
Fresh verifier test/review SHA-256 values are respectively
`d61e45363cb461a198e5d9c14aea8a7d27543968c9bf2ee79d6b3a38dbd56d3f`
and
`86e5fcece470801f70b44ea4985fcb5c10bde9a4d3e76abdecb1edcaac048da7`.

The verifier's independent run completed exactly 486 child launches and
passed in 101.61 seconds. It reproduced all 63 snapshot semantics and eight
stable count fields, both designed hostile successes, eight classified
hostile failures, every retained recovery, terminate/kill/reap behavior, and
exact two-descriptor closure. Its retained report SHA-256 was
`be83d2258261f4b25c2c518669ab612dd9fc3bd25b835807f0beea3032ca089f`.
All timing/RSS relations remain observations only and did not affect semantic
or stable-count verdicts.

## Exact accumulated Python partition

Before execution, root derived the inventory from the immutable raw candidate
and added only the replacement raw verifier. The resulting **55 modules** were
partitioned into an explicit **40 included** and **15 excluded** set. The
excluded set contains every old raw verifier, runner verifier, threshold
proposal, final candidate, semantic fixture candidate, and superseded C3
module. The optional untracked B2 path was absent and was not copied, read,
imported, collected, or executed.

The exact 40 paths collected **578 tests**. Their uninterrupted clean-clone
execution produced **572 passed**, **6 inherited classified skips**, and
**106 warnings** in 125.45 seconds. This included a second complete fresh
486-launch raw reproduction. Root's accumulated reproduction report SHA-256
was
`803f782833bd2df41fda9446ec883d0b8952b01c25d25657f5341ac544eb9a99`.
The skips were two sandbox-prohibited inherited loopback checks and four
optional Cycle-2 physical-artifact cases. No threshold, final-candidate, B2,
or superseded C3 test was collected or executed.

## Static, contract, CLI, and web accumulation

All remaining applicable gates passed:

- `pip check`; whole-project Ruff; and strict mypy over **28 source files**;
- canonical binding and deterministic fixture generator checks;
- six Cycle-2 evidence manifests validated separately against their schema;
- installed `pico-la --help` bounded command surface;
- Node 22 ESLint and TypeScript checks;
- Vitest: **3 files / 5 tests passed**;
- deterministic Vite production build: **29 modules transformed**, followed
  by the committed asset drift check;
- isolated maximum-width Playwright gate: **1 passed**;
- separate live/shell Playwright gate: **3 passed**;
- isolated B6 performance Playwright gate: **1 passed**, followed by the
  accepted B5 threshold checker. Performance-report SHA-256:
  `514932bc7c9a4c974fb9097f5e515f7701e18b8a704d26abe763534373ceec4a`.

The browser gates reused the single previously approved stable Playwright
command class. No per-action approval class was introduced. Final process and
tool-inventory audits found no characterization, snapshot host, worker,
collector, decoder, browser, Vite, or web-server survivor and no runner
bytecode cache. `git diff --check` passed.

The four discarded write-at-end collection attempts remain disclosed only as
history; none of their output, timing, memory, digest, count, or authority was
used. The three pre-existing untracked B2 paths in the main worktree remained
untouched.

Findings: none.

`pass`
