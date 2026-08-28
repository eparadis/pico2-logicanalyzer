# C3-B1 raw-baseline accumulated validation — round 2

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable raw candidate/tree:
  `2ae1e4335c38a5cf717491c7936f857292f71498` /
  `772b13476c97a976eb3a304e9b87aec8011260ec`.
- Corrected independent verification descendant/tree:
  `10a6a1f72fc4973c112bd1da0877ffdc2590f3f8` /
  `bb555307abe49d95dd2eda54ce2621c2cb56949e`.
- Completed: `2026-08-28T05:39:50Z`.
- Verdict: **pass**. No mandatory applicable check failed or remained skipped.

This gate authorizes only a fresh raw-baseline acceptance audit. It creates no
threshold proposal or decision, operator approval, final-B1 binder, replacement
manifest, checkpoint, or B2 authority.

## Raw candidate and corrected verification

The five canonical raw SHA-256 values are:

- environment:
  `fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34`;
- requests:
  `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`;
- observations:
  `28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd`;
- hostile observations:
  `d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080`;
- manifest:
  `7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e`.

The candidate binds accepted runner `ca0ee751...`, accepted runner-chain
descendant `bf1fc5e...`, corrected fixture `a98d328...`, binding
`144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`,
and corrected caps
`6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.
Raw, runner, and corrected fixture path families are byte-identical to their
immutable owners in the clean verification descendant.

Round-2 verification commit `b76554c...` reproduced every raw case but its
static test incorrectly required the verifier executable path to equal the
recorded collection executable path. The first accumulated run therefore
reported 606 passed, one failed, and one deselected. `C3B1-RV001` records that
failure; it supplied no pass. Round-3 corrected only verifier-owned path
provenance logic, leaving the raw candidate unchanged.

Corrected verifier-test SHA-256 is
`b29634ace872049ce275d93bc81274e0776236d688b6ef2cbbb243922b0db016`;
round-3 record SHA-256 is
`8fdf25cd7da0b07deae21631709a1a5b76700f233af5590fae0cf1eee4f4c2eb`.
The verifier's round-3 reproduction performed 486 child launches and passed.

## Clean Python 3.12 accumulated gate

The successful gate ran from clean clone
`/private/tmp/c3-raw-refresh-10a6a1f` at the exact corrected verification
descendant. Stable environment `/private/tmp/cycle3-clean-python` used managed
CPython 3.12.13 and was built from the exact hash-locked development
requirements. `requirements-dev.lock` SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Exact result |
| --- | --- |
| clean hash-locked dependency install | exit 0; 21 locked packages |
| no-build-isolation/no-dependency editable install | exit 0; `pico-logic-analyzer==0.1.0` |
| clean `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| strict mypy over product `src` | exit 0; 21 files |
| strict mypy over runner tools | exit 0; seven files |
| fixture generator `--check` | exit 0; no drift |
| runner binding `--check` | exit 0 |
| installed CLI help | exit 0 |
| exact 64-GiB `RLIMIT_AS` set/readback | `(68719476736, 68719476736)` |
| Cycle 2 B1 through B6 evidence validators | six exit-0 results |
| complete candidate-applicable pytest | 607 passed, one deselected, 149 inherited warnings |

The applicable suite included another full raw reproduction: 63 snapshot
warm-ups plus 315 retained snapshots; ten hostile warm-ups plus 50 retained
hostile runs; and eight recovery warm-ups plus 40 retained recoveries. All 63
snapshot semantics and stable counts matched five of five. Both designed
success-hostile kinds passed five of five; all eight designed failures failed
as classified and every retained recovery passed. Every child was reaped and
both protocol descriptors were closed. The accumulated reproduction report
SHA-256 is
`9c79b32e8488bd6aa9118cfa799f7442249b2fbf08a83f90348b0980e504b1f7`.

## Exact downstream invalidation audit

A separate targeted suite ran the historical exact-six-file inventory
assertion and the four downstream B1 modules not applicable until later gates.
It reported **43 failed and 45 passed**. The failures were exactly:

- one historical fixture-inventory assertion;
- 18 final-candidate assertions;
- one superseded runner-candidate assertion;
- 22 threshold-proposal assertions;
- one threshold-proposal-round-2 assertion.

The applicable command therefore deselected only
`tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`
and ignored only:

```text
tests/verification/test_c3_b1_final_candidate.py
tests/verification/test_c3_b1_preexecution_runner_candidate.py
tests/verification/test_c3_b1_threshold_proposal.py
tests/verification/test_c3_b1_threshold_proposal_round2.py
```

These are ordered invalidations, not waivers. Each downstream module must be
rebound and rerun by its owning gate.

## Frozen Node 22 regression

Node was exactly v22.14.0 at `/private/tmp/cycle2-node22`.
`package-lock.json` SHA-256 is
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`production-assets.json` SHA-256 is
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

- `npm ci --no-audit --no-fund` installed 215 locked packages.
- ESLint and TypeScript passed.
- Vitest passed three files and five tests.
- Vite built 29 modules; the production-asset checker found no drift.
- Exact-Node-22 Playwright passed the one-test maximum-width suite and the
  three-test live/shell suite.
- Exact-Node-22 Playwright passed the frozen B6 performance test; the clean
  Python threshold checker accepted report SHA-256
  `9d72ea71b240367d75288da5cba94d021ccecf95fb842fa2f9a60b636292bb04`.

The clone-local `.venv` symlink and Playwright `test-results` directory are
validation-only untracked state. Tracked clone bytes remain unchanged.

## Scope, cleanup, and disposition

- Process queries after validation returned only their own transient query
  PIDs; the underlying test, browser, Vite, pytest, runner, worker, and decoder
  processes had exited.
- No tool bytecode cache remained after each raw reproduction boundary.
- No expected-output oracle, threshold derivation, product decoder host,
  public decode API, hardware, USB/serial, firmware, C#/.NET/pythonnet,
  libsigrokdecode, publication, or Cycle 4 action occurred.
- The main worktree's untracked B2 paths were neither inspected nor modified.
- Open raw-candidate findings: none. `C3B1-RV001` is resolved.

The exact raw candidate and corrected verification evidence are ready only for
fresh raw-baseline acceptance.

`pass`
