# C3-B1 semantic-fixture correction accumulated validation — round 1

## Subject and result

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact fixture-correction candidate/tree:
  `a98d328aab92f3dad66988fb70cc567946dc89d0` /
  `450aadcf26bd6c74860872bfbf0a0a1b32d94f3b`.
- Independent verification: `pass`, descendant commit
  `b708293ec7e2f4f938e6fb6c669304ee2dba8721`; record SHA-256
  `092dadbce88288a544b4c7c14253095a580765501cd60afc6ceaaa5cad3cf2e2`;
  verification-test SHA-256
  `d5a6a3f69fcdaf2b5d86e334d0091c758f7bb67c33b1e9b6bca2c056efe9a75d`.
- Completed: `2026-08-28T04:17:26Z`.
- Result: **pass for the reopened semantic-fixture gate**. The complete
  candidate-applicable gate passed. Downstream B1 runner, raw, proposal,
  approval, final-binder, manifest, and checkpoint suites deliberately reject
  the changed fixture/cap identity and remain ordered correction work; no old
  pass transfers and this result grants no B2 authority.

The exact candidate was validated from clean detached clone
`/private/tmp/c3-fixture-correction-a98d328`, not from the main worktree that
preserves untracked B2 work. The clone's tracked tree remained identical to
the candidate. Its only untracked validation state was a `.venv` link to the
stable clean environment and ignored Playwright `test-results` output.

## Clean Python 3.12 gate

Environment: macOS x86_64; managed CPython 3.12.13; freshly cleared stable
environment `/private/tmp/cycle3-clean-python`; pip 25.0.1. The development
lock SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Exact result |
| --- | --- |
| CPython 3.12 `-m venv --clear /private/tmp/cycle3-clean-python` | exit 0 |
| clean pip `install --require-hashes -r requirements-dev.lock` | exit 0; cached artifacts matched every lock hash |
| clean pip `install --no-build-isolation --no-deps -e .` | exit 0; `pico-logic-analyzer==0.1.0` |
| clean pip `check` | exit 0; no broken requirements |
| clean Ruff over `.` | exit 0 |
| clean mypy over `src` | exit 0; no issues in 21 source files |
| installed `python -m pico_logic_analyzer --help` | exit 0 |
| generator `--check` | exit 0; byte-identical deterministic artifacts |
| applicable fixture implementation suite | exit 0; 11 passed, one historical inventory assertion deselected |
| independent verifier suite in the evidence descendant | exit 0; 20 passed |
| accepted Cycle 2 evidence validators B1 through B6 | six exit-0 results |

## Full-suite invalidation audit

The unfiltered clean command
`python -m pytest -m 'not hardware' -q` was run first and was not represented
as green: **512 passed and 149 failed**. One failure is the already classified
exact-six-file fixture inventory assertion, which predates this candidate and
rejects four later governing JSON artifacts. The other 148 failures are the
required fail-closed reaction of downstream B1 tests to the changed fixture,
experiment-cap, runner-binding, raw, threshold, final-binder, and evidence
identities. Their first failures explicitly report the old accepted cap digest
instead of the corrected digest; no product regression or unrelated Cycle 1/2
failure was hidden in that set.

The candidate-applicable command then ignored only the six wholly invalidated
downstream B1 modules and deselected only the historical inventory assertion:

```text
tests/implementation/test_cycle3_preexecution_runner.py
tests/verification/test_c3_b1_preexecution_runner_candidate.py
tests/verification/test_c3_b1_raw_baseline_candidate.py
tests/verification/test_c3_b1_threshold_proposal.py
tests/verification/test_c3_b1_threshold_proposal_round2.py
tests/verification/test_c3_b1_final_candidate.py
tests/implementation/test_cycle3_fixtures.py::
  test_cycle3_fixture_surface_is_present_and_rebuildable
```

It passed **403 tests with one deselection** and the accepted 149 inherited
warnings. These exclusions are not waivers or transferred evidence: every
named downstream module must be rebound and rerun in its owning correction
stage before the replacement B1 checkpoint.

## Frozen optional-web regression

The accepted Node executable was exactly v22.14.0 at the stable
`/private/tmp/cycle2-node22` path; `npm ci --no-audit --no-fund` installed 215
locked packages. Exact Node-22 commands then passed:

- ESLint and TypeScript: both exit 0;
- Vitest: three files and five tests passed;
- Vite production build: 29 modules; asset checker exit 0;
- Playwright maximum-width verification: one test passed;
- Playwright live/shell regression: three tests passed;
- Playwright B6 performance: one test passed; frozen threshold checker exit 0.

The retained temporary performance report SHA-256 is
`f623165d9a68e4af67c5872348f607618ae2d9ffcf1a53fc54725698e3808358`.
An initial npm-script performance attempt correctly failed because its child
resolved ambient Node v26.7.0, changing frozen method metadata. It supplied no
pass evidence. The final direct Playwright invocation used the exact Node
v22.14.0 executable and the unchanged checker accepted its report. Loopback
browser commands use the consolidated reusable exact-Node Playwright approval
shape; no repeated broad shell approval was introduced.

## Fixture, oracle, scope, and process closure

- The corrected generator, semantic fixture, experiment caps, and fixture
  manifest recompute at the exact independently verified digests. Provenance,
  option matrix, typed vectors, decoder snapshots, locks, product code, and
  package metadata remain unchanged.
- Expectations remain static source/timeline derivations. No decoder, B2 host,
  characterization runner, raw observation, C#/.NET/pythonnet,
  libsigrokdecode, `sigrok-cli`, or external/reference runtime supplied or
  corroborated expected output.
- No hardware, serial, firmware, live capture, publication, distribution, or
  Cycle 4 work occurred.
- A root-visible process audit after browser/performance completion found no
  retained browser server, decoder, worker, characterization runner, or
  prohibited runtime. Unrelated user-owned Codex, SSH, and 86Box processes
  were not touched.
- The changed experiment caps invalidate the accepted runner binding and all
  later raw/threshold/operator evidence. This gate neither enforces those caps
  nor reuses the earlier operator approval.

Open fixture-candidate findings: none.

`pass`
