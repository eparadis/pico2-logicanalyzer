# Architectural Domains and Reviewer Charters

## Provenance

The domain map was prepared by the architecture-discovery agent
`/root/domain_mapper` after inspecting the current implementation and rewrite
documents. It partitions review responsibility by architectural boundary rather
than by document, because each process document spans several code domains.

## Current architectural domains

### 1. Firmware and wire protocol

Framing and escaping, command IDs, C ABI layout/alignment, identity responses,
capture status and payload ordering, channel/bit ordering, limits, trigger
semantics, PIO behavior, and firmware variants.

Primary sources: `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c`,
`LogicAnalyzer_Structs.h`, capture/PIO sources, and board/configuration headers.

### 2. Transport, discovery, and hardware lifecycle

Serial/TCP setup, DTR/RTS behavior, partial reads, finite timeouts,
cancellation, disconnects, cleanup, close/reopen, discovery, and later
multi-device composition.

Primary sources: `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs`,
`AnalyzerDriverBase.cs`, `DeviceDetector.cs`, `MultiAnalyzerDriver.cs`,
`EmulatedAnalyzerDriver.cs`, and `VersionValidator.cs`.

### 3. Capture domain and validation

Capture settings, channel numbering, sample widths and storage, pre/post-trigger
semantics, mode-dependent capacities, burst metadata, validation, and wire-word
to channel-sample conversion.

Primary sources: `CaptureSession.cs`, `AnalyzerChannel.cs`, `BurstInfo.cs`,
`CaptureModes.cs`, plus duplicated validation in the CLI, terminal, and GUI.

### 4. Persistence, export, analysis, and editing

Legacy `.lac`, deterministic CSV/NPZ, schema evolution, regions, measurements,
sample transformations, signal composition, and untrusted input.

Primary sources: `LogicAnalyzer/Classes/`, `MainWindow.axaml.cs`,
`ChannelMeasures.axaml.cs`, `SignalDescriptionLanguage/`, and
`TerminalCapture/Classes/`.

### 5. Sigrok decoder runtime

Decoder discovery/metadata, Python embedding replacement, API-v3 `wait`,
annotations and Python outputs, stacking, option/channel mapping, failure
isolation, and executable-code trust boundaries.

Primary sources: `LogicAnalyzer/SigrokDecoderBridge/`, `Software/decoders/`, and
the decoder-management/annotation controls.

### 6. User-facing workflows and rendering

CLI contracts and exit behavior; GUI capture/edit/decode workflows; background
work; waveform, marker, overview, and annotation rendering; responsiveness.

Primary sources: `CLCapture/`, `TerminalCapture/`, `MainWindow.axaml*`,
`LogicAnalyzer/Controls/`, `Dialogs/`, and `Interfaces/`.

### 7. Platform integration, configuration, packaging, and release

Python/Qt/dependency choices, Linux/macOS device access, platform paths,
resources and licenses, clean-machine installation, signing/notarization,
artifacts, and C# rollback/retirement.

Primary sources: project/solution/publish files, settings, assets,
Python-installation handling, and platform discovery.

### 8. Verification and orchestration governance

Characterization evidence, fake/replay contracts, hardware acceptance, CI,
batch dependency and ownership, independent review, authority gates, progress
records, completion proof, deferral discipline, and the durable-goal stop.

Primary sources: the three rewrite/process documents and repository agent
instructions.

## Reviewer 1: Device Protocol and Hardware Boundary

### Scope

Domains 1–3, ending at a validated in-memory capture. This reviewer owns every
seam from firmware bytes through transport and lifecycle to raw capture-word
interpretation.

### Required inspection

- `Firmware/LogicAnalyzer_V2/`
- `Software/LogicAnalyzer/SharedDriver/`
- Capture validation in `CLCapture`, `TerminalCapture`, and GUI dialogs
- All three rewrite/process documents at the supplied commit

### Review invariants

- Python layout is never inferred from C# marshaling alone.
- Lengths are bounded before allocation/read.
- Timeouts and cleanup are deterministic.
- Port selection is explicit and discovery advisory.
- Fake success cannot replace a physical-board pass.
- Cycle 1 remains serial, normal 8-channel, single-edge capture only.
- The handoff is raw words plus settled metadata, not persistence or UI policy.

### Explicitly delegated

Reviewer 2 owns persistence, analysis, decoder, CLI/GUI, and rendering semantics.
Reviewer 3 owns governance, proof ownership, CI/platform delivery, review
records, and completion authorization.

## Reviewer 2: Capture Data, Decoder, and User-Workflow Boundary

### Scope

Domains 4–6, beginning with validated raw words and metadata and ending with
meaningful library, CLI, and future GUI behavior.

### Required inspection

- Capture models and `LogicAnalyzer/Classes/`
- `.lac`/CSV implementations and terminal file operations
- `CLCapture/`, `TerminalCapture/`, GUI workflows and renderers
- `SignalDescriptionLanguage/`
- `SigrokDecoderBridge/`, bundled decoders, and decoder UI
- All three rewrite/process documents at the supplied commit

### Review invariants

- One capture model serves CLI and future GUI.
- Internal zero-based channel identity remains distinct from display names.
- No pickle or arbitrary-class deserialization.
- Schemas are deterministic and explicitly versioned.
- Capture files cannot silently nominate decoder code to execute.
- Rendering scales by visible transitions, not per-sample UI objects.
- Cycle 1 provides useful capture/export/replay without premature GUI or
  decoder breadth.

### Explicitly delegated

Reviewer 1 owns byte protocol, serial lifecycle, and raw-word production.
Reviewer 3 owns installation/CI mechanics, orchestration authority and
ownership, records, and final proof.

## Reviewer 3: Delivery, Verification, and Orchestration Contract

### Scope

Domains 7–8 and every plan-to-proof seam. This reviewer owns whether agents can
execute safely from bounded discovery to one verifiable stop.

### Required inspection

- Repository agent instructions
- All three rewrite/process documents at the supplied commit
- `docs/rewrite-reviews/`
- Existing solution/project/publish/configuration files
- Repository test and CI state
- Platform discovery and Python bootstrap/embedding code

### Review invariants

- There is one bounded objective and one verifiable stop.
- Each requirement has a batch owner and objective evidence.
- Independent verification does not approve its own implementation.
- Evidence is provenance-tagged, sanitized, reproducible, and linked.
- Hardware absence never becomes fake completion.
- Existing C# and firmware remain rollback paths.
- Review records contain all required metadata.
- All three final passes name the same commit.

### Explicitly delegated

Reviewer 1 determines protocol, serial, and physical-capture correctness.
Reviewer 2 determines capture/file/decoder/workflow semantics and practical
utility. Reviewer 3 requires their evidence but does not substitute its own
technical judgment.

## Cross-domain seam rule

A reviewer records a finding when its own domain cannot safely consume another
domain's promised output. It assigns the technical resolution to the owning
reviewer but verifies that the handoff is explicit. Conflicting findings are
resolved by the document authority order in `ORCHESTRATION.md`; a substantive
resolution triggers all-three re-review.
