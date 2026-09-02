# C3-B4 hosted diagnostic implementation, round 7

- Identity and role: `c3-b4-public-implementor-1`; bounded evidence-first
  hosted-diagnostic correction implementor
- Timestamp: `2026-09-02T00:27:18Z`
- Immutable failed evidence commit/tree:
  `79ee8e6b004e21d20fd3fc15bec7d6bd45bdbf12` /
  `dde6925259841d86f48c9a16570afc544e237366`
- Exact hosted evidence commit/tree:
  `a75874236e1d15dfa3abe969aafa27140a78253c` /
  `7e099b2a92ea6776f38409143e025dec749736aa`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted run disposition

The preserved exact-candidate GitHub Actions run
[`33573907523`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33573907523),
job
[`100073568756`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33573907523/job/100073568756),
resolved exact head `a75874236e1d15dfa3abe969aafa27140a78253c` on
the governed `macos-15-intel` runner and concluded `failure`. Guard, full
checkout, setup, locks, Ruff, production mypy, strict consumer mypy, and the
focused inherited-SIGTERM proof passed. The broad gate collected 1,449 items,
deselected nine, selected 1,440, and failed after approximately six minutes.

The public error annotation is exactly 4,096 characters and ends at 56 percent
of the run. The workflow sanitized the final 12,000 raw bytes, then GitHub
retained the annotation prefix rather than the final failure report. The exact
failing node therefore remains unknown. This implementation does not infer it
from unrelated or non-governing execution.

## Evidence-first bounded correction

The sanitizer's byte tail is reduced from 12,000 to 1,300. Redaction,
printable-byte filtering, log capture, shared focused/broad status, report
printing, GitHub escaping, failure annotation, and nonzero exit remain
unchanged. There is no retry or alternate result path.

The 1,300-byte ceiling is deliberately below 4,096 rather than equal to it.
Every allowed raw byte can expand by at most three characters during the
existing GitHub escaping (`%` to `%25`, CR to `%0D`, and LF to `%0A`). Thus the
worst escaped report is 3,900 ASCII bytes. Including the exact 51-byte command
prefix and terminating LF produces an exact worst-case command length of 3,952
bytes, safely within 4,096. Since the sanitizer keeps the tail, a pytest final
failure-summary suffix remains present.

The implementation regression proves the exact 1,300-byte workflow bound,
rejects the prior 12,000-byte value, constructs the worst-case percent-only
report and obtains exactly 3,952 bytes including wrapper, and proves a modeled
final `FAILED ...` summary remains the suffix after byte-tail selection.

The correction appends only these three now-stale round-6 workflow identity
selectors after the existing ordered eight:

1. `tests/verification/test_c3_b4_public_round6.py::test_candidate_tree_and_workflow_digest_are_exact`
2. `tests/verification/test_c3_b4_public_round6.py::test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases`
3. `tests/verification/test_c3_b4_public_round6.py::test_runner_guard_and_every_other_gate_byte_are_preserved`

The resulting 11 ordered unique selectors expand to 12 deselected cases only
because the existing focused forced-kill selector has two parameters. The
other seven round-6 tests remain selected and passed. Every B2/B3/B4 module
remains unignored.

The diagnostic-only Python 3.14 stress observation is not promoted to governing
evidence. In particular,
`tests/verification/test_c3_b2_private_host_round3.py::test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation`
is neither focused nor deselected by this correction; it remained selected and
passed in the exact broad run. A fresh exact hosted diagnostic must identify
the failure before any additional isolation is considered.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `7b74489c4f540a8e1a5281ae642fd77b6f8a00b403346287c40480ee49655576`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `e89b45a9c7f612c48a10cfd8ffe2761b3d2456a4308b36c061cdb0692dad635e`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-7.md` —
  this handoff record

No product, B2/B3 test, prior verifier, fixture, limit, threshold, dependency,
lock, manifest, contract, or prior evidence byte changed.

## Commands and exact results

- Missing-behavior workflow regression before correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `2 failed in 0.07s`; the
  workflow still used 12,000 bytes and lacked the exact three stale selectors.
- Final focused workflow regression:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `2 passed in 0.02s`.
- Exact broad workflow partition using the ordered 15 ignores and ordered 11
  selectors: collection was `1450 items / 12 deselected / 1438 selected`;
  result was `1434 passed, 4 skipped, 12 deselected, 149 warnings in 236.93s`.
  The four skips were the classified optional machine-local physical-artifact
  checks. All seven retained round-6 checks and the unisolated second SIGTERM
  node passed.
- `.venv/bin/python -m ruff check
  tests/implementation/test_cycle2_workflow.py`: pass.
- `git diff --check`: pass.

No scratch artifact was created, inside or outside repository `.tmp/`. No
network, hosted dispatch, external mutation, approval, or escalation was used.

## Verdict and boundary

The annotation truncation defect is corrected in the worktree. A fresh
immutable candidate, independent verification, complete accumulated
validation, and orchestrator-owned exact-candidate hosted dispatch are required
to reveal the previously hidden failure. This identity does not accept its own
change and does not claim the prior hosted failure now passes.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
