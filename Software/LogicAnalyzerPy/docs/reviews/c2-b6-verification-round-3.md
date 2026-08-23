# C2-B6 verification round 3

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T22:02:42Z`.
- Product candidate: `758961069164a8700bc9a93a2709f78d86bc205d`;
  tree `2c016816dc64bf21d231cd0e5ea3770ac6a1d475`.
- Implementation record: commit `5fcd202`, SHA-256
  `dc869adea7bb23bc2f6723eff4659c4e8031cbcd6ff3dabe772e23cb01518e3b`, evidence only.
- Verdict: `pass`.

## Findings and dispositions

1. `C2B6-V001` — closed. The producer observes every waveform request, computes `end - start`,
   requires at least one observation, rejects any span above 100,000, and records both the
   approved and observed maxima as exactly 100,000 for the frozen workload. The chained checker
   freezes those values. Independent mutations to either value at the former 393,216 capture
   capacity reject, as do all five earlier viewport/fixture/raw-timing/load-role/product-identity
   mutations. `npm run benchmark:b6` automatically runs Playwright generation followed by the
   checker and exited successfully.
2. `C2B6-V002` — remains closed. The strengthened installed native test is unchanged from the
   independently audited correction and root's exact-candidate rerun passed 1/1 in 14.5 seconds,
   covering physical values, trigger/cursor, ordered bus values, exact export content,
   reopen/second capture, nondisclosure, and shutdown.
3. `C2B6-V003` — remains closed. The minimal correction changes only benchmark observation,
   report/checker identity, and its regression test. Driver, live API, viewer, generated API,
   production assets, sanitized physical evidence, and bound round-one capture/recovery digests
   are unchanged, so the previously independently inspected exact physical artifacts remain
   applicable.

## Independent evidence

- Canonical enforcement passed. Seven targeted mutations—five prior classes plus approved and
  observed waveform spans changed to 393,216—were rejected 7/7.
- Focused enforcement/evidence/native-harness/OpenAPI tests: 17 passed.
- Fresh automatic B6 benchmark passed 1/1 plus chained enforcement. It observed maximum request
  span exactly 100,000 and retained the 960-pixel, 46,129-command, below-1,000-DOM, 100-row, and
  memory-unavailable rules. Independent nearest-rank p95 values were load `447.6`, interaction
  `344.0`, representative bus `153.2`/`70.2`, and worst bus `405.9`/`153.3` ms, all within both
  approved ceilings. Generated report SHA-256:
  `100df4e75d714d26e83299365acaf87f20cc308c9132b40eedd54e4ed2f4f3c2`;
  generated residue was removed.
- Clean accumulated nonhardware Python: 379 passed, 2 documented sandbox-loopback skips,
  106 warnings. Focused Ruff, strict mypy over 21 source files, frontend lint/typecheck, and diff
  checks passed.
- Root's exact-candidate strengthened native 1/1 and automatic benchmark 1/1 reruns agree with
  the independent static and benchmark evidence. No raw port, serial, location, device identity,
  capability, or machine-local value is recorded.

Corrected file identities match: threshold report
`09b5d5238b35d55d6122e13a69ec9e6608a75c863cac7b6302e5416ddbf8c555`, implementation test
`630554d5b8589f2f023adf4b1f1ede2ac8a10c22d253d1aec4723736a8f9ac1c`, checker
`9e087ca8dcc9a232d5859326066c77aa6debebc41a68edf2681c19285d7bdfe9`, and benchmark producer
`34242c14be1d796c8f3db97be31b3296ee642a530a2b88f9cb6994b8232d536a`.

## Scope and conclusion

No threshold was weakened, rebased, or proposed. No product outside the minimal enforcement
correction, prior evidence, contract, progress, manifest, firmware, wiring, persistent device
state, public service, packaging, .NET surface, acceptance, completion record, or Cycle 3 work
was changed.

Open findings: none. Deferred findings: none.
