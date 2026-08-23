# C2-B4 verification round 5

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T19:07:08Z`.
- Product candidate: `9b1e3058b07cda1b69c89ca2371d563e2959aa1d`;
  tree `adda851305e750777d7b7869f164568842ce29e4`.
- Implementation record reviewed as evidence only: `d2743adeafbf214f04b38f1c3ed61b9fffb1262a`.
- Verdict: `changes_required`.

## Findings and dispositions

1. `C2B4-V001` — open. The candidate now rejects canonical `BusRow.decimal`, a
   representative primitive, an enum, and direct generated model/response mutations, but
   it does not establish complete OpenAPI/generated-TypeScript parity. Independent literal
   mutations proved that the checker accepts all five of the following:
   - OpenAPI `BusRequest.strobe_channel` nullability removal;
   - OpenAPI `BusRequest.channel_ids.items` integer-to-string drift;
   - generated TypeScript `BusRequest.offset` number-to-string drift, masked by the
     same-named `BusPage.offset` field;
   - generated TypeScript `channel_ids` number-array-to-string-array drift;
   - generated TypeScript `strobe_channel` nullability removal.
   These are frozen request/wire-model properties, so accepting any one is type drift.
2. `C2B4-V004` — resolved; the accumulated independent simultaneous-first-upload test passes.
3. `C2B4-V006` — resolved; the accumulated independent maximum B2-valid replay browser import
   passes without changing the established bounds.
4. `C2B4-V011` — resolved; prior verifier-owned evidence remains restored and unmodified.

## Independent evidence

- Fresh round-five mutation suite: canonical contract accepted; 6 rejection cases passed and
  5 required rejection cases failed as enumerated in `C2B4-V001`.
- Prior independent B4 focused suite, including literal bus/export, waveform, concurrency,
  cleanup, maximum replay, and checker checks: 19 passed.
- Clean accumulated non-hardware Python suite (excluding this intentionally failing mutation
  evidence): 305 passed, 2 loopback sandbox skips, 44 warnings. Ruff passed; mypy passed for
  21 source files; dependency check, canonical checker, CLI help, and diff check passed.
- Pinned Node 22 lint and typecheck passed; Vitest 1 passed; production build transformed 26
  modules; generated asset tree was unchanged.
- Root-brokered fresh real-loopback API test: 1 passed, exit 0. Root-brokered pinned Node 22
  Playwright production-shell smoke: 1 passed, exit 0; generated residue was removed.

## Contract, security, and scope audit

The complete B4 REST-plus-polling route, status, closed schema, runtime/TypeScript surface,
bounded multipart/replay and JSON handling, transition-reduced waveform, bus pagination and
deterministic export, hostile Host/Origin/capability enforcement, no-CORS/no-WebSocket boundary,
redaction, concurrency/cancellation/shutdown cleanup, and no-residue requirements were
rechecked through current source and accumulated independent tests. No new defect was found
outside checker completeness. No serial/device, firmware, wiring, persistent service, .NET,
B5/B6, acceptance, or Cycle 3 action occurred. Product files and earlier verifier evidence were
not modified.

Open findings: `C2B4-V001`.
