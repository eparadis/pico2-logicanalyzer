# C3-B1 pre-execution runner accumulated validation — round 2

## Subject and result

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Corrected immutable runner candidate/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`.
- Accepted fixture candidate/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Required independent round-2 runner verification: `pass`, committed at
  `8bcd7ba19795633a9e0e215c1d9f2cc47a893b03`; record SHA-256
  `0fc07aea133702352d0dee74d18e4287f707481b598773481d7c9d37501942dc`
  and verifier-test SHA-256
  `c6cec19e2e97a833315270d2ae9dbf1cd9b19433122cf545b1f5d2512204bf5b`.
- Clean validation descendant before this record: commit/tree
  `4bbffc8568ccf2915713abf14b5f2ad8725117e9` /
  `95a6553c942f90a73e16bb27888e52af403fd980`.
- Completed: `2026-08-27T05:36:25Z`.
- Result: **pass**. No mandatory check failed or remained skipped.

This is the complete fresh accumulated **non-decoder** gate after RI013. The
superseded round-1 candidate, verification, accumulated result, acceptance, and
provisional raw attempts transfer no pass. This result authorizes only a fresh
acceptance audit of the corrected unchanged runner. It does not authorize a
snapshot retry, raw candidate, threshold, public host, manifest, or checkpoint.

## RI013 history and corrected repeatability

The originally accepted `-I worker.py` launch ignored environment-only
`PYTHONDONTWRITEBYTECODE`, so each of three ordered raw-collection attempts ran
only the unrecorded `uart-rx-valid-default` warm-up before a child-created
`snapshot_host.pyc` made every recorded repetition and later request fail
pre-launch. No SPI or I2C snapshot and no recorded raw repetition ran. Those
provisional files and caches remain quarantined under the explicit
`/private/tmp/cycle3-raw-invalidated-launch-v1-20260827T0518` and
`/private/tmp/cycle3-characterize-pycache-failed-*` paths.

The corrected candidate fixes both frozen launch identities at
`-I -B worker.py`. Fresh implementation and independent verification exercise
two consecutive real inert sibling-import workers, require bytecode-disabled
diagnostics, exact-path-bound `probes.py`, unchanged inventory after each run,
and valid recovery. The clean accumulated runs repeatedly exercised that path;
no `__pycache__`, extra inventory entry, or worker remained. No fourth snapshot
execution occurred.

## Clean Python 3.12 gate

Environment: macOS 15.7.7 build 24G720, x86_64; managed CPython 3.12.13; fresh
`--clear` environment `/private/tmp/cycle3-clean-python`; pip 25.0.1.
`requirements-dev.lock` SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
`pyproject.toml` SHA-256 is
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Exact result |
| --- | --- |
| managed Python `-m venv --clear /private/tmp/cycle3-clean-python` | exit 0; Python 3.12.13 |
| clean Python hash-locked requirements install | exit 0; 21 locked packages |
| clean Python no-build-isolation/no-dependency editable install | exit 0; `pico-logic-analyzer==0.1.0` |
| clean Python `pip check` | exit 0; no broken requirements |
| clean Python Ruff over the whole project | exit 0; all checks passed |
| clean Python strict mypy over `src` | exit 0; no issues in 21 source files |
| clean Python strict mypy over runner tools | exit 0; no issues in seven files |
| clean Python unrestricted non-hardware pytest | exit 0; 593 passed, no skip, 149 accepted warnings |
| clean Python installed CLI help | exit 0; help rendered |
| clean Python corrected implementation plus verifier | exit 0; 190 passed |

The first sandboxed full-test run produced 591 passes and the same two explicit
loopback-sandbox skips as historical validation. It is invalidated as the
authoritative result. The exact command was rerun using the saved loopback
pytest capability and produced all 593 passes with no skip. Warnings are the
inherited aiohttp key/deprecation observations plus the deliberate duplicate-
ZIP warning; no new runner warning or failure appeared.

The installed distribution lists exactly ten files and exposes no decoder,
snapshot, or runner file. `find_spec` found no `pythonnet`, `clr`,
`sigrokdecode`, or `libsigrokdecode` module. The existing project/legal
engineering review at `538a4aa` remains unchanged; no package-publication or
license conclusion is added.

## Runner, fixtures, resources, and inherited evidence

| Check | Exact result |
| --- | --- |
| fixture generator write followed by `--check` | both exit 0; no byte drift |
| corrected runner binding `--check` | exit 0; exact inventory and digests |
| corrected focused implementation plus verifier | 190 passed |
| exact 64-GiB `RLIMIT_AS` set/readback | `(68719476736, 68719476736)` |
| Cycle 2 `c2-b1.json` through `c2-b6.json` validation | six exit-0 results |
| accepted Cycle 1 manifest SHA-256 values | five exact matches |
| Cycle 1/2 evidence and completion preservation | quiet diff against `7fe1f5c` |
| corrected candidate path equality | quiet diff against `48d139f` |
| accepted fixture/snapshot path equality | quiet diff against `7c57a34` |
| installed/prohibited import and active-source scan | zero exposed modules/files and zero prohibited use |
| final process and inventory audit | no worker/decoder/pytest/Vite/Playwright; exact cache-free tool inventory |
| final repository diff/status | diff check passed; clean before this record |

Corrected candidate SHA-256 values are binding
`1d36da4a8e06707c5fad8830c7037fd5aa601fdc8854dc4f33b9aec4b2d992eb`,
launch `3df74d88a1f013a7aa9f09c81d76a653159de09e9b42270137fb0f3956efbf27`,
runner `2f0d32ec2d2fea047cb5f78e6b3d32753e6d69d3f9d0f398bd589691011ef942`,
worker `76124299334fc4fb5a7ea5d28750afff9b19f59b4fda0618dd0be215f59f890c`,
probes `dc0d5ba2e5c1ec1f3e805f9a41a92b29e5edce8a4bb6172ef6fc82dbf8848b2a`,
method `8ef7bdac50554fb42ec97d3c5d685d3f6b55074c82478c750e4e62ff3d318325`,
and implementation test
`74e5c8d823f1f58ffc84e57bbae7264ee80c67586dec1e3e816e8ccce8f341c1`.

Accepted Cycle 1 manifest identities remain:

| Manifest | SHA-256 |
| --- | --- |
| `c1-b1.json` | `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc` |
| `c1-b2.json` | `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af` |
| `c1-b3.json` | `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598` |
| `c1-b4.json` | `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead` |
| `c1-b5.json` | `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d` |

## Exact Node 22 browser and performance regression

The exact Node identity is v22.14.0. `web/package-lock.json` SHA-256 is
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`web/production-assets.json` SHA-256 is
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

| Command class | Exact result |
| --- | --- |
| exact Node 22 `npm ci --no-audit --no-fund` | exit 0; 215 packages |
| exact Node 22 ESLint and TypeScript | both exit 0 |
| exact Node 22 Vitest | exit 0; three files, five tests |
| exact Node 22 Vite build and asset checker | exit 0; 29 modules; no drift |
| exact Node 22 browser regressions | exit 0; one plus three tests |
| exact Node 22 B6 offline performance spec | exit 0; one test |
| clean Python accepted-threshold checker | exit 0 |

The first sandboxed browser command could not start its local test server and
is invalidated. The exact command was rerun through the saved Node-22 browser
capability and all four tests passed. The performance report SHA-256 is
`9feb7d3e1dbe21235dc096ed34c0dfbf4a64293adbff359f69000f33c9c3282f`;
generated test results were moved intact to
`/private/tmp/cycle3-runner2-web-20260827T0535` before final scope inspection.

## Scope, approvals, and disposition

- Candidate-owned paths remain byte-identical to `48d139f`; accepted fixture,
  snapshot, Cycle 1/2, product, lock, workflow, governing, and excluded-scope
  bytes are unchanged.
- This accumulated gate ran only static checks, fixture rebuilding,
  inert/hostile non-decoder probes, inherited product regressions, and local
  browser regressions. It did not call the private snapshot route or
  `execute_snapshot`, and ran no decoder, compatibility helper, C#/.NET/
  pythonnet/libsigrokdecode/sigrok runtime, hardware, USB/serial action,
  publication, raw retry, excluded action, or Cycle 4 work.
- Root saved one reusable clean-Python pytest loopback prefix and one reusable
  exact-Node-22 browser prefix after their sandboxed forms exposed the expected
  local-loopback restriction. Hash-locked installation and performance used
  the previously saved stable classes. No package-by-package, credential,
  device, or subagent escalation occurred.
- Findings: none. Approval needed: none. The exact unchanged corrected
  candidate is ready only for fresh runner acceptance round 2.

`pass`
