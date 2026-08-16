# Python Logic Analyzer Rewrite: Implementation and Verification Plan

> **Document role:** This is the technical roadmap. Cycle 1 objective, scope,
> authority, validation, checkpoints, and stopping conditions are governed by
> [`ORCHESTRATION.md`](../../ORCHESTRATION.md). Repeatable batch mechanics and
> concrete Cycle 1 batches are governed by
> [`BATCH_EXECUTION.md`](../../BATCH_EXECUTION.md). Where execution instructions
> here overlap, the two top-level documents are authoritative. Commit-anchored
> domain reviews are stored in
> [`docs/rewrite-reviews/`](../../docs/rewrite-reviews/README.md).

## Purpose

This document is an execution plan for an orchestrating agent coordinating a
team of implementation and verification agents. The objective is to replace
the current .NET/Avalonia logic-analyzer applications with a Python package,
CLI, and desktop GUI that run on Linux and macOS while preserving device,
capture-file, decoder, and user-visible behavior.

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

The first useful delivery is source-installed on Python 3.12. Non-hardware tests
run on Linux and macOS, while the physical smoke test runs on whichever supported
host has the board. Packaging, broad firmware compatibility, automated device
selection, TCP, wider captures, advanced triggers, decoder compatibility, and a
full GUI are later cycles.

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

#### Cycle 2: wider capture and basic native viewing

Add 16- and 24-channel normal capture, `.lac` compatibility, and a read-only
PySide6 viewer. The viewer initially opens replay/CSV captures, renders supported
digital channels, and provides zoom, pan, cursor time/sample readout, channel
labels, and export. After replay viewing is stable, connect it to the same proven
serial capture service. Add a simple parallel-bus value table/export before
claiming whole-bus SBC debugging support.

#### Cycle 3: focused decoder support

Implement only the sigrok host behavior exercised by checked-in UART, SPI, and
I2C fixtures. Keep the public Python capture/analysis API usable without the GUI.
Broader API-v3 compatibility, decoder stacking, user decoder directories, and
the all-decoder import gate are later parity work.

#### Cycle 4 and later: parity and distribution

Complete advanced triggers/capture modes, decoder breadth, editing, TCP,
multi-device support, device-management workflows, optimized rendering, and
self-contained distribution in evidence-driven increments. Apply the detailed
work packages below only when their prerequisite cycle has passed.

## Reviewed decision log

The following choices were reviewed one at a time by an independent evaluator.
When options tied, the review policy was to retain the original recommendation.

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
    states, and close/reopen recovery; characterize protocol abort later. Benefit:
    safe reusable behavior with little concurrency machinery; tradeoff: initial
    cancellation is not graceful in-protocol abort. **Alternatives:** complete
    abort/state semantics are robust but broad; no cancellation is small but can
    hang and leak ports. **Evaluator choice and final resolution:** recommendation.

## Desired outcomes

1. A typed Python library is the single implementation of device access,
   capture validation, capture processing, file formats, measurements, and
   decoder execution.
2. A scriptable CLI and a PySide6 desktop GUI consume that library without
   duplicating business logic.
3. Serial and TCP devices work on Linux and macOS. USB discovery uses VID/PID,
   serial number, and physical location where available.
4. Existing `.lac` files remain readable. New files have an explicit versioned
   schema and round-trip without data loss.
5. Bundled sigrok API-v3 Python decoders run without pythonnet or runtime C#
   compilation, including stacked decoders.
6. Unit, contract, integration, GUI, packaging, and opt-in hardware acceptance
   tests exist and run in CI where appropriate.
7. Linux and macOS users receive self-contained desktop artifacts and can also
   install/use the Python package and CLI.

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
│   └── gui/
├── tests/
│   ├── unit/
│   ├── protocol/
│   ├── decoder/
│   ├── compatibility/
│   ├── gui/
│   ├── packaging/
│   └── hardware/
└── testdata/
    ├── protocol/
    ├── captures/
    ├── decoder/
    └── legacy/
```

Recommended baseline stack:

- Python 3.12 or newer, subject to PySide6 packaging support.
- Standard-library dataclasses and enums for the domain model.
- NumPy for raw sample storage, extraction, editing, and measurements.
- pySerial for serial access and cross-platform USB-port discovery.
- Standard-library sockets for TCP transport.
- PySide6 Qt Widgets for the desktop application.
- pytest, pytest-qt, Hypothesis, and coverage for tests.
- Ruff plus mypy or Pyright for static checks.
- `pyside6-deploy` for initial application packaging; reconsider only if
  packaging spikes reveal a blocker.

Do not make `asyncio` a required foundation. Prefer synchronous core APIs with
clear cancellation and timeout semantics. Run blocking capture and decoder work
outside the Qt UI thread. An optional async wrapper may be added after the core
API stabilizes.

## Architectural rules

1. `gui` and `cli` may depend on the public library; the public library must not
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

Top-level orchestration policy is defined in `ORCHESTRATION.md`; per-batch
assignment, integration, verification, checkpoint, and rollback procedures are
defined in `BATCH_EXECUTION.md`. This roadmap supplies technical work packages
for those documents to reference. It does not independently authorize an agent
to start a later cycle or bypass a batch gate.

## Phase 0: Inventory, decisions, and repository scaffold

### Work package P0-A: Feature inventory

Produce `docs/feature-parity.md` in the new project. Enumerate current behavior
and classify each feature as:

- required for CLI milestone;
- required for GUI MVP;
- required before C# retirement;
- intentionally changed or deferred.

At minimum cover device enumeration, serial/TCP connection, all trigger modes,
all channel modes, burst capture/measurement, multi-device capture, abort,
bootloader, blink, voltage, Wi-Fi settings, capture creation/editing, regions,
measurements, signal composer, `.lac`, CSV, decoder stacking, settings, and
known-device persistence.

### Work package P0-B: Technical decisions

Record short architecture decision records for:

- PySide6/Qt Widgets;
- raw sample-word representation;
- synchronous core I/O and UI workers;
- pure-Python sigrok compatibility host;
- versioned capture schema and legacy reader;
- packaging tool and supported OS/architectures.

### Work package P0-C: Scaffold

Create `pyproject.toml`, source/test layouts, console entry point, lint/type/test
configuration, basic logging, and a minimal CI workflow. Pin direct dependencies
and document how locks are updated. Include a placeholder GUI entry point that
can start and exit in an offscreen test.

For Cycle 1, put GUI dependencies in an optional dependency group and omit the
placeholder GUI/offscreen test. Activate them when Cycle 2 viewer work begins.

### Phase 0 gate

- Package installs in a clean virtual environment.
- `python -m pico_logic_analyzer --help` or the chosen console script works.
- Lint, type checking, unit-test discovery, and a headless Qt smoke test pass on
  Linux and macOS CI.
- Feature inventory and decisions have been reviewed.

This complete Phase 0 gate applies before broad parity work. The Cycle 1 gate
requires only package installation, CLI help, lint/type/unit checks on Linux and
macOS, and the decisions necessary for the narrow V2 capture slice.

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

### Work package P1-C: Legacy capture corpus

Collect or construct sanitized `.lac` fixtures covering:

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

Implement:

- legacy `.lac` reader;
- versioned new `.lac` writer/reader;
- CSV writer compatible with current header/sample behavior;
- deterministic JSON output for tests and version control.

Document the new schema. Preserve unknown legacy fields when feasible, or
explicitly report what cannot round-trip. Consider compression only after
baseline compatibility is proven.

### Work package P2-D: Sample operations and measurements

Implement vectorized channel extraction, insert, delete, cut/copy/paste, shift,
region adjustment, pulse measurements, and capture slicing independently of the
GUI. Port the signal-description parser only after its grammar and examples
have characterization tests.

### Phase 2 gate

- All golden frames and payloads pass.
- All valid legacy captures load and round-trip through the domain model.
- Malformed data is rejected without uncontrolled allocation or arbitrary type
  construction.
- Sample operations have unit/property coverage for boundary and trigger/region
  adjustment behavior.
- Core modules do not import Qt, CLI, or serial implementations.

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
must have finite configurable timeouts. Timeout, Ctrl-C, disconnect, or parsing
failure closes the serial port; close/reopen is the defined recovery mechanism.
Implement stopping/failed refinements and protocol abort only after the abort
exchange has traced fixtures.

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

The Cycle 1 CLI surface is smaller: `devices`, `info --port PATH`, and
`capture --port PATH`. Capture must expose channel selection, rising/falling
edge, trigger channel, output path/format, and timeout. Frequency and pre/post
sample counts may begin as recorded safe defaults, but the command must print or
store their actual values and validation limits. Configuration files, JSON
machine output, decoding, conversion, and compatibility syntax can wait until
the core command behavior is stable.

### Phase 3 gate

- All driver behavior passes against fake serial and fake TCP transports.
- Fragmentation, timeout, abort, and reconnect tests pass.
- CLI can perform a complete emulated/replayed capture and write `.lac` and CSV.
- JSON output is schema-tested and contains no progress text on stdout.
- On both Linux and macOS, discovery unit/contract tests correctly interpret
  representative pySerial port records.

## Phase 4: Sigrok decoder runtime

### Work package P4-A: Decoder discovery and metadata

Load decoder modules directly from the bundled decoder tree. Implement metadata,
categories/tags, required/optional channels, options, annotations, annotation
rows, inputs, and outputs. Validate decoder IDs and isolate import failures.

Support bundled decoders, a user data directory, and an explicit CLI path.
Define deterministic precedence and duplicate-ID behavior. Record the upstream
sigrok commit or release from which bundled decoders came; keep local changes as
reviewable patches where practical.

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

### Phase 4 gate

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
- Hardware verification for at least a two-device chain passes before GUI
  multi-device support is declared complete.

## Phase 6: PySide6 desktop GUI

Keep GUI state thin. Introduce view models/controllers where they make workflows
testable, but do not create a framework-heavy abstraction layer.

### Work package P6-A: Application shell and settings

Implement menus, logging/error presentation, platform data/config paths,
remembered windows, themes/colors, known devices, and a background-work service.
No capture or decoder work may block the Qt event loop.

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

Do not allocate a Qt item for every sample or edge. Add rendering benchmarks and
tests for empty, constant, dense-transition, and maximum-size captures.

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

GUI MVP gate:

- Discover/connect, configure capture, capture/abort, render/navigate, open/save,
  CSV export, decode, and show annotations.
- pytest-qt workflow tests pass under the offscreen platform.
- Manual smoke tests pass on macOS and Linux native desktops.

Full parity gate:

- Every non-deferred item in `docs/feature-parity.md` is implemented and tested.
- Editing and region operations use core implementations.
- Multi-device and device-management workflows pass manual/hardware acceptance.
- Maximum representative captures remain interactive according to recorded
  performance thresholds.

## Phase 7: Packaging, release verification, and transition

### Work package P7-A: Reproducible builds

Build artifacts on their target OS. Bundle Python, Qt, application resources,
decoders, decoder data files, licenses, and version metadata. Ensure resource
lookup never relies on the current working directory.

Target artifacts:

- macOS `.app`, distributed in a DMG or ZIP; build/sign Apple Silicon and Intel
  variants according to the supported-platform decision;
- Linux portable archive or AppImage, plus installation documentation and udev
  rules for USB permissions;
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
- protocol and legacy-file compatibility suites pass;
- decoder gates pass;
- Linux and macOS packaged smoke tests pass;
- the full hardware matrix below passes on supported firmware;
- at least one side-by-side preview cycle has completed without an unresolved
  data-loss, protocol, or packaging blocker;
- maintainers explicitly approve removal or archival.

## Test and verification matrix

### Always-on pull request checks

"Always-on" means once the corresponding subsystem lands. A missing later-cycle
subsystem is not a Cycle 1 failure. Cycle 1 always runs Ruff, static type checks,
unit/protocol golden tests, fake/replay serial contract tests, CSV/NPZ round-trip
tests, and CLI tests on Linux and macOS. Add each remaining check to the required
set in the same change that introduces its subsystem.

- Ruff formatting/linting.
- Static type checking.
- Unit and property tests.
- Protocol golden tests.
- Fake serial/TCP contract tests.
- Legacy capture compatibility tests.
- Representative decoder tests and all-decoder import smoke test.
- pytest-qt offscreen workflow tests.
- Build/package configuration validation.

### Scheduled or release checks

- Full decoder corpus/performance tests.
- Linux native GUI smoke test under X11 and, where practical, Wayland.
- macOS native GUI smoke test.
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
| Discovery | Linux USB, macOS USB, explicit serial port |
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

- The legacy `.lac` reader is permanent unless a future migration policy says
  otherwise.
- New capture files include a schema version and application version.
- Readers accept unknown fields and reject unsupported major schema versions
  with a useful error.
- Writers use deterministic field names and do not serialize Python class names.
- CLI JSON output is separately versioned from the capture-file schema.
- Protocol behavior is keyed by firmware capabilities/version when differences
  are unavoidable; avoid scattered version checks.
- Intentional behavior changes are recorded in `docs/compatibility.md` with the
  prior behavior, new behavior, reason, and tests.

## Security and robustness requirements

- Treat capture files and decoder packages as untrusted input.
- Do not deserialize arbitrary classes or evaluate capture-file content.
- Bound packet lengths and sample allocations by negotiated device limits and
  configured safety limits.
- Redact Wi-Fi passwords from logs, exceptions, CLI JSON, and persisted history.
- Never automatically execute decoders discovered inside a capture file.
- User-installed decoders are executable Python code; state this clearly in the
  UI/docs and require an explicit trusted decoder directory.
- Timeouts and cancellation must release ports/sockets and leave state reusable
  or explicitly failed.

## Performance budgets to establish

During Phase 2, record baseline hardware and set reviewed thresholds for:

- parsing a maximum capture payload;
- extracting all channels;
- loading/saving representative `.lac` files;
- decoding representative I2C/SPI/UART captures;
- first waveform paint;
- pan/zoom frame latency;
- peak memory for maximum single- and multi-device captures.

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
Cycle 2: wider modes + .lac -> replay viewer -> live basic viewer
                                                        |
                                                        v
Cycle 3: focused UART/SPI/I2C host + parallel-bus table/export
                                                        |
                                                        v
Cycle 4+: advanced P1-P6 parity work -> P7 packaging/preview
                                                        |
                                                        v
                                             C# retirement review
```

Within a cycle, parallelize only work packages with settled interfaces. A
verification agent should derive fixtures independently while the implementation
agent builds the matching narrow surface. Do not begin a later-cycle feature
merely because an agent is idle; use spare capacity for negative tests,
documentation, and review of the current gate.

This diagram is technical sequencing context. `ORCHESTRATION.md` is
authoritative for the active durable objective, and `BATCH_EXECUTION.md` is
authoritative for Cycle 1 checkpoint order.

## First orchestration iteration

The approved Cycle 1 iteration is divided into C1-B1 through C1-B5 in
`BATCH_EXECUTION.md`. Its stopping condition is defined exclusively in
`ORCHESTRATION.md`. Do not infer completion or permission to expand scope from
the broader phases in this roadmap.

## Consciously deferred work

The orchestrator must keep these items out of Cycle 1 unless a prerequisite for
the proven V2 serial path is discovered and documented:

- **Cycle 2:** 16/24-channel normal capture; `.lac` legacy/current compatibility;
  read-only replay and live waveform viewer; simple parallel-bus table/export.
- **Cycle 3:** focused UART, SPI, and I2C sigrok-host behavior and decoder UI
  integration only after its headless fixtures pass.
- **Later parity cycles:** complex, fast, blast, external, and burst/timestamp
  modes; graceful protocol abort; broad firmware compatibility; all bundled
  decoders; decoder stacking; user decoder directories; editing, regions,
  signal composer, measurements, annotations, settings/themes, overview, and
  maximum-capture optimization.
- **Later connectivity/device cycles:** TCP, Wi-Fi, voltage, blink, bootloader,
  remembered/hot-plug devices, stable physical ordering, and multi-device
  capture.
- **Release cycle:** AppImage/portable Linux artifact, macOS app/DMG, signing,
  notarization, universal/multiple architecture builds, clean-machine tests,
  and polished USB-permission installation.

Deferral is not deletion. Keep these features in the parity inventory and bring
them forward only through a new reviewed cycle with explicit fixtures and gates.
