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
Do not have implementation and verification agents edit the same test file.
Agents may inspect all relevant sources but should not rewrite another agent's
owned files without reassignment.

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
python -m ruff check .
python -m mypy src
python -m pytest -m "not hardware"
python -m pico_logic_analyzer --help
```

Use the approved alternative type checker if Cycle 1 selected Pyright and
recorded that decision. Hardware batches then run their explicit opt-in command.
Do not treat an untested code path, a skipped required test, or manual visual
inspection alone as passing evidence.

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

## Cycle 1 batch sequence

### C1-B1: Preflight, scaffold, and narrow protocol evidence

**Outcome:** A runnable Python 3.12 project skeleton and evidence sufficient to
implement V2 identity and one normal 8-channel edge-triggered capture without
guessing native layout.

**Prerequisites:** Approved preparatory documents; known target board/firmware;
workspace is writable.

**In scope:**

- Create `Software/LogicAnalyzerPy/` with `pyproject.toml`, `src/`, `tests/`,
  `testdata/`, and `docs/`.
- Configure CLI entry point, Ruff, the approved type checker, pytest markers,
  and Linux/macOS non-hardware CI.
- Create `docs/orchestration-progress.md`, `docs/device-protocol.md`, and the
  Cycle 1 operator-input template.
- Document the implemented frame delimiters/escaping, identity exchange,
  capture request offsets, explicit padding/size, 8-bit result format, and
  relevant serial settings.
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
- CLI help succeeds.
- Static/test tools execute successfully, even if the initial test set is
  small.
- Golden fixtures have provenance and explicit expected lengths/bytes.
- Protocol note distinguishes observed behavior, source-derived behavior, and
  unresolved hardware confirmation.
- No Qt/pythonnet/Roslyn dependency is introduced.

### C1-B2: Models, codec, and fake/replay contract

**Outcome:** Pure, hardware-independent code can encode the narrow requests and
parse identity/capture streams correctly under normal and adverse reads.

**Prerequisite:** C1-B1 complete.

**In scope:**

- Typed device information and narrow capture configuration/results.
- Frame escaping/encoding and identity/capture parsing with explicit byte order,
  widths, padding, and allocation limits.
- Minimal transport protocol supporting exact read, write, finite timeout,
  close, and cancellation-by-close semantics.
- Scripted fake/replay transport.
- Tests for reserved bytes, fragmented reads, truncated/malformed responses,
  invalid lengths, timeout, disconnect, and idempotent cleanup.

**Out of scope:** pySerial, CLI hardware commands, NumPy file format beyond a
minimal model decision, channel widths above eight, or generic future protocol
abstractions.

**Acceptance:**

- Golden byte-for-byte request tests pass.
- Fake identity and capture round trips pass with one-byte fragmentation.
- Malformed size cannot allocate beyond the negotiated/configured bound.
- Timeout/disconnect tests terminate and close resources.
- No core module imports serial, Qt, or CLI modules.
- Accumulated non-hardware validation passes.

### C1-B3: pySerial discovery and physical identity

**Outcome:** The CLI safely locates candidate ports, opens only the explicitly
selected port, reads the attached V2 analyzer identity, and closes/reopens it.

**Prerequisites:** C1-B2 complete; operator supplies `<PORT>`; host permission to
open the device is available.

**In scope:**

- pySerial transport.
- Best-effort `devices` output using VID `0x1209`, PID `0x3020`, while tolerating
  missing metadata.
- Explicit-port `info` command with human-readable and deterministic machine-
  readable output if the CLI exposes JSON.
- Finite timeouts, clear errors, close on all paths, and an identity read after
  close/reopen.
- Fake pySerial/list-port tests plus opt-in real identity smoke.

**Out of scope:** Automatic device selection, remembered devices, hot-plug
monitoring, TCP, or capture implementation.

**Acceptance:**

- No command silently selects among devices.
- Fake port metadata tests cover Linux/macOS-like records and absent fields.
- Real identity/capabilities match the recorded V2 baseline.
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
- Encode/send rising and falling edge-triggered normal 8-channel requests.
- Read/validate raw 8-bit samples with configured/negotiated bounds.
- Deterministic CSV with stable channel headers and sample rows.
- Provisional versioned `.npz` containing raw sample words and validated
  non-object metadata, loadable with pickling disabled.
- CLI capture/export/replay validation.
- Opt-in physical capture using the operator's known periodic source.

**Out of scope:** Rich measurements, graphical viewing, public long-term replay
schema, `.lac`, wider modes, immediate/no-trigger unless already proven and
strictly required, and graceful firmware abort.

**Acceptance:**

- Fake capture/export tests pass for rising and falling edge cases.
- CSV is byte-deterministic for a fixed capture and reloads to expected values.
- `.npz` loads with `allow_pickle=False`; schema/version and required metadata
  validate; samples match the capture exactly.
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
- Objective evidence: <tests/artifacts/observations>
- Files changed: <paths or concise groups>
- Focused commands: <command and pass/fail result>
- Accumulated commands: <command and pass/fail result>
- Hardware evidence: <not applicable, or sanitized board/signal/result summary>
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
