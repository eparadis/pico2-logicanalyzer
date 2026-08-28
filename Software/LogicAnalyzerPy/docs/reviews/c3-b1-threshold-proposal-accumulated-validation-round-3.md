# C3-B1 threshold-proposal accumulated validation — round 3

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable proposal candidate/tree:
  `b260d9ecc0e74ed2502dda89beebb851ddfedb77` /
  `8a65628df5ba63727e8305e901b9954fe0bec7e5`.
- Required fresh verification descendant/tree:
  `92de4e6c9c57ba258f2991c92c3e1569cf659ad4` /
  `1317567a736035e8123da1b5a50ab8a3c1250da7`.
- Completed: `2026-08-28T06:32:37Z`.
- Verdict: **pass**. No applicable mandatory check failed or remained skipped.

This gate authorizes only fresh independent proposal acceptance. It does not
approve any numeric value, transfer the superseded round-2 approval, create
product enforcement, authorize B2, or create a final-B1 binder or checkpoint.

## Identity and fresh verification

The proposal and rationale remain byte-identical to candidate `b260d9e`, with
SHA-256 values
`7fb9e88aaa5888e1a3133ff2234253bdfbbc4bd7151fc3a3be3c387dd619f510`
and
`8ea67712009a8a730c6eba8834e063179b709f07dfcdc5ffd7e9a55f6a93c58b`.
The proposal remains exactly `proposal-not-approved`.

Fresh verifier test and record SHA-256 values are respectively
`60068a4cc155b9661a5a558c4ca07a0766b0b581ecd86dcc246eccc2c311953d`
and
`2209b61e8460e77a6118a9c934315d4bd89c150d46e5645436e52c9df304338c`.
Its 29-case static suite passed. Independent recomputation covered all 29 raw
maxima, formulae, units, kinds, caps, accept/reject boundaries, cross-limit
guards, evidence identities, and the exact prior-round comparison. Twenty-eight
numeric values are unchanged; only `successful_parent_total_ns` changes from
900,000,000 to 1,000,000,000 ns. The former proposal and approval are explicitly
superseded and confer no round-3 authority.

## Repository-local Python gate

Formatting, typing, validation, and testing used the ignored repository-local
`Software/LogicAnalyzerPy/.venv`, Python 3.12.13. The exact verification
descendant source was supplied from clean clone
`/private/tmp/c3-threshold-round3-92de4e6` via `PYTHONPATH`; no Python virtual
environment was created or run from `/private/tmp`, no package was installed,
and no dependency or network authorization was needed. `pip check` passed.
`requirements-dev.lock` and `pyproject.toml` SHA-256 values remain
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
and
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Result |
| --- | --- |
| repository-local `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| strict mypy over `src` | exit 0; 21 source files |
| strict mypy over all seven characterization modules | exit 0; seven files |
| deterministic Cycle 3 fixture generator `--check` | exit 0; no drift |
| characterization binding `--check` | exit 0; no drift |
| installed CLI help | exit 0 |
| all six accepted Cycle 2 evidence validators | exit 0 each |
| complete applicable unrestricted non-hardware pytest | 635 passed, two explicitly deselected, 149 inherited warnings in 133.93 s |

The passing suite included the full raw-baseline reproduction: 486 child
launches across snapshot, hostile, and recovery executions. Every child was
reaped, protocol descriptors were closed, all retained semantics and stable
counts matched, all designed failures were classified, and every recovery
succeeded.

### Exact applicability classification

The first unrestricted inventory produced 633 passes, one history-sensitive
failure, two sandbox loopback skips, and one deselection. It discovered that
the semantic-fixture correction inventory assertion, like the earlier fixture
inventory assertion, freezes the JSON namespace before the required round-3
proposal existed. The final run enabled loopback and deselected exactly these
two historical node IDs:

1. `tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`;
2. `tests/verification/test_c3_b1_semantic_fixture_correction.py::test_historical_inventory_failure_and_broad_mypy_non_gate_are_not_weakened`.

It ignored only these downstream or superseded exact-subject modules:

```text
tests/verification/test_c3_b1_final_candidate.py
tests/verification/test_c3_b1_preexecution_runner_candidate.py
tests/verification/test_c3_b1_threshold_proposal.py
tests/verification/test_c3_b1_threshold_proposal_round2.py
```

These are ordered invalidations, not waivers. A separate targeted audit ran the
two historical nodes and all four modules. Its exact expected result was 44
failed and 45 passed: two inventory assertions, 18 final-candidate assertions,
one superseded runner assertion, 22 round-1 proposal assertions, and one
round-2 proposal assertion failed, while their remaining negative coverage
continued to pass.

## Repository-local exact Node 22 regression

Node was exactly v22.14.0 at ignored repository-local path
`Software/LogicAnalyzerPy/.venv/node22`. No Node runtime or dependency was
installed in `/private/tmp`, and no dependency download occurred.
`web/package-lock.json` and `web/production-assets.json` SHA-256 values remain
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
and
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

- ESLint and TypeScript passed.
- Vitest passed three files and five tests.
- Vite built 29 modules; the governed production-asset checker found no drift.
- Playwright passed the one-test maximum-width suite and three-test live/shell
  suite.
- The frozen B6 performance test passed and the unchanged threshold checker
  accepted report SHA-256
  `387eaeb878960aa7239f7f0a265cb7e435576665fd8537e10579557c481a8979`.

One reusable loopback/browser authorization class covered the pytest and
Playwright process families; no per-child authorization was requested.

## Scope and disposition

Final hash checks and `git diff --check` passed. The clean validation clone had
no tracked or untracked change. Main-worktree browser results are ignored
validation artifacts. The two pre-existing untracked B2 paths were neither
inspected nor modified.

No product decoder host, public decode API, approved-limit file, hardware,
USB/serial action, firmware, external runtime, publication, Cycle 4 work, or
numeric operator decision occurred. Findings: none. Next authority: fresh
independent round-3 threshold-proposal acceptance.

`pass`
