# Round 1 Review: Delivery, Verification, and Orchestration Contract

- **Reviewer:** `/root/review_delivery_contract` — Reviewer 3, Delivery,
  Verification, and Orchestration Contract
- **Reviewed commit:** `1a6fb5aed5f0714368f3bf97af04c1789b8f9dc9`
- **UTC timestamp:** `2026-08-16T15:00:21Z`
- **Verdict:** `changes_required`

## Scope

I reviewed the immutable tree at the commit above, not working-tree changes. The
review covered `ORCHESTRATION.md`, `BATCH_EXECUTION.md`,
`Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`, the review
framework under `docs/rewrite-reviews/`, repository instructions (including
`/Users/ed/.codex/RTK.md`), the existing solution/project/publish configuration,
the absence of a Python project and CI workflows at this commit, platform
discovery in `SharedDriver/DeviceDetector.cs`, and the existing Python bootstrap
in `LogicAnalyzer/SigrokDecoderBridge/PythonInstallation.cs`.

The proposed work has one appropriately bounded Cycle 1 objective and an
objective physical-board stop. Discovery has four explicit outcomes, later work
is deferred, dangerous device/repository operations cross authority gates, and
the five batches form a useful hardware-first path. The following findings are
limited to delivery, proof, ownership, and contract seams; protocol and
capture/data semantics remain with Reviewers 1 and 2.

### Stopping-condition coverage check

| Stop item | Intended owner and proof | Review result |
| --- | --- | --- |
| 1. Install and CLI help | C1-B1 clean source install and CLI-help check | Proof command/environment is not yet defined; Finding 2. |
| 2. Static and non-hardware checks | C1-B1 establishes tools/CI; every batch and C1-B5 rerun the canonical suite | CI write authority conflicts with the top-level contract; Finding 1. Bootstrap and cross-platform reproducibility are unresolved; Finding 2. |
| 3. Provenance-tagged V2 fixtures | C1-B1 golden evidence; C1-B2 request/parser tests; C1-B3/B4 hardware confirmation | Evidence provenance has no minimum schema or immutable tested revision; Finding 4. |
| 4. Fake/replay adverse behavior | C1-B2 focused and accumulated tests | Mapped and non-circular. |
| 5. Physical identity/capture/frequency | C1-B3 identity; C1-B4 capture; C1-B5 stable hardware smoke | The B1 firmware prerequisite can make reaching B3 circular; Finding 5. Edge scope is inconsistent; Finding 6. |
| 6. Deterministic CSV/replay | C1-B4 independent reload/determinism tests; C1-B5 final packet | Mapped; provenance of final proof is covered by Finding 4. |
| 7. Cleanup and second capture | C1-B2/B3 negative cleanup; C1-B4 close; C1-B5 failure and two-capture proof | Mapped, but verifier independence is not enforceable as written; Finding 3. |
| 8. Final progress record | C1-B5 checkpoint and final review packet | Content is listed, but exact reproducible provenance is incomplete; Finding 4. |
| 9. C#/firmware rollback | Cycle 1 exclusions plus C1-B5 rollback confirmation | Mapped and non-circular. Existing `.sln`, `.csproj`, and Linux/macOS publish profiles provide a concrete comparison path. |

## Findings and disposition

### 1. C1-B1 requires a CI edit that the higher-authority contract does not authorize

- **Severity:** high
- **Evidence:** `BATCH_EXECUTION.md:194-195` requires Linux/macOS non-hardware
  CI in C1-B1. `ORCHESTRATION.md:205-206` authorizes creation and editing only
  under `Software/LogicAnalyzerPy/` (apart from the separately constrained
  roadmap update). At the reviewed commit, `.github/` contains only
  `.github/FUNDING.yml`; no workflow exists that could merely be configured in
  place.
- **Impact:** An implementation agent must either violate the top-level
  authority boundary, omit a C1-B1 acceptance deliverable, or pause for an
  approval that the batch does not identify. Because `ORCHESTRATION.md` has
  higher authority, the batch cannot resolve this locally.
- **Requested resolution:** Amend the top-level authority gate to permit a
  narrowly named Cycle 1 workflow under `.github/workflows/` and make that path
  part of C1-B1 ownership, or explicitly defer repository-hosted CI and replace
  it with an equally concrete Linux/macOS proof mechanism. Retain the rule that
  workflow changes outside the Cycle 1 validation surface need user direction.
- **Disposition:** open — substantive authority/batch resolution required; all
  three reviewers must review the resolving commit.

### 2. The install and Linux/macOS validation proof is not runnable from a clean checkout

- **Severity:** high
- **Evidence:** stopping condition 1 at `ORCHESTRATION.md:50-51` requires a
  source install, while the canonical block at `ORCHESTRATION.md:256-263` starts
  after `cd Software/LogicAnalyzerPy` and invokes an unspecified `python`
  environment. C1-B1 acceptance at `BATCH_EXECUTION.md:219-222` says that a
  clean source install and tools succeed, but provides neither an install
  command nor an environment/bootstrap command. The reviewed commit contains no
  `Software/LogicAnalyzerPy/`, Python lock/config file, or CI workflow from
  which those commands can be inferred. The existing Python discovery code is
  application-embedding logic, not a Python 3.12 project bootstrap
  (`Software/LogicAnalyzer/LogicAnalyzer/SigrokDecoderBridge/PythonInstallation.cs`).
- **Impact:** Different agents or CI jobs can install different dependency sets,
  run a system `python` of the wrong version, or claim stop item 1 without
  reproducing it on Linux and macOS. The four canonical post-install commands
  do not themselves prove installation.
- **Requested resolution:** Choose and document one exact clean-checkout
  bootstrap/install sequence for Python 3.12 and one exact validation sequence
  that uses the created environment (for example, a checked-in locked `uv`
  workflow or a version-pinned virtualenv plus project dev extra). Require C1-B1
  to run the same sequence in explicit Linux and macOS CI jobs, including the
  CLI-help command, and require later checkpoints to cite the corresponding
  local run or CI run. If dependency locking is intentionally deferred, define
  the exact bounded substitute and its reproducibility limits now.
- **Disposition:** open — substantive validation/acceptance resolution required;
  all three reviewers must review the resolving commit.

### 3. Independent verification is encouraged but separation of duties is not required or recorded

- **Severity:** high
- **Evidence:** `BATCH_EXECUTION.md:98-110` defines implementation,
  verification, and orchestration roles, but only prohibits the two agents from
  editing the same test file. The implementation agent is expressly expected to
  add focused tests, and C1-B5 merely calls for an “Independent review” at
  `BATCH_EXECUTION.md:334-335`. The checkpoint template does not name the
  implementation and verification agents. Nothing prevents the author of a
  behavior from later serving as its independent verifier or the integrator
  from treating self-review as independent approval.
- **Impact:** A checkpoint can satisfy the literal procedure without a reviewer
  independently deriving and approving its acceptance evidence. This violates
  the Reviewer 3 invariant that verification must not approve its own
  implementation.
- **Requested resolution:** Require each batch manifest and checkpoint to name
  stable implementation, verification, and acceptance identities. State that a
  verifier may not verify production behavior or fixtures it implemented and
  may not silently rewrite expected results; its handoff must give an explicit
  `pass` or `changes_required`. Require the orchestrator to record disposition
  of every verification finding before acceptance. Define a bounded reassignment
  procedure when staffing makes the original separation impossible.
- **Disposition:** open — substantive ownership/checkpoint resolution required;
  all three reviewers must review the resolving commit.

### 4. Checkpoint evidence is not anchored strongly enough to reproduce the claimed result

- **Severity:** high
- **Evidence:** stopping condition 8 at `ORCHESTRATION.md:67-69` asks for exact
  commands and results, while `ORCHESTRATION.md:300-302` prohibits committing
  actual machine-specific serial paths. The completion summary permits
  uncommitted changes (`ORCHESTRATION.md:330`). The checkpoint template in
  `BATCH_EXECUTION.md` records a broad “Repository state” but no exact tested
  commit/tree, OS, Python/dependency identity, exit status, verifier identity,
  artifact digest, or distinction between source-derived and physically
  observed evidence. Hardware artifacts may be summarized, so a prose success
  assertion can be the only durable evidence. The review framework correctly
  anchors document reviews to commits, but the execution evidence has no
  equivalent anchor.
- **Impact:** A final packet can combine commands from one revision, artifacts
  from another, and uncommitted fixes; it can also be impossible to distinguish
  a sanitized command template from the command actually run. That makes the
  stopping proof non-reproducible and weakens fixture provenance.
- **Requested resolution:** Define a small checked-in evidence manifest and add
  required checkpoint fields for tested full commit (or immutable tree hash),
  clean/qualified worktree state, UTC time, OS/architecture, Python and locked
  dependency identity, normalized command plus exit status, verifier identity,
  fixture source category, and artifact path/digest. For hardware, require
  board/firmware identity, all non-sensitive signal/capture parameters, and a
  sanitized port placeholder while explicitly recording that the real port was
  supplied. Require the final accumulated and hardware proofs to run against
  one identified candidate revision; enumerate unrelated excluded changes
  rather than allowing implementation changes to remain ambiguous.
- **Disposition:** open — substantive proof/checkpoint resolution required; all
  three reviewers must review the resolving commit.

### 5. The target-firmware prerequisite can block the discovery step needed to settle it

- **Severity:** medium
- **Evidence:** `ORCHESTRATION.md:111-125` allows an uncertainty to be resolved
  by bounded board experiment and says unavailable input pauses only the
  affected path. In contrast, C1-B1 requires “known target board/firmware” at
  `BATCH_EXECUTION.md:187-188`, while the first planned physical identity read
  is C1-B3. The goal preconditions at `ORCHESTRATION.md:92-94` allow either a
  supported V2 analyzer or its exact reported firmware identity, but “known” is
  not defined at the B1 gate.
- **Impact:** An orchestrator could interpret exact identity as a prerequisite
  to scaffold/codec work, yet exact identity can only be obtained after that
  work. Conversely, it could accept an unsupported board based on an unrecorded
  assumption. This is a circular or non-verifiable batch boundary.
- **Requested resolution:** Define B1's prerequisite as an operator assertion
  and source baseline for a V2 analyzer, explicitly allowing exact identity to
  remain an open, provenance-recorded uncertainty. Make C1-B3 the required
  checkpoint that resolves the exact identity; a mismatch must enter the
  documented authority/input-required path rather than being normalized by
  changing the baseline.
- **Disposition:** open — substantive prerequisite/discovery resolution
  required; all three reviewers must review the resolving commit.

### 6. The objective does not settle whether Cycle 1 implements one edge polarity or both

- **Severity:** medium
- **Evidence:** the durable objective says “rising or falling” at
  `ORCHESTRATION.md:37`, and stopping item 5 checks the singular operator-chosen
  edge polarity. C1-B4 nevertheless requires encoding/sending rising **and**
  falling requests at `BATCH_EXECUTION.md:301`, with fake cases for both. The
  scope list similarly says a “selected rising/falling” edge rather than whether
  both are product capabilities.
- **Impact:** One agent can implement only the selected polarity and reasonably
  claim the objective, while another can reject the batch because both fixture
  paths are required. The ambiguity changes Cycle 1 product scope and physical
  proof expectations.
- **Requested resolution:** State explicitly whether both rising and falling
  are required CLI capabilities. To preserve the current narrow useful slice,
  the recommended contract is: implement and independently fake-test both
  polarities, while the hardware smoke must exercise at least the one
  operator-selected polarity and record the untested polarity as a hardware
  limitation. If both physical polarities are required, say so in stopping item
  5 and the operator prerequisites instead.
- **Disposition:** open — substantive objective/scope clarification required;
  all three reviewers must review the resolving commit.

## Same-commit final-pass rule

This review names the requested full commit
`1a6fb5aed5f0714368f3bf97af04c1789b8f9dc9`. At that commit,
`docs/rewrite-reviews/final/` does not exist and therefore the all-three final
pass rule is **not yet satisfied**, as expected for Round 1. The rule itself is
stated consistently in `docs/rewrite-reviews/README.md:60` and the pre-goal
checklist in `ORCHESTRATION.md`. After the substantive findings above are
resolved in a new proposed commit, all three reviewers must review that same
full commit; no final record may be promoted from this Round 1 review.
