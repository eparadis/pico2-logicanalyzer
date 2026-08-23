# C2-B4 independent verification — round 2

- Lane / stable identity: verifier / `cycle2-verifier-replacement-3`
- Implementation identity: `cycle2-implementor-replacement-6`
- Product candidate commit: `dd49ee6aab0092c3963ed30f279fcde026ab70d7`
- Product candidate tree: `4d29e8309f8d0365b0b9804227a2587e929c2d01`
- Verification test layer: `9ae9eac`
- Verified at: `2026-08-23T18:22:17Z`
- Prior-verdict transfer: none
- Verdict: `changes_required`

## Authority, candidate, and scope

The assigned commit exists and resolves to the assigned tree. Verification
independently reread the operator-approved REST/polling/OpenAPI decision, full
B4 governing bus/API/security/file-transfer clauses, accepted B1 web and B2/B3
data boundaries, immutable round-one findings/tests, implementation round two,
the exact correction delta, and every public route/schema/type/checker surface.
No prior pass transferred.

Verifier-owned literal fixtures cover reordered/noncontiguous LSB-first bus
values, transition intervals, both distinct-strobe edges, trigger-relative
times, exact formatting/CSV, narrow waveform pulses, replay dispatch, closed
wire shapes, reachable upload limits, and retained schema-1 bounds. No
serial/device, firmware, wiring, persistent state, public serving, .NET,
packaging, future-batch, or Cycle 3 operation occurred.

## Prior finding dispositions

1. `C2B4-V001`: open. Route names and response references were expanded, but
   the OpenAPI schemas still do not describe the complete runtime wire objects.
   `CaptureMetadata` omits four emitted fields while declaring additional
   properties forbidden; most object properties are not required; arrays such
   as waveform channels and bus rows lack item schemas. Generated TypeScript
   consequently uses `unknown[]` and cannot establish complete drift safety.
   The checker remains a shallow presence/enum check rather than validating
   route methods, statuses, parameters, recursive closure, or generated types.
2. `C2B4-V002`: resolved for bounded small artifacts. Replay media now retains
   its discriminator, does not require CSV metadata, and reaches the inert
   replay byte loader; CSV continues to require exact metadata.
3. `C2B4-V003`: resolved. The independent narrow-pulse fixture now retains the
   initial state, pulse edges, and final endpoint under a two-pixel window.
4. `C2B4-V004`: open. Import still performs synchronous replay/CSV parsing and
   allocation inside the request handler. It sets `running` and then reaches a
   terminal state before yielding a pollable operation response; no production
   path creates `pending` or `cancelling`, and cancel cannot interrupt active
   work because the event loop is occupied. Conflict is checked only after the
   complete multipart body has been read. Implement genuine bounded background
   offline work, observable states, pre-upload conflict rejection, cancellation,
   disconnect cleanup, and deterministic 409 ownership.
5. `C2B4-V005`: resolved. Unknown bus modes/export formats and inconsistent
   transition-versus-sampled fields now reject.
6. `C2B4-V006`: open. The advertised 3 MiB part limit is unreachable because
   the outer aiohttp and request middleware limit remains 1 MiB, including
   multipart framing. Separate the larger aggregate streaming upload limit from
   the stricter JSON limit and enforce both consistently before allocation.
7. `C2B4-V007`: resolved. Locked mypy passes over all 21 source files without a
   configuration change.
8. `C2B4-V008`: resolved. The corrected literal loopback fixture expects all
   three transition rows and passes outside the sandbox.

## New findings

### C2B4-V009 — replay byte import regresses accepted schema-1 bounds

Owner: implementor. The new byte loader rejects every archive above 2 MiB and
every sample member above approximately 385 KiB. The accepted replay security
contract retains schema-1 reads up to 16,777,216 uint8 samples, a 17 MiB sample
member, and a 32 MiB archive. An independently constructed canonical inert
2,100,000-sample schema-1 NPZ is valid under those frozen bounds but is rejected
as too large. Restore the accepted schema-1 archive/member limits while applying
the mode-appropriate V2 bounds only to schema 2 after bounded header/metadata
inspection.

### C2B4-V010 — connection and request-rate limits remain absent

Owner: implementor. The governing boundary requires explicit finite connection
and request-rate limits. The server has byte/window/row/capture constants but no
connection-owner or request-rate accounting, deterministic excess response, or
cleanup test. Add bounded loopback connection/request ownership without remote
or multi-user scope.

Open findings are `C2B4-V001`, `C2B4-V004`, `C2B4-V006`, `C2B4-V009`, and
`C2B4-V010`. No finding is deferred.

## Security and behavior audit

The corrected candidate retains literal loopback-only binding, hostile Host
rejection before routing, exact single Origin and capability cookie checks for
every mutation, host-only HttpOnly SameSite-Strict cookie delivery/expiry, no
CORS grant, no WebSocket route, bounded redacted errors, fixed safe CSV download
headers, opaque in-memory IDs, no accepted server paths, and no serial imports.
Unknown/duplicate multipart parts and wrong media reject, and no persistent or
temporary import/export file is created. These passing observations do not
close the operation, aggregate-upload, connection/rate, or schema findings.

## Commands and concise results

- Independent B4 regression: 4 passed, 3 failed; failures prove V001, V006,
  and V009.
- Full non-hardware suite before the added failing boundaries: 287 passed, 2
  sandbox-loopback skips, 20 warnings.
- Brokered corrected real-loopback API: 1 passed, 5 warnings, exit 0.
- Pip check, Ruff, mypy over 21 source files, CLI help, existing OpenAPI checker,
  deterministic assets, and `git diff --check`: pass.
- Pinned Node 22.14.0 lint/typecheck/Vitest/build: pass; 1 unit test and
  26-module build.
- Brokered pinned-Node production Playwright shell: 1 passed in 1.1 seconds;
  residue removed centrally.

## Verdict and authority

Verdict is `changes_required`. The exact corrected candidate still fails the
complete B4 schema/type, asynchronous operation/concurrency, reachable-upload,
accepted replay compatibility, and connection/rate-limit contracts. No B4
acceptance, manifest, checkpoint, or B5 work is authorized. A new immutable
candidate must repeat complete verification and accumulated validation; no
round-two passing result transfers.
