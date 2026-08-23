# C2-B2 independent verification — round 1

- Verifier: `cycle2-verifier`
- Candidate commit: `49293f54a045cae08c8afcdada2e16bed33b0031`
- Candidate tree: `fcafa83000cdf85adb11decf5af286527242f20c`
- Date: 2026-08-23
- Verdict: **changes_required**

## Authority and scope

The current macOS-only Cycle 2 goal, orchestration and batch contracts; settled model/protocol/replay/CSV sections; B2 activation and implementor-replacement records; accepted B1 and Cycle 1 evidence; and checked-in V2 firmware were reviewed. The candidate product delta is confined to the authorized Python model, protocol, device, CLI, replay/CSV and implementation-test surfaces. No firmware, C#, web API/viewer, bus-analysis, decoder, packaging, public serving, hardware operation, or Cycle 3 change was found.

The checked-in Pico 2 authority selects `BOARD_PICO_2`, defines `CAPTURE_BUFFER_SIZE` as `128 * 3 * 1024` (393216 bytes) and `MAX_CHANNELS` as 24. The C request layout independently yields channels at offsets 6–29, channel count 30, alignment padding 31, frequency/pre/post 32/36/40, loop/measure 44/45, and `captureMode` 46 in the 48-byte payload. Firmware derives maximum word counts as buffer bytes divided by 1, 2, or 4.

## Independent results

- Literal request and response coverage passed for modes 0/1/2, reordered subsets, canonical zero slots/padding, little-endian words, one-byte fragmentation, malformed status, truncation, extra bytes, and nonzero timestamp contamination with receive-owner invalidation.
- Exact-type, uniqueness, physical range, trigger membership, negotiated channel/frequency/buffer bounds, mode dtype/rank/contiguity/count, and 24-bit upper-byte checks passed in the focused and accumulated suites.
- Schema 1 hostile/read compatibility and schema 2 deterministic round trips, canonical inert two-member NPZ, bounded headers/members/metadata, dtype/count/cross-field checks, and pickle prohibition passed.
- Generalized explicit-metadata CSV ordered-subset round trips, packed-position extraction, canonical timing, binary values, labels, and Cycle 1 exact export compatibility passed where exercised.
- Focused wider/replay run: 64 passed, one expected duplicate-member construction warning.
- Corrected independent verifier suite: 168 passed, 1 sandbox-only loopback skip, one expected duplicate-member warning.
- Full non-hardware suite: 251 passed, 94 warnings.
- Ruff passed; mypy passed 19 source files.
- Pinned Node 22 shell gates passed: lint, typecheck, one unit test, 26-module production build, asset drift check, and escalated loopback browser smoke (1 passed in 1.4 seconds). The initial sandbox browser start failure was environmental and was superseded by the successful authorized loopback run.

## Findings

### C2B2-V001 — verifier fixture expected obsolete schema-1 writes

Owner: verifier. The prior Cycle 1 artifact assertion required newly written replay metadata to remain schema 1 with `provisional=true`. The settled B2 contract instead requires new writes to be schema 2 while retaining schema-1 reads. The verifier-owned assertion was corrected to require schema 2 and absence of the provisional marker. This is a verifier-fixture correction, not a product defect, but it changes the verification tree and therefore requires a new immutable candidate and fresh verification.

### C2B2-V002 — verifier fixture rejected an approved seven-channel subset

Owner: verifier. The old Cycle 1 boundary parameter treated `(0,1,2,3,4,5,6)` as invalid. B2 explicitly permits every unique ordered subset of one through 24 physical channels. The stale rejection was removed and replaced with a positive seven-channel/mode-0 assertion. This verifier-tree change also requires a new candidate and fresh verification.

### C2B2-V003 — legacy CSV integer-rate inference is absent

Owner: implementor. A literal externally constructed three-row accepted Cycle 1 D0–D7 CSV with canonical `-0.01,0,0.01` timing and no supplied rate was rejected with `CSV sample rate must be supplied explicitly`. The settled CSV contract requires the exact legacy header to infer an integer rate when nonzero rows produce exactly one in-range candidate reproducing every canonical `.12g` cell; only zero/one-row input requires an explicit rate. Implement the bounded exact-decimal candidate algorithm and hostile/ambiguous/no-candidate tests.

### C2B2-V004 — required CLI CSV-import surface is absent

Owner: implementor. The production CLI exposes devices, info, capture, replay validation, hardware smokes, and web, but no CSV-import command or equivalent explicit import options. The settled contract states that CLI import requires explicit metadata equivalent to the browser form, and B2 owns the importer/necessary CLI exposure. Add a bounded CLI import surface preserving explicit paths, deterministic output, and established validation/I/O exit contracts.

## Disposition

Open findings are `C2B2-V001`, `C2B2-V002`, `C2B2-V003`, and `C2B2-V004`. The verifier owns V001/V002 and has made only those test corrections. The implementor owns V003/V004. No acceptance or B2 evidence manifest is authorized for this candidate. After all four corrections are committed into a new exact candidate, repeat independent B2 verification from scratch.
