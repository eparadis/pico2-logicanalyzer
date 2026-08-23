# Logic Analyzer Python Rewrite: Cycle 2 Orchestration Contract

## Status and purpose

This is the proposed top-level contract for a future durable Cycle 2 `/goal`.
It governs the bounded expansion of the accepted Cycle 1 Python vertical slice
into a wider-capture application with a local browser frontend. It does not
start a goal. It must be reviewed and approved together with
`CYCLE2_BATCH_EXECUTION.md` before a durable Cycle 2 goal is created.

The documents have the following authority order:

1. `AGENTS.md` and its included repository instructions govern agent behavior.
2. This document governs the Cycle 2 objective, scope, authority, validation,
   checkpoints, and stopping conditions.
3. `CYCLE2_BATCH_EXECUTION.md` governs how each Cycle 2 batch is assigned,
   implemented, independently verified, integrated, and recorded.
4. `Software/LogicAnalyzerPy/docs/cycle-2-discovery-review.md` records the
   approved discovery decisions that these contracts operationalize.
5. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` remains the
   broader technical roadmap. Work outside this cycle is context, not authority.
6. The accepted Cycle 1 contracts, completion proof, checkpoint manifests, and
   fixtures are regression baselines, not authority to narrow Cycle 2.
7. `docs/rewrite-reviews/` defines the durable common-commit review protocol.

If these sources conflict, follow the order above and record the conflict in the
Cycle 2 progress log before proceeding.

## Durable objective

Build and verify a source-installed Python 3.12 application that preserves the
accepted Cycle 1 CLI and hardware behavior, supports normal edge-trigger capture
of explicit ordered subsets of one to 24 physical channels from the fixed V2
Pico 2 firmware, stores mode-appropriate raw words, reads replay schema 1 and
writes a secure deterministic replay schema 2, imports and exports the
self-timed CSV contract, provides deterministic transition and strobe-sampled
parallel-bus analysis, and exposes those capabilities through a loopback-only
local web application built with React, TypeScript, Vite, and bounded Canvas
waveform rendering.

macOS is the only accepted and supported platform. The complete native browser,
hosted-CI, and USB-attached-board workflow must pass on macOS. Other operating
systems are outside Cycle 2 scope and have no support claim.

The application should be useful for debugging a simple 8-bit SBC by viewing an
8-bit bus together with selected address or control signals and by sampling an
ordered bus at a clock, read, write, or enable strobe. It does not decode CPU
instructions or processor-specific bus cycles in Cycle 2.

## Verifiable stopping condition

Cycle 2 is complete only when every condition below is proven against one final
candidate commit and tree:

1. A clean Python 3.12 installation, the existing CLI help and commands, and all
   accepted Cycle 1 non-hardware tests pass.
2. A clean locked Node installation, TypeScript checks, React tests, production
   Vite build, and browser test entry point pass without runtime CDN access.
3. The accumulated Python, frontend, API, and headless-browser suite passes on
   macOS CI for the exact final candidate.
4. Provenance-tagged literal fixtures cover 8-, 16-, and 24-channel V2 normal
   requests and responses, including ordered subsets, packed request positions,
   little-endian word widths, reserved-byte escaping, and the zero upper byte
   required for 24-channel words.
5. Fake, replay, API, and browser tests cover success, fragmentation, malformed
   inputs, hostile files, bounds before allocation, finite timeouts,
   cancellation, disconnect, reconnect, concurrent-operation rejection, and
   cleanup without weakening Cycle 1 recovery behavior. Local-web negative
   tests also prove the capability-cookie, canonical-Origin, file-transfer, and
   secret-redaction contracts defined in `CYCLE2_BATCH_EXECUTION.md`.
6. Replay schema 1 remains readable. Canonical replay schema 2 and generalized
   self-timed CSV with the explicit import metadata defined in
   `CYCLE2_BATCH_EXECUTION.md` round-trip deterministically, preserve ordered
   channel metadata and mode-appropriate samples, use no pickle or executable
   metadata, and contain no machine-local values.
7. Transition and strobe-sampled parallel-bus modes have independent fixtures
   proving LSB-first ordering, sample/time semantics, edge selection, value
   formatting, interval fields, and deterministic CSV.
8. With the operator-confirmed protected 3.3 V source connected simultaneously
   to D0, D8, D16, and D23, physical captures of D0-D7, D0-D15, and D0-D23 prove
   the driven masks `0x01`, `0x0101`, and `0x810101`, the expected word widths
   and NumPy dtypes, exact counts, approximate 1 kHz activity, and zero bits
   24-31. Floating, electrically uncontrolled inputs are not required to remain
   zero.
9. The Cycle 1 physical identity, capture, timeout/cancellation recovery,
   close/reopen/re-identification, and second-capture paths remain usable without
   a power cycle.
10. The offline browser application opens schema-1/schema-2 replay and
    self-timed CSV, displays 8/16/24-channel waveforms, and passes automated
    tests for labels, visibility, pan, cursor-centered zoom, trigger marker,
    cursor sample/time/value readout, bus table, export, errors, reconnect, and
    clean shutdown.
11. Native macOS acceptance starts the local server, opens an installed browser,
    identifies the real Pico 2, captures and displays the approved physical
    pattern, interacts with all three widths, exports and validates artifacts,
    closes/reopens, performs a second physical capture, and shuts down cleanly.
12. Rendering baselines are recorded for the approved fixture classes. Concrete
    thresholds are approved at C2-B5 using the procedure in
    `CYCLE2_BATCH_EXECUTION.md`, and the final candidate meets them.
13. Final checkpoint and completion records identify the exact commit/tree,
    dependency-lock digests, commands and results, sanitized hardware identity
    and parameters, evidence paths and digests, limitations, deferrals,
    repository status, and the precise macOS-only support claim.
14. Checked-in firmware, the existing C# applications, Cycle 1 fixtures, and the
    accepted Python CLI remain present as rollback or regression paths. No
    firmware, .NET, persistent-device, public-server, packaging, or publication
    operation occurred.

Passing only fake tests, only browser tests, or only a D0 signal in wider word
modes is insufficient. A skipped required stopping-condition item cannot be
reported as success.

## Scope boundaries

### Required product surface

- Explicit ordered capture subsets containing one to 24 unique physical channel
  IDs D0-D23; the trigger channel must be included.
- Firmware mode selection from the highest physical channel requested.
- One-dimensional C-contiguous NumPy sample arrays with exact dtype `uint8`,
  `uint16`, or `uint32` for the 8-, 16-, or 24-channel word mode.
- Independent metadata for physical channel IDs, display labels, request order,
  packed bit positions, sample timing, trigger, and device identity.
- Replay schema 2 writes and bounded replay schema 1 reads.
- Generalized deterministic self-timed CSV import/export while retaining the
  accepted Cycle 1 D0-D7 representation where applicable.
- Pure Python parallel-bus transition and strobe-sampling analysis shared by
  CLI/API export and the browser table.
- A local Python application server with a versioned API and deterministic
  lifecycle.
- A Python `web` optional dependency extra and a separate hash-checked
  `requirements-web.lock` that installs the complete supported web runtime
  before a `--no-deps` source install. The reviewed development lock and CI
  include the same web versions, while CLI/library installation remains
  possible without the web stack and fails with an actionable message if
  `pico-la web` is requested without the extra.
- React, TypeScript, Vite, Canvas waveform rendering, offline production assets,
  and browser automation.
- Deterministically built frontend assets committed with a build manifest and a
  CI drift check, so an end user can run the source-installed web application
  without Node.js or network access.
- Loopback-only default binding, the canonical-Origin and capability-cookie
  policy frozen in `CYCLE2_BATCH_EXECUTION.md`, no CORS, and an unpredictable
  per-launch capability token for every mutating API operation, including
  cancellation and shutdown. Tokens and local URLs are sanitized from all
  output and committed evidence.
- Finite limits for requests, uploads, decoded samples, response windows, table
  rows, connections, capture concurrency, and shutdown.
- Background capture/file work that does not block the browser event loop or
  server request handling.
- macOS native browser/hardware acceptance and macOS CI.
- Deterministic generated and sanitized hardware-derived fixtures with
  provenance and digests.

### Explicitly excluded

- Firmware edits, builds, flashing, bootloader entry, Wi-Fi changes, or any
  other persistent device-management operation.
- `.lac` reading, writing, conversion, fixtures, or compatibility.
- Any feature that installs, runs, embeds, invokes, or otherwise requires .NET,
  NuGet, pythonnet, Roslyn, or a C# serializer.
- Qt, PySide, QML, Electron, or another bundled browser engine.
- Runtime CDN assets or a runtime Node.js requirement.
- Public or non-loopback serving, remote access, authentication for remote
  deployment, TLS termination, or multi-user operation.
- TCP/Wi-Fi analyzer transport, automatic device selection, or multi-device
  capture.
- Complex, fast, blast, burst, external-clock, immediate, or other capture
  modes beyond the already accepted normal edge-trigger path.
- CPU-specific bus-cycle or instruction decoding, sigrok decoder hosting, or a
  general decoder plugin system.
- Capture editing, regions, annotations, signal composition, or protocol
  annotations.
- Self-contained installers, Electron-style packaging, signing, notarization,
  release publication, or distribution support.
- Native support or acceptance for non-macOS platforms in this cycle.
- Removal or material refactoring of the existing C# application or firmware.
- Beginning Cycle 3.

Excluded work remains deferred even if it would be useful. Discovery is not
authority to implement it.

## Preconditions for the durable goal

Before implementation begins:

- `CYCLE2_ORCHESTRATION.md` and `CYCLE2_BATCH_EXECUTION.md` have been committed,
  reviewed through the protocol under `docs/rewrite-reviews/`, and approved.
- All three final review records say `pass` for the same full reviewed commit.
- The current branch and unrelated worktree changes have been recorded.
- The accepted Cycle 1 completion proof and tests are available.
- Normal dependency-download and CI authority can be requested when needed.

## Preparatory review requirement

Before the durable goal is created, three independent reviewers inspect the
same proposed commit containing both Cycle 2 contracts and the approved
discovery record:

1. **Device protocol and hardware boundary:** firmware bytes, ordered-channel
   packing, word modes, serial lifecycle, recovery, electrical safety, physical
   masks, and hardware proof.
2. **Capture data and browser workflow boundary:** model semantics, replay/CSV,
   bus analysis, API handoff, React/Canvas behavior, usability, and performance
   evidence.
3. **Delivery, web security, verification, and orchestration:** dependency and
   asset reproducibility, loopback/token/origin boundaries, macOS CI,
   agent ownership, authority, checkpoints, evidence, and the durable stop.

Create a Cycle 2 review directory under `docs/rewrite-reviews/` and update its
domain charter/README where needed before reviews begin. Each immutable record
contains reviewer identity, exact reviewed commit, UTC timestamp, verdict
`pass` or `changes_required`, and numbered findings with disposition. Mechanical
corrections may be re-reviewed by the affected reviewer; any substantive
objective, scope, contract, authority, ownership, batch, validation, checkpoint,
security, or stopping-condition change requires all three reviewers to inspect
a new common commit. Final approval requires three `pass` records naming the
same exact commit.

Before C2-B3 physical work, the operator must confirm:

- the attached device remains a Raspberry Pi Pico 2 running the latest
  checked-in V2 firmware built with `BOARD_TYPE=BOARD_PICO_2`;
- the integrated LogicAnalyzerV2 protection circuit, 3.3 V VRef, and common
  ground remain in place;
- the exact physical labels or mapping for D0, D8, D16, and D23;
- every destination is an analyzer input, not an output;
- the 3.3 V, approximately 1 kHz source can safely drive the combined
  high-impedance input load; and
- D1/GPIO3 remains operator-confirmed fixed low at analyzer ground, or another
  explicit fixed-level idle input is provided for the Cycle 1 recovery
  regression; and
- the explicit serial port is supplied at execution time.

The existing port must be committed only as `<PORT_SUPPLIED>`. Unknown voltage,
ground, direction, mapping, or source-drive safety blocks the physical path.

## Discovery model

Discovery is bounded investigation needed to settle the active Cycle 2
interface. It is not permission to redesign the roadmap or change firmware.

### Evidence precedence

For protocol and physical behavior:

1. Reproducible bytes and samples observed from the fixed physical V2 board.
2. The exact checked-in V2 firmware source used for the flashed build.
3. Accepted Cycle 1 fixtures and completion evidence.
4. Independently constructed synthetic fixtures and calculations.
5. Existing C# source only as non-authoritative historical context.

C# application file formats and serializer behavior have no precedence because
they are not Cycle 2 compatibility targets. No uncertainty may be resolved by
running .NET.

For browser behavior, authoritative evidence is the frozen API contract,
standards-based browser behavior, deterministic pure-function fixtures, and
observable production-build behavior. Tests must not derive expected geometry
or bus values by invoking the same production function under test.

### Discovery outcomes

Each uncertainty must end in one state:

- **Resolved locally:** checked-in source, accepted contract, or independent
  fixture settles it.
- **Resolved by bounded experiment:** a non-persistent board or browser
  experiment settles it and produces sanitized evidence.
- **Deferred:** it is unnecessary for the stopping condition and is recorded
  with a later-cycle destination.
- **Authority or operator input required:** the affected path pauses while
  other independent in-scope work continues.

### New-work scope test

New work may enter an active batch only when all are true:

1. The stopping condition cannot be met without it.
2. It stays within the required Cycle 2 surface.
3. It does not cross an authority gate.
4. It has an owning batch and objective acceptance evidence.

Otherwise record and defer it. Do not begin a later-cycle feature merely to keep
an agent occupied.

## Batch boundaries and checkpoints

Cycle 2 executes these six batches in order, as defined in
`CYCLE2_BATCH_EXECUTION.md`:

1. C2-B1: contracts, dependencies, workflow, and web shell.
2. C2-B2: wider capture domain, codec, replay, and CSV core.
3. C2-B3: physical byte-boundary capture gate.
4. C2-B4: parallel-bus core and versioned browser API.
5. C2-B5: offline browser viewer and performance-threshold checkpoint.
6. C2-B6: live browser capture integration and final proof.

A checkpoint is valid only after its complete acceptance gate passes, its
evidence manifest is committed, and its checkpoint record is appended to the
Cycle 2 progress log. Later batches may investigate only disjoint settled
interfaces; they may not become complete out of order. A fix to an earlier
contract reopens that checkpoint and all dependent gates.

C2-B5 contains an authorized decision checkpoint: after reproducible rendering
baselines exist, the orchestrator proposes concrete thresholds, independent
verification checks their measurement method, the acceptance agent records a
verdict, and the operator approves the threshold record. The immutable approved
record becomes a subordinate Cycle 2 acceptance input. This does not authorize
editing or weakening this top-level stopping condition.

## Authority gates

### Authorized within the future Cycle 2 goal

- Read repository sources and accepted evidence.
- Edit Python product code, tests, generated fixtures, built static assets,
  evidence schemas, and documentation under `Software/LogicAnalyzerPy/`.
- Create the frontend source and locks under
  `Software/LogicAnalyzerPy/web/` and install its reviewed dependencies.
- Rename or replace only
  `.github/workflows/logic-analyzer-python-cycle1.yml` with one Cycle 2 workflow
  that runs the approved macOS Python, Node, and browser suite. Creating
  redundant full workflows is not authorized.
- Run deterministic format, lint, type, unit, integration, replay, API,
  frontend, production-build, and headless-browser tests.
- Use an installed browser for the local native macOS smoke.
- Enumerate serial candidates but open only the operator-specified device.
- Send V2 identity and validated normal edge-trigger capture requests for
  approved D0-D23 subsets.
- Use exactly the already characterized single `0xFF` byte only for recovery
  from an in-flight normal capture, followed by the accepted bounded
  drain/close/reopen/re-identification sequence.
- Save sanitized local artifacts and evidence within reviewed project paths.
- Make the smallest fixes needed to pass the active batch and rerun affected
  gates.

### Requires normal execution approval when prompted

- Downloading/installing locked Python, Node, browser-test, or system packages.
- Accessing USB serial or opening a native browser outside the sandbox.
- Pushing a candidate commit to run required hosted CI.

Execution approval does not expand product scope.

### Requires explicit user direction and pauses the affected path

- Editing, building, or flashing firmware; entering the bootloader; changing
  Wi-Fi or persistent device state.
- Installing or running .NET or adding `.lac` support.
- Binding the application server to a non-loopback address or adding remote
  access.
- Destructive repository operations or deletion/replacement of the C# app.
- Adding excluded or later-cycle product features.
- Publishing packages/releases, packaging, signing, or notarization.
- Editing these approved Cycle 2 contracts outside a separately requested
  document-review step.
- Changing the durable objective, batch ownership, or stopping condition.
- Choosing undocumented electrical connections or voltage levels.

## Validation loop

Every batch follows `CYCLE2_BATCH_EXECUTION.md` and repeats:

1. Define or reproduce the missing behavior with an independent test or
   evidence artifact.
2. Make the smallest in-scope implementation change.
3. Run focused checks for changed Python and/or frontend components.
4. Run the accumulated non-hardware Python, frontend, API, and browser suites.
5. Run the owning opt-in physical or native-browser checks when applicable.
6. Diagnose failures without weakening assertions or rewriting expected
   behavior to match production.
7. Record commands, results, provenance, decisions, limitations, and deferrals.
8. Accept the checkpoint only after independent verification and acceptance
   both pass.

The canonical Python validation remains:

```bash
cd Software/LogicAnalyzerPy
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e .
.venv/bin/python -m pip check
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy src
.venv/bin/python -m pytest -m "not hardware"
.venv/bin/python -m pico_logic_analyzer --help
```

C2-B1 additionally freezes this supported clean web-runtime installation path,
which is run on macOS CI before production web smoke:

```bash
cd Software/LogicAnalyzerPy
python3.12 -m venv .venv-web
.venv-web/bin/python -m pip install --require-hashes -r requirements-web.lock
.venv-web/bin/python -m pip install --no-build-isolation --no-deps -e '.[web]'
.venv-web/bin/python -m pip check
```

C2-B1 must establish and document canonical frontend commands equivalent to:

```bash
cd Software/LogicAnalyzerPy/web
npm ci
npm run lint
npm run typecheck
npm test -- --run
npm run build
npm run test:browser
```

The exact script names and pinned Node version are frozen in C2-B1 and then
replace the equivalent placeholders above. `package-lock.json` is the
JavaScript dependency identity; `requirements-dev.lock` remains the Python
dependency identity. Production execution must use prebuilt local assets and
must not invoke Node or contact a CDN.

Clean bootstraps are required in C2-B1, CI, C2-B5, and C2-B6. Later local
batches may reuse environments only when interpreter/runtime versions and lock
digests match their evidence records. Focused checks never replace accumulated
checks.

## Progress and evidence

C2-B1 creates:

- `Software/LogicAnalyzerPy/docs/cycle-2-orchestration-progress.md`;
- a Cycle 2 machine-readable evidence schema at
  `Software/LogicAnalyzerPy/docs/evidence-manifest/cycle2-schema.json` and its
  validator at `Software/LogicAnalyzerPy/scripts/validate_cycle2_evidence.py`;
  and, if useful, a directory marker or template whose name and contents state
  unambiguously that it is not evidence and cannot satisfy a checkpoint.

C2-B1 does not pre-create any future batch manifest. After C2-B1 verification
and acceptance evidence exists, the orchestrator atomically creates only
`Software/LogicAnalyzerPy/testdata/evidence/c2-b1.json`, validates it, commits
it, and only then appends the C2-B1 checkpoint. C2-B2 through C2-B6 follow the
same lifecycle: the owning batch alone atomically creates its `c2-bN.json` only
after that batch's verification and acceptance evidence exists; schema
validation passes before the checkpoint record is appended. A filename,
placeholder, empty object, example, or template for a future manifest is not
evidence and must never be pre-populated or presented as an accepted manifest.

The Cycle 2 evidence schema is JSON Schema draft 2020-12 with
`schema_version: 2`, checkpoint pattern `^C2-B[1-6]$`, and
`additionalProperties: false` recursively for every object. Each manifest must
validate with:

```bash
cd Software/LogicAnalyzerPy
.venv/bin/python scripts/validate_cycle2_evidence.py \
  docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-bN.json
```

The validator rejects fields or values containing an actual serial path,
capability token, machine-local URL, credential, user home, or other secret.
Each accepted manifest records:

- full tested commit and tree, plus clean or explicitly qualified worktree;
- UTC time; OS/version and architecture; Python and Node versions; browser name,
  version, and automation version where applicable;
- separate SHA-256 values for `requirements-dev.lock`,
  `requirements-web.lock`, `package-lock.json`, and the built-asset manifest,
  using an explicit not-applicable value only where the schema permits it;
- normalized command, exit status, stable command-verifier identity, and CI
  run/job URL or identifier plus the exact CI commit when CI is required;
- evidence source category (`firmware-source`, `cycle1-accepted`, `synthetic`,
  `hardware-observation`, `browser-observation`, or `generated-fixture`), source
  revision, artifact path, and SHA-256;
- for hardware, sanitized board/firmware/front-end identity, mapping, voltage,
  ground, signal, capture parameters, expected masks, and results; and
- stable and mutually distinct implementation, verification, and acceptance
  identities and their verdicts; decisions; numbered findings and disposition;
  limitations; deferred work; and
- explicit identifiers for every applicable one of the fourteen stopping
  conditions, with evidence artifact references and digests. C2-B5/B6 also
  record the approved performance-threshold record digest.

The actual serial path, launch capability token or cookie, machine-local URL,
credentials, user-selected filename, and sensitive target details must not be
committed or reflected in evidence. Record the serial path only as
`<PORT_SUPPLIED>` and token-bearing values only as `<TOKEN_REDACTED>`. Schema
validation is a gate for every checkpoint and final completion, not a
best-effort documentation check. An evidence manifest is immutable once its
checkpoint is accepted; a reopened checkpoint produces a separately identified
replacement or correction record rather than silently mutating prior evidence.

Final accumulated, physical, performance, and native-browser proofs must run
against one identified candidate with no implementation changes afterward.
Unrelated user changes must be enumerated and excluded. Uncommitted product,
test, lock, workflow, or built-asset changes invalidate final completion proof.

## Failure, retry, and blocking policy

- A normal implementation or test failure remains in the owning batch.
- A regression reopens the earliest owning checkpoint and pauses dependent
  acceptance.
- Browser timing variance is diagnosed and measured; it is not grounds to
  remove an approved threshold silently.
- Missing hardware input, unsafe wiring uncertainty, hosted-CI unavailability,
  or a required scope expansion is recorded precisely. Continue independent
  in-scope work where useful.
- The durable goal may be marked blocked only after the same external blocker
  has persisted for the number of consecutive goal turns required by the goal
  system and no meaningful in-scope work remains.
- Hardware absence, a skipped native test, or a fake substitute never becomes
  completion evidence.

## Completion proof and handoff

At completion, produce
`Software/LogicAnalyzerPy/docs/cycle-2-completion.md` containing:

- all fourteen stopping conditions with linked pass evidence;
- the exact final candidate commit/tree and dependency/build digests;
- canonical Python, frontend, CI, physical, and native-browser commands and
  results;
- sanitized device, firmware, electrical, signal, and capture parameters;
- replay/CSV/bus determinism and security evidence;
- rendering baselines, approved thresholds, method, and final measurements;
- the macOS native acceptance result and macOS-only support statement;
- every checkpoint/review/evidence path and digest;
- known limitations and deferred work; and
- repository status plus confirmation that firmware, .NET, persistent device
  state, public serving, packaging, publishing, and Cycle 3 were untouched.

Stop successfully only when every stopping condition is linked to objective
evidence and the independent final acceptance verdict is `pass`. Do not begin
Cycle 3.
