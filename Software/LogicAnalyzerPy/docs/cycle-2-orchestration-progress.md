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

- State: Ready
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
