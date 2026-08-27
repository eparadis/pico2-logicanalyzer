# C3-B1 raw-baseline accumulated validation — round 1

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable raw candidate/tree:
  `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`.
- Unchanged corrected runner candidate/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`.
- Required independent raw verification: `pass`, committed at
  `9ac10d77cf1e8c492e7b5dae564baa43b09ebf71`; verifier-test SHA-256
  `08687a9bcc7fed1cfb55dbb6ec9b3c31f2ea486cfd389857916d6039b33567ca`
  and record SHA-256
  `c9c08720039de278c12c54501e09c71634f084408330af849011004a666441c2`.
- Clean validation descendant before this record: commit/tree
  `cf4824aa193a49d7dc82f0a00f1b40c5e6b3fcd1` /
  `dc2218f7f181a767b6955b4d6eeec9f6f4658c78`.
- Completed: `2026-08-27T06:34:24Z`.
- Verdict: **pass**. No mandatory check failed or remained skipped.

This gate repeats the full raw reproduction inside the complete accumulated
Python and Node regression matrix. It authorizes only a fresh independent raw
acceptance audit. It creates no threshold conclusion, proposal, operator
decision, product-host authority, B1 manifest, or checkpoint.

## Clean Python 3.12 environment

The environment was freshly cleared and rebuilt at
`/private/tmp/cycle3-clean-python` using managed CPython 3.12.13 on macOS
15.7.7 build 24G720, x86_64. The temporary path contains only the acceptance
interpreter and tools; every lint, type, test, generator, and product command
used `Software/LogicAnalyzerPy` as its repository working directory.

`requirements-dev.lock` SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Result |
| --- | --- |
| managed Python 3.12.13 `-m venv --clear /private/tmp/cycle3-clean-python` | exit 0 |
| `pip install --require-hashes -r requirements-dev.lock` | exit 0; 21 locked packages |
| `pip install --no-build-isolation --no-deps -e .` | exit 0; `pico-logic-analyzer==0.1.0` |
| clean `pip check` | exit 0; no broken requirements |
| Ruff over the complete project | exit 0 |
| strict mypy over `src` | exit 0; 21 files |
| strict mypy over all seven characterization tool modules | exit 0; seven files |
| fixture generator write plus `--check` | both exit 0; no drift |
| characterization binding `--check` | exit 0 |
| unrestricted non-hardware pytest | exit 0; 596 passed, no skip, 149 accepted warnings in 133.51 s |
| installed `pico-la --help` | exit 0 |
| focused semantic-fixture suites | exit 0; 18 passed |
| focused corrected-runner suites | exit 0; 190 passed |

The full pytest result includes all three raw verifier tests. It therefore
repeated one fresh unrecorded warm-up and five repetitions for all 63 derived
snapshot requests and repeated all ten hostile warm-up/five-repetition/recovery
cases. Canonical semantics, stable counts, cap enforcement, deadline,
terminate/kill, descriptor close, exact reap, recovery, summaries, identities,
and cache cleanup all passed again. The temporary full-run discrepancy report
SHA-256 was
`34fbbc0081cf5350af39b02d83b584227e36258e5811eff1a0fd46d72f3a21a1`;
it is diagnostic scratch, not immutable evidence or a threshold input.

The accepted warnings are inherited aiohttp application-key/deprecation
warnings and the deliberate duplicate-ZIP warning. No raw, runner, decoder,
fixture, containment, or new warning appeared.

## Resources, dependencies, and inherited evidence

- Exact `RLIMIT_AS` set/readback passed as
  `(68719476736, 68719476736)`.
- Cycle 2 evidence validator passed independently for `c2-b1.json` through
  `c2-b6.json` against the accepted draft-2020-12 schema.
- Accepted Cycle 1 manifest SHA-256 values remain: C1-B1
  `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc`,
  C1-B2
  `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af`,
  C1-B3
  `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598`,
  C1-B4
  `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead`,
  and C1-B5
  `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d`.
- The editable distribution lists only the installed CLI, editable-path file,
  and eight distribution-metadata files. It exposes no decoder snapshot,
  characterization runner, fixture, or raw file.
- `find_spec` returned `None` for `pythonnet`, `clr`, `sigrokdecode`, and
  `libsigrokdecode`. Active source/dependency scans found no prohibited runtime
  use. The accepted project/license disposition remains unchanged.
- Raw, corrected-runner, fixture/snapshot, Cycle 1/2 evidence, governing, and
  excluded-scope path families are quiet against their immutable owners.

## Exact Node 22 regressions

Node was exactly v22.14.0. `web/package-lock.json` SHA-256 is
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`web/production-assets.json` SHA-256 is
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

| Command class | Result |
| --- | --- |
| exact Node 22 `npm ci --no-audit --no-fund` | exit 0; 215 packages |
| ESLint and TypeScript | both exit 0 |
| Vitest | exit 0; three files, five tests |
| Vite build | exit 0; 29 modules |
| clean Python production-asset checker | exit 0; no drift |
| browser regressions | exit 0; one plus three tests |
| B6 offline performance plus accepted-threshold checker | exit 0; one test |

An orchestration-only attempt invoked a nonexistent JavaScript asset-checker
path after the successful build. It changed no file and transfers no result;
the actual governed Python asset checker was then run and passed. Browser and
performance output was moved intact to
`/private/tmp/cycle3-raw-accumulated-web-20260827T0632`. Performance report
SHA-256 is
`460ccc7426095c52cc9908b1f4457116ff709af003df583269e9b0a6b4db0ab9`.

## Discrepancies, scope, and disposition

The independent record's transparent discrepancy remains controlling: 61 of
63 reproduced total-time ranges were lower and non-overlapping while two
overlapped; child RSS overlapped for 58 cases and was lower for five, with none
higher and non-overlapping. The accumulated rerun did not edit raw evidence,
average away a failure, weaken a cap, or derive a numeric threshold.

The initial sandboxed hash-lock installation could not access the package
index and produced no valid environment result. Root reran the exact whole
hash-locked command under one reusable install capability; no package-by-
package authority was requested. Browser regression reused its existing exact
command capability, and one narrow reusable performance command class replaced
repeated per-process authorization. These orchestration observations do not
weaken any gate.

No product decoder host, public decode API, expected-output oracle, hardware,
USB/serial action, firmware, C#/.NET/pythonnet/libsigrokdecode/`sigrok-cli`,
external decoder runtime, publication, non-macOS claim, or Cycle 4 work ran.
No worker, pytest, Playwright, Vite, or npm process remained at each successful
test boundary; no characterization bytecode cache remained. Final repository
diff/status was clean before this record. Findings: none. Approval needed for
raw acceptance: none.

`pass`
