# Final Review: Delivery, Verification, and Orchestration Contract

- **Reviewer:** `/root/review_delivery_contract` — Reviewer 3, Delivery,
  Verification, and Orchestration Contract
- **Reviewed commit:** `de93d47dabb64cfc0e014ce9eed807877b9f5b69`
- **UTC timestamp:** `2026-08-16T17:15:39Z`
- **Verdict:** `changes_required`

## Scope

I reviewed only the immutable tree at the full commit above, including the three
rewrite/process documents, architectural review framework, all Round 1 findings
and recorded dispositions, repository instructions, and the project/CI/platform
delivery sources required by the Reviewer 3 charter. I did not use uncommitted
working-tree changes as evidence.

The Cycle 1 objective remains bounded and hardware-first. Its nine stopping
items still map to the five batches as follows:

| Stop item | Batch/proof owner | Final review |
| --- | --- | --- |
| 1. Source install and CLI help | C1-B1 clean bootstrap, Linux/macOS CI, CLI help | Mapped, but the editable install can bypass the hash lock; Finding 1. |
| 2. Static/non-hardware suite | C1-B1 creates CI; every batch accumulates; C1-B5 reruns clean | Mapped, subject to Finding 1. |
| 3. Provenance-tagged protocol fixtures | C1-B1 fixtures/schema; C1-B2 goldens; C1-B3/B4 observations | Mapped with commit/tree, source category, verifier, and artifact digest. |
| 4. Fake/replay adverse behavior | C1-B2 fragmentation, malformed, timeout, disconnect, cleanup, recovery | Mapped and non-circular. |
| 5. Physical identity/capture/frequency | C1-B3 identity; C1-B4 selected-polarity capture; C1-B5 final smoke | Mapped and electrically gated. |
| 6. Deterministic CSV/replay | C1-B4 independent validation; C1-B5 final packet | Mapped and bounded. |
| 7. Cleanup, cancellation, and second capture | C1-B2 fake recovery; C1-B3 reopen; C1-B4 close; C1-B5 physical failure/recovery and two captures | Product behavior is mapped, but its authority and runnable physical proof are incomplete; Findings 2 and 3. |
| 8. Final progress/evidence record | Per-batch manifests and C1-B5 final packet against one candidate commit/tree | Mapped with reproducible provenance. |
| 9. C#/firmware rollback | Explicit exclusion throughout; C1-B5 confirmation | Mapped; existing sources and publish profiles remain untouched. |

## Round 1 finding dispositions

1. **CI edit authority — resolved.** `ORCHESTRATION.md:228-230` authorizes only
   `.github/workflows/logic-analyzer-python-cycle1.yml`, and C1-B1 owns that
   exact Linux/macOS workflow. Other workflow changes still need direction.
2. **Clean install and cross-platform validation — not fully resolved.** The
   documents now select Python 3.12, an exact virtual-environment sequence,
   hashed lock, and identical Linux/macOS jobs, but the editable-install command
   can still create an unpinned isolated build environment; Finding 1.
3. **Independent verification — resolved.** `BATCH_EXECUTION.md:57-61` records
   three identities, and `BATCH_EXECUTION.md:112-122` requires them to be
   distinct, forbids approval of authored behavior/fixtures, requires an exact
   verifier verdict and dispositions, and mandates reassignment rather than
   waiver.
4. **Evidence provenance — resolved.** `ORCHESTRATION.md:325-351` defines the
   checkpoint manifest fields and one-candidate-revision rule, while
   `BATCH_EXECUTION.md:503-521` carries commit/tree, environment, verifier,
   command, hardware, and manifest provenance into every checkpoint.
5. **Circular firmware prerequisite — resolved.** C1-B1 now needs only the
   operator's V2 assertion (`BATCH_EXECUTION.md:307-309`); C1-B3 resolves exact
   identity and pauses on mismatch without changing the baseline
   (`BATCH_EXECUTION.md:429-430`).
6. **Edge-polarity scope — resolved.** The objective and settled contract require
   both CLI polarities and independent fake tests; C1-B4 tests both
   (`BATCH_EXECUTION.md:462`), while hardware exercises and records at least the
   selected polarity.

## Findings and disposition

### 1. The editable install is not actually constrained by the hash-pinned dependency identity

- **Severity:** high
- **Evidence:** `ORCHESTRATION.md:285-286` first installs
  `requirements-dev.lock` with `--require-hashes`, then runs
  `pip install --no-deps -e .`. `ORCHESTRATION.md:293-296` says the lock pins all
  transitive dependencies and is the Cycle 1 dependency identity. A normal PEP
  517 editable install uses build isolation; `--no-deps` suppresses project
  runtime dependencies but does not prevent pip from creating an isolated build
  environment and downloading the `pyproject.toml` build-system requirements
  outside the hashed lock.
- **Impact:** A clean local or CI bootstrap can consume unrecorded, unhashed
  build packages and vary between Linux/macOS runs while still claiming that the
  lock is the complete dependency identity. This leaves Round 1 Finding 2 only
  partially resolved.
- **Requested resolution:** Put the editable-build requirements in the hashed
  lock and invoke the editable install with `--no-build-isolation --no-deps`, or
  use another exact command that proves no dependency or build requirement is
  resolved outside the lock. Apply the same command in both process documents
  and the C1-B1 CI acceptance contract.
- **Disposition:** open — substantive validation correction required; all three
  reviewers must review the new candidate commit.

### 2. The newly required cancellation byte is omitted from the hardware authority contract

- **Severity:** high
- **Evidence:** the objective and stopping condition now require transmitting
  the V2 `0xFF` recovery byte (`ORCHESTRATION.md:38-41,68-73,100-103`). However,
  the authorized hardware-send action mentions only identity and normal capture
  requests (`ORCHESTRATION.md:236-237`), and the batch-level authority checklist
  allows only an identity or characterized normal capture operation
  (`BATCH_EXECUTION.md:573`). The cancellation operation was added after Round 1
  but was not added to either authority gate.
- **Impact:** An agent following the higher-authority contract must either omit
  required C1-B5 recovery proof or send a device command not authorized by the
  hardware checklist. Treating it implicitly as capture cleanup defeats the
  purpose of enumerating the permitted wire operations.
- **Requested resolution:** Explicitly authorize exactly one characterized
  `0xFF` cancellation byte only for recovery from an in-flight Cycle 1 normal
  capture, followed by the settled drain/reopen/re-identification sequence. Add
  that case to the batch authority checklist while continuing to prohibit any
  public/general abort or other device-management operation.
- **Disposition:** open — substantive authority correction required; all three
  reviewers must review the new candidate commit.

### 3. The physical cancellation proof has no stable runnable interface

- **Severity:** high
- **Evidence:** stop item 7 requires physical no-trigger timeout or Ctrl-C
  recovery, and C1-B5 repeats that requirement at
  `BATCH_EXECUTION.md:485-486`. The settled CLI and canonical physical command
  expose only the ordinary `hardware-smoke` parameters
  (`BATCH_EXECUTION.md:262-265`; `ORCHESTRATION.md:305-312`): there is no
  recovery-test mode, cancel delay, expected timeout, or equivalent pytest
  interface. C1-B5 asks for a stable command (`BATCH_EXECUTION.md:487`) without
  requiring that it exercise the preceding recovery behavior.
- **Impact:** The most important failure-path hardware proof can degrade into an
  ad hoc manual Ctrl-C observation. Its command, timing, expected intermediate
  state, and pass/fail result cannot be reproduced from the evidence manifest,
  so stop item 7 is not fully verifiable even though the success capture is.
- **Requested resolution:** Settle a non-interactive opt-in interface, such as a
  separate `hardware-recovery-smoke` command or an explicit
  `hardware-smoke --exercise-cancel --cancel-after SECONDS` mode. Require it to
  use a deliberately absent trigger, send the characterized byte after a
  bounded delay, re-identify, perform the follow-up known-signal capture without
  a power cycle, and emit the same sanitized manifest fields and deterministic
  exit status as the ordinary hardware smoke. If a pytest interface is chosen,
  specify equivalent required parameters now.
- **Disposition:** open — substantive proof/CLI-contract correction required;
  all three reviewers must review the new candidate commit.

## Same-commit final-pass rule

This final review names exactly
`de93d47dabb64cfc0e014ce9eed807877b9f5b69`. The review protocol at
`docs/rewrite-reviews/README.md:60` still requires all three final records to say
`pass` for one identical full commit. This record is `changes_required`, so the
rule is not satisfied regardless of the other two verdicts. After the findings
above are resolved, all three reviewers must independently review the same new
immutable commit; this record cannot be treated as a pass or promoted to one.
