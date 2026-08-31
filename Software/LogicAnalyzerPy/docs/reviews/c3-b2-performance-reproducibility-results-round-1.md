# C3-B2 C3B2-A002 performance reproducibility results — round 1

## Binding and verdict

- Owner: primary Cycle 3 orchestrator (`/root`).
- Exact candidate/tree:
  `959edf77945176b26c7cec86bcdd806d7e5769ea` /
  `bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`.
- Fresh verifier pass: `ed39a653612b5e879aa08391fcb264f43f09a956`.
- Predeclared plan commit:
  `de470abdab63ebdf7014747b4a4e1fc2fb694a75`.
- Plan SHA-256:
  `c35079e6b2ba7bcf04c700b18e53d8f948387a56e2a13eff2084d879c331c1f6`.
- Completed: `2026-08-31T15:15:35Z`.
- Verdict: **pass** — exactly five of five required invocations passed; no
  failure, interruption, retry, replacement, sixth run, aggregation, or
  outlier selection occurred.

The earlier valid failed report `e2602ab8...` and later ad hoc passing report
`460b2825...` remain preserved conflicting history. This series neither
invalidates nor selects between them. It supplies new bounded evidence under a
rule committed before execution.

## Immutable preflight

Before run 1, the worktree was clean; repository-local Node was exactly
v22.14.0; no pytest, Vite, Playwright, or private decoder worker process was
present; and these frozen identities matched:

| Artifact | SHA-256 |
| --- | --- |
| `web/package-lock.json` | `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9` |
| `web/production-assets.json` | `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9` |
| `web/tests/b6-performance.spec.ts` | `34242c14be1d796c8f3db97be31b3296ee642a530a2b88f9cb6994b8232d536a` |
| `tools/check_b5_thresholds.py` | `9e087ca8dcc9a232d5859326066c77aa6debebc41a68edf2681c19285d7bdfe9` |

Every run used the same already-approved pinned-Node command. Each Playwright
test passed 1/1 and its chained unchanged checker exited 0 before the report
was hashed and moved intact. After run 5, a separate checker invocation over
each preserved report also exited 0, and final process inspection found no
surviving repository test/server/worker process.

## Complete five-run result

Columns are p95 milliseconds in frozen checker order: load, interaction,
representative transition, representative distinct-strobe, worst transition,
and worst distinct-strobe.

| Run | Report SHA-256 | Six p95 values (ms) | Preserved location |
| ---: | --- | --- | --- |
| 1 | `a02de4b65aa137840617b4948f7d1280984a666a2a1b88a895cccf55db8ef0c6` | `461.7000000178814, 380.5, 155.40000000596046, 62.80000001192093, 405.30000001192093, 147.5` | `/private/tmp/c3-b2-a002-series-1` |
| 2 | `508d1ad1f22e129c1c8c60a4868b059607c2efab5c2c80d4c88327a054f70ca5` | `423, 348.09999999403954, 138.90000000596046, 60.69999998807907, 402, 147.2000000178814` | `/private/tmp/c3-b2-a002-series-2` |
| 3 | `175008c92ab39f40d913d9bf1b72964588d826a4433f1632e421b2c02deb51c7` | `518.7000000178814, 343.2000000178814, 137.69999998807907, 66.60000002384186, 406.19999998807907, 155` | `/private/tmp/c3-b2-a002-series-3` |
| 4 | `a2f85b22f578cec4a5ca9074bcf986ef42f59b57ce8f8521c6e3779e5eaff1e1` | `524.3999999761581, 352.09999999403954, 150.59999999403954, 73.5, 401.19999998807907, 150.40000000596046` | `/private/tmp/c3-b2-a002-series-4` |
| 5 | `80fb201f846849ab208fed5fc7da2f179bd78f07d42a30b59f4a961a09193f45` | `451, 346.90000000596046, 151.40000000596046, 64.2999999821186, 400.19999998807907, 148.5` | `/private/tmp/c3-b2-a002-series-5` |

Every value independently satisfies both its unchanged absolute ceiling and
its stricter regression ceiling. No product, browser, fixture, environment
path, dependency, method, warm-up, iteration, statistic, checker, or threshold
byte changed during the series.

## Scope and next gate

This pass is only the predeclared performance component of a new complete
accumulated gate. It does not itself close `C3B2-A002`, waive the original
failure, create manifest/checkpoint authority, or permit B3. Root must now
repeat every other accumulated command against the unchanged exact candidate,
commit the resulting complete record, and obtain a new independent acceptance
verdict that audits all historical and new evidence.

`pass`
