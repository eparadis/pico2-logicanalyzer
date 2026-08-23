# C2-B4 independent verification — round 3

- Lane / stable identity: verifier / `cycle2-verifier-replacement-3`
- Implementation identity: `cycle2-implementor-replacement-6`
- Product candidate commit: `c627cc33999e3d1caef03dd281f99ef0487e4c6a`
- Product candidate tree: `81cbccda857122df7a7d51dba530d0c985c7d8be`
- Implementation evidence record commit: `945a409`
- Verified at: `2026-08-23T18:40:47Z`
- Prior-verdict transfer: none
- Verdict: `changes_required`

## Authority, candidate, and scope

The candidate exists and resolves to the assigned tree. Verification reread the
operator-approved REST/polling/OpenAPI decision, full B4 governing clauses,
accepted B1/B2/B3 boundaries, immutable rounds one and two, implementation
round three, the exact correction delta, and every public API/schema/type,
operation, replay, upload, bus, waveform, export, security, and limit surface.
The implementation record was treated only as an audit input.

A new verifier-owned round-three test independently races two first imports
before multipart completion and checks browser upload capacity against the
accepted schema-1 replay limit. No serial/device, firmware, wiring, persistent
state, public serving, .NET, packaging, future-batch, or Cycle 3 operation
occurred.

## Prior finding dispositions

1. `C2B4-V001`: open. The OpenAPI artifact now recursively describes the
   observed capture/channel/waveform/bus/operation objects and generated
   TypeScript currently matches them. However, the required deterministic
   schema/type drift checker still reads no TypeScript and verifies only four
   path names, top-level schema closure, and one enum. It therefore passes when
   generated types, route methods/statuses, parameters, nested schemas, or
   runtime shapes drift. Extend the checker to validate the complete approved
   route/schema surface and generated TypeScript artifact.
2. `C2B4-V004`: open. Pollable background decoding and cancellation were added,
   but ownership is checked without reservation before awaiting multipart. Two
   simultaneous first uploads both observe no operation, both enter body
   consumption, and both return `202`; neither receives the required
   deterministic `409`. Reserve the pending owner atomically before any body
   read, and release it on malformed upload, disconnect, cancellation, failure,
   completion, and shutdown.
3. `C2B4-V006`: open. The outer 4 MiB limit now reaches the 3 MiB artifact
   limit, but B4 must import every valid replay retained by B2. Accepted
   schema-1 artifacts may approach the frozen 32 MiB archive bound and 17 MiB
   sample-member bound. The browser API/OpenAPI still rejects those valid
   artifacts at 3 MiB. Use an aggregate streaming limit accommodating the
   accepted archive maximum plus multipart framing while retaining separate
   strict JSON/metadata bounds.
4. `C2B4-V009`: resolved at the core byte loader. Independent canonical
   2,100,000-sample schema-1 replay loading passes, and the loader restores the
   frozen 32 MiB archive, 17 MiB sample member, and 64 KiB metadata bounds.
   Browser reachability of the larger accepted artifacts remains V006.
5. `C2B4-V010`: resolved. Finite eight-in-flight and 32-per-second loopback
   limits reject with bounded `429` responses and clean their counters.

## New finding

### C2B4-V011 — implementation changed verifier-owned evidence

Owner: implementor/process. The product candidate modifies
`tests/verification/test_c2_b4_contract_blackbox.py`, a path explicitly owned by
the independent verification lane, adding implementation-authored disposition
tests and altering imports. This invalidates lane separation and makes the
candidate's claimed verifier-test pass non-independent. Move any useful cases
to implementation-owned tests, restore the verifier-owned file exactly, and
create a new immutable product candidate. Verification must then rerun from its
own unchanged evidence plus any separately owned new tests.

Open findings are `C2B4-V001`, `C2B4-V004`, `C2B4-V006`, and `C2B4-V011`.
No finding is deferred.

## Passing independent observations

- Literal reordered/noncontiguous bus, transition intervals, both strobe
  edges, exact time/value formatting, deterministic CSV/export: pass.
- Pulse-preserving bounded waveform fixture: pass.
- Replay-versus-CSV dispatch, exact discriminators, closed multipart parts,
  accepted core schema-1 bounds, poll/cancel terminal cleanup, Host/Origin/
  cookie/no-CORS/no-WebSocket/redaction/no-path/safe-download behavior: pass
  where independently exercised.
- Real loopback implementation workflow and production browser shell pass, but
  neither covers the simultaneous pre-body race or accepted large replay upload.

## Commands and concise results

- Fresh round-three verifier boundary: 2 failed, proving V004 and V006.
- Candidate-carried B4 contract file: 9 passed; not credited as independent
  because the candidate modified the verifier-owned path (V011).
- Clean accumulated Python excluding the two intentionally failing new cases:
  pip check, Ruff, mypy over 21 files, OpenAPI checker, CLI help, and diff check
  passed; pytest reported 292 passed, 2 sandbox-loopback skips, 35 warnings.
- Stable real-loopback API command: 1 passed, exit 0.
- Pinned Node 22.14.0 lint/typecheck/Vitest/build/assets: pass; 1 unit test and
  26-module build.
- Brokered pinned-Node Playwright production shell: 1 passed, exit 0; generated
  residue removed centrally.

## Residual risks and verdict

The unresolved first-upload race permits simultaneous body allocation and
multiple active import operations, directly weakening concurrency and cleanup
guarantees. The upload ceiling rejects accepted schema-1 replay data, and the
checker does not enforce the advertised OpenAPI/TypeScript authority. Candidate
ownership contamination independently requires replacement even if product
behavior were otherwise corrected.

Verdict is `changes_required`. No B4 acceptance, evidence manifest, checkpoint,
or B5 work is authorized. A new immutable candidate must resolve all four open
findings, restore lane ownership, and repeat complete verification and
accumulated validation with no pass transfer.
