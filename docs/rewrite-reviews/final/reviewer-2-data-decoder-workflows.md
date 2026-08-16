# Final Review: Capture Data, Decoder, and User-Workflow Boundary

- Reviewer: `/root/review_data_workflows` — Reviewer 2, Capture Data,
  Decoder, and User-Workflow Boundary
- Reviewed commit: `de93d47dabb64cfc0e014ce9eed807877b9f5b69`
- UTC timestamp: `2026-08-16T17:15:34Z`
- Verdict: `changes_required`

## Scope

This is the mandatory final re-review under the Reviewer 2 charter in
`docs/rewrite-reviews/ARCHITECTURAL_DOMAINS.md`. It reviews only the exact commit
above, including all three process documents and the recorded Round 1
dispositions. It verifies the six prior capture-data/decoder/workflow findings
and checks the resolutions for newly introduced ambiguity. Wire protocol,
transport lifecycle, CI/platform delivery, and orchestration governance remain
delegated except where their outputs cross the capture-data boundary.

## Findings and disposition

### 1. Prior Finding 1 — capture model/export semantics: not fully resolved

- Severity: high
- Evidence:
  - The resolution correctly fixes raw storage to a one-dimensional contiguous
    `uint8` array, captures exactly D0–D7, separates bit/request position from
    channel identity/display metadata, and defines required replay/CSV fields at
    `BATCH_EXECUTION.md:199-251`.
  - It defines indices `0..pre_trigger_samples-1` as pre-trigger, places the
    trigger marker on index `pre_trigger_samples-1`, begins post-trigger data at
    index `pre_trigger_samples`, and calculates time from the marker index at
    `BATCH_EXECUTION.md:211-215`. Consequently the first post-trigger sample is
    assigned `+1/sample_rate_hz`, while the last pre-trigger sample is assigned
    time zero and the CSV `trigger=1` flag (`:223-228`).
  - The existing viewer draws its trigger boundary at `PreSamples`, not at
    `PreSamples - 1`
    (`Software/LogicAnalyzer/LogicAnalyzer/Controls/SampleViewer.axaml.cs:290-291`).
    The revised convention is therefore an unrecorded behavior change and is
    internally at odds with calling index `pre_trigger_samples-1` part of the
    pre-trigger region.
  - The model also describes sample counts, trigger channel, device identity,
    and capabilities collectively as “required positive/validated metadata” at
    `BATCH_EXECUTION.md:208-210`, although trigger channel D0 is explicitly legal
    at `:216-217`. Implementers could reasonably reject zero.
- Requested resolution: Represent the trigger as the boundary at
  `pre_trigger_samples` and define whether time belongs to sample instants or
  interval boundaries. Recommended: set `trigger_index=pre_trigger_samples`,
  define the first post-trigger sample as time zero, the last pre-trigger sample
  as `-1/sample_rate_hz`, and either rename the CSV column to
  `trigger_boundary` with an explicit row convention or state precisely that its
  `1` marks the first post-trigger sample. If hardware traces establish a
  different ordering, record that evidence and the intentional compatibility
  change instead. Replace “positive/validated” with field-specific invariants:
  rates/counts as their protocol limits require, channel IDs in `0..7`,
  `requested_count = pre_trigger_samples + post_trigger_samples`, and all counts
  consistent with the array. Add boundary tests for D0 and the samples on both
  sides of the trigger.
- Disposition: open — the raw/channel portion is resolved, but the settled
  trigger/time contract is inconsistent and must be corrected before C1-B1
  copies it into an ADR.

### 2. Prior Finding 2 — automation-safe CLI contract: resolved

- Severity: none
- Evidence: `BATCH_EXECUTION.md:253-277` now defines complete Cycle 1 command
  forms, explicit output paths, exit codes, stdout/stderr separation, JSON
  behavior, collision/`--force` rules, temporary validation, and two-output
  rollback. C1-B3 and C1-B4 require subprocess coverage at `:408-419` and
  `:443-465`.
- Disposition: resolved — no open CLI-contract issue remains for Cycle 1.

### 3. Prior Finding 3 — bounded NPZ replay loading: resolved

- Severity: none
- Evidence: `BATCH_EXECUTION.md:233-251` fixes the two-member schema, inert
  metadata, exact ranks/dtypes, supported version and count consistency, and
  numeric archive/member/metadata/sample limits before materialization. It
  rejects encryption, duplicates, unexpected/path-bearing members, unsupported
  compression, unsafe dtypes, and unknown top-level keys. C1-B2 and C1-B4
  explicitly require hostile-container tests at `:367-398` and `:460-465`.
- Disposition: resolved — `allow_pickle=False` is retained as one layer rather
  than treated as the complete security policy.

### 4. Prior Finding 4 — broad Phase 3 gate versus Cycle 1: resolved

- Severity: none
- Evidence: The roadmap adds a narrow Cycle 1 transport/CLI gate at
  `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:577-586` and
  explicitly states that TCP, broader abort/reconnect, `.lac`, and broader JSON
  requirements belong to the non-blocking later parity gate at `:588-598`.
- Disposition: resolved — the Cycle 1 batch gates can be followed without
  implementing deferred transport/file features.

### 5. Prior Finding 5 — focused decoder milestone versus broad parity: resolved

- Severity: none
- Evidence: The focused gate at
  `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:650-667` limits
  Cycle 3 to pinned I2C/SPI/UART versions and fixture-enumerated API-v3 behavior,
  with headless library/CLI execution, deterministic mappings/options,
  samplerate metadata, annotations, cancellation, and exception isolation. It
  explicitly excludes stacking, user discovery, capture-selected code, and the
  all-decoder promise. Those features are labeled later parity at `:669-678`.
- Disposition: resolved — no decoder breadth or trust requirement has leaked
  into Cycle 1 or focused Cycle 3.

### 6. Prior Finding 6 — performance-baseline sequencing: resolved

- Severity: none
- Evidence: The revised schedule assigns raw parsing/extraction/CSV/NPZ to
  Cycle 1/Phase 2, `.lac`, decoder, multi-device, and viewer measurements to the
  cycles that first implement those subsystems, and explicitly includes empty,
  constant, dense-transition, and maximum viewer workloads
  (`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:922-936`).
- Disposition: resolved — future UI/decoder/multi-device code is no longer a
  Phase 2 prerequisite, and the visible-transition rendering direction remains
  viable.

### 7. New finding — the roadmap still promises legacy CSV behavior that conflicts with the settled Cycle 1 CSV

- Severity: medium
- Evidence:
  - The settled Cycle 1 CSV header is exactly
    `sample_index,time_seconds,trigger,D0,D1,D2,D3,D4,D5,D6,D7` at
    `BATCH_EXECUTION.md:219-228`.
  - Existing CSV writers emit only selected channel-name headers and bit rows
    (`Software/LogicAnalyzer/TerminalCapture/Classes/FileOperations.cs:57-79` and
    `Software/LogicAnalyzer/CLCapture/Program.cs:223-244`).
  - P2-C still requires a “CSV writer compatible with current header/sample
    behavior” at
    `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:486-497`,
    without saying whether that means a second legacy mode, import compatibility,
    or replacing the new self-timed contract. The same roadmap requires
    intentional behavior changes to be recorded at `:900-907`.
- Requested resolution: Make the roadmap name the settled self-timed Cycle 1 CSV
  as the default writer contract and record its difference from the C# export in
  `docs/compatibility.md` during C1-B1/B4. If legacy CSV interoperability is
  required later, define it as an explicitly named import/export compatibility
  mode with fixtures; do not let “compatible” alter the fixed Cycle 1 header.
- Disposition: open — the process documents currently give two incompatible CSV
  writer requirements.

## Final status

Five prior findings are resolved. Prior Finding 1 remains partially open, and
one new cross-document CSV contradiction remains open. A final `pass` is not
appropriate until both are corrected and all three reviewers re-review the same
new commit.
