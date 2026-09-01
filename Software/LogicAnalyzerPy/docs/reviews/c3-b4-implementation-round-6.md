# C3-B4 hosted harness implementation, round 6

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-harness
  correction implementor
- Timestamp: `2026-09-01T23:36:18Z`
- Immutable failed accumulated evidence commit/tree:
  `0cbf159b8abfe3f7ad1d8c136f43e9a2b6b8ee7d` /
  `825659122a7a029673fa056e74fc71bd06a4d75c`
- Independently verified candidate exercised by that gate:
  `ec805b506ef18f6fc0844d9586764d35aba021ec` /
  `2591ba20af36d3ce903de21020b62e9dddb65ff7`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted run disposition

The preserved exact-candidate GitHub Actions run
[`33570173317`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33570173317),
job
[`100062197241`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33570173317/job/100062197241),
resolved exact head `ec805b506ef18f6fc0844d9586764d35aba021ec` and
concluded `failure`. Its runner-class guard, setup, Ruff, production mypy, and
strict installed-consumer checks passed. The non-hardware gate failed for
three hosted-harness causes: shallow Git history, Python-created bytecode in a
closed tool inventory, and a startup race in the parametrized forced-kill
cleanup proof. The failed run was not retried, waived, or represented as a
product failure or success.

## Exact bounded correction

The workflow-only correction makes three changes before or within the existing
non-hardware gate:

1. `actions/checkout@v4` now uses `fetch-depth: 0`, making the verifier's
   historical Git assertions available.
2. Job-wide `PYTHONDONTWRITEBYTECODE: "1"` is declared before every workflow
   step and therefore before every Python command. This prevents workflow
   execution from adding bytecode to the closed characterization-tool
   inventory.
3. The existing parametrized forced-kill node runs exactly once as one focused
   pytest command in a bash subshell that first executes `trap '' TERM`.
   Python and the child under test inherit the ignored SIGTERM disposition.
   Focused output appends to the same bounded log as the broad suite, its
   status is captured once, and the broad suite runs only when that status is
   zero. There is no retry. The broad suite then transparently deselects that
   already-executed function.

The 15 accepted superseded-B1 ignores and the preceding three ordered
deselections remain byte-for-byte and order-for-order intact. The forced-kill
function is the fourth selector. Because it has `timeout` and `cancelled`
parameters, that one selector represents two collected cases, both covered by
the preceding focused command.

The first exact broad validation correctly exposed four immutable round-5
checks that bind the prior workflow rather than current behavior. After root
authorized their transparent disposition, these exact selectors were appended
in failing-node order:

1. `tests/verification/test_c3_b4_public_round5.py::test_candidate_binding_and_exact_workflow_digest`
   pins the superseded workflow digest.
2. `tests/verification/test_c3_b4_public_round5.py::test_partition_has_exact_ordered_unique_ignores_and_deselections`
   pins the superseded three-selector tuple.
3. `tests/verification/test_c3_b4_public_round5.py::test_every_candidate_b2_b3_b4_module_is_retained`
   permits only the two prior round-4 selectors and therefore rejects the
   required focused-then-deselected B2 function.
4. `tests/verification/test_c3_b4_public_round5.py::test_partition_is_the_only_workflow_change_from_round4`
   parses the superseded single broad-command redirection and cannot represent
   the required focused status gate.

These are node-level deselections, not module ignores. The other three
round-5 behavior/scope checks remain collected and passed. Every current
B2/B3/B4 module remains collected; the regression explicitly requires the
round-5 module to exist and remain absent from the ignore set. The exact broad
partition has 15 ordered ignores and eight ordered unique node selectors,
which expand to nine deselected cases only because the forced-kill node has two
parameters.

The `macos-15-intel` runner, pre-checkout `x86_64` guard, product gates,
sanitizer and bounded annotation path, all product/decoder/API bytes, fixtures,
limits, thresholds, locks, manifests, and earlier evidence remain unchanged.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `2b7c35159c9f6a6b521830290c4c4a4e17a1f7753911dad97c94161084256d82`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `fb4c19e15f4c19ed928806bde28d704eb0015deeef6fe8aca04f7adbb973dba1`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-6.md` —
  this handoff record

No B2/B3 product, test, or evidence byte changed. No prior verifier,
accumulated evidence, contract, manifest, fixture, dependency, or lock changed.

## Commands and exact results

- Missing-behavior regression before workflow correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 failed in 0.06s`; the
  workflow lacked full checkout, job-wide bytecode suppression, and the
  focused status gate.
- Final implementation-owned workflow regression:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 passed in 0.04s`.
- Focused proof under the hosted signal disposition:
  `/usr/local/bin/bash -c 'trap "" TERM; exec .venv/bin/python -m pytest -q
  tests/implementation/test_c3_b2_private_host.py::test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure
  --tb=short --disable-warnings'`: `2 passed in 0.16s`.
- The first broad run with the mandated fourth selector but before disposition
  of newly stale round-5 identity assertions produced `1426 passed, 4 skipped,
  5 deselected, 4 failed in 233.02s`. The four failures were exactly the nodes
  and causes enumerated above; no product or retained behavior check failed.
- Final exact workflow partition, using the workflow's ordered 15 `--ignore`
  arguments and ordered eight `--deselect` arguments:
  `.venv/bin/python -m pytest -m "not hardware" --tb=short
  --disable-warnings ...`: collection was `1439 items / 9 deselected / 1430
  selected`; result was `1426 passed, 4 skipped, 9 deselected, 149 warnings in
  230.43s`. All three retained round-5 checks passed.
- `.venv/bin/python -m ruff check
  tests/implementation/test_cycle2_workflow.py`: pass.
- `git diff --check`: pass.

No hosted CI was dispatched. No network, external mutation, approval, or
escalation was used. No new scratch artifact was created outside repository
`.tmp/`; this implementation created no explicit scratch artifact at all.

## Verdict and boundary

The three observed hosted-harness defects are corrected in the worktree, and
the focused proof plus exact combined local partition are green. A new
immutable candidate, fresh independent verification, complete accumulated
validation, and orchestrator-owned exact-candidate hosted dispatch remain
required. This identity does not accept its own changes and does not claim the
failed hosted run now passes.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
