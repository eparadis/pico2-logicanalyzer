# Python Rewrite Document Reviews

This directory contains durable, commit-anchored reviews of the Python logic-
analyzer rewrite process documents.

## Reviewed documents

- `ORCHESTRATION.md`
- `BATCH_EXECUTION.md`
- `Software/LogicAnalyzer/PYTHON_REWRITE_IMPLEMENTATION_PLAN.md`

The architectural review domains and three reviewer charters are defined in
`ARCHITECTURAL_DOMAINS.md`.

## Directory layout

```text
docs/rewrite-reviews/
├── README.md
├── ARCHITECTURAL_DOMAINS.md
├── round-1/
│   ├── reviewer-1-device-protocol-hardware.md
│   ├── reviewer-2-data-decoder-workflows.md
│   └── reviewer-3-delivery-orchestration.md
└── final/
    ├── reviewer-1-device-protocol-hardware.md
    ├── reviewer-2-data-decoder-workflows.md
    └── reviewer-3-delivery-orchestration.md
```

Additional rounds use `round-N/` without rewriting earlier records.

## Required review-record fields

Every review record contains:

- **Reviewer:** stable agent task name and domain role.
- **Reviewed commit:** full Git commit hash containing the exact documents
  reviewed.
- **UTC timestamp:** ISO-8601 time ending in `Z`.
- **Verdict:** exactly `pass` or `changes_required`.
- **Findings and disposition:** numbered findings with evidence, severity,
  requested resolution, and final disposition. A pass explicitly states that no
  findings remain.

Review records are committed after the commit they review. This avoids the
impossible requirement for a commit to contain a review file naming its own hash.
All three final review files must name the same reviewed commit.

## Change and re-review rule

- Mechanical corrections may be applied and reviewed again by the affected
  reviewer.
- Any substantive objective, scope, contract, authority, ownership, batch,
  validation, checkpoint, or stopping-condition change requires a new proposed
  commit and a fresh review by all three reviewers.
- Findings are never erased. Their original record remains and its disposition
  points to the resolving commit and final review round.
- Preparatory review is complete only when all findings have a disposition and
  all three final records say `pass` for one identical full commit hash.

## Review rounds

No review round has been accepted merely by creating this directory. Round
records and final status are added only after agents inspect an immutable
proposed commit.
