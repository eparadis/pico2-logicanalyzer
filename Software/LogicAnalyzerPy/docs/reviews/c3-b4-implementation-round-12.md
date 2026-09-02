# C3-B4 hosted-test correction implementation, round 12

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-test
  correction implementor
- Immutable failed verifier commit/tree:
  `773460d980349d6449cb2f522558ad2f03808f9a` /
  `bc9a166ca8222764f4a1751a142a3a948fb2d84a`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Timestamp: `2026-09-02T07:06:52Z`

## Failed hosted evidence disposition

The preserved exact GitHub Actions run `33599975263`, job `100151298994`,
passed bootstrap and static gates. Its Python gate failed after 657.69 seconds
with `3 failed, 1457 passed, 4 skipped, 33 deselected`.

1. The actual-child private-deadline test correctly proved its deliberately
   tiny 200 ms deadline, but incorrectly reused that loaded-runner profile for
   its post-timeout recovery probe. Recovery raised `RunnerFailure: worker
   request discarded`.
2. Round 10's clean-venv execution test remained bound to the superseded local
   uv-managed interpreter and was missed from the transparent partition.
3. Round 11's artifact reproduction test required verifier-private
   `.tmp/c3-b4-ci/round11` bytes that do not exist in a clean hosted checkout,
   despite the workflow-provided archive and interpreter being present.

## Implementation and validation

The actual-child deadline proof still launches `hang` with the deliberately
small private profile (`wall_deadline_ms=200`, `terminate_grace_ms=20`) and
still requires `RunnerFailure`. Only its subsequent recovery probe now uses the
governed default profile. This tests recovery independently of transient hosted
load and does not change a product limit, threshold, or implementation byte.

The missed immutable round-10 uv-managed venv execution node is transparently
deselected. It cannot describe the accepted direct-artifact bootstrap and is
not replaced by a weaker runtime assertion.

Round 11's dynamic artifact test no longer names verifier-private repository
scratch. When both workflow-provided `PICO_LA_PYTHON_ARCHIVE` and
`PICO_LA_PYTHON` are present, it validates the actual hosted archive size,
SHA-256, `python/` layout, executable, exact accepted `sys.version`, and x86_64
architecture. If neither variable is present, ordinary local broad validation
reports a specific pytest skip while the immutable URL, checksum, extraction,
and ordering remain statically selected. Supplying only one variable fails.
The committed round-11 review retains the independent local reproduction
evidence.

Adding the named round-10 selector changed four immutable round-11 identity
assertions exactly as predicted: candidate/workflow digest, exact prior
partition, exact six-node round-10 suffix, and candidate-qualified collection
counts. Root authorized those four nodes in that order. No other selector or
module disposition was added. Round 11 contains 10 tests; with four disposed,
all six remaining behavior/scope nodes are retained.

The final workflow partition contains 15 ordered ignores and 37 unique ordered
selector strings representing 38 cases. The final exact broad result was
`1497 collected / 38 deselected / 1459 selected`; `1452 passed, 7 skipped, 38
deselected, 106 warnings in 233.00s`. The additional seventh skip is the
explicit local no-workflow-environment artifact classification. Hosted
artifact-byte behavior was separately exercised with the exact ignored
archive and extracted interpreter and passed.

Focused results:

- initial correction/R11 analysis: `8 passed, 1 skipped, 4 failed`; the four
  failures were exactly the authorized stale identities;
- hosted-style artifact environment, corrected deadline test,
  implementation regression, and all selected round-11 nodes: `9 passed, 4
  deselected in 1.42s`;
- final implementation workflow regression: pass;
- Ruff on all changed Python tests: pass; and
- `git diff --check`: pass.

Changed paths and pre-commit hashes:

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`;
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `69d3de7d2eba27f0557835ae248e1b14d06832de4b31e6993db4a2f634ddd777`;
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle3_preexecution_runner.py` —
  `9fa8f300139d9bb66808225a863349132bf29839745d5321597f99c277d80a3d`;
- `Software/LogicAnalyzerPy/tests/verification/test_c3_b4_public_round11.py` —
  `abd5501c44162c0393fa48b9154371b0a9ef7454c20aade8fff8df28228cf7e1`;
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-12.md` —
  this implementation record.

No production, decoder, B1/B2/B3 fixture, limit, threshold, dependency lock,
manifest, contract, or prior evidence byte changed. All scratch remained below
ignored repository `.tmp/`. No network download, hosted retry/dispatch, or
external mutation was performed by this identity.

## Verdict and boundary

The three observed hosted-test defects have bounded corrections and the full
local partition is green. Fresh independent verification and root-owned hosted
dispatch remain required, so the verdict is `candidate-not-accepted`.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.
