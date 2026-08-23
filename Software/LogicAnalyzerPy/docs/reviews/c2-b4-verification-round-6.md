# C2-B4 verification round 6

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T19:13:25Z`.
- Product candidate: `85125528e5fa65f43b4550541ef0114c800aefe3`;
  tree `6021c28ab98e72d975ee767af9b5c41ac8c46938`.
- Implementation record reviewed as evidence only: `1fdf6e18268f5f430f3041ab7664b261b54d4438`.
- Verdict: `changes_required`.

## Findings and dispositions

1. `C2B4-V001` — open. Interface scoping corrects every round-four and round-five
   representative mutation, but the checker still accepts five new wire/type mutations:
   - OpenAPI deeply nested `WaveformWindow.channels[].transitions[].value`
     integer-to-string drift;
   - generated TypeScript `BusPage.rows` referenced-array model drift from `BusRow[]` to
     `Channel[]`;
   - generated TypeScript interface-name drift from `BusPage` to `BusPageShadow`;
   - generated TypeScript `OperationState` enum contraction to two states;
   - generated TypeScript nested `WaveformWindow.channels[].channel_id` number-to-string
     drift when a same-interface injected field supplies the expected text.
   Each mutated artifact was accepted by `validate`; each is incompatible with the frozen
   schema or generated model. The regex/sub-string comparison therefore remains incomplete.
2. `C2B4-V004` — resolved. Accumulated independent simultaneous first-upload ownership and
   cleanup tests pass.
3. `C2B4-V006` — resolved. Accumulated independent maximum B2-valid replay browser import
   passes within the established bounds.
4. `C2B4-V011` — resolved. Earlier verifier evidence remains restored and unmodified.

## Independent evidence

- Fresh round-six suite: canonical checker accepted; all prior primitive, enum, nullability,
  primitive-array, interface-collision, and `BusRow.decimal` cases rejected; 11 passed and the
  5 required new rejections listed in `C2B4-V001` failed.
- Focused implementation plus round-four/five independent checks: 21 passed.
- Clean accumulated non-hardware Python suite, excluding this intentionally failing mutation
  evidence: 316 passed, 2 loopback sandbox skips, 44 warnings. Ruff passed; mypy passed for
  21 source files; dependency check, canonical checker, CLI help, and diff check passed.
- Pinned Node 22 lint and typecheck passed; Vitest 1 passed; build transformed 26 modules;
  generated assets were unchanged.
- Fresh root-brokered real-loopback API: 1 passed. Fresh pinned Node 22 Playwright
  production-shell smoke: 1 passed; generated residue was removed. Neither result changes the
  deterministic checker finding.

## Complete B4 and scope audit

Candidate/source comparison confirms the correction changes only the checker; API runtime,
OpenAPI, generated TypeScript, assets, and prior verifier evidence are unchanged. The complete
B4 route/status/schema/runtime surface, bounded multipart/replay and JSON handling, waveform,
bus/export determinism, hostile Host/Origin/capability boundary, no CORS/WebSockets, redaction,
resource bounds, concurrency/cancellation/shutdown cleanup, and no-residue behavior remain
covered by accumulated independent validation. No new issue was found outside checker
completeness. No serial/device, firmware, wiring, persistent service, .NET, acceptance, B5/B6,
or Cycle 3 action occurred; no product or earlier evidence was modified.

Open findings: `C2B4-V001`.
