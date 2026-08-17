# Cycle 2 bounded discovery review

- Review baseline commit: `e85fc642b922d089e7ffe019128f34fda65d1fc9`
- Review baseline tree: `bff37f32223cc022e0d2d4b2c416ab45ecb42170`
- Completed: `2026-08-17T05:46:27Z`
- Status: preparatory discovery complete; recommendations require approval
  before Cycle 2 orchestration is written

## Purpose and boundary

This review identifies the smallest useful and verifiable Cycle 2 shape after
the accepted Cycle 1 vertical slice. It is evidence for discussing scope,
authority, batch boundaries, and completion proof. It is not an implementation
plan, does not authorize Cycle 2 work, and does not alter the completed Cycle 1
contracts.

No firmware, hardware, dependency, workflow, or product operation was performed
for this review. Cycle 2 must receive new top-level orchestration and batch
documents, common-commit review approval, and a new durable goal before
implementation begins.

## Evidence inspected

### Accepted Python baseline

- [`docs/cycle-1-completion.md`](cycle-1-completion.md) and the five accepted
  evidence manifests.
- Current models, V2 codec, serial driver, capture/export/replay code, CLI,
  recovery code, and independent tests under `Software/LogicAnalyzerPy/`.
- Current Linux/macOS Python 3.12 workflow and hash-pinned dependency lock.

### Firmware and C# compatibility sources

- V2 request and mode definitions in
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Structs.h`,
  `LogicAnalyzer.c`, `LogicAnalyzer_Capture.c`, and board settings.
- Mode selection, buffer limits, request composition, word reads, and channel
  extraction in `SharedDriver/AnalyzerDriverBase.cs` and
  `SharedDriver/LogicAnalyzerDriver.cs`.
- Current `.lac` producers/consumers in TerminalCapture `FileOperations.cs` and
  `LACEnvelope.cs`, plus the Avalonia application's `ExportedCapture.cs`,
  `CaptureSession.cs`, `AnalyzerChannel.cs`, `SampleRegion.cs`, and open/save
  paths.
- Historical `.lac` shapes at commits `f33e8ab`, `fc05977`, and `02a6aab`.
- Existing Avalonia `SampleViewer`, `SamplePreviewer`, `ChannelViewer`, and main
  window navigation/capture paths as behavioral references only.

### External platform evidence

Qt for Python is the official Python binding for Qt and currently documents
Python 3.10+, Linux, and macOS support, including macOS `x86_64` and `arm64`.
PySide wheels include Qt binaries. Exact Cycle 2 versions and wheel availability
must still be frozen through a clean Python 3.12 lock/bootstrap probe:

- <https://doc.qt.io/qtforpython-6/gettingstarted.html>
- <https://doc.qt.io/qtforpython-6.10/overviews/qtdoc-supported-platforms.html>
- <https://doc.qt.io/qtforpython-6/>

Linux offscreen Qt tests may need system XCB/OpenGL packages even when PySide is
installed from wheels. Packaging/deployment remains outside Cycle 2.

## Discovered technical facts

### Wider normal capture

1. The native V2 capture request remains 48 bytes. It already contains 24
   channel identifiers, `channelCount`, and `captureMode` values `0`, `1`, and
   `2` for 8-, 16-, and 24-channel word modes.
2. Normal capture words are little-endian `uint8`, `uint16`, or `uint32` for
   those modes. The 24-channel mode occupies four bytes per word; only its lower
   24 bits are meaningful.
3. Firmware captures from the physical input range, then repacks requested
   channels so returned bit position `i` corresponds to request-list position
   `i`, not necessarily physical channel D`i`. The C# client extracts channels
   with the same request-order convention.
4. Word mode is selected from the highest requested physical channel: D0-D7 is
   8-bit, any D8-D15 requires 16-bit, and any D16-D23 requires 24-bit/32-bit
   storage.
5. The reported Pico 2 buffer is 393216 bytes, giving maxima of 393216,
   196608, and 98304 sample words for 8-, 16-, and 24-channel modes before other
   contract limits are applied.
6. Firmware does not safely validate every channel-list element before indexing
   `pinMap`. The Python client must reject non-integer, duplicate, out-of-range,
   or otherwise inconsistent lists before sending a request.

### Capture and interchange formats

1. Cycle 1 hard-codes `uint8`, D0-D7, eight labels, and eight mappings in its
   model, codec, CSV, and replay contracts. Wider support is a deliberate model
   and schema evolution, not a parser-only change.
2. The repository contains no checked-in `.lac` files. Compatibility cannot be
   accepted from source inspection alone.
3. At least four `.lac` families exist in source history:

   - current TerminalCapture: `{ "Settings": CaptureSession }`;
   - current Avalonia: `{ "Settings": CaptureSession, "Samples": null or
     packed words, "SelectedRegions": ... }`, normally with per-channel sample
     arrays inside `Settings.CaptureChannels`;
   - older Avalonia: `CaptureSettings` plus packed `UInt128[] Samples` and
     regions;
   - earliest inspected form: packed `uint[] Samples`, `ChannelTexts`, and an
     older selected-region object.

4. C# uses Newtonsoft.Json defaults plus a custom region-color converter. Exact
   `UInt128` JSON representation, null/default behavior, case handling, and
   historical round-trip behavior require generated fixtures from the relevant
   serializer versions.
5. The current host has no `dotnet` executable. Producing authoritative `.lac`
   fixtures therefore requires an approved .NET 8/NuGet bootstrap, a controlled
   CI fixture job, or operator-supplied sanitized real captures.
6. Cycle 1 CSV is self-timed and deterministic. The current C# CSV is a separate
   channel-only format and must not silently redefine the Python default.

### Viewer and analysis surface

1. The existing Avalonia viewer eagerly computes transition intervals for all
   samples, and its preview loops across every sample and visible channel. It is
   useful behavioral evidence but should not be line-for-line ported.
2. A Qt item per sample or edge would be unbounded. The Python viewer needs a
   Qt-independent viewport/transition model and one custom-painted widget whose
   work is proportional to visible transitions and pixels.
3. No parallel-bus table exists in the current application. Its bit ordering,
   sampling rule, table row semantics, and export schema therefore require a new
   explicit contract rather than compatibility inference.

### Documentation and delivery debt

- `README.md` now reflects Cycle 1, but `docs/cli-contract.md`, the project
  description, and comments in `requirements-dev.in` still contain Cycle 1
  scaffold/batch wording. They should be corrected mechanically in the first
  Cycle 2 batch without changing accepted Cycle 1 behavior.
- The current workflow is named and authorized specifically for Cycle 1. Cycle
  2 must explicitly authorize its rename/replacement or a new GUI workflow and
  must avoid running two redundant full matrices on every Python change.

## Recommended Cycle 2 target

Deliver one source-installed Python 3.12 application that preserves the Cycle 1
CLI and adds:

1. normal edge-trigger capture of an explicitly ordered, unique subset of
   physical D0-D23;
2. correct 8-, 16-, and 24-channel word modes selected by the highest physical
   channel, with raw dtypes `uint8`, `uint16`, and `uint32` respectively;
3. backward loading of provisional replay schema 1 and a generalized replay
   schema 2 for arbitrary channel sets and word dtypes;
4. strict import of the exact self-timed Python CSV contract, generalized to
   explicit captured-channel columns while preserving byte-identical Cycle 1
   D0-D7 output;
5. bounded readers for the fixture-proven historical/current `.lac` families
   and a deterministic, explicitly versioned `.lac` writer that remains
   readable by the current C# application where representable;
6. a read-only PySide6 Qt Widgets application that opens replay, self-timed CSV,
   and `.lac`, then renders digital waveforms with channel labels/visibility,
   horizontal pan, cursor-centered zoom, cursor sample/time/value readout,
   trigger marker, and export;
7. live capture through the already proven serial application service only
   after offline viewing is accepted; and
8. a Qt-independent parallel-bus table/export with ordered LSB-to-MSB data
   channels, transition rows, and optional sampling on a distinct strobe
   channel's rising or falling edge.

This target is useful for an 8-bit SBC because a 24-channel capture can combine
an 8-bit data bus, selected address/control lines, and a strobe, while the bus
table converts those samples into inspectable values. It does not claim full
CPU-cycle or protocol decoding.

## Recommendations requiring approval

### 1. Keep firmware fixed

**Recommendation:** use the same checked-in and already flashed V2 Pico 2
firmware throughout Cycle 2. Record firmware defects or throughput limits and
defer fixes to a separately reviewed system cycle.

**Benefit:** wider host behavior is compared against one stable peer, avoiding
simultaneous protocol changes. **Alternative:** permit narrowly scoped firmware
fixes, which could unblock a genuine defect but would require paired firmware
and host baselines, reflashing authority, and a larger hardware matrix.

### 2. Support explicit ordered channel subsets

**Recommendation:** allow one to 24 unique physical channel IDs in explicit
request order; require the trigger channel to be captured; derive word mode from
the highest ID; and retain separate physical IDs, display labels, mappings, and
request-bit positions.

**Benefit:** matches firmware/C# behavior and lets an SBC user select useful
data/control groups without pretending returned bit positions are physical IDs.
**Alternative:** support only exact contiguous D0-D15 and D0-D23 sets. That is
simpler to explain and test but unnecessarily removes a working hardware
capability and weakens practical probe selection.

### 3. Evolve raw samples by dtype, not by widening everything

**Recommendation:** preserve `uint8` for Cycle 1 captures and use exact
`uint16`/`uint32` arrays for wider words. Require the upper eight bits of a
24-channel word to be zero. Keep vectorized channel extraction based on request
position.

**Benefit:** preserves existing artifacts and uses memory proportional to wire
width. **Alternative:** normalize every capture to `uint32`, simplifying some
downstream code at four times the memory for 8-bit captures and changing the
accepted Cycle 1 representation.

### 4. Introduce replay schema 2 while retaining schema 1 reads

**Recommendation:** schema 2 records word dtype/mode and arbitrary ordered
channel metadata. New Cycle 2 writes use schema 2; the loader continues to
accept validated schema 1. Keep the same hostile-archive bounds and no-pickle
rules, adjusted only where wider maximum payloads require a reviewed limit.

**Benefit:** makes evolution explicit and keeps all accepted Cycle 1 evidence
replayable. **Alternative:** extend schema 1 in place, which creates ambiguous
meaning for existing validators despite the format's provisional label.

### 5. Make `.lac` compatibility corpus-first

**Recommendation:** before implementing a reader, generate immutable fixtures
with the relevant C# serializers for every identified shape, including 8/16/24
channels, packed and per-channel samples, colors/hidden/labels, regions, bursts,
null optionals, unknown fields, and malformed/oversized inputs. The Python
reader should be bounded and inert, preserve bounded unknown JSON fields for
round-trip where feasible, and never instantiate named types.

Write one canonical envelope with an explicit format-version field, current
`Settings` shape, per-channel sample arrays, and regions. Prove the current C#
application can read representable output; report unsupported historical fields
rather than silently discarding them.

**Benefit:** compatibility is based on bytes, not assumptions about
Newtonsoft.Json. **Alternative:** implement from class definitions first, which
is faster but risks accepting tests that reproduce neither historical nor
current files.

### 6. Use a thin Qt Widgets frontend over Qt-independent geometry

**Recommendation:** add a `pico-la-gui` entry point and a PySide6 optional
dependency group. Keep core and CLI imports free of Qt. Put viewport state,
transition indexing, cursor/sample conversion, and bus extraction in pure
modules; use one custom `QWidget`/`QPainter` waveform surface and model-backed
channel/bus tables. Run file I/O and serial capture outside the UI thread.

**Benefit:** gives deterministic unit coverage, bounded painting, and a light
frontend without creating a framework-heavy view-model layer. **Alternative:**
`QGraphicsScene` items per edge simplify early interaction but scale poorly;
QML/Qt Quick offers acceleration but conflicts with the reviewed Qt Widgets
stack and adds a second UI language.

### 7. Keep GUI dependencies optional but fully locked in development

**Recommendation:** pin PySide6 and pytest-qt only after clean wheel probes on
Python 3.12 Linux and macOS. Expose them through a `gui` project extra while the
reviewed development lock includes them for CI. A core/CLI source installation
must remain possible without Qt, and `pico-la-gui` must fail with an actionable
message when the extra is absent.

**Benefit:** scripting users avoid a large Qt install while GUI CI remains
reproducible. **Alternative:** make PySide6 unconditional, simplifying install
instructions but coupling every CLI user and environment to Qt.

### 8. Define a useful but narrow parallel-bus contract

**Recommendation:** data channels are an explicit ordered tuple interpreted
LSB first. Transition mode emits one interval row whenever the packed value
changes; sampled mode emits a row at each selected edge of a distinct strobe
channel. Rows include sample index, trigger-relative time, binary, fixed-width
hex, unsigned decimal, and interval end/duration where applicable. Export is
deterministic CSV and uses the same pure core as the GUI table.

**Benefit:** supports both waveform inspection and clock/read/write-strobe SBC
work without becoming a CPU decoder. **Alternative:** emit every sample, which
is simplest but produces large, repetitive tables; transition-only output is
compact but may miss the value at the bus-valid strobe.

### 9. Require upper-channel physical proofs

**Recommendation:** retain the protected 3.3 V source and fixed firmware, then
perform separate full-width captures with the 1 kHz signal temporarily moved to
the highest requested channel: D15 for 16-bit mode and D23 for 24-bit mode.
Confirm the integrated board's labels and GPIO mapping before wiring. Each proof
checks identity, request bytes, word width/dtype, exact count, requested upper
bit transitions, approximate frequency, zero upper byte in 24-bit words,
cleanup, and reuse without a power cycle.

**Benefit:** detects a parser that merely widens zero-valued Cycle 1 data.
**Alternative:** reuse a D0-only signal in wider modes, which proves framing and
count but not upper-bit mapping or endianness.

### 10. Use offscreen cross-platform CI plus one native-host smoke

**Recommendation:** the Linux/macOS Python 3.12 matrix retains all Cycle 1
checks and adds Qt import/start/close, pytest-qt workflows, pure geometry tests,
and deterministic render invariants under the offscreen platform. Install only
the documented Linux system libraries required by Qt. Run native interactive
open/zoom/pan/cursor/export and live-capture smoke on the attached macOS host.
Record a Linux native-desktop smoke when such a host is available, but do not
make packaging a Cycle 2 gate.

**Benefit:** continuously proves both supported source platforms while using
available physical hardware. **Alternative:** require manual native desktops on
both operating systems before completion, providing stronger UX evidence but
introducing an external host blocker unrelated to the source-installed scope.

### 11. Establish rendering baselines before thresholds

**Recommendation:** benchmark first paint and repeated pan/zoom for empty,
constant, dense-transition, and maximum representative 8/16/24 captures. Record
CPU time, peak memory, visible transition count, viewport size, OS, and Qt
version. Approve thresholds only after the first reproducible baseline; enforce
them thereafter.

**Benefit:** produces meaningful regression gates rather than arbitrary numbers.
**Alternative:** set thresholds during orchestration, which appears decisive but
has no evidence that the target host or Qt backend can meet them.

## Proposed batch boundaries

These are discovery recommendations, not yet authoritative batches.

### C2-B1: Contracts, fixtures, dependency and GUI shell preflight

- Freeze channel/mode/dtype, replay 2, generalized CSV/import, `.lac`, bus, GUI,
  and evidence contracts.
- Generate and independently verify the `.lac` corpus with provenance.
- Probe and hash-pin PySide6/pytest-qt wheels on Linux/macOS Python 3.12.
- Add an offscreen `pico-la-gui` start/close shell without capture/viewer logic.
- Settle the workflow migration and correct stale Cycle 1 wording.

### C2-B2: Wider domain, codec, replay and CSV core

- Generalize the model and normal request/response parser for ordered D0-D23
  subsets and `uint8`/`uint16`/`uint32`.
- Add literal 8/16/24 golden requests/responses, fragmentation, malformed width,
  count/buffer bounds, 24-bit upper-byte, schema-1 compatibility, schema-2, and
  strict self-timed CSV import/export tests.
- Preserve all Cycle 1 behavior and evidence fixtures.

### C2-B3: Physical 16/24-channel capture gate

- Run full D0-D15 and D0-D23 normal captures with a safe 1 kHz signal on D15
  and D23 respectively.
- Validate upper-bit polarity/frequency, word dtype/endianness/count, artifacts,
  close/reopen/re-identification, and a following known capture without power
  cycle.

### C2-B4: `.lac` compatibility and parallel-bus core

- Implement bounded historical/current `.lac` readers and the canonical writer.
- Prove fixture round-trips and current C# readability where representable.
- Implement pure transition/strobe bus extraction and deterministic table CSV.

### C2-B5: Offline read-only viewer

- Open replay 1/2, self-timed CSV, and `.lac` without serial access.
- Render 8/16/24 channels; labels/visibility, pan, cursor zoom, cursor readout,
  trigger marker, export, and bus table.
- Pass pure geometry, pytest-qt interaction, render-invariant, failure-dialog,
  threading, and recorded performance-baseline checks.

### C2-B6: Live capture integration and final proof

- Use the existing explicit-port service from a worker without blocking Qt.
- Capture, display, export, close/reopen, and repeat on the physical board.
- Run accumulated Linux/macOS CI, native macOS GUI/hardware smoke, independent
  acceptance, evidence manifests, rollback audit, and final Cycle 2 handoff.

## Authority gates for the future orchestration

Cycle 2 documentation should explicitly authorize only:

- Python implementation, tests, fixtures, evidence, and documentation under
  `Software/LogicAnalyzerPy/`;
- the reviewed workflow rename/replacement needed for the Cycle 2 Linux/macOS
  matrix;
- approved dependency downloads for PySide6, pytest-qt, fixture generation, and
  their transitive locked dependencies;
- read-only execution of controlled current/historical C# serializers to create
  `.lac` fixtures;
- explicit-port identity and normal 8/16/24 capture requests, plus the already
  characterized Cycle 1 recovery byte when needed; and
- safe operator-confirmed temporary 3.3 V signal placement on D15/D23.

The following should remain prohibited without separate direction:

- firmware edits/flashing, bootloader, Wi-Fi, or persistent device changes;
- advanced trigger, fast/complex/blast/burst, TCP, multi-device, decoder, editing,
  or device-management implementation;
- packaging, signing, notarization, publication, or C# removal;
- executing untrusted `.lac` content or treating JSON type metadata as code; and
- beginning Cycle 3.

## Required completion evidence for a Cycle 2 goal

A future orchestration document should require, at minimum:

1. Cycle 1 clean install, CLI, tests, and physical capture/recovery remain green.
2. Literal source/provenance-backed 16- and 24-channel golden wire fixtures pass.
3. Wider fake/replay tests cover all widths, request ordering, malformed inputs,
   bounds, timeouts, cancellation, and cleanup.
4. Physical D15 and D23 captures prove upper-bit mapping, word widths,
   endianness, count, polarity, frequency, and reuse without power cycle.
5. Every accepted historical/current `.lac` fixture loads; canonical output
   round-trips and is checked against the current C# reader where representable;
   hostile inputs are bounded and inert.
6. Replay schema 1 remains readable; schema 2 and generalized self-timed CSV
   round-trip deterministically without pickle or machine-local metadata.
7. Parallel-bus transition and strobe modes have exact bit-order/time/export
   fixtures suitable for an 8-bit SBC.
8. The offline GUI opens all three formats and passes interaction/render tests
   on Linux/macOS CI without importing serial or blocking the event loop.
9. Native macOS viewing and live capture pass: open, zoom, pan, cursor readout,
   export, close/reopen, and second capture.
10. Rendering baselines and approved post-baseline thresholds are recorded for
    representative and maximum captures.
11. Evidence manifests identify one final candidate/tree, dependencies, OS/Qt
    versions, commands, sanitized hardware results, limitations, and deferrals.
12. Existing C# applications, firmware, Cycle 1 fixtures, and replay artifacts
    remain usable as rollback and regression paths.

## Inputs that must be settled before the Cycle 2 goal

1. Approval or amendment of the eleven recommendations above.
2. Authority to install/use .NET 8 and Newtonsoft.Json, or provision of
   independently generated `.lac` fixtures.
3. Operator confirmation that protected 3.3 V test-signal access to the board
   inputs corresponding to D15 and D23 is practical, including label/GPIO
   mapping and common ground.
4. Approval for the Cycle 2 workflow migration and Linux Qt system packages.
5. Agreement that Linux offscreen CI plus native macOS smoke is sufficient for
   Cycle 2 source-install acceptance, with native Linux manual smoke recorded
   when a host is available.

None of these inputs prevents drafting the new orchestration and batch documents;
they must be resolved in those documents' approval checklist before the durable
implementation goal is created.

## Discovery conclusion

The repository contains enough evidence to draft `CYCLE2_ORCHESTRATION.md` and
`CYCLE2_BATCH_EXECUTION.md`. The two hard pre-implementation evidence gaps are
the missing serializer-generated `.lac` corpus and the absence of a physical
upper-channel test record. The recommended sequence makes both early gates,
keeps firmware fixed, proves wider capture before GUI integration, and defers
decoder and parity complexity explicitly.
