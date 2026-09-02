# C3-B4 hosted Python environment implementation, round 9

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-environment
  correction implementor
- Timestamp: `2026-09-02T01:30:32Z`
- Immutable failed evidence commit/tree:
  `5cc615044c0bcaac6f640e5decc74503025745f3` /
  `1734e85ad0b5552aaf04539ff9ad810b9cbb1647`
- Exact hosted evidence commit/tree:
  `68ccf70dbdfd2d1312c16a3b601847913e9d003b` /
  `2914e14ea131d20b271cd79d021cd87b9c4c6d5b`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted evidence disposition

The preserved exact-candidate GitHub Actions run
[`33578403022`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33578403022),
job
[`100087285659`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33578403022/job/100087285659),
resolved exact head `68ccf70dbdfd2d1312c16a3b601847913e9d003b` on
the governed `macos-15-intel` runner and concluded `failure`.

The workflow's floating setup-python value `3.12` resolved CPython 3.12.10.
The accepted raw B1 evidence binds exact CPython 3.12.13, so the immutable
`test_c3_b1_raw_baseline_candidate_replacement.py::test_candidate_identity_digest_environment_schema_and_summary_arithmetic`
correctly failed. The hosted result was `1 failed, 1446 passed, 4 skipped, 18
deselected`. This is an environment mismatch, not a decoder or verifier defect.

## Exact bounded correction

The sole setup-python value changes from floating `3.12` to exact accepted B1
`3.12.13`. The implementation regression requires the exact setup block once,
rejects the floating value everywhere, and proves setup precedes clean core
environment creation.

Exact Node 22.14.0, full-history checkout, job-wide bytecode suppression,
`macos-15-intel` and its architecture guard, the one three-case inherited-
SIGTERM focused command, focused-success gate, 1,300-byte diagnostic tail,
redaction, log/status/failure exit, all later gates and their ordering, and all
product bytes remain unchanged. The accepted raw B1 replacement verifier is
neither ignored nor deselected and passed both broad executions.

The first exact broad execution used the unchanged 17-selector partition and
identified exactly two immutable round-8 workflow identity assertions:

1. `tests/verification/test_c3_b4_public_round8.py::test_candidate_tree_and_workflow_digest_are_exact`
   pins the prior workflow digest; and
2. `tests/verification/test_c3_b4_public_round8.py::test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged`
   restores round-7 bytes and therefore retains the prior floating Python
   value.

Appending those two selectors necessarily makes the round-8 exact-partition
identity assertion stale. Root authorized appending this third exact node:

3. `tests/verification/test_c3_b4_public_round8.py::test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases`.

No other disposition was added. The final partition has 20 ordered unique
selector strings and 21 deselected cases; the only parameter expansion remains
the original two-case forced-kill function. The other six round-8 nodes remain
selected and passed. No module is ignored.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `b25d28ae03bc203dccc819d90aca8f76199e2b034e5b5e7b94575e2ed4a64a84`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `e48ba90ad513c0c3b8c2e050c818dfbf74415fac6357234e374712f0b8280c5d`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-9.md` —
  this handoff record

No product, B1/B2/B3 test, prior verifier, fixture, limit, threshold,
dependency, lock, manifest, contract, or prior evidence byte changed.

## Commands and exact results

- Missing-behavior workflow regression before correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 failed, 1 passed in
  0.08s`; exact Python 3.12.13 setup was absent.
- Final workflow regression:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `2 passed in 0.05s`.
- Exact focused command in a bash child inheriting ignored SIGTERM: `3 passed
  in 0.25s`.
- First exact broad run with the unchanged 17 selector strings collected 1,469
  items, selected 1,451, and produced `1445 passed, 4 skipped, 18 deselected,
  2 failed in 229.96s`. The only failures were the two exact round-8 identity
  assertions above; no product, accepted B1, or retained behavior node failed.
- Final exact broad workflow partition using 15 ordered ignores and 20 ordered
  selectors: collection was `1469 items / 21 deselected / 1448 selected`;
  result was `1444 passed, 4 skipped, 21 deselected, 149 warnings in 228.98s`.
  The four skips were classified optional machine-local physical-artifact
  checks. All six retained round-8 nodes and the accepted raw B1 replacement
  verifier passed.
- `.venv/bin/python -m ruff check
  tests/implementation/test_cycle2_workflow.py`: pass.
- `git diff --check`: pass.

No scratch artifact was created, inside or outside repository `.tmp/`. No
network, hosted dispatch, external mutation, approval, or escalation was used.

## Verdict and boundary

The hosted setup now requests the exact accepted B1 Python environment, and the
focused plus broad local partition is green. A fresh immutable candidate,
independent verification, complete accumulated validation, and orchestrator-
owned exact-candidate hosted dispatch remain required. This identity does not
accept its own change or claim the prior hosted run now passes.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
