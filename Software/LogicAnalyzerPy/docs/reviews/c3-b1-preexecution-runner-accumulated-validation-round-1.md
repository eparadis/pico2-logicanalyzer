# C3-B1 pre-execution runner accumulated validation — round 1

## Subject and result

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact immutable runner candidate/tree:
  `11a8ade5d828830347095bf2580766c149cb8aef` /
  `61fa5ba18f3620188ee61dac7e3622803591aad9`.
- Accepted fixture candidate/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Required independent runner verification: round-1 `pass`, committed at
  `8464a049c0809c9f0338c1cf7ad7ac90d1ec19eb`; record SHA-256
  `a1ca9a6c75b6bdca682ef00c07a4bb72e48c69d18cc493d05ba812a5bb241024`
  and independent-test SHA-256
  `6dc7f48c7312a318f370c4e98de57aed72cec270e378339ccc44f05bbc15bf7a`.
- Clean validation descendant before this record: commit/tree
  `8464a049c0809c9f0338c1cf7ad7ac90d1ec19eb` /
  `3288701308794cdb42e61f75fbe7ec18266d8596`.
- Completed: `2026-08-27T05:03:46Z`.
- Result: **pass**. No mandatory check failed or remained skipped.

This is the ordered accumulated **non-decoder** gate for the exact runner
candidate. It authorizes only assignment of the distinct runner acceptance
identity. It does not execute or approve a snapshot, create a raw baseline,
approve a threshold, expose a public host, create a B1 manifest/checkpoint, or
transfer to changed runner bytes.

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
| clean Python `-m pip install --require-hashes -r requirements-dev.lock` | exit 0; 21 hash-locked packages installed |
| clean Python `-m pip install --no-build-isolation --no-deps -e .` | exit 0; `pico-logic-analyzer==0.1.0` |
| clean Python `-m pip check` | exit 0; no broken requirements |
| clean Python `-m ruff check .` | exit 0; all checks passed |
| clean Python `-m mypy src` | exit 0; no issues in 21 source files |
| clean Python `-m mypy tools/cycle3_characterize` | exit 0; no issues in seven runner modules |
| clean Python unrestricted `-m pytest -m "not hardware"` | exit 0; 590 passed, no skip, 149 accepted warnings |
| clean Python `-m pico_logic_analyzer --help` | exit 0; installed help rendered |

The first sandboxed full-test run produced 588 passes and two explicit
loopback-sandbox skips. It is not the authoritative result. Root reran the same
complete command through the stable approved test capability; all 590 tests
then passed with no skip. The inherited aiohttp key/deprecation warnings and
deliberate duplicate-ZIP warning are non-failing accepted regressions.

The installed distribution has ten files and exposes no decoder, Cycle 3
snapshot, or runner file. `find_spec` found no `pythonnet`, `clr`,
`sigrokdecode`, or `libsigrokdecode` module. The existing project/license
engineering disposition remains the immutable `538a4aa` pass; no distribution
claim or metadata change is made here.

## Runner, fixture, containment, and inherited evidence gates

| Check | Exact result |
| --- | --- |
| clean Python accepted fixture generator write plus `--check` | two exit-0 results; no byte drift |
| clean Python runner implementation plus independent verifier | exit 0; 187 passed |
| exact 64-GiB `RLIMIT_AS` set/readback | exit 0; `(68719476736, 68719476736)` |
| runner binding `--check` and exact candidate-path quiet diff | exit 0; unchanged candidate |
| independent verifier source/method/cap/process matrix | 21 passed; immutable `pass` at `8464a04` |
| accepted Cycle 2 validator for `c2-b1.json` through `c2-b6.json` | six exit-0 results |
| Cycle 1 manifest SHA-256 and Cycle 1/2 checkpoint preservation | five exact hashes; quiet diff exit 0 |
| installed forbidden-import/snapshot exposure audit | zero imports; zero exposed files |
| product/dependency/lock/Cycle-2-workflow prohibited-name scan | exit 1 for no matches |
| final process snapshot | no runner, worker, decoder, prohibited runtime, pytest, Vite, or Playwright process |
| repository diff check and final status | exit 0; clean before this record |

The independent and root runner matrices exercise the exact immutable 17-cap
profile and private non-weakenable test profiles; pre-spawn sample/request
limits; streaming protocol/stdout/stderr/diagnostic limits; output/text/binary/
decoded/encoded/depth/item/retention accounting; recursion and address-space
limits; malformed/partial/extra/nonfinite results; graceful terminate, forced
kill, close, exact reap, and recovery. Static checks bind the accepted fixture,
exact nine source bytes and ordered sets, fixed Python/CWD/environment/import
graph, closed options, API-v3 compatibility behavior, disabled public route,
and structurally present private post-gate route. No snapshot route was called.

Exact runner candidate SHA-256 values remain: binding
`0b9fc2a02eef194c48392db2903c6296e764c0fe9a8368d51c2551c83ed60682`,
launch `c6cf91ebc42d3770ffc239b531424a128a2cf06c5aa97ed99b980bc48a86c9f8`,
runner `cd70e895794ace146be5830aeb5fff99a3aaf009c0049eb730e69ab53e5a9d32`,
worker `69e8eaccad236c6ec746aa5fd2ca11c26ae47f4b7306323c9710e2603ed65be5`,
snapshot host
`0da598c3facd1af89d34d6a82996a09a24b0cc4d691eb5c79f0ac576e051ab67`,
accounting
`924f563067bb23fc838b9b63b05b7e209f656fab68ee9859df4839f270bbd2d5`,
probes `be0da3bdc27e0a228b946a339ca278b55466c48d24170552ee8eac3150942f2e`,
method `eb4349d60aad922381a64579e1584271ec035dfa80d52f16881709b5260e2837`,
and focused implementation test
`c97cd9a66b1a5fff6ec72565ca41008bc8874f9a929d01e84b2e582a379a9f4d`.

Accepted Cycle 1 manifest identities remain:

| Manifest | SHA-256 |
| --- | --- |
| `c1-b1.json` | `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc` |
| `c1-b2.json` | `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af` |
| `c1-b3.json` | `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598` |
| `c1-b4.json` | `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead` |
| `c1-b5.json` | `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d` |

## Exact Node 22 browser and performance regression

The accepted Node identity is v22.14.0. `web/package-lock.json` SHA-256 is
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`web/production-assets.json` remains
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

| Command class | Exact result |
| --- | --- |
| exact Node 22 npm `ci --no-audit --no-fund` | exit 0; 215 locked packages |
| exact Node 22 ESLint and TypeScript | both exit 0 |
| exact Node 22 Vitest | exit 0; three files, five tests |
| exact Node 22 Vite build plus asset checker | exit 0; 29 modules; no asset drift |
| exact Node 22 accepted browser regressions | exit 0; one plus three tests passed |
| exact Node 22 B6 offline performance spec | exit 0; one test passed |
| clean Python approved-threshold checker | exit 0 |

An initial npm command inherited host Node 26.7.0 through the npm shebang. Its
results are explicitly invalidated. Root reset the exact environment through
`PATH=/private/tmp/cycle2-node22/bin:/usr/bin:/bin`, reran npm clean-install and
every Node gate, and confirmed v22.14.0. The temporary performance report
SHA-256 is
`325206187507f0672b9a6c1edd08aeb4398a6fa5b1a4712d5207a8f406835dae`;
all generated Playwright results were moved to
`/private/tmp/cycle3-runner-web.tSXXOT` before final scope inspection.

## Scope, approval preflight, and disposition

- Candidate-owned paths are byte-identical to `11a8ade5`; descendant changes
  before this record are only the assignment progress commit and the two
  immutable verifier-owned paths. The corrected fixture and governing bytes are
  unchanged.
- The accumulated gate ran the accepted fixture generator only for byte-stable
  regression. It did not run a decoder, approved snapshot, compatibility
  helper, product decode host, C#/.NET/pythonnet/libsigrokdecode/sigrok runtime,
  hardware, USB/serial action, raw characterization, publication, or Cycle 4
  work. Browser tests used temporary loopback servers only and left none active.
- Hosted exact-candidate CI is mandatory at C3-B4 and C3-B5, not this internal
  B1 runner gate. Physical regression remains accepted Cycle 1/2 evidence and
  was not rerun because Cycle 3 prohibits hardware access.
- Approval preflight reused stable command classes. One stable hash-locked
  clean-environment pip-install capability and exact Node-22 project browser/
  performance script capabilities were centrally brokered; there was no
  package-by-package, credential, device, or subagent escalation.
- Findings: none. Approval needed: none. The exact unchanged candidate is ready
  only for the distinct runner acceptance audit.

pass
