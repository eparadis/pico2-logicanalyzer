# C3-B1 raw-baseline acceptance — round 3

Verdict: `pass`.

## Immutable subject and scope

- Acceptance identity: `c3-b1-raw-baseline-acceptance-replacement-1`.
- Raw candidate commit/tree:
  `d0d9dbe87f7841f09f261556de0909475e048b95` /
  `a749b4e192246afab34eb6f11438d64eaeaa4d0c`.
- Fresh verifier commit/tree:
  `17397360770f3aab7d79a479a53499b50a1245cd` /
  `5760b6b003036252b44a110acb6772412ce6b312`.
- Root accumulated-pass commit:
  `7295e4d`.
- Accumulated record SHA-256:
  `b8bc5373d708a69a8d121c9aca28c29ca5bf35f4e4bb84f32f9bf4b62b7467da`.

The candidate is an ancestor of the verifier, and the verifier is an ancestor
of the accumulated pass. The candidate commit changes only four documents in
the closed raw set plus its collection record; `requests.json` is the fifth
closed raw artifact and remains byte-identical because the independently
derived requests did not change. The verifier owns only its replacement test
and review, and the accumulated commit owns only its accumulated review.

This acceptance owns only this review. It did not edit the candidate, verifier,
fixture, runner, threshold, final, product, B2, hardware, network, or Cycle 4
state. It did not read or execute B2 and did not execute a raw reproduction,
threshold check, final gate, product route, or downstream route.

## Identity and artifact closure

The accepted runner candidate is
`380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` /
`aa55b4884c39981026ba233b48dc8f360d404c8a`; its accepted chain is
`01f059cb5f60e885c7d19e8bf5376bdb27dcca19` /
`1c15252a26e5a4af571228dbf37999e385026f87`. The corrected semantic-fixture
candidate is `3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
`14c010153ea5542617e601e4126047c561a48483`. Both accepted identities precede
the raw candidate, and the raw manifest closes over their exact identities and
digests.

The five raw SHA-256 values independently recomputed at acceptance are:

- environment: `d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f`;
- requests: `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`;
- observations: `ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee`;
- hostile observations: `af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91`;
- manifest: `5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8`.

The collection review SHA-256 is
`75822b3dd81bba77701b57628126cc643b0b96595133d094208ecc152b386e01`.
The verifier test/review SHA-256 values are respectively
`d61e45363cb461a198e5d9c14aea8a7d27543968c9bf2ee79d6b3a38dbd56d3f`
and
`86e5fcece470801f70b44ea4985fcb5c10bde9a4d3e76abdecb1edcaac048da7`.

## Static acceptance audit

The permitted static replacement-verifier slice passed **3 tests**, with its
complete reproduction test explicitly deselected. It validated canonical
encoding, closed schemas for the environment, requests, observations, hostile
observations, and manifest, exact manifest closure, 63 unique timeline
identities, five retained repetitions, ten hostile kinds, all min/median/max
summary arithmetic, 17 production caps, nine frozen source digests, and
non-vacuous rejection of manifest, snapshot-summary, and hostile-cleanup
mutations.

The verifier independently derives all 63 requests only from timeline
transitions, physical-channel mapping, sample count, samplerate, options, and
provenance source sets before comparing them with the closed requests artifact.
Expected calls, records, waits, typed vectors, goldens, historical observations,
and historical timings are not derivation inputs.

The collection records exactly 486 complete-collection launches: 378 snapshot,
60 hostile, and 48 recovery launches. A fresh independent verifier reproduction
records another 486 launches, and root's clean accumulated gate records a
second independent 486-launch reproduction. Across those accepted records, all
63 semantic results and eight stable count fields reproduced, both designed
hostile successes completed, all eight expected failures were classified, all
retained recoveries succeeded, children were reaped, and each child closed two
protocol descriptors. Timing and RSS triples and their range relations remain
transparent observations only; none was treated as a threshold or semantic
verdict input.

The accumulated gate derived an explicit 40-module include-only partition from
55 modules, collected 578 tests, and completed with 572 passed, six inherited
classified skips, and 106 warnings. Its clean-clone static, fixture, binding,
CLI, web, performance, process, inventory, cache, and `git diff --check` gates
all passed. It records no surviving characterization, snapshot-host, worker,
collector, decoder, browser, Vite, or web-server process and no runner bytecode
cache.

The collection's four pre-write attempts and all 847 launches from them are
explicitly disclosed and discarded. No output, timing, memory, digest, count,
or authority transferred from those attempts. The accepted runner and fixture
gates precede raw execution; fresh raw verification precedes accumulated
validation; this acceptance follows that accumulated pass. The required gate
ordering is therefore intact.

One initial local static-test invocation was made from the repository root and
failed during collection because the project-local `tools` package was absent
from its import path. It collected and executed zero tests and launched no raw
reproduction. The same explicitly deselected static slice was then invoked
from `Software/LogicAnalyzerPy` with `PYTHONPATH=src` and passed 3 tests with 1
deselected.

## Authority

This verdict accepts only the exact raw evidence commit/tree and evidence chain
named above. It authorizes preparation of a fresh numeric-threshold proposal.
It grants no threshold verdict, operator approval, final-B1 authority, manifest,
checkpoint, B2, product, hardware, network, or Cycle 4 authority.

Findings: none.

`pass`
