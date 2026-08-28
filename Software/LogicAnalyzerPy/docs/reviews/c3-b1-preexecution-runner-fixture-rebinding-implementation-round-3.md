# C3-B1 pre-execution runner fixture rebinding — implementation round 3

## Subject and disposition

- Implementor: `c3-b1-pre-execution-runner-implementor-replacement-4`.
- Finding disposition: `C3B1-RA001`, replacement candidate after the runner
  accumulated-order violation.
- State: **implementation ready; candidate-not-accepted**.
- Verdict: **pass** for this record-only implementation handoff. Fresh
  verification, clean pre-acceptance-safe accumulation, and fresh acceptance
  remain required.

This replacement candidate adds only this record around the byte-unchanged
reviewed runner candidate `55d22640334ef05176568f275c3e4e7ec63c3336` /
tree `b96790c572f2fceda4445f55d8373b9a21e2cd9d`. The immutable verifier at
`570cfe8a0977d8d3e9d5198d671cd157ce1b6696` is cited only as a historical
`pass` for that now-superseded candidate; its verdict does not transfer.

The immutable `C3B1-RA001` `changes_required` record is committed at
`91ee8f818ce6bb26196d673cdf6975e9a7248d6a`. It conservatively classifies the
interrupted unfiltered test run as a possible pre-acceptance decoder launch.
That interrupted command supplied no completed result, raw artifact, digest,
timing, count, or pass evidence. No result or authority from that attempt, its
later diagnostic reruns, candidate `55d2264`, or verifier `570cfe8` transfers
to this replacement candidate.

## Exact unchanged bound bytes

The accepted fixture identity remains commit/tree
`3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
`14c010153ea5542617e601e4126047c561a48483`. The binding remains canonical and
retains all 17 positive experiment caps, the closed source/snapshot inventory,
isolated launch protocol, containment, termination, descriptor-close/reap,
recovery, and disabled-characterization behavior.

| Artifact | SHA-256 |
| --- | --- |
| `docs/cycle-3-characterization-method.md` | `f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341` |
| `tools/cycle3_characterize/runner.py` | `0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80` |
| `tools/cycle3_characterize/candidate-binding.json` | `4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7` |
| `tests/implementation/test_cycle3_preexecution_runner.py` | `1511083a3254a44bd95f33f75d9cf5adb022162b20a9e0c274929f4f9325ad19` |
| `testdata/decoders/cycle3/semantic-fixtures.json` | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| `testdata/decoders/cycle3/manifest.json` | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| `testdata/decoders/cycle3/experiment-caps.json` | `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d` |

## Replacement pre-acceptance command partition

The replacement accumulated gate must use an explicit include-only pytest
partition. It may collect the inherited non-hardware regression tests plus the
accepted fixture implementation test, current runner implementation test, and
fresh replacement runner-verifier test. Before execution, root must enumerate
the resulting collection and prove it contains none of these excluded classes:

- every raw-baseline module, including
  `tests/verification/test_c3_b1_raw_baseline_candidate.py`;
- every threshold-proposal module (`test_c3_b1_threshold_proposal*.py`);
- every final-B1 candidate module (`test_c3_b1_final_candidate*.py`);
- every Cycle 3 evidence-manifest, manifest-verification, checkpoint, or final
  accumulated/acceptance execution module;
- every B2 or later Cycle 3 module, including all `test_c3_b2*.py` paths and
  any product/private-host execution path;
- every superseded exact-candidate fixture or runner verifier module;
- any module that imports or invokes the private approved-snapshot entrypoint,
  snapshot-host characterization, raw reproduction, or downstream decoder
  execution.

This is an allowlist boundary, not merely a marker filter. A broad
`pytest -m "not hardware"` command is forbidden before runner acceptance even
if it previously failed closed or is expected to stop at a stale binding. The
safe partition must be assembled from named test paths after static collection
audit; discovery of any excluded module fails before tests start. Ruff, strict
mypy, binding/generator checks, dependency checks, inherited evidence
validators, CLI help, web regressions, and process audits remain separate
commands and convey no decoder/raw authority.

## Focused implementation results

Repository-local Python 3.12 with `PYTHONDONTWRITEBYTECODE=1` was used:

- complete inert implementation runner suite: **177 passed**;
- canonical candidate binding check: **passed**;
- deterministic fixture generator check: **passed**;
- scoped Ruff over the runner tool and implementation runner test: **passed**;
- strict mypy over all seven runner modules: **passed**;
- exact digest, one-new-path scope, status, and `git diff --check` audits:
  **passed**.

Only inert internal hostile/cleanup/recovery probes ran. No raw verifier,
decoder, snapshot-host characterization, B2 path, downstream test module,
external runtime, hardware, or network operation ran. No runner, method,
binding, test, fixture, prior record, progress, raw/threshold/final/manifest,
product, or B2 byte changed. No approval capability was required.
