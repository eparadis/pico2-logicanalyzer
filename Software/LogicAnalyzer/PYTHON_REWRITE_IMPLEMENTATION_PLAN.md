# Python Logic Analyzer Rewrite: Implementation and Verification Plan

> **Document role:** This is a historical and forward-looking technical
> roadmap, not current execution authority. Cycle 1 remains governed by
> [`ORCHESTRATION.md`](../../ORCHESTRATION.md) and
> [`BATCH_EXECUTION.md`](../../BATCH_EXECUTION.md). Accepted Cycle 2 behavior is
> established by [`CYCLE2_ORCHESTRATION.md`](../../CYCLE2_ORCHESTRATION.md),
> [`CYCLE2_BATCH_EXECUTION.md`](../../CYCLE2_BATCH_EXECUTION.md), and the
> [Cycle 2 completion proof](../LogicAnalyzerPy/docs/cycle-2-completion.md).
> Cycle 3 is still in preparation under
> [`CYCLE3_PREPARATION.md`](../../CYCLE3_PREPARATION.md); its discovery,
> contracts, reviews, and durable goal must approve any implementation scope.
> Commit-anchored domain reviews are stored in
> [`docs/rewrite-reviews/`](../../docs/rewrite-reviews/README.md).

## Purpose

This document began as an execution plan for replacing the .NET/Avalonia
logic-analyzer applications with a Python implementation. It now records both
the original long-range parity ideas and the accepted incremental result. The
accepted product through Cycle 2 is a Python package and CLI plus a loopback-
only local browser application built with React, TypeScript, and Vite. Its
audited support claim is macOS only. Linux support, `.lac` interoperability,
desktop packaging, and complete legacy parity are possible later-cycle topics,
not current requirements or support claims.

The rewrite must be incremental. Do not remove or substantially change the
existing C# implementation until the Python replacement passes the compatibility
and hardware acceptance gates defined below. Treat the existing implementation
and firmware as behavioral references, not automatically as correct
specifications; known defects must be captured as tests and intentionally fixed.

## Execution policy: hardware-first, complexity-later

The phase plan below describes the eventual replacement, but it is not the order
for the first useful delivery. The orchestrator must first prove a deliberately
narrow vertical slice against one physical analyzer. Do not expand Cycle 1 to
meet later parity gates.

The initial supported target is one board running
`Firmware/LogicAnalyzer_V2`, connected by an explicitly selected USB serial
port. Cycle 1 supports identity and one normal 8-channel capture with a
single-channel rising/falling edge trigger, known-safe defaults, CSV export, and
a provisional internal replay artifact. It is intentionally a partial bus tool:
it can inspect an 8-bit data bus or a selected group of control/address signals,
but it does not yet claim simultaneous full address/data/control visibility.

The first useful delivery was source-installed on Python 3.12. Its historical
non-hardware tests ran on Linux and macOS, while physical smoke ran on the host
with the board. Cycle 2 subsequently completed wider capture and the local
browser application under a macOS-only support claim. Packaging, broad firmware
compatibility, automated device selection, TCP, advanced triggers, decoder
compatibility, and fuller application parity remain later-cycle topics.

### Delivery cycles and hard scope boundaries

#### Cycle 1: physical capture vertical slice

Implement only what is needed to:

1. list candidate serial ports on a best-effort basis;
2. open an operator-supplied `--port PATH`;
3. read and report identity/version/capabilities from the known V2 board;
4. encode one normal 8-channel capture request with a rising or falling edge
   trigger on one selected channel;
5. read, validate, and store the returned 8-bit raw sample words;
6. export deterministic CSV and a minimal versioned `.npz` replay artifact;
7. close safely on success, timeout, Ctrl-C, disconnect, or parse failure; and
8. repeat a capture after close/reopen.

The `.npz` artifact is an internal test/replay format, not a promised user
interchange format. It must contain raw sample words plus the minimum typed
metadata needed to reproduce export and viewing. Load it with pickling disabled;
store metadata as validated JSON or non-object arrays. Its filename/schema must
be marked provisional in code and documentation.

Cycle 1 uses finite configurable timeouts and explicit disconnected, idle, and
capturing states. Initial recovery is close/reopen. Do not implement the
firmware abort command until its wire behavior is characterized.

Cycle 1 is accepted only after fake/replay tests and the physical smoke procedure
under "Cycle 1 hardware gate" pass. Documentation and scaffolding should be just
complete enough to support this slice; exhaustive inventory and characterization
must not delay it.

#### Cycle 2: accepted wider capture and local browser viewing

Cycle 2 is complete. The accepted candidate adds ordered one-to-24-channel
normal capture with 8-, 16-, and 24-channel transfer modes; schema-1 replay
reads and canonical replay-schema-2 writes; generalized deterministic
self-timed CSV import/export; deterministic transition and distinct-strobe
parallel-bus analysis; and a loopback-only React/TypeScript/Vite browser
application using bounded Canvas rendering. Offline replay/CSV viewing, live
serial capture, labels and visibility, pan, cursor-centered zoom, cursor and
trigger readout, bus tables, export, lifecycle recovery, security boundaries,
and approved performance gates all passed. Cycle 2 deliberately excluded
PySide6/Qt, `.lac`, .NET, packaging, public serving, protocol decoders, and any
non-macOS support claim.

#### Cycle 3: focused decoder support

The proposed focused direction is to implement only the sigrok host behavior
exercised by the checked-in UART, SPI, and I2C decoder versions while keeping
the public Python capture/analysis API usable without a frontend. This is not
yet approved scope. Cycle 3 discovery and operator decisions must settle the
decoder identities and provenance, trusted-code boundary, process isolation,
resource limits, expected-annotation sources, accepted library/CLI/browser
surfaces, platform claim, and whether replay/synthetic evidence is sufficient.
Broader API-v3 compatibility, decoder stacking, user decoder directories, and
an all-decoder import gate remain Cycle 4-or-later parity candidates unless the
approved Cycle 3 contracts say otherwise.

#### Cycle 4 and later: parity and distribution

Consider advanced triggers/capture modes, decoder breadth, editing, TCP,
multi-device support, device-management workflows, further interactive parity,
non-macOS support, `.lac` compatibility, and self-contained distribution in
separately approved evidence-driven increments. Apply the detailed work
packages below only after their prerequisites and product/platform decisions
have been reviewed; their presence here is not a promise or authorization.

## Reviewed decision log

The following choices preserve the original Cycle 1 planning history. Later
approved contracts supersede them where they conflict: in particular Cycle 2
selected React/TypeScript/Vite instead of PySide6, replay schema 2 and the
self-timed CSV contract instead of `.lac`, and an audited macOS-only support
claim instead of Linux/macOS support. These historical entries are not current
Cycle 3 authority.

1. **First useful cycle.** Ambiguity: the original first iteration stopped
   before serial work although the plan favored a vertical slice.
   **Recommendation:** identity plus one normal 8-channel serial capture, CLI,
   CSV, fake tests, and a physical smoke test. Benefit: retires the highest-risk
   boundary and produces immediate value; tradeoff: incomplete documentation and
   expected refactoring. **Alternatives:** documentation/golden corpus first
   reduces later rework but gives no hardware evidence; completing all of P0-P3
   gives a cohesive CLI but delays feedback and combines too many failure modes.
   **Evaluator choice and final resolution:** recommendation.
2. **Initial firmware scope.** Ambiguity: supported variants were unspecified.
   **Recommendation:** support only the available V2 board/version and reject
   unknown incompatible versions clearly. Benefit: a concrete test target;
   tradeoff: no initial legacy-board support. **Alternatives:** characterize all
   repository variants for broader compatibility at substantial cost, or assume
   one universal format for less work but unsafe failures. **Evaluator choice
   and final resolution:** recommendation.
3. **Initial channel width.** Ambiguity: 8/16/24-bit modes were gated together
   even though an 8-bit processor does not imply that its whole bus fits in eight
   analyzer channels. **Recommendation:** prove 8-channel capture first and add
   16/24 in Cycle 2. Benefit: simplest useful wire path; tradeoff: no initial
   full-bus correlation. **Alternatives:** 24 channels gives maximum visibility
   but expands first-cycle parsing/wiring/testing; 8+16 is more useful than 8
   alone but still expands the first matrix without full visibility. **Evaluator
   choice and final resolution:** recommendation.
4. **Initial capture/trigger modes.** Ambiguity: all modes and triggers were
   grouped together. **Recommendation:** one normal mode and a single-channel
   rising/falling edge trigger, adding immediate/no-trigger only if it is already
   unambiguous. Benefit: useful clock/reset/strobe capture with a small request
   matrix; tradeoff: no pattern, high-speed, or burst workflows. **Alternatives:**
   all triggers maximize parity but delay capture; no trigger is smaller but
   inadequate for intermittent faults. **Evaluator choice and final
   resolution:** recommendation.
5. **First output/viewing surface.** Ambiguity: `.lac`, CSV, GUI, and decoder
   delivery order was unclear. **Recommendation:** deterministic CSV plus a
   minimal internal/versioned `.npz` replay artifact in Cycle 1, then a read-only
   GUI and `.lac` compatibility in Cycle 2. Benefit: immediate inspection and
   faithful replay without prematurely freezing the public schema; tradeoff: a
   temporary internal format and no first-cycle graph. **Alternatives:** `.lac`
   first improves legacy interoperability but delays hardware proof; CSV-only is
   smallest but loses typed raw data and weakens replay. **Evaluator choice and
   final resolution:** recommendation.
6. **Early decoder scope.** Ambiguity: broad sigrok support could block basic
   SBC work. **Recommendation:** raw viewing/export and Python API first; then
   implement only host behavior needed by UART, SPI, and I2C, plus a parallel-bus
   view/export. Benefit: earlier diagnostic value and evidence-driven host work;
   tradeoff: bundled/stacked decoders remain unavailable. **Alternatives:** full
   sigrok compatibility preserves breadth but is a large unrelated blocker;
   native-only decoders simplify the host but discard the ecosystem. **Evaluator
   choice and final resolution:** recommendation.
7. **Early GUI scope.** Ambiguity: the GUI phase combined shell, capture,
   rendering, decoders, editing, and management. **Recommendation:** a read-only
   PySide6 waveform viewer with zoom, pan, cursor readout, labels, and export,
   initially using replay and then the shared serial service. Benefit: bounded
   native value and early rendering/thread validation; tradeoff: sparse UX and
   CLI-first capture. **Alternatives:** a complete GUI MVP is polished but slow;
   external CSV viewers are fastest but do not validate the native application.
   **Evaluator choice and final resolution:** recommendation.
8. **Connection/discovery contract.** Ambiguity: discovery, auto-selection,
   stable identity, TCP, and persistence were conflated. **Recommendation:**
   require `--port PATH`, provide best-effort VID/PID listing, allow an explicit
   metadata override, and never silently choose among multiple devices. Benefit:
   deterministic real-board operation; tradeoff: manual selection. **Alternatives:**
   auto-selecting the first device is convenient but unsafe; robust persistence
   first is polished but unnecessary for capture. **Evaluator choice and final
   resolution:** recommendation.
9. **First physical acceptance evidence.** Ambiguity: the broad hardware matrix
   lacked a minimal fixture and pass criteria. **Recommendation:** use a known
   periodic signal and check V2 identity, shape/width, nonconstant samples, edge
   polarity, approximate frequency, clean close, and a second capture after
   reopen; add fixed-high/low lines when practical. Benefit: objective bit/timing
   and lifecycle evidence; tradeoff: requires documented wiring/source.
   **Alternatives:** identity plus nonempty data is easy but can accept corrupt
   captures; the full matrix gives confidence but blocks early use. **Evaluator
   choice and final resolution:** recommendation.
10. **Early OS/distribution promise.** Ambiguity: cross-platform support and
    packaged delivery were not separated. **Recommendation:** Python 3.12 source
    installs for Cycles 1-2, non-hardware CI on Linux/macOS, and hardware smoke on
    the attached host; package later. Benefit: portability feedback without
    packaging blocking function; tradeoff: users install dependencies.
    **Alternatives:** package first is convenient but lets distribution dominate;
    single-OS development is fast locally but accumulates portability risk.
    **Evaluator choice and final resolution:** recommendation.
11. **Protocol evidence precedence.** Ambiguity: firmware source, C# behavior,
    and deployed wire bytes can disagree. **Recommendation:** for the recorded V2
    version, successful known-good C#/board byte traces are authoritative for
    compatibility, firmware explains intent, and C# source fills trace gaps;
    discrepancies become provenance-tagged fixtures and compatibility notes.
    Benefit: talks to the deployed board; tradeoff: may preserve accidental wire
    behavior. **Alternatives:** firmware-only risks build/packing differences;
    C#-only risks reproducing client/runtime bugs. **Evaluator choice and final
    resolution:** recommendation.
12. **Timeout/cancellation behavior.** Ambiguity: full state/cancellation design
    could block capture, but an unbounded trigger wait is unusable.
    **Recommendation:** finite timeouts, exception/Ctrl-C-safe close, three basic
    states, and the characterized internal V2 `0xFF` recovery byte followed by
    drain and close/reopen/re-identification. Defer a public/general abort API.
    Benefit: bounded reusable behavior with little concurrency machinery;
    tradeoff: cancellation remains an internal V2 recovery path rather than a
    general protocol abstraction. **Alternatives:** complete abort/state
    semantics are robust but broad; close-only recovery can leave firmware
    capturing; no cancellation is small but can hang and leak ports.
    **Evaluator choice and final resolution:** recommendation as refined by the
    device/protocol review.

## Long-range outcomes and current qualifications

1. A typed Python library is the single implementation of device access,
   capture validation, capture processing, file formats, measurements, and
   decoder execution.
2. The accepted scriptable CLI and local React/TypeScript/Vite browser
   application consume that library without duplicating business logic.
3. Serial operation is accepted on macOS. TCP, stable-device discovery, and
   support on any other operating system require later reviewed work.
4. Replay schema 2 and the generalized self-timed CSV contract are the accepted
   native formats. `.lac` is excluded unless a later parity cycle approves it.
5. Focused checked-in UART/SPI/I2C decoder support without pythonnet or runtime
   C# compilation is the proposed Cycle 3 direction; stacking and broader
   decoder compatibility are later candidates.
6. Unit, contract, integration, browser, performance, and opt-in hardware tests
   exist or are added with their owning approved subsystem.
7. Self-contained artifacts and additional platform support remain Cycle 4-or-
   later decisions. The current accepted delivery is source-installed and
   macOS-only.

## Existing system map

Use these files as the primary sources when establishing compatibility:

- GUI and application orchestration:
  `Software/LogicAnalyzer/LogicAnalyzer/MainWindow.axaml.cs`
- GUI controls and editing behavior:
  `Software/LogicAnalyzer/LogicAnalyzer/Controls/`
- Capture dialogs and secondary workflows:
  `Software/LogicAnalyzer/LogicAnalyzer/Dialogs/`
- Device protocol and capture processing:
  `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs`
- Multi-device composition:
  `Software/LogicAnalyzer/SharedDriver/MultiAnalyzerDriver.cs`
- Domain models and limits:
  `Software/LogicAnalyzer/SharedDriver/CaptureSession.cs`,
  `AnalyzerChannel.cs`, `CaptureModes.cs`, and `BurstInfo.cs`
- Current platform discovery:
  `Software/LogicAnalyzer/SharedDriver/DeviceDetector.cs`
- Existing command-line behavior:
  `Software/LogicAnalyzer/CLCapture/`
- Existing terminal UI behavior:
  `Software/LogicAnalyzer/TerminalCapture/`
- Capture file models:
  `Software/LogicAnalyzer/LogicAnalyzer/Classes/ExportedCapture.cs` and
  `SampleRegion.cs`
- Sigrok compatibility implementation:
  `Software/LogicAnalyzer/LogicAnalyzer/SigrokDecoderBridge/`
- Vendored decoders:
  `Software/decoders/`
- Signal-description language:
  `Software/LogicAnalyzer/SignalDescriptionLanguage/`
- Firmware-side protocol structures and dispatch:
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Structs.h` and
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c`

Known issues that should become regression tests include:

- macOS discovery is currently unimplemented.
- `CLCapture` rejects both `.csv` and `.lac` because its extension condition
  uses `||` where `&&` was intended.
- Several channel-count validations compare an array length with zero using
  `< 0`, which can never detect an empty array.
- Binary request compatibility currently depends on implicit C and .NET
  structure padding/alignment.
- File, validation, and capture behavior is duplicated among front ends.
- Decoder discovery dynamically generates and compiles C# wrapper types.

## Target architecture

Create the new implementation under:

```text
Software/LogicAnalyzerPy/
├── pyproject.toml
├── README.md
├── src/pico_logic_analyzer/
│   ├── __init__.py
│   ├── model/
│   ├── protocol/
│   ├── transport/
│   ├── driver/
│   ├── decoders/
│   ├── formats/
│   ├── analysis/
│   ├── cli/
│   └── web/
├── web/
│   ├── src/
│   └── tests/
├── tests/
│   ├── unit/
│   ├── protocol/
│   ├── decoder/
│   ├── compatibility/
│   ├── implementation/
│   ├── packaging/
│   └── hardware/
└── testdata/
    ├── protocol/
    ├── captures/
    ├── decoder/
    └── legacy/
```

The accepted stack through Cycle 2 is:

- Python 3.12.
- Standard-library dataclasses and enums for the domain model.
- NumPy for raw sample storage, extraction, editing, and measurements.
- pySerial for serial access and cross-platform USB-port discovery.
- A loopback-only Python web service plus React, TypeScript, Vite, Canvas, and
  Playwright for the local browser application.
- pytest, frontend unit/browser tests, Ruff, and strict mypy checks.
- Hash-locked Python and JavaScript dependency sets and deterministic checked-
  in production assets.

TCP, desktop packaging, and additional supported operating systems are later
decisions. PySide6/Qt and an embedded browser are not part of the accepted
Cycle 2 architecture.

Do not make `asyncio` a required foundation. Prefer synchronous core APIs with
clear cancellation and timeout semantics. Run blocking capture and decoder work
outside the local server request loop. An optional async wrapper may be added
after the core API stabilizes.

## Architectural rules

1. `web` and `cli` may depend on the public library; the public library must not
   depend on either front end.
2. Transport code only moves bytes. Protocol code only frames/parses bytes.
   Driver/application services own state transitions and capture orchestration.
3. All binary layouts must use explicit byte order, sizes, and padding. Never
   rely on native `struct` alignment.
4. Test doubles implement the same transport protocol as serial and TCP.
5. Raw capture words are the canonical sample representation. Per-channel
   arrays are derived lazily or vectorially and must not become lists of Python
   integer objects for large captures.
6. File parsing is separate from domain models and must validate untrusted
   input. Do not reproduce Newtonsoft `TypeNameHandling` behavior.
7. Decoder execution is UI-independent and must be callable from Python and
   the CLI.
8. Decoder failures must be isolated and reported with decoder identity,
   configuration, and traceback; one failing decoder must not corrupt a
   capture.
9. Hardware-mutating operations such as bootloader entry and Wi-Fi
   configuration require explicit user intent and remain opt-in in tests.
10. Every phase ends with tests and artifacts that the next phase can consume.

## Orchestration protocol

Cycle-specific approved contracts define orchestration, batch assignment,
integration, verification, checkpoints, and rollback. Cycle 1 uses
`ORCHESTRATION.md` and `BATCH_EXECUTION.md`; Cycle 2 uses the corresponding
`CYCLE2_` contracts. This roadmap supplies historical and technical context. It
does not independently authorize an agent to start Cycle 3 or a later cycle,
select unsettled scope, or bypass a batch gate.

## Phase 0: Inventory, decisions, and repository scaffold

### Work package P0-A: Feature inventory

Produce `docs/feature-parity.md` in the new project. Enumerate current behavior
and classify each feature as:

- required for CLI milestone;
- required for an interactive-application milestone;
- required before C# retirement;
- intentionally changed or deferred.

At minimum cover device enumeration, serial/TCP connection, all trigger modes,
all channel modes, burst capture/measurement, multi-device capture, abort,
bootloader, blink, voltage, Wi-Fi settings, capture creation/editing, regions,
measurements, signal composer, `.lac`, CSV, decoder stacking, settings, and
known-device persistence.

### Work package P0-B: Technical decisions

Record short architecture decision records for:

- the accepted local React/TypeScript/Vite browser boundary and any separately
  approved later frontend change;
- raw sample-word representation;
- synchronous core I/O and UI workers;
- pure-Python sigrok compatibility host;
- versioned capture schema and legacy reader;
- packaging tool and supported OS/architectures.

### Work package P0-C: Scaffold

Create `pyproject.toml`, source/test layouts, console entry point, lint/type/test
configuration, basic logging, and a minimal CI workflow. Pin direct dependencies
and document how locks are updated. This scaffold and the optional locked web
runtime are complete through Cycle 2; production uses checked-in Vite assets and
does not require Node or runtime network access.

### Phase 0 gate

- Package installs in a clean virtual environment.
- `python -m pico_logic_analyzer --help` or the chosen console script works.
- Lint, type checking, unit-test discovery, and the approved production-browser
  smoke pass on the supported macOS surface.
- Feature inventory and decisions have been reviewed.

This complete Phase 0 gate applies before broad parity work. Historical Cycle 1
validation covered Linux and macOS, but the current accepted support claim is
macOS only.

## Phase 1: Protocol characterization and golden test data

This phase blocks broad production driver implementation. Cycle 1 is an explicit
exception: an agent may implement the smallest identity/8-channel serial slice
in parallel with its corresponding traced fixtures. No other protocol surface
may be added ahead of characterization.

### Work package P1-A: Protocol specification

Write `docs/device-protocol.md` from both firmware and C# sources. Specify:

- frame start `0x55 0xAA`, end `0xAA 0x55`, escape `0xF0`, and escaping rules;
- commands 0 through 6 and command-specific payloads/responses;
- capture request field offsets, byte order, padding, and total size;
- identity response sequence and firmware-version requirements;
- capture result prefix, width-dependent sample words, timestamp marker, and
  timestamp payload;
- serial settings, TCP behavior, timeout behavior, cancellation, and reconnect;
- trigger types, delays, limits, external trigger handling, and burst rules;
- differences between firmware variants if they are supported.

Use a field-offset table and show complete example frames.

### Work package P1-B: Golden vectors

Add immutable fixtures for:

- every command containing no payload;
- reserved bytes appearing inside payloads;
- edge, complex, fast, and blast requests;
- 8-, 16-, and 24-channel captures;
- burst captures with and without timing data;
- fragmented and truncated responses;
- malformed lengths and error responses.

Where possible, generate request bytes from the existing C# implementation and
confirm them against the firmware struct. Store provenance beside each fixture.
Fixture generation utilities must be separate from the tests so tests do not
recompute expected values with the same implementation under test.

### Later parity candidate P1-C: Legacy capture corpus

This work was not accepted or delivered in Cycle 2. Only if a later approved
cycle selects `.lac` interoperability, collect or construct sanitized fixtures
covering:

- current per-channel sample arrays;
- the legacy packed `Samples` field;
- regions in both directions;
- burst metadata;
- one, several, and 24 channels;
- absent optional properties and unknown extra properties;
- malformed/untrusted JSON.

### Phase 1 gate

- Protocol specification is sufficient to implement a client without reading
  the C# driver.
- Golden request frames match both C# output and firmware layout.
- Test-data provenance is documented.
- Any uncertainty about struct padding or firmware variants is resolved with a
  device trace or a small C/C# layout probe.

## Phase 2: Domain, protocol, and file-format core

### Work package P2-A: Domain model

Implement typed models for device information, capture configuration, trigger,
channel metadata, capture data, bursts, regions, and decoder annotations.
Validation must return actionable exceptions rather than generic booleans or
silently caught errors.

Test boundary values for frequencies, channel modes, trigger ranges,
pre/post-sample limits, loop counts, empty/duplicate channels, and external
triggers.

### Work package P2-B: Protocol codec

Implement pure functions for frame encoding/decoding, request encoding, identity
parsing, and capture payload parsing. Add property tests for escaping and stream
fragmentation. Enforce maximum response sizes before allocating arrays.

### Work package P2-C: Capture formats

Accepted through Cycle 2:

- bounded inert NPZ replay with schema-1 read compatibility and canonical
  schema-2 writes;
- strict generalized self-timed CSV import/export; and
- deterministic metadata and hostile-input validation without pickle or
  executable content.

`.lac` reading/writing and C# serializer interoperability were explicitly
excluded. They are Cycle 4-or-later parity candidates only if separately
approved; no current requirement may treat them as missing Cycle 2 work.

### Work package P2-D: Sample operations and measurements

Implement vectorized channel extraction, insert, delete, cut/copy/paste, shift,
region adjustment, pulse measurements, and capture slicing independently of the
frontend. Port the signal-description parser only after its grammar and examples
have characterization tests.

### Phase 2 gate

- All golden frames and payloads pass.
- Accepted replay schema-1/schema-2 and self-timed CSV fixtures load and round-
  trip through the domain model. Any future `.lac` gate belongs to its own
  approved parity cycle.
- Malformed data is rejected without uncontrolled allocation or arbitrary type
  construction.
- Sample operations have unit/property coverage for boundary and trigger/region
  adjustment behavior.
- Core modules do not import the browser frontend, CLI, or serial
  implementations.

## Phase 3: Transports, single-device driver, and consolidated CLI

### Work package P3-A: Transport contracts

Define a small transport interface supporting exact reads, writes, timeouts,
close, and cancellation. Implement scripted fake and replay transports first.
Contract-test partial reads, zero-byte reads, timeouts, disconnects, cancellation,
and close idempotency.

### Work package P3-B: Serial and TCP

Implement pySerial and socket transports. Use `serial.tools.list_ports` for
cross-platform discovery and filter VID `0x1209`, PID `0x3020`. Preserve serial
number and physical location for stable identification and later multi-device
ordering. Permit explicit ports and host/port endpoints even when discovery is
unavailable.

For Cycle 1, implement only pySerial, require an explicit port for commands, and
treat discovery as a non-authoritative listing aid. Do not auto-connect a single
match and do not select the first of multiple matches. TCP, stable identity, and
persistence remain deferred.

### Work package P3-C: Device driver

Implement a stateful device client for identity, capture, abort/reconnect,
bootloader, network configuration, voltage status, blink, and stop-blink.
Represent states explicitly, such as disconnected, idle, capturing, stopping,
and failed. Ensure resources close on every exception path.

For Cycle 1, only disconnected, idle, and capturing are required. All operations
must have finite configurable timeouts. Timeout or Ctrl-C during capture uses
the characterized internal V2 `0xFF` cancellation primitive, documented
drain/timing, close/reopen, and re-identification sequence. Disconnect or parsing
failure closes the port and reports whether reuse was proven. A richer public
abort workflow and generalized stopping/failed states remain deferred.

### Work package P3-D: CLI

Provide a single CLI with stable exit codes and human/JSON output:

```text
pico-la devices
pico-la info ENDPOINT
pico-la capture ENDPOINT ...
pico-la decode CAPTURE ...
pico-la convert INPUT OUTPUT
pico-la network configure ENDPOINT ...
pico-la bootloader ENDPOINT
```

Capture configuration should also be accepted from a versioned JSON/TOML file.
Do not encode the current CLCapture positional syntax as the only interface;
optionally accept it through a compatibility subcommand.

The authoritative Cycle 1 CLI surface, options, stdout/stderr rules, exit codes,
atomic-output behavior, CSV columns, and replay-validation command are specified
in `BATCH_EXECUTION.md`. Cycle 1 fixes the captured channel list to D0–D7 while
requiring explicit sample rate, trigger, pre/post counts, CSV path, and replay
path. Configuration files, decoding, conversion, and compatibility syntax wait
until the core command behavior is stable.

### Cycle 1 transport/CLI gate

- Fake serial behavior covers fragmentation, bounded text/binary parsing,
  timeout, the internal `0xFF` recovery sequence, disconnect, and close/reopen.
- The explicit-port CLI identifies the physical V2 device and captures D0–D7.
- Both edge polarities are fake-tested and at least the operator-selected
  polarity passes the physical smoke.
- Deterministic CSV and bounded provisional NPZ contracts pass subprocess,
  atomic-output, hostile-input, and replay tests.
- Linux and macOS CI run the approved locked Python 3.12 validation sequence.

The following broader gate applies only to later transport/CLI parity and cannot
block Cycle 1:

### Later Phase 3 parity gate

- All driver behavior passes against fake serial and fake TCP transports.
- Fragmentation, timeout, abort, and reconnect tests pass.
- CLI can perform a complete emulated/replayed capture and write the accepted
  schema-2 replay and CSV formats. `.lac` applies only if a later approved
  parity cycle adds it.
- JSON output is schema-tested and contains no progress text on stdout.
- Discovery unit/contract tests cover each platform claimed by the owning
  approved cycle; only macOS is currently supported.

## Phase 4: Sigrok decoder runtime

The work packages below mix the proposed focused Cycle 3 slice with broader
later parity. `CYCLE3_PREPARATION.md` and the Cycle 3 discovery review must
settle the focused boundary before implementation. In particular, this roadmap
does not decide trusted decoder sources, in-process versus isolated execution,
resource limits, expected-output provenance, browser integration, physical
proof, or the Cycle 3 platform claim.

### Work package P4-A: Decoder discovery and metadata

Load decoder modules directly from the bundled decoder tree. Implement metadata,
categories/tags, required/optional channels, options, annotations, annotation
rows, inputs, and outputs. Validate decoder IDs and isolate import failures.

Broad later parity may support bundled decoders, a user data directory, and an
explicit CLI path with deterministic precedence and duplicate-ID behavior.
Focused Cycle 3 instead proposes checked-in UART/SPI/I2C versions only, subject
to operator approval. Record the upstream sigrok commit or release and keep
local changes as reviewable patches where practical.

### Work package P4-B: API-v3 compatibility host

Provide the `sigrokdecode` surface required by the vendored decoders:

- constants and base `Decoder`;
- `has_channel()`;
- `wait()` including lists of alternative conditions and `matched`;
- `samplenum` and skip conditions;
- `register()` and `put()`;
- samplerate metadata;
- annotation and Python outputs.

Optimize transition searching using NumPy or precomputed edge indexes only
after the reference implementation passes correctness tests.

### Work package P4-C: Decoder stacking

Implement directed decoder pipelines where `OUTPUT_PYTHON` events feed compatible
child decoders. Validate cycles, missing input types, duplicate branch names,
channel mapping, options, and deterministic output ordering.

### Work package P4-D: Decoder verification corpus

At minimum include known signal fixtures and expected annotations for:

- I2C;
- SPI;
- UART;
- one single-wire or pulse-width protocol;
- one stacked decoder chain;
- optional/missing channels;
- invalid options and a decoder that raises an exception.

Add a smoke test that imports and inspects every bundled decoder. Compare the
representative fixtures with outputs recorded from the current application or
libsigrokdecode when available.

### Decoder gate separation

Before broad Phase 4 parity, the focused Cycle 3 decoder milestone has its own
gate:

### Proposed focused Cycle 3 decoder gate

- Subject to discovery and operator approval, only the checked-in I2C, SPI, and
  UART decoder versions are in scope.
- Pinned decoder provenance and logic fixtures enumerate the exact API-v3 calls
  exercised by those versions.
- The accepted surface may include headless library and CLI execution and may
  include browser annotation behavior; Step 4 of `CYCLE3_PREPARATION.md` must
  decide it.
- Cancellation and decoder exception isolation are tested.
- Stacking, user decoder discovery, capture-selected code, and an all-decoder
  import promise remain excluded from the proposed focused slice.

The existing bullets below are the later broad compatibility gate and cannot
block focused Cycle 3:

### Later Phase 4 parity gate

- Every supported bundled decoder imports or appears on an explicit reviewed
  incompatibility list.
- Representative annotation and stacked-output golden tests pass.
- Decoder execution works from the library and CLI without pythonnet, Roslyn,
  or a separately located Python shared library.
- A faulty decoder produces a scoped error and does not invalidate the capture.
- Performance is measured on small, medium, and maximum representative captures;
  correctness remains the gate, with performance regressions documented.

## Phase 5: Multi-device capture

### Work package P5-A: Composition service

Implement two-to-five-device composition, master/slave ordering, firmware
compatibility checks, per-device channel mapping, trigger compensation, capture
fan-out, cancellation, error propagation, and sample merge.

Do not reuse mutable capture arrays among per-device configurations. Verify that
one device failure cancels or closes all participating devices deterministically.

### Work package P5-B: Physical ordering and persistence

Use USB serial number and physical location to present stable device identities.
Persist explicit master/order selections using platform-appropriate user config
directories. Never silently reorder a previously saved analyzer chain when a
device is missing.

### Phase 5 gate

- Two- through five-device scenarios pass with fake transports.
- Channel mapping and trigger-offset fixtures match the current driver where its
  behavior is valid.
- Failure, timeout, and cancellation of each participating device are tested.
- Hardware verification for at least a two-device chain passes before frontend
  multi-device support is declared complete.

## Phase 6: Later interactive-application parity

Cycle 2 established the React/TypeScript/Vite local browser application as the
accepted frontend baseline. Whether a later cycle extends that surface or adds
another frontend requires a separately approved technology and platform
decision. Keep frontend state thin and business logic in the tested Python core.

### Work package P6-A: Application shell and settings

Implement menus, logging/error presentation, platform data/config paths,
remembered UI state, themes/colors, known devices, and a background-work
service. No capture or decoder work may block the browser or server request
loop.

### Work package P6-B: Capture workflow

Implement discovery, connect/disconnect, capability display, capture configuration,
validation, capture progress/state, repeat, abort, and device actions. Reuse the
same application services and validation as the CLI.

### Work package P6-C: Waveform viewer

Implement a custom-painted digital waveform with:

- channel labels/colors/visibility;
- zoom centered on cursor;
- horizontal navigation and overview;
- trigger, user, and region markers;
- annotation rows and tooltips;
- burst boundaries;
- level-of-detail rendering based on visible transitions.

Preserve the accepted bounded Canvas approach; do not allocate a DOM object for
every sample or edge. Extend the approved rendering benchmarks and tests for
empty, constant, dense-transition, and maximum-size captures.

### Work package P6-D: Decoder UI

Implement searchable/category-based decoder selection, channel mapping, typed
options, stacked pipelines, execution/cancellation, and annotation visibility.
Persist decoder configurations using stable decoder and option IDs rather than
display text or array indexes.

### Work package P6-E: File, analysis, and editing parity

Implement open/save/export, measurements, regions, sample creation, insert,
delete, shift, cut/copy/paste, and the signal composer. All transformations must
delegate to tested core functions.

### Work package P6-F: Multi-device and network workflows

Implement device composition/order, network connection/configuration, voltage
display, bootloader, blink, and device information. Require confirmations for
mutating actions.

### Phase 6 gates

Interactive-application gate:

- Discover/connect, configure capture, capture/abort, render/navigate, open/save,
  CSV export, decode, and show annotations.
- Automated production-browser workflow tests pass.
- Manual/native smoke tests pass on every platform claimed by the owning
  approved cycle; only macOS is currently supported.

Full parity gate:

- Every non-deferred item in `docs/feature-parity.md` is implemented and tested.
- Editing and region operations use core implementations.
- Multi-device and device-management workflows pass manual/hardware acceptance.
- Maximum representative captures remain interactive according to recorded
  performance thresholds.

## Phase 7: Packaging, release verification, and transition

### Work package P7-A: Reproducible builds

Build artifacts on their target OS. Bundle Python, application resources,
decoders, decoder data files, licenses, and version metadata. Ensure resource
lookup never relies on the current working directory.

Target artifacts:

- macOS `.app`, distributed in a DMG or ZIP; build/sign Apple Silicon and Intel
  variants according to the supported-platform decision;
- Linux artifacts and USB-permission installation are considered only if a
  later cycle approves Linux support;
- Python wheel/sdist for scripting users if dependency/licensing checks permit.

### Work package P7-B: Clean-machine smoke tests

On clean systems or CI images verify:

- application starts without a system Python installation;
- CLI starts and reports its version;
- decoders and their auxiliary data files load;
- a replay capture opens, renders, decodes, saves, and exports;
- settings are stored in the correct platform directory;
- missing USB permission produces a useful diagnostic;
- macOS artifact signing/notarization status is valid when enabled.

### Work package P7-C: Side-by-side release

Publish the Python application as a preview without removing the C# application.
Document known differences and provide a structured issue template containing
OS, architecture, transport, firmware version, capture settings, and logs.

### Retirement gate

The orchestrator may propose retiring the C# implementation only when:

- all required feature-parity items are complete;
- protocol and every separately approved file-compatibility suite pass;
- decoder gates pass;
- packaged smoke tests pass on every platform claimed by the release;
- the full hardware matrix below passes on supported firmware;
- at least one side-by-side preview cycle has completed without an unresolved
  data-loss, protocol, or packaging blocker;
- maintainers explicitly approve removal or archival.

## Test and verification matrix

### Always-on pull request checks

"Always-on" means once the corresponding subsystem lands. Historical Cycle 1
ran its approved Linux/macOS matrix. The accepted Cycle 2 product runs the
governed macOS Python, CLI, API, frontend, production-browser, replay/CSV/bus,
security, and performance checks. Add each future check to the required set in
the same approved cycle that introduces its subsystem; historical Linux CI does
not create a current Linux support claim.

- Ruff formatting/linting.
- Static type checking.
- Unit and property tests.
- Protocol golden tests.
- Fake serial/TCP contract tests.
- Replay-schema and self-timed CSV compatibility/security tests.
- Representative decoder tests when the focused decoder subsystem is approved;
  an all-decoder import smoke remains later parity.
- Production-browser workflow tests.
- Build/package configuration validation.

### Scheduled or release checks

- Full decoder corpus/performance tests.
- Native browser smoke on the supported macOS platform.
- Other-platform browser/native smoke only after that platform is approved.
- Clean-machine packaged application test.
- Large-capture rendering and memory benchmark.
- Dependency/license and bundled-file audit.

### Opt-in hardware acceptance matrix

#### Cycle 1 hardware gate

Provide a checked-in operator procedure and an opt-in automated smoke command.
The operator supplies the serial port and wires a known periodic source (a Pico
test/PWM output or known SBC clock is preferred) to the selected trigger channel.
When practical, wire one sampled input fixed low and another fixed high to expose
bit-order errors. The smoke must verify:

- identity/version/capabilities equal the recorded V2 baseline;
- the returned sample count and 8-channel width equal the request;
- the periodic channel is nonconstant and contains the requested edge polarity;
- measured frequency is within a documented tolerance determined by sample rate
  and fixture stability;
- fixed inputs remain fixed when those wires are present;
- the port closes cleanly; and
- a second capture succeeds after close/reopen.

The smoke must not change Wi-Fi settings, enter the bootloader, or otherwise
mutate persistent device state. Save sanitized CSV/NPZ artifacts only when the
operator explicitly requests it. The full matrix below applies to later parity
and release cycles, not Cycle 1.

Run against each supported firmware/device variant:

| Area | Cases |
| --- | --- |
| Discovery | Explicit serial port on each supported host; macOS currently |
| Identity | version, max/blast frequency, buffer, channels |
| Transport | serial and TCP |
| Width | 8-, 16-, and 24-channel capture modes |
| Trigger | edge normal/inverted, external, complex, fast, blast |
| Samples | minimum/maximum pre/post and representative full buffer |
| Burst | no timing, timing enabled, several loop counts |
| Control | abort during wait/read, reconnect, unplug/disconnect |
| Commands | voltage, blink/stop, network settings, bootloader |
| Multi-device | at least two devices, reordered devices, slave failure |

Network settings and bootloader cases must use dedicated devices or explicit
operator confirmation. Capture logic should be verified using known generated
signals where possible, with expected edge/sample positions and allowed timing
tolerances recorded in the fixture.

## Compatibility and schema policy

- Replay schema 2 is the accepted canonical native format, with bounded schema-1
  reads. `.lac` has no accepted reader or writer and requires a later explicit
  interoperability decision.
- New replay files include a schema version and sanitized application/device
  metadata defined by the accepted contract.
- Readers accept unknown fields and reject unsupported major schema versions
  with a useful error.
- Writers use deterministic field names and do not serialize Python class names.
- CLI JSON output is separately versioned from the capture-file schema.
- Protocol behavior is keyed by firmware capabilities/version when differences
  are unavoidable; avoid scattered version checks.
- Intentional behavior changes are recorded in `docs/compatibility.md` with the
  prior behavior, new behavior, reason, and tests.

## Security and robustness requirements

- Treat capture files as untrusted input. Decoder packages are executable code;
  Cycle 3 preparation must decide which exact sources are trusted and what
  isolation claim applies before any decoder execution is authorized.
- Do not deserialize arbitrary classes or evaluate capture-file content.
- Bound packet lengths and sample allocations by negotiated device limits and
  configured safety limits.
- Redact Wi-Fi passwords from logs, exceptions, CLI JSON, and persisted history.
- Never automatically execute decoders discovered inside a capture file.
- User-installed decoder discovery is outside the proposed focused Cycle 3
  slice. If later approved, state clearly that such decoders are executable
  Python code and require an explicit trusted-code policy.
- Timeouts and cancellation must release ports/sockets and leave state reusable
  or explicitly failed.

## Performance budgets to establish

Establish each baseline only when its owning subsystem first exists:

- Cycle 1/Phase 2: raw payload parsing, D0–D7 extraction, CSV, and provisional
  NPZ read/write.
- Any separately approved `.lac` phase: representative legacy/current `.lac`
  read/write.
- Focused decoder cycle: representative I2C/SPI/UART decoding.
- Multi-device phase: peak memory for maximum representative composed captures.
- Viewer phase: Cycle 2 established and enforced production-browser load,
  interaction, bus, Canvas, DOM, request-span, and row-count thresholds. Later
  cycles must preserve them or use their governed approval process.

Do not choose arbitrary pass/fail values before collecting baselines. Once
accepted, store benchmark scenarios and thresholds in the repository and treat
material regressions as release blockers or explicitly approved exceptions.

## Definition of done for every work package

A work package is complete only when:

1. Public behavior and interfaces are documented.
2. Implementation respects the architectural boundaries in this plan.
3. Positive, boundary, failure, timeout/cancellation, and malformed-input tests
   appropriate to the package exist.
4. Tests do not require physical hardware unless marked as hardware tests.
5. Lint, type checking, and affected tests pass.
6. No secrets, generated build outputs, machine-local paths, or unrelated edits
   are committed.
7. The agent provides a concise handoff with changed files, commands/results,
   compatibility notes, and remaining risks.

## Recommended orchestration order

```text
Cycle 1: V2 trace/spec subset -> codec/fake -> serial -> CLI -> CSV/NPZ
                                                        |
                                                        v
                                             physical hardware gate
                                                        |
                                                        v
Cycle 2: wider modes + replay schema 2/CSV/bus -> browser/API -> live viewer
                                                        |
                                                        v
Cycle 3 proposal: focused UART/SPI/I2C host -> approved public surfaces/proof
                                                        |
                                                        v
Cycle 4+: separately approved parity/platform work -> packaging/preview
                                                        |
                                                        v
                                             C# retirement review
```

Within a cycle, parallelize only work packages with settled interfaces. A
verification agent should derive fixtures independently while the implementation
agent builds the matching narrow surface. Do not begin a later-cycle feature
merely because an agent is idle; use spare capacity for negative tests,
documentation, and review of the current gate.

This diagram is technical sequencing context. Cycle-specific approved contracts
are authoritative for their durable objective and checkpoint order. Cycle 3 has
no approved execution contract or durable goal yet.

## First orchestration iteration

The approved Cycle 1 iteration is divided into C1-B1 through C1-B5 in
`BATCH_EXECUTION.md`. Its stopping condition is defined exclusively in
`ORCHESTRATION.md`. Do not infer completion or permission to expand scope from
the broader phases in this roadmap.

## Consciously deferred work

The accepted Cycle 2 result completed wider normal capture, replay schema 2,
generalized self-timed CSV, the local browser/API, offline and live viewing,
parallel-bus analysis, and performance gates. They are regression baselines,
not deferred Cycle 3 work.

- **Proposed Cycle 3:** focused checked-in UART, SPI, and I2C sigrok-host
  behavior. Library/CLI/browser surfaces, trust and isolation, fixtures,
  resource bounds, platform, and physical-proof choices remain pending under
  `CYCLE3_PREPARATION.md`.
- **Later parity cycles:** complex, fast, blast, external, and burst/timestamp
  modes; graceful protocol abort; broad firmware compatibility; all bundled
  decoders; decoder stacking; user decoder directories; editing, regions,
  signal composer, measurements, advanced annotations, settings/themes,
  overview, `.lac` interoperability if approved, and further optimization.
- **Later connectivity/device cycles:** TCP, Wi-Fi, voltage, blink, bootloader,
  remembered/hot-plug devices, stable physical ordering, and multi-device
  capture.
- **Release/platform cycle:** macOS app/DMG, signing, notarization,
  universal/multiple architecture builds, and clean-machine tests; Linux
  support and artifacts only after a separately approved platform decision.

Deferral is not deletion. Keep these features in the parity inventory and bring
them forward only through a new reviewed cycle with explicit fixtures and gates.
