# Cycle 1 orchestration progress

## C1-B1: Preflight, scaffold, and narrow protocol evidence

- State: Complete
- Objective: Create a runnable Python 3.12 skeleton and narrow V2 evidence without guessing a native binary layout.
- Prerequisites: Approved preparatory documents; operator assertion of intended V2 target; writable workspace.
- Implementation agent: `/root/c1_b1_implementation`
- Verification agent: `/root/c1_b1_protocol_verification`
- Acceptance agent: `/root/c1_b1_acceptance` (assigned after integration)
- In scope: scaffold, contracts, operator template, evidence schema, protocol notes, lock, CI, and focused scaffold tests.
- Out of scope: production serial/capture, GUI, Qt/pythonnet/Roslyn, firmware changes, and later-cycle work.
- Owned files: all new project files except `testdata/protocol/`, `docs/protocol-fixture-provenance.md`, and acceptance-review records; `.github/workflows/logic-analyzer-python-cycle1.yml` only in `.github`.
- Source evidence: V2 `LogicAnalyzer_Structs.h`/`LogicAnalyzer.c`; C# `AnalyzerDriverBase.cs`, `LogicAnalyzerDriver.cs`, `CaptureSession.cs`, and `VersionValidator.cs`.
- Acceptance evidence: clean source install, CLI help, Ruff, mypy, pytest, independently authored golden fixtures, and protocol provenance review.
- Authority notes: dependency/Python installation requires the normal approval
  mechanism; no hardware I/O or firmware/persistent-device mutation in this
  batch.
- Risks/unknowns: no known-good C#/board trace is checked in; fixture provenance
  and deployed-layout confirmation are verifier/C1-B3 work. Linux/macOS CI must
  both pass before this checkpoint is accepted.

- Acceptance history: rounds 1 and 2 recorded `changes_required` while the
  clean-bootstrap, evidence-schema, and CI gates were resolved. Round 3 records
  `pass` for the exact CI-tested candidate.

### Checkpoint C1-B1 — Preflight, scaffold, and narrow protocol evidence

- State: Complete
- Completed at: 2026-08-16T22:55:23Z
- Tested commit: `476c075891e50e5525b3aa3acc3430415ff018d3`
- Tested tree: `36712636d4cfdb0a6859c2b9160cc532d8d9deeb`
- Worktree state: clean tracked worktree at validation; the final acceptance
  record, manifest, and this checkpoint record were added afterward as
  evidence-only files.
- Implementation agent: `/root/c1_b1_implementation`
- Verification agent and verdict: `/root/c1_b1_protocol_verification`; pass for
  source-derived protocol evidence with physical confirmation explicitly
  deferred to C1-B3/C1-B4.
- Acceptance agent: `/root/c1_b1_acceptance`; final round 3 verdict `pass`.
- Environment: macOS 15.7.7 (24G720), x86_64, Python 3.12.13, lock SHA-256
  `8f6f7e76f28f78a973c60d7cd54056ed8d3969bce5488a053f4dc1fef0539be4`;
  GitHub-hosted `macos-latest` and `ubuntu-latest`, Python 3.12.
- Objective evidence: hash-locked clean bootstrap; installed/module CLI help;
  Ruff, mypy, and two non-hardware pytest tests; provenance-tagged identity and
  rising/falling 48-byte request vectors; passing Linux/macOS GitHub Actions
  run `31977526293` on the exact candidate.
- Files changed: `.github/workflows/logic-analyzer-python-cycle1.yml` and the
  new `Software/LogicAnalyzerPy/` scaffold, contracts, fixtures, tests, reviews,
  progress log, and checkpoint manifest.
- Focused commands: fixture byte/layout validator pass; `pico-la --help` pass;
  `python -m pico_logic_analyzer --help` pass; `git diff --check` pass.
- Accumulated commands: locked install and no-isolation/no-deps editable install
  pass; `ruff check .` pass; `mypy src` pass; `pytest -m "not hardware"` pass
  locally and in GitHub jobs `95239134146` (macOS) and `95239134210` (Ubuntu).
- Hardware evidence: not applicable to C1-B1; no serial I/O was performed.
- Evidence manifest: `Software/LogicAnalyzerPy/testdata/evidence/c1-b1.json`,
  SHA-256 `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc`.
- Decisions/discrepancies: explicit little-endian 48-byte native-layout fixture
  is source-derived, not observed wire evidence; padding, polarity, identity,
  and deployed ABI remain mandatory physical confirmations. Cycle 1 CSV is
  self-timed and intentionally differs from the existing channel-only export.
- Deferred findings: GUI, broader modes/connectivity, decoder hosting, legacy
  CSV, and firmware/parser shortcomings remain in their later roadmap cycles.
- Known limitations: operational serial/capture commands remain deliberately
  unimplemented until C1-B2 through C1-B5; no known-good C#/board trace exists.
- Repository state: tested commit was clean and preserves all tracked C# and
  firmware sources; evidence-only files were then added for checkpointing.
- Next batch: C1-B2; no unmet inputs.
- Blocked: no

## C1-B2: Models, codec, and fake/replay contract

- State: Complete
- Objective: Implement and independently verify the bounded, hardware-free
  Cycle 1 data model, V2 codec/parser, fake transport/recovery lifecycle, and
  hostile provisional-replay validation surface.
- Prerequisites: accepted C1-B1 checkpoint at
  `81f9606a52dfe0efb42164d1ed08155aedd5fbc1`.
- Implementation agent: `/root/c1_b1_implementation` (reused as the stable
  implementation identity for C1-B2).
- Verification agent: `/root/c1_b1_protocol_verification` (reused as the stable
  independent verification identity for C1-B2).
- Acceptance agent: `/root/c1_b1_acceptance` (assigned only after integration).
- In scope: typed identity/config/result models; D0-D7 and trigger/time
  invariants; exact framing/request and bounded response parsing; minimal
  transport protocol; scripted fake/replay transport; bounded NPZ replay
  validation; exhaustive normal, fragmented, coalesced, timeout, cancellation,
  disconnect, malformed, and hostile-container tests.
- Out of scope: pySerial, hardware CLI behavior, real serial I/O, production
  artifact writes, widths above eight, generic protocol abstractions, GUI,
  firmware changes, and later-cycle features.
- Owned files: implementation owns package modules, dependency metadata/lock,
  implementation-focused unit tests, and directly related API docs; verifier
  owns `tests/verification/`, `testdata/replay/`, and its C1-B2 verification
  record; acceptance owns only its later C1-B2 acceptance record. The primary
  orchestrator owns shared integration and this progress log.
- Source evidence: accepted C1-B1 protocol fixtures/provenance; V2 firmware and
  C# sources named there; settled capture, CLI, replay-security, compatibility,
  and recovery contracts.
- Acceptance evidence: byte-for-byte golden requests; one-byte fragmented and
  single-read coalesced parsing; bounded malformed/timeout/disconnect/recovery
  behavior; hostile replay-container coverage; capture-boundary invariants;
  import-boundary enforcement; accumulated non-hardware gate.
- Authority notes: dependency acquisition follows the approved network
  mechanism; no serial port access or hardware command is permitted.
- Risks/unknowns: NumPy must be added and hash-locked without broadening the
  archive surface; text/binary phase ownership and cancellation lifecycle must
  remain one-buffer and finite; production source must not derive expectations
  from golden fixtures.

### Checkpoint C1-B2 — Models, codec, and fake/replay contract

- State: Complete
- Completed at: 2026-08-17T00:10:28Z
- Tested commit: `37bdd50da4c85f32eb0055ca2a34be92e7edb2f0`
- Tested tree: `ba16e00fdc4a4bc88d9e02dcdf6742d840ee7a9c`
- Worktree state: clean tracked worktree at independent acceptance; the
  acceptance record, manifest, and this checkpoint record were added afterward
  as evidence-only files.
- Implementation agent: `/root/c1_b1_implementation`
- Verification agent and verdict: `/root/c1_b1_protocol_verification`; final
  expanded and post-integration verdict `pass`.
- Acceptance agent: `/root/c1_b1_acceptance`; verdict `pass`.
- Environment: macOS 15.7.7 (24G720), x86_64, Python 3.12.13, lock SHA-256
  `1dd0a6e018394c276bc8a5e7939e7380b1a3ab3ac67fd306e53cfb75130c44c6`.
- Objective evidence: exact identity/rising/falling golden frames; fragmented
  and coalesced parsing; typed capture/time boundaries; bounded fake transport
  and one-byte cancellation/recovery; pre-materialization NPY/header and full
  hostile replay validation; forbidden-import checks.
- Files changed: NumPy dependency/lock; new model, protocol, transport, driver,
  and replay modules; implementation and independent verification tests;
  replay fixture notes and verification/acceptance records.
- Focused commands: `pytest tests/verification -q` pass (108 tests); exact
  identity/capture vectors pass; replay hostile/boundary tests pass; recovery
  deadline/byte-cap/failure-order tests pass.
- Accumulated commands: fresh locked install and no-isolation/no-deps editable
  install pass; `ruff check .` pass; `mypy src` pass; `pytest -m
  "not hardware"` pass (124 tests); module and installed CLI help pass; `pip
  check` pass; `git diff --check` pass.
- Hardware evidence: not applicable to C1-B2; no serial I/O was performed.
- Evidence manifest: `Software/LogicAnalyzerPy/testdata/evidence/c1-b2.json`,
  SHA-256 `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af`.
- Decisions/discrepancies: NumPy `2.2.2` is the exact runtime/locked version;
  replay rejects unsafe declarations before `np.load`; exact response phases
  reject trailing bytes; recovery shares one deadline and 4096-byte drain cap.
- Deferred findings: real pySerial/open ordering and physical identity move to
  C1-B3; physical capture and artifact writing to C1-B4; physical recovery and
  final lifecycle proof to C1-B5.
- Known limitations: core is hardware-free; ABI/padding/polarity and deployed
  identity remain source-derived pending their owning physical gates. One
  expected warning is emitted while constructing the duplicate-ZIP hostile
  fixture; production correctly rejects the archive.
- Repository state: tested commit was clean and preserves tracked C# and
  firmware sources; evidence-only files were then added for checkpointing.
- Next batch: C1-B3; operator port and safety inputs require preflight
  resolution before identity I/O.
- Blocked: no

## C1-B3: pySerial discovery and physical identity

- State: In progress
- Objective: Implement explicit-port pySerial discovery/identity with finite
  lifecycle handling, then prove two physical V2 identities separated by
  close/reopen without changing persistent device state.
- Prerequisites: accepted C1-B2 checkpoint at
  `5d9ceaf87766836d6989e040032d5d1e060a4932`; operator supplied a live port and
  host access. Hardware execution additionally awaits completion of the
  electrical/mapping fields in `docs/operator-input-template.md`.
- Implementation agent: `/root/c1_b1_implementation` (stable implementation
  identity reused for C1-B3).
- Verification agent: `/root/c1_b1_protocol_verification` (stable independent
  verification identity reused for C1-B3).
- Acceptance agent: `/root/c1_b1_acceptance` (assigned after integration).
- In scope: pySerial dependency/transport; exact 115200/8N1/no-flow-control,
  DTR/RTS, configure/open/stabilize/drain/close/reopen sequence; best-effort
  VID `0x1209`/PID `0x3020` discovery without auto-selection; exact `devices`
  and explicit-port `info` CLI/JSON/exit contracts; finite errors and cleanup;
  fake port/list-port tests; opt-in two-identity physical smoke.
- Out of scope: capture/export, automatic selection, remembered devices,
  hot-plug monitoring, TCP, persistent device management, firmware changes,
  and later-cycle features.
- Owned files: implementation owns serial transport/service modules, CLI
  integration, pySerial dependency/lock, implementation tests, and the C1-B3
  operator procedure; verifier owns C1-B3 additions under `tests/verification/`
  and its C1-B3 verification record; acceptance owns only its later acceptance
  record. The primary orchestrator owns this progress log and hardware run.
- Source evidence: settled serial/receive/CLI contracts; accepted C1-B1/B2
  protocol evidence; C# `LogicAnalyzerDriver.cs` serial constructor/open paths,
  `SerialPortScanner.cs` discovery metadata, and `VersionValidator.cs`.
- Acceptance evidence: constructor/configuration sequence and list-port fakes;
  Linux/macOS-like/absent metadata; exact stdout/stderr/JSON/exit codes;
  timeout/permission/unplug cleanup; explicit-port-only behavior; two real V2
  identity reads separated by close/reopen with sanitized evidence.
- Authority notes: no port open until operator electrical/mapping template is
  complete; real I/O is identity-only and may not flash, enter bootloader,
  change Wi-Fi, or mutate persistent state.
- Risks/unknowns: exact deployed identity/capabilities and USB CDC timing remain
  unresolved until physical smoke; protection-board revision, target voltage,
  VRef, permitted range, ground point, and channel-1 mapping await operator
  confirmation.

## Deferred work

- C1-B2 owns production models, codec, parser, fake/replay transport, and negative protocol tests.
- C1-B3 owns pySerial, explicit-port identity, and physical identity confirmation.
- C1-B4 owns physical capture and CSV/replay writes; C1-B5 owns lifecycle hardening and final hardware proof.
