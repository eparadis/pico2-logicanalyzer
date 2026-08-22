# Cycle 2 Durable Goal

## Status

This file is the proposed execution prompt for Cycle 2. It does not start the
goal and must not be modified during goal execution.

Because it defines agent ownership and review flow, it must receive the same
three-reviewer common-commit approval required by the Cycle 2 orchestration
contracts before the `/goal` command at the end of this file is used.

## Objective and stopping condition

Execute and verify Cycle 2 of the Python logic-analyzer rewrite. Continue across
turns until all fourteen stopping conditions in `CYCLE2_ORCHESTRATION.md` have
recorded evidence against one final candidate, or until the documented blocked
condition is genuinely reached. Do not begin Cycle 3.

## Authority and required reading

Read these sources in order before implementation:

1. `AGENTS.md` and every included instruction.
2. This file in full.
3. `CYCLE2_ORCHESTRATION.md` in full.
4. `CYCLE2_BATCH_EXECUTION.md` in full.
5. `Software/LogicAnalyzerPy/docs/cycle-2-discovery-review.md`.
6. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` as roadmap
   context only.
7. `Software/LogicAnalyzerPy/docs/cycle-1-completion.md` and the accepted Cycle
   1 evidence as regression baselines.
8. `docs/rewrite-reviews/cycle-2/README.md`,
   `docs/rewrite-reviews/cycle-2/ARCHITECTURAL_DOMAINS.md`, and the three passing
   records under `docs/rewrite-reviews/cycle-2/final-round-2/`.

`CYCLE2_ORCHESTRATION.md` and `CYCLE2_BATCH_EXECUTION.md` remain the governing
product, authority, validation, evidence, and checkpoint contracts. This file
only specifies how the orchestration agent delegates them. If it conflicts with
either governing contract, stop and request direction rather than silently
choosing or editing a contract.

Confirm that the repository contains approved contract commit
`7a5f429db93c2164ef54334c0eb3adf48ae68ff0`, tree
`eb52d5e8f16efd855b09b7672b532403c8454c19`, and three final-round-2 `pass`
records for that exact commit. Record initial repository status and preserve
unrelated user changes.

Do not modify this file or either approved governing contract during the goal.

## Execution configuration

Run the primary orchestration agent as:

- Model: `gpt-5.6-sol`
- Reasoning effort: `low`

Create one fixed three-agent pool and reuse it throughout C2-B1 through C2-B6:

| Lane | Model | Reasoning | Responsibility |
| --- | --- | --- | --- |
| Implementor | `gpt-5.6-terra` | `low` | Product changes and focused implementation tests |
| Verifier | `gpt-5.6-sol` | `low` | Independent black-box, boundary, security, protocol, and hardware verification |
| Acceptance | `gpt-5.6-sol` | `low` | Independent integrated-candidate, evidence, scope, and checkpoint acceptance |

Reuse each agent only within its original lane. Never convert an implementor to
a review role, never convert a verifier or acceptance agent to implementation,
and never combine verification and acceptance. If replacement is necessary,
create a new agent with the same lane, model, and reasoning effort and record the
identity change. Do not reuse a preparatory agent whose earlier role, model, or
reasoning configuration does not match the required lane.

Subagents must not create further subagents. The primary orchestrator owns the
three available worker slots and keeps the work sequential except where the
governing batch procedure explicitly permits disjoint parallel work.

When first creating a worker, provide a self-contained assignment rather than a
full conversation fork. Include the active batch, authoritative files, exact
candidate commit/tree, owned and prohibited paths, required commands/evidence,
authority boundaries, and handoff schema. Reuse that worker with follow-up tasks
for later iterations and batches so it retains relevant repository context.

## Context-preserving delegation

The primary orchestrator coordinates and validates the process but does not
perform a second code or evidence review of agent work.

The orchestrator must not:

- read implementation source or diffs to judge correctness;
- inspect detailed test logs when a compact result is available;
- review the contents of verifier or acceptance records; or
- independently reinterpret or summarize detailed reviewer findings.

Workers write code, tests, fixtures, and durable review records directly to
their owned paths. Their conversational handoff to the orchestrator is limited
to:

- lane and stable identity;
- candidate commit and tree;
- changed or reviewed paths;
- commands with concise result counts and exit status;
- evidence and review-record paths plus digests;
- verdict exactly `pass` or `changes_required` for review lanes;
- open finding identifiers; and
- blockers or required operator input.

Do not paste source, diffs, long logs, fixture bodies, or detailed findings into
the orchestrator conversation. Preserve full detail in repository artifacts.
The acceptance agent receives and may read the durable evidence and exact gate
results for the candidate it audits; compact conversational handoffs limit the
orchestrator's context, not the acceptance lane's required audit inputs.

The orchestrator may inspect repository status, changed-path lists, commit/tree
identity, concise command results, manifest-schema validation, checkpoint state,
and stopping-condition coverage. It may stage and commit reviewed paths without
performing its own content review. It owns shared-interface decisions only when
the approved contracts already settle them. For an unsettled substantive
decision, request a compact recommendation and alternatives from the appropriate
review lane, then request operator direction when the governing contracts do not
choose.

When a review lane reports `changes_required`, direct the implementor to read the
durable review record itself. The orchestrator does not relay its contents.

## Per-batch loop

Execute C2-B1 through C2-B6 in order using the complete procedure and gates in
`CYCLE2_BATCH_EXECUTION.md`:

1. Record the active-batch progress entry, prerequisites, ownership, repository
   state, and authority inputs.
2. Give the implementor the bounded batch assignment. The implementor changes
   only owned product/test paths and runs focused checks.
3. Only after the focused checks pass, record an immutable implementation
   candidate commit without independently reviewing its contents. A focused
   failure remains with the implementor; after correction and passing focused
   checks, record a new candidate that starts again at independent verification.
4. Give the verifier that exact candidate. The verifier writes an immutable
   review record and returns only its compact verdict.
5. If verification requires changes, return the durable record to the same
   implementor. The implementor corrects the work and reruns focused checks;
   record a new immutable candidate and reuse the same verifier. Repeat until
   that exact candidate passes independent verification.
6. Run every accumulated validation gate required by the active batch against
   that exact verified candidate and record the exact durable results plus a
   concise handoff. Delegate diagnosis of failures to the owning worker rather
   than loading detailed logs into orchestrator context.
7. Only after the exact candidate passes independent verification and the
   complete required accumulated validation, give that candidate, its verifier
   record, and its exact accumulated-gate results to the acceptance agent. The
   acceptance agent audits that same candidate and complete batch gate, writes
   an immutable review record, and returns only its compact verdict.
8. Any focused or accumulated validation failure, and every implementation
   correction made in response, requires a new immutable candidate. The new
   candidate must repeat independent verification and the complete accumulated
   validation before it can be submitted to acceptance. If acceptance requires
   changes, return its durable record to the same implementor; after correction
   and focused checks, record a new candidate and require that candidate to pass
   the same verifier and the complete accumulated validation before reusing the
   same acceptance agent. No earlier pass transfers to a corrected candidate.
9. After implementation, verification, accumulated-validation, and acceptance
   evidence exists for the same candidate, create
   only the owning batch's evidence manifest atomically. Validate and commit it
   before appending the checkpoint record.
10. Advance only after the complete checkpoint passes. Reopen the earliest owning
   checkpoint when a regression is found.

Never precreate future manifests, weaken assertions, replace physical evidence
with fake evidence, accept skipped stopping conditions, or let one lane approve
its own work.

## Validation and authority

Use the exact Python, Node, browser, API, CI, evidence-schema, physical, and
performance commands established by the governing contracts and C2-B1. Run
focused checks after each change and accumulated non-hardware validation after
each integration. Clean bootstraps, hosted macOS/Linux CI, native macOS browser
work, physical captures, and performance thresholds remain mandatory in their
owning batches.

Use the normal approval mechanism when dependency downloads, USB access, native
browser launch, or pushing an exact candidate for hosted CI requires it.
Execution approval does not expand product scope.

Do not modify or flash firmware, enter the bootloader, change Wi-Fi or persistent
device state, install or run .NET, implement `.lac`, expose a public server, add
Qt or Electron, package or publish a release, implement decoders/editing, or
begin Cycle 3.

## Hardware checkpoints

Treat accepted Cycle 1 hardware facts as historical inputs, not permission to
guess the current setup. Before C2-B3, request fresh operator confirmation of:

- the explicit serial port;
- Pico 2 and fixed checked-in V2 firmware identity;
- integrated LogicAnalyzerV2 protection, 3.3 V VRef, and common ground;
- D0, D8, D16, and D23 labels, mapping, and input direction;
- safe fan-out of the approximately 1 kHz 3.3 V source to those four inputs; and
- a fixed-level, non-floating idle input for the Cycle 1 recovery regression.

Do not perform physical capture until every required item is confirmed. Sanitize
the serial port as `<PORT_SUPPLIED>` and capability-bearing values as
`<TOKEN_REDACTED>` in committed evidence.

At C2-B5, present the evidence-based rendering-threshold proposal to the
operator. Do not accept C2-B5 until the threshold record is explicitly approved.

## Progress, blocking, and completion

Keep the compact Cycle 2 progress log required by the governing documents. User
updates state only the active checkpoint, concise verified result, remaining
work, and whether operator input or authority is needed.

Continue safe independent work when one path awaits input. Mark the durable goal
blocked only under the repeated-external-blocker rule in
`CYCLE2_ORCHESTRATION.md`; incomplete, difficult, slow, or failed work is not by
itself a blocker.

Stop successfully only when all fourteen stopping conditions have immutable,
validated evidence against one final candidate and final independent acceptance
is `pass`. Produce `Software/LogicAnalyzerPy/docs/cycle-2-completion.md` and the
handoff required by `CYCLE2_ORCHESTRATION.md`, including exact commit/tree,
dependency/build digests, commands/results, CI identity, sanitized hardware and
browser evidence, checkpoint manifests, performance thresholds/results,
limitations, deferrals, repository status, the macOS-native/Linux-CI support
qualification, and confirmation that no prohibited action occurred.

## Launch command

```text
/goal Execute and verify Cycle 2 of the Python logic-analyzer rewrite by following CYCLE2_GOAL.md exactly. Continue until all fourteen stopping conditions in CYCLE2_ORCHESTRATION.md have recorded proof or the documented blocked condition is genuinely reached. Do not modify CYCLE2_GOAL.md or the approved governing contracts. Do not begin Cycle 3.
```
