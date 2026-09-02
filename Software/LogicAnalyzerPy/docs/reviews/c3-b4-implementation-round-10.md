# C3-B4 hosted managed-Python implementation, round 10

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-environment
  correction implementor
- Timestamp: `2026-09-02T02:01:22Z`
- Immutable failed evidence commit/tree:
  `13f8ef1b1f56594abd70fa631b5d9f1ed6ce09c8` /
  `238fffd0d429df9f5fd7727f298897a88f9625f5`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted evidence disposition

The preserved exact-candidate GitHub Actions run `33580345130`, job
`100093114545`, failed before dependency installation because
`actions/setup-python@v5` could not supply CPython 3.12.13 x64 on the governed
macOS 15 Intel runner. The accepted raw B1 environment instead binds uv-managed
`cpython-3.12.13-macos-x86_64-none`, so substituting another setup-python patch
or weakening the raw verifier was not permissible.

## Exact bounded correction

The unavailable setup-python step is removed. The workflow now uses immutable
`astral-sh/setup-uv@c771a70e6277c0a99b617c7a806ffedaca235ff9` (`v9.0.0`),
requests exact uv `0.12.6`, and disables setup-uv caching. The uv cache and
managed-Python installation roots are job-wide paths below repository
`.tmp/c3-b4-ci/`.

Before any dependency installation, the workflow runs exactly
`uv python install 3.12.13 --no-bin` and checks all accepted runtime identity:
full `sys.version` `3.12.13 (main, Jun 23 2026, 15:54:40) [Clang 22.1.3 ]`,
machine `x86_64`, managed-key base-prefix suffix
`/cpython-3.12.13-macos-x86_64-none`, and `BUILD` value `20260623`. Both
`.venv` and `.venv-web` are created from the same exact absolute managed
interpreter and independently recheck full version and architecture before
their respective hash-locked installs.

Full-history checkout, exact Node 22.14.0, locked installs, the inherited-
SIGTERM focused three-case gate, 1,300-byte diagnostic tail, redaction,
focused-success condition, no retry, and every product gate remain present.
No product, decoder, B1/B2/B3 fixture, limit, threshold, lock, manifest,
contract, or prior evidence byte changed.

## Transparent stale-node disposition

The first exact broad run retained the prior 20-selector partition. It
collected 1,478 items, deselected 21 cases, selected 1,457, and finished with
`1446 passed, 6 skipped, 21 deselected, 5 failed, 106 warnings in 230.09s`.
The failures were exactly the five predicted immutable workflow-identity
assertions:

1. round 4's setup-python-based prebootstrap-order assertion;
2. round 6's literal job-header/setup-python assertion;
3. round 9's exact prior workflow digest;
4. round 9's exact setup-python 3.12.13 block; and
5. round 9's prior-workflow byte-restoration assertion.

Appending those five selectors necessarily invalidated round 9's exact
20-selector/21-case partition assertion. Root had pre-authorized appending that
sixth predicted node only. The final ordered partition therefore contains 26
unique selector strings representing 27 cases; the sole extra case remains the
original parametrized forced-kill node. The five other round-9 behavior and
scope nodes remain selected and passed. The accepted raw B1 replacement
verifier remains selected and passed. No module is ignored.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `f5b2a05ba66d54944e624ee0c6777f39d4cffc8a5aa3bf719086a1f1b28d5cc8`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `b40f0b06505897804b70f5664db227ebb08141efdf9ce5ea231e0683ed401301`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-10.md` —
  this handoff record

## Commands and exact results

- Missing-behavior workflow regression before workflow correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 failed, 1 passed in
  0.07s`; the accepted uv-managed provisioner and identity guards were absent.
- Final workflow regression: `2 passed in 0.06s`.
- Existing local accepted managed interpreter guard: passed for full version,
  x86_64, base suffix, and `BUILD=20260623`.
- Offline clean-venv semantics: the accepted interpreter created independent
  core and web scratch environments below ignored
  `Software/LogicAnalyzerPy/.tmp/c3-b4-ci/`; both exact full-version and
  architecture guards passed without network access.
- Exact focused command in a bash child inheriting ignored SIGTERM: `3 passed
  in 0.25s`.
- First broad run with unchanged partition: the exact result above confirmed
  only the predicted stale identities.
- Final exact broad run with 15 ordered ignores and 26 ordered selectors:
  `1478 collected / 27 deselected / 1451 selected`; `1445 passed, 6 skipped,
  27 deselected, 106 warnings in 229.06s`. The skips were the existing local
  loopback and optional machine-local physical-artifact checks.
- `.venv/bin/python -m ruff check
  tests/implementation/test_cycle2_workflow.py`: pass.
- `git diff --check`: pass.

No network, hosted dispatch, external mutation, approval, escalation, staging,
or commit was used. Newly created scratch was confined to the repository's
ignored `Software/LogicAnalyzerPy/.tmp/c3-b4-ci/` subtree.

## Verdict and boundary

The workflow now has a pinned, accept-or-fail path to the exact accepted
uv-managed CPython rather than an unavailable setup-python artifact. A fresh
immutable candidate, independent verification, complete accumulated
validation, and root-owned exact-candidate hosted dispatch remain required.
This implementation identity does not accept its own changes or predict the
external download succeeds without that hosted proof.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
