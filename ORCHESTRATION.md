# Logic Analyzer Python Rewrite: Cycle 1 Orchestration Contract

## Status and purpose

This is the top-level contract for a future durable `/goal`. It governs only
Cycle 1 of the Python logic-analyzer rewrite: proving a narrow, useful capture
path against one physical Pico-based logic analyzer. It does not itself start a
goal and must be reviewed and approved together with `BATCH_EXECUTION.md` before
any durable goal is created.

This contract follows the official OpenAI `/goal` guidance to name one durable
objective and stopping condition, point to required plans, define proof
commands/artifacts, work in checkpoints, and keep a short progress log:
<https://learn.chatgpt.com/use-cases/follow-goals>.

The documents have distinct authority:

1. `AGENTS.md` and included repository instructions govern agent behavior.
2. This document governs objective, scope, authority, checkpoints, validation,
   and stopping conditions for Cycle 1.
3. `BATCH_EXECUTION.md` governs how each batch is selected, assigned,
   implemented, independently verified, integrated, and recorded.
4. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` is the
   technical roadmap and source inventory. Its later-cycle work is context, not
   authority to expand Cycle 1.
5. `docs/rewrite-reviews/` defines the architectural review domains and stores
   immutable, commit-anchored review records.

If these documents conflict, follow the order above and record the conflict in
the progress log before proceeding.

## Durable objective

Build and verify a source-installed Python 3.12 command-line vertical slice
that communicates over USB serial with one supported analyzer running
`Firmware/LogicAnalyzer_V2`, reports its identity and capabilities, performs a
normal 8-channel capture using a single-channel rising or falling edge trigger,
exports deterministic CSV and a provisional replay artifact, closes safely,
and successfully performs a second physical capture after closing and reopening
the port.

The result should already be useful for examining an 8-bit data bus or a
selected group of clock, reset, read/write, chip-select, and interrupt signals
on a simple 8-bit single-board computer. It does not claim simultaneous full
address/data/control-bus visibility in Cycle 1.

## Verifiable stopping condition

The Cycle 1 goal is complete only when all of the following are true:

1. The package installs from `Software/LogicAnalyzerPy/` on Python 3.12 and its
   CLI help command succeeds.
2. Static checks and all non-hardware tests pass using the canonical commands
   recorded below.
3. Provenance-tagged fixtures cover V2 identity and the implemented normal
   8-channel rising/falling-edge capture request and response surface.
4. Fake/replay transport tests cover successful operation, fragmented reads,
   malformed input, finite timeouts, disconnects, and cleanup.
5. Given an operator-supplied serial port and known periodic input, the CLI
   reads the expected V2 identity and completes a capture whose sample count,
   width, edge polarity, and approximate measured frequency satisfy the checked-
   in hardware procedure.
6. CSV and replay outputs reload or validate deterministically without object
   pickling or machine-local metadata.
7. The port closes on success and failure paths, and a second physical capture
   succeeds after explicit close/reopen.
8. The final progress record identifies the exact commands, test results,
   hardware/firmware identity, sanitized evidence artifacts, known limitations,
   and remaining deferred work.
9. The existing C# applications and firmware remain available as rollback and
   comparison paths.

Passing only fake tests is not sufficient. If physical hardware is unavailable
or its required inputs are unknown, the goal is not complete.

## Scope boundaries

### Required

- Minimal Python package and CLI scaffold.
- Explicit `--port PATH`; best-effort candidate-port listing.
- V2 identity/version/capability parsing.
- Normal 8-channel capture only.
- One selected rising/falling edge-trigger channel.
- Raw 8-bit sample storage.
- Deterministic CSV export.
- A clearly provisional, versioned `.npz` replay artifact with pickling
  disabled and validated JSON or non-object-array metadata.
- Finite configurable timeouts.
- Disconnected, idle, and capturing states.
- Exception-, disconnect-, and Ctrl-C-safe resource cleanup.
- Close/reopen recovery.
- Fake/replay verification and the physical hardware gate.
- Concise protocol and operator documentation for the implemented slice.

### Explicitly excluded

- PySide6 or any GUI.
- `.lac` compatibility.
- 16- and 24-channel modes.
- TCP or Wi-Fi connectivity.
- Complex, fast, blast, external, or burst capture modes.
- Burst timestamps and graceful in-protocol abort.
- Sigrok decoder hosting.
- Editing, regions, annotations, signal composition, or measurements beyond the
  hardware smoke's frequency check.
- Multi-device capture.
- Bootloader entry, firmware flashing, Wi-Fi configuration, voltage queries,
  blink commands, or other device-management operations.
- Self-contained packaging, signing, notarization, or release publication.
- Removal or material refactoring of the existing C# application or firmware.

Excluded work remains in the technical roadmap. Discovering that it would be
useful is not authority to bring it into Cycle 1.

## Preconditions for starting the durable goal

The following must be settled during document approval or the goal's initial
preflight checkpoint:

- The attached board is a supported V2 analyzer or its exact reported firmware
  identity is available for comparison.
- The operator can provide an explicit serial port path.
- A safe periodic source, expected frequency, sample rate, trigger channel,
  edge polarity, pre-sample count, and post-sample count are supplied or can be
  derived from a checked-in test-signal procedure.
- Analyzer ground and target ground can be connected safely.
- The host user has permission to open the serial device.
- Dependency installation, if needed, can use the normal approval mechanism.

Use placeholders such as `<PORT>` and `<SIGNAL_HZ>` in documentation, never a
machine-specific port or laboratory secret committed to the repository.

## Discovery model

Discovery is bounded investigation needed to settle the next Cycle 1 interface,
not permission to redesign the roadmap.

### Evidence precedence

For the exact attached V2 firmware version:

1. Successful, reproducible bytes observed between the existing C# client and
   the physical board are compatibility evidence of highest priority.
2. Firmware source explains intended layout and behavior.
3. Existing C# source fills gaps and identifies current validation and recovery
   behavior.
4. README prose and historical behavior provide supporting context.

When sources disagree, do not silently choose one. Record the discrepancy,
source provenance, chosen Cycle 1 behavior, and a fixture demonstrating it.

### Discovery outcomes

Each uncertainty must end in one of four states:

- **Resolved locally:** source, trace, or test evidence settles it; proceed.
- **Resolved by bounded experiment:** a non-mutating board read/capture settles
  it; save sanitized evidence and proceed.
- **Deferred:** it does not block the required Cycle 1 path; add it to the
  deferred list and proceed.
- **Authority/input required:** it needs a user choice, unavailable physical
  setup, persistent device mutation, firmware change, or scope expansion; stop
  that path and request direction.

### Scope test for newly discovered work

New work may enter the active batch only if all are true:

1. The current stopping condition cannot be met without it.
2. It stays within the required Cycle 1 surface.
3. It does not cross an authority gate.
4. Its acceptance evidence can be added to the current or immediately following
   batch.

Otherwise defer it explicitly. Do not begin a later-cycle feature merely to
keep an agent occupied.

## Batch boundaries and checkpoints

Cycle 1 is executed through the five batches defined in
`BATCH_EXECUTION.md`:

1. C1-B1: preflight, scaffold, and narrow protocol evidence.
2. C1-B2: models, codec, fake/replay transport, and negative tests.
3. C1-B3: pySerial discovery and physical identity.
4. C1-B4: physical capture, CSV, and provisional replay artifact.
5. C1-B5: lifecycle hardening, independent review, and final hardware proof.

A checkpoint is valid only after its batch acceptance evidence passes and its
record is appended to the progress log. A later batch may not use an unsettled
interface from an earlier batch. Small fixes may be folded backward into the
owning batch, but the affected gate must be rerun.

The orchestrator may parallelize implementation and independent fixture/test
work only when file ownership is disjoint and the interface under test is
settled. At most one integration-changing task should be active for a shared
module.

## Authority gates

### Authorized without additional scope approval

- Read repository files and inspect the existing application and firmware.
- Create and edit implementation, tests, evidence, and working documentation
  under `Software/LogicAnalyzerPy/`.
- Update the technical roadmap only to record factual discoveries or approved
  deferrals without changing this contract.
- Run non-destructive format, type, unit, integration, and replay tests.
- Enumerate serial ports.
- Open the operator-specified analyzer port.
- Send the characterized identity request and required normal 8-channel capture
  request.
- Read capture data, close/reopen the connection, and save sanitized local test
  artifacts inside the project test-data/evidence locations.
- Make minimal fixes needed to pass the current batch and rerun its validation.

### Requires normal execution approval when prompted

- Installing or downloading Python dependencies.
- Accessing hardware or host resources outside the sandbox when the environment
  requires permission.
- Running platform-specific tools that require elevated host access.

Approval to execute a command does not expand Cycle 1 product scope.

### Requires explicit user direction and must pause the affected path

- Flashing or changing firmware.
- Entering the bootloader.
- Changing Wi-Fi/network settings or persistent device state.
- Destructive repository operations or deleting/replacing the C# application.
- Pushing commits, publishing packages/releases, signing, or notarization.
- Adding later-cycle product features.
- Editing `ORCHESTRATION.md` or `BATCH_EXECUTION.md` after approval, except in a
  separately requested document-review step.
- Changing the durable objective or weakening its stopping condition.
- Choosing undocumented electrical connections or voltage levels when safety is
  uncertain.

## Validation loop

Every batch follows the procedure in `BATCH_EXECUTION.md` and repeats this loop:

1. Reproduce or define the failing/missing behavior with a test or evidence
   artifact.
2. Make the smallest in-scope implementation change.
3. Run the focused tests for the changed component.
4. Run the accumulated non-hardware suite.
5. When the batch involves hardware, run its opt-in hardware check.
6. Inspect failures and iterate without weakening assertions or silently
   changing expected behavior.
7. Record commands, outcomes, evidence, decisions, and deferrals.
8. Mark the checkpoint complete only when the batch gate passes.

Canonical non-hardware commands, once the scaffold exists:

```bash
cd Software/LogicAnalyzerPy
python -m ruff check .
python -m mypy src
python -m pytest -m "not hardware"
python -m pico_logic_analyzer --help
```

If the scaffold selects Pyright instead of mypy, the approved decision and
replacement command must be recorded before implementation depends on it.
Agents may add focused commands, but may not replace the accumulated suite with
only focused tests.

The canonical physical command must be created and documented during Cycle 1.
It must accept explicit parameters rather than hard-coded laboratory values. Its
stable interface should be equivalent to:

```bash
pico-la hardware-smoke \
  --port <PORT> \
  --signal-hz <SIGNAL_HZ> \
  --sample-rate <SAMPLE_RATE> \
  --trigger-channel <CHANNEL> \
  --edge rising \
  --pre-samples <PRE> \
  --post-samples <POST>
```

If a pytest-based command is chosen instead, it must expose the same explicit
operator inputs and evidence. The final command is part of the completion proof.

## Progress and evidence

The first batch creates:

`Software/LogicAnalyzerPy/docs/orchestration-progress.md`

Append one compact checkpoint record per batch using the template in
`BATCH_EXECUTION.md`. Each record must name the checkpoint, changed files,
verification commands/results, hardware evidence where applicable, remaining
work, deferrals, and whether the run is blocked.

Machine-specific serial paths, credentials, and sensitive target details must
not be committed. Hardware artifacts should be deterministic and sanitized;
large or unstable captures should be summarized rather than committed.

## Failure, retry, and blocking policy

- A normal test failure causes diagnosis and another bounded iteration in the
  same batch.
- A regression in a previously completed checkpoint reopens that checkpoint.
- Three repetitions of the same external blocker without a new safe avenue are
  sufficient to report the durable goal blocked according to the goal system's
  rules; difficulty or incomplete work alone is not a blocker.
- Missing user input, unavailable hardware, unsafe electrical uncertainty, or a
  required scope/authority expansion must be reported precisely. Continue other
  independent in-scope work when it remains meaningful.
- Do not claim completion, substitute fake hardware evidence, or weaken the
  stopping condition because the board is unavailable.

## Completion proof and handoff

At Cycle 1 completion, produce a final summary that includes:

- exact stopping-condition checklist with pass evidence;
- canonical validation and hardware commands with results;
- detected analyzer/firmware identity;
- description and location of committed fixtures and sanitized artifacts;
- demonstrated CSV and replay outputs;
- confirmation of clean close and successful second capture;
- known limitations and deferred-cycle links;
- confirmation that rollback through the existing C# application remains;
- repository status and any uncommitted or unrelated changes.

The durable goal must stop at this point. Starting Cycle 2 requires a new review
of scope, batches, authority, validation, and stopping condition, followed by a
new or updated approved goal.

## Approval checklist before `/goal`

- [ ] The durable objective and Cycle 1 boundary are approved.
- [ ] The physical board/firmware assumption is correct.
- [ ] The operator can provide `<PORT>` and signal parameters safely.
- [ ] The validation loop and physical acceptance evidence are approved.
- [ ] The authority gates are approved.
- [ ] `BATCH_EXECUTION.md` has been reviewed and approved.
- [ ] All three final domain reviews in `docs/rewrite-reviews/final/` say
      `pass` for the same reviewed commit.
- [ ] The technical plan remains the referenced roadmap.
- [ ] No unresolved contradiction exists among the three documents.

Only after this checklist is approved should a durable goal be created.
