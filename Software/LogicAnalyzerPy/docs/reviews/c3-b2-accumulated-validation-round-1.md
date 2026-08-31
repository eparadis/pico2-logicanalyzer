# C3-B2 private host accumulated validation — round 1

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Corrected C3-B1 prerequisite checkpoint: `d4f984d`.
- Exact immutable B2 candidate/tree:
  `d8e14bbe490035894f3103a1289b27464a89d0d6` /
  `0ca3d0aec612183e3da01b24f341580743489d38`.
- Fresh passing verifier commit/tree:
  `5178a63eeb56abc623d4bc10a0a5ae68eb868299` /
  `3105c6cf683b3ba6ffb4f5198bcaeffba85d9608`.
- Accumulated-validation source state commit/tree:
  `45da453dcc006179401ea85f3f7d3425e5074df4` /
  `6d9119969ca433e3a43957389dc91ec72a198c25`.
- Completed: `2026-08-31T14:16:01Z`.
- Verdict: **pass**. No applicable mandatory gate failed or remained skipped.

This record authorizes only fresh independent C3-B2 acceptance. It creates no
manifest, checkpoint, public API or CLI authority, B3 authority, non-macOS
claim, distribution authority, or Cycle 4 authority.

## Candidate and independent verification

The only changes after candidate `d8e14bb` and before this gate were the fresh
round-3 verifier test/review and orchestration progress. Candidate-owned host
and implementation bytes remained unchanged. Their SHA-256 values are:

| Artifact | SHA-256 |
| --- | --- |
| `_decode/host.py` | `b913febe115299aa761e913e9f953c9acfdcda6f076fdfaffa29e2a4ca9e3e71` |
| `_decode/ipc.py` | `f3502eba02c66c957c6fc12a9d6c7e181d8c5e0c8e75ea75cb59c8027c460114` |
| `_decode/worker.py` | `9a01a2c03ecb255fb3dddc43036a8d4ba3b7b62923e4a687748a1db70ffdb160` |
| implementation test | `e3da648cb4dccbf97023a886a43a616c7249ccb614fc692cadde79e7508323c4` |
| round-3 implementation review | `12105221def9e51705577e032882bc8cb47df9916e603a2b79b552829964bf27` |
| round-3 verifier test | `0fa95ab5e4e849c7f63c34e4badab2a32321dc39897ccf838e40e1dc8c1fa432` |
| round-3 verifier review | `0c78a9e8d2143e8b488f8780083a19227c166de0221fd7b90dae0385851769d2` |

Fresh verifier `c3-b2-private-host-verifier-replacement-3` passed the exact
candidate with no finding. Its 32 new hostile rows and the complete focused
set produced 304 passes: 229 current implementation rows, eight immutable
round-1 verifier rows, 35 immutable round-2 verifier rows, and 32 round-3
verifier rows. Separate live-success and forced-kill cleanup observations
passed the unchanged exact-candidate regression ceilings.

The focused and accumulated evidence covers the closed API-v3 subset, typed
request/result and declaration graph, request/result identity binding,
versioned streaming IPC, all 18 hard product limits, all 11 private macOS
regression observations, cancellation races, deadline terminate/kill/close/
reap behavior, hostile frames and processes, resource readback, bounded output
and diagnostics, no retained partial result, failure-then-success recovery,
and inert host-ID-only code selection. The 11 regression values remain
validation gates and were not converted into real-time product errors.

## Complete Python 3.12 accumulated gate

The reused ignored repository-local environment was CPython 3.12.13 on macOS
15.7.9 build 24G830, x86_64. This is permitted for B2; its exact lock and
project identities remained:

- `requirements-dev.lock`:
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
- `pyproject.toml`:
  `56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

The applicable nonhardware inventory used the accepted B1 include-only
partition extended by all B2 implementation and verifier evidence. It ran
`pytest -m 'not hardware'` with the frozen fixture-surface historical node
deselected and these 15 superseded B1 verifier modules ignored:

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

The command collected 934 tests and completed with **929 passed, four skipped,
one deselected, and 149 warnings** in 159.16 seconds. The four skips are the
inherited optional C2-B3 machine-local physical-artifact reruns. Both formerly
sandbox-only loopback checks passed in this run. No Cycle 3 mandatory row was
skipped.

| Command class | Result |
| --- | --- |
| repository-local `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| mypy over product `src` | exit 0; 30 source files |
| strict mypy over characterization | exit 0; seven files |
| fixture generator `--check` | exit 0; no drift |
| characterization binding `--check` | exit 0; no drift |
| installed CLI help | exit 0 |
| Cycle-2 evidence `c2-b1.json` through `c2-b6.json` | six exit-0 validations |
| corrected Cycle-3 B1 manifest | schema validation exit 0 |
| applicable nonhardware pytest | 929 passed; four classified skips; one deselected |

## Locked frontend, browser, and performance regressions

The accepted frontend commands used ignored repository-local Node v22.14.0
with npm 10.9.2. `web/package-lock.json` and
`web/production-assets.json` remained respectively:

- `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
- `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

ESLint and TypeScript passed. Vitest passed three files and five tests. Vite
built 29 modules, and the governed production-asset checker found no drift.
The isolated browser gate passed its one-test maximum-width suite and its
three-test live/shell suite.

The frozen B6 production benchmark passed 1/1, and the unchanged approved
threshold checker accepted report SHA-256
`fe646a5906bdb4c24162bb788c4213dd2d7806ed53b51de0e054ea57eabefaee`.
The report records Chromium 133.0.6943.16, Playwright 1.50.1, exact Node
v22.14.0, the approved method and fixture/product identities, and these p95
observations:

| Measurement | Observed p95 ms | Approved ceiling ms |
| --- | ---: | ---: |
| load | 420.40000000596046 | 1000 |
| interaction | 331.40000000596046 | 750 |
| representative bus transition | 158.5 | 500 |
| representative bus distinct-strobe | 66.40000000596046 | 300 |
| worst bus transition | 400.80000001192093 | 900 |
| worst bus distinct-strobe | 151.59999999403954 | 500 |

The checker also accepted the frozen raw-sample/statistical derivation,
viewport, bounds, Canvas/DOM limits, nondisclosure fields, and unreliable-heap
classification. Generated browser results were preserved outside the worktree
at `/private/tmp/c3-b2-web-20260831T1416` after hashing.

### Discarded environment attempts

Initial browser and benchmark launches inside the restricted sandbox could not
bind their loopback web server and supply no evidence. Root reran each through
one exact, reusable command-class approval. These pinned-Node command classes
are now saved, preventing child-by-child or rerun-by-rerun prompts.

Before selecting the pinned runtime, one browser run passed under system Node
v26.7.0 and one benchmark measured successfully but was rejected by the
unchanged checker with `frozen benchmark method metadata changed`. Those runs
are invalid environment diagnostics, not accepted evidence. Root did not alter
the report, checker, method, or thresholds; every accepted frontend, browser,
and performance result above was rerun from the start under exact Node
v22.14.0.

## Prohibited-runtime, cleanup, and scope audit

An active-source, tooling, script, project, lock, and frontend dependency scan
found no `pythonnet`, `libsigrokdecode`, `sigrok-cli`, `dotnet`, or
`clr.AddReference` use. Installed-environment discovery returned no
`pythonnet`, `clr`, `sigrokdecode`, or `libsigrokdecode` module. A final process
inventory found no decoder host, characterization runner, pytest, Vite,
Playwright, or prohibited external/reference runtime. The exact candidate
descendant passed `git diff --check`; generated browser residue was moved out
of the worktree, leaving it clean before this record.

No C#/.NET/reference decoder executed. No USB/serial hardware was accessed, no
firmware or live capture ran, no dependency or workflow changed, no public
decode API/CLI was exposed, no package was built or published, and no B3, B4,
B5, Cycle 4, non-macOS, or broad-decoder work occurred. Findings: none. Next
authority is fresh independent C3-B2 acceptance of this exact candidate and
complete accumulated record.

`pass`
