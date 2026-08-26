# Logic Analyzer Python Rewrite: Cycle 3 Batch Procedure

## Purpose and authority

This document is the mandatory per-batch operating procedure for Cycle 3. It is
subordinate to `CYCLE3_ORCHESTRATION.md` and operationalizes the settled
contract and proof ownership in
`Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`.

It defines how the primary orchestrator selects, assigns, integrates, verifies,
accepts, and records C3-B1 through C3-B5. It does not start a `/goal`, approve
these draft contracts, authorize work before the approved Cycle 3 goal is
invoked, or authorize Cycle 4.

If this document conflicts with the approved orchestration contract, the
orchestration contract controls and execution pauses for a common-commit
document correction. An implementor, verifier, or acceptance agent may not
reinterpret a conflict into new product, security, evidence, or execution
authority.

## Required reading order

Before selecting C3-B1, the orchestrator reads:

1. `AGENTS.md`, every included repository instruction, and the applicable
   subagent approval policy.
2. The exact approved `CYCLE3_GOAL.md` and its three common-commit passes.
3. `CYCLE3_ORCHESTRATION.md` in full.
4. This document in full.
5. `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` in full,
   especially the settled Step 5 contract, R1-R26 ownership map, operator and
   execution gates, and 18 stopping conditions.
6. `CYCLE3_PREPARATION.md`, the factual Cycle 3 roadmap context, and the three
   common-commit contract passes.
7. The accepted Cycle 1 and Cycle 2 completion records, manifests, current
   implementation and tests, and Cycle 3 review-domain charters.

Every assignment names the exact governing contract commit/tree, batch outcome,
scope, owned paths, prohibited work, authoritative sources, prerequisite
checkpoint, focused and accumulated evidence, and current repository state.
“Implement decoder support” or “continue Cycle 3” is not a bounded assignment.

## Batch state model

Each batch has exactly one current state:

- **Pending:** a prerequisite, accepted checkpoint, contract, goal invocation,
  operator decision, or required authority is absent.
- **Ready:** all prerequisites for bounded work are present.
- **In progress:** implementation or independent verification is active.
- **Verifying:** one immutable candidate is undergoing verification and the
  complete accumulated gate.
- **Awaiting approval:** objective evidence exists but a required project/legal,
  hosted-CI, execution-authority, or operator decision is pending.
- **Complete:** verification, accumulated validation, and acceptance pass in
  order; the atomic manifest is committed; and the checkpoint is appended.
- **Blocked:** the same external blocker has persisted under the approved goal
  policy and no meaningful safe in-scope work remains.

Batches complete only in order. At most one batch may be `Verifying` or
`Awaiting approval`. Later experimentation cannot advance a checkpoint or
consume an unsettled interface. In B1, the accepted semantic-fixture candidate
and the reviewed threshold-proposal sequence are internal gates, not extra
checkpoints and not permission to reorder the five batches.

## Required identities and separation

Each batch uses three distinct stable identities:

- **Implementation agent:** owns only the bounded implementation surface and
  its focused implementation checks.
- **Verification agent:** derives independent boundary, negative, conformance,
  security, resource, performance, provenance, or compatibility checks from
  authoritative evidence and reports exactly `pass` or `changes_required`.
- **Acceptance agent:** audits the exact candidate, verifier findings and
  dispositions, complete accumulated results, scope, authority, provenance,
  evidence ordering, and checkpoint gate and reports exactly `pass` or
  `changes_required`.

The primary orchestrator is a fourth role. It owns preflight, assignments,
integration, immutable candidate creation, complete accumulated validation,
approval routing, evidence assembly, manifest digest/schema checks, checkpoint
records, and final completion. Those duties do not make it one of the three
independent identities.

The following separation rules are mandatory:

- A verifier never approves production behavior or expected fixture output it
  authored and never derives expected output from decoder or host output.
- An acceptance agent never repairs the candidate it audits.
- A B2, B3, or B4 product implementor must not have authored B1 authoritative
  expected outputs. Reassign the product role if this boundary would cross.
- An agent that changes role or edits outside its assigned ownership invalidates
  the affected independence claim; assign a fresh identity and repeat the
  affected review.
- Parallel work is allowed only on disjoint paths behind settled interfaces.
  Keep one integration-changing owner at a time for shared Python models,
  decoder allowlists, IPC schema, package metadata, dependency locks,
  generated fixtures, evidence schema, workflows, or generated assets.
- The orchestrator preserves a coordination slot whenever it delegates work.

## Active-batch progress entry

Before assigning work, create or update the Cycle 3 progress record at the path
frozen by C3-B1. Its active entry has this form:

```markdown
## C3-BN: <name>

- State: Ready
- Objective: <one bounded outcome>
- Prerequisites: <accepted checkpoints, decisions, and authority>
- Governing commit/tree: <full approved contract identities>
- Starting commit/tree: <full repository identities>
- Implementation agent: <stable identity>
- Verification agent: <different stable identity>
- Acceptance agent: <third stable identity>
- In scope: <specific behaviors and artifacts>
- Out of scope: <nearby tempting or prohibited work>
- Owned paths: <non-overlapping path ownership by identity>
- Authoritative evidence: <settled contracts, fixtures, literals, prior manifests>
- Focused evidence: <commands and artifacts>
- Accumulated evidence: <commands and artifacts>
- Authority notes: <allowed execution and approvals required>
- Prohibited runtime audit: <method and expected absence>
- Risks and unknowns: <resolve, defer, or request input>
```

For C3-B1, create the progress record and append this entry before accepting
implementation work. A progress entry is planning state, not machine-readable
evidence, and cannot satisfy a checkpoint. Never rewrite Cycle 1 or Cycle 2
progress history.

## Standard batch procedure

### 1. Select and bound

Select the earliest incomplete batch whose prerequisites are satisfied. Restate
its single outcome and apply the Cycle 3 new-work scope test. Map the assignment
to its earliest-owned R identifiers and stopping conditions. Record unrelated
or excluded findings in the Cycle 3 deferred list immediately; do not repair
them opportunistically.

### 2. Preflight authority and repository state

Before every implementation or validation phase:

- record `git status`, branch, full HEAD, tree, and every unrelated user change;
- confirm the exact approved governing and goal commit/tree and review records;
- confirm required prior checkpoints, manifests, fixtures, decisions, locks,
  tools, environment identity, and operator inputs;
- rerun the narrow prerequisite gate and verify artifact digests;
- resolve owned files and generated-file authority before assignment;
- derive dependency-download, process-inspection, resource-observation, and
  hosted-CI capabilities expected by the phase;
- reuse only approved, stable, narrowly scoped command shapes and route missing
  authority through the root orchestrator under the approval-broker policy;
- prove that no decoder identity, capture, metadata, option, environment value,
  working directory, path, symlink, or output value selects executable code;
  and
- confirm that no prohibited runtime, dependency, platform, hardware, browser,
  or publication action is reachable from the assignment.

No decoder executes before the approved goal is invoked. C3-B1 additionally
requires acceptance of the exact semantic-fixture candidate before its
characterization runner or any decoder snapshot executes. If a prerequisite is
absent, keep the batch pending or record the exact blocker. Never simulate
operator approval, hosted CI, process/resource evidence, project/legal review,
or decoder execution.

### 3. Assign bounded path ownership

Each identity receives:

- one objective and objective acceptance criteria;
- exact paths it may create or edit;
- exact shared or generated paths it must not edit;
- product, fixture, dependency, workflow, and evidence exclusions;
- authoritative sources and independently fixed literals;
- focused commands, accumulated commands, and expected stopping behavior;
- the immutable evidence/review record it must produce; and
- the handoff template below.

An assignment may inspect relevant repository sources, including C# or upstream
source already present as inert explanatory material, but it may execute none
of that reference code. Any unplanned interface or path ownership need returns
to the orchestrator before an edit.

### 4. Implement the smallest owning surface

The implementation agent creates or identifies a focused check that fails for
the intended missing behavior, then makes the smallest change within the
batch's earliest-owned surface. It runs only authorized focused checks and
hands off with an enumerated worktree. Passing implementation-focused checks is
necessary but is not independent verification or acceptance.

C3-B1's semantic fixtures are exceptional only in ordering, not rigor: their
expected records are independently calculated from human-reviewable timelines
before decoder execution. They cannot be generated, corrected, or corroborated
from decoder, host, C#, .NET, libsigrokdecode, `sigrok-cli`, or external runtime
output.

### 5. Integrate and create an immutable candidate

The orchestrator inspects the worktree and integrates only accepted ownership.
It verifies:

- exact Cycle 3 scope, authority, file/digest allowlists, and license gates;
- independent fixture provenance and no output-derived oracle;
- exact mapping, option, samplerate, sample-coordinate, ordering, and typed-
  output contracts;
- one private, single-use, subprocess-only host with closed imports and inert
  request data;
- streaming IPC, parent-owned limits, cancellation, kill/close/reap, typed
  failures, and no partial success;
- one semantic path for private host, public library, and CLI;
- optional-web independence and no live capture, serial open, browser decoder
  path, or unsupported platform claim;
- no production or non-production dependency on or execution of C#/.NET,
  pythonnet, libsigrokdecode, `sigrok-cli`, or external/reference hosts;
- tests that fail for the intended defect rather than encode implementation
  output; and
- preservation of accepted Cycle 1/2 behavior, evidence, rollback paths, and
  unrelated user changes.

The orchestrator runs implementation-focused checks, commits the bounded
candidate, and records its full commit and tree. That immutable identity is the
only object eligible for the next three gates. Reviews of a dirty worktree,
different tree, manifest descendant, or superseded candidate do not transfer.

### 6. Verify the exact candidate independently

The verification agent checks out or otherwise reads the exact candidate and
tests it as an immutable object. It may add only separately owned verification
artifacts in a descendant evidence commit; those artifacts do not change the
tested candidate identity. The review record names:

- verifier identity, UTC timestamp, candidate commit/tree, and worktree state;
- authoritative sources and independently derived expectations;
- exact commands, environment, exit results, artifact paths, and digests;
- numbered findings with requested resolution and disposition; and
- verdict exactly `pass` or `changes_required`.

`changes_required` returns to implementation. The record remains immutable.
Every correction—whether product, fixture, method, dependency, limit, test, or
evidence-affecting—creates a new candidate and requires fresh verification.

### 7. Run complete accumulated validation

Only after independent verification reports `pass`, the orchestrator runs the
batch's entire accumulated gate against the same candidate commit/tree. This is
not a subset chosen from changed files. It includes every prior checkpoint gate,
the active focused suite, inherited Cycle 1/2 regression and evidence checks,
the prohibited dependency/runtime/process audit, and any batch-specific clean
bootstrap or hosted-CI requirement.

C3-B1 freezes exact command names, stable environment paths, lock identities,
evidence schema/validator paths, progress/review/manifest paths, and the mapping
from the minimum command classes below. Until that freeze, proposed names are
placeholders and no missing command may be represented as passing. B1 may
refine names but may not remove a required class:

```text
fresh Python 3.12 hash-locked development environment creation
hash-locked development dependency installation
no-build-isolation, no-dependency editable product installation
pip dependency consistency check
Ruff over the complete Python scope
strict mypy over the production source
complete pytest suite excluding only tests explicitly marked hardware
installed pico-la help smoke
Cycle 1/2 evidence schema validation
Cycle 3 fixture byte-rebuild and digest validation
prohibited dependency/import/process audit
```

Existing Cycle 2 web checks may be included as unchanged regressions using the
accepted lock and commands. They cannot become Cycle 3 browser implementation
or evidence. Exact-candidate hosted macOS CI is mandatory at C3-B4 and C3-B5.
A local sandbox skip, cached result, or run on another candidate is not CI
proof. Clean bootstraps are mandatory at B1, B4, and B5; reused environments in
other batches require matching Python, OS class, lock, and fixture identities.

### 8. Accept the exact candidate independently

Only after the complete accumulated gate passes does the acceptance agent audit
the exact candidate, verifier record, every finding/disposition, accumulated
commands and results, authority, provenance, scope, role separation, and
manifest readiness. Its immutable record uses the same identity/result fields
as verification and reports exactly `pass` or `changes_required`.

Acceptance never precedes accumulated validation. It cannot waive a failed,
skipped, missing, wrong-candidate, wrong-environment, unapproved, or simulated
gate. A correction after acceptance creates a new candidate and invalidates the
candidate's verification, accumulated, and acceptance passes.

### 9. Create the manifest atomically, then checkpoint

Only after implementation evidence, independent verification `pass`, complete
accumulated validation, and independent acceptance `pass` all exist does the
orchestrator assemble that batch's machine-readable manifest in one atomic
write. It then independently recomputes every digest, validates the manifest
against the accepted Cycle 3 schema, commits the manifest, and appends the
checkpoint in a later commit.

The manifest is an evidence descendant and names the tested candidate's full
commit and tree. It includes role identities, review records, exact commands
and results, environment/lock/fixture/limit identities, artifacts and digests,
R-identifier and stopping-condition mappings, exclusions audit, and any
applicable operator/project/legal/CI evidence. It does not imply that evidence
documents were part of the product candidate.

Never create, reserve, pre-populate, or copy a future `c3-bN.json`. A filename,
placeholder, empty object, sample, schema example, or template is not evidence
and cannot be presented as accepted. B1 may create the Cycle 3 schema,
validator, and an explicitly non-evidence documented format example; only
after B1 acceptance may it create the actual B1 manifest. B2-B5 each create
only their own manifest at the equivalent point.

A batch becomes `Complete` only after its schema-valid manifest commit and
checkpoint commit exist. The next batch consumes the checkpoint, not an
uncommitted manifest or conversational pass.

### 10. Decide the next action

- **Pass:** append the checkpoint and select the next batch.
- **Product or owned-proof defect:** remain in the earliest owning batch and
  create a new candidate.
- **Earlier-interface regression:** reopen the earliest owning checkpoint and
  every dependent accumulated gate.
- **Out of scope:** record and defer without implementation.
- **Authority or operator input needed:** pause that path; continue only safe,
  independent, in-scope work that cannot pre-decide the missing input.
- **Contract ambiguity:** stop affected work and use the common-commit contract
  review process; do not settle it in code or fixture output.

## Assignment template

Use this minimum assignment shape for each identity:

```markdown
### Assignment: C3-BN <role> — <bounded objective>

- Governing commit/tree: <full hashes>
- Candidate commit/tree: <full hashes or “not yet created”>
- Prerequisite checkpoint: <identity and manifest digest>
- Earliest-owned requirements: <R identifiers>
- Stopping conditions exercised: <numbers>
- May edit: <exact paths>
- Must not edit: <exact/shared/prohibited paths>
- Authoritative sources: <contracts, accepted fixtures, literal calculations>
- Required focused checks: <commands/artifacts>
- Required accumulated awareness: <commands owned by orchestrator>
- Required review/evidence path: <exact proposed path>
- Execution authority: <allowed command shapes or root-routed need>
- Prohibited actions: <batch-specific plus global exclusions>
- Handoff format: <the standard handoff below>
```

## Handoff template

Every implementation, verification, and acceptance handoff contains:

```markdown
### C3-BN <role> handoff

- Identity and role: <stable identity>
- Governing commit/tree: <full hashes>
- Tested candidate commit/tree: <full hashes>
- Starting and ending worktree: <clean or enumerated changes>
- Changed files: <paths, or none>
- Behavior/evidence delivered: <bounded summary>
- Authoritative provenance: <sources and independently fixed values>
- Commands and exact results: <including exit/skips>
- Environment and dependency identities: <OS/arch/Python/locks as applicable>
- Artifact paths and SHA-256: <all evidence>
- Findings and dispositions: <numbered links>
- Assumptions/discrepancies: <none or explicit>
- Deferrals: <destination>
- Prohibited-runtime/action audit: <method and result>
- Verdict: <implementation ready, pass, changes_required, or blocked>
- Approval needed: <none or policy-compliant request to root>
```

Handoffs are context-preserving coordination records. They do not replace an
immutable verifier/acceptance record, operator decision, manifest, or
checkpoint.

## Global ownership and path boundaries

C3-B1 freezes the exact repository paths after inspecting the approved starting
tree. Until then, these are path classes, not permission to invent product
structure:

- **Orchestrator-only shared governance:** Cycle 3 progress/deferred/completion
  records, evidence schema/validator, active manifests, shared requirement
  traceability, shared locks/workflows, and checkpoint integration.
- **Implementation-owned product:** only the active batch's private host,
  compatibility primitives, decoder-specific adapters, public decode module,
  CLI integration, documentation, package-resource, or focused test paths
  explicitly assigned for that batch.
- **B1 fixture owner:** declarative timelines, independent expected records,
  deterministic generator, characterization-only runner, and measurement
  method/raw-result paths. Expected-output ownership may not later become B2-B4
  product implementation ownership.
- **Verification-only:** independent adversarial fixtures/tests and immutable
  verification records. These may consume public or frozen private contracts
  but may not modify production output or authoritative expected records.
- **Acceptance-only:** immutable acceptance records and audit inputs; no product,
  fixture, threshold, or test correction.
- **Read-only preserved sources:** checked-in decoder snapshots after B1 freezes
  their hashes; accepted Cycle 1/2 manifests and review history; firmware; C#;
  accepted browser/frontend sources except unchanged regression execution.

Decoder snapshot edits are outside Cycle 3. A required source edit is a scope
and provenance decision, not a local correction. Generated output changes must
name their generator owner and regeneration command. No agent edits another
identity's review record or rewrites failed history.

## C3-B1: provenance, semantic fixtures, and approved limits

### Outcome and prerequisites

Record exact UART, SPI, I2C, shim, and helper identities, provenance, hashes,
closed imports, notices, and project/license disposition. Produce independently
derived declarative semantic/stress fixtures that freeze all five unresolved
API-v3 edge semantics. Then, and only then, execute the accepted snapshots in a
non-installed characterization-only runner, record reproducible raw baselines,
derive exact limits, obtain independent proposal review and acceptance, and
obtain explicit operator approval.

The governing contracts and goal must have their required common-commit passes,
and the operator must have invoked the goal. Before that invocation, no decoder
executes and static work cannot become execution evidence. Project/legal review
must settle source placement, notices, and project metadata before editable
source installation exposes snapshots. No wheel, sdist, package publication,
or distributable artifact is authorized.

### Mandatory internal gate order

1. Statically inventory exact files, digests, imports, provenance, notices, and
   dependency/runtime exclusions.
2. Implement human-reviewable declarative timelines, independently calculated
   expected calls/records, generator, and semantic/stress fixture tests without
   executing decoder or host code. The fixtures decide explicitly: first and
   later `wait({})`; current-versus-next-sample search, sample-zero history, and
   exact skip advancement; simultaneous conjunction/alternative priority;
   interval endpoint and boundary coordinates; and end-of-input treatment of
   partial units and already-emitted records.
3. Commit one immutable **semantic-fixture candidate** binding every source,
   generator, timeline, expected record, decision, and digest.
4. A verifier independently reviews that exact fixture candidate and records
   `pass` or `changes_required`.
5. The orchestrator runs the complete fixture accumulated gate against that
   exact candidate, including byte rebuild, schema/generator tests, literal
   review coverage, provenance/import/license audit, and inherited regressions.
6. The acceptance identity audits that same fixture candidate, verifier record,
   and accumulated result and records `pass` or `changes_required`.
7. Only after all three gates pass may the implementation identity add the non-installed
   characterization runner and measurement method and execute the approved
   checked-in snapshots.
8. Commit an immutable raw-baseline candidate containing the runner, method,
   and observations with machine/OS/Python, warm-up, repetition,
   deterministic input/output counts, fixture/method/runner digests, and the
   macOS resource-observation mechanisms. Raw data is never edited to match a
   later limit.
9. The verifier independently reproduces the method and raw observations; the
   orchestrator then runs the complete raw-baseline accumulated gate; and only
   then does the acceptance identity audit the candidate, method, environment,
   completeness, provenance, reproduction, and discrepancies.
10. Only after those passes does the orchestrator commit an immutable proposal
    candidate naming exact input sample/request-byte, deadline, cancellation-
    grace, memory/address-space, recursion, output record/encoded/decoded/text/
    bytes/item/depth, diagnostic, retained-result, performance, and SPI-word-
    size ceilings.
11. The verifier reviews the exact proposal candidate against raw evidence and
    boundary cases; the orchestrator runs the complete proposal accumulated
    gate; and the acceptance identity then audits that same proposal candidate
    and records its verdict.
12. The operator explicitly approves or amends the committed values. An
    amendment creates a new proposal candidate and repeats proposal
    verification, accumulated validation, and acceptance before renewed
    operator approval.
13. The orchestrator assembles the final B1 candidate binding all intermediate
    identities/digests and exact frozen commands. It receives the standard
    candidate verification, complete accumulated validation, acceptance,
    atomic manifest, and checkpoint sequence.

A correction at steps 1-6 creates a new semantic-fixture candidate and transfers
no fixture pass. A changed fixture, method, runner, environment class, worker
model, or weakened ceiling after steps 7-13 reopens the owning internal gate and
invalidates all dependent observations, proposals, approvals, and batch passes.

### Ownership and proof

Implementation owns R1-R5 and the B1 start of R21, R23-R25: provenance/license
inventory; timeline schema; independently calculated expected records;
deterministic generator; characterization-only runner; method; raw results; and
deterministic counts. The runner is never installed/imported by the product and
has no public API.

Verification independently reviews every literal timeline and expected record,
proves the generator consumes no decoder/host output, inspects closed imports
and hashes, reproduces characterization, exercises representative, boundary,
dense-output, malformed, cancellation/reap, and hostile-worker cases, and
issues a distinct threshold-proposal verdict.

Acceptance audits fixture independence, all five API-edge decisions,
provenance/notices/project-license disposition, method, raw data, reproduction,
proposal reasoning, verifier findings, exclusions, and candidate ordering.
Only the operator approves exact numeric values.

Focused evidence includes byte-stable fixture rebuild, literal defaults/options/
mappings/all-output/order/edge-case review, file/import/license audit,
reproducible raw characterization, proposal review, acceptance verdict, and
operator decision. Accumulated evidence includes accepted Cycle 1/2 non-hardware
and manifest validation, a fresh locked environment, and dependency/import/
process proof that every prohibited runtime is absent.

Raw characterization covers input samples/request bytes; spawn/import/decode
wall time; cancellation/terminate/kill/reap latency; worker peak address space
and parent retained memory; recursion behavior; record, encoded/decoded byte,
text/bytes, nested item/depth, diagnostic, and retained-result counts; and
reviewed UART skip-heavy, SPI edge-heavy/default-word-size, I2C mixed-condition,
malformed, dense-output, and hostile-worker cases. Missing or unreliable
observations remain explicit and cannot be converted into convenient limits.

B1 cannot checkpoint with a provisional semantic answer, numeric value, SPI
maximum, project/license disposition, command/path mapping, or operator
decision. No B2 work begins before its checkpoint.

## C3-B2: isolated compatibility host and containment

### Outcome and prerequisite

Implement a private native host that consumes validated inert requests,
executes exactly one hash-pinned focused decoder in one fresh single-use Python
process, returns the settled typed result, and enforces approved containment and
cleanup. It provides no public library API or installed CLI command.

C3-B1 must be complete with immutable fixtures and operator-approved numeric
ceilings. Any changed fixture, method, worker model, environment class, or
ceiling first reopens B1.

### Ownership and proof

Implementation owns R6-R12 and R22: internal immutable request/result/value
models; digest/import-root enforcement; exact pre-spawn capture, samplerate,
mapping, and option validation; the frozen API-v3 primitives; one single-use
worker; versioned streaming length-framed IPC; output normalization and every
approved counter; parent-owned deadline/cancellation; typed failure conversion;
and deterministic kill/close/reap cleanup. It may not add a public surface,
in-process mode, dynamic decoder path, or prohibited dependency.

Verification independently mutates IDs, hashes, paths, symlinks, environment/
import shadowing, mappings, options, frames, lengths, tags, output IDs,
coordinates, nested values, diagnostics, exits, signals, exceptions, hangs,
memory/recursion pressure, output floods, cancellation races, and partial IPC.
It recomputes boundaries without production counters and proves no partial
success, traceback/path disclosure, descriptor/worker leak, retained partial
result, poisoned global state, or failed subsequent valid request.

Acceptance audits every frozen host primitive and the narrow macOS containment
claim, confirms exact approved limits without weakening/rebasing, verifies that
request/capture data remains inert, and confirms no public interface appeared.

Focused evidence includes B1 semantic fixtures against the private host,
internal unit/contract tests, hostile IPC/process tests, deterministic repeated
serialization, process/descriptor lifecycle inspection, limit boundary/overrun
tests, prohibited import/dependency/process tests, and successful decode after
every failure class. Accumulated evidence includes immutable B1 identities,
fixture rebuild, approved limits, B2 proof, and inherited regressions/evidence.

## C3-B3: focused UART, SPI, and I2C conformance

### Outcome and prerequisite

Prove that the private host produces every settled annotation, Python, binary,
and metadata output applicable to the exact UART, SPI, and I2C snapshots across
defaults, material options, mappings, boundaries, malformed/incomplete traffic,
simultaneous waits, and equivalent inert capture sources.

C3-B2 must be complete. Decoder identities, source hashes, fixture semantics,
host contract, and numeric ceilings remain exactly those accepted in B1/B2.

### Ownership and proof

Implementation owns only R13-R16 decoder-specific adapters or static tables
required to feed the generic B2 host and preserve declared metadata/results.
It may not edit decoder snapshots, expected fixtures, generic-host exceptions,
or hard-code fixture outputs.

Verification independently materializes equivalent `CaptureResult`, replay
schema 1/2, and explicit-metadata CSV inputs from reviewed timelines. It compares
complete typed records and canonical bytes for every default/material option,
required/optional channel combination, noncontiguous/reordered physical mapping,
start/end and simultaneous events, malformed/incomplete traffic, and repeat
runs. Static source inspection is the sole allowed use of C# or upstream
material; its runtime output is never generated or used.

Acceptance audits complete focused-decoder coverage, fixture ownership,
cross-source equality, output kinds/order, source/digest identity, and absence
of decoder-specific expansion to the host API or trust boundary.

Focused evidence consists of separate UART, SPI, and I2C conformance records;
complete expected-record comparisons; mapping/option negatives; cross-source
byte equality; exact digest/import proof; and byte-identical repeats.
Accumulated evidence adds B1 fixtures/limits, B2 containment/failure matrix,
B3 conformance, and inherited non-hardware/evidence regressions.

## C3-B4: public library and installed CLI

### Outcome and prerequisite

Expose the already accepted private host through the one settled synchronous
typed library and offline installed CLI, without a second semantic path,
dynamic code selection, optional-web dependence, serial/live capture, or
browser/API behavior. C3-B3 must be complete for all three decoders.

### Ownership and proof

Implementation owns R17-R20: immutable public types and stable exports under
`pico_logic_analyzer.decode`; `decode_capture(...)` delegation to the B2 host;
non-weakenable limits; exact `pico-la decode` replay/CSV grammar; typed option/
mapping parsing; canonical compact sorted-key JSON plus LF; stderr-only
diagnostics; existing exits plus decoder failure exit 7; documentation;
package-resource placement allowed by B1; and hash-locked metadata with no
prohibited production or development/test dependency.

Verification runs editable-installed library and CLI black-box tests from
outside the source directory: success bytes; stderr/exits; duplicate, unknown,
and invalid inputs; replay/CSV equivalence; no caller limit weakening; import/
open spies proving no web or serial side effect; clean install and lock/process
audit; and exact-candidate hosted macOS CI.

Acceptance audits public types, examples, machine-output contract, notices and
metadata, optional-web independence, lock closure, macOS-only documentation,
CI identity, absence of external runtime use, and lack of publication.

Focused evidence includes strict-mypy consumer use, installed library examples,
installed CLI golden/negative tests, clean hash-locked bootstrap, `pip check`,
source/resource/license audit, prohibited dependency/import/process audit, and
exact-candidate hosted CI. Accumulated evidence includes all B1-B3 gates, public
black-box tests, the full existing core/CLI/web regression without Cycle 3 web
changes, static checks, manifest validation, and exact-candidate CI.

## C3-B5: exact-candidate accumulated proof and completion

### Outcome and prerequisite

Prove one immutable final product candidate against R1-R26 and all 18 Cycle 3
stopping conditions. B5 introduces no product behavior, changes no fixture or
threshold, and rebases no approved method. C3-B4 must be complete with no
unresolved finding, missing decision, changed approved identity, or unexplained
repository delta.

### Ownership and proof

Implementation makes no product change unless a defect reopens its earliest
owning batch. Any correction creates a new candidate there and reruns every
dependent verification, accumulated gate, acceptance, manifest, and checkpoint
sequence before B5 resumes.

Verification independently reruns semantic fixtures, all three conformance
suites, containment/failure/cancellation cleanup, public library/CLI, clean
installation, dependency/import/process absence, Cycle 1/2 regression/evidence,
and exact-candidate resource/performance suites. It verifies every artifact
digest, excluded-action absence, repository state, and unchanged approved
fixture/method/environment/limit identities.

Acceptance audits the exact final candidate/tree, all five ordered role
sequences and manifests, every finding/disposition, local and hosted-CI results,
limit enforcement, source/license/support/rollback statements, clean or fully
qualified repository, R1-R26 mapping, and conditions 1-18. It records final
`pass` or `changes_required` before the B5 manifest and checkpoint exist.

The B5 focused gate checks final packet completeness, schema/digest audit,
repository/prohibited-action audit, role/evidence ordering, and stopping-
condition traceability. Its accumulated gate is fresh and complete: Python 3.12
locked bootstrap; dependency consistency; Ruff; strict mypy; every non-hardware
test; installed CLI help and black-box decode; Cycle 1/2 evidence validation;
B1 fixture regeneration; UART/SPI/I2C conformance; the full process/IPC/
security/cancellation matrix; final measurements against unchanged approved
thresholds on the characterized macOS environment class; exact-candidate hosted
macOS CI; license/resource audit; and a second independent evidence-digest
verification.

The Cycle 3 goal remains active until the B5 manifest and checkpoint are
committed, the completion record identifies the exact accepted candidate/tree,
and every stopping condition is durably mapped to evidence.

## Correction, reopening, and rollback

When any candidate or completed checkpoint regresses:

1. Identify the earliest R-owner and checkpoint.
2. Mark that batch `In progress` with regression evidence; preserve history.
3. Pause dependent implementation and acceptance.
4. Apply the smallest correction within the owning surface.
5. Create a new immutable candidate; no earlier pass transfers.
6. Repeat independent verification, complete accumulated validation, and
   acceptance for the owning batch.
7. Create a new post-acceptance manifest and checkpoint correction record.
8. Rerun every dependent accumulated gate and refresh its evidence before
   resuming the next incomplete batch.

The following always reopen C3-B1: any changed decoder/helper/shim file or hash,
provenance/license disposition, declarative or expected fixture, API-edge
semantic, generator, characterization runner/method, environment class, worker
model used for baselines, or numeric ceiling/SPI maximum. Weakened limits require
a new proposal, independent review, acceptance, and explicit operator approval.
B2 host/IPC/limit-enforcement changes reopen B2; decoder-specific conformance
changes reopen B3; public library/CLI/package changes reopen B4. B5 corrections
always reopen the actual earliest owner rather than being patched “in final.”

Rollback means returning to the prior accepted Python candidate or using the
preserved existing application/firmware operationally. It never authorizes
modifying or deleting accepted evidence, firmware, C# sources, decoder snapshots,
or user changes and never authorizes running C#/.NET as Cycle 3 evidence.

## Authority, escalation, and prohibited actions

Only the root orchestrator may request execution escalation. Every delegated
assignment follows the approval-broker policy, never requests approval directly,
and returns a structured `APPROVAL_NEEDED` handoff containing command,
capability, target scope, justification, and a narrow stable prefix proposal.
The root checks existing approvals, normalizes command shape, consolidates
equivalent needs, and requests the narrowest reusable authority. Approval is a
capability gate, not product-scope authority.

Normal external execution may be required only for approved locked dependency
retrieval, macOS process/resource observation, or exact-candidate hosted macOS
CI. It must be owned by an active batch and recorded without credentials,
sensitive paths, or machine-local capability values. Safe static inspection and
independent documentation may continue while approval is pending if it cannot
pre-decide the blocked result.

The following are prohibited throughout production, development, fixture
generation, tests, verification, characterization, performance work,
acceptance, and CI:

- executing, installing, importing, linking, or depending on C#/.NET,
  pythonnet, libsigrokdecode, `sigrok-cli`, upstream/reference decoder hosts, or
  any differential runtime;
- using output from any such runtime to generate, correct, corroborate, or
  accept a fixture;
- executing user, system, capture-selected, request-selected, path-selected, or
  dynamically discovered decoder code;
- decoder stacking, decoder-selected files, output files/exports, `.lac`,
  browser/API/frontend decoder integration, serial/live capture, hardware or
  firmware operations, package publication, distributable builds, or Linux/
  Windows support claims;
- weakening subprocess isolation, hash/import allowlists, parent-owned limits,
  cancellation/reaping, or inert-data rules for convenience; and
- treating a required skip, manual assertion, stale candidate result, missing
  operator decision, or unapproved external result as passing evidence.

Encountering a prohibited runtime or action is a scope violation to remove or
report, never a reason to request authority for it. C# and already available
upstream/reference source may be read only as inert explanatory material.

## Checkpoint record template

Append one record after each accepted batch:

```markdown
### Checkpoint C3-BN — <name>

- State: Complete
- Completed at: <ISO-8601 UTC timestamp>
- Tested candidate commit: <full hash>
- Tested candidate tree: <full hash>
- Candidate worktree state: <clean or enumerated unrelated changes>
- Candidate creation commit: <identity>
- Implementation agent: <stable identity>
- Verification agent and verdict: <different identity; pass>
- Accumulated-validation owner/result: <orchestrator; exact result>
- Acceptance agent and verdict: <third identity; pass>
- Governing contract/goal identities: <full commits/trees>
- Prior checkpoint/manifest identity: <path, commit, SHA-256>
- Environment: <OS/arch/Python and characterized class>
- Dependency identity: <development lock and installed-set digests>
- Decoder/fixture identity: <allowlist, file-set, fixture digests>
- Approved-limit identity: <decision path/commit/digest>
- Objective evidence: <tests, reports, observations>
- R identifiers and stopping conditions: <mapped evidence>
- Files changed: <paths or concise groups>
- Focused commands: <command and exact outcome>
- Accumulated commands: <command and exact outcome>
- CI evidence: <run/jobs/exact commit, or not applicable>
- Resource/performance evidence: <record/digest, or not applicable>
- Project/license evidence: <record/digest, or inherited B1 identity>
- Prohibited dependency/runtime/process audit: <method/result>
- Evidence manifest: <path, commit, SHA-256, schema validation result>
- Findings and dispositions: <immutable review links>
- Decisions/discrepancies: <settled behavior and provenance>
- Deferred findings: <destination>
- Known limitations: <remaining accepted constraints>
- Repository state: <checkpoint commit/worktree summary>
- Next batch: <identifier and unmet inputs>
- Blocked: no
```

Failed or superseded attempts remain concise immutable history under the active
batch. They are never rewritten into a completed checkpoint.

## Independent verification expectations

Verification must be structurally independent of production output:

- Review literal protocol timelines, transitions, expected wait calls, and
  complete records rather than asking the decoder to create expected data.
- Rebuild samples and expected outputs using fixture-owned declarative rules,
  with generator independence and byte digests proved.
- Mutate decoder IDs, files, hashes, imports, paths, symlinks, environment, IPC,
  tags, lengths, coordinates, values, exits, signals, time, memory, recursion,
  diagnostics, and cancellation independently of production helpers.
- Recompute counts and limit boundaries separately from host counters.
- Inspect exact process and descriptor cleanup after every failure and run a
  valid subsequent request.
- Materialize equivalent in-memory, replay-schema-1/2, and explicit-metadata
  CSV captures independently and compare complete canonical bytes.
- Invoke installed library/CLI behavior outside the source directory and spy on
  optional-web and serial imports/opens.
- Reproduce B1 characterization and B5 final measurement methods on the
  approved macOS environment class without changing fixtures or thresholds.
- Audit locks, installed distributions, imports, process tables, CI steps, and
  evidence to prove prohibited runtimes are absent from all non-production as
  well as production paths.

Ambiguous evidence is reported before changing expected behavior. A finding
that changes objective, scope, trust, authority, batch ownership, evidence
ordering, or stopping conditions pauses execution for the common-commit contract
review process.

## Cycle 3 final review packet

Before C3-B5 acceptance, assemble immutable links and digests for:

- R1-R26 and all 18 stopping conditions;
- five checkpoint records and five post-acceptance manifests;
- every implementation handoff and immutable verification/acceptance record,
  including failed and superseded rounds;
- exact decoder/shim/helper files, hashes, provenance, closed imports, notices,
  project/license disposition, and package placement;
- independent timelines, expected outputs, generator, all five API-edge
  decisions, rebuild proof, and fixture digests;
- characterization method/environment, raw B1 observations, reproduced
  results, proposal reviews, operator-approved values, and final B5 measurements;
- private-host API-v3, IPC, typed-output, limit, failure, cancellation, cleanup,
  and post-failure evidence;
- UART, SPI, and I2C conformance plus in-memory/replay/CSV equality;
- installed public library/CLI type, byte, stderr, exit, inert-input,
  optional-web, and no-serial evidence;
- fresh locked installation, static checks, every non-hardware regression,
  Cycle 1/2 manifest validation, and exact-candidate hosted macOS CI;
- dependency/import/process/CI proof that C#/.NET, pythonnet,
  libsigrokdecode, `sigrok-cli`, and external/reference runtimes were never used;
- repository status, support/rollback statement, limitations, deferrals, and
  prohibited/excluded-action audit; and
- a second independent verification of every final evidence digest and manifest
  schema result.

This packet is completion evidence, not a sixth batch and not permission to add
features. Preparatory common-commit review approves the contracts before the
goal; B5 acceptance instead proves that one exact executed candidate fulfilled
them without reordering or weakening any gate.
