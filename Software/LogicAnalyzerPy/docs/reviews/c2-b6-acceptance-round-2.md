# C2-B6 independent acceptance — round 2

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-3`
- Product candidate: `2d5484a73d881496cdf5a35c799dfb01eedad229`
- Product tree: `8c76bce79922263468cb6ceaa4f1990703a84bfc`
- Implementation record commit: `a349cc5`
- Implementation record SHA-256:
  `655c56b770e35e2bb4b4dbb6a78116b5e7842b714cf29c2e5f61d7dca3a379af`
- Verification record commit: `436e187`
- Verification record SHA-256:
  `9907b1f50de115f37a7181b1bf0a43ce8108a4633e027222d192315bd7b01926`
- Reviewed at: `2026-08-23T22:49:28Z`
- Prior-result transfer: none; retained evidence was independently checked for
  applicability to the exact candidate
- Verdict: `pass`

## Audit boundary and candidate identity

Acceptance independently reassessed the complete macOS-only B6 contract, all
B6 implementation, verification and acceptance history, the accepted C2-B1
through C2-B5 checkpoints, the approved B5 ceilings, the exact round-4 delta,
physical 8/16/24 and recovery evidence, installed native-browser evidence,
performance enforcement, security/confidentiality controls, accumulated gates,
and exact-candidate hosted macOS CI. There is no Linux requirement or claim.

The assigned commit exists and resolves exactly to tree
`8c76bce79922263468cb6ceaa4f1990703a84bfc`. The round-4 implementation and
independent verification records match the assigned commits and SHA-256 values.
The candidate delta is confined to the macOS workflow, immutable review records,
workflow and artifact-availability tests, and the physical-artifact verifier's
explicit availability classification. It does not change the runtime, driver,
API, frontend, benchmark producer/checker, native harness, firmware or physical
evidence. The worktree was clean before this record.

## Findings and dispositions

1. `C2B6-A001` — **closed**. Exact-candidate hosted CI is green. Dedicated
   branch `cycle2-b6-ci-candidate-r6`, push event run `32671356406`, job
   `97272584254`, used head SHA
   `2d5484a73d881496cdf5a35c799dfb01eedad229` and the assigned tree. The run and
   sole `macos-latest` job completed `success`. Every substantive step passed:
   clean environment setup; hash-locked Python and Node installation; both
   dependency checks; Ruff; strict mypy; the complete non-hardware pytest gate;
   CLI; web runtime; frontend lint, type, unit, build and asset checks; frozen
   Chromium installation; and browser validation.
2. `C2B6-A001-AVAILABILITY` — **closed**. A completely absent default set of
   seven machine-local physical artifacts is classified as unavailable and
   skips the four physical black-box tests on a clean hosted worker. Partial
   default sets, explicit missing inputs and corrupt complete sets fail. A
   complete set executes all original physical assertions without weakening
   their digests or semantics. Acceptance's complete local evidence set ran the
   focused workflow/availability/physical suite: 8 passed.
3. `C2B6-A001-DIAGNOSTICS` — **closed**. The bounded sanitizer preserves the
   useful pytest failure tail and exit status while its hostile self-test rejects
   raw capability values, serial/device paths and user-home paths. It does not
   publish artifacts or access repository secrets.
4. `C2B6-V001` — **closed**. The approved B5 performance ceilings remain bound
   to the governed method and candidate identity, including maximum observed
   request span `100000` against approved ceiling `100000`. The round-4 delta
   does not alter the benchmark producer, checker, browser runtime or threshold
   governance, and no hidden threshold rebase occurred.
5. `C2B6-V002` — **closed**. The strengthened installed native production
   workflow still validates real D0/D8/D16/D23 display at 8/16/24 widths,
   trigger/cursor values, LSB-first bus order, transition/strobe rows, exact CSV,
   reopen/reidentify, second capture, nondisclosure and shutdown. Its latest
   exact applicable run passed 1/1 without persistent device change.
6. `C2B6-V003` — **closed**. The immutable physical evidence remains bound to
   `uint8`/`uint16`/`uint32`, masks `0x01`/`0x0101`/`0x810101`, exact zero/mask
   projections, 31 rising edges per driven channel, zero bits 24-31 and ordered
   CSV/NPZ equivalence. Recovery retains accepted `ff` cancellation, 6,144
   samples, 42 transitions, 1011.5963483839131 Hz, reidentification and no
   persistent change. The candidate's complete seven-artifact set reproduced
   every frozen digest and all original assertions.

Open findings: none. Deferred findings: none.

## Fresh acceptance results and evidence integrity

- `pip check`, Ruff and strict mypy over 21 source files passed.
- Focused workflow, availability and complete physical-artifact validation
  reported 8 passed.
- The complete non-hardware Python suite reported 383 passed, 2 documented
  sandbox-loopback skips and 106 warnings. The skips were only the two tests
  that require opening a local listener in the restricted acceptance sandbox;
  the exact hosted run exercised and passed the accumulated workflow.
- The C2-B3 physical-evidence validator and `git diff --check` passed.
- Workflow SHA-256 is
  `ab0809523370ecfe308fe733be011c83f926315eeca12e7a0d3ab294b357ea22`;
  workflow-invariant test SHA-256 is
  `434d7869c8ee94207afb79fc0dd7e44c0a0390eb005d790f4f8289443facf241`;
  guarded physical verifier SHA-256 is
  `94d794349fff256862c82e513e0e0e7d736fed46eafaf2aad2d1b65ea36f83ac`;
  and availability-test SHA-256 is
  `852bfe65f98bfe00e3a8fb2e16aacf8dcdee27aea0cbb1f50ab96c7d73d536b2`.
- Sanitized C2-B3 evidence SHA-256 is
  `9db03e36f5fe2ffb2ed4f7fa297446ced4c7e9a77e4c71fd7eb5fa871a789ad5`;
  its validator SHA-256 is
  `d2bbddeaedbf11ad31c25123dfa553ebc2f44b88b21bb1becfae12743427037f`.
- Python lock SHA-256 is
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
  Node lock SHA-256 is
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
  B6 asset manifest SHA-256 is
  `c27b08c3fbbce7ead5e7afa4b92bffdaf9623f46f4319d92c78942ab2e59059d`;
  B6 OpenAPI SHA-256 is
  `3d1a4717ca6f174c3f9394316492319601b9175b7a3e0ac09dea5c622eea2e88`;
  and generated B6 TypeScript SHA-256 is
  `2f01d137876ebea792dbb868b37eb7044f172ee3fb395fb8cc42cca6d63179f6`.

The workflow has exactly one `macos-latest` job, top-level `contents: read`, no
write permission, no secret expression, no privileged pull-request target, no
device/serial access and no externally published diagnostic artifact. Push and
pull-request path filters remain bounded, and manual dispatch has no inputs.
The production remains offline: no CDN or production Node dependency, no public
listener authorization and no raw capability, port, serial, location, firmware
identity, token or user-home path in durable evidence.

## Verdict, scope, and Git handoff

Verdict is `pass`. All B6 acceptance clauses are satisfied for candidate
`2d5484a73d881496cdf5a35c799dfb01eedad229`; `C2B6-A001` and its availability
and diagnostic subfindings are closed; `C2B6-V001`, `C2B6-V002` and
`C2B6-V003` remain closed. No open or deferred finding remains.

No firmware, bootloader, Wi-Fi, wiring, persistent-device, public-server,
packaging/publication, C#/.NET, `.lac`, threshold rebase, Linux support,
completion record or Cycle 3 action occurred. This acceptance changed no
product or prior evidence.

Exact Git handoff: stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b6-acceptance-round-2.md`; record its
SHA-256 in the immutable handoff. After that acceptance-record commit, the root
orchestrator may create the B6 evidence manifest and checkpoint using the exact
candidate and audited evidence. This record does not itself create the manifest
or checkpoint, declare Cycle 2 complete or authorize Cycle 3.
