# C3-B1 semantic-fixture accumulated validation — round 1

## Subject and result

- Root validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact tested fixture candidate/tree:
  `c1420ad9b4309fc7417acbc228085b68237c24d0` /
  `26ef344bfb76bec4a8e68be06a411b4d27d20de1`.
- Required independent verification: round-8 `pass`, committed at `fa85b83`;
  record SHA-256
  `9e1ad275730f30ff1ccbaf3c8e0a59e06c98463d332f249e46b4242be2d18bd5`.
- Validation descendant before this record:
  `d5f1c6946a79541fbd811bd16526a0cdf4b2583a` / tree
  `490bba96ab5df8038b58bc0cd18fae3f8f85ff38`. Candidate-path quiet diff
  was empty and the worktree was clean before this record was created.
- Validation completed: `2026-08-27T02:14:58Z`.
- Result: **pass**. No mandatory check remains failed or skipped.

This is accumulated validation of the static semantic-fixture and finite-cap
specification. It makes no executable cap-enforcement, decoder-runtime,
characterization, threshold, operator-approval, publication, or hosted-CI
claim.

## Clean Python 3.12 gate

Environment: macOS 15.7.7 build 24G720, x86_64; managed CPython 3.12.13;
stable clean environment `/private/tmp/cycle3-clean-python`; pip 25.0.1.
`requirements-dev.lock` SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command | Exact result |
| --- | --- |
| managed `python3.12 -m venv --clear /private/tmp/cycle3-clean-python` | exit 0; Python 3.12.13 |
| clean Python `-m pip install --require-hashes -r requirements-dev.lock` | exit 0; every artifact hash-locked |
| clean Python `-m pip install --no-build-isolation --no-deps -e .` | exit 0; `pico-logic-analyzer==0.1.0` |
| clean Python `-m pip check` | exit 0; no broken requirements |
| clean Python `-m ruff check .` | exit 0; all checks passed |
| clean Python `-m mypy src` | exit 0; no issues in 21 source files |
| clean Python `-m pytest -m "not hardware"` | exit 0; 401 passed, two sandbox-only loopback skips, 106 warnings |
| root-brokered clean Python `-m pytest -q tests/implementation/test_web_api.py tests/verification/test_c2_b1_foundation_blackbox.py` | exit 0; 8 passed, including both skipped loopback cases |
| clean Python `-m pico_logic_analyzer --help` | exit 0; installed module help rendered |

The second pytest command reran both complete affected files with loopback
authority. Six tests had already passed in the full run and the two skipped
tests then passed, so all 403 collected non-hardware tests have passing proof;
no mandatory skip is accepted. Existing aiohttp key/deprecation warnings and
the deliberate duplicate-ZIP warning are inherited, non-failing regression
warnings and do not weaken a gate.

The editable distribution file list contains only the `pico-la` entry point,
editable package pointer, and distribution metadata. It exposes no checked-in
decoder snapshot. Existing package metadata remains MIT; the separate GPL
snapshot placement/notices review is still explicitly pending and was neither
simulated nor bypassed by installation.

## Fixture, source, and evidence gates

| Check | Exact result |
| --- | --- |
| clean Python `scripts/generate_cycle3_fixtures.py`, then `--check` | exit 0; byte-identical rebuild |
| clean Python focused implementation plus immutable verifier tests | exit 0; 18 passed |
| nine-file SHA-256 plus static AST import-closure evaluator | exit 0; 9 digests and 14 import statements exactly match provenance |
| installed-distribution and `find_spec` prohibited dependency/import audit | exit 0; no pythonnet, CLR, libsigrokdecode, sigrok package/CLI, or importable `sigrokdecode` |
| scoped source/lock/test/script/tool/workflow prohibited-name scan | exit 0; zero matches |
| root-brokered active-process inspection | exit 0; zero prohibited-runtime, decoder-runner, or characterization-process matches |
| accepted Cycle 1 draft-2020-12 schema-subset evaluator | exit 0; all five manifests schema-valid |
| accepted Cycle 2 validator against `c2-b1.json` through `c2-b6.json` | six exit-0 results |

Accepted Cycle 1 manifest identities remain exactly:

| Manifest | SHA-256 |
| --- | --- |
| `c1-b1.json` | `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc` |
| `c1-b2.json` | `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af` |
| `c1-b3.json` | `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598` |
| `c1-b4.json` | `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead` |
| `c1-b5.json` | `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d` |

The Cycle 1 and Cycle 2 manifests are byte-unchanged from accepted checkpoint
`7fe1f5c`. The Cycle 3 fixture manifest and cap SHA-256 values are respectively
`6a5b26f73ff3ae5e4ec64962acc43d08d52dbf8b7ab2e574b976ceab5d8f9a43`
and `fc5f3b0de17ae9f74b363ee5d4847ea2f9a88b9e0918cba8e848305ebbda05a1`.

## Inherited optional-web and performance regression

The accepted official Node 22.14.0 archive SHA-256 remains
`6698587713ab565a94a360e091df9f6d91c8fadda6d00f0cf6526e9b40bed250`.
`web/package-lock.json` remains
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`web/production-assets.json` remains
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

| Command class | Exact result |
| --- | --- |
| exact Node 22 npm `ci --no-audit --no-fund` | exit 0; 215 locked packages |
| exact Node 22 ESLint and TypeScript | both exit 0 |
| exact Node 22 Vitest | exit 0; 3 files, 5 tests |
| exact Node 22 Vite production build plus `scripts/check_web_assets.py` | exit 0; 29 modules; no asset drift |
| exact Node 22 Playwright accepted browser regressions | exit 0; 1 plus 3 tests passed |
| exact Node 22 B6 offline performance spec | exit 0; 1 test passed |
| clean Python approved-threshold checker over generated performance report | exit 0 |

The temporary performance report SHA-256 is
`d72ec3ba02764c751ee729fa1e4ce09a6a71a579b7615e4f21dfbaa33f843e28`.
It records Node v22.14.0, Playwright 1.50.1, Chromium 133.0.6943.16, macOS
24.6.0 x64, and passed the unchanged Cycle 2 threshold checker. Generated
browser results were moved outside the repository; all Playwright/Vite/test
servers were reaped. These commands are unchanged regression only and create
no Cycle 3 browser-decoder authority.

## Scope, state, and disposition

- Candidate fixture, generator, implementation-test, and immutable-verifier
  paths are byte-identical to candidate `c1420ad`; descendant changes before
  this record are review/progress evidence only.
- `git diff --check` passed; deterministic frontend and fixture rebuilds left
  no tracked or untracked repository change.
- No decoder, compatibility host, helper runtime, C#, .NET, pythonnet,
  libsigrokdecode, `sigrok-cli`, or external/reference decoder runtime was
  imported or executed. No hardware, USB/serial device, live capture,
  firmware, native port procedure, publication, unsupported-platform claim,
  or Cycle 4 work occurred.
- Hardware/native-port regression is preserved through accepted immutable
  Cycle 1/2 evidence and was not rerun because Cycle 3 prohibits physical
  access. Hosted exact-candidate CI is mandatory only at C3-B4 and C3-B5, not
  this internal B1 fixture gate.
- Project/legal snapshot placement remains an ordered later B1 input. The
  current inventory accurately records notices and makes no legal conclusion.
- Executable experiment-cap enforcement belongs only to the later distinct
  pre-execution-runner candidate and is neither present nor claimed here.
- Findings: none.
- Approval needed: none. Dependency installation, loopback/browser execution,
  and process visibility used consolidated root-brokered command classes.

pass
