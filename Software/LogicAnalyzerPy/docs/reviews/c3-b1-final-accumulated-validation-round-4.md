# C3-B1 replacement final accumulated validation — round 4

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable replacement candidate/tree:
  `7246dcbe55a60ef7ee9196f4bf265c7c75141d55` /
  `51e895a1e2c95580d04bc8a31ed8d58a85613e1a`.
- Fresh verification descendant/tree:
  `e1b87533d09d716634095ebb8d5748cf4b857c98` /
  `a31ff03e22bc516f0d712c59fc8ab09aa6496464`.
- Clean clone: `/private/tmp/c3-final-r4`.
- Completed: `2026-08-28T20:07:58Z`.
- Verdict: **pass**. No applicable mandatory gate failed or remained skipped.

This gate authorizes only fresh independent replacement final-B1 acceptance.
It creates no manifest, checkpoint, B2 authority, product enforcement,
distribution authority, non-macOS claim, or Cycle 4 authority.

## Exact candidate and verification

The candidate JSON and rationale remain byte-identical to immutable candidate
`7246dcb`, at SHA-256 values
`a186af26805c804613271641e5f57b1393ae31d79fa800a29249e37efc0650fd`
and
`591459742b9453e94047438ec79a6e2bdd54ed3b6d0c71207bbae4c64b563d73`.
Status remains `candidate-not-accepted`.

Fresh verifier `c3-b1-final-verifier-replacement-1` added only its verifier
test and round-5 record. Their SHA-256 values are respectively
`56a4892a9a25ace4a7cc6ec640ab12e1669ad56f7e345410c5e26eb9e9d8b32b`
and
`b3eb336c66ab35d1ef7981477bcc97267ad144f387b9b922547402fae7ad9378`.
Its focused static suite passed 22 tests, covering 38 live digest bindings,
the exact 29 approved limits and boundaries, all current identities and
ordered invalidations, frozen commands/applicability, exclusions, and 20
direct negative-mutation families. Findings: none.

## Exact accumulated Python 3.12 gate

Root derived the inventory from the immutable verifier descendant before
execution. Exactly 57 tracked test modules partitioned into 42 included and 15
excluded modules. The included set is the accepted round-4 proposal partition
plus only the new final verifier. It contains the current fixture and runner
implementation modules, corrected-fixture replacement raw verifier, round-4
proposal verifier, and round-4 final verifier. Optional untracked B2 was absent
and was not copied, read, imported, or executed.

The exact 42 paths collected 630 tests. The accepted run completed with **624
passed**, **six inherited classified skips**, **106 warnings**, and no failure
in 121.76 seconds. It included the complete 486-launch replacement raw
reproduction and all 30 threshold and 22 final-verifier tests. Reproduction
report SHA-256 is
`e814352ee573f9c5ce2b80eea11e2d46fc320999d681dc523a6b3a199cc4a255`.

The 15 excluded modules are historical, superseded, or non-active exact-subject
C3 verifier routes under the frozen include-only partition:

```text
tests/verification/test_c3_b1_threshold_proposal_round2.py
tests/verification/test_c3_b1_final_candidate.py
tests/verification/test_c3_b1_raw_baseline_candidate.py
tests/verification/test_c3_b1_runner_fixture_rebinding.py
tests/verification/test_c3_b1_semantic_fixture_candidate.py
tests/verification/test_c3_b1_threshold_proposal_round3.py
tests/verification/test_c3_b1_preexecution_runner_candidate.py
tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py
tests/verification/test_c3_b1_final_candidate_round3.py
tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py
tests/verification/test_c3_b1_semantic_fixture_correction_round2.py
tests/verification/test_c3_b1_runner_fixture_rebinding_round2.py
tests/verification/test_c3_b1_runner_fixture_rebinding_round3.py
tests/verification/test_c3_b1_threshold_proposal.py
tests/verification/test_c3_b1_semantic_fixture_correction.py
```

The six skips are inherited and classified: two sandbox loopback checks and
four optional C2-B3 machine-local physical-artifact reruns. Checked-in
sanitized evidence and the mandatory nonhardware paths passed. No Cycle 3
mandatory test was skipped.

### Discarded inventory-selection attempt

Before the accepted run, root made one invalid include-only selection: it used
superseded raw verifier `test_c3_b1_raw_baseline_candidate.py` instead of
current replacement verifier
`test_c3_b1_raw_baseline_candidate_replacement.py`. That command completed
with 623 passed, six inherited skips, and the expected one stale-digest
failure. It is an orchestrator inventory error, not a candidate finding, and
supplies no result or authority. Root corrected exactly that path, repeated
collection (630 tests), and reran the complete gate from the start. No byte or
candidate changed between attempts.

## Static, inherited, and frontend regressions

Python tooling ran from ignored repository-local environment
`Software/LogicAnalyzerPy/.venv`, CPython 3.12.13. Exact source came from the
clean clone through `PYTHONPATH`; no virtual environment was created or run
from `/private/tmp`, no package was installed, and no dependency download was
needed. `requirements-dev.lock` and `pyproject.toml` SHA-256 values remain
`6f78ec8f0219b919c44edb9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
and
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Result |
| --- | --- |
| repository-local `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| mypy over product `src` | exit 0; 21 source files |
| strict mypy over characterization | exit 0; seven files |
| fixture generator `--check` | exit 0; no drift |
| characterization binding `--check` | exit 0; no drift |
| installed CLI help | exit 0 |
| six Cycle-2 evidence validators | exit 0 each |
| exact include-only nonhardware pytest | 624 passed, six classified skips |

Repository-local Node was exactly v22.14.0. `web/package-lock.json` and
`web/production-assets.json` SHA-256 values remain
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
and
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
ESLint and TypeScript passed; Vitest passed three files and five tests; Vite
built 29 modules; and the production-asset checker found no drift.

Browser gates ran only in the established isolated shapes. Maximum-width
passed 1/1, then live/shell passed 3/3. The frozen B6 performance test passed
1/1 and the accepted threshold checker passed report SHA-256
`f5eabd27003fc27f672bcdf6984ca2c042b2fb868a5949294dbe1fb2c093dd87`.
The first maximum-width launch inside the sandbox could not start the required
loopback server and supplies no evidence. Root reran the unchanged command
through one narrowly scoped reusable Playwright approval; that isolated rerun
and all later browser gates passed without further approval requests.

## Scope, cleanup, and disposition

Clean-clone tracked bytes remain unchanged. Its untracked state is limited to
the two validation-only environment/dependency symlinks and generated browser
results. Final process checks found no surviving clean-clone process. Main
worktree preserved B2 paths remain the only untracked content and were neither
inspected nor modified.

No product decoder host, public decode API, external/reference runtime,
hardware/USB/serial action, firmware, package build/publication, non-macOS
claim, B2 execution, or Cycle 4 work occurred. Next authority is fresh
independent replacement final-B1 acceptance.

`pass`
