# C3-B1 pre-execution runner fixture rebinding — acceptance round 3

## Subject and verdict

- Acceptor: `c3-b1-pre-execution-runner-rebinding-acceptance-3`.
- Immutable replacement candidate commit/tree:
  `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` /
  `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Fresh verifier-5 pass commit:
  `e95706f10a8a5a2f955e29b23cda25e157bf373e`.
- Root accumulated-pass commit:
  `e1e8bab06ce74cb051f92d8f399153d63824a56a`.
- Completed: `2026-08-28T17:32:37Z`.
- Verdict: **pass**.

This accepts only the exact replacement runner gate. The acceptance becomes
effective when this record is committed, and that acceptance commit first
authorizes a fresh raw characterization against the accepted runner. It does
not transfer any old raw attempt, result, artifact, timing, digest, count, or
authority. It does not authorize B2, thresholds, final B1, manifests,
checkpoints, hardware, or Cycle 4.

## Independent identity and scope inspection

The candidate resolves to the exact named tree and differs from immutable
`C3B1-RA001` record commit
`91ee8f818ce6bb26196d673cdf6975e9a7248d6a` by exactly one new path:
`docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-implementation-round-3.md`.
Its SHA-256 is
`bbf2cb087ec97790c2403b7406560656d84ebb4f600190a3a881c7143fa8bf0e`.
No runner, method, binding, fixture, cap, test, source, launch, worker, probe,
snapshot, product, or B2 byte is part of that replacement delta.

Verifier-5 is an ancestor of the accumulated-pass commit. Its assigned test
and review have independently recomputed SHA-256 values:

- verifier test:
  `f84f123e6f8bbc1c3bcb1063faa11d0177438012db8b6ec314248b8c1d0984b1`;
- verifier review:
  `027d0109336f3f5160a0dc609d2c79cf37722b845d9a050406463d921e4b28c2`.

The accumulated record is the only path added by accumulated commit
`e1e8bab06ce74cb051f92d8f399153d63824a56a`; its SHA-256 is
`aedc2782b3cdeab8334d6d970c5f847da8fe92c7c4595a7bd0b261352d8d5a93`.
It records an explicit 40-path pre-acceptance partition: 585 tests collected,
579 passed, 6 inherited classified skips, and no broad pytest, raw, decoder,
snapshot characterization, B2, or downstream module collected or executed.
Its independent Python, CLI, evidence, Node, browser, performance, process,
and diff checks all passed.

The bound bytes independently recomputed as:

| Artifact | SHA-256 |
| --- | --- |
| `docs/cycle-3-characterization-method.md` | `f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341` |
| `tools/cycle3_characterize/runner.py` | `0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80` |
| `tools/cycle3_characterize/candidate-binding.json` | `4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7` |
| `tests/implementation/test_cycle3_preexecution_runner.py` | `1511083a3254a44bd95f33f75d9cf5adb022162b20a9e0c274929f4f9325ad19` |
| `testdata/decoders/cycle3/semantic-fixtures.json` | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| `testdata/decoders/cycle3/manifest.json` | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| `testdata/decoders/cycle3/experiment-caps.json` | `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d` |

## Finding dispositions

- `C3B1-RA001`: preserved as immutable history. Candidate `55d2264` and the
  interrupted broad command receive no verdict or authority. The exact
  replacement candidate, portable verifier-5, fresh safe accumulation, and
  this independent acceptance complete the required replacement sequence.
- `C3B1-RV002`: verifier-3 remains non-authoritative because its inventory
  required optional untracked B2. No verifier-3 result transfers.
- `C3B1-RV003`: verifier-4 remains non-authoritative because its clean-clone
  assertions still required optional B2. No verifier-4 result transfers.
- Verifier-5 closes the portable evidence requirement from a candidate-tree
  inventory, while testing optional B2 and superseded verifier pathnames only
  synthetically and fail-closed. B2 content was not read or executed here.

## Focused acceptance rerun

Using repository-local Python 3.12 with `PYTHONDONTWRITEBYTECODE=1` and
`PYTHONPATH=src`, acceptance executed only verifier-5 plus the complete inert
runner implementation suite:

- verifier-5: **11 passed**;
- inert/hostile runner implementation suite: **177 passed**;
- focused total: **188 passed** in 15.95 seconds.

Candidate/verifier/accumulated ancestry, exact candidate tree, one-record
replacement delta, assigned evidence digests, bound artifact digests, and
`git diff --check` also passed. No broad pytest, raw baseline,
characterization, snapshot execution, decoder, threshold, final-candidate,
manifest/checkpoint, B2+, hardware, network, or downstream route ran. No
approval capability was required.

Findings: none.

`pass`
