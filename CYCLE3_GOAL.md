# Cycle 3 Durable Goal

## Status

This file is the proposed execution prompt for Cycle 3. It does not start the
goal, authorize implementation, execute a decoder, or permit a dependency or
environment change. Do not modify it during goal execution.

The exact governing contract is commit
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. Its three
`contract-final-round-5` passes are committed in
`0d3755a2798cdfafd2a89ebaedcac40acc8c356a` at:

- `docs/rewrite-reviews/cycle-3/contract-final-round-5/reviewer-1-decoder-api-runtime-fixtures.md`;
- `docs/rewrite-reviews/cycle-3/contract-final-round-5/reviewer-2-capture-annotation-cli-workflows.md`; and
- `docs/rewrite-reviews/cycle-3/contract-final-round-5/reviewer-3-security-delivery-orchestration.md`.

This goal must itself receive the separate three-reviewer common-commit
approval required by Step 9 of `CYCLE3_PREPARATION.md` before the `/goal`
command at the end of this file is used.

## Objective and authority

Execute and verify the bounded native UART, SPI, and I2C compatibility-host
Cycle 3 defined by the approved contract. Continue across turns through C3-B1
to C3-B5 until the directed terminal completion seal exists and all eighteen
stopping conditions have immutable proof for the required exact candidates, or
until the governing blocked condition is genuinely reached. Do not begin later
parity work or Cycle 4.

Read these sources in order before implementation:

1. `AGENTS.md`, every included instruction, and the subagent approval policy.
2. This file in full, including its approved goal-review records.
3. `CYCLE3_ORCHESTRATION.md` in full.
4. `CYCLE3_BATCH_EXECUTION.md` in full.
5. `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` in full.
6. `CYCLE3_PREPARATION.md` and
   `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` as
   preparation and roadmap context only.
7. The accepted Cycle 1 and Cycle 2 completion records, manifests, fixtures,
   contracts, and tests as regression baselines.
8. `docs/rewrite-reviews/cycle-3/README.md`,
   `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`, and the three
   `contract-final-round-5` records named above.

`CYCLE3_ORCHESTRATION.md` and `CYCLE3_BATCH_EXECUTION.md` at the approved
contract commit remain authoritative for objective, scope, product contracts,
security, proof, ordering, checkpoints, blocking, and completion. This file
delegates those contracts; it does not restate or relax them. If this file is
incomplete or conflicts with an approved governing source, follow the authority
order in `CYCLE3_ORCHESTRATION.md`, record the conflict, and stop affected work
for common-commit correction and review. Never settle a conflict through code,
fixture output, or conversational interpretation.

At launch, confirm the exact contract commit/tree, approval-record commit and
paths above, the separately approved goal commit/tree and three common-commit
goal passes, and the completed Step 10 preflight. Record full HEAD, tree,
branch, worktree qualification, and all unrelated user changes. Do not modify
this file or the approved governing contracts during execution.

## Execution configuration and role separation

Run the primary orchestration agent as:

- Model: `gpt-5.6-sol`
- Reasoning effort: `low`

Use these fixed worker-lane profiles throughout Cycle 3:

| Lane | Model | Reasoning | Responsibility |
| --- | --- | --- | --- |
| Implementor | `gpt-5.6-terra` | `low` | Bounded implementation, fixtures, methods, or focused checks within assigned ownership |
| Verifier | `gpt-5.6-sol` | `low` | Independent exact-candidate verification and immutable verdict |
| Acceptance | `gpt-5.6-sol` | `low` | Independent accumulated-evidence, scope, authority, and readiness acceptance |
| Manifest verifier | `gpt-5.6-sol` | `low` | Post-acceptance digest recomputation, schema validation, and immutable manifest verdict |
| Completion-closure auditor | `gpt-5.6-sol` | `low` | Independent audit of the already committed B5 manifest and manifest-verifier record, closure-pending checkpoint, and immutable completion-proof candidate; immutable closure verdict only |

The primary orchestrator is separate from all five evidence lanes and remains
the only approval broker. Workers do not spawn subagents. Keep one coordination
slot for the orchestrator and run no more than three workers concurrently;
role-separated work may be sequential. Reuse an identity only within its
original role and only where the contracts permit its prior authorship. A
replacement uses the same lane profile and is recorded as a new identity.

The completion-closure auditor is a fresh identity distinct from the primary
orchestrator; every author or assembler of an audit-input artifact; and the B5
verifier, acceptance identity, and manifest verifier. It may not be reused from
any role that authored, assembled, verified, accepted, manifest-verified,
approved, or repaired an audit input. It audits
only the already committed inputs named in its lane responsibility, cannot edit
or repair any input, and issues only its immutable `pass` or
`changes_required` verdict. Its work is scheduled within the same maximum of
three concurrent workers; it does not create an additional concurrency slot.

B1 uses a semantic-fixture implementor and a different pre-execution-runner
implementor. Each internal candidate also uses its own verifier and acceptance
identities, distinct from both implementors and the other internal candidate's
reviewers. The fixture identity never authors runner, method, launch/import,
cap-enforcement, cleanup, or probe content. The runner identity never authors
authoritative expected fixtures. An author of B1 expected output cannot later
implement B2-B4 product behavior. The final B1 and all progress, handoff,
manifest, and checkpoint records preserve the complete identity map. No role
conversion or transferred pass is allowed.

## Bounded, context-preserving assignments

Before each assignment, the orchestrator records the active batch entry and
performs the repository, prerequisite, authority, capability, dependency,
execution, and path-ownership preflights required by the contracts. Every
assignment is self-contained and names the full governing commit/tree, exact
candidate or starting identity, one bounded outcome, earliest-owned R items and
stopping conditions, prerequisite checkpoint, editable and prohibited paths,
authoritative inputs, focused and accumulated checks, evidence path, allowed
command shapes, exclusions, and the standard handoff schema.

Use a context-preserving follow-up with the same stable identity for corrections
within one permitted role. Give a fresh identity a complete bounded assignment,
not an unexplained conversation fork. Workers write full findings and evidence
to their owned durable records and return a compact handoff with identity,
candidate, paths, commands/results, artifacts/digests, findings, verdict, and
any root-routed approval need. The orchestrator preserves unrelated user work,
integrates only reviewed ownership, and never edits another identity's record.

Parallel work is allowed only for disjoint paths behind settled interfaces.
Keep one integration-changing owner for each shared model, allowlist, IPC
schema, package/lock/workflow, generated fixture, evidence schema, or generated
asset. An unplanned interface, path, capability, or substantive decision returns
to the orchestrator before editing or execution.

## Exact batch loop

Execute C3-B1 through C3-B5 in order, including all B1 internal gates, using the
complete procedure in `CYCLE3_BATCH_EXECUTION.md`:

1. Select the earliest ready batch; record its bounded progress entry,
   prerequisites, authority, identities, ownership, and repository state.
2. Assign the smallest owning change. The implementor begins with the focused
   failing check, changes only assigned paths, runs authorized focused checks,
   and provides the required handoff.
3. The orchestrator integrates the bounded work, reruns focused checks, and
   commits one immutable candidate with full commit/tree identity.
4. A separate verifier reviews that exact candidate and commits an immutable
   verdict exactly `pass` or `changes_required`.
5. Only after verification passes, the orchestrator runs the complete
   accumulated gate against that same candidate, including inherited gates and
   all required dependency/runtime/process, fixture, bootstrap, CI, resource,
   performance, and evidence checks.
6. Only after the accumulated gate passes, a separate acceptance identity
   audits that exact candidate and complete evidence and commits a verdict
   exactly `pass` or `changes_required`.
7. Only after verification, accumulated validation, and acceptance all pass,
   the orchestrator atomically creates only the active batch manifest. It may
   name the assigned manifest verifier but contains no future verdict, verifier
   record identity/path, or self-dependent digest. The distinct manifest
   verifier recomputes all digests, validates the unchanged manifest and schema,
   and creates the immutable record that owns its manifest digest, commands,
   findings, and verdict. A pass permits the orchestrator to commit the
   unchanged manifest and verifier record together.
8. Only after that commit does the orchestrator append and commit the batch
   checkpoint. The next batch consumes the committed checkpoint.

For B5, step 6 is pre-manifest acceptance of B1-B4 committed evidence, the exact
B5 candidate, and proposed-manifest readiness only. After it passes, follow the
directed terminal chain exactly: commit the B5 manifest and manifest-verifier
record together; commit the B5 checkpoint as `Complete; Cycle 3 closure
pending`; commit the immutable `cycle-3-completion.md` proof candidate naming
that checkpoint and no future closure artifact; have the fixed, independent
completion-closure auditor inspect the already committed B5 manifest and
manifest-verifier record, closure-pending checkpoint, and immutable completion-
proof candidate without editing or repairing them; obtain and commit that
auditor's immutable verdict; then, only after `pass`, the primary orchestrator
commits `cycle-3-completion-seal.md` last. The seal is not an audit input.

Every correction to product, fixture, expected value, method, dependency,
workflow, environment class, runner, launch/import configuration, cap
plumbing, limit, test, evidence-affecting input, manifest, or completion proof
creates a new immutable candidate at its earliest owning gate. Preserve failed
records. No verification, accumulated-validation, acceptance, manifest, CI,
operator, or closure pass transfers to a corrected or different commit/tree.
Reopen every dependent gate required by the contracts.

## Authority and safety gates

Before each implementation or validation phase, apply the approval-broker
policy. Only the root orchestrator may request missing narrowly scoped external
authority. An approval permits the command capability, not additional product
scope or weaker evidence.

Enforce every approved gate, especially:

- C# and upstream material are inert text for static inspection only. Never
  restore, build, install, import, load, execute, or use C# as evidence.
- C#, .NET, pythonnet, libsigrokdecode, `sigrok-cli`, and external/reference
  decoder hosts are forbidden dependencies and executables in every product
  and non-product path, including development, tests, fixtures,
  characterization, verification, performance, acceptance, CI, bootstrap,
  locks, distribution, imports, commands, active processes, and evidence.
- No decoder executes before the goal is invoked. In B1, independently derived
  semantic fixtures and finite experiment-cap specification pass their exact
  internal gates first. The separate immutable runner candidate then proves
  every cap, import/digest boundary, termination, close, and reap path using
  only inert/hostile non-decoder probes. Only that unchanged accepted runner may
  execute the three exact hash-pinned checked-in snapshots. Never use runtime
  output to generate, correct, corroborate, or accept expected fixtures.
- Raw characterization and independent reproduction precede a committed
  numeric-limit proposal; independent verification, accumulated validation,
  and acceptance precede explicit operator approval. An amendment repeats
  those gates. Never weaken a cap or threshold to obtain passing data.
- Project/legal review must reconcile decoder packaging, provenance, notices,
  and package metadata before editable installation exposes snapshots. It does
  not authorize publication; no wheel, sdist, or distribution is in scope.
- macOS with Python 3.12 is the only supported acceptance platform. Required
  clean bootstraps and exact-candidate hosted macOS CI cannot be replaced by a
  local skip, cache, historical run, or other platform.
- Physical capture/decode evidence is neither required nor authorized. Do not
  access USB/serial hardware, flash firmware, start live capture, or add browser
  decoder behavior. Preserve Cycle 1/2 regressions and optional-web separation.
- Never precreate a future manifest, simulate an operator/project/legal/CI
  result, weaken an assertion, accept a skipped mandatory gate, expose dynamic
  code selection, or expand into excluded work.

The exact details and any additional gates in the approved contract control
over this summary.

## Progress, blocking, and completion

Maintain the Cycle 3 progress and deferred records defined by B1. Report the
active checkpoint, exact candidate, concise verified results, remaining work,
and required operator input or authority. Continue useful safe independent work
when one path awaits an external input, without pre-deciding that input.

Normal implementation, test, review, evidence, or threshold failure remains in
the earliest owning batch. A prohibited request is rejected as out of scope,
not converted into an approval request or execution blocker. Mark the durable
goal blocked only after the same external blocker persists for the number of
consecutive goal turns required by the goal system and no meaningful safe
in-scope work remains. Difficulty, delay, failed checks, or incomplete work is
not by itself a blocker.

Complete only through the exact B5 terminal chain. All R1-R26 requirements and
all eighteen stopping conditions must map to immutable, schema-valid evidence;
the exact final candidate must pass every required regression, conformance,
containment, security, dependency, performance, CI, scope, manifest, and
acceptance gate; and the terminal completion seal must be the final commit and
must not have been an audit input. Preserve the macOS-only and bounded-process-
containment qualifications, limitations, deferrals, rollback identities,
unrelated user changes, and proof that no prohibited action occurred.

## Launch command

```text
/goal Execute and verify Cycle 3 of the Python logic-analyzer rewrite by following CYCLE3_GOAL.md exactly and the approved contract commit ea83a403bb6f644d33069d3bebd41d5f1e0a60c0 / tree d9fb09345ab85580cd8c877745262d1b481e366f. Continue until all eighteen stopping conditions in CYCLE3_ORCHESTRATION.md have immutable proof and the directed terminal completion seal is committed, or the documented blocked condition is genuinely reached. Do not modify CYCLE3_GOAL.md or the approved governing contracts. Do not begin Cycle 4.
```
