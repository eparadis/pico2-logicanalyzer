# C3-B3 combined accumulated validation — round 1

## Subject, environment, and verdict

- Validator: `c3-b3-accumulated-validator-1` (`/root/c3_b3_accum_r1`).
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Accepted B2 checkpoint prerequisite: `18614cc812edda68598e19d200f7bb4c87861ebd`.
- Exact accumulated candidate commit/tree:
  `0e1f619c8c744c16a96119c0834ed2f7d2518d0e` /
  `d22ecdd374446cef9e4b1e941b0937ae6389a1cb`.
- Environment: macOS 15.7.9 build 24G830, x86_64, CPython 3.12.13.
- Verdict: **pass**. All executable, static, identity, scope, process-cleanup,
  and cleanup-path checks passed; no candidate or product finding was observed.

This is combined accumulated validation, not independent acceptance. It creates
no B3 manifest, predicts no manifest-verification result, and makes no acceptance
or checkpoint claim. Those steps remain explicitly deferred in contractual order.

## Immutable history and identity audit

The candidate is an ordered descendant of the accepted B2 checkpoint. The B3
history is exactly: preflight/baseline, UART implementation and verification,
SPI implementation and verification, I2C implementation and verification, then
R16 implementation and verification. The four candidate identities and four
fresh verifier identities are distinct and auditable:

| Item | Candidate commit/tree | Test SHA-256 | Review SHA-256 |
| --- | --- | --- | --- |
| R13 UART implementation | `e5ac88ef7425bfab75a7901d1ca6552cc587fec0` / `b6fc418cb6ed907d78a03061b47c63da7a390a8d` | `6ebad5ba914a41904fc6965dbc592e201e0d1bee8211efb030e2bd18a6d5bd16` | `bf7ffcd8e147139a7f02436f324858408e414937dac0a0140ee33432debbe56c` |
| R13 UART verification | descendant `25d4849459ff238a28a41a4d72156b64f5fc8251` | `da85f425e93107002e9eefd18e614355a7a374d94c4e372042520346fa4ca187` | `045f8fac0da2eb6f2737158e50d4b1f12b2dbfee0499d3efa570eec87f0e9f8f` |
| R14 SPI implementation | `3e6124ab68d1bcea7df628c520741add93658350` / `c4d88ada4bc6c0869b53b5f19f7c325c27697112` | `e35c8d2ac472a7ae4c557daaba54521696971f871ef158d794c3d754cfdc0250` | `5590414dee3de853d441f3413bcbc23ce33da4e7b05b923a945a6d0d2f2e58b7` |
| R14 SPI verification | descendant `db825eff3ab4ca0e30f5ed0197dcad6bc93cda88` | `9bbcbcc70db1d53a23375d44c353875c198d59a7e20f456be52d5ee28918a118` | `c0a6284e7212e02ba3f478835c4b41fe26d3b5108812ee68a3067aa5a836cd0d` |
| R15 I2C implementation | `844d69d22d2f82ae78f423762861abf3b18def66` / `513c4c4bc2a8d053bfc7e6229390207bc265b60e` | `20c04a6f1eeb77760fe16b522ccaf1b1def8b8ca5a3418b29b3af6471bd433c3` | `1cf39a040e6c9a0a85f9406cc3088031729d36c272ef22903879012f03688f41` |
| R15 I2C verification | descendant `30b020a3f8cc14ce65b42c8764dcaff9900dcd45` | `997e50b97edaff76f40bb48f2002cff836537ce780dac1445a379986b8bfd6ef` | `92e6d324111c033166fa8d9509ad9ef28de74b37d68d058bf3ed67a87eb2c8d2` |
| R16 implementation | `970f9a79169733d20bc06db60e2c736a8234b7eb` / `beffab143acd64eeb776c48f3138df17828a8079` | `90754fb7a3d32da70c1526bde29dcc359d2a9e17ac21ea0a97273650f5bd1159` | `f2c89da83d745d0269b0a7a9c077f2b759a89f64587a851051620762d0052358` |
| R16 verification | final candidate `0e1f619c8c744c16a96119c0834ed2f7d2518d0e` / `d22ecdd374446cef9e4b1e941b0937ae6389a1cb` | `1cd77c44b14bff2e23ec0451a9f9184fad167001f229aac8e913e8494cc6740c` | `a69262dfe5c5658c81a6d806e94c177451ce18985e2dc63adb758467de53ad37` |

The B2-checkpoint-to-candidate diff contains only eight new B3 tests, eight
new B3 implementation/verification reviews, and the root-owned orchestration
progress update. It contains no decoder snapshot, product/API/CLI, fixture,
dependency/lock, workflow, browser/frontend, hardware, firmware, serial, live
capture, contract, manifest, or checkpoint change.

Correction history is preserved rather than erased: UART defaults were moved
from production to the accepted matrix; SPI's no-CS probe was made distinct;
the SPI verifier corrected its incomplete-CS expectation; I2C corrected packed
channel order and its verifier separated declared read surfaces from emitted
write records; R16 corrected an inert device identity, added the missing packed
sample hostile control, refreshed its command record, and corrected verifier
Ruff grouping. None was a product defect, and every correction preceded the
relevant immutable pass.

## Accepted inputs and coverage accounting

Recomputed accepted hashes are:

- semantic corpus: `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`;
- option matrix: `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`;
- accepted B1 fixture manifest: `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`;
- accepted C3-B1 evidence: `3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`;
- accepted C3-B2 evidence: `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`.

The accepted corpus contains exactly 63 timelines: 54 UART, six SPI, and three
I2C. R13-R15 execute all 63, complete typed declarations/records and canonical
bytes, mappings, malformed/incomplete and boundary cases, and repeatability.
Their defaults and expected results are fixture/matrix sourced; candidate and
verifier hostile checks close production-default and decoder-as-oracle routes.

The accepted matrix actually contains **165 unique rows**, not 215: UART 127
(50 direct, 77 unsupported), SPI 30 (10 direct, 20 unsupported), and I2C eight
(two direct, six unsupported). All 165 are covered. The assignment's phrase
“215 option rows” is inconsistent with the governing accepted B1 artifact and
its prior acceptance records; 215 is the historical locked npm package count.
This is recorded as an instruction-count discrepancy, not a candidate defect,
and no synthetic or duplicated option rows were invented.

R16 independently covers six integration-only mapping classes: UART RX, UART
TX, SPI MOSI, SPI MISO, SPI data with CS, and I2C SCL/SDA. Each crosses direct
memory, hand-built schema 1, independently built schema 2, and explicit-metadata
CSV, for 24 private decodes, with exact capture identity and byte-identical
canonical results. Serial/live capture is fail-fast trapped. The remaining 57
timelines retain authoritative R13-R15 ownership; R16 does not transfer or
sample their semantic claims. Schema 1's D0-D7 constraint is handled by the
reviewed UART TX D9-to-D4 semantic wire remap across all four source forms.

## Fresh commands and results

Every shell command used the mandatory `rtk` prefix. Commands ran from
`Software/LogicAnalyzerPy` unless repository scope was needed.

| Command class | Result |
| --- | --- |
| all eight B3 implementation/verifier modules | `421 passed in 59.43s` |
| capture artifacts, black-box artifacts, wider formats, one B2 private-host implementation module plus four B2 verifier generations (five B2 modules total) | `380 passed in 40.29s` |
| complete applicable `pytest -m 'not hardware'` with the accepted 15 superseded-B1 ignores and one frozen historical deselection | `1359 passed, 4 skipped, 1 deselected, 149 warnings in 222.47s` |
| `.venv/bin/python -m pip check` | exit 0; no broken requirements (only an inert unwritable-cache warning) |
| `.venv/bin/python -m ruff check .` | exit 0 |
| `.venv/bin/python -m mypy src` | exit 0; 30 source files |
| `.venv/bin/python -m mypy --strict tools/cycle3_characterize` | exit 0; seven source files |
| fixture generator `--check` and characterization binding `--check` with bytecode disabled | both exit 0; no drift |
| installed `.venv/bin/pico-la --help` | exit 0; unchanged pre-B4 command surface and no decode command |
| Cycle 2 evidence validator over `c2-b1.json` through `c2-b6.json` | six exit-0 validations |
| Cycle 3 evidence validator over accepted `c3-b1.json` and `c3-b2.json` | two exit-0 validations |
| active-path prohibited-runtime scan | zero matches in `src`, `tools`, project/lock inputs |
| installed-module discovery | `pythonnet`, `clr`, `sigrokdecode`, and `libsigrokdecode` all absent |
| root-brokered current process audit using the already approved stable `rtk proxy pgrep -fl PATTERN` class | eight separate patterns returned exit 1 and empty output; no matching process |
| `git diff --check` and pre-review worktree status | clean |

The four skips are exactly the optional C2-B3 machine-local physical-artifact
reruns (three parameter rows at line 95 and one at line 136); mandatory sanitized
evidence remains exercised. No mandatory Cycle 3 test skipped. The single
deselection is the established superseded historical B1 fixture-surface
inventory assertion. The 149 warnings are inherited aiohttp state-key/
deprecation warnings plus one deliberate hostile duplicate replay member.

Dependency identities remained `requirements-dev.lock`
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
and `pyproject.toml`
`56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.
The already accepted repository-local environment was reused because its
Python/OS/architecture and lock identities remain exact; no network or package
mutation was required.

## Requirements, stopping conditions, and scope disposition

- R13-R15 / condition 9: pass. UART covers all 54 timelines and 127 rows; SPI all
  six timelines and 30 rows; I2C all three timelines and eight rows, including
  applicable annotation/Python/binary/meta output and sentinel/mapping cases.
- R16 / condition 10: pass. Four source representations are byte-equivalent
  for all six mapping classes without physical I/O.
- R21 / condition 13: pass for static dependency/import/lock/command/evidence
  and executable test coverage. No prohibited dependency or module resolved.
  Root separately queried `pico_logic_analyzer._decode.worker`, `pytest`, `vite`,
  `playwright`, `characteriz`, `dotnet`, `sigrok-cli`, and `libsigrokdecode` with
  the already approved stable `rtk proxy pgrep -fl` command; all eight returned
  exit 1 with empty output. An initial combined-pattern query briefly observed
  PID 98945, but an immediate approved `rtk ps -p 98945 -o
  pid=,etime=,stat=,command=` returned exit 1/empty because it had exited. The
  separate non-self-matching queries are the authoritative final inventory.
- R23 / condition 14: pass. Applicable Cycle 1/2 behavior, capture/replay/CSV/
  CLI regressions, all six Cycle 2 manifests, accepted B1/B2 manifests,
  rollback evidence, optional-web separation, and macOS-only claim remain intact.
- R24 / applicable condition-16 portion: pass. Candidate order, distinct roles,
  immutable findings/corrections, and deferred manifest/checkpoint ordering are
  auditable. The five-checkpoint final condition is not claimed at B3.
- R25 / condition 17 continuous audit: pass for B3. No browser/API/frontend
  decoder, hardware, firmware, serial/live capture, dynamic discovery, stacking,
  `.lac`, packaging/publication, unsupported-platform, lock, or workflow work occurred.

No external/reference decoder, C#/.NET, pythonnet, libsigrokdecode, sigrok-cli,
hardware, serial device, browser, hosted CI, package build/publication, or
unsupported-platform action was invoked or relied on. Existing product web and
CLI tests ran only as inherited Cycle 1/2 regression coverage.

## Findings and deferred authority

1. No candidate or product finding.
2. Count clarification: the immutable accepted option matrix has 165 rows; the
   requested 215 is not an accepted B1 fact. All real rows pass.
3. The sandbox denied this validator's broad RTK-prefixed process-table command.
   Root completed the same required cleanup audit through an already approved,
   narrower per-pattern process-query class; no approval was presented and no
   process remained. This is an execution-note disposition, not an open finding.

Independent acceptance, post-acceptance B3 manifest creation, independent
manifest verification, and the B3 checkpoint remain deferred. This validator
does not predict their verdicts or identities.

`pass`
