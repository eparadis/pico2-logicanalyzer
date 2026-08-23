# C2-B5 independent acceptance — round 1

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-3`
- Implementation identity: `cycle2-b5-implementor-replacement-1`
- Verification identity: `cycle2-verifier-replacement-3`
- Product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`
- Product tree: `06d6498f010f9cf230697aa922c2a550f8cca24c`
- Passing product verification commit:
  `d6b366bd81ff19dc6ce982941efabb9f00742c53`
- Passing threshold verification commit:
  `62e49d98da2af1151af4c021fae4bf6e69c234aa`
- Passing threshold acceptance commit:
  `dbdc9efe1e18be8dfea51419c8028347153b2088`
- Operator approval commit: `4bd025f5e252683a265df30f73e31d5a1dfca6c5`
- Accepted at: `2026-08-23T20:59:15Z`
- Prior-result transfer: none
- Verdict: `pass`

## Audit inputs and evidence integrity

Acceptance independently audited the complete macOS-only C2-B5 contract and
performance-threshold procedure; accepted C2-B1 through C2-B4 checkpoints and
manifests; exact B5 candidate and delta; both implementation and product
verification rounds; immutable round-1 failed baseline/proposal/review history;
corrected baseline and product verification; corrected threshold proposal,
passing verification, and threshold acceptance; and explicit operator approval.

The product candidate exists and resolves to the assigned tree. Its passing
product verification record has SHA-256
`ebcf3d9aac7dd1e9b3817f6567ab997cc90cf537f11cb4f5b3344a7949fc0541`
and reports no open or deferred finding. Implementation records round 1 and
round 2 have SHA-256 respectively
`91bda696a539f904045986c696c84b0155032e4bb881b11ba0c79e8366f798f6`
and
`84549590c2d2b5ebdc0e59fb7e53fbdacef730473d1a2db5e973f90676434c33`.

The approved round-2 proposal commit is
`c5eb6575625158d05b12fdd16b1c35167af385d5`, with SHA-256
`d314eea0979b567086eed7b346162eef76865507f9d8a111c736c94f62bbc597`.
Threshold verification record SHA-256 is
`7e77999b30650ab19f3b623def7f11b4e1c72b666e1c6f5791b984881eb79b71`;
threshold acceptance record SHA-256 is
`c8f0211ec189a0e5bc5c62bf610f3b40c62e95d08b8109b657ba2be86536f5e6`.
The operator-approved threshold record has SHA-256
`57183190d5d48642e9621862aeed343b0a435477a5b4b6276551e55dd01a6053`
and incorporates the unchanged round-2 proposal by exact commit and digest.

Accepted manifest SHA-256 identities remain unchanged: C2-B1
`7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0`,
C2-B2
`d930bce4ae20576ea030e35cf0e993a3caf89e95f5eb5195638471c1790c2be4`,
C2-B3
`9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`,
and C2-B4
`4876b781f4569ae1599b6c5df4d824fbd54223c736c87c96746e6bb821806fd0`.
All four strictly validate under the Cycle 2 evidence schema.

## Complete B5 product acceptance

The production React application opens schema-1 and schema-2 replay plus the
supported self-timed CSV contract through the bounded B4 API. Automated native
browser evidence covers ordered 8-, 16-, and 24-channel labels and visibility;
pan; pointer interaction; cursor-centered zoom; trigger marker; cursor
sample/time/channel-value readout; transition and distinct-strobe bus tables;
pagination; deterministic export; and explicit loading, ready, empty, error,
disconnected, cancelling, reconnect, shutdown, and second-open states.

Pure geometry and Canvas tests independently cover viewport transforms,
clamping, cursor mapping and zoom focus. Waveform work is bounded by the visible
window, visible channels, 960 CSS pixels, reduced transitions, and device-pixel
ratio rather than raw sample count. Bus DOM is paginated to 100 rows. The
maximum-width browser verifier proves request span, pixel, Canvas, DOM, and
capability-secret bounds at DPR 2, while the frozen benchmark proves the
approved DPR-1 production method.

Malformed and oversized files, API errors, failed export, cancellation,
disconnect, reconnect and shutdown do not leave false success or a partial
server-side artifact. Downloads use the bounded B4 byte response and a
browser-owned destination; imports and exports create no persistent or
temporary server file. The production application uses checked-in deterministic
assets and the loopback-only Python server: it starts no Vite development
server, requires no runtime Node or CDN, imports or opens no serial service, and
makes no non-loopback request.

Capability nondisclosure is independently checked across URL, Referer, local
and session storage, DOM, console and network observations, errors, snapshots,
and durable reports while same-origin protected requests continue to work via
the host-only HttpOnly SameSite-Strict cookie. No URL credential, wildcard
CORS, WebSocket surface, server path, remote deployment, or public serving was
introduced.

## Approved performance enforcement

The frozen baseline SHA-256 is
`c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`;
fixture-manifest SHA-256 is
`dd3ccbb4b5da4952422f2c3fc4f60dfbd4f7d2d81e789a697a19750668a1c350`;
fixture-generator SHA-256 is
`3e0be8f90e6dc846803a28bb278b21f797ddc0576f5371149beb9ad185fb29c4`;
benchmark-script SHA-256 is
`2efeca32fcac6eb8c98480d49d02b304b9985121d9f2fe3f85e8ffe47e1c930b`;
and production-asset-manifest SHA-256 is
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

A fresh valid acceptance run matched the complete frozen production identity:
method `c2-b5-playwright-production-v2`; macOS x86_64; Chromium
`133.0.6943.16`; Playwright `1.50.1`; Node `22.14.0`; 1280x900 viewport;
DPR 1; fixture bytes/roles; generator; benchmark; assets; timing boundaries;
three warmups; 16 initial loads; 30 pan/zoom observations; and two observations
for each representative/worst bus mode. The transient sanitized report had
SHA-256
`0a08297e34974148660de24701f24aa29a87a7f0804f35a9e33a8bdbd6d66dad`
and was removed after independent evaluation.

| Metric | Fresh p95 (ms) | Regression ceiling (ms) | Absolute ceiling (ms) | Result |
| --- | ---: | ---: | ---: | --- |
| Initial ready/paint | 450.30000000074506 | 772.0999999986961 | 1000 | pass |
| Pan/zoom | 331.30000000074506 | 580.3000000026077 | 750 | pass |
| Representative transition | 153.69999999925494 | 261.4499999973923 | 500 | pass |
| Representative distinct strobe | 66 | 116.7250000052154 | 300 | pass |
| Worst transition | 403.0999999977648 | 710.1499999947846 | 900 | pass |
| Worst distinct strobe | 155.5 | 263.1999999973923 | 500 | pass |

Every fresh p95 satisfies both applicable ceilings without omission,
substitution, averaging, rounding, invalid-run retry, or baseline rebase.
Fresh resource maxima were 12,755 planned Canvas commands, 216 DOM nodes, and
100 bus rows, below the approved 46,129, 1,000, and 100 bounds; waveform
requests remain capped at 100,000 samples and 960 pixels. Reliable heap data
remained unavailable and correctly recorded as `null` with
`memory_reliable: false`; no unapproved memory claim is made.

## Fresh accumulated validation

- Environment: macOS 15.7.7 build 24G720, x86_64; Python 3.12.13; Node
  22.14.0; Playwright 1.50.1 and frozen Chromium build.
- Dependency identity: both Python locks SHA-256
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
  `web/package-lock.json` SHA-256
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`.
- Clean Python gate: `pip check`, Ruff, strict mypy over 21 source files,
  OpenAPI/type validation, CLI help, deterministic asset check, and
  `git diff --check` passed. Full non-hardware pytest reported 354 passed, two
  documented sandbox-only loopback skips, and 44 warnings.
- Fresh evidence/baseline matrix: 19 passed. Accepted C2-B1 through C2-B4
  manifests strictly validated.
- Frontend gate: ESLint and TypeScript passed; Vitest reported 3 files and 5
  tests passed; deterministic production build transformed 29 modules and
  reproduced the committed assets.
- Native browser gate: independent maximum-width DPR/security test passed 1;
  complete production viewer workflows passed 2; fresh approved benchmark
  passed 1 in 24.9 seconds.
- Fresh root-brokered real-loopback API regression passed 1, exit 0. This and
  the three native browser workflows cover the two sandbox-only loopback skips.
- Generated benchmark and Playwright residue was removed after evaluation.

## Findings and dispositions

1. `C2B5-V001`: closed. Corrected durable evidence contains every required raw
   timing array, real representative/worst bus-table observations, exact roles,
   counts and identities, and independently reproducible statistics.
2. `C2B5-TV001`: closed. Frozen fixture/capture/method identities remain
   distinct from required fresh timing arrays.
3. `C2B5-TV002`: closed. Exact per-channel and aggregate Canvas command formulas
   are approved and freshly enforced without weakening proportional work.
4. `C2B5-A001`: no new overall acceptance finding; closed by this verdict.

No finding is open or deferred. Failed round-1 product/proposal reviews remain
immutable history and transfer no pass.

## Scope, repository state, and checkpoint decision

The product delta is confined to the B5 offline viewer, production assets,
frontend tests, reproducible fixture/benchmark corpus, and B5 evidence records.
Checked-in firmware, electronics, enclosure, existing C# applications, Cycle 1
fixtures, accepted CLI, B4 API/OpenAPI/generated types, and governing contracts
remain present and unchanged. No serial/hardware, firmware edit/build/flash,
bootloader, Wi-Fi, persistent-device, C#/.NET or `.lac`, public-server,
packaging/publication, live B6 integration, unsupported-platform support claim,
or Cycle 3 action occurred.

Repository state before this acceptance record was the immutable descendant
ending at operator approval commit
`4bd025f5e252683a265df30f73e31d5a1dfca6c5`, plus unrelated untracked
`.ORCHESTRATION.md.swp` of unknown ownership. That file was not read as product
evidence, modified, removed, or authorized for staging; the orchestrator must
preserve and explicitly exclude it from the B5 manifest/checkpoint state unless
its owner separately disposes of it.

Verdict is `pass`. Exact candidate
`b5d502b5ded71fdf03b38058cb4fd6438d9110ad`, tree
`06d6498f010f9cf230697aa922c2a550f8cca24c`, satisfies the complete C2-B5
product, security, performance, evidence and checkpoint-readiness gate under
the operator-approved thresholds. Exact Git handoff: the root orchestrator may
stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b5-acceptance-round-1.md`, record its
SHA-256, then create/validate/commit only the C2-B5 manifest and append the B5
checkpoint while explicitly excluding the unrelated swap file. Do not begin
B6 until that checkpoint is complete; this verdict does not authorize Cycle 3.
