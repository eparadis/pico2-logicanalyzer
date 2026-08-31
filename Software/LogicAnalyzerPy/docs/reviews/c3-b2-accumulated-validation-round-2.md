# C3-B2 streamed-request accumulated validation — round 2

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Corrected C3-B1 checkpoint: `d4f984d`.
- Exact immutable B2 candidate/tree:
  `959edf77945176b26c7cec86bcdd806d7e5769ea` /
  `bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.
- Fresh verifier evidence commit/tree:
  `ed39a653612b5e879aa08391fcb264f43f09a956` /
  `dc94ec3af39363f6b6c9a41ce5f9a11b04bfe65e`.
- Validation source state commit/tree:
  `a6ea7dd625a5b661e8dfff5b8efbfba1a18cea56` /
  `abaa82f77cffea3296fc90d8ee1742d3520ebaf5`.
- Completed: `2026-08-31T14:57:58Z`.
- Verdict: **pass**. The final accepted execution of every applicable gate
  passed; the earlier failed performance observation is preserved below.

This record authorizes only fresh independent replacement C3-B2 acceptance.
It creates no manifest, checkpoint, public decoder API or CLI, B3 authority,
distribution authority, non-macOS claim, or Cycle 4 authority.

## Candidate, finding history, and verification

Predecessor candidate `d8e14bb`, verifier `5178a63`, accumulated record
`bba6662`, and failed acceptance at `6825e88` remain immutable history and
transfer no result. Acceptance finding `C3B2-A001` established that the former
blocking request write occurred before deadline/cancellation handling.

Candidate `959edf7` closes that implementation defect by making request
delivery a nonblocking selector participant beside response, stdout, and
stderr reads under one parent deadline/cancellation lifecycle. Partial writes,
never-reading workers, early close/exit/signal, cancellation during delivery,
simultaneous hostile output, readiness anomalies, stable typed failure,
terminate/kill/close/reap, atomic discard, and real subsequent recovery have
direct evidence. Candidate artifact SHA-256 values are:

| Artifact | SHA-256 |
| --- | --- |
| `_decode/host.py` | `8a555fb08a88badf59bdabe2f558bcd9f7918ccebd52d3c2539013bff733c990` |
| implementation test | `77116dab6279a2e6bb579f14d72a2be59a02725cba2ef1f888b69492ae6954b5` |
| round-4 implementation review | `c0d5b2573a21c80a9d8e89c5c81e22412642ecd42eda7acf0d7a0fa459d88dbf` |
| round-4 verifier test | `a77b4e6081da5dead4e4f9d3e7b3761a28efa765c24fd9a1c88016b114408607` |
| round-4 verifier review | `4813ccafec2c66d324e1427646cff34ebaa113d0346dc2019c91716767c6a724` |

Fresh verifier `c3-b2-private-host-verifier-replacement-4` returned `pass`
with no finding. Root reproduced all 313 current B2 rows: 232 implementation,
eight round-1 verifier, 35 round-2 verifier, 32 round-3 verifier, and six new
round-4 verifier rows. Ruff, strict mypy over nine private source files,
diff-check, and final exact-child process cleanup passed.

The combined evidence retains complete R6-R12/R22 coverage: closed host-ID,
digest, import, environment, and inert-data code selection; pre-spawn request
validation; frozen API-v3 primitives; request/result identity and complete
declaration/record graph validation; versioned framed IPC; all 18 hard product
limits; the separate 11 evidence-only macOS regression gates; hostile
process/frame/output/resource behavior; cancellation/deadline cleanup; no
partial retained result or poisoned state; and success after every failure.
No private regression observation became a product real-time failure.

## Complete Python 3.12 accumulated gate

The ignored repository-local environment was CPython 3.12.13 on macOS 15.7.9
build 24G830, x86_64. B2 permits reuse because the OS/Python and lock identities
match. `requirements-dev.lock` and `pyproject.toml` SHA-256 values are:

- `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
- `56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

The accepted B1 include-only partition was extended by every B2
implementation and verifier module. The exact command ran
`pytest -m 'not hardware'`, deselected only the frozen historical fixture-
surface node, and ignored these 15 superseded B1 verifier modules:

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

It collected 943 tests, selected 942, and completed
with **938 passed, four skipped, one deselected, and 149 warnings** in 193.99
seconds. The four skips are only the inherited optional C2-B3 machine-local
physical-artifact reruns; their checked-in sanitized evidence passed. No Cycle
3 mandatory test was skipped.

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
| applicable nonhardware pytest | 938 passed; four classified skips; one deselected |

## Locked frontend, browser, and performance regressions

Every accepted frontend command used repository-local Node v22.14.0 and npm
10.9.2. The unchanged package lock and production-asset manifest SHA-256 values
are `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
and `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
ESLint and TypeScript passed; Vitest passed three files/five tests; Vite built
29 modules; and the governed production-asset comparison passed. The saved
exact pinned-Node browser command passed one maximum-width test and three
live/shell tests without a new approval request.

The final frozen B6 benchmark invocation passed 1/1 and its unchanged checker
accepted report SHA-256
`460b28250af8d8d5fa899dd426c1bf6b61b1791444215cbc2c87a471d940f7b0`.
It records exact Node v22.14.0, Chromium 133.0.6943.16, Playwright 1.50.1,
approved method/fixture/product identities, raw iterations/statistics,
viewport, Canvas/DOM bounds, nondisclosure, and unreliable-heap treatment.
The checker requires each result to satisfy both its absolute ceiling and the
more restrictive regression ceiling:

| Measurement | Accepted p95 ms | Regression ceiling ms | Absolute ceiling ms |
| --- | ---: | ---: | ---: |
| load | 426.7999999821186 | 772.0999999986961 | 1000 |
| interaction | 431.30000001192093 | 580.3000000026077 | 750 |
| representative bus transition | 150.59999999403954 | 261.4499999973923 | 500 |
| representative bus distinct-strobe | 73 | 116.7250000052154 | 300 |
| worst bus transition | 406.7999999821186 | 710.1499999947846 | 900 |
| worst bus distinct-strobe | 154 | 263.1999999973923 | 500 |

### Preserved failed performance observation

The first exact-Node benchmark invocation completed its Playwright test but the
unchanged checker rejected representative distinct-strobe p95 140.5 ms against
the 116.7250000052154-ms regression ceiling. Its report SHA-256 was
`e2602ab8c3dd02e56b1a8492bd85e12f5d6215e8254e2f9462ae5aed32ebd131`;
the two raw observations were 59.20000001788139 and 140.5 ms. This invocation
is a failed observation and supplies no pass. It is not hidden, averaged,
deleted from history, or used to change product, method, iterations, checker,
or either threshold.

Root confirmed no surviving Playwright, Vite, pytest, or private worker process
and reran the exact unchanged command once on the quiescent host. That complete
invocation produced the accepted report and exit-0 checker result above. No
root cause beyond transient host scheduling is asserted. Fresh acceptance must
audit both observations and decide readiness; this accumulated record does not
waive or rebase the failed measurement.

Generated accepted browser results were preserved intact outside the worktree
at `/private/tmp/c3-b2-r2-web-20260831T1455` after hashing. The exact reusable
pinned-Node browser and benchmark approval classes were reused without any new
authorization request.

## Prohibited-runtime, cleanup, and scope audit

Active source, tooling, scripts, project metadata, locks, and frontend
dependencies contain no `pythonnet`, `libsigrokdecode`, `sigrok-cli`, `dotnet`,
or `clr.AddReference` use. Installed-environment discovery returned no
`pythonnet`, `clr`, `sigrokdecode`, or `libsigrokdecode` module. Final process
inventory found no private worker, characterization runner, pytest, Vite,
Playwright, or prohibited external/reference runtime. Candidate product and
implementation bytes remained identical from `959edf7`; only progress and the
round-4 verifier evidence were added. `git diff --check` passed and the
worktree was clean before this record.

No C#/.NET/reference decoder executed; no USB/serial hardware, firmware, live
capture, package build/publication, dependency/lock/workflow, public decoder
API/CLI, browser decoder, B3+, Cycle 4, or unsupported-platform action occurred.
Findings introduced here: none. Next authority is fresh independent acceptance
of the exact candidate, verifier, this complete accumulated record, and the
preserved performance history.

`pass`
