# Cycle 3 Preparation Procedure

## Status and purpose

This document coordinates the work required before Cycle 3 of the Python logic-
analyzer rewrite may begin. It is a preparation checklist and progress record;
it is not a Cycle 3 implementation contract, does not start a durable goal, and
does not authorize product, firmware, hardware, dependency, workflow, or decoder
execution changes.

Cycle 3 implementation begins only after all ten steps below are complete, the
governing Cycle 3 contracts and durable-goal prompt have the required independent
common-commit approvals, the final launch preflight is clean, and the operator
invokes the approved `/goal` command.

This file may be updated during preparation to record concise status, decisions,
artifact paths, and commit identities. It is not a substitute for any required
discovery record, governing contract, review record, or execution evidence.
Substantive decisions must be recorded in their owning authoritative artifact.

## Authority and boundaries

Preparation follows this authority order:

1. `AGENTS.md` and every included repository instruction.
2. Explicit operator direction for Cycle 3 preparation.
3. The accepted Cycle 2 completion proof and evidence as the regression
   baseline.
4. This preparation procedure.
5. `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` as technical
   roadmap context only.

The future `CYCLE3_ORCHESTRATION.md` and `CYCLE3_BATCH_EXECUTION.md` become the
governing Cycle 3 execution contracts only after their required approval. The
future `CYCLE3_GOAL.md` may launch execution only after its separate required
approval. Until then, none of those files authorizes implementation.

Preparation may:

- inspect repository history, accepted evidence, source, tests, decoder files,
  licenses, and documentation;
- run existing non-mutating baseline checks when needed to characterize the
  current repository;
- create or revise preparation, discovery, roadmap, contract, reviewer-charter,
  and immutable review documents; and
- request operator decisions needed to settle scope, trust, platform, evidence,
  or acceptance boundaries.

Preparation must not:

- implement the Cycle 3 decoder host, decoder integration, or decoder UI;
- add or update Cycle 3 product dependencies, locks, workflows, fixtures, or
  product tests as if execution had begun;
- execute decoder code merely to accelerate discovery; any necessary bounded
  reference experiment requires an explicit recorded authority decision first;
- modify, build, or flash firmware or change persistent device state;
- weaken or rewrite accepted Cycle 1 or Cycle 2 evidence;
- pre-create Cycle 3 checkpoint evidence manifests; or
- begin Cycle 4 or later work.

## Starting repository facts

The preparation baseline must initially reconcile these distinct identities:

- Cycle 2 final accepted product candidate:
  `2d5484a73d881496cdf5a35c799dfb01eedad229`
- Cycle 2 final accepted product tree:
  `8c76bce79922263468cb6ceaa4f1990703a84bfc`
- Cycle 2 completion checkpoint: `7fe1f5c`
- Cycle 2 completion-proof commit: `f558b58`
- Repository HEAD when this procedure was drafted:
  `5b409a6384624bfb6b51bc323c97a54244477dde`
- Repository tree when this procedure was drafted:
  `74249d3dcb3eb414268d34f467164d90fd3b90b4`
- Branch when this procedure was drafted: `python-rewrite`
- Draft-time worktree before adding this file: clean

Commit `5b409a6` adds the web frontend launcher and documentation after the Cycle 2
completion proof. Preparation must not silently describe that later state as the
accepted Cycle 2 product candidate. Step 1 must determine and record how the
post-completion delta enters the Cycle 3 starting baseline.

## Preparation records

Use the checklist at the end of this file for concise progress. Each completed
step must name its durable output and exact commit where applicable. Detailed
technical findings and operator decisions belong in the discovery review or
governing contracts rather than being duplicated here.

A preparation step is complete only when its exit gate is satisfied. Starting a
later independent step does not waive an earlier exit gate, and no approval may
be inferred from a draft, conversational handoff, uncommitted file, or review of
a different commit.

## Step 1: Reconcile the starting baseline

Compare the accepted Cycle 2 product candidate and completion evidence with the
current repository, including every post-completion commit and any unrelated or
uncommitted change.

Record:

- exact accepted Cycle 2 candidate, tree, checkpoint, manifests, and completion
  proof;
- exact current HEAD, tree, branch, and worktree state;
- a path-level inventory of post-completion changes;
- whether each later change is accepted as Cycle 3 starting input, requires
  focused validation or review, is unrelated and preserved, or is excluded from
  the proposed baseline; and
- the regression commands and concise results used to establish the selected
  baseline.

Do not rewrite accepted Cycle 2 records or imply that later changes inherited
Cycle 2 acceptance.

**Required output:** create
`Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` with a committed
baseline-reconciliation section containing exact commit and tree identities and
a clear disposition for the post-completion delta. Step 3 expands that same
record into the complete bounded discovery review.

**Exit gate:** one unambiguous proposed Cycle 3 baseline exists, with no
unclassified repository change.

## Step 2: Reconcile the technical roadmap

Update `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md` only to
make its historical and future-cycle context factually consistent with accepted
Cycle 2 decisions and results. In particular, reconcile its obsolete Cycle 2
references to PySide6, `.lac`, Linux support, and work already delivered through
the React/TypeScript/Vite browser application, wider capture, replay schema 2,
CSV import/export, parallel-bus analysis, and performance gates.

Preserve useful history and clearly distinguish:

- accepted completed behavior;
- the proposed focused Cycle 3 direction;
- operator decisions still awaiting discovery; and
- Cycle 4 or later parity work.

A factual roadmap correction is not authority to select new Cycle 3 scope.

**Required output:** a committed factual roadmap revision linked from the Cycle
3 discovery review.

**Exit gate:** no known stale roadmap statement can be mistaken for current
Cycle 3 authority or an unmet Cycle 2 requirement.

## Step 3: Perform bounded Cycle 3 discovery

Expand `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md` from its
Step 1 baseline record. Inspect the proposed baseline and the minimum sources
needed to define a focused decoder cycle, including:

- accepted Cycle 1 and Cycle 2 completion evidence and regression surfaces;
- current Python capture, replay, CSV, bus-analysis, CLI, API, browser, security,
  cancellation, and evidence contracts;
- the checked-in UART, SPI, and I2C decoder versions and their auxiliary files;
- decoder provenance, local patches, licensing, imports, metadata, channels,
  options, outputs, and exact API-v3 calls exercised;
- the existing C# sigrok bridge and current application as read-only behavioral
  references;
- available deterministic captures and the gaps in reference annotations;
- dependency, process-isolation, resource-bound, platform, CI, and performance
  implications; and
- public-library, CLI, and possible browser annotation workflows.

Every uncertainty must be classified as resolved by existing evidence, requiring
a bounded approved experiment, requiring an operator decision, or deferred
outside Cycle 3. Discovery does not implement the proposed solution.

**Required output:** a committed bounded discovery review with exact baseline
identity, inspected evidence, unresolved questions, recommendations,
alternatives, risks, and proposed completion evidence.

**Exit gate:** the operator has enough evidence to decide the Cycle 3 product,
trust, platform, and proof boundaries without implementation guesswork.

## Step 4: Record operator decisions

Present the discovery recommendations and material alternatives to the operator.
Record explicit decisions in the discovery review, including at minimum:

1. whether Cycle 3 remains limited to the checked-in UART, SPI, and I2C decoder
   versions;
2. whether the accepted surface is headless library and CLI only or also
   includes browser annotation display and interaction;
3. which decoder-code sources are trusted and whether only checked-in code may
   execute;
4. whether execution is in-process or isolated, and the accepted security claim;
5. authoritative sources for expected annotations and fixture provenance;
6. required timeout, cancellation, memory, output, and exception-isolation
   bounds;
7. platform and CI support claims, including whether support remains macOS only;
8. dependency, decoder-version, patch, and license policy;
9. whether deterministic replay/synthetic fixtures suffice or a live physical
   capture/decode workflow is required; and
10. explicit exclusions and deferrals.

Operator decisions supersede unapproved discovery recommendations but do not
themselves start implementation.

**Required output:** a committed revision of the discovery review in which every
material recommendation is approved, rejected, replaced, or explicitly
deferred.

**Exit gate:** no unresolved operator choice can materially change the proposed
Cycle 3 objective, trust boundary, platform claim, or stopping condition.

## Step 5: Freeze the narrow Cycle 3 contract surface

Using the approved decisions, define the exact behavior that the later governing
contracts must preserve. At minimum settle:

- decoder identity, provenance, version, license, and allowed import boundary;
- the precise subset of `sigrokdecode` constants, base-class behavior,
  `has_channel()`, `wait()` conditions and `matched`, `samplenum`, skip behavior,
  `register()`, `put()`, samplerate metadata, annotations, and Python outputs
  actually required by the accepted decoders;
- deterministic channel mapping, option validation/defaults, annotation schema,
  ordering, time/sample semantics, and error reporting;
- library, CLI, and any approved browser/API contracts;
- cancellation, deadline, allocation, output-volume, recursion, and failure-
  isolation behavior;
- capture and decoder trust boundaries, including the prohibition on capture-
  selected executable code;
- fixture provenance and independent expected-output derivation;
- accepted performance-baseline and later-threshold procedure; and
- exclusions such as stacking, user decoder discovery, all-decoder import
  compatibility, decoder-selected files, `.lac`, .NET runtime dependence, and
  later parity features unless the operator expressly changes them.

**Required output:** settled contract material in the approved discovery review
that can be incorporated without reinterpretation into the governing documents.

**Exit gate:** independent implementor, verifier, and acceptance agents could
consume the proposed interfaces without making a substantive product or trust
decision themselves.

## Step 6: Define batches, proof ownership, and stopping conditions

Derive Cycle 3 batches from the settled dependency order rather than copying the
old roadmap mechanically. Assign every required behavior and every final proof
to exactly one earliest owning batch while retaining an accumulated final gate.

The proposed structure must identify:

- prerequisites and settled interfaces for each batch;
- implementation, independent verification, and independent acceptance
  ownership;
- focused, accumulated, security, compatibility, performance, and any physical
  commands or evidence;
- immutable candidate and correction behavior;
- evidence-manifest creation and checkpoint timing;
- operator or execution authority gates; and
- a numbered, objectively verifiable final stopping-condition checklist.

Do not pre-create checkpoint manifests or treat proposed evidence paths as
evidence.

**Required output:** approved proposed batch boundaries and a complete
requirement-to-proof ownership map in the discovery review.

**Exit gate:** every required outcome has an owner, prerequisite, objective
proof, checkpoint, and final stopping-condition mapping, with no circular gate.

## Step 7: Draft the governing contracts and review framework

Create:

- `CYCLE3_ORCHESTRATION.md`;
- `CYCLE3_BATCH_EXECUTION.md`;
- `docs/rewrite-reviews/cycle-3/README.md`; and
- `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`.

The orchestration contract must govern the durable objective, required and
excluded scope, authority, validation, evidence, checkpoints, blocking, and
stopping condition. The batch contract must govern assignment, candidate
creation, verification, accumulated validation, acceptance, correction,
manifest, and checkpoint mechanics.

Reviewer charters must cover at least these independent domains:

1. decoder API/runtime behavior and fixture correctness;
2. capture, annotation, library, CLI, API, and approved browser workflows; and
3. executable-code security, isolation, dependencies, licensing, platform/CI,
   performance, evidence, and orchestration governance.

**Required output:** one immutable proposed contract commit containing the
approved discovery review, roadmap correction, both governing contracts, and
the Cycle 3 review framework.

**Exit gate:** the documents are internally consistent and ready for independent
common-commit review; draft status alone is not approval.

## Step 8: Obtain common-commit contract approval

Assign three independent reviewers according to the Cycle 3 architectural
charters. Each reviewer must inspect the complete proposed document set at one
exact commit and write an immutable record containing reviewer identity, exact
commit and tree, UTC timestamp, verdict exactly `pass` or `changes_required`,
findings, requested resolutions, and dispositions.

Preserve every failed or superseded review round. Resolve findings in a new
commit. Any substantive objective, scope, authority, ownership, security,
batch, validation, evidence, checkpoint, platform, or stopping-condition change
requires a fresh review by all three reviewers on one new common commit.

**Required output:** three final `pass` records in one latest complete review
directory, all naming the same full governing-contract commit and tree.

**Exit gate:** every finding is durably disposed and the three common-commit
passes approve the exact discovery/roadmap/contract set. Passes may not be mixed
across commits or rounds.

## Step 9: Draft and approve the durable goal

Only after Step 8 passes, create `CYCLE3_GOAL.md`. It must point to rather than
redefine the approved governing contracts and must specify:

- exact approved contract commit/tree and review records;
- required reading and authority order;
- primary orchestrator and fixed worker-lane configuration;
- bounded assignments, context-preserving handoffs, and role separation;
- the exact per-batch sequence: focused checks, immutable candidate,
  independent verification, complete accumulated validation, independent
  acceptance, manifest, then checkpoint;
- the rule that every correction creates a new candidate and transfers no
  earlier pass;
- operator, dependency, platform, decoder-execution, and any hardware gates;
- blocking and completion behavior; and
- the exact `/goal` launch command.

Submit the complete common-commit set, now including `CYCLE3_GOAL.md`, to the
same three architectural review domains. Preserve failed rounds and resolve any
finding on a new common commit with the required fresh reviews.

**Required output:** three final `pass` records in one latest complete goal-
review directory, all naming the same full commit and tree containing the exact
durable-goal prompt and governing document set.

**Exit gate:** the execution prompt cannot bypass, reorder, weaken, or leave
ambiguous any approved product, security, evidence, candidate, acceptance, or
stopping-condition rule.

## Step 10: Complete final launch preflight

Immediately before invoking `/goal`, record and verify:

- exact current HEAD, tree, branch, and clean or explicitly qualified worktree;
- the selected Cycle 3 starting baseline and disposition of every later or
  unrelated change;
- approved discovery, roadmap, orchestration, batch, and goal identities;
- three contract-review passes and three goal-review passes on their required
  exact common commits;
- current decoder and dependency provenance/digests required at launch;
- concise results of the approved baseline regression commands;
- required operator decisions and any inputs needed before their owning batch;
- platform/support qualification;
- absence of pre-created Cycle 3 evidence manifests; and
- confirmation that no prohibited preparation action occurred.

If the repository changed after the approved goal candidate, classify the delta
and determine whether the governing review rules require a new common-commit
review. Do not launch from an unexplained tree.

The initial Cycle 3 progress record created under the durable goal must repeat
the exact launch repository identity and approvals. This preparation record does
not substitute for that execution record.

**Required output:** a completed preparation checklist below, a clean or fully
qualified repository, and an exact approved launch command.

**Exit gate:** the operator can invoke the approved `/goal` without any agent
needing to infer scope, authority, trust, evidence, baseline, or completion
semantics.

## Step 10 launch preflight record

The final preparation preflight ran at `2026-08-26T16:04:09Z`. Its clean
pre-record inspection identity was:

- HEAD: `f67843a7dc8fd6f97e1f4389b3fd7e90db03c3d6`;
- tree: `3afb02e68c9ea6187f3905c7c835318855faa3a2`;
- branch: `python-rewrite`;
- upstream qualification: 37 commits ahead of `origin/python-rewrite`, with no
  tracked, staged, unstaged, or untracked change; and
- unrelated user changes: none observed.

The only descendants of the approved goal candidate are its three immutable
`goal-final-round-4` approval records and the preparation-checklist identity
refresh. They change no product, decoder snapshot, dependency, fixture,
workflow, approved governing contract, or approved goal. The final launch HEAD
is the commit that contains this preflight record. The root orchestrator must
verify that commit's full HEAD/tree, branch, and clean worktree after committing
this record and before invoking the goal; the initial Cycle 3 progress record
must repeat that exact launch identity and the approvals below. This unavoidable
post-record commit identity does not alter an approved governing file.

### Baseline, governing identities, and approvals

The selected technical and governance input baseline remains
`c163a8353550e0b80dd7f001b21147659ad307ff`, tree
`45556769aab973c7671f58d57bae1878a46af9f2`, on `python-rewrite`. It inherits
the accepted Cycle 2 candidate
`2d5484a73d881496cdf5a35c799dfb01eedad229`, tree
`8c76bce79922263468cb6ceaa4f1990703a84bfc`, includes the focused launcher and
documentation delta `5b409a6384624bfb6b51bc323c97a54244477dde`
without retroactive Cycle 2 acceptance, and includes the preparation governance
at `c163a83`. Every later change is committed preparation, review, or approval
evidence; no later product or unrelated change is present.

The approved discovery review, roadmap, orchestration contract, batch contract,
and review framework are byte-for-byte equal in the worktree and HEAD to the
six-file governing set at contract commit
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. All three immutable
`contract-final-round-5` records name that exact commit/tree and verdict `pass`;
the records are committed unchanged in
`0d3755a2798cdfafd2a89ebaedcac40acc8c356a`.

`CYCLE3_GOAL.md` and the governing set are byte-for-byte equal in the worktree
and HEAD to goal commit
`6a2d09a444797bb0b73c94b259b1cbd826084129`, tree
`b6e1441af95f4e4a3cc17adeb1681e94d06a2557`. All three immutable
`goal-final-round-4` records name that exact commit/tree and verdict `pass`; the
records are committed unchanged in
`3ff24fcacd893869ddb717e6b130b528ff8fd931`.

### Launch provenance and platform

Static SHA-256 recomputation confirmed the approved checked-in snapshot:

| File | SHA-256 |
| --- | --- |
| `Software/decoders/sigrokdecode.py` | `385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a` |
| `Software/decoders/uart/__init__.py` | `351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f` |
| `Software/decoders/uart/pd.py` | `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc` |
| `Software/decoders/spi/__init__.py` | `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c` |
| `Software/decoders/spi/pd.py` | `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d` |
| `Software/decoders/i2c/__init__.py` | `37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f` |
| `Software/decoders/i2c/pd.py` | `b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305` |
| `Software/decoders/common/srdhelper/__init__.py` | `125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1` |
| `Software/decoders/common/srdhelper/mod.py` | `602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6` |

The preflight platform is macOS 15.7.7 build 24G720 with the existing project
environment's Python 3.12.13. The support and acceptance claim remains macOS
with Python 3.12 only. No other platform gains a support claim.

### Regression results and qualifications

All commands below were run without installing or updating dependencies:

| Command | Result |
| --- | --- |
| `bash -n Software/LogicAnalyzerPy/start_web.sh` | Exit 0; shell syntax passed. |
| `.venv/bin/python -m pytest -q tests/unit/test_cli.py tests/implementation/test_web_boundary.py tests/implementation/test_web_api.py` | Exit 0; 22 passed, no skips, 57 existing `aiohttp` `NotAppKeyWarning`/started-application state warnings. The warnings do not weaken or replace a mandatory gate. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b1.json` | Exit 0. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b2.json` | Exit 0. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b3.json` | Exit 0. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b4.json` | Exit 0. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b5.json` | Exit 0. |
| `.venv/bin/python scripts/validate_cycle2_evidence.py docs/evidence-manifest/cycle2-schema.json testdata/evidence/c2-b6.json` | Exit 0. |
| `git diff --check` | Exit 0 before this record; rerun after editing also passed. |

Static inspection found no .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or
`dotnet` reference in the current Python package's product source, production
or development dependency inputs/locks, tests, scripts, or Cycle 2 workflow.
No matching prohibited runtime was active in the inspected process-name list.
Preserved C# sources and metadata remain inert rollback/reference material and
were not included in that scoped absence claim.

### Decisions, future inputs, manifests, and prohibited actions

All ten Step 4 operator decisions remain the launch authority: exact checked-in
UART/SPI/I2C scope; typed library plus installed CLI only; host-owned closed
allowlist; single-use isolated subprocess; independently derived reviewed
fixtures as the sole oracle; staged numeric-limit approval; no production or
development/test dependency or execution path involving C#, .NET, pythonnet,
libsigrokdecode, `sigrok-cli`, or another reference host; preserved
provenance/notices with project/legal review; macOS-only support; and no
physical proof.

No additional operator input is required to launch. During C3-B1, the recorded
project/legal packaging review and the independently verified and accepted
numeric-ceiling/SPI-maximum proposal must exist before their owning gates can
pass; only then may the operator approve the exact numeric values. Later
hash-locked installation and hosted macOS CI require normal execution approval
when prompted. A changed fixture, method, worker model, environment class,
ceiling, objective, scope, trust boundary, platform, proof source, ownership,
or stopping condition requires the exact contract's reopening and review rules.

No `c3-b1.json` through `c3-b5.json` or other Cycle 3 evidence manifest exists.
Preparation did not execute decoder or C# code; build, install, import, invoke,
or depend on .NET, pythonnet, libsigrokdecode, `sigrok-cli`, or another reference
host; install dependencies; run a server, browser, network, USB/serial, live
capture, hardware, firmware, or non-macOS acceptance action; create Cycle 3
product/tests/fixtures/workflows/manifests; or begin later-cycle work.

### Exact approved launch command

```text
/goal Execute and verify Cycle 3 of the Python logic-analyzer rewrite by following CYCLE3_GOAL.md exactly and the approved contract commit ea83a403bb6f644d33069d3bebd41d5f1e0a60c0 / tree d9fb09345ab85580cd8c877745262d1b481e366f. Continue until all eighteen stopping conditions in CYCLE3_ORCHESTRATION.md have immutable proof and the directed terminal completion seal is committed, or the documented blocked condition is genuinely reached. Do not modify CYCLE3_GOAL.md or the approved governing contracts. Do not begin Cycle 4.
```

This record and the checked checklist do not invoke `/goal`.

## Preparation progress checklist

- [x] Step 1 — starting baseline reconciled in `cb877ed`; proposed technical
      and governance input baseline `c163a83`, tree `45556769`; post-completion
      launcher delta classified as included input without retroactive Cycle 2
      acceptance
- [x] Step 2 — technical roadmap reconciled in `cefb386`; accepted Cycle 2
      facts separated from proposed Cycle 3 and later-parity work
- [x] Step 3 — bounded discovery completed in `50a5e9f`; exact focused decoder
      inventory, integration seams, evidence gaps, alternatives, and proposed
      proof recorded without decoder execution
- [x] Step 4 — all ten operator decisions recorded in `eb5bc31`, including the
      prohibition on C# execution and on production or development/test use of
      .NET, pythonnet, or libsigrokdecode
- [x] Step 5 — narrow Cycle 3 contract surface settled in `50d4600`; staged
      API-edge fixtures and numeric thresholds assigned to explicit reviewed
      gates rather than implementation judgment
- [x] Step 6 — five batches, 26 requirement-to-proof mappings, and 18 stopping
      conditions settled in `faf81a3`, with fixture and threshold approval
      preceding public-host implementation
- [x] Step 7 — governing contracts and three-domain review framework drafted
      in proposed contract commit `8bd6ba0`; cross-document consistency audit
      passed after making review sets and repository instructions durable
- [x] Step 8 — governing contracts have three common-commit passes in
      `contract-final-round-5`, approving contract commit `ea83a40` / tree
      `d9fb093`; immutable approval records committed in `0d3755a`
- [x] Step 9 — durable goal has three common-commit passes in
      `goal-final-round-4`, approving goal commit `6a2d09a` / tree `b6e1441`;
      immutable approval records committed in `3ff24fc`
- [x] Step 10 — final launch preflight complete; all governing-file equality,
      approval, provenance, platform, baseline-regression, manifest-absence,
      operator-gate, and prohibited-action checks passed at the pre-record
      identity above; launch identity is the clean commit containing this record

Preparation status: **ready to launch Cycle 3 after the root orchestrator commits
this record and verifies that exact launch HEAD/tree and clean worktree**. The
goal has not been invoked.

## Completion rule

Preparation is complete only when every checklist item is checked, all required
artifacts and immutable review records are committed, the final repository state
is clean or explicitly qualified, and the operator has the exact approved
`/goal` command. Checking the list does not itself invoke the goal.

If any governing document changes after its final common-commit approval, apply
the review framework to determine whether fresh reviews are required. Never
edit an approved contract or goal silently to make the checklist appear
complete.
