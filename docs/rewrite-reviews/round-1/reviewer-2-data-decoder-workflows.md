# Round 1 Review: Capture Data, Decoder, and User-Workflow Boundary

- Reviewer: `/root/review_data_workflows` — Reviewer 2, Capture Data,
  Decoder, and User-Workflow Boundary
- Reviewed commit: `1a6fb5aed5f0714368f3bf97af04c1789b8f9dc9`
- UTC timestamp: `2026-08-16T15:00:03Z`
- Verdict: `changes_required`
- Resolving commit: `7d04ed1a2a2f9c90a6017b90e41b9df61ba620c7`

## Scope

This review applies the Reviewer 2 charter in
`docs/rewrite-reviews/ARCHITECTURAL_DOMAINS.md`. It begins with validated raw
capture words and metadata and reviews the proposed capture model, CSV/NPZ
persistence, scriptable CLI behavior, later `.lac`/decoder/GUI boundaries, and
waveform-rendering direction. It compares the three process documents at the
reviewed commit with the current capture models, file operations, CLI and
terminal workflows, GUI renderers, signal-description implementation,
`SigrokDecoderBridge`, and representative bundled API-v3 decoders.

Wire encoding, serial lifecycle, CI/platform delivery, review governance, and
completion authority are outside this review except where their promised
outputs or requirements cross this boundary.

## Findings and disposition

### 1. The Cycle 1 capture model and export semantics are not settled before implementation

- Severity: high
- Evidence:
  - `BATCH_EXECUTION.md:235-248` asks C1-B2 for typed capture
    configuration/results but does not define their required fields or
    invariants and explicitly leaves even the minimal NumPy model as a decision.
  - `BATCH_EXECUTION.md:298-306` postpones the observable artifact work until
    C1-B4 and specifies only stable channel headers/sample rows and unspecified
    non-object metadata.
  - `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:333-335`
    correctly makes raw words canonical, but does not settle sample origin,
    trigger index, physical channel identity, display labels, or the relation
    between a requested subset and bits in each raw word.
  - The existing model distinguishes zero-based `ChannelNumber` from the
    one-based `TextualChannelNumber` in
    `Software/LogicAnalyzer/SharedDriver/AnalyzerChannel.cs:10-13`. The current
    extraction path instead uses the selected channel's ordinal position in
    `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs:497-508`, which
    demonstrates why this mapping must be specified rather than inherited.
  - Existing CSV contains only channel headers and bit rows, with no sample
    index, time base, or trigger metadata
    (`Software/LogicAnalyzer/TerminalCapture/Classes/FileOperations.cs:57-79`).
    Yet Cycle 2 proposes opening CSV in a timed waveform viewer
    (`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:80-84`).
- Requested resolution: Make C1-B1 or C1-B2 produce and approve a narrow data
  contract/ADR before codec, CLI, or format agents depend on it. At minimum it
  must define: the `uint8` raw-word array and its shape; integer sample rate;
  requested/actual sample counts; pre-trigger count and exact trigger/sample-zero
  convention; physical zero-based channel IDs independent from one-based display
  names and user labels; trigger channel and edge; configuration/capability
  metadata required for replay; and invariants checked at construction/load.
  Define whether Cycle 1 always stores all physical D0-D7 bits or a selected
  subset and how selection affects export only. Specify how a later viewer gets
  sample rate and trigger origin when importing CSV (for example, a documented
  sidecar or an explicit operator-supplied interpretation); do not silently
  invent them. Add golden tests using a non-contiguous channel selection so an
  ordinal/physical-bit mix-up fails.
- Disposition: resolved — the resolving commit defines the exact `uint8` model,
  D0–D7 mapping, counts, sample rate, trigger origin, required metadata, timed
  CSV columns, invariants, ADR ownership, and fake acceptance evidence.

### 2. Cycle 1 does not define a stable, automation-safe `capture` CLI contract

- Severity: medium
- Evidence:
  - The broad roadmap promises stable exit codes and human/JSON output at
    `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:551-563`, but
    its Cycle 1 exception defers JSON and gives only option categories at
    `:569-575`.
  - `BATCH_EXECUTION.md:292-307` requires CLI capture/export/replay validation
    without specifying an invocation, output selection rules, stdout/stderr
    behavior, overwrite behavior, or what remains after a failed capture/write.
  - The existing CLI is not a safe compatibility default: it has an always-true
    extension rejection at `Software/LogicAnalyzer/CLCapture/Program.cs:43-48`,
    writes progress to standard output throughout, and returns `1` on success at
    `:198-207`.
- Requested resolution: Add a Cycle 1 command contract before C1-B3. It should
  give complete `devices`, `info`, `capture`, replay-validation, and
  `hardware-smoke` invocations; define zero as success and a small documented
  nonzero exit-code taxonomy; reserve stdout for requested machine data or state
  explicitly that machine-readable output is deferred; send diagnostics/progress
  to stderr; require explicit output format/path; reject an existing output
  unless `--force` is supplied; and publish outputs atomically so timeout,
  Ctrl-C, validation, or disk errors do not leave an apparently valid final
  artifact. Add subprocess tests for success, usage error, capture failure,
  output collision, and interrupted/failed export.
- Disposition: resolved — the resolving commit specifies every Cycle 1 CLI
  invocation, exit taxonomy, stdout/stderr behavior, collision/force behavior,
  transactional output publication, and subprocess tests.

### 3. The provisional NPZ loader is not sufficiently bounded for untrusted replay input

- Severity: high
- Evidence:
  - `ORCHESTRATION.md:87-89` and `BATCH_EXECUTION.md:303-318` require
    `allow_pickle=False` and validated metadata, which prevents object-array
    deserialization but does not by itself bound ZIP expansion, array count,
    dimensions, dtype widths, sample count, or JSON metadata size/depth.
  - The roadmap says all capture files are untrusted at
    `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:876-885`, but
    its explicit bounds at `:880-881` cover packet/sample allocation and do not
    give a replay-container policy.
  - The same security section correctly forbids capture files from automatically
    selecting decoder code at `:883-885`; the provisional replay schema does not
    explicitly exclude decoder paths/modules/configuration from executable
    interpretation.
- Requested resolution: Add a Cycle 1 replay-reader policy and negative tests.
  Before materializing arrays, constrain archive/member count, compressed and
  declared uncompressed sizes, accepted member names, metadata byte/depth limits,
  exact sample dtype/endianness/rank, and maximum sample count derived from a
  configured safety cap. Reject duplicate/unexpected required members,
  unsupported schema major versions, object/structured/string sample dtypes,
  inconsistent counts, and trailing/extra sample arrays according to a stated
  unknown-field policy. State that replay metadata is inert and cannot nominate
  or configure executable decoder code. `allow_pickle=False` remains required
  but is not the complete acceptance criterion.
- Disposition: resolved — the resolving commit fixes the NPZ member/schema
  contract and numeric file/member/metadata/sample bounds, rejects unsafe or
  unexpected archives/dtypes, keeps metadata inert, and requires hostile-input
  tests with `allow_pickle=False`.

### 4. Broad Phase 3 gates contradict the explicit Cycle 1 deferrals

- Severity: medium
- Evidence:
  - Cycle 1 explicitly defers TCP, graceful abort, `.lac`, and JSON machine
    output in `ORCHESTRATION.md:97-105` and
    `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:569-575`.
  - The roadmap's undifferentiated Phase 3 gate nevertheless requires fake TCP,
    abort, `.lac`, and JSON at
    `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:577-584`.
  - The higher-authority batch procedure correctly limits C1-B2/B4 to fake
    serial/replay and CSV/NPZ (`BATCH_EXECUTION.md:228-257`, `:290-323`), but an
    implementation agent told to complete the roadmap phase could reasonably
    expand scope or report a false failure.
- Requested resolution: Split or label the Phase 3 gate explicitly. Add a
  Cycle 1 Phase 3 gate matching C1-B1 through C1-B5, and mark the existing
  fake-TCP/abort/`.lac`/JSON bullets as later broad-parity gates that cannot block
  Cycle 1. Apply the same terminology anywhere a broad phase gate overlaps a
  narrower cycle gate, with `BATCH_EXECUTION.md` remaining authoritative.
- Disposition: resolved — the resolving commit adds a narrow Cycle 1
  transport/CLI gate and labels TCP, public abort, `.lac`, and broader JSON work
  as a later Phase 3 parity gate that cannot block Cycle 1.

### 5. The focused Cycle 3 decoder promise conflicts with the all-decoder Phase 4 gate

- Severity: medium
- Evidence:
  - The delivery sequence intentionally limits Cycle 3 to I2C, SPI, and UART and
    defers broad API-v3 compatibility, stacking, user directories, and the
    all-decoder import gate at
    `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:87-92`.
  - Phase 4 instead combines user decoder directories, stacking, additional
    protocols, every supported bundled decoder, and maximum-capture performance
    into one gate at `:586-645`.
  - Representative bundled decoders do require nontrivial API-v3 behavior:
    alternate `wait()` conditions in `Software/decoders/i2c/pd.py:332-361`,
    samplerate metadata in `Software/decoders/uart/pd.py:230-232`, and
    `OUTPUT_PYTHON`/binary outputs in `Software/decoders/parallel/pd.py:72-107`.
    Treating all of that as the first decoder checkpoint defeats the stated
    complexity deferral.
- Requested resolution: Define a distinct focused Cycle 3 decoder gate for only
  I2C, SPI, and UART, driven by checked-in signal/golden fixtures and the exact
  API-v3 calls those versions exercise. Require a headless library and CLI path,
  deterministic channel mapping/options/annotations, samplerate metadata,
  cancellation/failure isolation, pinned decoder provenance, and no user-code
  discovery. Relabel the present Phase 4 stacking/user-directory/all-decoder gate
  as a later parity gate. Keep the existing rule that capture files never select
  code, and require an explicit trusted path only when user decoders eventually
  land.
- Disposition: resolved — the resolving commit adds a focused Cycle 3
  I2C/SPI/UART fixture-driven gate and explicitly moves stacking, user discovery,
  and all-decoder import to later Phase 4 parity.

### 6. The performance-baseline schedule requires unimplemented future subsystems during Phase 2

- Severity: medium
- Evidence:
  - `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:889-903`
    requires Phase 2 baselines for decoder execution, first waveform paint,
    pan/zoom, and multi-device peak memory.
  - Decoders, multi-device composition, and GUI rendering do not arrive until
    Phases 4, 5, and 6 respectively (`:586-704`).
  - The rendering design itself is viable: it mandates custom painting,
    visible-transition level of detail, no per-sample Qt items, and dense/max
    tests at `:691-704`. The scheduling contradiction, not the rendering
    direction, is the problem.
- Requested resolution: Keep Phase 2 baselines only for raw capture parsing,
  channel extraction, Cycle 1 CSV/NPZ, and later `.lac` when implemented. Move
  decoder, multi-device memory, and waveform paint/pan/zoom baselines to the
  batch that first introduces each subsystem. Require the Cycle 2 viewer to
  benchmark empty, constant, dense-transition, and maximum representative
  captures before its gate; defer numerical thresholds until those baselines
  exist, then record the environment and reviewed thresholds.
- Disposition: resolved — the resolving commit assigns capture/format, decoder,
  multi-device, and viewer baselines to the cycle that first implements each
  subsystem, including the required viewer workload classes.

## Accepted observations requiring no change

1. The Cycle 1 choice to stop at a source-installed CLI, deterministic CSV, and
   provisional NPZ is appropriate for reaching physical-board utility quickly;
   GUI, `.lac`, decoder, editing, and signal-composer work are correctly excluded
   by `ORCHESTRATION.md:97-108`.
2. The architecture correctly makes one UI-independent library serve CLI and
   future GUI, keeps raw words canonical, and prohibits core imports from Qt,
   CLI, or serial implementations
   (`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:324-345` and
   `BATCH_EXECUTION.md:250-257`).
3. The future waveform approach is technically viable because it specifies
   custom painting and visible-transition level of detail rather than a UI item
   per sample (`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:691-704`).
4. The later decoder trust direction is sound: decoder failures are isolated,
   capture-file decoder nomination is forbidden, and user decoder directories
   are explicitly trusted executable-code locations
   (`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:338-342`,
   `:876-885`).
