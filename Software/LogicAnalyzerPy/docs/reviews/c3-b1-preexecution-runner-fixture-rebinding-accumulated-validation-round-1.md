# C3-B1 pre-execution runner fixture rebinding — accumulated validation round 1

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact runner-rebinding candidate/tree:
  `ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` /
  `457240c481afcdf20ef41a74208749e112efa9b6`.
- Independent verification descendant/tree:
  `6a9f8a1451e7d887ba0dbe7fac1695ea0b55169c` /
  `f3a97c27d21a5d70856707726ac284700399a641`.
- Independent verifier identity:
  `c3-b1-pre-execution-runner-rebinding-verifier-1`.
- Completed: `2026-08-28T04:52:23Z`.
- Verdict: **pass for the reopened runner-rebinding gate**.

This accumulated gate authorizes only a fresh acceptance audit of the exact
runner-rebinding candidate and its verifier evidence. It transfers no prior
raw-baseline, threshold, operator-approval, final-binder, manifest, checkpoint,
or B2 pass.

## Corrected fixture binding and independent evidence

The runner binds corrected fixture candidate/tree
`a98d328aab92f3dad66988fb70cc567946dc89d0` /
`450aadcf26bd6c74860872bfbf0a0a1b32d94f3b` and these exact SHA-256 values:

- semantic fixtures:
  `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`;
- experiment caps:
  `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`;
- fixture manifest:
  `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`;
- candidate binding:
  `144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`.

The independent verification record SHA-256 is
`59bed0b1b0aac89b686425bf98e7b63b106b80b31a71c0e48b9dc5e6204a9031`;
its verifier-test SHA-256 is
`14793a958bdfa4bc92cb8a46115b413d70f8d0cd9e7fb28fb65ef0f8197f0562`.
The focused implementation plus independent suite passed 180 tests. It checks
all 17 exact cap accept/value-plus-one reject boundaries and independently
proves that stale candidate commit, candidate tree, cap, manifest, and semantic
fixture identities fail before `os.pipe` or `subprocess.Popen`.

Candidate-owned paths are byte-identical to `ca0ee751...` in the verification
descendant. The corrected cap, semantic-fixture, and fixture-manifest paths are
byte-identical to `a98d328...`.

## Clean Python 3.12 gate

Validation ran from clean clone
`/private/tmp/c3-runner-rebind-6a9f8a1` at the exact verification descendant,
not from the main worktree preserving untracked B2 work. The stable environment
`/private/tmp/cycle3-clean-python` was freshly cleared with managed CPython
3.12.13. `requirements-dev.lock` SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Exact result |
| --- | --- |
| clean hash-locked dependency install | exit 0; 21 locked packages |
| no-build-isolation/no-dependency editable install | exit 0; `pico-logic-analyzer==0.1.0` |
| clean `pip check` | exit 0; no broken requirements |
| Ruff over the whole project | exit 0 |
| strict mypy over `src` | exit 0; 21 files |
| strict mypy over runner tools | exit 0; seven files |
| installed CLI help | exit 0 |
| fixture generator `--check` | exit 0; no byte drift |
| runner binding `--check` | exit 0; no process launch |
| applicable clean pytest | 603 passed, one deselected, 149 inherited warnings |
| Cycle 2 evidence validators B1 through B6 | six exit-0 results |
| exact 64-GiB `RLIMIT_AS` set/readback | `(68719476736, 68719476736)` |

The initial dependency install inside the network-restricted sandbox failed
before installing any package. Root retried the same stable, hash-locked pip
class once through the reusable approval broker and it succeeded; no broad
interpreter approval or package-by-package request was used.

## Full-suite invalidation audit

The unfiltered clean suite was run first and is not represented as green: it
reported **650 passed and 44 failed** with 149 inherited warnings. One failure
is the historical exact-six-file fixture inventory assertion, which rejects
later governing JSON artifacts. The remaining 43 failures are exclusively in
five deliberately invalidated downstream B1 modules whose old runner, raw,
threshold, and final-candidate identities cannot survive this correction:

```text
tests/verification/test_c3_b1_final_candidate.py
tests/verification/test_c3_b1_preexecution_runner_candidate.py
tests/verification/test_c3_b1_raw_baseline_candidate.py
tests/verification/test_c3_b1_threshold_proposal.py
tests/verification/test_c3_b1_threshold_proposal_round2.py
```

The candidate-applicable rerun ignored exactly those five modules and
deselected exactly
`tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`.
It passed 603 tests with one deselection. These exclusions are ordered
invalidations, not waivers: raw baseline, threshold proposal, operator
approval, and final B1 evidence must be regenerated and accepted before a
replacement checkpoint.

## Frozen Node 22 regression

The exact Node executable was v22.14.0 at the stable
`/private/tmp/cycle2-node22` path. `npm ci --no-audit --no-fund` installed 215
locked packages. `package-lock.json` SHA-256 is
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`production-assets.json` SHA-256 is
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

- ESLint and TypeScript passed.
- Vitest passed three files and five tests.
- Vite built 29 modules and the asset checker found no drift.
- Exact-Node-22 Playwright passed the one-test maximum-width suite and the
  three-test live/shell suite.
- Exact-Node-22 Playwright passed the frozen B6 performance test and the clean
  Python threshold checker accepted the report. Report SHA-256:
  `7404120803bde93c151ab642b3f5a50572398f6da75c5fd7a66af619012770e2`.

The first browser invocation failed before running a test because the clean
clone lacked its expected `.venv` link. After linking only that clone to the
stable clean environment, the same saved Playwright command passed. No failed
browser attempt supplied evidence.

## Scope and disposition

- No decoder, compatibility helper, snapshot host with decoder input, raw
  baseline, fixture generation write, B2 host, C#/.NET/pythonnet,
  libsigrokdecode, hardware, serial, firmware, publication, or Cycle 4 action
  ran.
- The clean clone has only validation-local `.venv` and ignored Playwright
  `test-results` state; tracked files remain unchanged.
- The main worktree's two untracked B2 paths were neither inspected nor
  modified.
- No finding remains open in the runner-rebinding candidate. The exact evidence
  is ready only for fresh runner acceptance.

`pass`
