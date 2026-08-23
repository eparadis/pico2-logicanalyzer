# Cycle 2 orchestration progress

This is the compact execution log for Cycle 2. Historical Cycle 1 progress and
accepted evidence remain unchanged.

## Initial repository state

- Recorded: 2026-08-22 (America/Los_Angeles)
- Branch: `python-rewrite`, four commits ahead of `origin/python-rewrite`
- Initial HEAD: `ce0b1ce89344af689558e965bfed9170db394e82`
- Initial tree: `f2c8eea5ef53c21e43a6f3a8de81d7645d34c4ae`
- Worktree: clean; no unrelated user changes recorded
- Approved contract commit: `7a5f429db93c2164ef54334c0eb3adf48ae68ff0`
- Approved contract tree: `eb52d5e8f16efd855b09b7672b532403c8454c19`
- Preparatory approval: three `pass` records in
  `docs/rewrite-reviews/cycle-2/final-round-2/` name that exact commit and tree
- Prohibited actions: none performed; firmware, C# applications, .NET, `.lac`,
  public serving, packaging/publication, persistent device state, and Cycle 3
  remain untouched

## C2-B1: Contracts, dependencies, workflow, and web shell

- State: In progress
- Objective: Establish the reproducible Python/React development and CI
  foundation, freeze the Cycle 2 data/API/security contracts, and provide a
  production-built loopback-only offline shell that starts and stops without
  serial access.
- Prerequisites: approved Cycle 2 contract commit and three common-commit
  passes; accepted Cycle 1 baseline; writable workspace. All are present.
- Implementation agent: `cycle2-implementor` (`/root/implementor`)
- Verification agent: `cycle2-verifier` (`/root/verifier`)
- Acceptance agent: `cycle2-acceptance` (`/root/acceptance`)
- In scope: B1 contracts and ADRs; strict Cycle 2 evidence schema and validator;
  optional locked Python web runtime; React/TypeScript/Vite shell and lock;
  deterministic committed assets/build manifest; loopback/Host/Origin/cookie
  security shell; canonical tests and commands; single Cycle 2 CI workflow;
  mechanical stale Cycle 1 wording corrections.
- Out of scope: wider model/codec, replay-schema-2 production I/O, capture API,
  waveform viewer behavior, physical I/O, Qt/Electron, `.lac`, .NET, firmware,
  packaging/public serving, and Cycle 3.
- Owned paths: implementor owns B1 product, implementation tests, locks, built
  assets, focused B1 documents, and the authorized workflow replacement;
  verifier owns separate B1 verification tests/fixtures and immutable verifier
  records; acceptance owns immutable acceptance records; orchestrator owns this
  progress log and the post-review B1 manifest/checkpoint.
- Authoritative evidence: `CYCLE2_ORCHESTRATION.md`,
  `CYCLE2_BATCH_EXECUTION.md`, approved discovery review, accepted Cycle 1
  completion/manifests/tests, exact preparatory review records, and applicable
  platform/tool documentation captured by the implementor.
- Acceptance evidence: clean Python 3.12 core and web-runtime installs; exact
  frontend lint/type/unit/build/browser commands; production offline shell and
  security negatives; missing-web-extra behavior; schema/secret-scanner tests;
  macOS/Linux exact-candidate CI; accumulated Cycle 1 non-hardware tests.
- Authority notes: locked dependency downloads and exact-candidate hosted-CI
  push may require normal execution approval. No serial, native hardware, or
  native interactive-browser action is authorized in B1.
- Risks and unknowns: dependency and supported Node/browser versions require
  clean probes; hosted CI evidence requires an exact-candidate push; neither
  permits scope expansion.

### Implementor identity change

- Original identity: `cycle2-implementor` (`/root/implementor`)
- Replacement identity: `cycle2-implementor-replacement-1`
  (`/root/implementor_replacement_1`)
- Reason: the original implementor exhausted its execution window while B1
  implementation work remained; it was not reassigned to review or acceptance.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- Verification and acceptance identities remain unchanged.

## Deferred work

- No deferred Cycle 2 finding recorded at B1 selection.

## Operator-approved platform requirement revision

- Recorded: 2026-08-23 (America/Los_Angeles)
- Authority: the operator directed removal of the active Linux requirements and
  workflows while preserving immutable historical records for possible future
  use.
- Active support scope: macOS only.
- Revised active artifacts: `CYCLE2_GOAL.md`,
  `CYCLE2_ORCHESTRATION.md`, `CYCLE2_BATCH_EXECUTION.md`, the Cycle 2
  workflow, and the Python client README support statement.
- Historical discovery, review, acceptance, CI, and evidence records remain
  unchanged. Their Linux references describe the requirements or results in
  force when those records were created; they are not current support claims.
- The prior uncommitted C2-B1 manifest was discarded before checkpoint
  finalization. C2-B1 must be reverified and reaccepted under the revised
  macOS-only contract before its manifest and checkpoint may be recorded.
- Future Linux support, if requested, requires a separately approved contract
  revision and new verification; historical records may be used as provenance
  but do not establish current support.

## C2-B1 checkpoint

- State: Complete
- Recorded: 2026-08-23T07:07:42Z
- Exact accepted candidate:
  `e266d88815b0dabdd1397cbfcf3e1187bf8dfc24`
- Exact accepted tree: `9ec8c3ef73e47c940fd686656708cfaa212d9058`
- Current support scope: macOS only
- Verification: pass, no open findings,
  `docs/reviews/c2-b1-verification-round-18.md`,
  SHA-256
  `28b3c6e8349982e3faec8517572cedc42e7086da12a3c3c5f6858d8149f08feb`
- Acceptance: pass, no open findings,
  `docs/reviews/c2-b1-acceptance-round-3.md`,
  SHA-256
  `c79618342a5c18b246c01e530fa35e67fc77afc11fabb9296349d06490dee957`
- Platform revision acceptance:
  `docs/reviews/cycle2-platform-revision-acceptance.md`,
  SHA-256
  `ae07e21b9038b0ad58a59b68801878a083710b6df1929ce672f8ab20833e5925`
- Accumulated validation: clean hash-locked core and web installs; Ruff; mypy;
  232 non-hardware tests; CLI; evidence security probes; Node 22.14.0
  lint/typecheck/unit/build; deterministic assets; Playwright 1.50.1 browser
  smoke; workflow, scope, rollback, and prohibited-action audits all passed.
- Hosted validation: run `32624529709` at the exact candidate; sole macOS job
  `97157701532` passed.
- Evidence manifest: `testdata/evidence/c2-b1.json`, committed separately,
  SHA-256
  `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0`
- Earliest proof recorded for stopping conditions 1, 2, 3, and 14; their final
  accumulated proof remains owned by C2-B6.
- Historical records from the superseded platform scope remain immutable and
  are not current support claims.
- Prohibited actions: none performed; firmware, C# applications, .NET, `.lac`,
  public serving, packaging/publication, persistent device state, and Cycle 3
  remain untouched.
- Next boundary: C2-B2 is not started. Execution is paused here by operator
  request.

## C2-B2: Wider capture domain, codec, replay, and CSV core

- State: Active
- Activated: 2026-08-23 (America/Los_Angeles)
- Activation HEAD: `873c4f631069d498812358c4ca13d86260028407`
- Activation tree: `cdd674e65cc8208a54dae401163f1de295e53238`
- Prerequisite: C2-B1 checkpoint complete; manifest
  `testdata/evidence/c2-b1.json` validates with SHA-256
  `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0`.
- Objective: safely represent, encode, parse, persist, import, export, and
  reload ordered one-to-24-channel normal captures across 8-, 16-, and 24-bit
  word modes.
- Implementation agent: `cycle2-implementor-replacement-1`
  (`/root/implementor_replacement_1`)
- Verification agent: `cycle2-verifier` (`/root/verifier`)
- Acceptance agent: `cycle2-acceptance` (`/root/acceptance`)
- In scope: generalized capture model and validation; 48-byte normal request
  and response codecs; literal golden/adverse fixtures; schema-2 replay with
  retained schema-1 reads and pre-materialization security bounds;
  deterministic self-timed CSV import/export; bounded CLI exposure and tests.
- Out of scope: physical I/O beyond fake transports, bus analysis, browser
  capture API or viewer, performance optimization, other firmware modes,
  decoders, firmware/C# changes, packaging/public serving, and Cycle 3.
- Ownership: the implementor owns B2 Python product code, focused
  implementation tests, literal/generated fixtures, and directly required
  focused documentation. The verifier owns independent B2 black-box/adverse
  tests and immutable review records. Acceptance owns immutable acceptance
  records. The orchestrator owns this progress log and the post-acceptance B2
  manifest/checkpoint.
- Authority inputs: current macOS-only governing contracts, the accepted B1
  manifest/checkpoint, settled Cycle 2 protocol/replay/CSV contracts, accepted
  Cycle 1 schema-1 and D0-D7 artifacts/tests, and checked-in firmware source as
  read-only protocol authority.
- Required accumulated gate: full non-hardware Python suite plus the locked
  frontend shell gates; no hardware, serial, or native interactive action is
  authorized in B2.
- Evidence lifecycle: no `c2-b2.json` exists or may be created until one exact
  candidate passes implementation checks, independent verification, complete
  accumulated macOS validation, and independent acceptance.

### C2-B2 implementor identity change

- Original B2 identity: `cycle2-implementor-replacement-1`
  (`/root/implementor_replacement_1`)
- New replacement identity: `cycle2-implementor-replacement-2`
- Reason: the first replacement preserved partial B2 work but twice ended a
  continuation turn without advancing or producing the required complete
  candidate.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- Existing uncommitted B2 product and implementation-test changes remain in the
  shared worktree for the new replacement to inspect, validate, correct, and
  complete. No partial candidate is accepted.
- Verification and acceptance identities remain unchanged.

### C2-B2 second implementor identity change

- Prior identity: `cycle2-implementor-replacement-2`
  (`/root/implementor_replacement_2`)
- New replacement identity: `cycle2-implementor-replacement-3`
- Reason: the prior agent became unavailable during the round-one correction
  iteration while scoped CLI, CSV, and implementation-test changes remained
  uncommitted in the shared worktree.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- The replacement must inspect and validate the inherited changes against
  `docs/reviews/c2-b2-verification-round-1.md`; no partial correction is
  accepted by inheritance.
- Verification and acceptance remain distinct fixed lanes.

### C2-B2 verifier identity change

- Original identity: `cycle2-verifier` (`/root/verifier`)
- Replacement identity: `cycle2-verifier-replacement-1`
- Reason: the original verifier became unavailable after completing and
  durably recording C2-B2 verification round 1.
- Lane/model/reasoning preserved: Verifier, `gpt-5.6-sol`, low.
- The replacement begins a fresh independent round against the new immutable
  candidate and may rely on the prior immutable record only as finding
  provenance, not as transferred acceptance.
- Implementation and acceptance identities remain distinct.

### C2-B2 second verifier identity change

- Prior identity: `cycle2-verifier-replacement-1`
- New replacement identity: `cycle2-verifier-replacement-2`
- Reason: the first replacement became unavailable after leaving an
  uncommitted round-two review record without a compact verdict handoff.
- Lane/model/reasoning preserved: Verifier, `gpt-5.6-sol`, low.
- The new replacement must independently reconcile the exact candidate and the
  uncommitted record; the record is not accepted merely because it exists.
- Implementation and acceptance identities remain distinct.

### C2-B2 third implementor identity change

- Prior identity: `cycle2-implementor-replacement-3`
- New replacement identity: `cycle2-implementor-replacement-4`
- Reason: the prior implementor completed its candidate handoff and then became
  unavailable before round-two product corrections were assigned.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- The replacement owns only product findings in the immutable round-two review
  and starts from the current clean descendant containing review/progress
  records.
- Verification and acceptance identities remain distinct.

### C2-B2 acceptance identity change

- Original identity: `cycle2-acceptance` (`/root/acceptance`)
- Replacement identity: `cycle2-acceptance-replacement-1`
- Reason: the original acceptance agent is no longer available before the B2
  exact candidate entered independent acceptance.
- Lane/model/reasoning preserved: Acceptance, `gpt-5.6-sol`, low.
- The replacement audits exact candidate
  `c3f43a9ef0311c34ece3f95c94871fcfcd2c12a3`, tree
  `782f101981348ebdde23a338c8db5a92eb81f73b`, from a fresh acceptance
  assignment. Verification and implementation evidence does not transfer
  acceptance authority.

### C2-B2 exact-candidate accumulated validation

- Candidate: `c3f43a9ef0311c34ece3f95c94871fcfcd2c12a3`; tree
  `782f101981348ebdde23a338c8db5a92eb81f73b`.
- Independent verification: pass with no open findings; round 3 record SHA-256
  `765e00cfe542ce29f712bf433b05e99c7175500b9bacb4cc5868348c98caa85a`.
- Clean core: Python 3.12.13; hash-locked install; `pip check`, Ruff, and mypy
  (19 source files) passed; non-hardware pytest reported 265 passed, 1 skipped,
  and 94 warnings; CLI help passed and exposed `csv-import`. The sandbox-only
  loopback skip is covered by the separately authorized production browser
  smoke below.
- Locked frontend: official Node 22.14.0 archive SHA-256
  `6698587713ab565a94a360e091df9f6d91c8fadda6d00f0cf6526e9b40bed250`;
  clean `npm ci` installed 215 packages; lint, typecheck, one Vitest unit test,
  production Vite build, and deterministic asset validation passed; Playwright
  1.50.1 production-shell smoke passed 1 test.
- Lock/evidence inputs: `requirements-dev.lock` and `requirements-web.lock`
  SHA-256 `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
  `web/package-lock.json` SHA-256
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
  `web/production-assets.json` SHA-256
  `1d1b44794eed6f288f1140e67c1520d847fb3263718672cf743ff70b9da0ece9`.
- Repository hygiene: asset drift check and `git diff --check` passed; generated
  browser residue was removed; no hardware, serial, firmware, .NET, persistent
  state, public-server, packaging/publication, or Cycle 3 action occurred.
- B2 requires the complete local non-hardware Python/frontend shell gate; a
  separate exact-candidate hosted-CI run is not an owning B2 acceptance item.
  Hosted macOS CI remains mandatory for the final candidate at C2-B6.

## C2-B2 checkpoint

- State: Complete
- Recorded: 2026-08-23T15:38:59Z
- Exact accepted candidate:
  `c3f43a9ef0311c34ece3f95c94871fcfcd2c12a3`
- Exact accepted tree: `782f101981348ebdde23a338c8db5a92eb81f73b`
- Verification: pass, no open findings,
  `docs/reviews/c2-b2-verification-round-3.md`, SHA-256
  `765e00cfe542ce29f712bf433b05e99c7175500b9bacb4cc5868348c98caa85a`.
- Acceptance: pass, no open findings,
  `docs/reviews/c2-b2-acceptance-round-1.md`, SHA-256
  `b5eca46652d8449438be5d228a055aad91f8e9dcb8ac5221295df6785ab3fdc8`.
- Accumulated validation: clean locked Python 3.12.13 install; pip check;
  Ruff; mypy; 265 passed and 1 covered sandbox skip in the orchestrator
  non-hardware run; CLI; clean Node 22.14.0 install; lint; typecheck; unit;
  production build; deterministic assets; and Playwright production smoke all
  passed. Independent verification separately ran 266 non-hardware tests with
  no skip.
- Evidence manifest: `testdata/evidence/c2-b2.json`, committed separately at
  `ff8c978`, SHA-256
  `6e3a42fa4955e17c39a3c13fe09613327d21b572696fd3ecd69d485a3bd21b2a`;
  strict validation and the 9-test evidence-schema suite passed.
- Checkpoint proof records stopping conditions 4 and 6 and the B2-owned portion
  of condition 5. Their final accumulated audit remains owned by C2-B6.
- Prohibited actions: none performed; no hardware or serial access, firmware,
  C# or .NET change/execution, public serving, persistent device state,
  packaging/publication, or Cycle 3 work occurred.
- Next boundary: C2-B3 remains pending until the operator supplies every fresh
  hardware, electrical, mapping, firmware-identity, idle-input, and explicit
  serial-port confirmation required by the governing contracts. No physical
  I/O is authorized before that confirmation.

## C2-B3: Physical byte-boundary capture gate

- State: Ready
- Selected: 2026-08-23 (America/Los_Angeles)
- Selection HEAD: `4919c52432e76070c2b65c579466a53dcb769fc9`
- Selection tree: `4dd57406c729032b692b52f16411d231802ffe15`
- Objective: prove genuine protected Pico 2 normal captures through the 8-, 16-,
  and 24-bit byte boundaries while retaining the accepted Cycle 1 identity,
  recovery, reopen, and second-capture paths without a power cycle.
- Prerequisite present: C2-B2 checkpoint complete; manifest
  `testdata/evidence/c2-b2.json` strictly validates with SHA-256
  `6e3a42fa4955e17c39a3c13fe09613327d21b572696fd3ecd69d485a3bd21b2a`.
- Missing operator prerequisite: none.
- Implementation agent: `cycle2-implementor-replacement-4`
- Verification agent: `cycle2-verifier-replacement-2`
- Acceptance agent: `cycle2-acceptance-replacement-1`
- In scope after confirmation: accepted Cycle 1 identity/recovery regression;
  simultaneous protected-source captures of D0-D7, D0-D15, and D0-D23;
  independently checked masks, dtypes, counts, timing, activity, zero upper
  byte, artifacts, reopen, and reuse.
- Out of scope: firmware changes or flashing, bootloader entry, probing unknown
  pins, requiring floating inputs to remain zero, browser UI, other capture
  modes, performance-limit exploration, persistent-state change, and Cycle 3.
- Ownership: implementor owns bounded physical capture execution and sanitized
  implementation evidence after confirmation; verifier owns independent raw
  artifact checks and immutable review records; acceptance owns immutable
  acceptance records; orchestrator owns operator confirmation, accumulated
  validation, manifest, and checkpoint.
- Authority note: no serial open, device request, wiring transition, capture,
  cancellation, or other physical I/O is authorized until every missing
  operator prerequisite above is explicitly confirmed. Port and capability
  values must be sanitized in committed evidence.
- Independent later-batch work cannot advance because C2-B4 requires accepted
  B2 schemas plus the B3 physical artifacts. No later-batch implementation is
  started while this prerequisite is pending.

### C2-B3 read-only preflight

- Checked-in firmware authority is present and unchanged by Cycle 2 product
  work. `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Build_Settings.cmake` selects
  `BOARD_PICO_2`; `CMakeLists.txt` maps it to `pico2` and defines firmware
  version `V6_0`.
- Firmware authority SHA-256 values: build settings
  `2a80e102a89bae1b554afb2df3d9aec96b955f1cf6b1edd1794873e92ea3297b`;
  CMake configuration
  `93263c2402dfc44595555570d252c025c5da743e283cb917ca200c4338b3e662`;
  command source
  `6039a08c07e364a2aaa519561ee80f02b7caa5707b5ce31512a15c59cf06e32e`;
  capture source
  `c0cb981ec60fc780fbc5e98a76ccfcb290756b7eca5224e5d7a10a27454b0d8a`;
  protocol structures
  `0180750a5b9327da346b730d58c044ddd9f24d8a9dc66c542aab5142e46c8b6b`.
- Accepted Cycle 1 recovery baseline remains present at
  `testdata/evidence/c1-b5-recovery-smoke.json`, SHA-256
  `44a7bffc0bcc7c415ba8fa09efb26624853dce26833216d78d408b9c45907815`;
  it records the sanitized `LOGIC_ANALYZER_PICO_2_V6_0` identity, fixed-low
  D1/GPIO3 recovery, re-identification, and a successful second capture.
- Source-installed CLI read-only help passed for `capture`, `hardware-smoke`,
  and `hardware-recovery-smoke`. `capture` exposes explicit ordered physical
  channels plus finite timeout and explicit output paths; the recovery command
  exposes explicit idle channel/level and bounded cancel/timeout settings.
- No device enumeration, serial open, device request, capture, wiring change,
  firmware build/flash, bootloader entry, or persistent operation occurred.
  Operator confirmation remains the only missing B3 prerequisite.

### C2-B3 blocked audit

- The same complete operator-confirmation prerequisite remained absent for
  three consecutive durable-goal turns.
- All safe read-only preflight work is complete. C2-B3 cannot perform physical
  I/O without the confirmation, and C2-B4 cannot begin without accepted B3
  physical artifacts. Simulated, historical, or partial confirmation cannot
  replace fresh operator authority.
- Resume condition: the operator explicitly supplies every item listed under
  `Missing operator prerequisite` above. On resume, recheck the exact repository
  state and treat any later repeated blocker under a fresh blocked audit.

### C2-B3 operator confirmation after resume

- Confirmed: the approximately 1 kHz signal is connected simultaneously to
  board-labeled pins 1, 9, 17, and 24, corresponding respectively to logical
  analyzer signals D0, D8, D16, and D23.
- Confirmed by the operator's statement that all other connections remain the
  same as the accepted prior setup and are correct: integrated LogicAnalyzerV2
  protection; 3.3 V VRef; common analyzer ground; all four destinations as
  analyzer inputs; safe source fan-out to their high-impedance load; and the
  prior D1/GPIO3 fixed-low analyzer-ground recovery connection.
- Not inferred from connection state: serial-port identity and the current
  board/firmware identity remain explicitly required before any physical I/O.
- The prior blocked state is reopened as Pending. This resume starts a fresh
  repeated-blocker audit if the remaining prerequisite is not supplied.

### C2-B3 resumed blocked audit

- The explicit serial port and current Pico 2/fixed checked-in V2 firmware
  identity confirmation remained absent for three consecutive resumed goal
  turns.
- Wiring and electrical confirmation remains accepted, but it does not grant
  authority to infer a machine-local port or current firmware identity.
- No safe independent work remains: physical I/O requires both confirmations,
  and C2-B4 requires accepted B3 physical artifacts.
- Resume condition: the operator supplies the explicit serial port and confirms
  the attached Raspberry Pi Pico 2 is running the fixed checked-in V2 firmware
  built with `BOARD_TYPE=BOARD_PICO_2`.

### C2-B3 authorized port discovery

- The operator explicitly authorized the source-installed `pico-la devices`
  command to discover candidate serial ports.
- `pico-la devices --json` exited 0 and returned exactly one candidate described
  as `LogicAnalyzer`. Its machine-local port, location, and serial number are
  retained only as runtime inputs and will be committed as `<PORT_SUPPLIED>` or
  otherwise redacted.
- No serial port was opened and no identity request or capture was issued by
  discovery. The port prerequisite is satisfied for runtime execution.
- The prior blocked state is reopened as Pending. Current Pico 2/fixed V2
  firmware confirmation remains required before opening the discovered port.

### C2-B3 board and firmware confirmation

- The operator explicitly confirmed that the attached board is a Raspberry Pi
  Pico 2 running the checked-in V2 firmware.
- Together with the recorded checked-in build authority selecting
  `BOARD_TYPE=BOARD_PICO_2`, the discovered single `LogicAnalyzer` candidate,
  and the accepted wiring/electrical confirmation, every B3 operator
  prerequisite is satisfied.
- State advances to Ready. Bounded identity and physical capture operations are
  authorized on the discovered runtime port; committed evidence must sanitize
  it as `<PORT_SUPPLIED>` and must not contain serial numbers or machine-local
  location values.

### C2-B3 bounded identity result

- The root used the approved source-installed `pico-la info` command with a
  finite 10-second application timeout on the discovered runtime port.
- Identity passed: `LOGIC_ANALYZER_PICO_2_V6_0`; reported capabilities are 24
  channels, 393216-byte buffer, 200000000 Hz maximum capture frequency, and
  400000000 Hz blast frequency.
- The runtime port and device serial/location values remain uncommitted and
  must be represented as `<PORT_SUPPLIED>` or redacted in durable evidence.
- This read-only identity request made no firmware, bootloader, Wi-Fi, power,
  wiring, or persistent-state change.

### C2-B3 physical implementation finding and B2 reopen

- Runtime recovery regression exited 0. The bounded 8-channel and 16-channel
  physical capture commands succeeded, but this partial evidence is not
  accepted or checkpointed independently.
- The required ordered D0-D23 capture failed before artifact creation with exit
  3 and `invalid channel labels or mappings`.
- Finding `C2B3-I001`: the accepted B2 generalized CLI/model path does not
  currently admit the contract-required 24-channel default-label/mapping
  request. This is a product defect in the earliest B2-owned interface, not an
  electrical or operator-input failure.
- C2-B2 is reopened for a focused failing test and bounded correction by the
  implementation lane. Any correction requires a new immutable candidate,
  fresh independent B2 verification, the complete accumulated validation, and
  fresh acceptance before B3 can rerun its entire physical sequence.
- No 8/16/recovery partial pass transfers to the corrected candidate. The
  runtime artifacts remain uncommitted and do not constitute B3 evidence.
- No firmware, bootloader, Wi-Fi, power-cycle, persistent-state, .NET,
  public-server, packaging/publication, or Cycle 3 action occurred.

### C2B3-I001 correction candidate

- Implementation identity: `cycle2-implementor-replacement-5`.
- Candidate: `90adb3adb38a938ce470fa854e6fc7b98e1501c9`; tree
  `5a09d57e4caa266a43f164edaffc94fc9a3236d7`.
- Bounded correction: generalized default capture-result labels/mappings no
  longer stop at eight entries; exact D0-D23 CLI/config construction is covered
  while wrong-length and duplicate labels remain rejected.
- Implementation gates: 35 focused tests; Ruff; mypy over 19 files; 266 passed
  and 1 sandbox-loopback skip in non-hardware Python; CLI help; frontend lint,
  typecheck, unit, and production build; and `git diff --check` passed.
- The browser smoke could not start its local server inside the implementation
  sandbox and is not credited. Root accumulated validation must run it under
  the existing centralized loopback/browser approval.
- The untracked B3 physical-validation helper remains outside this product
  candidate. No physical result transfers to the corrected candidate.

### C2-B2 reopened verifier identity change

- Prior identity: `cycle2-verifier-replacement-2`.
- New replacement identity: `cycle2-verifier-replacement-3`.
- Reason: the prior verifier is no longer available when physical finding
  `C2B3-I001` reopens the B2 interface and creates a new immutable candidate.
- Lane/model/reasoning preserved: Verifier, `gpt-5.6-sol`, low.
- The replacement must independently verify the entire exact corrected
  candidate and prior B2 finding dispositions; no prior verification or partial
  physical pass transfers.

### C2-B2 reopened verification and accumulated validation

- Corrected candidate: `90adb3adb38a938ce470fa854e6fc7b98e1501c9`;
  tree `5a09d57e4caa266a43f164edaffc94fc9a3236d7`.
- Independent verification: pass with no open findings; round 4 record
  `docs/reviews/c2-b2-verification-round-4.md`, SHA-256
  `56f5a99c0d34464ae09081145ef2b9d1378e6b6c792276152515cb3dc47e443a`.
- Independent results: 45 focused tests; 276 passed and 1 covered sandbox skip
  in full non-hardware Python; Ruff; mypy over 19 files; CLI; Node 22.14.0
  lint/typecheck/unit/build/assets; and brokered Playwright smoke all passed.
- Root accumulated results: pip check; Ruff; mypy over 19 files; 276 passed and
  1 covered sandbox-loopback skip with 94 warnings; CLI help; deterministic
  assets; Node 22.14.0 lint/typecheck/one unit/production build; brokered
  Playwright production-shell smoke 1 passed; and `git diff --check` passed.
- The untracked B3 validation helper is excluded from the product candidate and
  does not affect the accumulated product gate. No hardware result transfers.

### C2-B2 reopened acceptance identity change

- Prior identity: `cycle2-acceptance-replacement-1`.
- New replacement identity: `cycle2-acceptance-replacement-2`.
- Reason: the prior acceptance lane is no longer available when C2B3-I001
  requires fresh acceptance of the corrected B2 candidate.
- Lane/model/reasoning preserved: Acceptance, `gpt-5.6-sol`, low.
- The replacement must audit the exact corrected candidate, fresh round-4
  verification, complete accumulated gate, scope, and the prior B2 checkpoint
  reopening. No earlier acceptance transfers.

### C2-B2 corrected-candidate recheckpoint

- State: Complete
- Corrected accepted candidate:
  `90adb3adb38a938ce470fa854e6fc7b98e1501c9`
- Corrected accepted tree: `5a09d57e4caa266a43f164edaffc94fc9a3236d7`
- Physical finding `C2B3-I001`: accepted closed; the exact D0-D23 default
  label/mapping path now passes while malformed metadata remains rejected.
- Verification: pass, no open findings,
  `docs/reviews/c2-b2-verification-round-4.md`, SHA-256
  `56f5a99c0d34464ae09081145ef2b9d1378e6b6c792276152515cb3dc47e443a`.
- Acceptance: pass, no open findings,
  `docs/reviews/c2-b2-acceptance-round-2.md`, SHA-256
  `9930b43a96adcbebfa4670f3c01507c5c5bc89e2bf7640a953fdb9a0f1fa2d3e`.
- Complete accumulated Python/frontend/browser validation passed as recorded
  above; no earlier verification, acceptance, or partial hardware result was
  transferred.
- Updated active evidence manifest: `testdata/evidence/c2-b2.json`, committed
  separately at `5f5eebb`, SHA-256
  `d930bce4ae20576ea030e35cf0e993a3caf89e95f5eb5195638471c1790c2be4`;
  strict validation and the 9-test evidence-schema suite passed.
- Git history preserves the superseded accepted B2 manifest/checkpoint as
  immutable historical evidence; it no longer identifies the active product
  candidate after the physical finding.
- C2-B3 is authorized to restart its entire physical sequence against the
  corrected candidate. No prior recovery, 8-channel, or 16-channel runtime pass
  transfers.

### C2-B3 implementation identity change

- Prior identity: `cycle2-implementor-replacement-4`
- New replacement identity: `cycle2-implementor-replacement-5`
- Reason: the prior B2 implementor lane is no longer available when the
  operator-authorized B3 physical gate becomes executable.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- State advances to In progress for the bounded physical procedure. Verification
  and acceptance remain separate and will receive fresh same-lane replacements
  if their prior identities are unavailable.

### C2-B3 corrected-candidate implementation result

- Corrected product candidate:
  `90adb3adb38a938ce470fa854e6fc7b98e1501c9`; tree
  `5a09d57e4caa266a43f164edaffc94fc9a3236d7`.
- Implementation evidence commit: `cdea2946f18e111db31c60b25efd0f53132ddbda`;
  evidence tree `4415fc8a0131ece3c889b041ac642a3c4fe28a45`.
- Recovery: bounded fixed-low D1 cancellation/drain, close/reopen,
  re-identification, and second 6144-sample D0 capture passed without a power
  cycle; 41 rising transitions measured 1000.0 Hz.
- D0-D7: `uint8`, 6144 samples, driven mask `0x01`, all-low/all-high driven
  projections, 42 rising transitions, 1005.641403 Hz.
- D0-D15: `uint16`, 6144 samples, driven mask `0x0101`, all-low/all-high driven
  projections, 42 rising transitions, 1010.349926 Hz.
- D0-D23: `uint32`, 6144 samples, driven mask `0x810101`, all-low/all-high driven
  projections, 42 rising transitions, 1005.394801 Hz, and bits 24-31 zero.
- Independent implementation helper reconstructed byte-exact deterministic CSV
  from each raw schema-2 artifact. Helper
  `scripts/validate_c2_b3_capture.py` SHA-256
  `993f9c7691f9ded4b70049e5fe685d2fc2d5b20c430d999fab74e654b19cd5ec`;
  sanitized record `docs/reviews/c2-b3-implementation-round-1.md` SHA-256
  `2549b62755eec859bf34954d1f8a612e8be77bdba6e12fc88a6a5d4dd2dff27e`.
- Focused/accumulated implementation gates: 45 focused; Ruff; mypy; 276
  non-hardware passed with 1 covered sandbox skip; CLI; frontend
  lint/typecheck/unit/build; and diff check passed.
- Runtime raw artifacts remain outside the repository for independent verifier
  inspection. Durable artifacts contain no port, serial, location, or
  capability values. State advances to Verifying; no result is accepted yet.

### C2-B3 independent verification and accumulated validation

- Independent verification identity: `cycle2-verifier-replacement-3`.
- Verdict: pass with no open findings; record
  `docs/reviews/c2-b3-verification-round-1.md`, SHA-256
  `ebeee036728cada9a9046fdcdee4e4a356955a5e3a1a3f10d075ba66ff4fad78`.
- The verifier independently read all seven runtime recovery/CSV/NPZ artifacts,
  matched their digests, derived exact dtypes/counts/masks/transitions,
  reconstructed every CSV byte-for-byte without the implementation helper,
  proved the 24-bit upper byte zero, and audited bounded recovery,
  reopen/re-identification, and the second capture.
- Independent focused artifact/recovery suite: 14 passed. Full non-hardware:
  280 passed and 1 covered sandbox-loopback skip. Ruff, mypy over 19 files, and
  CLI help passed.
- Root accumulated gate: pip check; Ruff; mypy; 280 non-hardware passed with 1
  covered sandbox-loopback skip and 94 warnings; CLI help; deterministic assets;
  Node 22.14.0 lint/typecheck/one unit/production build; Playwright production
  smoke 1 passed; and `git diff --check` passed.
- Verification test
  `tests/verification/test_c2_b3_physical_artifacts_blackbox.py` SHA-256
  `cbf2bf036e6edfe264964f6ab286cf993e5577573abb951a9027cc9243e2d8d1`.
- No additional USB operation, firmware/persistent action, power cycle, or
  sensitive durable value occurred during verification/accumulated validation.
  C2-B3 is ready for fresh independent acceptance of this complete gate.

## C2-B3 checkpoint

- State: Complete
- Exact accepted product candidate:
  `90adb3adb38a938ce470fa854e6fc7b98e1501c9`
- Exact accepted product tree: `5a09d57e4caa266a43f164edaffc94fc9a3236d7`
- Implementation: pass; sanitized record
  `docs/reviews/c2-b3-implementation-round-1.md`, SHA-256
  `2549b62755eec859bf34954d1f8a612e8be77bdba6e12fc88a6a5d4dd2dff27e`.
- Verification: pass with no open findings; record
  `docs/reviews/c2-b3-verification-round-1.md`, SHA-256
  `ebeee036728cada9a9046fdcdee4e4a356955a5e3a1a3f10d075ba66ff4fad78`.
- Acceptance: pass with no open findings; record
  `docs/reviews/c2-b3-acceptance-round-1.md`, SHA-256
  `5e2eba90c93b610220fb77105bbed968374a5a375739e85142b45d385a508985`.
- Accepted physical proof: fixed V2 identity; complete fresh recovery and
  D0-D7/D0-D15/D0-D23 sequence; exact masks `0x01`, `0x0101`, `0x810101`;
  `uint8`/`uint16`/`uint32`; 6144 samples each; approximately 1 kHz activity;
  both driven states; zero bits 24-31; deterministic CSV; bounded recovery,
  reopen/re-identification, and second capture without a power cycle.
- Accumulated gate: 280 non-hardware passed with 1 covered sandbox skip; Ruff;
  mypy; CLI; assets; Node 22 lint/typecheck/unit/build; Playwright; and diff
  check passed.
- Evidence manifest: `testdata/evidence/c2-b3.json`, committed separately at
  `4635bf4`, SHA-256
  `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`;
  strict validation and the 9-test evidence-schema suite passed.
- Checkpoint proves stopping conditions 8 and 9 and refreshes B3-owned rollback
  proof for condition 14; final accumulated audit remains owned by C2-B6.
- Runtime port/serial/location and raw artifacts remain uncommitted. No firmware,
  bootloader, Wi-Fi, power-cycle, persistent-state, .NET, public-server,
  packaging/publication, or Cycle 3 action occurred.
- Next boundary: C2-B4 may begin against the accepted B2 schemas and B3 physical
  artifacts.

## C2-B4: Parallel-bus core and versioned browser API

- State: Ready
- Activated: 2026-08-23 (America/Los_Angeles)
- Activation HEAD: `1fe22ffaadbaefd0bc3fafa22e4723388a6b4c30`
- Activation tree: `9037e8e85de6c12524f963f310e929f126be9b05`
- Objective: implement deterministic transition and distinct-strobe sampled
  parallel-bus analysis plus a bounded, secured, versioned loopback API that
  exposes shared Python capture/replay/export/bus authority without serial I/O.
- Prerequisites: corrected C2-B2 checkpoint complete; C2-B3 physical checkpoint
  complete; `testdata/evidence/c2-b3.json` strictly validates with SHA-256
  `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`.
- Implementation agent: `cycle2-implementor-replacement-5`.
- Verification agent: `cycle2-verifier-replacement-3`.
- Acceptance agent: `cycle2-acceptance-replacement-2`.
- In scope: pure Python transition and distinct-strobe bus analysis and
  deterministic CSV; versioned health/readiness, bounded replay/CSV import,
  capture metadata/channel/waveform/bus/export/operation/cancel/shutdown API;
  loopback/canonical-Origin/capability-cookie/Host/WebSocket/file-transfer and
  concurrency boundaries; reviewed schema and generated/validated TypeScript
  types; fake/replay/API tests and accumulated headless shell gates.
- Out of scope: real serial API, device opening, complete viewer interaction,
  performance thresholds, native browser acceptance, remote serving, TLS,
  multi-user authentication, decoders, firmware/C# changes, packaging, and
  Cycle 3.
- Ownership: implementation owns B4 Python product/API/schema, corresponding
  TypeScript API types, focused tests/fixtures, and implementation records;
  verifier owns independent bus/security/API fixtures/tests and immutable
  records; acceptance owns immutable acceptance records; orchestrator owns
  integration, accumulated validation, manifest, and checkpoint.
- Authoritative evidence: settled bus/API/security/file-transfer contracts,
  accepted B2 schema/CSV behavior, accepted B3 8/16/24 physical semantics and
  sanitized evidence, standards-based loopback/origin/cookie behavior, and
  independently fixed literal bus samples.
- Acceptance evidence: independent LSB-first transition/strobe fixtures;
  deterministic bus CSV; exact API/schema/type agreement; bounded hostile
  imports/windows/rows/connections; token/origin/Host/WebSocket negatives;
  no-path upload/download and cleanup; conflict/cancel/disconnect behavior;
  accumulated Python/frontend/headless-browser gates with no serial open.
- Authority notes: dependency downloads and loopback/browser execution use the
  normal centralized approval broker. No USB, hardware, firmware, .NET,
  persistent-state, public-server, or future-batch action is authorized.
- Risks: shared Python/API/TypeScript interfaces remain single-writer; any
  unsettled substantive choice must return for contract/operator direction
  rather than expanding scope.

### C2-B4 shared-interface contract gap

- State: In progress
- Implementation completed only an uncommitted focused bus-core slice with 3
  passing tests, then stopped before API work or candidate creation.
- Independent read-only verifier verdict: `contract_gap`. The governing sources
  settle B4 bus semantics, loopback/Host/Origin/capability-cookie/file/security
  invariants, bounds classes, required resources, and schema/type drift
  enforcement, but do not settle exact routes/methods/statuses, JSON and
  multipart shapes, waveform/bus/export representations, operation lifecycle,
  WebSocket inclusion, numeric limits, or schema/type generation format.
- Minimal alternatives: REST plus polling with OpenAPI 3.1; REST plus polling
  with a JSON-Schema bundle and route manifest; or REST plus a secured WebSocket
  progress stream. The last materially enlarges B4 security, reconnect,
  ordering, and cleanup work.
- Verifier recommendation: REST plus polling; omit WebSockets; freeze one
  Python-owned OpenAPI 3.1 document with closed schemas and generated/validated
  TypeScript types. Retain existing health/readiness/shutdown routes and add
  bounded multipart imports, capture metadata/channels/waveform resources,
  paginated transition/strobe bus analysis, direct byte exports, and explicit
  polling/cancel operation states with one redacted error envelope.
- Operator direction is required before defining this shared Python/API/
  TypeScript interface. A three-reviewer governing-contract revision is not
  required for an operator-selected interface that remains within B4 and is
  frozen in a new machine-readable B4 contract under normal independent
  implementation/verification/acceptance. Editing the governing contracts,
  weakening security, requiring WebSockets, or expanding scope would require
  the common-commit review process.
- No API implementation, server launch, dependency change, candidate, or
  prohibited action occurred. The uncommitted bus core is preserved but is not
  accepted evidence.

### C2-B4 interface-decision blocked audit

- The same operator decision remained absent for three consecutive durable-goal
  turns after the independent verifier confirmed the substantive contract gap.
- All safe work outside the unsettled shared interface is exhausted. The
  partial bus core is not a candidate, B4 cannot implement or freeze the
  Python/API/TypeScript boundary without direction, and B5 cannot begin before
  B4 is accepted.
- Resume condition: the operator selects the recommended REST plus polling with
  Python-owned OpenAPI 3.1 and generated/validated TypeScript types, selects one
  of the documented alternatives, or supplies another in-scope interface for
  independent review. A resumed run starts a fresh blocked audit.

### C2-B4 operator-approved shared interface

- The operator approved the verifier-recommended interface after the documented
  blocked decision gate.
- Approved architecture: REST plus polling; no WebSockets; one Python-owned
  OpenAPI 3.1 document with closed schemas and generated/validated TypeScript
  types.
- Approved resource boundary: retain existing versioned health, readiness, and
  shutdown routes; add bounded multipart replay/CSV import with a single
  artifact part and CSV-only metadata part; capture metadata and channels;
  transition-reduced bounded waveform windows; closed transition/strobe bus
  requests with bounded pagination; direct deterministic byte exports with
  generated safe filenames/headers; and explicit polling/cancel operation
  states `pending`, `running`, `cancelling`, `succeeded`, `failed`, and
  `cancelled`.
- Approved error/security boundary: one closed redacted error envelope; opaque
  process-local identifiers with no filesystem meaning; no server paths,
  persistent import/export files, capability values, URL credentials, wildcard
  CORS, remote deployment, or WebSocket surface. Existing canonical
  Host/Origin/capability-cookie and bounded-request guarantees remain mandatory.
- Exact route/method/schema details and numeric limits must be frozen in the
  machine-readable OpenAPI artifact and independently verified against the
  approved Cycle 2 bounds; they may not weaken or expand the governing
  contracts.
- B4 reopens as In progress. The preserved uncommitted bus core remains
  implementation-lane work and receives no acceptance by inheritance.

### C2-B4 implementation identity change

- Prior identity: `cycle2-implementor-replacement-5`.
- New replacement identity: `cycle2-implementor-replacement-6`.
- Reason: after the operator resolved the shared-interface decision, the prior
  lane acknowledged the durable decision but ended without advancing the
  preserved partial bus core or beginning the required API/schema work.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- The replacement inherits the uncommitted bus-core files only as work to
  inspect, validate, correct, and complete. They are not accepted by
  inheritance and no partial candidate exists.
- Verification and acceptance identities remain distinct and unchanged.

### C2-B4 implementation candidate

- Implementation identity: `cycle2-implementor-replacement-6`.
- Exact product candidate: `296feec8d9a6441b0194fa95c06128be173d234e`;
  tree `660a1f3d7689002c588c583591d8bf30b589d09f`.
- Implemented complete scoped bus analysis, bounded secured REST/polling API,
  Python-owned OpenAPI 3.1 closed schemas, deterministic schema checker, and
  generated/validated TypeScript types. No WebSocket or serial surface exists.
- Focused implementation: 17 passed and 1 sandbox-loopback skip. Full Python:
  283 passed and 2 sandbox-loopback skips. Ruff, mypy, OpenAPI/type drift, CLI,
  Node lint/type/unit/build, and diff checks passed.
- OpenAPI SHA-256
  `d4ed2aeb0c4181858002b057b3b44f1a90d14d3a4125a5bb6587f5b229a2c3a2`;
  generated TypeScript SHA-256
  `acb72dad34116e7b562da3e5f6afea8f608aa73573b8127d433fba2f823de734`;
  checker SHA-256
  `0bfdec71e13fd9edec13a80d8455bccb26aaf6519e824c10feef87132d4309e9`.
- Immutable implementation record committed separately at `28032cf`:
  `docs/reviews/c2-b4-implementation-round-1.md`, SHA-256
  `5735ad3c47b8f3dc7fcf18f6a3a8a981d3e08e4c2e867ab924b948ffbd5ccee2`.
- Loopback/browser skips are not credited and remain for independent/root
  brokered execution. No device, firmware, persistent-state, public-server,
  .NET, packaging/publication, B5/B6 feature, or Cycle 3 action occurred.

### C2-B4 verification round 1

- Candidate: `296feec8d9a6441b0194fa95c06128be173d234e`; tree
  `660a1f3d7689002c588c583591d8bf30b589d09f`.
- Verification identity: `cycle2-verifier-replacement-3`.
- Verdict: `changes_required`; open findings `C2B4-V001` through `C2B4-V008`.
- Independent regression: 1 passed and 3 failed. Existing non-hardware suite:
  283 passed and 2 covered loopback skips. Brokered real-loopback API: 1 failed.
  Mypy reported 4 errors in 2 files.
- Pip check, Ruff, CLI, OpenAPI checker, Node 22 lint/type/unit/build/assets, and
  brokered Playwright 1-test smoke passed.
- Immutable record: `docs/reviews/c2-b4-verification-round-1.md`, SHA-256
  `4384d1382d181b8e7d1a788d12bbff5f8928d7c52a0a31750292b79247bf093d`;
  verification tests and record were committed at `5efadbc` and `dd36a79`.
- No pass transfers. The same implementation lane must read the durable record,
  correct all findings, run focused/full gates including real loopback, and
  produce a new immutable candidate for a fresh verification round.

### C2-B4 correction candidate

- Implementation identity: `cycle2-implementor-replacement-6`.
- Corrected candidate: `dd49ee6aab0092c3963ed30f279fcde026ab70d7`;
  tree `4d29e8309f8d0365b0b9804227a2587e929c2d01`.
- Implementation reports `C2B4-V001` through `C2B4-V008` corrected: complete
  schema/type surface, bounded in-memory replay/CSV import, pulse-preserving
  waveform reduction, operation lifecycle/conflicts/cancel, exact bus/export
  discriminators, replay-sized multipart bound, clean typing, literal expected
  rows, and real-loopback behavior.
- Gates: round-1 verifier tests 4 passed; focused 21 passed with 1 covered
  sandbox skip; full Python 287 passed with 2 covered sandbox skips; Ruff,
  mypy, OpenAPI checker, CLI, Node lint/type/unit/build, and brokered loopback
  test passed.
- Corrected OpenAPI SHA-256
  `118d982c02853ea97e491e0c532376c1ce99524bcfc4e19ca947c3088493a58c`;
  generated TypeScript SHA-256
  `49fdc88cc75ed65f83f0240eaedd7796fcc728cd6f5b61c9831f3b35c30d3896`.
- Round-2 implementation record committed separately at `17ccab6`:
  `docs/reviews/c2-b4-implementation-round-2.md`, SHA-256
  `d4e6b1c67c3093c68ddb75010776cb4187bf4e94ee5b95c97ca527f2479a53f1`.
- Fresh independent verification and complete accumulated validation are
  required; no round-1 or implementation pass transfers.

### C2-B4 verification round 2

- Candidate: `dd49ee6aab0092c3963ed30f279fcde026ab70d7`; tree
  `4d29e8309f8d0365b0b9804227a2587e929c2d01`.
- Verification identity: `cycle2-verifier-replacement-3`.
- Verdict: `changes_required`; open findings `C2B4-V001`, `C2B4-V004`,
  `C2B4-V006`, `C2B4-V009`, and `C2B4-V010`.
- Independent regression: 4 passed and 3 failed. Existing non-hardware: 287
  passed and 2 covered sandbox skips. Brokered loopback API and Playwright each
  passed 1 test.
- Pip check, Ruff, mypy, CLI, Node 22 lint/type/unit/build/assets all passed.
- Immutable record: `docs/reviews/c2-b4-verification-round-2.md`, SHA-256
  `65befa7e91af39a2523e9735bd012c337b4cd5d521b1f5bfac3f9d3f8debc587`;
  test and record commits `9ae9eac` and `89afea9`.
- No pass transfers. The same implementation lane must read the durable record,
  correct every open finding without weakening the approved interface/security,
  and produce a new immutable candidate for a complete fresh round.

### C2-B4 second implementation identity change

- Prior identity: `cycle2-implementor-replacement-6`.
- New replacement identity: `cycle2-implementor-replacement-7`.
- Reason: during round-2 corrections the prior lane twice ended continuation
  turns with required asynchronous operation/cancellation and connection/rate
  ownership incomplete, despite an explicit instruction to continue through
  complete gates.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- The inherited uncommitted replay/server/OpenAPI corrections reportedly make
  the seven independent round-2 tests pass, but the replacement must inspect,
  validate, correct, and complete them. They are not accepted by inheritance
  and no new candidate exists.
- Verification and acceptance identities remain distinct and unchanged.

### C2-B4 final correction and review sequence

- Replacement implementation identity `cycle2-implementor-replacement-7`
  completed the asynchronous import ownership/cancellation foundation. After
  that lane repeatedly stopped at the OpenAPI artifact boundary,
  `cycle2-implementor-replacement-6` resumed the same implementation role and
  completed the bounded contract corrections; neither identity performed
  verification or acceptance.
- Candidate `c627cc33999e3d1caef03dd281f99ef0487e4c6a` was rejected in independent
  verification round 3 for incomplete schema/type drift enforcement, a
  simultaneous-first-upload ownership race, an upload ceiling below the
  accepted B2 replay bound, and implementation modification of verifier-owned
  evidence.
- Candidate `f618455a370c7de57c1a310335c0095b2660cc58` corrected ownership,
  cleanup, accepted replay capacity, and lane separation. Verification round 4
  closed those findings but retained `C2B4-V001` because primitive TypeScript
  and OpenAPI type mutations could evade the drift checker.
- Candidates `9b1e3058b07cda1b69c89ca2371d563e2959aa1d` and
  `85125528e5fa65f43b4550541ef0114c800aefe3` successively closed sampled
  primitive, enum, nullability, array-item, and interface-scoping gaps.
  Independent rounds 5 and 6 demonstrated that incremental field sampling
  still allowed other deep, reference, interface, and enum mutations.
- Final candidate `c8029a1c431092f5cf08de23ecc394ecc8e721d4`, tree
  `d8a5e64f9a64f96a6c52c3cdd6da574a6f6a0c33`, replaced spot-check-only drift
  enforcement with canonical full-OpenAPI and whole-generated-TypeScript
  fingerprints while retaining semantic diagnostics and runtime tests.
- Final implementation record:
  `docs/reviews/c2-b4-implementation-round-7.md`, SHA-256
  `ff283b698a10c8bcda747b8fa8567b69e2af22d5d3f807ae2f6f1b05057cad2e`.
- Independent verification round 7 passed 49 focused checks, including all
  prior mutations, more than 100 individual OpenAPI scalar-leaf mutations,
  route/container/array mutations, every generated-TypeScript character
  replacement, and named interface/reference/type/nullability/identifier/enum/
  field mutations. JSON whitespace and recursive mapping-key reorder remained
  accepted. Record: `docs/reviews/c2-b4-verification-round-7.md`, SHA-256
  `59fb4849d5a0f415dd183892911a484c91dfde49483f956a29944f2e74f0653e`.
- All B4 findings `C2B4-V001`, `C2B4-V004`, `C2B4-V006`, and `C2B4-V011`
  are closed with no open or deferred finding.

### C2-B4 acceptance identity change

- The previously recorded acceptance identity was unavailable when the final
  candidate entered acceptance. Fresh identity
  `cycle2-acceptance-replacement-3` performed no implementation or
  verification work and independently audited the exact final candidate,
  every immutable finding/disposition, accumulated validation, scope,
  security, evidence integrity, and checkpoint readiness.
- Acceptance passed with no findings. Record:
  `docs/reviews/c2-b4-acceptance-round-1.md`, SHA-256
  `ef31d583d6df874ceb8a92fe8e54246e903d1265a93ef28a00a45cbbc4f0a906`.

## C2-B4 checkpoint

- State: Complete
- Recorded: 2026-08-23T19:25:14Z
- Exact accepted product candidate:
  `c8029a1c431092f5cf08de23ecc394ecc8e721d4`
- Exact accepted product tree:
  `d8a5e64f9a64f96a6c52c3cdd6da574a6f6a0c33`
- Product result: deterministic transition and distinct-strobe parallel-bus
  analysis; deterministic bus CSV; bounded secured REST/polling API; closed
  Python-owned OpenAPI 3.1 schemas; generated/validated TypeScript types;
  bounded asynchronous imports, polling, cancellation, conflict handling, and
  cleanup; no serial, WebSocket, remote, persistent-file, or public surface.
- Accumulated acceptance validation: 344 non-hardware Python tests with 2
  covered sandbox-loopback skips; 50 B4 verifier checks; 9 evidence-schema
  tests; pip check; Ruff; mypy; OpenAPI drift checker; CLI; diff check; Node
  22.14.0 lint/typecheck/Vitest/production build/assets; root-brokered real
  loopback API and Playwright production shell each passed 1 test.
- Evidence manifest: `testdata/evidence/c2-b4.json`, committed separately at
  `ef74970`, SHA-256
  `4876b781f4569ae1599b6c5df4d824fbd54223c736c87c96746e6bb821806fd0`;
  strict validation and the 9-test evidence-schema suite passed.
- Checkpoint records B4-owned proof for stopping conditions 5 and 7 and
  refreshes prohibited-action proof for condition 14. Final accumulated proof
  remains owned by C2-B6.
- Process limitation: intentional approved OpenAPI or generated-TypeScript
  regeneration requires a reviewed fingerprint update; this is a review
  trigger, not an open product finding.
- Prohibited actions: none performed; no serial/device open, firmware, C#/.NET,
  persistent state, public serving, packaging/publication, non-macOS support
  claim, B5/B6 implementation, or Cycle 3 action occurred.
- Next boundary: C2-B5 may now be selected. Its concrete rendering thresholds
  require the governing proposal-and-operator-approval procedure before they
  can become acceptance criteria.

## C2-B5: Offline browser viewer and performance-threshold checkpoint

- State: In progress
- Activated: 2026-08-23 (America/Los_Angeles)
- Activation HEAD: `eb693ed`
- Prerequisite: C2-B4 checkpoint complete; manifest
  `testdata/evidence/c2-b4.json` strictly validates with SHA-256
  `4876b781f4569ae1599b6c5df4d824fbd54223c736c87c96746e6bb821806fd0`.
- Objective: deliver a useful bounded offline production React waveform/bus
  workflow for schema-1/schema-2 replay and self-timed CSV across 8/16/24
  channels, then freeze reproducible evidence-based rendering thresholds.
- Implementation agent: `cycle2-implementor-replacement-6`.
- Verification agent: `cycle2-verifier-replacement-3`.
- Acceptance agent: `cycle2-acceptance-replacement-3`.
- In scope: labels/visibility; bounded Canvas digital waveforms; pan;
  cursor-centered zoom; trigger marker; cursor sample/time/value readout;
  transition/strobe bus table; deterministic export; loading/ready/empty/error/
  disconnected/cancelling/shutdown states; production-browser interaction,
  failure, reconnect, cleanup, secret-nondisclosure, and geometry/Canvas/DOM
  bounds; frozen empty/constant/sparse/dense/maximum-width/bus fixtures and
  reproducible primary-macOS performance method.
- Out of scope: live serial capture, device opening, arbitrary million-row DOM,
  pixel-perfect screenshot acceptance, public serving, packaging, threshold
  rebasing without operator approval, B6 integration, and Cycle 3.
- Ownership: implementation owns B5 frontend product, implementation tests,
  production assets, benchmark fixtures/scripts, and implementation records;
  verification owns independent geometry/browser/performance tests and review
  records; acceptance owns independent acceptance and threshold-proposal review
  records; orchestrator owns integration, threshold proposal, operator decision,
  manifest, and checkpoint.
- Authoritative evidence: governing Cycle 2 contracts; accepted B2 replay/CSV
  and 8/16/24 model semantics; accepted B4 API/OpenAPI/TypeScript contract and
  security bounds; fixed independent geometry mathematics; production-browser
  observation; and frozen benchmark fixture digests.
- Acceptance evidence: offline production workflow for all widths and both bus
  modes; bounded visible-window/transition Canvas work and DOM; pointer/keyboard
  pan/zoom/readout; failure/cancel/reconnect/shutdown and secret-nondisclosure;
  clean production runtime without Node/CDN/serial/dev server; clean accumulated
  gates; reproducible performance baseline; independently checked threshold
  proposal; operator-approved immutable threshold record.
- Authority notes: loopback/browser launch uses the centralized approval broker.
  Thresholds are not acceptance criteria until baseline evidence exists,
  verification reproduces the method, acceptance passes the proposal, and the
  operator approves or amends the immutable record.
- Risks: rendering work must remain proportional to visible pixels/transitions,
  baseline fixtures must include dense and maximum-width cases, CI timing is
  informational absent a repeatable relative method, and exact approved
  thresholds cannot be inferred before measurement.

### C2-B5 implementation identity change

- Prior identity: `cycle2-implementor-replacement-6`.
- New identity: `cycle2-b5-implementor-replacement-1`.
- Reason: the prior lane established useful geometry, API, Canvas, and shell
  foundations but repeatedly ended bounded continuation turns while explicitly
  assigned pointer interaction, marker integration, width coverage, bus,
  cancellation, negative, and benchmark work remained incomplete.
- The shared uncommitted frontend, tests, and rebuilt assets remain partial
  implementation work for the replacement to inspect, correct, validate, and
  complete. No candidate or acceptance transfers by inheritance.
- Verification and acceptance identities remain distinct and unchanged.

### C2-B5 verified product and threshold decision gate

- Exact product candidate: `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`;
  tree `06d6498f010f9cf230697aa922c2a550f8cca24c`.
- Independent product verification round 2 passed with `C2B5-V001` closed and
  no open or deferred findings. Record:
  `docs/reviews/c2-b5-verification-round-2.md`, SHA-256
  `ebcf3d9aac7dd1e9b3817f6567ab997cc90cf537f11cb4f5b3344a7949fc0541`.
- Frozen corrected baseline:
  `docs/performance/c2-b5-baseline-round-1.json`, SHA-256
  `c4ad9dab9ed9f53495bba5b93714f069d6f3192bc554148ae68401d2020082d5`.
  It retains raw samples for 16 initial loads, 30 response-complete pan/zoom
  interactions, and four transition/distinct-strobe representative/worst bus
  groups, with exact independently recomputable nearest-rank statistics.
- Threshold proposal round 1 remains immutable failed history. Corrected round
  2 is committed at `c5eb657`:
  `docs/performance/c2-b5-threshold-proposal-round-2.md`, SHA-256
  `d314eea0979b567086eed7b346162eef76865507f9d8a111c736c94f62bbc597`.
- Independent threshold verification round 2 passed and closed
  `C2B5-TV001`/`C2B5-TV002`; record SHA-256
  `7e77999b30650ab19f3b623def7f11b4e1c72b666e1c6f5791b984881eb79b71`.
- Distinct threshold acceptance passed with no findings; a fresh benchmark
  remained below all six timing limits and deterministic resource ceilings.
  Record `docs/reviews/c2-b5-threshold-acceptance-round-1.md`, SHA-256
  `c8f0211ec189a0e5bc5c62bf610f3b40c62e95d08b8109b657ba2be86536f5e6`.
- Proposed effective regression ceilings are 772.10 ms load, 580.30 ms
  pan/zoom, 261.45/116.73 ms representative transition/strobe bus, and
  710.15/263.20 ms worst transition/strobe bus, each also subject to its
  absolute ceiling. Resource ceilings are 46,129 Canvas commands, fewer than
  1,000 DOM nodes, 100,000 samples and 960 pixels per waveform request, and
  100 rows per bus page.
- State: Awaiting approval. The proposal is not an acceptance criterion until
  the operator explicitly approves or amends the exact round-2 record. Overall
  B5 acceptance, manifest, checkpoint, and B6 remain prohibited until then.

## C2-B5 checkpoint

- State: Complete
- Recorded: 2026-08-23T21:01:06Z
- Exact accepted product candidate:
  `b5d502b5ded71fdf03b38058cb4fd6438d9110ad`
- Exact accepted product tree:
  `06d6498f010f9cf230697aa922c2a550f8cca24c`
- Product result: bounded offline production React viewer for schema-1/schema-2
  replay and self-timed CSV; 8/16/24 labels and visibility; reduced-transition
  Canvas waveforms; pointer/keyboard pan and cursor-centered zoom; trigger and
  exact cursor readout; transition/distinct-strobe bus tables, pagination and
  exports; explicit lifecycle/failure/cancel/reconnect/shutdown states; bounded
  DOM/requests/commands; no Node/CDN/serial/development-server runtime.
- Independent product verification: pass with no findings,
  `docs/reviews/c2-b5-verification-round-2.md`, SHA-256
  `ebcf3d9aac7dd1e9b3817f6567ab997cc90cf537f11cb4f5b3344a7949fc0541`.
- Operator-approved threshold record:
  `docs/performance/c2-b5-threshold-approval.md`, committed at `4bd025f`,
  SHA-256
  `57183190d5d48642e9621862aeed343b0a435477a5b4b6276551e55dd01a6053`.
  It incorporates verified proposal round 2 exactly and is a mandatory C2-B6
  acceptance input; silent rebasing is prohibited.
- Overall acceptance: pass with no findings,
  `docs/reviews/c2-b5-acceptance-round-1.md`, SHA-256
  `32252c54a2cd3e0e88370009316a2557659d0132fca7c4c0f66842aa9954771a`.
  Fresh validation reported 354 Python tests with 2 covered sandbox skips, 19
  evidence/baseline tests, frontend lint/typecheck/5 Vitest tests/29-module
  production build, DPR/security browser 1 pass, viewer workflows 2 pass,
  benchmark 1 pass, and root-brokered loopback 1 pass.
- Fresh acceptance benchmark p95 values 450.30/331.30/153.70/66.00/403.10/
  155.50 ms all passed approved dual ceilings; maximum Canvas commands 12,755,
  DOM nodes 216, and bus rows 100 passed deterministic resource ceilings.
- Evidence manifest: `testdata/evidence/c2-b5.json`, committed separately at
  `f561d31`, SHA-256
  `8fcdf9714e2ad94af845d9676227bf6750159075bb49416d9c78c16d5b3c14e9`;
  strict validation and the 9-test evidence-schema suite passed.
- Checkpoint proves B5-owned stopping conditions 10 and 12 and refreshes
  prohibited-action proof for condition 14. Final native/browser/hardware and
  accumulated proof remains owned by C2-B6.
- Unrelated state: untracked repository-root `.ORCHESTRATION.md.swp` was found
  during acceptance, ownership is unknown, and it remains preserved and
  excluded from all B5 staging/evidence.
- Prohibited actions: no live serial/device open, firmware, C#/.NET, public
  serving, packaging/publication, non-macOS support claim, B6 implementation,
  or Cycle 3 action occurred.
- Next boundary: C2-B6 may now be selected only after rechecking the fresh
  operator-confirmed physical setup and explicit runtime port required by the
  governing contract.

## C2-B6: Live browser capture integration and final proof

- State: In progress
- Activated: 2026-08-23 (America/Los_Angeles)
- Activation HEAD: `abc85a0`
- Prerequisites: C2-B5 complete with operator-approved thresholds; prior fresh
  operator confirmations remain in force for the Pico 2 running checked-in V2
  firmware, integrated protection/VRef/common ground, analyzer-input direction,
  fixed-low D1 recovery input, safe shared approximately 1 kHz source, and
  board-label mapping 1/9/17/24 to D0/D8/D16/D23. Read-only `pico-la devices`
  enumeration found exactly one LogicAnalyzer runtime candidate. Its machine-
  local port, serial, and location are runtime-only and will be recorded only
  as `<PORT_SUPPLIED>` or sanitized identity.
- Objective: connect the secured loopback API to the explicit-port device
  service through bounded nonblocking ownership and prove the complete native
  macOS capture/view/analyze/export/reconnect/second-capture/shutdown workflow
  while closing all fourteen Cycle 2 stopping conditions on one final candidate.
- Implementation agent: `cycle2-b5-implementor-replacement-1`, continuing in
  the implementation role for the next batch.
- Verification agent: `cycle2-verifier-replacement-3`.
- Acceptance agent: `cycle2-acceptance-replacement-3`.
- In scope: explicit-port identify/capture/cancel/recovery/close/reopen/reidentify
  API and browser workflow; approved D0-D7/D0-D15/D0-D23 physical pattern;
  native installed-browser waveform/bus/trigger/cursor/export interactions;
  approved B5 threshold enforcement; final clean local and exact-candidate
  macOS CI; independent security/concurrency/disconnect/cleanup proof; final
  manifest, rollback/support audit, and fourteen-condition completion record.
- Out of scope: automatic device selection, Wi-Fi/TCP transport, firmware or
  persistent-device changes, non-macOS support, remote serving, packaging,
  unrelated polish, threshold rebasing, and Cycle 3.
- Ownership: implementation owns B6 device-service/API/browser integration,
  implementation tests, sanitized implementation evidence, and final candidate;
  verification owns independent hardware/browser/security/performance tests and
  immutable review evidence; acceptance owns the final candidate and complete
  proof audit; orchestrator owns shared integration, approval brokerage,
  exact-candidate hosted CI, manifest, checkpoint, and completion audit.
- Required evidence: clean Python/Node bootstraps; every accumulated gate;
  exact-candidate sole macOS hosted CI; native production browser and real Pico
  identity/capture/waveform/bus/export/reopen/second-capture/shutdown; device/API
  concurrency, disconnect, cancel/timeout/recovery and serial cleanup; final
  security regression; approved threshold enforcement; immutable mapping for
  all fourteen stopping conditions; macOS-only completion/support claim.
- Unrelated worktree state: `.ORCHESTRATION.md.swp` remains untracked with
  unknown ownership and must be preserved and excluded from every B6 commit.
- Prohibited-action preflight: enumeration only occurred; no port was opened,
  no capture or recovery byte was sent, and no firmware, bootloader, Wi-Fi,
  persistent-state, .NET, public-server, packaging/publication, or Cycle 3
  operation occurred.
