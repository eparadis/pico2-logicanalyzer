# C3-B4 hosted x86_64 workflow implementation, round 4

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-environment
  correction implementor
- Timestamp: `2026-09-01T22:29:29Z`
- Immutable failed accumulated/hosted evidence commit/tree:
  `3764a26f5b00ea2cd287a56bfbad512ce8f3a992` /
  `69003cceaaa401247320911cc04fd158a5072168`
- Independently verified B4 product evidence commit/tree consumed by that gate:
  `a076d185fd24e1531e2a76aea70824d0b7659837` /
  `a30b03c6406d33f361634827a246c9dc9a009a05`
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`

## Failed hosted run disposition

The preserved exact-candidate GitHub Actions run
[`33501933713`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33501933713),
job
[`99837032689`](https://github.com/eparadis/pico2-logicanalyzer/actions/runs/33501933713/job/99837032689),
resolved head `a076d185fd24e1531e2a76aea70824d0b7659837` and concluded
`failure`. Environment setup, checkout, Python 3.12, Node 22.14.0, both clean
dependency installs, Ruff, production mypy, and strict consumer checking
passed. Non-hardware pytest then produced repeated B3 UART worker
`HostFailure: process-exit` failures; later CLI, web, frontend, asset, and
browser steps were skipped. This remains failed evidence and is neither retried
nor reclassified by this implementation identity.

The immutable accumulated diagnosis records the retrieved official
[`actions/runner-images`](https://github.com/actions/runner-images#available-images)
inventory: `macos-latest` mapped to macOS 26 arm64, while
`macos-15-intel` mapped to macOS 15 x64. The ignored diagnostic inventory bytes
had SHA-256
`e2282f1ccf4a8c952433ada336e1eeda9eaffe97592c9b9c334fcaac6115f63d`.
That official label evidence explains why a moving arm64 runner could not
transfer the governed macOS x86_64 proof for the exact 64-GiB absolute
`RLIMIT_AS` ceiling.

## Bounded correction

The sole workflow job now uses exact runner label `macos-15-intel` rather than
moving label `macos-latest`. Its first step, before checkout, Python/Node setup,
virtual-environment creation, dependency installation, or test bootstrap,
executes `uname -m` and requires exact `x86_64`. A mismatch emits one fixed
diagnostic and exits 2. Thus future label drift fails before a non-governed
environment can produce apparently transferable product evidence.

Every pre-existing workflow trigger, permission, action pin, Python/Node
version, hash-locked install, product check, sanitizer, CLI, web/frontend,
asset, and browser step remains unchanged and in the same order after the new
guard. No product, decoder, API, CLI, fixture, limit, threshold, manifest,
contract, dependency, or lock changed.

## Changed paths and hashes

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `3df72bff1cde7fdd8619bc74e1f796d9f3d755a5e35a4d4ef2070327fa602f0e`
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `02393c5d907e0c8f4df70c77f67c8f0a0c4d54f44799dd353ee6b9b4820a2298`
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-4.md` —
  this handoff record

Prior verifier, accumulated, acceptance, manifest, and governing evidence was
read but not edited.

## Commands and exact results

- Missing-behavior workflow regression before correction:
  `.venv/bin/python -m pytest -q
  tests/implementation/test_cycle2_workflow.py`: `1 failed in 0.05s`, proving
  the workflow still selected `macos-latest` and lacked the x86_64 guard.
- The same focused regression after correction: `1 passed in 0.02s`.
- Workflow regression plus the complete B4 implementation, all three immutable
  public verifier rounds, and existing CLI tests: `71 passed in 8.74s`.
- Ruff over the changed workflow regression test: pass.
- Installed editable `pico-la decode --help` was not changed or invoked for
  this workflow-only correction; the accumulated regression above covers the
  preserved CLI/product surface.
- `git diff --check`: pass.

No test skipped. No CI was dispatched, no network or external mutation was
performed, and no approval was required.

## Verdict and boundary

The hosted environment-class defect is corrected in the worktree. A new
immutable candidate, fresh independent verification, full accumulated gate,
and orchestrator-owned exact-candidate hosted dispatch remain required. This
identity does not accept its own change or claim that the earlier failed run
now passes.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.

Verdict: `candidate-not-accepted`. `APPROVAL_NEEDED`: none. The worktree is
intentionally unstaged and uncommitted.
