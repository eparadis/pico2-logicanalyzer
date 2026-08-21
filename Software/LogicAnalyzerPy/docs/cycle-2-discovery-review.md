# Cycle 2 bounded discovery review

- Review baseline commit: `e85fc642b922d089e7ffe019128f34fda65d1fc9`
- Review baseline tree: `bff37f32223cc022e0d2d4b2c416ab45ecb42170`
- Discovery completed: `2026-08-17T05:46:27Z`
- Recommendations reviewed with the operator: `2026-08-20`
- Status: all eleven recommendations resolved; ready for Cycle 2 orchestration

## Purpose and boundary

This review identifies the smallest useful and verifiable Cycle 2 shape after
the accepted Cycle 1 vertical slice. It records the approved scope, authority
boundaries, batch candidates, and completion evidence needed to draft
`CYCLE2_ORCHESTRATION.md` and `CYCLE2_BATCH_EXECUTION.md`.

It is not an implementation plan and does not authorize Cycle 2 implementation.
Cycle 2 still requires new top-level orchestration and batch documents,
common-commit review approval, and a new durable goal.

No firmware, hardware, dependency, workflow, or product operation was performed
for the discovery review. The operator decisions recorded below supersede the
original unapproved recommendations in this document's first revision.

## Evidence inspected

### Accepted Python baseline

- [`docs/cycle-1-completion.md`](cycle-1-completion.md) and the five accepted
  evidence manifests.
- Current models, V2 codec, serial driver, capture/export/replay code, CLI,
  recovery code, and independent tests under `Software/LogicAnalyzerPy/`.
- Current Linux/macOS Python 3.12 workflow and hash-pinned dependency lock.

### Firmware and existing application sources

- V2 request and mode definitions in
  `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Structs.h`, `LogicAnalyzer.c`,
  `LogicAnalyzer_Capture.c`, and board settings.
- Mode selection, buffer limits, request composition, word reads, and channel
  extraction in `SharedDriver/AnalyzerDriverBase.cs` and
  `SharedDriver/LogicAnalyzerDriver.cs`.
- Existing viewer behavior was inspected only to understand present user
  workflows and likely scaling risks. Its implementation and file formats are
  not compatibility targets for Cycle 2.

### Frontend platform decision

The operator selected browser technology over Qt. The approved frontend stack
is React, TypeScript, and Vite, with locked JavaScript dependencies. The local
Python application will serve prebuilt assets and a versioned browser API.
Node.js is a development and build dependency, not a runtime requirement for a
source or packaged production installation containing the built assets.

The browser frontend must:

- use an installed browser rather than bundle Qt, Chromium, or Electron;
- work without CDN or other runtime network access;
- bind its local application server to loopback by default;
- keep serial ownership, capture validation, replay, export, and analysis in
  the Python core; and
- render dense waveforms through a bounded Canvas path rather than a DOM node
  per sample or transition.

Exact supported browser versions, Python server dependencies, Node version,
package locks, asset-build rules, and the JSON/WebSocket API contract must be
frozen in the first Cycle 2 batch.

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
   `i`, not necessarily physical channel D`i`.
4. Word mode is selected from the highest requested physical channel: D0-D7 is
   8-bit, any D8-D15 requires 16-bit, and any D16-D23 requires 24-bit/32-bit
   storage.
5. The reported Pico 2 buffer is 393216 bytes, giving maxima of 393216, 196608,
   and 98304 sample words for 8-, 16-, and 24-channel modes before other
   contract limits are applied.
6. Firmware does not safely validate every channel-list element before indexing
   `pinMap`. The Python client must reject non-integer, duplicate, out-of-range,
   or otherwise inconsistent lists before sending a request.

### Capture and interchange formats

1. Cycle 1 hard-codes `uint8`, D0-D7, eight labels, and eight mappings in its
   model, codec, CSV, and replay contracts. Wider support is a deliberate model
   and schema evolution, not a parser-only change.
2. Replay schema 2 will be the canonical native capture format. New files use
   schema 2; the bounded loader retains schema 1 read compatibility.
3. Test data will be generated synthetically, derived from the checked-in
   firmware protocol, or captured from the approved physical hardware. Valid
   and hostile fixtures must have recorded provenance and digests.
4. Cycle 1 CSV is self-timed and deterministic. Cycle 2 generalizes its explicit
   captured-channel columns while preserving byte-identical Cycle 1 D0-D7
   output where the existing contract applies.
5. Existing `.lac` files and C# application formats are not interoperability
   targets. There is no operator-owned historical data requiring migration.
6. No feature in this project may require .NET. Cycle 2 must not install or run
   .NET, NuGet, C# fixture generators, or C# round-trip validators.

### Viewer and analysis surface

1. Rendering work must be proportional to visible pixels and transitions, not
   total samples or a browser object per edge.
2. Viewport transformations, transition reduction, cursor calculations, bus
   extraction, and formatting should be deterministic, independently testable
   functions even when implemented in TypeScript for the browser boundary.
3. Serial and filesystem operations remain behind the Python application
   service and must not block request handling or the browser event loop.
4. No parallel-bus table exists in the current application. Its bit ordering,
   sampling rule, table rows, and export schema therefore require a new explicit
   contract rather than compatibility inference.

### Documentation and delivery debt

- `README.md` reflects Cycle 1, but `docs/cli-contract.md`, the project
  description, and comments in `requirements-dev.in` still contain Cycle 1
  scaffold/batch wording. Correct these mechanically in the first Cycle 2 batch
  without changing accepted Cycle 1 behavior.
- The current workflow is named and authorized specifically for Cycle 1. Cycle
  2 must authorize its migration or replacement and avoid redundant full
  matrices on every change.

## Approved Cycle 2 target

Deliver one source-installed Python 3.12 application that preserves the Cycle 1
CLI and adds:

1. normal edge-trigger capture of an explicitly ordered, unique subset of one
   to 24 physical channels D0-D23, with the trigger channel captured;
2. correct 8-, 16-, and 24-channel word modes selected by the highest physical
   channel, with raw dtypes `uint8`, `uint16`, and `uint32` respectively;
3. backward loading of replay schema 1 and a generalized canonical replay
   schema 2 for arbitrary channel sets and word dtypes;
4. strict import and export of the self-timed Python CSV contract, generalized
   to explicit captured-channel columns while preserving applicable Cycle 1
   output;
5. a local browser application built with React, TypeScript, and Vite that
   opens replay and self-timed CSV, renders digital waveforms with channel
   labels and visibility, horizontal pan, cursor-centered zoom, cursor
   sample/time/value readout, trigger marker, and export;
6. live capture through the already proven serial application service only
   after offline viewing is accepted; and
7. a deterministic parallel-bus table/export with ordered LSB-to-MSB data
   channels, transition rows, and optional sampling on a distinct strobe
   channel's rising or falling edge.

This target is useful for an 8-bit SBC because a 24-channel capture can combine
an 8-bit data bus, selected address/control lines, and a strobe while the bus
table converts samples into inspectable values. It does not claim full CPU-cycle
or instruction decoding.

## Approved recommendations

### 1. Keep firmware fixed

Use the same checked-in and already flashed V2 Pico 2 firmware throughout Cycle
2. Record reproducible firmware defects or throughput limits and defer fixes to
a separately reviewed system cycle. Do not edit, build, flash, or manage the
device persistently during Cycle 2.

This keeps the peer stable so host failures remain attributable. A genuine
firmware blocker requires pausing the affected proof and seeking separately
reviewed authority rather than changing both implementations together.

### 2. Support explicit ordered channel subsets

Allow one to 24 unique physical channel IDs in explicit request order. Require
the trigger channel to be captured, derive word mode from the highest physical
ID, and retain physical IDs, labels, request order, mappings, and returned bit
positions as distinct metadata.

This matches the checked-in firmware behavior and supports practical mixtures
of SBC data, address, and control signals.

### 3. Use mode-appropriate raw sample dtypes

Preserve `uint8` for 8-bit captures, use `uint16` for 16-bit captures, and use
`uint32` for 24-bit captures. Require bits 24-31 of every 24-bit word to be zero.
Extract channel values vectorially by packed request position.

This preserves Cycle 1 artifacts and keeps memory proportional to transfer
width instead of widening every capture to `uint32`.

### 4. Introduce replay schema 2 and retain schema 1 reads

Schema 2 explicitly records dtype, transfer mode, arbitrary ordered physical
channels, request-bit mappings, labels, timing, and trigger metadata. New Cycle
2 files use schema 2. The loader continues to accept valid schema 1 while
retaining hostile-archive bounds, canonical metadata checks, and the no-pickle
rule.

### 5. Use only native synthetic and hardware-derived test data

Replay schema 2 is the sole canonical Python capture format. Do not implement
`.lac` reading or writing. Build the corpus from deterministic synthetic
captures, source-derived protocol bytes, sanitized physical captures, and
adverse archive/metadata/NumPy cases.

No project feature may depend on .NET. The existing C# application is only an
unchanged rollback tool; it is not a data-interchange or validation target.

### 6. Use a browser frontend rather than Qt

Serve the application locally from Python and use an installed browser. Keep
the browser/server boundary versioned, loopback-only by default, and offline at
runtime. Use Canvas for bounded waveform painting and keep capture, validation,
replay, export, and analysis authority in the Python core.

This provides a versatile Linux/macOS frontend without bundling Qt, Electron,
or another browser engine.

### 7. Use React, TypeScript, and Vite

Use React with TypeScript and Vite, locked JavaScript dependencies, type and
component tests, and committed production-build rules. Node.js is required to
develop and build the frontend but not to run an installation containing
prebuilt assets. Do not use CDN-hosted runtime dependencies.

### 8. Define a narrow parallel-bus contract

Data channels are an explicit ordered tuple interpreted least-significant bit
first. Transition mode emits a row whenever the packed value changes. Sampled
mode emits a row at each selected edge of a distinct strobe channel. Rows
include sample index, trigger-relative time, binary value, fixed-width
hexadecimal value, unsigned decimal value, and applicable interval fields.

Export deterministic CSV from the same Python analysis core that supplies the
browser table. CPU-specific cycle or instruction decoding is deferred.

### 9. Prove byte boundaries with one simultaneous physical pattern

After operator confirmation, fan out the safe 3.3 V, 1 kHz source to analyzer
inputs D0, D8, D16, and D23 simultaneously. All destinations must be confirmed
inputs, common ground must remain connected, and the source must be safe for the
combined high-impedance load. Do not require floating inputs to remain zero.

Run these contiguous ordered captures:

| Capture | Requested channels | Expected driven mask | Storage |
| --- | --- | --- | --- |
| 8-channel | D0-D7 | `0x01` | `uint8` |
| 16-channel | D0-D15 | `0x0101` | `uint16` |
| 24-channel | D0-D23 | `0x810101` | `uint32` |

Prove identity, request mapping, wire width, dtype, exact count, synchronous
activity at the driven bits, approximate frequency, and zero bits 24-31 in the
24-channel words. Record uncontrolled floating inputs rather than treating
their activity as failure. This pattern proves the transfer-width boundaries
and highest supported channel, though identical waveforms cannot detect every
permutation among the four driven inputs.

### 10. Make macOS the primary accepted platform

Run locked Python and Node installation, Python checks, TypeScript checks,
React tests, production Vite build, API tests, and headless browser tests on
both macOS and Linux CI.

On the available macOS host, additionally run native interactive browser
acceptance and every physical Pico 2 capture/recovery proof. These are Cycle 2
completion gates. Linux hardware, USB-permission, and native interactive tests
are explicitly deferred because only one USB-attached board is available and
macOS is the primary target. Describe Linux as CI-supported, not equivalently
hardware-accepted.

### 11. Establish rendering baselines before thresholds

Benchmark first paint and repeated pan/zoom for empty, constant, sparse,
dense-transition, and maximum representative 8/16/24-channel captures, plus
representative and worst-case bus tables. Record browser and version, OS,
capture and viewport dimensions, device-pixel ratio, sample and visible
transition counts, timing, fixture digest, and memory where measurement is
reliable.

Approve concrete thresholds at a checkpoint only after reproducible baselines
exist. Enforce those thresholds in later batches. Shared-CI timing must use a
method that avoids flaky single-run limits; primary usability evidence comes
from the macOS target.

## Proposed batch boundaries

These are settled discovery recommendations, not yet authoritative batches.

### C2-B1: Contracts, dependencies, workflow, and web shell

- Freeze channel/mode/dtype, replay 2, generalized CSV, bus, browser API,
  server lifecycle, frontend build, and evidence contracts.
- Select and hash-pin the minimal Python web dependencies; lock the Node,
  React, TypeScript, Vite, and test dependencies.
- Prove clean Python and Node bootstraps and production asset builds on macOS
  and Linux CI.
- Add a loopback-only offline application shell that starts, serves built
  assets, reports readiness, and shuts down cleanly without serial access.
- Settle workflow migration and correct stale Cycle 1 wording.

### C2-B2: Wider domain, codec, replay, and CSV core

- Generalize the model and normal request/response parser for ordered D0-D23
  subsets and `uint8`/`uint16`/`uint32`.
- Add literal 8/16/24 golden requests/responses, fragmentation, malformed word
  width, count/buffer bounds, 24-bit upper-byte, and ordered-subset tests.
- Implement canonical replay schema 2 with schema 1 reads and generalized
  deterministic self-timed CSV import/export.
- Preserve all Cycle 1 behavior and evidence fixtures.

### C2-B3: Physical byte-boundary capture gate

- After explicit operator confirmation, connect the safe source to D0, D8,
  D16, and D23 and run the approved 8/16/24 contiguous captures.
- Validate exact masks, synchronous transitions, frequency, word dtype,
  endianness, count, artifacts, close/reopen/re-identification, and a following
  known capture without a power cycle.
- Sanitize the serial port and record the final wiring state.

### C2-B4: Parallel-bus core and browser API

- Implement pure transition and strobe bus extraction and deterministic table
  CSV.
- Expose bounded, versioned replay, capture, viewport-data, bus-table, export,
  error, cancellation, and lifecycle endpoints without duplicating domain
  authority in TypeScript.
- Prove hostile requests, disconnects, cancellation, concurrency limits, and
  loopback/default-origin behavior with fake and replay data.

### C2-B5: Offline browser viewer and performance checkpoint

- Open replay schema 1/2 and self-timed CSV without serial access.
- Render 8/16/24 channels with labels/visibility, pan, cursor-centered zoom,
  cursor readout, trigger marker, export, and bus table.
- Pass deterministic TypeScript, React, browser interaction, Canvas geometry,
  API-failure, reconnect, and cleanup tests on macOS and Linux CI.
- Record reproducible rendering baselines, then approve thresholds before this
  batch is accepted and later work advances.

### C2-B6: Live capture integration and final proof

- Use the existing explicit-port service through the local server without
  blocking request handling or the browser event loop.
- Capture, display, inspect, export, close/reopen, and repeat on the physical
  board from the native macOS browser.
- Enforce the approved performance thresholds.
- Run accumulated macOS/Linux CI, native macOS browser/hardware acceptance,
  independent acceptance, evidence manifests, rollback audit, and final Cycle
  2 handoff.

## Authority gates for future orchestration

Cycle 2 documentation should explicitly authorize only:

- Python implementation, tests, generated fixtures, evidence, built static
  assets, and documentation under `Software/LogicAnalyzerPy/`;
- React, TypeScript, Vite, frontend tests, and their reviewed locked JavaScript
  dependencies within the same project;
- a reviewed workflow migration for the macOS/Linux Python, Node, and browser
  matrix;
- approved dependency downloads for the locked Python web and JavaScript build
  stacks;
- explicit-port identity and normal 8/16/24 capture requests plus the already
  characterized Cycle 1 recovery byte when required; and
- operator-confirmed temporary 3.3 V signal fan-out to D0, D8, D16, and D23.

The following remain prohibited without separate direction:

- firmware edits, builds, flashing, bootloader entry, Wi-Fi changes, or other
  persistent device management;
- .NET installation or execution, NuGet, C# fixture generation, `.lac`
  compatibility, or C# round-trip validation;
- advanced trigger, fast/complex/blast/burst, TCP, multi-device, protocol
  decoder, CPU decoder, editing, or device-management implementation;
- runtime CDN dependencies, public/non-loopback server exposure, authentication
  design, or remote deployment;
- Electron, embedded-browser packaging, signing, notarization, publication, or
  removal of the C# application; and
- beginning Cycle 3.

## Required completion evidence for a Cycle 2 goal

A future orchestration document should require, at minimum:

1. Cycle 1 clean install, CLI, tests, and physical capture/recovery remain green.
2. Clean locked Python and Node bootstraps, production frontend build, and the
   accumulated macOS/Linux CI matrix pass on one final candidate.
3. Literal source/provenance-backed 8/16/24 golden wire fixtures pass.
4. Wider fake/replay tests cover dtypes, ordered subsets, request mappings,
   malformed inputs, bounds, timeouts, cancellation, and cleanup.
5. Physical captures of the D0/D8/D16/D23 pattern prove masks `0x01`, `0x0101`,
   and `0x810101`, word widths, endianness, count, frequency, zero bits 24-31,
   re-identification, and reuse without a power cycle.
6. Replay schema 1 remains readable; schema 2 and generalized self-timed CSV
   round-trip deterministically without pickle or machine-local metadata.
7. Parallel-bus transition and strobe modes have exact bit-order/time/export
   fixtures suitable for an 8-bit SBC.
8. The offline browser application passes API, interaction, Canvas/render,
   failure, cancellation, reconnect, and cleanup tests on macOS/Linux CI.
9. Native macOS viewing and live capture pass: start, open, capture, zoom, pan,
   cursor readout, bus table, export, close/reopen, and second capture.
10. Rendering baselines and approved post-baseline thresholds are recorded for
    representative and maximum captures, and the final candidate meets them.
11. Evidence manifests identify one final commit/tree, dependency locks,
    Python/Node/browser/OS versions, commands, sanitized hardware results,
    limitations, and deferrals.
12. The Python CLI, Cycle 1 fixtures, checked-in firmware, and existing C#
    sources remain unchanged or usable as their documented rollback paths; no
    prohibited firmware, .NET, persistent-device, or public-server action
    occurred.

## Inputs for the orchestration approval checklist

The following decisions are settled:

1. All eleven recommendations are approved as recorded above.
2. `.lac` and .NET work are excluded rather than treated as missing inputs.
3. React, TypeScript, and Vite replace Qt.
4. macOS native browser/hardware acceptance plus Linux CI is sufficient for
   Cycle 2; native Linux hardware evidence is deferred.
5. The intended physical proof uses one safe 3.3 V source fanned out to D0, D8,
   D16, and D23.

Before the physical C2-B3 operation, the operator must still confirm the actual
D0/D8/D16/D23 labels or mapping, common ground, 3.3 V reference, that every
destination is an analyzer input, and that the source may safely drive their
combined high-impedance load. Before the durable implementation goal, the new
orchestration documents must receive the required common-commit reviews and
approval.

## Discovery conclusion

The bounded discovery review is complete. The repository contains enough
evidence to draft `CYCLE2_ORCHESTRATION.md` and
`CYCLE2_BATCH_EXECUTION.md`. Cycle 2 will keep firmware fixed, prove wider
capture before live browser integration, use a Python-native replay corpus, and
deliver a React/TypeScript/Vite Canvas frontend with macOS as the primary
hardware-accepted platform and Linux supported through CI.

The remaining pre-implementation work is documentation governance: draft the
two Cycle 2 orchestration contracts, review them by architectural domain on one
common commit, resolve all findings, approve the final contracts, and only then
create the durable Cycle 2 goal.
