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

- State: Complete
- Objective: Implement explicit-port pySerial discovery/identity with finite
  lifecycle handling, then prove two physical V2 identities separated by
  close/reopen without changing persistent device state.
- Prerequisites: accepted C1-B2 checkpoint at
  `5d9ceaf87766836d6989e040032d5d1e060a4932`; operator supplied a live port and
  host access. Hardware execution additionally awaits completion of the
  electrical/mapping fields in `docs/operator-input-template.md`.
- Implementation agent: `/root/c1_b3_implementation` (the initially named
  C1-B1 implementation identity reviewed scope but made no C1-B3 edits and was
  replaced before implementation began).
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
- Risks/unknowns: preflight unknowns were resolved by the operator record and
  physical smoke. The deployed CRLF behavior differed from LF-only fixtures and
  was corrected and independently regression-tested before acceptance.

- Acceptance history: round 1 recorded `changes_required` while the operator
  electrical/mapping gate and physical identity proof were pending. Observed
  CRLF line endings reopened implementation and verification. Round 2 records
  `pass` for the corrected candidate and sanitized two-identity close/reopen
  evidence.

### Checkpoint C1-B3 — pySerial discovery and physical identity

- State: Complete
- Completed at: 2026-08-17T03:12:54Z
- Tested commit: `c71db28f17bd2ba8b68542b8514c383610bb7635`
- Tested tree: `bc724c1f071062c4cfd397aac016c3af3083415d`
- Worktree state: clean tracked worktree at physical validation; the final
  operator confirmation, sanitized observation, acceptance record, manifest,
  and this checkpoint record were added afterward as evidence-only files.
- Implementation agent: `/root/c1_b3_implementation`
- Verification agent and verdict: `/root/c1_b1_protocol_verification`; round-2
  verdict `pass` after independently binding LF/CRLF, invalid-terminator,
  whitespace, failure-cleanup, discovery, CLI, and reopen behavior.
- Acceptance agent: `/root/c1_b1_acceptance`; round-2 verdict `pass`.
- Environment: macOS 15.7.7 (24G720), x86_64, Python 3.12.13, lock SHA-256
  `931e790473b3ca014c248cdd3b665389ddb3f24425c4320124c40f1a608ab726`.
- Objective evidence: explicit-port-only pySerial at 115200/8N1 with flow
  control disabled, finite timeouts, DTR/RTS, configure/open/stabilize/drain,
  deterministic VID/PID discovery, exact CLI streams/exits, strict LF/CRLF
  identity parsing, and two real identities separated by close/reopen.
- Files changed: pySerial dependency/lock; serial transport and explicit-port
  device service; `devices`/`info` CLI; implementation and independent tests;
  CLI/operator procedures; immutable verification and acceptance records.
- Focused commands: C1-B3 verifier pass (22 tests); physical
  `V2DeviceService.identify_after_reopen(<PORT_SUPPLIED>, 10.0)` pass with two
  equal identities and exit 0; manifest schema validation pass.
- Accumulated commands: locked durable-environment install and editable install
  pass; `ruff check .` pass; `mypy src` pass; `pytest -m "not hardware"` pass
  (159 tests, one expected duplicate-ZIP construction warning); module help and
  `pip check` pass; `git diff --check` pass.
- Hardware evidence: `LOGIC_ANALYZER_PICO_2_V6_0`, normal maximum 200 MHz,
  blast maximum 400 MHz, buffer 393216 bytes, 24 reported channels, CRLF wire
  lines; two equal reads separated by close/reopen. The port is committed only
  as `<PORT_SUPPLIED>`.
- Wiring evidence: operator confirms the installed integrated checked-in
  LogicAnalyzerV2 protection design, 3.3 V VRef, 3.3 V 1 kHz source, common
  ground at labeled `GND`, and direct circuit inspection establishing labeled
  input `1` as logical D0/Pico GPIO2.
- Evidence manifest: `Software/LogicAnalyzerPy/testdata/evidence/c1-b3.json`.
- Decisions/discrepancies: the deployed USB CDC stream uses CRLF although the
  source-derived fixtures used LF. The transport now accepts exactly LF or
  CRLF without arbitrary whitespace normalization. An initial evidence
  formatter used a nonexistent convenience method after both reads completed;
  the corrected dataclass formatter was rerun and exited 0.
- Deferred findings: capture/export and physical waveform validation remain
  C1-B4; cancellation, timeout recovery, and second post-recovery capture
  remain C1-B5. Broader 24-channel support remains outside Cycle 1.
- Known limitations: Cycle 1 intentionally uses only logical D0-D7 and normal
  capture mode despite the device reporting 24 channels and higher modes.
- Repository state: tested candidate preserves all tracked C# and firmware
  sources; no firmware, bootloader, Wi-Fi, or persistent-device operation was
  performed.
- Next batch: C1-B4; the 1 kHz D0/GPIO2 signal and safe electrical parameters
  are confirmed.
- Blocked: no

## C1-B4: Physical capture, CSV, and provisional replay

- State: Complete
- Objective: Implement the exact normal eight-channel capture/export CLI and
  prove a deterministic rising-edge capture of the operator's 1 kHz D0 signal
  on the physical Pico 2.
- Prerequisites: accepted C1-B3 checkpoint at
  `70015f13b48d30b9710374a81284388aefa84b2f`; operator-confirmed integrated
  protection design, 3.3 V VRef/source, common ground, and labeled input `1`
  physically mapped to logical D0/GPIO2.
- Implementation agent: `/root/c1_b4_implementation`.
- Verification agent: `/root/c1_b4_verification`.
- Acceptance agent: `/root/c1_b1_acceptance` (assigned after integration and
  physical evidence).
- In scope: narrow D0-D7 normal rising/falling capture; negotiated validation;
  bounded sample receive; deterministic self-timed CSV; bounded provisional NPZ
  writer compatible with the accepted loader; capture/replay-validate CLI;
  transactional two-output collision/force/rollback behavior; explicit
  hardware-smoke command and 1 kHz rising-edge proof.
- Out of scope: recovery/cancellation, fixed-level checks without confirmed
  wires, second post-recovery capture, wider/multidevice modes, rich
  measurements, GUI, decoders, legacy `.lac`/CSV, TCP, firmware or persistent
  device changes, and Cycle 2 work.
- Owned files: implementation owns capture driver/service and artifact-writer
  modules, CLI integration, implementation-focused tests, capture/format docs,
  and the hardware-smoke procedure; verifier owns C1-B4 additions under
  `tests/verification/`, independent golden artifact expectations, and its
  C1-B4 verification record; acceptance owns only its later C1-B4 acceptance
  record. The primary orchestrator owns physical execution, evidence manifests,
  shared integration, and this progress log.
- Source evidence: accepted C1-B1/B2 request/parser/replay fixtures; C1-B3
  observed identity/capabilities; firmware `LogicAnalyzer.c`,
  `LogicAnalyzer_Capture.c`, and structs; C# `LogicAnalyzerDriver.cs`; settled
  capture/CSV/replay/CLI/atomic-output contracts.
- Acceptance evidence: literal rising/falling requests; fragmented/coalesced
  fake captures; negotiated count/width/bounds; independent CSV parsing and
  exact-byte determinism; `allow_pickle=False` NPZ reload and hostile-loader
  regression; collision/force/fsync/rollback subprocess tests; exact stream and
  exit codes; physical 1 kHz D0 capture with sample count, nonconstant bit,
  rising transition, measured-frequency tolerance, artifact validation, and
  closed port.
- Authority notes: the hardware run may open only `<PORT_SUPPLIED>`, send the
  characterized identity and normal capture requests, read results, close the
  port, and write sanitized evidence. No cancellation byte belongs to C1-B4;
  no firmware, bootloader, Wi-Fi, or persistent-device operation is permitted.
- Physical parameters: choose 100000 samples/s, rising edge on D0, 2048
  pre-trigger samples, and 4096 post-trigger samples. This yields 100 nominal
  samples per 1 kHz period and 61.44 ms total observation while remaining far
  below the reported 200 MHz normal limit and 393216-byte buffer; the final
  procedure must state and independently justify its frequency tolerance.
- Risks/unknowns: deployed capture status/data framing, source-derived native
  request padding/endianness, and physical polarity remain to be confirmed.
  Any firmware limitation is recorded and deferred rather than repaired in
  Cycle 1.

- Acceptance history: the initial verification record was
  `changes_required` while physical evidence and an explicit frequency
  tolerance were pending. Round-2 verification passed the completed
  non-hardware surface. Final acceptance passed the frozen candidate and its
  physical artifacts.

### Checkpoint C1-B4 — Physical capture, CSV, and provisional replay

- State: Complete
- Completed at: 2026-08-17T03:51:09Z
- Tested commit: `53bfc2184c825296da20a644777729096cff3c1f`
- Tested tree: `7b5828208fbe72839fee2f59fd41652d5abee073`
- Worktree state: clean tracked worktree at physical validation; raw physical
  CSV/NPZ and smoke output were untracked evidence inputs. Sanitized summaries,
  the final acceptance record, manifest, and this checkpoint record were added
  afterward as evidence-only files.
- Implementation agent: `/root/c1_b4_implementation`.
- Verification agent and verdict: `/root/c1_b4_verification`; round-2 verdict
  `pass` for the complete non-hardware surface, with physical proof pending for
  the acceptance owner.
- Acceptance agent: `/root/c1_b1_acceptance`; verdict `pass` after independent
  secure replay loading, byte-identical CSV reconstruction, transition scan,
  and accumulated validation.
- Environment: macOS 15.7.7 (24G720), x86_64, Python 3.12.13, lock SHA-256
  `931e790473b3ca014c248cdd3b665389ddb3f24425c4320124c40f1a608ab726`.
- Objective evidence: exact normal rising/falling capture framing and bounds;
  deterministic transactional CSV/NPZ writes; secure replay reload; explicit
  port and finite failures; sanitized physical waveform evidence.
- Focused commands: C1-B4 verifier pass (22 tests); physical capture,
  replay-validation, and hardware-smoke commands all exited 0; manifest schema
  and artifact digest checks pass.
- Accumulated commands: `pip check`, `ruff check .`, `mypy src`, all verifier
  tests (152), all non-hardware tests (188), module help, and `git diff
  --check` pass. The only warning is the expected duplicate-ZIP hostile-fixture
  construction warning whose archive the production loader rejects.
- Hardware evidence: 100000 samples/s, D0/GPIO2 rising trigger, 2048 pre and
  4096 post samples, 6144 requested/received samples, nonconstant D0, 41 rising
  transitions over a 4000-sample endpoint span, and measured 1000.0 Hz within
  the documented 2.05% combined source/quantization tolerance.
- Evidence manifest: `Software/LogicAnalyzerPy/testdata/evidence/c1-b4.json`.
- Decisions/discrepancies: the physical low-to-high transition appears at
  sample 2047 while the settled logical trigger marker/time-zero boundary is
  sample 2048. The requested polarity is present and periodic, so this does not
  block the Cycle 1 gate; the sequencing relationship is explicitly recorded
  for later protocol/firmware investigation rather than changing the settled
  data contract.
- Deferred findings: timeout/cancellation recovery, a fixed-level no-trigger
  proof, close/reopen/re-identification, and the second physical capture remain
  C1-B5. Wider modes, GUI, decoders, and any firmware changes remain later
  cycles.
- Known limitations: the provisional replay format is Cycle 1 only; the
  physical edge is not claimed to coincide exactly with the logical time-zero
  sample.
- Repository state: the tested candidate preserves all tracked C# and firmware
  sources. No firmware, bootloader, Wi-Fi, or persistent-device operation was
  performed.
- Next batch: C1-B5; awaiting operator confirmation of a fixed-level idle input
  for the intentional no-trigger recovery proof.
- Blocked: no

## C1-B5: Lifecycle hardening and final hardware proof

- State: Ready
- Objective: Prove bounded timeout/Ctrl-C recovery, exact single-byte V2
  cancellation, drain/close/reopen/re-identification, and a second physical
  1 kHz D0 capture without a power cycle, then assemble the final Cycle 1
  stopping-condition proof.
- Prerequisites: accepted C1-B4 checkpoint at
  `b251b755fc0296c2f731fe26fb2109035f44d38e`; physical recovery additionally
  awaits operator confirmation of a fixed-level idle input. The operator has
  been asked to leave the 1 kHz signal on labeled input `1`/D0/GPIO2 and connect
  labeled input `2`/D1/GPIO3 to ground as the simplest fixed-low setup.
- Implementation agent: `/root/c1_b4_implementation` (stable implementation
  identity reused after the C1-B4 checkpoint).
- Verification agent: `/root/c1_b1_protocol_verification` (independent of the
  C1-B5 implementation identity).
- Acceptance agent: `/root/c1_b1_acceptance` (assigned only after integration,
  clean bootstrap, and physical evidence).
- In scope: production recovery-smoke CLI; a normal capture on the confirmed
  fixed-level channel; bounded cancellation delay; exactly one `0xFF`; bounded
  drain; close/reopen/re-identification; second normal capture of the known
  periodic D0 signal; atomic sanitized evidence; Ctrl-C, timeout, malformed,
  disconnect, cleanup, command-stream/exit, and Cycle 1 regression tests; final
  clean Python 3.12 bootstrap and handoff evidence.
- Out of scope: firmware or bootloader operations, persistent device changes,
  public/general abort APIs, immediate/complex/fast/blast/burst modes, wider
  captures, GUI, decoders, TCP/Wi-Fi, release packaging, and Cycle 2 work.
- Owned files: implementation owns the minimal recovery service/CLI modules,
  implementation-focused tests, and recovery procedure; verifier owns C1-B5
  additions under `tests/verification/` and its immutable verification review;
  acceptance owns only its C1-B5 acceptance review. The primary orchestrator
  owns shared integration, physical execution, evidence manifests, final
  stopping checklist, and this progress log.
- Source evidence: accepted C1-B2 recovery primitive/tests; C1-B3 serial
  lifecycle and observed CRLF identity; C1-B4 capture/smoke behavior and
  artifacts; firmware V2 cancellation handling; C# capture cancellation and
  reopen paths; settled recovery/CLI/evidence contracts in the governing
  documents.
- Acceptance evidence: literal fake transport and pySerial order proving one
  `0xFF`, shared finite drain deadline/byte cap, cleanup under timeout/Ctrl-C,
  malformed input and disconnect; exact CLI streams/exits and atomic evidence;
  physical fixed-level no-trigger cancellation followed by reopen/identity and
  second 1 kHz D0 capture without power cycle; clean Python 3.12 hash-locked
  bootstrap; accumulated static/non-hardware gates; exact final candidate/tree
  and all nine stopping-condition links.
- Authority notes: non-hardware work may proceed while fixed-level wiring is
  pending. Physical I/O may use only `<PORT_SUPPLIED>`, the confirmed idle and
  periodic inputs, normal eight-channel requests, and exactly one `0xFF` while
  recovering an in-flight capture. No firmware flash, bootloader, Wi-Fi, or
  persistent-device action is allowed.
- Risks/unknowns: the fixed-level jumper is not yet operator-confirmed; deployed
  cancellation acknowledgement/drain timing must be bounded from observed wire
  behavior without changing firmware; the C1-B4 one-sample physical-edge versus
  logical-trigger-marker relationship remains a documented later-cycle issue.

## Deferred work

- C1-B2 owns production models, codec, parser, fake/replay transport, and negative protocol tests.
- C1-B3 owns pySerial, explicit-port identity, and physical identity confirmation.
- C1-B4 owns physical capture and CSV/replay writes; C1-B5 owns lifecycle hardening and final hardware proof.
