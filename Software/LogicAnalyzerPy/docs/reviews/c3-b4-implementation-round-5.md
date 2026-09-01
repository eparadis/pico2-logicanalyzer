# C3-B4 hosted pytest partition implementation, round 5

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-partition
  correction implementor
- Timestamp: `2026-09-01T22:54:22Z`
- Immutable failed accumulated evidence commit/tree:
  `350d6f28acaea4bd14966e01cd93a5a95e799e31` /
  `14f5f7692c7fc3a4c7bca660db73a1029f60b589`
- Independently verified B4 candidate tested by that gate:
  `e3b169f8744c6f4ff80d6a06172d86b14cd49085` /
  `4567fdae34e1a0d37b0e7d5b1fd277f56a2f5737`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted run disposition

The preserved exact-candidate GitHub Actions run
[`33567808584`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33567808584),
job
[`100054884701`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33567808584/job/100054884701),
resolved exact head `e3b169f8744c6f4ff80d6a06172d86b14cd49085` and
concluded `failure`. Exact `x86_64` architecture selection, checkout, Python
3.12, Node 22.14.0, clean locked installs, Ruff, production mypy, and strict
installed-consumer checks passed, closing the preceding arm64-class defect.

Hosted non-hardware pytest then ran the unfiltered command and collected
intentionally superseded B1 verifier modules. Failures included historical Git
revisions unavailable in the shallow checkout and obsolete fixture/import
digest expectations, including
`test_c3_b1_runner_fixture_rebinding_round5.py` and
`test_c3_b1_semantic_fixture_correction.py`. Later workflow steps were skipped.
The failed run is not retried, waived, or represented as product failure or
success by this implementation record.

## Exact bounded correction

The existing non-hardware pytest invocation now includes exactly these 15
accepted superseded-B1 ignores, in the accumulated-gate order and each once:

1. `tests/verification/test_c3_b1_threshold_proposal_round2.py`
2. `tests/verification/test_c3_b1_final_candidate.py`
3. `tests/verification/test_c3_b1_raw_baseline_candidate.py`
4. `tests/verification/test_c3_b1_runner_fixture_rebinding.py`
5. `tests/verification/test_c3_b1_semantic_fixture_candidate.py`
6. `tests/verification/test_c3_b1_threshold_proposal_round3.py`
7. `tests/verification/test_c3_b1_preexecution_runner_candidate.py`
8. `tests/verification/test_c3_b1_runner_fixture_rebinding_round4.py`
9. `tests/verification/test_c3_b1_final_candidate_round3.py`
10. `tests/verification/test_c3_b1_runner_fixture_rebinding_round5.py`
11. `tests/verification/test_c3_b1_semantic_fixture_correction_round2.py`
12. `tests/verification/test_c3_b1_runner_fixture_rebinding_round2.py`
13. `tests/verification/test_c3_b1_runner_fixture_rebinding_round3.py`
14. `tests/verification/test_c3_b1_threshold_proposal.py`
15. `tests/verification/test_c3_b1_semantic_fixture_correction.py`

It also includes exactly these three transparent ordered deselections:

1. frozen historical fixture surface:
   `tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`;
2. superseded round-4 exact-candidate workflow digest:
   `tests/verification/test_c3_b4_public_round4.py::test_candidate_binding_and_exact_workflow_digest`;
   and
3. superseded round-4 prior-workflow-byte restoration:
   `tests/verification/test_c3_b4_public_round4.py::test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order`.

The two round-4 nodes are candidate identity assertions over the workflow
before this authorized partition correction; they are not behavior/scope
waivers. No other ignore or deselection is present. The implementation
regression enumerates every current B2 private-host module, all eight B3
conformance modules, and the B4 implementation plus all four existing verifier
rounds. It requires every path to exist, proves none is ignored, permits exactly
the two named round-4 nodes, and keeps the other three round-4 tests collected.

The `macos-15-intel` runner, pre-checkout `x86_64` guard, pytest sanitizer and
failure annotation behavior, every other workflow command/step/order, and all
product bytes remain unchanged.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `5c6b9cb1904d2096592bfc13e3854df24ddf84cba921df320556555b457eacff`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `88c0995a0c03409e16ac1c4243394381c7757bde02e5f25e91df326c17b32a77`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-5.md` —
  this handoff record

No product, fixture, limit, threshold, dependency, lock, manifest, contract,
or prior verifier/accumulated evidence changed.

## Commands and exact results

- Missing-behavior workflow regression before correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 failed in 0.05s`; the
  parsed ignore tuple was empty rather than the accepted 15 paths.
- The focused workflow regression after the complete three-deselection
  correction: `1 passed in 0.04s`.
- Exact accepted partition with `--collect-only -q`: exit 0;
  `1429/1432 tests collected (3 deselected) in 0.81s`. Output included the
  round-4 module and all current B2/B3/B4 modules; only the exact ordered three
  nodes above were deselected.
- The first direct current B2/B3/B4 module sweep before the two round-4
  deselections were authorized produced
  `801 passed, 2 failed in 111.01s`. Both failures are deliberately preserved
  immutable round-4 verifier sensitivity, not product regressions:
  `test_candidate_binding_and_exact_workflow_digest` pins the prior workflow
  SHA-256 `3df72bff...602f0e`, and
  `test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order`
  requires the prior workflow bytes after removing only the round-4 runner
  correction. Both correctly detect this newly authorized partition change.
  They were not edited, ignored, deselected, or reported as passing; fresh
  instruction then authorized their transparent superseded-candidate
  disposition.
- Final direct sweep using the exact 15-ignore/three-deselection partition and
  explicitly collecting the fixture-surface module, workflow regression, every
  current B2/B3 module, the B4 implementation, and the complete round-4 module:
  `812 passed, 3 deselected in 111.27s`. This is green with exactly the three
  declared deselections; the remaining round-4 behavior/scope tests passed.
- Ruff over the changed implementation workflow test: pass.
- `git diff --check`: pass.

No hosted CI was dispatched. No network, external mutation, or approval was
used.

## Verdict and boundary

The wrong hosted pytest partition is corrected in the worktree. A new
immutable candidate, fresh independent verification that preserves and
dispositions the prior exact-byte assertions, complete accumulated validation,
and orchestrator-owned exact-candidate hosted dispatch remain required. This
identity does not accept its own change or claim that either failed hosted run
now passes.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
