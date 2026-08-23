# C2-B4 independent verification — round 1

- Lane / stable identity: verifier / `cycle2-verifier-replacement-3`
- Implementation identity: `cycle2-implementor-replacement-6`
- Product candidate commit: `296feec8d9a6441b0194fa95c06128be173d234e`
- Product candidate tree: `660a1f3d7689002c588c583591d8bf30b589d09f`
- Verification test commit: `5efadbc`
- Verified at: `2026-08-23T18:11:26Z`
- Verdict: `changes_required`

## Authority, candidate, and scope

The candidate exists and resolves to the assigned tree. Verification reviewed
the operator-approved REST/polling and Python-owned OpenAPI decision, complete
B4 bus/API/security/file-transfer clauses, accepted B1 web boundary and B2/B3
data semantics, current progress, implementation record, exact candidate
delta, OpenAPI artifact, generated TypeScript, checker, server routes, and bus
core. No prior implementation result was transferred as verification evidence.

Verifier-owned literal fixtures independently calculate reordered,
noncontiguous LSB-first transition and distinct-strobe rows, both edge
polarities, trigger-relative time, binary/hex/decimal formatting, interval
fields, and exact CSV bytes. The passing literal case does not derive expected
values through the production implementation. No serial/device, firmware,
wiring, persistent state, public server, .NET, packaging, B5/B6, or Cycle 3
operation occurred.

## Findings and dispositions

### C2B4-V001 — OpenAPI is not the approved closed wire contract

Owner: implementor. Most operations contain descriptions only: request bodies,
parameters, success/error status sets, JSON/media response schemas, multipart
parts, limits, and route identifiers are absent. Only Error and Operation are
schemas. Generated TypeScript consequently contains only four partial types,
not capture, channel, waveform, bus request/page, export request, import, or
readiness shapes. The checker verifies presence of four paths, two schema
properties, and an enum; it cannot detect route/schema/type drift. Freeze all
public shapes and limits with recursively closed schemas, generate or validate
the complete TS surface, and make the checker compare routes and types.

### C2B4-V002 — replay import is not implemented

Owner: implementor. Multipart recognizes replay media but returns only bytes
and optional metadata, losing the media discriminator. The route requires the
CSV metadata part for every upload and always calls `import_csv_bytes`; a valid
schema-1/schema-2 replay without CSV metadata returns `invalid_metadata`, and
replay bytes with metadata reach the CSV parser. Dispatch replay media through
the bounded replay loader while requiring metadata only for CSV.

### C2B4-V003 — waveform stride sampling erases real transitions

Owner: implementor. The endpoint labels output as transitions but samples one
word per stride. A literal one-sample high pulse between stride points is
absent from the response, so B5 cannot render the defined waveform. Return a
pixel-bounded transition reduction that preserves visible state changes,
including narrow pulses and endpoint state, with work/output proportional to
channels, pixels, and reduced transitions.

### C2B4-V004 — operation lifecycle and concurrency contract is inert

Owner: implementor. The application exposes one hard-coded `op-1` already in
`succeeded`; no API action creates pending/running/cancelling operations, active
work cannot be cancelled, and there is no deterministic 409 single-operation
conflict path or operation/connection/rate ownership limit. Implement the
approved polling lifecycle and bounded owner/cleanup behavior using fake and
offline work only in B4; retain real serial integration for B6.

### C2B4-V005 — request discriminators are not exact

Owner: implementor. Any bus mode other than literal `transition` is treated as
sampled when other sampled fields are valid, and any export format other than
literal `bus-transition-csv` is treated as sampled. This admits unknown
semantics contrary to the closed-schema/exact-input boundary. Validate exact
mode-specific unions before analysis and bind them to the OpenAPI schemas.

### C2B4-V006 — valid replay bounds are narrowed to one MiB

Owner: implementor. Generic request and upload limits are both one MiB, so
valid bounded replay artifacts allowed by the accepted schema-2 archive/sample
limits cannot be imported. Set a finite streaming boundary that accommodates
the accepted replay maximum, enforce aggregate multipart accounting before
full materialization, and retain stricter JSON/metadata limits separately.

### C2B4-V007 — candidate fails the accumulated mypy gate

Owner: implementor. Current locked-environment mypy reports four errors across
the new bus/server sources: two missing ndarray type parameters, one redundant
cast, and one Any return from a declared capture lookup. Correct them without
weakening static configuration.

### C2B4-V008 — focused loopback API test has an incorrect transition count

Owner: implementor. The brokered focused loopback test fails because its
three-row literal CSV changes bus value from `00` to `01` to `11`, so the
transition contract emits sample zero plus two changes (total 3), while the
implementation test requires total 2. The endpoint returned HTTP 200 and the
contract-correct total 3. Correct the focused expected value and extend the API
fixture to assert the literal rows rather than only a mistaken count.

No finding is deferred. Open findings are `C2B4-V001` through `C2B4-V008`.

## Passing observations

- Independent literal bus semantics and deterministic CSV: pass.
- Existing canonical loopback/Host/Origin/cookie middleware remains ordered
  before routes; every current POST mutation calls the shared mutation guard.
- Initial cookie remains host-only, HttpOnly, SameSite Strict and Path `/`;
  shutdown expires it. No CORS grant or WebSocket route exists.
- Errors use the bounded JSON envelope; downloads use a fixed filename,
  `text/csv`, attachment disposition, and `nosniff`; imports/exports retain only
  in-memory values and accept no server paths.
- B4 server source imports no serial driver or transport and exposes no device
  route.

These observations do not close the findings or substitute for the missing
hostile, lifecycle, replay, and complete schema tests.

## Commands and concise results

- Verifier B4 regression: 1 passed, 3 failed, exposing V001--V003.
- Existing non-hardware suite excluding the new failing regression: 283 passed,
  2 sandbox-loopback skips, 16 warnings.
- Pip check and Ruff: pass. Mypy: fail with 4 errors in 2 new source files.
- Existing OpenAPI checker and CLI help: pass; checker insufficiency is V001.
- Brokered focused loopback API: 1 failed; HTTP 200 bus response reported the
  contract-correct total 3 while the implementation test expected 2 (V008).
- Pinned Node 22.14.0 lint/typecheck/Vitest/build/assets: pass; 1 unit test and
  26-module production build.
- Brokered pinned-Node Playwright production-shell smoke: 1 passed in 1.5
  seconds; residue removed centrally.
- `git diff --check`: pass.

## Verdict and authority

Verdict is `changes_required`. The exact candidate does not satisfy the
complete B4 API, replay, waveform, lifecycle/concurrency, schema/type, bounds,
or accumulated static gates. No acceptance, B4 manifest, checkpoint, or B5
work is authorized. After all findings are corrected in a new immutable
candidate, repeat complete independent verification and the accumulated gate;
no passing observation transfers as acceptance.
