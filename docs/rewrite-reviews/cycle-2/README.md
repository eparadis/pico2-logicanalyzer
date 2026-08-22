# Cycle 2 rewrite document reviews

This directory stores immutable, commit-anchored reviews of:

- `CYCLE2_ORCHESTRATION.md`
- `CYCLE2_BATCH_EXECUTION.md`
- `Software/LogicAnalyzerPy/docs/cycle-2-discovery-review.md`

Reviewers use the domains in `ARCHITECTURAL_DOMAINS.md` and the record protocol
in the parent [`README.md`](../README.md).

Each round is stored in a new `round-N/` or `final-round-N/` directory. Every
record contains the reviewer identity and domain, exact reviewed commit, UTC
timestamp, verdict exactly `pass` or `changes_required`, and numbered findings
with evidence, requested resolution, and disposition. Findings are never erased.

Mechanical corrections may be re-reviewed by the affected reviewer. Any
substantive objective, scope, contract, authority, ownership, batch, validation,
security, checkpoint, or stopping-condition change requires a fresh review by
all three reviewers. Preparatory approval requires three final `pass` records
that name the same full commit.

