# C3-B1 replacement final accumulated validation — round 3

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable replacement candidate/tree:
  `4a7dc728048812cfb4cf46f010939c182ac948cf` /
  `5ee316695d3a4acf8f30e60da377ba6651844969`.
- Fresh verification descendant/tree:
  `fdbbc120d8bfa4d57e10c5c0ebe3737b3b98a71f` /
  `8ef2194c11f1561ab79e5a766fa4c01d5c26ef94`.
- Completed: `2026-08-28T13:42:41Z`.
- Verdict: **pass**. No applicable mandatory gate failed or remained skipped.

This gate authorizes only fresh independent replacement final-B1 acceptance.
It creates no manifest, checkpoint, B2 authority, or Cycle 4 authority.

## Exact candidate and verification

The candidate JSON and rationale remain byte-identical to immutable candidate
`4a7dc72`, at SHA-256 values
`a46a7b3fc5a684a77990b8f4373f710002411901d2610d1fa30d275e5b07f57c`
and
`eb570fe3498232a0a206dc168a5afa0f404eca9dd8d1a173a99e746b6a6af20b`.
The candidate remains `candidate-not-accepted`.

Fresh verifier `c3-b1-final-verifier-3` added only its verifier-owned test and
round-4 record. Their SHA-256 values are respectively
`3fc6503e2273bfd24c4f908ffb08f0235b498e86913eca33137725224dc6118f`
and
`caadb30ef321413329cc4f9b976ace41232c4cf90df4f891239b082347ce7355`.
Its independent static suite passed 23 tests, including exact candidate/tree,
34 live digest bindings, complete role histories, correction/finding order,
all 29 approved boundaries, frozen commands, applicability, exclusions, and a
non-vacuous mutation matrix. No finding remains open.

## Repository-local Python 3.12 gate

Python tooling ran from ignored repository-local environment
`Software/LogicAnalyzerPy/.venv`, CPython 3.12.13. Exact tested source came from
clean clone `/private/tmp/c3-final-clean` through `PYTHONPATH`; no Python
virtual environment was created or executed from `/private/tmp`, no package
was installed, and no dependency/network approval was needed.
`requirements-dev.lock` and `pyproject.toml` remain at SHA-256 values
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
and
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Result |
| --- | --- |
| repository-local `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| strict mypy over product `src` | exit 0; 21 source files |
| strict mypy over all seven characterization modules | exit 0; seven files |
| deterministic Cycle 3 fixture generator `--check` | exit 0; no drift |
| characterization binding `--check` | exit 0; no drift |
| installed CLI help | exit 0 |
| all six accepted Cycle 2 evidence validators | exit 0 each |
| fresh static final verifier | exit 0; 23 passed |
| complete applicable unrestricted non-hardware pytest | exit 0; 654 passed, four optional inherited skips, two historical deselections, 149 warnings in 120.91 s |

The applicable suite included the complete 486-child raw-baseline reproduction.
Every retained snapshot and hostile/recovery case matched its accepted
semantics and counts; all designed failures were classified, every recovery
succeeded, every child was reaped, and protocol descriptors were closed.

### Exact applicability and optional-artifact classification

The suite deselected exactly two immutable historical JSON-namespace nodes:

1. `tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`;
2. `tests/verification/test_c3_b1_semantic_fixture_correction.py::test_historical_inventory_failure_and_broad_mypy_non_gate_are_not_weakened`.

It ignored only four downstream or superseded exact-subject modules:

```text
tests/verification/test_c3_b1_final_candidate.py
tests/verification/test_c3_b1_preexecution_runner_candidate.py
tests/verification/test_c3_b1_threshold_proposal.py
tests/verification/test_c3_b1_threshold_proposal_round2.py
```

The four skips are exclusively
`tests/verification/test_c2_b3_physical_artifacts_blackbox.py`: three
parameterized physical-capture artifact cases and one recovery-summary case.
The test's accepted optional branch states that the machine-local C2-B3
physical-artifact directory was not supplied and that checked-in sanitized
evidence remains covered by mandatory nonhardware validation. The default
directory exists but is currently empty. These are inherited optional physical
artifact reruns, not skipped Cycle 3 or mandatory nonhardware proof.

A separate targeted invalidation audit reported exactly 44 expected historical
failures and 45 passes: two inventory assertions, 18 old final-candidate
assertions, one old runner assertion, 22 round-1 proposal assertions, and one
round-2 proposal assertion failed while remaining negative checks passed.
These are ordered invalidations, not waivers.

## Repository-local exact Node 22 regression

Node was exactly v22.14.0 from ignored repository-local path
`Software/LogicAnalyzerPy/.venv/node22`. The clean source clone used only
validation-only symlinks to the repository-local `.venv` and existing
`node_modules`; no runtime or dependency was installed in `/private/tmp` and no
download occurred. `web/package-lock.json` and `web/production-assets.json`
remain at SHA-256 values
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
and
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

- ESLint and TypeScript passed.
- Vitest passed three files and five tests.
- Vite built 29 modules; the governed production-asset checker found no drift.
- Playwright passed the one-test maximum-width suite and three-test live/shell
  suite.
- Frozen B6 performance passed; the unchanged threshold checker accepted
  report SHA-256
  `ac9068e15313ecb9c5c8f19b79739881741d881263fa970240519c7534ab86c4`.

The first maximum-width Playwright invocation exited before a test because the
clean clone did not yet have its validation-only `.venv` link. It supplied no
evidence. After linking the existing repository-local environment, the exact
test passed; no package, runtime, source, or candidate byte changed. The saved
reusable Playwright approval class covered all browser child processes without
per-process prompts.

## Scope, cleanup, and disposition

Tracked clean-clone bytes remain unchanged. Its only untracked state is the two
validation-only environment/dependency symlinks and generated browser results.
Final root-brokered process inspection found no pytest, Playwright, Vite,
characterization, product-web, or `server.main` process. Main-worktree B2 paths
were neither inspected nor modified.

No product decoder host, public decode API, external/reference runtime,
hardware/USB/serial action, firmware, package build/publication, non-macOS
claim, B2 execution, or Cycle 4 work occurred. Findings: none. Next authority:
fresh independent replacement final-B1 acceptance.

`pass`
