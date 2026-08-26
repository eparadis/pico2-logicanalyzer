# Cycle 3 document reviews

This directory stores immutable, commit-anchored architectural reviews for the
two preparation approval gates defined by `CYCLE3_PREPARATION.md`. It defines
review mechanics only. It does not approve a draft, authorize Cycle 3
implementation or decoder execution, install or permit a dependency, create
execution evidence, or start the durable goal.

Reviewers use the domains in `ARCHITECTURAL_DOMAINS.md` and the repository-wide
record protocol in the parent [`README.md`](../README.md). The stricter Cycle 3
rules in this file apply where they add detail.

## Exact complete document sets

Every reviewer inspects every file in the applicable set at one immutable Git
commit and tree. Reviewing only the files associated with the reviewer's
primary domain is invalid.

The Step 8 **contract-review set** is exactly:

- `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`;
- `Software/LogicAnalyzerPy/docs/cycle-3-discovery-review.md`;
- `CYCLE3_ORCHESTRATION.md`;
- `CYCLE3_BATCH_EXECUTION.md`;
- `docs/rewrite-reviews/cycle-3/README.md`; and
- `docs/rewrite-reviews/cycle-3/ARCHITECTURAL_DOMAINS.md`.

The Step 9 **goal-review set** is exactly the complete contract-review set plus
`CYCLE3_GOAL.md`. The goal review checks the whole set again; a Step 8 pass is
not a review of the later goal commit and cannot be transferred to Step 9.

A review record itself is committed after the candidate it names, because a
commit cannot contain a record naming its own identity. Review-record commits
are not members of the reviewed document set. `CYCLE3_PREPARATION.md`, earlier
Cycle 1/Cycle 2 contracts, completion evidence, manifests, repository
instructions, and source may be required inspection evidence, but they are not
silently added to these two exact common-commit sets.

## Directory and round naming

Contract reviews use new directories named:

```text
contract-round-N/
contract-final-round-N/
```

Goal reviews use new directories named:

```text
goal-round-N/
goal-final-round-N/
```

`N` increases independently within the contract and goal sequences. A normal
round is used while findings are being resolved. A final round is an intended
approval attempt; the name does not confer approval. A final directory that is
incomplete or contains any `changes_required` verdict remains a failed or
superseded attempt. The next attempt uses a new, higher-numbered directory.

Every complete round contains exactly one record for each charter:

```text
reviewer-1-decoder-api-runtime-fixtures.md
reviewer-2-capture-annotation-cli-workflows.md
reviewer-3-security-delivery-orchestration.md
```

Review files and directories are append-only history. They are never renamed,
replaced, deleted, or edited to make an earlier round appear successful.

## Required immutable review record

Each review record must contain:

- **Gate and round:** `contract` or `goal`, plus the exact round directory.
- **Reviewer:** stable agent task identity and charter name. The three records
  must name three independent reviewer identities.
- **Reviewed commit:** the full 40-character Git commit hash containing the
  exact complete document set.
- **Reviewed tree:** the full 40-character tree hash for that commit.
- **Set-completeness declaration:** an explicit statement that every path in
  the applicable exact set was inspected at that commit, with no worktree file
  substituted.
- **UTC timestamp:** ISO-8601 time ending in `Z`.
- **Verdict:** exactly `pass` or `changes_required`.
- **Findings and dispositions:** numbered findings with severity, exact
  document/source evidence, the violated invariant or cross-domain seam,
  requested resolution, and current disposition. A pass explicitly states
  that no finding remains open.
- **Prior-round reconciliation:** for each earlier finding in the same gate and
  domain, the earlier record/finding identifier, resolving commit and evidence,
  and disposition. An unresolved earlier finding requires
  `changes_required`.

The named commit and tree must exist and agree. All three records in one round
must name the same commit, tree, gate, and exact set. A detached note, chat
message, summary, review of staged/uncommitted content, short hash alone, or
record lacking a required field is not a pass.

## Finding resolution and substantive re-review

The original finding remains immutable and open in its original record. A
resolution changes the candidate documents in a new commit; the later review
record documents the disposition and points back to the original finding.
No finding is erased, silently waived, or marked resolved merely by an
orchestrator assertion.

A purely mechanical correction may be re-reviewed by the affected reviewer
only when it cannot alter meaning, authority, scope, ordering, proof, or any
cross-domain handoff. Examples are spelling or a broken link whose one intended
target is already unambiguous. The record must justify why the change is
mechanical.

Any substantive change requires a fresh complete-set review by all three
reviewers on one new common commit and tree. Substantive changes include any
change to:

- objective, required or excluded scope, authority, trust, platform, or
  stopping condition;
- decoder identity, provenance, license, import boundary, API-v3 semantics, or
  authoritative fixture content;
- product interface, capture/annotation/result semantics, library/CLI surface,
  API/browser exclusion, or deterministic ordering/serialization;
- process isolation, IPC, cancellation, failure handling, resource or
  performance method/value, dependency prohibition, or security claim;
- batch boundaries, role/requirement ownership, candidate order, accumulated
  validation, evidence, manifest/checkpoint mechanics, operator gates, or CI;
  or
- any resolution that changes a promised input/output at a cross-domain seam.

When classification is uncertain, treat the change as substantive. Passes may
never be mixed across commits, trees, rounds, gates, or reviewer identities.

## Approval conditions

Step 8 contract approval exists only when the latest complete
`contract-final-round-N/` contains three verdicts exactly `pass`, all naming one
identical full commit and tree for the complete contract-review set, and every
finding from every earlier contract round has a durable disposition.

Step 9 goal approval exists only when the latest complete
`goal-final-round-N/` independently meets the same rule for one identical full
commit and tree containing the complete goal-review set. Goal approval does not
retroactively alter the Step 8 approved contract identity; if adding or fixing
the goal substantively changes another reviewed document, Step 8 must first be
reopened and passed on the changed contract set.

No review may rely on executing C#, .NET, pythonnet, libsigrokdecode,
`sigrok-cli`, an external/reference decoder runtime, or any other prohibited
reference executable. C# and upstream material are static code-inspection
references only. Independently derived, reviewed fixtures are the sole oracle
for expected decoder outputs. The prohibition on .NET, pythonnet, and
libsigrokdecode applies to production, development, test, fixture-generation,
verification, performance, acceptance, and review dependencies and execution.

Creating this framework or any review directory grants no implementation,
dependency, decoder-execution, hardware, firmware, serial, browser, publication,
or `/goal` authority.
