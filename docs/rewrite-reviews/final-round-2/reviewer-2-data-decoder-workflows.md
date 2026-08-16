# Final Round 2 Review: Capture Data, Decoder, and User-Workflow Boundary

- Reviewer: `/root/review_data_workflows` — Reviewer 2, Capture Data,
  Decoder, and User-Workflow Boundary
- Reviewed commit: `134a4b69d1a6d0f81bb0fab37d355254d2b440ba`
- UTC timestamp: `2026-08-16T17:21:33Z`
- Verdict: `pass`

## Scope

This mandatory common-commit re-review applies the Reviewer 2 charter in
`docs/rewrite-reviews/ARCHITECTURAL_DOMAINS.md` to the exact immutable commit
above. It inspected all three process documents, the Round 1 record and
dispositions, the preserved attempted-final record, and the current
capture/file/CLI/GUI/decoder sources referenced by those reviews. It specifically
rechecked trigger index and time-zero semantics, D0 validation, self-timed versus
legacy CSV behavior, and the recovery-smoke additions where they cross the
automation/data boundary. Working-tree changes were not considered.

## Findings and disposition

### 1. Round 1 Finding 1 and attempted-final Finding 1 — capture model, channel identity, trigger origin, and export semantics

- Status: resolved
- Evidence:
  - `BATCH_EXECUTION.md:205-213` fixes a one-dimensional C-contiguous `uint8`
    raw-word array, exactly D0–D7 in ascending request order, raw-bit/request-list
    mapping, and separate logical/physical/display metadata.
  - Field-specific validation now makes `trigger_channel` an integer in `0..7`,
    so D0 is unambiguously legal, while rates and counts use their own protocol
    limits (`BATCH_EXECUTION.md:214-228`).
  - `requested_count = pre_trigger_samples + post_trigger_samples`, actual count
    and array length must match, and `trigger_index = pre_trigger_samples`
    (`BATCH_EXECUTION.md:219-226`). The first post-trigger sample is time zero and
    the preceding sample is `-1/sample_rate_hz`, matching the current viewer's
    trigger boundary at `PreSamples`
    (`Software/LogicAnalyzer/LogicAnalyzer/Controls/SampleViewer.axaml.cs:290-291`).
  - The CSV `trigger` flag is explicitly attached to that first post-trigger,
    time-zero sample (`BATCH_EXECUTION.md:230-242`). C1-B1, C1-B2, and C1-B4 now
    require D0 and both sides of the trigger boundary as examples/tests at
    `BATCH_EXECUTION.md:371-388,397-430,492-500`.
- Disposition: accepted/no change — the core, CLI, replay, CSV, and future viewer
  now share one coherent channel and sample-time interpretation.

### 2. Round 1 Finding 2 — automation-safe CLI contract

- Status: resolved
- Evidence: The settled CLI retains explicit capture inputs and output paths,
  deterministic exit codes, stdout/stderr separation, JSON testing,
  collision/`--force` behavior, and transactional CSV/replay publication at
  `BATCH_EXECUTION.md:264-299`. The new smoke commands are evaluated separately
  in Finding 9 below.
- Disposition: accepted/no change — Cycle 1 remains directly scriptable without
  inheriting the current C# CLI's exit/output defects.

### 3. Round 1 Finding 3 — bounded NPZ replay loading

- Status: resolved
- Evidence: `BATCH_EXECUTION.md:244-262` retains the exact two-member schema,
  inert metadata, numeric archive/member/sample limits, pre-materialization ZIP
  checks, exact safe ranks/dtypes, `allow_pickle=False`, supported-major and
  count validation, and rejection of unexpected keys/members. Hostile-container
  tests remain required in C1-B2 and C1-B4.
- Disposition: accepted/no change — replay files cannot silently nominate
  decoder code or bypass the bounded typed loader contract.

### 4. Round 1 Finding 4 — broad Phase 3 gate versus Cycle 1 deferrals

- Status: resolved
- Evidence: The narrow Cycle 1 transport/CLI gate remains separate from the
  non-blocking later parity gate at
  `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:585-606`.
- Disposition: accepted/no change — TCP, public abort, `.lac`, and broader JSON
  work do not enter Cycle 1.

### 5. Round 1 Finding 5 — focused decoder milestone versus broad parity

- Status: resolved
- Evidence: The focused I2C/SPI/UART fixture-driven gate remains separate from
  stacking, user discovery, capture-selected code, and all-decoder import parity
  at `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:658-686`.
- Disposition: accepted/no change — decoder complexity and executable-code trust
  remain explicitly deferred without foreclosing the native Python host.

### 6. Round 1 Finding 6 — performance-baseline sequencing

- Status: resolved
- Evidence: Capture/format, `.lac`, focused decoder, multi-device, and viewer
  workloads remain assigned to the cycles where their subsystems first exist at
  `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:930-944`.
- Disposition: accepted/no change — no future GUI/decoder/multi-device benchmark
  blocks the first hardware-capable CLI.

### 7. Attempted-final Finding 1 remainder — trigger-index/time-zero and D0 invariants

- Status: resolved
- Evidence: The field-specific and sample-boundary corrections at
  `BATCH_EXECUTION.md:214-228` implement the requested convention exactly, and
  the required boundary evidence at `:385-387,413-414,496-498` prevents
  regression.
- Disposition: accepted/no change — no open remainder from the prior finding.

### 8. Attempted-final Finding 7 — self-timed versus legacy CSV contradiction

- Status: resolved
- Evidence:
  - P2-C now names the settled self-timed CSV as the default writer contract and
    requires its difference from the C# channel-only format to be recorded in
    `docs/compatibility.md`
    (`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md:490-507`).
  - Any future legacy CSV support must be an explicitly named compatibility mode
    with dedicated fixtures and cannot change the Cycle 1 header. C1-B1 owns the
    compatibility record and C1-B4 verifies it
    (`BATCH_EXECUTION.md:341-346,492-500`).
- Disposition: accepted/no change — there is one Cycle 1 default CSV schema and
  a clear later path for legacy interoperability.

### 9. New recovery-smoke CLI and evidence contract

- Status: accepted
- Evidence:
  - `hardware-smoke` and the non-interactive `hardware-recovery-smoke` expose
    explicit port, signal, capture, cancellation-delay, and evidence-path inputs
    at `BATCH_EXECUTION.md:264-280` and `ORCHESTRATION.md:306-342`.
  - The recovery path is bounded to a fixed-level idle channel, exactly one
    characterized `0xFF`, drain/close/reopen/re-identification, and a following
    known-periodic-signal capture. It uses the same deterministic exit taxonomy
    and atomically writes the sanitized evidence manifest
    (`BATCH_EXECUTION.md:283-299,507-528`).
  - Evidence retains command/status, provenance, non-sensitive capture
    parameters, and sanitized hardware identity while replacing the actual port
    with `<PORT_SUPPLIED>` (`ORCHESTRATION.md:344-378`).
- Disposition: accepted/no change — the new command makes failure recovery
  repeatable and machine-verifiable without adding a public decoder/file schema
  or a general abort workflow. No stdout/stderr, exit-code, or capture-data
  ambiguity was introduced.

## Final status

All prior Reviewer 2 findings are resolved. The common-commit corrections
introduce no new open capture-data, persistence, decoder, CLI/GUI, or rendering
finding. The reviewed commit satisfies the Reviewer 2 domain contract.
