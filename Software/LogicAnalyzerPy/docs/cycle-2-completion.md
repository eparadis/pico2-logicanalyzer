# Cycle 2 completion proof

- Final independent acceptance identity: `cycle2-acceptance-replacement-3`
- Final product candidate: `2d5484a73d881496cdf5a35c799dfb01eedad229`
- Final product tree: `8c76bce79922263468cb6ceaa4f1990703a84bfc`
- B6 checkpoint commit: `7fe1f5c`
- Audited support claim: macOS only
- Final acceptance verdict: `pass`
- Open findings: none
- Deferred findings: none

This final audit applied the fourteen conditions in `CYCLE2_ORCHESTRATION.md`
individually and rejected indirect evidence, historical passes for superseded
candidates, and required-path skips. All final accumulated, physical,
performance, native-browser, security and hosted-CI proof resolves to the one
final product candidate and tree above. Later immutable implementation,
verification, acceptance, manifest and checkpoint commits record that candidate
without changing its product tree.

## Fourteen-condition proof

1. **Clean Python and Cycle 1 regression — pass.** Clean Python 3.12.13,
   hash-locked development and web environments, `pip check`, Ruff, strict mypy
   over 21 source files, source-installed CLI help and the full non-hardware
   suite passed. The final local result was 383 passed, 2 restricted-sandbox
   loopback skips and 106 warnings. Those skips are not accepted as omitted
   requirements: the root-brokered real-loopback API passed 1/1, native
   production workflow passed 1/1, and the exact hosted suite passed the same
   listener/browser path.
2. **Clean locked frontend and offline production — pass.** Node 22.14.0,
   `npm ci`, ESLint, TypeScript, five Vitest tests, the 29-module Vite production
   build, deterministic asset check, frozen Chromium 133.0.6943.16 and
   Playwright 1.50.1 passed. Production uses checked-in local assets; it neither
   invokes Node nor contacts a CDN at runtime.
3. **Exact-candidate hosted macOS CI — pass.** Push run `32671356406`, job
   `97272584254`, branch `cycle2-b6-ci-candidate-r6`, ran head SHA
   `2d5484a73d881496cdf5a35c799dfb01eedad229`, tree
   `8c76bce79922263468cb6ceaa4f1990703a84bfc`, and completed `success` on the
   sole `macos-latest` job. Clean setup, locked installs, dependency checks,
   Ruff, mypy, complete non-hardware pytest, CLI, frontend lint/type/unit/build/
   assets, Chromium and production browser validation all passed.
4. **Literal 8/16/24 V2 protocol fixtures — pass.** The B2 manifest and final
   B6 verification bind literal request/response fixtures for ordered subsets,
   packed positions, little-endian `uint8`/`uint16`/`uint32` words, reserved-byte
   escaping and the required zero upper byte for 24-channel words. The later
   physical proof independently reproduced all three widths.
5. **Adverse lifecycle and local-web security — pass.** Fake, replay, API and
   browser suites cover fragmentation, malformed/hostile inputs, pre-allocation
   bounds, finite timeouts, cancel, disconnect/reconnect, single-operation
   conflicts and cleanup. Negative tests prove loopback Host, canonical Origin,
   capability-cookie, file-transfer, redaction and nondisclosure boundaries.
   The final live API root pass and hosted run cover the two locally skipped
   listener cases.
6. **Replay and CSV determinism — pass.** Schema 1 remains readable; canonical
   schema 2 and generalized self-timed CSV round-trip deterministically with
   ordered metadata, mode-appropriate samples and explicit import metadata.
   Bounds apply before materialization. No pickle, executable metadata or
   machine-local value is used.
7. **Parallel-bus determinism — pass.** Independent transition and distinct-
   strobe fixtures prove LSB-first order, sample/time semantics, selected-edge
   behavior, value formatting, interval fields and deterministic CSV. B4's
   closed OpenAPI/type fingerprint tests preserve the shared CLI/API/browser
   authority.
8. **Physical byte-boundary captures — pass.** The operator-confirmed protected
   3.3 V approximately 1 kHz source was connected simultaneously to board pins
   1/9/17/24, mapped D0/D8/D16/D23, with 3.3 V VRef and common ground. Fresh
   D0-D7, D0-D15 and D0-D23 captures each contained 6,144 samples and proved
   `uint8`/`uint16`/`uint32`, driven masks `0x01`/`0x0101`/`0x810101`, both
   driven states, 31 rises per driven channel, approximate 1 kHz activity and
   zero bits 24-31. Seven sanitized CSV/NPZ/recovery artifacts matched frozen
   digests and independent byte reconstruction.
9. **Identity and recovery continuity — pass.** Sanitized identity is
   `LOGIC_ANALYZER_PICO_2_V6_0` on the operator-confirmed Pico 2 running the
   checked-in fixed V2 firmware. Fixed-low D1 recovery accepted one bounded
   `0xFF` cancellation, then drain/close/reopen/re-identify and a second capture
   without power cycle or persistent device change. Recovery recorded 6,144
   samples, 42 transitions and 1011.5963483839131 Hz.
10. **Offline viewer workflow — pass.** Production-browser proof covers
    schema-1/schema-2 replay and self-timed CSV; 8/16/24 labels and visibility;
    pan; cursor-centered zoom; trigger marker; cursor sample/time/value;
    transition and distinct-strobe tables; pagination/export; explicit error,
    cancel, reconnect and clean-shutdown states.
11. **Native macOS acceptance — pass.** The installed-browser production
    workflow passed 1/1: local server start, real Pico identify, 8/16/24 capture
    and display, exact D0/D8/D16/D23 values, trigger/cursor values, LSB-first bus
    order, transition rows, 31 distinct-rising-strobe rows, validated exported
    CSV bytes, close/reopen/reidentify, second capture, nondisclosure and clean
    shutdown. The test took 13.4 seconds (14.5-second suite) and made no
    persistent device change.
12. **Approved performance — pass.** The operator-approved record freezes
    method `c2-b5-playwright-production-v2`, viewport 1280x900 at DPR 1, three
    warmups, 16 load observations, 30 interaction observations, two bus
    iterations per mode/role, and unrounded nearest-rank p95. Approved
    regression ceilings are 772.10 ms load, 580.30 ms interaction,
    261.45/116.73 ms representative transition/strobe and 710.15/263.20 ms
    worst transition/strobe, each also bounded by its absolute ceiling. Final
    p95 values were 445.60, 335.20, 156.50, 63.90, 402.20 and 149.50 ms.
    Maximum observations were 12,755 Canvas commands, 221 DOM nodes, 100 bus
    rows and exactly 100,000 request samples at 960 pixels; all passed approved
    ceilings of 46,129, fewer than 1,000, 100 and 100,000 respectively. The
    automatic benchmark chained the governed checker and no threshold was
    rebased.
13. **Complete identity and handoff — pass.** This record and the six strict
    manifests identify final commit/tree, environments, locks, commands,
    results, CI run/job, sanitized physical/native proof, accepted thresholds,
    limitations, deferrals and repository state. All six manifests validate
    against the strict Cycle 2 schema.
14. **Rollback paths and prohibited actions — pass.** Checked-in
    `Firmware/LogicAnalyzer_V2/`, `Software/LogicAnalyzer/`, Cycle 1 manifests
    and fixtures, and the accepted Python CLI remain tracked. Cycle 2 did not
    edit/build/flash firmware, enter the bootloader, install or run .NET, alter
    Wi-Fi/wiring/persistent device state, implement `.lac`, bind a public
    server, package/publish a release, claim non-macOS support or begin Cycle 3.

## Canonical commands and final results

The canonical Python gate was a clean Python 3.12 environment followed by the
hash-locked `requirements-dev.lock` install, no-build-isolation/no-deps source
install, `pip check`, `ruff check .`, `mypy src`,
`pytest -m "not hardware"`, and `python -m pico_logic_analyzer --help`: exit 0,
383 passed, 2 explicitly covered loopback skips. The clean web-runtime variant
used `requirements-web.lock`, `.[web]`, and `pip check`: exit 0.

The canonical frontend gate was `npm ci`, `npm run lint`,
`npm run typecheck`, `npm test -- --run`, `npm run build`, deterministic asset
validation and `npm run test:browser`: exit 0. Root-brokered real-loopback API,
production-shell and native installed-browser gates each passed 1/1. The native
command was the bounded C2-B6 procedure with a runtime-supplied explicit port;
no raw port or capability entered durable output.

The physical command sequence was source-installed `pico-la info`, bounded
recovery smoke, and ordered captures for D0-D7, D0-D15 and D0-D23 using
`<PORT_SUPPLIED>`, finite timeouts and explicit artifact paths. All exited 0;
the verifier's focused physical/recovery suite passed 14, and final guarded
workflow/availability/complete-artifact validation passed 8.

The final performance command was `npm run benchmark:b6`, which produced the
bound report and automatically invoked the approved-threshold checker: exit 0,
Playwright 1/1 and checker pass. The exact hosted workflow result is run
`32671356406`, job `97272584254`, success. Final schema audit ran
`scripts/validate_cycle2_evidence.py` against each `c2-b1.json` through
`c2-b6.json`; all six exited 0.

## Dependency, build, and performance identities

- `requirements-dev.lock` SHA-256:
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
- `requirements-web.lock` SHA-256:
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
- `web/package-lock.json` SHA-256:
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
- governed B6 production-asset identity:
  `c27b08c3fbbce7ead5e7afa4b92bffdaf9623f46f4319d92c78942ab2e59059d`
- checked-in `web/production-assets.json` file SHA-256:
  `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`
- B5 baseline SHA-256:
  `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`
- B6 threshold-enforcement report SHA-256:
  `09b5d5238b35d55d6122e13a69ec9e6608a75c863cac7b6302e5416ddbf8c555`
- approved threshold record SHA-256:
  `57183190d5d48642e9621862aeed343b0a435477a5b4b6276551e55dd01a6053`

## Checkpoints, manifests, and accepted reviews

The immutable checkpoint commits are C2-B1 `873c4f6`, corrected C2-B2
`f586277`, C2-B3 `1fe22ff`, C2-B4 `eb693ed`, C2-B5 `abc85a0`, and C2-B6
`7fe1f5c`. They are recorded in
`Software/LogicAnalyzerPy/docs/cycle-2-orchestration-progress.md`, whose
pre-completion SHA-256 is
`958544bca8a3c35cd79ff3c59fa295be846d8fc9107e087c45037d2de84e8ef5`.

The active manifests, their commits and SHA-256 values are:

- C2-B1: `testdata/evidence/c2-b1.json`, commit `4bb2561`,
  `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0`.
- C2-B2 corrected: `testdata/evidence/c2-b2.json`, commit `5f5eebb`,
  `d930bce4ae20576ea030e35cf0e993a3caf89e95f5eb5195638471c1790c2be4`.
- C2-B3: `testdata/evidence/c2-b3.json`, commit `4635bf4`,
  `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`.
- C2-B4: `testdata/evidence/c2-b4.json`, commit `ef74970`,
  `4876b781f4569ae1599b6c5df4d824fbd54223c736c87c96746e6bb821806fd0`.
- C2-B5: `testdata/evidence/c2-b5.json`, commit `f561d31`,
  `8fcdf9714e2ad94af845d9676227bf6750159075bb49416d9c78c16d5b3c14e9`.
- C2-B6: `testdata/evidence/c2-b6.json`, commit `354c299`,
  `ed8036ef48654efd98a5c3a852fb1f1dba847a34e12bf1c5dec253a2b9a83ffb`.

Accepted current review/evidence records are:

- B1: `docs/reviews/c2-b1-verification-round-18.md`
  `28b3c6e8349982e3faec8517572cedc42e7086da12a3c3c5f6858d8149f08feb`;
  `docs/reviews/c2-b1-acceptance-round-3.md`
  `c79618342a5c18b246c01e530fa35e67fc77afc11fabb9296349d06490dee957`;
  platform verification/acceptance
  `e4c94cfac3810300aa7c813f564d57a7af4e5225bcc4349f417038b2e501ea00` /
  `ae07e21b9038b0ad58a59b68801878a083710b6df1929ce672f8ab20833e5925`.
- Corrected B2: `docs/reviews/c2-b2-verification-round-4.md`
  `56f5a99c0d34464ae09081145ef2b9d1378e6b6c792276152515cb3dc47e443a`;
  `docs/reviews/c2-b2-acceptance-round-2.md`
  `9930b43a96adcbebfa4670f3c01507c5c5bc89e2bf7640a953fdb9a0f1fa2d3e`.
- B3: implementation/verification/acceptance
  `docs/reviews/c2-b3-implementation-round-1.md`
  `2549b62755eec859bf34954d1f8a612e8be77bdba6e12fc88a6a5d4dd2dff27e`,
  `docs/reviews/c2-b3-verification-round-1.md`
  `ebeee036728cada9a9046fdcdee4e4a356955a5e3a1a3f10d075ba66ff4fad78`,
  and `docs/reviews/c2-b3-acceptance-round-1.md`
  `5e2eba90c93b610220fb77105bbed968374a5a375739e85142b45d385a508985`.
- B4: implementation/verification/acceptance
  `docs/reviews/c2-b4-implementation-round-7.md`
  `ff283b698a10c8bcda747b8fa8567b69e2af22d5d3f807ae2f6f1b05057cad2e`,
  `docs/reviews/c2-b4-verification-round-7.md`
  `59fb4849d5a0f415dd183892911a484c91dfde49483f956a29944f2e74f0653e`,
  and `docs/reviews/c2-b4-acceptance-round-1.md`
  `ef31d583d6df874ceb8a92fe8e54246e903d1265a93ef28a00a45cbbc4f0a906`.
- B5: implementation/verification/acceptance
  `docs/reviews/c2-b5-implementation-round-2.md`
  `84549590c2d2b5ebdc0e59fb7e53fbdacef730473d1a2db5e973f90676434c33`,
  `docs/reviews/c2-b5-verification-round-2.md`
  `ebcf3d9aac7dd1e9b3817f6567ab997cc90cf537f11cb4f5b3344a7949fc0541`,
  and `docs/reviews/c2-b5-acceptance-round-1.md`
  `32252c54a2cd3e0e88370009316a2557659d0132fca7c4c0f66842aa9954771a`.
  Threshold proposal/verification/acceptance/approval digests are respectively
  `d314eea0979b567086eed7b346162eef76865507f9d8a111c736c94f62bbc597`,
  `7e77999b30650ab19f3b623def7f11b4e1c72b666e1c6f5791b984881eb79b71`,
  `c8f0211ec189a0e5bc5c62bf610f3b40c62e95d08b8109b657ba2be86536f5e6`
  and `57183190d5d48642e9621862aeed343b0a435477a5b4b6276551e55dd01a6053`.
- B6: `docs/reviews/c2-b6-implementation-round-4.md`, commit `a349cc5`,
  `655c56b770e35e2bb4b4dbb6a78116b5e7842b714cf29c2e5f61d7dca3a379af`;
  `docs/reviews/c2-b6-verification-round-4.md`, commit `436e187`,
  `9907b1f50de115f37a7181b1bf0a43ce8108a4633e027222d192315bd7b01926`;
  and `docs/reviews/c2-b6-acceptance-round-2.md`, commit `6054004`,
  `7a6abbf69f48bd0e720f446b2713be581a893376f9724c4fbc9a7a68dd934216`.

Earlier failed/superseded rounds remain immutable historical records and do not
stand in for the accepted records above.

## Sanitization, limitations, deferrals, and repository status

Durable hardware identity is limited to the Pico 2/V2 product identity and
approved electrical facts. The serial port is `<PORT_SUPPLIED>`; launch and
cookie capabilities are `<TOKEN_REDACTED>` or absent. No serial number,
machine-local location/URL, credential, user filename or home path is retained.
The sole hosted workflow is read-only (`contents: read`), has no secret
expression, no write permission, no privileged pull-request target, and no
device access.

Known limitations are: macOS is the only supported and accepted Cycle 2
platform; reliable browser heap measurement is unavailable, so no heap limit is
claimed; machine-local physical artifacts are intentionally not committed, and
a complete supplied set is required to rerun their offline assertions. Total
default absence is reported as unavailable, while partial, explicitly missing
or corrupt sets fail. There is no deferred Cycle 2 work or deferred finding.
Features outside this cycle remain outside scope rather than completion debt.

Repository status immediately before this record was clean at checkpoint
`7fe1f5c`. Creation of this completion proof adds only
`Software/LogicAnalyzerPy/docs/cycle-2-completion.md`; there are no uncommitted
product, test, lock, workflow or built-asset changes. Firmware, C#/.NET,
persistent device state, public serving, packaging, publishing and Cycle 3 were
untouched.

## Final verdict and handoff

Final independent acceptance verdict: `pass`. Conditions 1–14 are all proven
against final candidate `2d5484a73d881496cdf5a35c799dfb01eedad229`, tree
`8c76bce79922263468cb6ceaa4f1990703a84bfc`. No open, missing or deferred
condition remains.

Exact Git handoff: stage and commit only
`Software/LogicAnalyzerPy/docs/cycle-2-completion.md`; record its SHA-256 in the
completion handoff. Do not modify the final product candidate or any immutable
contract/history, and do not begin Cycle 3.
