# C3-B2 C3B2-A002 replacement accumulated validation — round 3

## Subject and verdict

- Owner: primary Cycle 3 orchestrator (`/root`).
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
- Predeclared plan/results descendant commit/tree:
  `41cccdfce71482418ac01f14d6b7669e073b626b` /
  `0590d1972b2abd94ac41f6e245ea2d28e04cb34d`.
- Completed: `2026-08-31T15:22:20Z`.
- Verdict: **pass**. Every newly predeclared performance invocation and every
  from-scratch replacement accumulated command passed.

This record does not itself close acceptance finding `C3B2-A002`. Only a new
independent acceptance identity may decide whether the complete immutable
history and replacement proof are sufficient. No manifest, checkpoint, B3,
public decoder API/CLI, distribution, non-macOS, or Cycle 4 authority follows.

## Candidate and immutable finding order

Candidate `959edf7` remains byte-identical. Host, implementation test, round-4
implementation review, round-4 verifier test, and round-4 verifier review
SHA-256 values remain respectively:

- `8a555fb08a88badf59bdabe2f558bcd9f7918ccebd52d3c2539013bff733c990`;
- `77116dab6279a2e6bb579f14d72a2be59a02725cba2ef1f888b69492ae6954b5`;
- `c0d5b2573a21c80a9d8e89c5c81e22412642ecd42eda7acf0d7a0fa459d88dbf`;
- `a77b4e6081da5dead4e4f9d3e7b3761a28efa765c24fd9a1c88016b114408607`;
- `4813ccafec2c66d324e1427646cff34ebaa113d0346dc2019c917167c6a724`.

`C3B2-A001` is closed by nonblocking request delivery under the unified
response/stdout/stderr/deadline/cancellation lifecycle and fresh independent
verification. All 313 focused B2 rows remain passing and cover complete
R6-R12/R22 scope, 18 hard product limits, 11 distinct evidence-only regression
gates, request/result and graph validation, closed code selection, hostile
IPC/process/resource behavior, deterministic cleanup, atomic failure, and real
recovery.

The original exact benchmark failure and ad hoc later pass remain immutable:

- failed report `e2602ab8c3dd02e56b1a8492bd85e12f5d6215e8254e2f9462ae5aed32ebd131`,
  representative distinct-strobe p95 140.5 ms versus 116.7250000052154 ms;
- later pass `460b28250af8d8d5fa899dd426c1bf6b61b1791444215cbc2c87a471d940f7b0`.

Failed acceptance at `d5d77a8` correctly opened `C3B2-A002`; neither report nor
any earlier candidate/verifier/accumulated/acceptance verdict is invalidated or
transferred.

## Predeclared no-retry performance proof

Before any new performance execution, root committed the exact five-run rule
at `de470abdab63ebdf7014747b4a4e1fc2fb694a75`. Plan SHA-256 is
`c35079e6b2ba7bcf04c700b18e53d8f948387a56e2a13eff2084d879c331c1f6`.
It required all five unchanged invocations to pass independently and prohibited
retry, replacement, sixth-run selection, averaging, and outlier removal. Any
single failure would have stopped the gate.

The series passed exactly 5/5. Result record
`docs/reviews/c3-b2-performance-reproducibility-results-round-1.md` has
SHA-256 `66442c98fff290626242146a315be1b24fc681bcd4ed93928255760383526369`.
Every complete report was hashed and preserved before the next run:

| Run | Report SHA-256 | Load | Interaction | Rep. transition | Rep. distinct | Worst transition | Worst distinct |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `a02de4b65aa137840617b4948f7d1280984a666a2a1b88a895cccf55db8ef0c6` | 461.7000000178814 | 380.5 | 155.40000000596046 | 62.80000001192093 | 405.30000001192093 | 147.5 |
| 2 | `508d1ad1f22e129c1c8c60a4868b059607c2efab5c2c80d4c88327a054f70ca5` | 423 | 348.09999999403954 | 138.90000000596046 | 60.69999998807907 | 402 | 147.2000000178814 |
| 3 | `175008c92ab39f40d913d9bf1b72964588d826a4433f1632e421b2c02deb51c7` | 518.7000000178814 | 343.2000000178814 | 137.69999998807907 | 66.60000002384186 | 406.19999998807907 | 155 |
| 4 | `a2f85b22f578cec4a5ca9074bcf986ef42f59b57ce8f8521c6e3779e5eaff1e1` | 524.3999999761581 | 352.09999999403954 | 150.59999999403954 | 73.5 | 401.19999998807907 | 150.40000000596046 |
| 5 | `80fb201f846849ab208fed5fc7da2f179bd78f07d42a30b59f4a961a09193f45` | 451 | 346.90000000596046 | 151.40000000596046 | 64.2999999821186 | 400.19999998807907 | 148.5 |

Columns are p95 milliseconds. Every report independently passed the unchanged
checker and both its absolute and stricter regression ceilings. Separate
post-series checker calls accepted all five intact reports. Exact Node
v22.14.0, Chromium 133.0.6943.16, Playwright 1.50.1, fixtures, product assets,
viewport, warm-ups, iterations, statistics, method, bounds, nondisclosure,
checker, and ceilings remained unchanged. The full report directories remain
preserved at `/private/tmp/c3-b2-a002-series-1` through `-5`.

This is additional validation evidence, not a new benchmark method or a rule
that erases the earlier failure. Fresh acceptance owns the disposition.

## From-scratch Python 3.12 accumulated rerun

After sealing the five raw reports, root reran the rest of the complete gate
from the beginning against the unchanged candidate and verifier descendant.
The repository-local environment was CPython 3.12.13 on macOS 15.7.9 build
24G830, x86_64. Matching lock/project SHA-256 values are
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
and `56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

The accepted B1 include-only partition plus all B2 modules used the exact same
15 superseded-B1 ignores and one frozen historical fixture-surface deselection
listed in round-2 accumulation. It collected 943 tests and completed with
**938 passed, four skipped, one deselected, and 149 warnings** in 164.97
seconds. The four skips are only inherited optional C2-B3 machine-local
physical-artifact reruns; no Cycle 3 mandatory test was skipped.

| Command class | Fresh result |
| --- | --- |
| `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| mypy over product `src` | exit 0; 30 source files |
| strict characterization mypy | exit 0; seven files |
| fixture generator and runner binding checks | both exit 0; no drift |
| installed CLI help | exit 0 |
| Cycle-2 manifests `c2-b1` through `c2-b6` | six exit-0 validations |
| corrected C3-B1 manifest | schema validation exit 0 |
| applicable nonhardware pytest | 938 passed; four classified skips; one deselected |

## Frontend, inherited, prohibited, cleanup, and scope rerun

Repository-local Node v22.14.0 reran ESLint and TypeScript successfully;
Vitest passed three files/five tests; Vite built 29 modules; and the governed
asset checker passed. Lock and asset SHA-256 values remain
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
and `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
The unchanged browser regression passed one maximum-width test and three
live/shell tests. Its generated results were preserved at
`/private/tmp/c3-b2-r3-browser`.

Static active-path scanning found no `pythonnet`, `libsigrokdecode`,
`sigrok-cli`, `dotnet`, or `clr.AddReference` use. Installed discovery found no
`pythonnet`, `clr`, `sigrokdecode`, or `libsigrokdecode` module. Final process
inventory found no private worker, pytest, Vite, Playwright, characterization,
or prohibited runtime. The worktree was clean and `git diff --check` passed.

No external/reference decoder or C#/.NET executed. No hardware, USB/serial,
firmware, live capture, package build/publication, dependency/lock/workflow,
public decoder API/CLI, browser decoder, B3+, Cycle 4, or unsupported-platform
action occurred. Findings introduced by this run: none. The only next authority
is fresh independent replacement acceptance over the complete ordered record.

`pass`
