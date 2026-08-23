# C2-B3 independent acceptance — round 1

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-2`
- Implementation identity: `cycle2-implementor-replacement-5`
- Verification identity: `cycle2-verifier-replacement-3`
- Product candidate commit: `90adb3adb38a938ce470fa854e6fc7b98e1501c9`
- Product candidate tree: `5a09d57e4caa266a43f164edaffc94fc9a3236d7`
- Accepted at: `2026-08-23T17:44:47Z`
- Prior-result transfer: none
- Verdict: `pass`

## Audit inputs

Acceptance independently audited the current macOS-only Cycle 2 goal,
orchestration and complete C2-B3 batch contract; approved discovery and progress
records; accepted Cycle 1 recovery evidence; accepted C2-B1 and corrected,
reaccepted C2-B2 checkpoints; the physical `C2B3-I001` history and disposition;
the exact corrected product candidate; the sanitized B3 implementation record;
the independent B3 verification record; all seven raw runtime artifacts; and
the fresh complete accumulated-gate results.

The exact candidate exists and resolves to the assigned tree. The B3
implementation record SHA-256 is
`2549b62755eec859bf34954d1f8a612e8be77bdba6e12fc88a6a5d4dd2dff27e`;
the independent verification record SHA-256 is
`ebeee036728cada9a9046fdcdee4e4a356955a5e3a1a3f10d075ba66ff4fad78`.
Both name the exact candidate/tree, and verification reports `pass` with no
open finding.

## Authority and complete-sequence audit

The operator confirmed the integrated protection circuit, 3.3 V VRef, common
ground, D0/D8/D16/D23 physical mapping and analyzer-input direction, safe
approximately 1 kHz source fan-out, fixed-low D1 recovery input, explicit
runtime port, attached Pico 2, and fixed checked-in V2 firmware before any
authorized I/O. Bounded identity then returned
`LOGIC_ANALYZER_PICO_2_V6_0` with the expected 24-channel and 393216-byte
capabilities.

After `C2B3-I001` was corrected, independently reverified, reaccepted, and
recheckpointed in B2, the entire recovery/8/16/24 physical sequence was run
fresh. No recovery, 8-channel, or 16-channel result from the failed earlier
attempt transferred. The fresh recovery performed bounded in-flight
cancellation with one literal `ff`, bounded drain, close/reopen,
re-identification, and a second 6144-sample rising-D0 capture without a power
cycle; its independently calculated frequency was exactly 1000 Hz.

## Physical and accumulated results

1. D0-D7: native `uint8`, 6144 samples, driven mask `0x01`, both driven
   projection states, 42 rising transitions, 1005.641403 Hz, deterministic CSV.
2. D0-D15: native `uint16`, 6144 samples, driven mask `0x0101`, both driven
   projection states, 42 rising transitions, 1010.349926 Hz, deterministic CSV.
3. D0-D23: native `uint32`, 6144 samples, driven mask `0x810101`, both driven
   projection states, 42 rising transitions, 1005.394801 Hz, all bits 24-31
   zero, deterministic CSV.
4. Every raw replay is an inert two-member canonical schema-2 archive with
   ordered physical IDs, labels and mappings, 100000 samples/s, 2048 pre and
   4096 post samples, rising D0, exact mode/dtype/count, and matching recorded
   SHA-256. Independent verification reconstructed every CSV byte-for-byte
   without using the implementation helper. Floating inputs were observational
   only and were not treated as acceptance criteria.
5. Independent focused artifact/recovery validation: 14 passed. Independent
   full non-hardware Python: 280 passed, 1 covered sandbox-only loopback skip,
   94 warnings; Ruff, mypy over 19 files, and CLI help passed.
6. Root accumulated gate: pip check, Ruff, mypy, 280 passed with 1 covered
   sandbox-only loopback skip and 94 warnings, CLI help, deterministic assets,
   pinned Node 22.14.0 lint/typecheck/unit/production build, brokered Playwright
   production smoke 1 passed, and `git diff --check` passed.

## Findings and dispositions

1. `C2B3-I001`: resolved; corrected D0-D23 defaults were fully reaccepted in
   B2 before the complete fresh physical sequence, and the 24-channel raw
   artifact contains complete ordered metadata.
2. `C2B3-V001`: resolved; independent raw-artifact integrity, settings, masks,
   dtypes, counts, timing, upper-byte, CSV, recovery, and sanitization checks
   passed.
3. `C2B3-A001`: no new acceptance finding; disposition closed by this verdict.

No finding is open.

## Sanitization, scope, and checkpoint decision

Committed evidence records the runtime port only as `<PORT_SUPPLIED>` and
retains no serial number, machine-local location, local URL, or capability
value. Raw runtime artifacts remain outside the repository. This audit did not
open USB, rerun hardware, or copy sensitive runtime values.

No firmware edit/build/flash, bootloader entry, Wi-Fi change, unknown-pin probe,
power cycle, persistent device action, C#/.NET or `.lac` action, public serving,
browser UI implementation, other capture mode, packaging/publication, future
batch implementation, or Cycle 3 action occurred or is authorized by this
acceptance.

Verdict is `pass`. The exact corrected candidate and complete fresh B3 evidence
satisfy the C2-B3 checkpoint-readiness gate. Only the orchestrator may now
create, validate, and commit the C2-B3 evidence manifest and append the B3
checkpoint before selecting C2-B4.
