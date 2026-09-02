# C3-B4 hosted SIGTERM isolation implementation, round 8

- Identity and role: `c3-b4-public-implementor-1`; bounded evidence-backed
  hosted-harness correction implementor
- Timestamp: `2026-09-02T00:59:38Z`
- Immutable failed evidence commit/tree:
  `b2b7fa24d0b90c96fb8da7295b861eb8021102f0` /
  `12af9ea8887596c2354f17629cf1862cc987919a`
- Exact hosted evidence commit/tree:
  `0bbc93dd722105f1080096454140c610b8843057` /
  `d943802b2913a3c67ba6c435c01ed03215dae734`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted evidence disposition

The preserved exact-candidate GitHub Actions run
[`33576227664`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33576227664),
job
[`100080675146`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33576227664/job/100080675146),
resolved exact head `0bbc93dd722105f1080096454140c610b8843057` on
the governed `macos-15-intel` runner and concluded `failure`.

The corrected 1,300-byte annotation identified the exact previously hidden
failure:

`tests/verification/test_c3_b2_private_host_round3.py::test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation`

Its child exited during terminate before its Python script installed its own
SIGTERM-ignore handler. The immutable observation was
`terminate_to_reap_ns=1337415` and `kill_to_reap_ns=0`, while the test requires
a positive kill-to-reap interval. A retained round-7 subprocess check reported
the same underlying race, not a second product defect. The hosted result was
`2 failed, 1442 passed, 4 skipped, 12 deselected`.

## Exact bounded correction

The one existing focused pytest command, already inside the single bash
subshell whose first operation is `trap '' TERM`, now has exactly two ordered
node selectors:

1. the existing two-parameter implementation forced-kill function; and
2. the evidence-backed singleton round-3 real-timeout function named above.

The command therefore executes exactly three cases once. The singleton is then
transparently deselected from the broad command, so it cannot execute twice.
Focused status is captured once and the broad command remains lexically inside
the focused-success branch. There is one focused pytest process, one broad
pytest process, no retry loop, and the same log/status/failure-exit path.

The exact 1,300-byte diagnostic tail, printable filtering, redaction,
3,952-byte worst-case escaped annotation bound, full-history checkout,
job-wide bytecode suppression, Intel guard, and all product gates remain
unchanged.

The correction appends exactly four newly stale round-7 identity assertions
after the prior 11 selectors and the newly focused singleton:

1. candidate tree/workflow digest;
2. prior redaction/workflow byte restoration;
3. exact prior 11-selector/12-case partition; and
4. the assertion that the second SIGTERM node remains selected.

The first exact broad run also proved one additional unavoidable stale round-6
node:

`tests/verification/test_c3_b4_public_round6.py::test_focused_gate_is_once_no_retry_and_broad_only_on_success`

That immutable assertion requires the old literal adjacency where the original
focused selector is immediately followed by `--tb`. Placing the authorized
singleton as the second selector necessarily invalidates that exact string.
Root authorized this one transparent selector after the initial broad result;
it is appended after the preceding 16 and is the only additional disposition.

The final partition has 17 ordered unique selector strings and 18 deselected
cases. The sole expansion remains the original two-parameter forced-kill
selector. Six other round-6 nodes and six other round-7 nodes remain selected
and passed. No module is ignored, and no B2/B3 product or test byte changed.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `9e427b6090f01a2506570246189df20ced8a077b25877d1e57af374e6c0e7805`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `a50db6ee11670124e0da72e1446753590772179398a9ca53014dc9b35aac2526`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-8.md` —
  this handoff record

No product, B2/B3 test, prior verifier, fixture, limit, threshold, dependency,
lock, manifest, contract, or prior evidence byte changed.

## Commands and exact results

- Missing-behavior workflow regression before correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 failed, 1 passed in
  0.07s`; the exact two-selector focused command was absent.
- Final workflow regression:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `2 passed in 0.05s`.
- Exact focused command in a bash child inheriting ignored SIGTERM, selecting
  the existing parametrized function followed by the evidence-backed
  singleton: `3 passed in 0.24s`.
- Initial broad run using 16 selector strings collected 1,460 items, selected
  1,443, and produced `1438 passed, 4 skipped, 17 deselected, 1 failed in
  229.48s`. The sole failure was the obsolete round-6 literal adjacency
  assertion documented above; no product or retained behavior node failed.
- Final exact broad workflow partition using 15 ordered ignores and 17 ordered
  selectors: collection was `1460 items / 18 deselected / 1442 selected`;
  result was `1438 passed, 4 skipped, 18 deselected, 149 warnings in 229.25s`.
  The four skips were classified optional machine-local physical-artifact
  checks. All retained round-6 and round-7 nodes passed.
- `.venv/bin/python -m ruff check
  tests/implementation/test_cycle2_workflow.py`: pass.
- `git diff --check`: pass.

No scratch artifact was created, inside or outside repository `.tmp/`. No
network, hosted dispatch, external mutation, approval, or escalation was used.

## Verdict and boundary

The exact governed hosted startup race is isolated without changing the
immutable test or host implementation, and the focused plus broad local
partition is green. A fresh immutable candidate, independent verification,
complete accumulated validation, and orchestrator-owned exact-candidate hosted
dispatch remain required. This identity does not accept its own change or
claim the prior hosted run now passes.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
