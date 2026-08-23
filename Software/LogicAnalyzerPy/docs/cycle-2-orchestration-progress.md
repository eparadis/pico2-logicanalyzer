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

### C2-B3 implementation identity change

- Prior identity: `cycle2-implementor-replacement-4`
- New replacement identity: `cycle2-implementor-replacement-5`
- Reason: the prior B2 implementor lane is no longer available when the
  operator-authorized B3 physical gate becomes executable.
- Lane/model/reasoning preserved: Implementor, `gpt-5.6-terra`, low.
- State advances to In progress for the bounded physical procedure. Verification
  and acceptance remain separate and will receive fresh same-lane replacements
  if their prior identities are unavailable.
