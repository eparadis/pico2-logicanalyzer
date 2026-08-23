# C2-B4 independent verification — round 4

- Lane / stable identity: verifier / `cycle2-verifier-replacement-3`
- Implementation identity: `cycle2-implementor-replacement-6`
- Product candidate commit: `f618455a370c7de57c1a310335c0095b2660cc58`
- Product candidate tree: `df7a1659a26d681ca585b2dd8f86b38e21c55a3e`
- Implementation evidence record commit: `acddbac`
- Verified at: `2026-08-23T18:57:54Z`
- Prior-verdict transfer: none
- Verdict: `changes_required`

## Authority, candidate, and scope

The assigned commit exists and resolves to the assigned tree. Verification
freshly reviewed the operator-approved REST/polling/OpenAPI authority, every B4
governing bus/API/security/file-transfer clause, accepted B1/B2/B3 boundaries,
all prior immutable findings, the implementation round-four record as evidence
only, the exact correction delta, and all runtime/schema/type/checker surfaces.

A new verifier-owned round-four test mutates nested OpenAPI and generated
TypeScript bus field types and independently imports the maximum accepted
16,777,216-sample schema-1 artifact through the asynchronous browser API. No
serial/device, firmware, wiring, persistent state, public serving, .NET,
packaging, acceptance, B5/B6, or Cycle 3 operation occurred.

## Prior finding dispositions

1. `C2B4-V001`: open. OpenAPI itself is now complete and recursively closed,
   with exact routes, methods, path parameters, statuses, multipart bounds,
   runtime objects, and generated TypeScript shapes. However, the required
   deterministic drift checker still validates structure rather than the
   authoritative field types. It accepts an OpenAPI mutation changing
   `BusRow.decimal` from integer to string, and independently accepts the
   corresponding generated TypeScript mutation from `number` to `string`.
   Make the checker derive or compare every generated type and validate the
   frozen primitive/enum/nullability constraints, then add mutations that prove
   each representative nested request/response/type class fails.
2. `C2B4-V004`: resolved. Independent simultaneous-first-upload execution now
   proves one owner is reserved before either multipart body is read, the second
   request receives deterministic 409, malformed-body release works, pollable
   pending/running/cancelling/terminal states work, and cleanup releases task,
   cancel, body, and owner state.
3. `C2B4-V006`: resolved. The 33 MiB aggregate artifact quota accommodates the
   accepted 32 MiB replay archive plus bounded metadata, and the 34 MiB outer
   request boundary adds multipart headroom while JSON/metadata remain stricter.
   A maximum accepted schema-1 sample artifact completes asynchronous import.
4. `C2B4-V011`: resolved. The candidate restores
   `tests/verification/test_c2_b4_contract_blackbox.py` byte-for-byte to the
   verifier-owned `9ae9eac` version; both SHA-256 values are
   `2d31d3914b8c209d3ccecd8a8c1bdec2c6c6245cf1115d9a99eb1f37011c9574`.
   New disposition cases reside under implementation-owned tests.

Open finding: `C2B4-V001`. No finding is deferred.

## Complete behavior and security result

Independent and accumulated coverage passes literal reordered/noncontiguous
LSB-first buses, transition intervals, both distinct-strobe edges,
trigger-relative time, fixed formatting, deterministic bus/export CSV,
pulse-preserving pixel-bounded waveform reduction, schema-1/schema-2 and CSV
imports, metadata/channels/windows/pagination, polling/cancel/shutdown cleanup,
and exact request discriminators.

The candidate retains literal loopback-only binding, hostile Host rejection
before routing, exact Origin and single capability cookie checks on all
mutations, cookie attributes/expiry, no CORS or WebSocket route, bounded and
redacted errors, duplicate/unknown/missing multipart/media rejection, aggregate
stream accounting, finite connection/rate/window/row/operation limits, safe
fixed downloads, opaque in-memory IDs, no server paths or persistent/temp files,
and no serial import/open surface. The open checker finding prevents acceptance
despite the current artifacts matching.

## Commands and concise results

- Fresh round-four verifier: maximum accepted browser replay 1 passed; two
  mutation-sensitivity cases failed, proving V001.
- Restored round-three concurrency/upload verifier: 2 passed.
- Clean accumulated Python excluding the intentionally failing round-four
  mutation cases: pip check, Ruff, mypy over 21 files, OpenAPI checker, CLI
  help, and diff check passed; pytest reported 301 passed, 2 sandbox-loopback
  skips, 37 warnings.
- Pinned Node 22.14.0 lint/typecheck/Vitest/build/assets: pass; 1 unit test and
  26-module build.
- Stable brokered real-loopback API: 1 passed, 37 warnings, exit 0.
- Brokered pinned-Node Playwright production shell: 1 passed, exit 0; generated
  residue removed centrally.

## Residual risk and verdict

The checked-in OpenAPI and TypeScript happen to agree, but the mandatory checker
cannot detect substantive primitive-type drift in either authority artifact.
That permits later incompatible Python/browser wire changes to pass the frozen
drift gate.

Verdict is `changes_required`. No B4 acceptance, evidence manifest, checkpoint,
or B5 work is authorized. After V001 is corrected in a new immutable candidate,
repeat complete verification and accumulated validation with no pass transfer.
