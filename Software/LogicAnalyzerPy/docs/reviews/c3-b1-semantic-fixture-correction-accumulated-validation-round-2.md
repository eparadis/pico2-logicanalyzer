# C3-B1 semantic-fixture correction accumulated validation — round 2

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact fixture candidate/tree:
  `3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
  `14c010153ea5542617e601e4126047c561a48483`.
- Independent verifier/verdict:
  `c3-b1-semantic-fixture-correction-verifier-2` / `pass`; evidence descendant
  commit `3a29e4684af6a4c8e53aa4f83f9692ddebab5670`; verifier-test SHA-256
  `9f750b51294b2078e82373adbbdd81ac287de669603f82bf59e65cc8e001a10a`;
  review SHA-256
  `e3402ea64e9dde2417c0aefbfd257e6a44db13947dae774ed33bcb6866645f23`.
- Completed: `2026-08-28T14:31:47Z`.
- Result: **pass for the reopened semantic-fixture gate**. `C3B2-IF002` is
  closed for this exact candidate. Runner binding, raw observations,
  thresholds/operator approval, final B1, manifest, checkpoint, and B2 remain
  invalidated or incomplete; no earlier verdict or authority transfers.

Validation ran from clean local clone `/private/tmp/c3-fixture-if002` at the
exact verification descendant. `PYTHONPATH` pinned product imports to that
clone while the repository-local managed CPython 3.12.13 and exact Node
22.14.0 environments supplied tools. The candidate's tracked bytes remained
unchanged. Validation-only `.venv` and `node_modules` links and ignored browser
results were the only clone-local additions.

## Fixture and static closure

- Generator `--check` passed deterministically. All manifest artifact digests
  and the generator self-digest recomputed. The corrected semantic corpus is
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`;
  fixture manifest is
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`.
- Independent comparison of all 63 timelines proved the sole semantic delta:
  `i2c-unshifted-repeated-start.expected_records[4].value.data_base64` changes
  from `UA==` to `oA==`. Frozen I2C source shifts only the `shifted` option,
  so unshifted Python, binary, and annotation output consistently represent
  `0xA0`; shifted output remains `0x50`.
- Python dependency check passed. Whole-project Ruff passed. Strict mypy over
  all 21 product source files passed. Installed CLI help passed. Six accepted
  Cycle 2 evidence manifests independently passed their frozen validator.
- Focused implementation fixture suite passed 12 tests. The fresh independent
  correction verifier passed 6 tests. No decoder, B2 host, characterization
  runner, raw observation, prohibited runtime, hardware, or external oracle
  supplied expected output.

## Full-suite invalidation audit

The unfiltered clean command `pytest -m 'not hardware' -q` was run first and
was not represented as green: **623 passed, 124 failed, and 6 skipped**. All
124 failures are expected fail-closed reactions in invalidated runner binding,
raw, threshold, prior exact-candidate correction verifier, final-binder, and
manifest-dependent tests. Their first failures identify the superseded fixture
or source digest. No unrelated Cycle 1/2 or current fixture regression was
hidden.

The candidate-applicable command then ignored only these wholly invalidated
modules:

- `tests/implementation/test_cycle3_preexecution_runner.py`;
- prior runner candidate and runner-rebinding verifier modules;
- raw-baseline verifier;
- all three threshold-proposal verifier modules;
- both superseded final-candidate verifier modules; and
- the prior exact-candidate semantic-correction verifier.

It passed **404 tests with 6 classified skips and 106 inherited warnings**.
Two skips are sandbox-only loopback tests covered by the explicit browser gate;
four are the documented optional C2-B3 machine-local physical-artifact branch,
whose checked-in sanitized evidence remains mandatory and passed. These
exclusions are ordered invalidations, not waivers: every downstream module must
be rebound and rerun before a replacement B1 checkpoint.

## Frozen web regression

Exact Node 22.14.0 checks passed: ESLint; TypeScript; three Vitest files and
five tests; Vite build of 29 modules; and the frozen asset checker. Contract-
defined isolated Playwright invocations then passed one maximum-width test and
three live/shell tests. The B6 performance test passed in 24.1 seconds and the
frozen threshold checker accepted report SHA-256
`7585e4253866cd89f440b956305fb0420c58cf5aa345504af13dc3335a510f6e`.

Two earlier browser attempts supplied no pass evidence. The first could not
start because the clean clone lacked its validation-only `.venv` link. The
second combined test files that the frozen npm command deliberately runs in
two separate invocations; concurrent shared-server activity made the
maximum-width import report `error` while the other three tests passed. After
restoring the exact two-invocation contract shape, all four passed. No product,
test, fixture, threshold, or configuration byte was changed to obtain the
passing result.

## Scope, process, and ordering closure

- Candidate scope remains the exact five committed fixture-owned paths.
  Verification adds only its two immutable evidence paths. The preserved
  untracked B2 implementation, test, and review paths were excluded from the
  clean clone and from all evidence.
- Process inspection after browser/performance completion found no surviving
  clone server, Playwright/Chromium process, characterization runner, decoder
  worker, C#/.NET, or sigrok process.
- No network dependency operation, hardware, serial, firmware, publication,
  distribution, non-macOS claim, B3+, or Cycle 4 action occurred.
- Fresh fixture acceptance is the next gate. A pass may authorize only runner
  rebinding and the remaining replacement-B1 sequence; it cannot resume B2.

Open fixture-candidate findings: none.

`pass`
