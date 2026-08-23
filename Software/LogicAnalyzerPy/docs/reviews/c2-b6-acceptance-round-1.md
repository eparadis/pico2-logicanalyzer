# C2-B6 independent acceptance — round 1

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-3`
- Implementation identity: `cycle2-b5-implementor-replacement-1`
- Verification identity: `cycle2-verifier-replacement-3`
- Product candidate: `758961069164a8700bc9a93a2709f78d86bc205d`
- Product tree: `2c016816dc64bf21d231cd0e5ea3770ac6a1d475`
- Implementation record commit: `5fcd20215729429cab1a1990fb226815b1510a67`
- Implementation record SHA-256:
  `dc869adea7bb23bc2f6723eff4659c4e8031cbcd6ff3dabe772e23cb01518e3b`
- Verification record commit: `e2ed5bc99e7263720264432ba2d987affbe1c719`
- Verification record SHA-256:
  `45bbee2984a0fb488431dd346d4c91f85cbe1ca47ca56300fc83ec796838881a`
- Reviewed at: `2026-08-23T22:22:19Z`
- Prior-result transfer: none
- Verdict: `changes_required`

## Audit boundary and candidate identity

Acceptance independently audited the macOS-only Cycle 2 goal and complete B6
contract; accepted C2-B1 through C2-B5 checkpoints and manifests; approved B5
performance thresholds; all three B6 implementation and verification rounds;
the exact candidate delta; corrected threshold enforcement; sanitized physical
and recovery evidence; installed native-browser evidence; security and
confidentiality invariants; accumulated local gates; and exact-candidate hosted
macOS CI.

The candidate exists and resolves to the assigned tree. Its round-3
implementation and independent verification records match the assigned commits
and SHA-256 values. Round-3 verification reports `pass`, closes
`C2B6-V001` through `C2B6-V003`, and has no open or deferred verifier finding.
The worktree was clean before this record.

## Closed product, physical, security, and performance evidence

1. `C2B6-V001`: closed locally and independently. Automatic B6 benchmark
   generation chains the governed checker, observes every waveform request,
   requires at least one observation, rejects a span above 100,000, and freezes
   both approved and observed maximum spans at exactly 100,000. Seven targeted
   mutations covering the earlier method, fixture, timing, role, product
   identity, approved-span and observed-span defects reject 7/7.
2. `C2B6-V002`: closed. The strengthened installed native test checks the real
   D0/D8/D16/D23 displayed values at 8/16/24 widths, trigger sample 1024,
   cursor sample/time/value, explicit LSB-first bus order, transition values,
   31 D23 distinct-rising-strobe rows, exact downloaded CSV contents,
   reopen/reidentify, second capture, nondisclosure and shutdown. A fresh
   acceptance-stage exact-candidate rerun passed 1/1 in 13.4 seconds, suite
   14.5 seconds, with no persistent-device change.
3. `C2B6-V003`: closed. Sanitized physical evidence binds the physically
   exercised live product commit/tree and independently inspected artifact
   digests. It records `uint8`/`uint16`/`uint32`, masks `0x01`/`0x0101`/
   `0x810101`, exact zero/mask projections, 31 rising edges per driven channel,
   zero bits 24-31, ordered CSV/NPZ equivalence, serial close/reopen,
   reidentification and second capture. Fixed-low D1 recovery records accepted
   `ff` cancellation, 6,144 samples, 42 transitions, 1011.5963483839131 Hz,
   reidentification and no persistent device change.

The sanitized implementation evidence SHA-256 is
`dfe1e7504e3289e21a556a423d1c5d417e3072bdf5be3156557e279567864a6a`.
It contains `<PORT_SUPPLIED>` and opaque `device-1`, but no raw port, serial,
location, firmware identity, capability, token or user-home path. Physical
artifact digests and recovery digest are retained in that immutable record.

The approved B5 thresholds were freshly enforced without rebasing. Root's
acceptance-stage automatic benchmark passed Playwright 1/1 and its chained
checker. Transient report SHA-256 was
`97ef971c0134b69817bf2091a266cf4421db054898043a3eb0d00fe96ad70a07`.
Fresh p95 values were load `445.5999999977648`, interaction
`335.20000000298023`, representative transition `156.5`, representative
distinct strobe `63.899999998509884`, worst transition
`402.20000000298023`, and worst distinct strobe `149.5` milliseconds; all
satisfied both approved regression and absolute ceilings. Maximum observed
request span was 100,000, Canvas commands 12,755, DOM nodes 221, and bus rows
100. Method/product identities and all nondisclosure flags passed. The report
and browser residue were removed.

Durable threshold report SHA-256 is
`09b5d5238b35d55d6122e13a69ec9e6608a75c863cac7b6302e5416ddbf8c555`;
checker SHA-256 is
`9e087ca8dcc9a232d5859326066c77aa6debebc41a68edf2681c19285d7bdfe9`;
benchmark producer SHA-256 is
`34242c14be1d796c8f3db97be31b3296ee642a530a2b88f9cb6994b8232d536a`.

## Fresh local accumulated acceptance results

- macOS 15.7.7 x86_64, Python 3.12.13, Node 22.14.0, Playwright 1.50.1 and
  frozen Chromium were used.
- `pip check`, Ruff, strict mypy over 21 source files, B4 and B6 OpenAPI/type
  checks, approved-threshold enforcement, production assets, CLI help and
  `git diff --check` passed.
- Full non-hardware Python reported 379 passed, 2 documented sandbox-loopback
  skips and 106 warnings. Focused threshold/evidence/native-harness/OpenAPI
  validation reported 17 passed.
- ESLint and TypeScript passed; Vitest reported 3 files and 5 tests passed; the
  production build transformed 29 modules and reproduced assets.
- Fresh browser evidence passed the independent DPR/request/DOM/secret case
  1/1 and fake-live plus complete offline workflows 3/3. The first attempt
  overlapped another root-owned server and failed only to start its configured
  listener; after the concurrent listener ended, the unchanged command passed
  completely and left no residue.
- Fresh native installed-browser evidence passed 1/1. Fresh automatic B6
  benchmark plus checker passed 1/1. No raw machine-local or capability value
  entered durable output.

Python lock SHA-256 is
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
Node lock SHA-256 is
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
B6 asset manifest SHA-256 is
`c27b08c3fbbce7ead5e7afa4b92bffdaf9623f46f4319d92c78942ab2e59059d`;
B6 OpenAPI SHA-256 is
`3d1a4717ca6f174c3f9394316492319601b9175b7a3e0ac09dea5c622eea2e88`;
and generated B6 TypeScript SHA-256 is
`2f01d137876ebea792dbb868b37eb7044f172ee3fb395fb8cc42cca6d63179f6`.

## Open acceptance finding

### C2B6-A001 — exact-candidate hosted macOS CI failed

Owner: implementation/integration. The governing B6 acceptance and Cycle 2
stopping condition 3 require the exact final candidate to pass the complete
accumulated suite on hosted macOS CI before acceptance and checkpoint
readiness.

Dedicated branch `cycle2-b6-ci-candidate` was pushed at exact commit
`758961069164a8700bc9a93a2709f78d86bc205d`, tree
`2c016816dc64bf21d231cd0e5ea3770ac6a1d475`. The sole workflow is macOS-only.
Run `32669668507`, job `97268420731`, completed with `failure`. Setup,
hash-locked installation, `pip check`, Ruff and mypy passed; the non-hardware
pytest step failed and every later workflow step was skipped. The public
annotation is sanitizer-truncated and does not expose the underlying assertion.

An exact local `CI=true` Python 3.12 rerun passes 379 tests with 2 documented
skips, but local success cannot waive or replace the required hosted failure.
The failure requires diagnosis within the owning product/test/workflow surface,
a corrected immutable candidate if any tracked change is made, fresh
independent verification, complete accumulated validation, and a new exact-
candidate hosted macOS pass before acceptance may repeat. No prior local,
native, physical, performance or verification pass transfers to a changed
candidate.

Open findings: `C2B6-A001`. Deferred findings: none.

## Scope, verdict, and Git handoff

No firmware, bootloader, Wi-Fi, wiring, persistent-device, public-server,
packaging/publication, C#/.NET, `.lac`, threshold rebase, non-macOS support
claim, completion record or Cycle 3 action occurred. Firmware/C# sources,
Cycle 1 fixtures and the accepted CLI remain present. This acceptance did not
modify product or prior evidence.

Verdict is `changes_required`. The exact candidate is not eligible for B6
acceptance, evidence manifest, checkpoint, Cycle 2 completion or a fourteen-
condition success claim while hosted run `32669668507` is red. Exact Git
handoff: stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b6-acceptance-round-1.md`; record its
SHA-256; return `C2B6-A001` to the implementation/integration owner; do not
create a B6 manifest/checkpoint, do not begin Cycle 3, and do not report Cycle 2
complete.
