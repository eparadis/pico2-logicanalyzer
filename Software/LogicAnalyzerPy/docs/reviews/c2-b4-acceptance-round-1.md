# C2-B4 independent acceptance — round 1

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-3`
- Implementation identity: `cycle2-implementor-replacement-7`
- Verification identity: `cycle2-verifier-replacement-3`
- Product candidate commit: `c8029a1c431092f5cf08de23ecc394ecc8e721d4`
- Product candidate tree: `d8a5e64f9a64f96a6c52c3cdd6da574a6f6a0c33`
- Implementation record commit: `4c7709b32ce2415627a34d6408b4182a17f939de`
- Verification evidence commit: `db065ad7795c9641a7ecde1240a3503c923b343e`
- Accepted at: `2026-08-23T19:23:27Z`
- Prior-result transfer: none
- Verdict: `pass`

## Audit inputs and identity

Acceptance independently audited the current macOS-only Cycle 2 goal and both
governing contracts; the discovery, frozen-contract, replay-security, and
orchestration-progress records; the operator-approved REST-plus-polling,
no-WebSocket, Python-owned OpenAPI 3.1 authority; accepted C2-B1 through C2-B3
checkpoints and manifests; every B4 implementation and verification record;
all finding dispositions; the exact candidate delta; implementation record
commit `4c7709b32ce2415627a34d6408b4182a17f939de`; and passing independent
verification evidence commit `db065ad7795c9641a7ecde1240a3503c923b343e`.

The assigned candidate exists and resolves to the assigned tree. The
implementation record is its direct child and has SHA-256
`ff283b698a10c8bcda747b8fa8567b69e2af22d5d3f807ae2f6f1b05057cad2e`.
The verification evidence is the next direct descendant, names that exact
candidate/tree, reports `pass` with no open or deferred finding, and its review
record has SHA-256
`59fb4849d5a0f415dd183892911a484c91dfde49483f956a29944f2e74f0653e`.
Current HEAD is that verification commit, and the worktree was clean before and
after acceptance checks.

## Integrated product and authority audit

The candidate implements the approved bounded offline boundary: deterministic
transition and distinct-strobe bus analysis from the shared Python capture
model; versioned health/readiness, multipart import, capture metadata,
channels, transition-reduced waveform, bus, direct export, operation
poll/cancel, and shutdown resources; one recursively closed Python-owned
OpenAPI document; and generated TypeScript types bound to it by conservative
whole-artifact fingerprints and semantic checks. The browser does not duplicate
bus interpretation, no WebSocket route exists, and no serial/device service is
imported or opened.

Independent evidence covers reordered and noncontiguous LSB-first buses,
sample-zero transitions and interval fields, both real distinct-strobe edges,
trigger-relative time, fixed binary/hexadecimal/decimal formatting,
deterministic CSV, empty/no-edge bounds, and pulse-preserving pixel-bounded
waveforms. Replay and CSV import, API bus/export results, and direct Python-core
results agree under independently constructed fixtures.

The security and resource audit covers literal loopback binding; canonical Host
rejection before routing; exact canonical Origin and one constant-time-checked
host-only HttpOnly SameSite-Strict capability cookie for every mutation;
capability expiry; no CORS grant; explicit WebSocket-upgrade rejection; closed
redacted errors; no URL credential, server path, client-selected output path,
persistent file, or temporary residue; strict multipart media/part structure;
declared, streamed, aggregate, metadata, JSON, sample-window, pixel, row,
capture, request-rate, and active-connection bounds; safe generated download
headers; opaque process-local identifiers; atomic pre-body operation ownership;
deterministic conflict; polling, cancellation, terminal states, disconnect and
shutdown cleanup; and compatibility with the accepted maximum schema-1 replay
archive boundary.

## Findings and dispositions

1. `C2B4-V001`: closed. Canonical whole-OpenAPI and exact generated-TypeScript
   fingerprints plus semantic validation reject complete route, response,
   reference, nested model, primitive, enum, nullability, array, bound,
   interface, identifier, and field drift while accepting insignificant JSON
   serialization differences.
2. `C2B4-V002`: closed. Bounded schema-1/schema-2 replay import is implemented
   and independently exercised through the asynchronous API.
3. `C2B4-V003`: closed. Transition-reduced waveform output preserves narrow
   pulses within the pixel-bounded representation.
4. `C2B4-V004`: closed. One operation owner is atomically reserved before body
   consumption; concurrent, malformed, cancelled, failed, completed, and
   shutdown paths have deterministic state and cleanup.
5. `C2B4-V005`: closed. Bus modes, export formats, multipart parts, media types,
   and request objects use exact closed discriminators.
6. `C2B4-V006`: closed. The bounded multipart envelope admits every valid B2
   replay up to the frozen archive limit while retaining strict metadata and
   aggregate streaming limits.
7. `C2B4-V007`: closed. Mypy passes over all 21 source files.
8. `C2B4-V008`: closed. Fresh real-loopback API execution confirms the corrected
   literal transition count and shared Python authority.
9. `C2B4-V009`: closed. Byte replay import retains the accepted schema-1 archive,
   sample-member, metadata, count, and inert-loading bounds.
10. `C2B4-V010`: closed. Finite active-connection and per-second request limits
    return bounded deterministic errors and clean their counters.
11. `C2B4-V011`: closed. The product correction restored verifier-owned evidence;
    implementation cases reside in implementation-owned tests, and round-seven
    verification added its own distinct immutable evidence after the candidate.
12. `C2B4-A001`: no new acceptance finding; closed by this verdict.

No finding is open or deferred.

## Acceptance checks and accumulated validation

- Environment: macOS 15.7.7 build 24G720, x86_64; Python 3.12.13; Node
  22.14.0; Playwright 1.50.1 with the frozen Chromium build.
- Dependency identity: `requirements-dev.lock` and `requirements-web.lock`
  SHA-256
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
  `web/package-lock.json` SHA-256
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`.
- Build identity: `web/production-assets.json` SHA-256
  `1d1b44794eed6f288f1140e67c1520d847fb3263718672cf743ff70b9da0ece9`;
  deterministic asset validation passed after a fresh 26-module production
  build.
- API identity: `web/openapi.json` SHA-256
  `bd97bffe12e9101edbb275ce6319061f947251ade18f423c61586b08c6303315`;
  `web/src/api.generated.ts` SHA-256
  `56032d85b25ffbf2ff33c5377efe125317966bbec953e8192cb1a02b4fc6fbcf`;
  `tools/check_openapi.py` SHA-256
  `d873363e02017c70feec3c31d024ae13979e55da5e4a0f678d95e3aaf71328e9`.
- Fresh acceptance Python gate: `pip check`, Ruff, mypy over 21 source files,
  OpenAPI/type validation, CLI help, and `git diff --check` passed; full
  non-hardware pytest reported 344 passed, 2 sandbox-only loopback skips, and
  44 warnings.
- Fresh acceptance B4 independent matrix: 50 passed with 22 non-fatal aiohttp
  application-key warnings. The strict Cycle 2 evidence-schema suite reported
  9 passed, and accepted C2-B1, C2-B2, and C2-B3 manifests validated with
  SHA-256 respectively
  `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0`,
  `d930bce4ae20576ea030e35cf0e993a3caf89e95f5eb5195638471c1790c2be4`,
  and `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`.
- Fresh frontend gate: ESLint and TypeScript checks passed; Vitest reported one
  passed test; production build passed and the committed asset tree remained
  deterministic.
- Fresh root-brokered native-socket coverage: real-loopback API reported one
  passed test, exit 0; pinned-Node Playwright production-shell smoke reported
  one passed test, exit 0. Generated browser residue was removed and the
  worktree returned clean.

## Scope, limitations, process risks, and checkpoint decision

The exact delta is confined to B4 Python bus/API/replay integration, OpenAPI and
generated types, implementation and verifier tests, immutable B4 review
records, and orchestration history. Checked-in firmware, electronics, enclosure,
the existing C# applications, Cycle 1 fixtures and accepted CLI remain present
and unchanged. No hardware or serial access, firmware edit/build/flash,
bootloader, Wi-Fi, power-cycle, persistent-device action, C#/.NET or `.lac`
operation, public or non-loopback serving, packaging/publication, performance
threshold work, complete viewer work, B5/B6 feature, unsupported-platform
support claim, or Cycle 3 action occurred.

The two sandbox-only loopback skips are fully covered by fresh root-brokered
real-loopback and browser executions. Non-fatal aiohttp `NotAppKeyWarning`
messages are a maintainability risk but do not weaken the closed wire contract,
security checks, bounded lifecycle, or acceptance result. The fingerprint
checker intentionally requires governed review for even harmless generated
TypeScript byte changes; its expected fingerprints remain co-located with the
checker, a conservative process constraint rather than deferred product work.
macOS remains the only supported Cycle 2 platform.

Verdict is `pass`. Candidate
`c8029a1c431092f5cf08de23ecc394ecc8e721d4`, tree
`d8a5e64f9a64f96a6c52c3cdd6da574a6f6a0c33`, satisfies the complete C2-B4
acceptance and checkpoint-readiness gate with no deferral. Exact Git handoff:
the root orchestrator may stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b4-acceptance-round-1.md`, record its
SHA-256, then create/validate/commit only the C2-B4 evidence manifest and append
the C2-B4 checkpoint. This verdict does not authorize B5 until that checkpoint
is complete and does not authorize Cycle 3.
