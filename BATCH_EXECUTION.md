# Logic Analyzer Python Rewrite: Cycle 1 Batch Procedure

## Purpose and authority

This document is the per-batch operating procedure for Cycle 1. It is subordinate
to `ORCHESTRATION.md` and must be used with the technical roadmap at
`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`.

Architectural reviewer charters and durable review records live under
`docs/rewrite-reviews/` and follow its `README.md` protocol.

It defines how an orchestrator turns the Cycle 1 objective into bounded agent
assignments, verifies each result independently, integrates it, and records a
checkpoint. It does not authorize Cycle 2 work and does not start a `/goal`.

## Required reading order

Before selecting the first batch, the orchestrator must read:

1. Repository `AGENTS.md` and all included instructions.
2. `ORCHESTRATION.md` in full.
3. This document in full.
4. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`, concentrating
   on its execution policy, decision log, source inventory, architectural rules,
   Cycle 1 hardware gate, and consciously deferred work.
5. The firmware and C# sources named by the active batch.

Agents assigned a batch must receive its scope, relevant source references,
owned files, acceptance evidence, prohibited work, and current checkpoint log.

## Batch state model

Each batch has exactly one state:

- **Pending:** prerequisites have not been accepted.
- **Ready:** prerequisites and inputs are present.
- **In progress:** implementation or independent verification is active.
- **Verifying:** implementation is integrated and the complete batch gate is
  running.
- **Complete:** the gate passed and a checkpoint record was appended.
- **Blocked:** the same external blocker has persisted according to the policy
  in `ORCHESTRATION.md`, and no meaningful in-scope work remains.

Only one Cycle 1 batch may be in `Verifying` at a time. Normally only the
earliest incomplete batch may become `Complete`; later-batch experiments do not
advance the checkpoint sequence.

## Batch manifest

Before assigning work, the orchestrator writes or updates the active-batch entry
in `Software/LogicAnalyzerPy/docs/orchestration-progress.md` with:

```markdown
## C1-BN: <name>

- State: Ready
- Objective: <one bounded outcome>
- Prerequisites: <accepted checkpoints and required inputs>
- Implementation agent: <stable identity>
- Verification agent: <different stable identity>
- Acceptance agent: <third stable identity>
- In scope: <specific behavior and artifacts>
- Out of scope: <nearby tempting work>
- Owned files: <non-overlapping paths per agent>
- Source evidence: <files/traces/fixtures to consult>
- Acceptance evidence: <tests, commands, artifacts, hardware observations>
- Authority notes: <allowed actions and any approval required>
- Risks/unknowns: <items to resolve or defer>
```

Do not assign a batch described only as “continue the rewrite.”

For C1-B1 only, because the project and progress file do not exist yet, place
the manifest in the orchestrator's current progress update before assignment.
Copy it into the newly created progress file before accepting the C1-B1
checkpoint. Later batches must update the checked-in progress file first.

## Standard batch procedure

### 1. Select and bound

Select the earliest incomplete batch whose prerequisites are satisfied. Restate
its single outcome and apply the new-work scope test from `ORCHESTRATION.md`.
Move unrelated findings to a deferred section immediately.

### 2. Preflight

- Inspect repository status and preserve unrelated user changes.
- Confirm required sources, fixtures, tools, and operator inputs exist.
- Confirm the prior checkpoint still passes when the active work depends on it.
- Resolve exact output paths and agent file ownership.
- Identify commands that may require execution approval.
- For a hardware batch, verify wiring assumptions and prohibit persistent
  device mutation.

If a prerequisite is absent, keep the batch `Pending` or record the precise
blocker. Do not simulate approval or physical evidence.

### 3. Assign

Use bounded roles:

- **Implementation agent:** owns the smallest production-code surface required
  by the batch and its focused tests.
- **Verification agent:** independently derives negative, boundary,
  compatibility, fragmentation, or hardware checks from authoritative sources.
- **Orchestrator/integrator:** owns shared-interface decisions, conflict
  resolution, accumulated-suite execution, progress records, and checkpoint
  acceptance.

An agent assignment must state what it may edit and what it must not implement.
The implementation, verification, and acceptance identities must be three
distinct agents for production behavior and fixtures. A verifier may not approve
production behavior, fixtures, or expected results it authored, and may not
silently rewrite an expectation to match implementation. Its handoff verdict is
exactly `pass` or `changes_required`. The acceptance agent records every finding
and disposition before checkpoint acceptance. Agents may inspect all relevant
sources but should not rewrite another agent's owned files without reassignment.

If staffing or a conflict invalidates separation, pause acceptance and reassign
the affected work to a fresh agent in a later turn. Separation may be achieved
sequentially; it may not be waived or represented as independent self-review.

With limited concurrency, keep one slot available to the orchestrator. If an
interface is not settled, investigate it before parallelizing downstream work.

### 4. Implement and verify independently

The implementation agent should first add or identify focused evidence, then
make the smallest change that satisfies it. The verification agent should test
observable behavior without copying implementation logic into expected values.

Every agent handoff must include:

- files changed;
- behavior implemented or verified;
- commands run and exact outcomes;
- evidence provenance;
- assumptions, discrepancies, and deferrals;
- repository/commit state if commits are in use.

### 5. Integrate

The orchestrator reviews for:

- compliance with `ORCHESTRATION.md` scope and authority;
- explicit binary sizes/order/padding;
- separation among model, protocol, transport, driver, format, and CLI layers;
- bounded allocations and finite timeouts;
- safe cleanup on every path;
- deterministic artifacts with no secrets or machine-local values;
- tests that fail for the intended defect;
- absence of unrelated edits or later-cycle features.

Resolve conflicts by preserving the accepted interface and smallest in-scope
behavior. Any changed interface requires rerunning affected earlier gates.

### 6. Run the validation loop

Run focused tests first, then the accumulated non-hardware suite:

```bash
cd Software/LogicAnalyzerPy
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
.venv/bin/python -m pip install --no-deps -e .
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy src
.venv/bin/python -m pytest -m "not hardware"
.venv/bin/python -m pico_logic_analyzer --help
```

Run the clean bootstrap in a new environment for C1-B1, CI, and C1-B5; later
local batches may reuse `.venv` only when its Python version and lock-file digest
match their evidence manifest. Hardware batches then run their explicit opt-in
command. Do not treat an untested code path, a skipped required test, or manual
visual inspection alone as passing evidence.

### 7. Record and checkpoint

Append the checkpoint record shown below. Include failures encountered during
the batch when they explain design or risk. Mark `Complete` only after every
acceptance item passes.

### 8. Decide next action

- If the gate passes, select the next batch.
- If implementation is faulty, remain in the batch and iterate.
- If an earlier contract regressed, reopen the owning checkpoint.
- If the issue is outside Cycle 1, defer it.
- If it crosses an authority gate or requires unavailable input, request user
  direction and continue only independent safe work.

## Settled Cycle 1 public and data contracts

These decisions are inputs to the batches below and must be copied into focused
ADRs/docs during C1-B1. Changing them is a substantive contract change.

### Capture model

- `samples` is a one-dimensional C-contiguous NumPy array with exact dtype
  `uint8`; one element is one raw returned word.
- Cycle 1 requests exactly logical channels `[0,1,2,3,4,5,6,7]` in ascending
  order, rejects duplicates/subsets, and uses firmware capture mode `0`.
- Raw bit `i` represents request-list position `i`, which in Cycle 1 is logical
  channel D`i`. The model retains `channel_ids=[0..7]`, physical/header mapping,
  and display labels separately.
- `sample_rate_hz`, requested and actual sample counts, `pre_trigger_samples`,
  `post_trigger_samples`, `trigger_channel`, `trigger_edge`, device identity,
  and negotiated capabilities are required positive/validated metadata.
- Actual sample count must equal the validated requested total and the array
  length. Indices `0..pre_trigger_samples-1` are the pre-trigger region; the
  trigger marker is index `pre_trigger_samples-1`; post-trigger samples begin at
  index `pre_trigger_samples`. Sample time relative to the marker is
  `(index-trigger_index)/sample_rate_hz`.
- The trigger channel must be one of D0–D7 and is always captured. Both rising
  and falling values are supported and independently fake-tested.

### CSV artifact

- UTF-8, LF line endings, RFC-4180-compatible comma separation, no locale-
  dependent formatting.
- Header is exactly
  `sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7`.
- `sample_index` is zero-based; `time_seconds` is trigger-relative and formatted
  with the documented deterministic `.12g` rule; `trigger` is `1` only at the
  trigger marker and `0` otherwise; data columns are `0` or `1` derived from the
  corresponding raw bit.
- CSV is an inspection/export format, not the authoritative replay format. A
  future importer must treat its time and trigger columns as authoritative and
  must not silently invent missing timing for unrelated CSV files.

### Provisional replay artifact

- Schema major version `1`, explicitly marked provisional.
- Exactly two ZIP/NPY members: `samples.npy` and `metadata.npy`. The latter is a
  one-dimensional `uint8` array containing canonical UTF-8 JSON; no object,
  structured, string, or nested sample dtype is permitted.
- Required JSON keys are schema version, sample rate, requested/actual/pre/post
  counts, trigger index/channel/edge, channel IDs/labels/mapping, and sanitized
  device identity/capabilities. Metadata is inert and may not name, configure,
  import, or execute decoder code.
- Before NumPy materialization, inspect the ZIP central directory and enforce
  documented numeric defaults: file size at most 32 MiB, exactly two unique
  members, metadata uncompressed size at most 64 KiB, sample member uncompressed
  size at most 17 MiB, and sample count at most 16,777,216. Reject encrypted,
  duplicate, unexpected, path-bearing, or unsupported-compression members.
- Load with `allow_pickle=False`; require samples rank 1 and exact `uint8`,
  metadata rank 1 and exact `uint8`, a flat schema with bounded strings/lists,
  supported major version, and counts consistent with the sample array. Reject
  unknown top-level keys in Cycle 1.

### CLI contract

```text
pico-la devices [--json]
pico-la info --port PORT [--json] [--timeout SECONDS]
pico-la capture --port PORT --sample-rate HZ --trigger-channel CHANNEL
                --edge {rising,falling} --pre-samples N --post-samples N
                --csv PATH --replay PATH [--timeout SECONDS] [--force]
pico-la replay-validate PATH [--json]
pico-la hardware-smoke --port PORT --signal-hz HZ --sample-rate HZ
                       --trigger-channel CHANNEL --edge {rising,falling}
                       --pre-samples N --post-samples N
```

- Exit codes: `0` success, `2` usage/configuration, `3` connection/protocol,
  `4` capture timeout/cancellation, `5` validation/replay, `6` output I/O.
- JSON or other requested machine data goes to stdout; diagnostics and progress
  go to stderr. JSON schema is tested when `--json` is offered.
- Capture output paths are explicit. Existing outputs are rejected without
  `--force`. Both outputs are written, fsynced, and validated in same-directory
  temporary files before either final name changes. Installation is a
  transaction: preserve replaceable originals as temporary backups, atomically
  rename both outputs, restore originals/remove newly installed outputs if
  either rename fails, then remove backups after success. Failed capture or
  export leaves no new apparently valid final artifact.

### Serial and receive contract

- Configure 115200 baud, 8 data bits, no parity, one stop bit, no software or
  hardware flow control, and finite read/write timeouts. Assert DTR and RTS as
  the current compatible client does; document which USB CDC targets ignore
  these settings and the exact configure/open/stabilize/drain order.
- One byte-oriented receive buffer owns both ASCII and binary parsing. Do not
  layer independent buffered text and binary readers over the same stream.
- Identity is exactly five newline-terminated ASCII fields, each at most 128
  bytes including newline and matching the documented grammar. Capture status
  is one bounded line. Overlong, unterminated, missing, or extra fields fail.
- A coalesced `CAPTURE_STARTED\n` plus four-byte little-endian sample count and
  payload loses no bytes. The count must equal the validated request and be
  bounded before allocation/read. Non-burst Cycle 1 consumes and requires a
  trailing zero timestamp-count byte.
- Timeout or Ctrl-C during an in-flight capture sends the characterized single
  `0xFF` V2 cancellation byte, applies documented flush/drain/timing, closes and
  reopens, and re-identifies. This internal recovery primitive is required;
  richer public abort semantics remain deferred.

## Cycle 1 batch sequence

### C1-B1: Preflight, scaffold, and narrow protocol evidence

**Outcome:** A runnable Python 3.12 project skeleton and evidence sufficient to
implement V2 identity and one normal 8-channel edge-triggered capture without
guessing native layout.

**Prerequisites:** Approved preparatory documents; operator assertion that the
target is intended to run V2 analyzer firmware (exact identity may remain open
until C1-B3); workspace is writable.

**In scope:**

- Create `Software/LogicAnalyzerPy/` with `pyproject.toml`, `src/`, `tests/`,
  `testdata/`, and `docs/`.
- Configure CLI entry point, Ruff, the approved type checker, pytest markers,
  hash-pinned `requirements-dev.lock`, and the narrowly authorized
  `.github/workflows/logic-analyzer-python-cycle1.yml` with explicit Python 3.12
  Linux and macOS jobs running the canonical bootstrap/validation commands.
- Create `docs/orchestration-progress.md`, `docs/device-protocol.md`, and the
  Cycle 1 operator-input template, capture-model ADR, CLI contract, replay
  format/security contract, and evidence-manifest schema.
- Document the implemented frame delimiters/escaping, identity exchange,
  capture request offsets, explicit padding/size, 8-bit result format, and
  byte-oriented text/binary receive grammar, relevant serial settings/open
  ordering, and minimal `0xFF` cancellation/recovery exchange.
- Make the operator template require confirmed board/front-end/shifter revision,
  target logic voltage and VRef, permitted input range, common ground, and
  D0–D7 header/GPIO mapping. Unknown values block hardware. State explicitly
  that bare Pico GPIO must not receive 5 V.
- Add provenance-tagged golden bytes for identity and rising/falling 8-channel
  requests. Obtain a known-good C#/board trace when available; otherwise state
  which fields remain to be confirmed in C1-B3/C1-B4.

**Out of scope:** Production serial driver, GUI dependencies, broad feature
inventory, other commands/modes, and exhaustive protocol documentation.

**Primary sources:**

- `Firmware/LogicAnalyzer_V2/LogicAnalyzer_Structs.h`
- `Firmware/LogicAnalyzer_V2/LogicAnalyzer.c`
- `Software/LogicAnalyzer/SharedDriver/AnalyzerDriverBase.cs`
- `Software/LogicAnalyzer/SharedDriver/LogicAnalyzerDriver.cs`
- `Software/LogicAnalyzer/SharedDriver/CaptureSession.cs`
- `Software/LogicAnalyzer/SharedDriver/VersionValidator.cs`

**Acceptance:**

- Clean source install succeeds on Python 3.12.
- Clean bootstrap uses the hash-pinned lock and succeeds in both CI jobs.
- CLI help succeeds.
- Static/test tools execute successfully, even if the initial test set is
  small.
- Golden fixtures have provenance and explicit expected lengths/bytes.
- Protocol note distinguishes observed behavior, source-derived behavior, and
  unresolved hardware confirmation.
- Data, CSV/replay, CLI, serial, electrical, recovery, and evidence contracts
  match the settled section above.
- No Qt/pythonnet/Roslyn dependency is introduced.

### C1-B2: Models, codec, and fake/replay contract

**Outcome:** Pure, hardware-independent code can encode the narrow requests and
parse identity/capture streams correctly under normal and adverse reads.

**Prerequisite:** C1-B1 complete.

**In scope:**

- Typed device information and narrow capture configuration/results.
- Enforce the exact D0–D7 capture model, trigger convention, and metadata
  invariants defined above.
- Frame escaping/encoding and identity/capture parsing with explicit byte order,
  widths, padding, and allocation limits.
- One bounded byte-oriented parser for ASCII and binary response phases.
- Minimal transport protocol supporting exact read, write, finite timeout,
  close, and cancellation through the bounded `0xFF` recovery primitive.
- Scripted fake/replay transport.
- Tests for reserved bytes, fragmented reads, truncated/malformed responses,
  invalid lengths, timeout, disconnect, and idempotent cleanup.
- Tests for coalesced status-plus-binary data, overlong/unterminated/extra ASCII
  fields, trailing timestamp-count validation, timeout/Cancel recovery followed
  by identity, and every replay archive/dtype/size/schema bound above.

**Out of scope:** pySerial, CLI hardware commands, writing production artifacts,
channel widths above eight, or generic future protocol abstractions.

**Acceptance:**

- Golden byte-for-byte request tests pass.
- Fake identity and capture round trips pass with one-byte fragmentation.
- A single-read coalesced status/binary response parses losslessly.
- Malformed size cannot allocate beyond the negotiated/configured bound.
- Timeout/disconnect tests terminate and close resources.
- Timeout/cancellation fake tests send `0xFF`, follow the recovery state
  sequence, and successfully re-identify without a simulated power cycle.
- Capture model and hostile replay-container tests pass.
- No core module imports serial, Qt, or CLI modules.
- Accumulated non-hardware validation passes.

### C1-B3: pySerial discovery and physical identity

**Outcome:** The CLI safely locates candidate ports, opens only the explicitly
selected port, reads the attached V2 analyzer identity, and closes/reopens it.

**Prerequisites:** C1-B2 complete; operator supplies `<PORT>`; host permission to
open the device is available.

**In scope:**

- pySerial transport.
- Exact serial configuration/open/stabilize/drain/close/reopen behavior from the
  settled contract, with constructor/configuration-sequence tests.
- Best-effort `devices` output using VID `0x1209`, PID `0x3020`, while tolerating
  missing metadata.
- Exact `devices` and explicit-port `info` CLI contracts above, including JSON,
  exit-code, and stdout/stderr subprocess tests.
- Finite timeouts, clear errors, close on all paths, and an identity read after
  close/reopen.
- Fake pySerial/list-port tests plus opt-in real identity smoke.

**Out of scope:** Automatic device selection, remembered devices, hot-plug
monitoring, TCP, or capture implementation.

**Acceptance:**

- No command silently selects among devices.
- Fake port metadata tests cover Linux/macOS-like records and absent fields.
- Real identity/capabilities match the recorded V2 baseline.
- Exact reported identity is resolved here. A mismatch pauses the hardware path
  for user direction and does not rewrite the baseline.
- Two identity operations separated by close/reopen succeed.
- Unplug/permission/timeout failures are actionable and release the port.
- No persistent device state is changed.

### C1-B4: Physical capture, CSV, and provisional replay

**Outcome:** The CLI performs the required normal 8-channel capture and produces
deterministic outputs suitable for immediate SBC debugging and replay.

**Prerequisites:** C1-B3 complete; operator supplies safe periodic-signal
parameters and wiring.

**In scope:**

- Validate the narrow capture configuration.
- Encode/send both rising and falling edge-triggered requests for exactly D0–D7.
- Read/validate raw 8-bit samples with configured/negotiated bounds.
- Deterministic CSV using the exact self-timed header/row contract above.
- Provisional versioned `.npz` containing raw sample words and validated
  non-object metadata, loadable with pickling disabled.
- CLI capture/export/replay validation.
- Atomic output, collision, `--force`, stdout/stderr, exit-code, and failed-
  export subprocess tests.
- Opt-in physical capture using the operator's known periodic source.

**Out of scope:** Rich measurements, graphical viewing, public long-term replay
schema, `.lac`, wider modes, immediate/no-trigger unless already proven and
strictly required, and graceful firmware abort.

**Acceptance:**

- Fake capture/export tests pass for rising and falling edge cases.
- CSV is byte-deterministic for a fixed capture and reloads to expected values.
- `.npz` loads with `allow_pickle=False`; schema/version and required metadata
  validate under all archive/dtype/size bounds; samples match exactly.
- Real capture returns the requested sample count and 8-bit width.
- The periodic channel is nonconstant, contains the requested edge polarity,
  and measures within the documented tolerance.
- Fixed-high/low input checks pass when those optional wires are present.
- The port closes after the command.

### C1-B5: Lifecycle hardening and final hardware proof

**Outcome:** The entire Cycle 1 stopping condition is independently verified,
including failure cleanup and a second real capture after close/reopen.

**Prerequisite:** C1-B4 complete.

**In scope:**

- Independent review of protocol bytes, bounds, timeouts, cleanup, deterministic
  output, and scope compliance.
- Regression tests for all Cycle 1 defects found during integration.
- Ctrl-C, timeout, malformed input, disconnect, and close/reopen verification.
- A physical no-trigger timeout or Ctrl-C recovery that sends the characterized
  `0xFF` byte, re-identifies, and then captures without a power cycle.
- Stable documented `hardware-smoke` command or equivalent pytest interface.
- Two real captures separated by explicit close/reopen.
- Final progress record and Cycle 1 handoff.

**Out of scope:** Fixing non-blocking later-cycle shortcomings or polishing the
tool into a full release.

**Acceptance:** Every stopping-condition item in `ORCHESTRATION.md` has linked
evidence; canonical non-hardware commands pass; the hardware command passes;
the second real capture succeeds; C# rollback remains intact; no prohibited
operation occurred; repository status and deferred work are documented.

## Checkpoint record template

Append this after each accepted batch:

```markdown
### Checkpoint C1-BN — <name>

- State: Complete
- Completed at: <ISO-8601 timestamp>
- Tested commit: <full commit hash>
- Tested tree: <tree hash>
- Worktree state: <clean or explicitly enumerated unrelated changes>
- Implementation agent: <stable identity>
- Verification agent and verdict: <different identity; pass>
- Acceptance agent: <third identity>
- Environment: <OS/version, architecture, Python version, lock SHA-256>
- Objective evidence: <tests/artifacts/observations>
- Files changed: <paths or concise groups>
- Focused commands: <command and pass/fail result>
- Accumulated commands: <command and pass/fail result>
- Hardware evidence: <not applicable, or sanitized board/signal/result summary>
- Evidence manifest: <path and SHA-256>
- Decisions/discrepancies: <what was settled and provenance>
- Deferred findings: <roadmap destination>
- Known limitations: <remaining constraints>
- Repository state: <commit/worktree summary>
- Next batch: <identifier and unmet inputs>
- Blocked: no
```

For failed attempts, keep a concise note under the active manifest rather than
creating a false completed checkpoint.

## Independent verification expectations

Verification must derive expectations from external behavior and authoritative
sources, not mirror production code. Examples:

- Hard-code reviewed golden packet bytes instead of calling the encoder to
  construct expected values.
- Feed parser data in adversarial fragment sizes.
- Compare explicit field offsets with both firmware definitions and observed
  traces.
- Corrupt lengths and delimiters independently.
- Verify output using a separate CSV reader and NumPy load with pickling off.
- For hardware, calculate frequency tolerance from declared sample rate and
  fixture stability, then inspect captured transitions rather than trusting a
  success message.

The verification agent should report ambiguous evidence before changing an
expected result. If implementation and verification recommendations tie, use
the existing reviewed decision log in the technical plan; otherwise escalate a
true objective/scope change.

## Regression and rollback procedure

When a completed checkpoint regresses:

1. Identify the earliest owning checkpoint.
2. Change its state back to `In progress` in the log with the regression
   evidence.
3. Pause downstream interface expansion.
4. Apply the smallest correction in the owning files.
5. Rerun that checkpoint and every dependent accumulated gate.
6. Append a correction record; do not rewrite historical evidence as though the
   regression never occurred.

Do not delete or rewrite the C# application as part of rollback. It remains the
comparison path throughout Cycle 1.

## Batch-level authority checklist

Before hardware or external commands, confirm:

- [ ] The operation is identity or the characterized normal 8-channel capture.
- [ ] The operator supplied the exact port and safe signal parameters.
- [ ] No bootloader, flash, Wi-Fi, network, or persistent mutation command is
      reachable from the requested path.
- [ ] Timeouts are finite and cleanup is installed before the request begins.
- [ ] Evidence paths are resolved and contain no secrets or machine-local values.
- [ ] Required execution approval has been requested through the normal tool
      mechanism.

## Cycle 1 final review packet

Before declaring the last batch complete, assemble links to:

- `ORCHESTRATION.md` stopping-condition checklist;
- the five checkpoint records;
- protocol documentation and provenance-tagged fixtures;
- accumulated non-hardware test output;
- hardware operator procedure and sanitized result;
- CSV/replay determinism evidence;
- cleanup and second-capture evidence;
- deferred-work list and known limitations;
- repository status and rollback confirmation.

Preparatory-process step 4 reviews and approves `ORCHESTRATION.md` and this
batch procedure; only afterward should a durable goal be created. The final
packet above is instead the completion evidence reviewed at the end of that
goal; only after it passes may the Cycle 1 goal be marked complete.
