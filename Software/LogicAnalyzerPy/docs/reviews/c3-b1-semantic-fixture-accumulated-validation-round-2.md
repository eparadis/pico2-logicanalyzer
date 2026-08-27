# C3-B1 semantic-fixture accumulated validation — round 2

## Subject and result

- Root validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact tested corrected fixture candidate/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Required fresh independent verification: round-9 `pass`, committed at
  `8b08f7d`; record SHA-256
  `3e2f507332fdfc82e8e49df016b66db223508144677cc5166d8a4e090d0378c6`.
- Validation descendant before this record:
  `ca69401d46a31d0e0224c2239d95ef9b933d33fd` / tree
  `491b226fee517ea86996264c91dee8b65a9e4293`. Exact candidate-path quiet diff
  was empty and the worktree was clean before this record was created.
- Validation completed: `2026-08-27T03:19:26Z`.
- Result: **pass**. No mandatory check failed or skipped.

This is accumulated validation of the corrected static semantic-fixture and
finite-cap specification. It makes no executable cap-enforcement, decoder-
runtime, characterization, threshold, operator-approval, publication, or
hosted-CI claim. Round-8 verification, accumulated round 1, and acceptance
round 1 remain immutable old-candidate history and transfer no authority.

## Clean Python 3.12 gate

Environment: macOS 15.7.7 build 24G720, x86_64; managed CPython 3.12.13;
freshly cleared stable environment `/private/tmp/cycle3-clean-python`; pip
25.0.1. `requirements-dev.lock` SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command | Exact result |
| --- | --- |
| managed Python `-m venv --clear /private/tmp/cycle3-clean-python` | exit 0; Python 3.12.13 |
| clean Python `-m pip install --require-hashes -r requirements-dev.lock` | exit 0; every artifact hash-locked |
| clean Python `-m pip install --no-build-isolation --no-deps -e .` | exit 0; `pico-logic-analyzer==0.1.0` |
| clean Python `-m pip check` | exit 0; no broken requirements |
| clean Python `-m ruff check .` | exit 0; all checks passed |
| clean Python `-m mypy src` | exit 0; no issues in 21 source files |
| clean Python `-m pytest -m "not hardware"` | exit 0; all 403 collected tests passed, no skip, 149 warnings |
| clean Python `-m pico_logic_analyzer --help` | exit 0; installed module help rendered |

The inherited aiohttp key/deprecation warnings and deliberate duplicate-ZIP
warning are non-failing accepted regression warnings. No skip qualification or
historical result was needed: all 403 tests passed in the fresh run.

The editable distribution file list contains only the `pico-la` entry point,
editable package pointer, and distribution metadata; it exposes no decoder
snapshot. Existing metadata remains MIT. The independent project/license
engineering disposition passed at `538a4aa` (record SHA-256
`b7afc4df18ba9bf5e40ee5a795e4544e54a59be27b1fea9a8617681ea82919cf`),
but its prescribed future private placement, attribution/license files,
GPL-3.0-only distribution metadata, verification, and rights-holder/counsel
limitation have not been simulated or bypassed.

## Corrected fixture, source, and evidence gates

| Check | Exact result |
| --- | --- |
| clean Python generator write, then `--check` | two exit-0 results; byte-identical rebuild |
| clean Python implementation plus immutable verifier tests | exit 0; 18 passed |
| corrected 64-GiB `RLIMIT_AS` set/readback in clean Python | exit 0; exact `(68719476736, 68719476736)` |
| installed-distribution `find_spec` prohibited dependency/import audit | exit 0; no pythonnet, CLR, libsigrokdecode, sigrok package, or `sigrokdecode` |
| scoped active product/lock/workflow prohibited-name scan | exit 1 for no matches; zero prohibited references |
| root-visible process snapshot plus offline name scan | exit 1 for no matches; zero prohibited/runtime/runner/browser-server processes |
| accepted Cycle 2 validator against `c2-b1.json` through `c2-b6.json` | six exit-0 results |
| accepted Cycle 1 manifest JSON/hash and Cycle 1/2 checkpoint preservation | five exact hashes; checkpoint quiet diff exit 0 |
| candidate-path quiet diff, full repository diff check, and final status | all exit 0; candidate unchanged and worktree clean |

The round-9 independent verifier freshly recomputed the nine-file closed AST
imports, byte digests, notices, three ordered file sets, declarations, 63
timelines, 1,058 waits, 1,049 records, 165 option rows, 12 v1 roots/goldens,
and all 17 cap derivations. Root's fresh 18-test focused gate independently
exercised the deterministic generator and strong cap/fixture assertions. No
decoder or expected-output oracle was invoked.

Corrected candidate SHA-256 values are generator
`6fc5289ba1076413283942be0374bd97def08b284bf7a7cef4e7b6105636be63`,
semantic-fixture document
`86ca972e1522ad12ab459902dacffa933d6f89289088815d7584b9f627e69d39`,
experiment caps
`63cde36892a15a390be0c27c50eac18431d7a4b11381b0e4b82c0fe64f808cd8`,
fixture manifest
`0f5f1d9a01fc807dd0f4078ac84b20158f515a76ae4f1f83cc74651c4797413a`,
and implementation test
`838e5a81d5778437edf7ea652eea0921aee58a300f3a9f6a024ac1943e97d273`.
Provenance, semantic JSON, option matrix, and typed vectors remain respectively
`e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`,
`8da1d2aa2256cce5c56ac2df4a629d90a95c21cb84d633522780394439888e64`,
`5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`,
and `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`.

Accepted Cycle 1 manifest identities remain exactly:

| Manifest | SHA-256 |
| --- | --- |
| `c1-b1.json` | `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc` |
| `c1-b2.json` | `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af` |
| `c1-b3.json` | `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598` |
| `c1-b4.json` | `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead` |
| `c1-b5.json` | `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d` |

All Cycle 1/2 manifests remain byte-unchanged from accepted checkpoint
`7fe1f5c`.

## Inherited optional-web and performance regression

The accepted official Node identity remains v22.14.0 and archive SHA-256
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
| exact Node 22 Vite production build plus asset checker | exit 0; 29 modules; no asset drift |
| exact Node 22 Playwright accepted browser regressions | exit 0; 1 plus 3 tests passed |
| exact Node 22 B6 offline performance spec | exit 0; 1 test passed |
| clean Python approved-threshold checker | exit 0 |

The temporary performance report SHA-256 is
`722cdcbce8eeb58d694157bfe31e80e87ded5ed998cc4ed70b9b0ef37c4d1ac2`.
Generated Playwright results were moved outside the repository, and a fresh
root-visible process snapshot found no lingering Playwright, Vite, web server,
runner, worker, or prohibited runtime. These unchanged regressions create no
Cycle 3 browser-decoder authority.

## Scope, findings, and disposition

- The only corrected candidate delta is the five fixture-owned cap/prose/
  generator/manifest/assertion paths. All authoritative semantic outputs and
  source identities remain unchanged; descendant changes are review/progress
  evidence only.
- No decoder, compatibility shim/helper, runner candidate, C#, .NET,
  pythonnet, libsigrokdecode, `sigrok-cli`, external/reference runtime,
  hardware, USB/serial device, live capture, raw characterization, firmware,
  publication, unsupported-platform claim, or Cycle 4 work occurred.
- Hardware/native regression remains accepted immutable Cycle 1/2 evidence
  and was not rerun because Cycle 3 prohibits physical access. Hosted exact-
  candidate CI is mandatory only at C3-B4 and C3-B5, not this internal B1 gate.
- The corrected 64-GiB value is still an experiment-only absolute address-
  space specification. Set/readback proves feasibility only; executable
  boundary enforcement and cleanup remain exclusively the later distinct
  runner candidate's burden.
- Findings: none.
- Approval needed: none. The stable hash-locked install, browser, and process-
  visibility command classes reused consolidated root-brokered approvals.

pass
