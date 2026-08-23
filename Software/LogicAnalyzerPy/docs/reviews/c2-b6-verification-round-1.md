# C2-B6 verification round 1

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T21:40:00Z`.
- Product candidate: `4640f746c080087fc9783d89a18e3c8e5573a454`;
  tree `50945a9387709e7637d98294ba5b9cc08dc87cfd`.
- Implementation record: commit `eb200cd`, SHA-256
  `10bdd3188c68be6afdf961517fc29adb78f47e9dab6998456a9a8bc7361046d6`, evidence only.
- Verdict: `changes_required`.

## Findings and dispositions

1. `C2B6-V001` — open. `tools/check_b5_thresholds.py` does not enforce the complete
   operator-approved method/resource identity. Independent mutations of viewport, fixture
   digest, fixture-manifest digest, raw interaction timings, and a required load role were all
   accepted (5/5). It neither recomputes p95 from fresh raw arrays nor checks the frozen
   fixture/method identities, per-case repetitions, waveform request span/pixel width,
   per-channel Canvas formula, or nondisclosure fields. Moreover `npm run benchmark:b6` produces
   the report but does not invoke this checker. The current report happens to pass independent
   calculation, but B6 cannot reliably prevent omission/substitution or silent method drift.
2. `C2B6-V002` — open. The installed native-browser test proves API completion, channel-label
   presence, a rendered Canvas, bus-table presence, download filename, reopen, second capture,
   nondisclosure, and shutdown, but does not assert the approved D0/D8/D16/D23 physical values
   or activity, trigger/cursor values, bus contents/order, or exported bytes. The governing B6
   native-browser gate requires the physical pattern to be displayed and inspected and exported
   artifacts to be validated, not only that the corresponding elements exist.
3. `C2B6-V003` — open. The durable implementation evidence declares
   `source_revision = 844cf3fbcf8a01530ea05a63b02260f3d22ffedc`, the B6 activation commit/tree,
   rather than the product candidate. It also records only active-channel lists for physical
   captures, omitting exact masks, dtypes, high-bit-zero, frequency, CSV/export identity, and
   exact-candidate artifact digests. Fresh verification proves the device behavior, but the
   candidate's claimed immutable final hardware mapping remains incomplete and misidentified.

## Independent exact-candidate physical and native evidence

Root brokered three fresh explicit-port captures on the confirmed protected setup. Independent
inert NPZ and CSV readers—not the implementation harness—proved:

- 8 channels: `uint8`, 4,096 samples, trigger 1,024, driven projection exactly
  `{0, 0x01}`, and 31 rising edges on D0;
- 16 channels: `uint16`, 4,096 samples, trigger 1,024, projection exactly
  `{0, 0x0101}`, and 31 rising edges on D0/D8;
- 24 channels: `uint32`, 4,096 samples, trigger 1,024, projection exactly
  `{0, 0x810101}`, 31 rising edges on D0/D8/D16/D23, and bits 24–31 zero;
- all ordered channel IDs/labels and every CSV sample/bit value matched the inert NPZ data.

Temporary artifact SHA-256 values, ordered 8 NPZ/CSV, 16 NPZ/CSV, 24 NPZ/CSV, were
`edd4ca5f3d6b70575f540f09bb6e77e648f3e2ed8d1bb14a5954aefa7cb76c71` /
`af443f08089ac51aa3d93343730a864f172a948c14be68fa972399dbceb66311`,
`63f3ecc846c1b451f6832ff1c8adba864c70e6ec14901cc5c6b4e143511b24a0` /
`67830a7eafdadfced8145ba50a388fe7714002db23d3f9675ae5ce0f047d5548`, and
`75ae2fa1884f1725800babc37321bf653c989336bba3bc922d423f7e1ff0622e` /
`5cc335356ba8271ff20d44b81b9a8460f442b8f0147ec8228a29cc1dacbd2264`.

Fresh fixed-low D1 recovery used the accepted `ff` byte, reidentified, captured 6,144 samples,
observed 42 transitions and approximately 1.012 kHz on D0, and made no persistent device
change. Sanitized recovery artifact SHA-256:
`f72dd947d455b84ee0a12bbce48b7ff84c9c27ed749486b9f2d2623c45cd8862`.
Fresh installed native production Playwright passed 1/1 in 13.7 seconds. No raw port, serial,
location, device identity, or capability is recorded here.

## Performance, API, security, and accumulated evidence

- Fresh B6 benchmark passed. Independent nearest-rank p95 values were: load `450.8`, pan/zoom
  `347.9`, representative bus `138.8`/`64.4`, worst bus `411.3`/`144.1` ms. All satisfy both
  approved ceilings. Maximum planned commands were 12,755, maximum DOM nodes 221, bus pages
  100, and reliable memory remained unavailable. Generated report SHA-256:
  `247bbd497d2eece47dc211918de8b8abab5fec8e18669cdd84899fec10ff809d`;
  generated residue was removed.
- Clean nonhardware Python: 373 passed, 2 documented sandbox-loopback skips, 106 warnings.
  Ruff, strict mypy over 21 source files, dependency check, B4/B6 OpenAPI fingerprints,
  production assets, CLI, current threshold report, and diff checks passed.
- Node 22 lint/typecheck passed; Vitest 3 files/5 tests passed; production build transformed
  29 modules and reproduced committed B6 assets.
- Fresh production Playwright passed the independent DPR/request/DOM/security case 1/1 and the
  fake-live plus accepted offline lifecycle workflows 3/3; generated residue was removed.
- Source/fake-transport audit rechecked strict Host/Origin/capability protection before live
  mutations, no port in request schemas or public responses, bounded inputs/timeouts, one-device
  ownership, deterministic conflict, cancel/timeout recovery, disconnect/shutdown cleanup,
  generic errors, no WebSockets/CORS, replay/CSV compatibility, and additive fingerprinted B6
  OpenAPI/TypeScript artifacts. No additional issue was found.

Frozen durable identities independently match: implementation evidence
`9d82c69b790169077f644456e7ec45af5dad80addf90119c9ec6e01ba0235737`, threshold report
`e2544d068b43a3a6ac37674c95d56f220eb7ce7a5b6de39068df475a7c9d79f9`, B6 OpenAPI
`3d1a4717ca6f174c3f9394316492319601b9175b7a3e0ac09dea5c622eea2e88`, generated TypeScript
`2f01d137876ebea792dbb868b37eb7044f172ee3fb395fb8cc42cca6d63179f6`, and asset manifest
`c27b08c3fbbce7ead5e7afa4b92bffdaf9623f46f4319d92c78942ab2e59059d`.

## Scope and open state

No firmware, wiring, persistent-device, public-server, packaging, .NET, support-expansion,
threshold-rebase, acceptance, completion, or Cycle 3 action occurred. Product, contracts,
progress, manifests, and prior evidence were not modified.

Open findings: `C2B6-V001`, `C2B6-V002`, `C2B6-V003`. Deferred findings: none.
