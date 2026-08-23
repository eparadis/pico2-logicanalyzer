# C2-B1 independent acceptance

- Lane / identity: acceptance / `cycle2-acceptance`
- Implementor identity: `cycle2-implementor-replacement-1`
- Verifier identity: `cycle2-verifier`
- Reviewed candidate commit: `51f925ec571fff960e69d4fd0b040976789c51f5`
- Reviewed candidate tree: `33c7a9da27e0754f726ee0675a0af0baff997d65`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `changes_required`

## Integrated-candidate and evidence audit

The assigned commit exists and resolves to the assigned tree. The public hosted
run `32620092590` identifies that exact commit and tree and completed with
`success`; its macOS job `97146855750` and Ubuntu job `97146855810` both identify
the exact commit and completed with `success`.

Independent verification record
`Software/LogicAnalyzerPy/docs/reviews/c2-b1-verification-round-13.md` has SHA-256
`382bd656296bde606ae8bb4974788121ecf8c2132946564689cb681ec2b35c39`, names the
same candidate, reports seven verifier tests passing, 224 accumulated
non-hardware tests passing, and one pinned-Node browser smoke passing, closes
`C2B1-V011`, and reports no open verifier finding. Earlier verifier records
retain the history and dispositions of `C2B1-V001` through `C2B1-V011` and
`C2B1-CI-MAC-001` rather than erasing them.

The orchestrator-supplied accumulated gate reports success for the clean Python
dependency check, Ruff, mypy over 19 source files, 223 tests with one explicitly
sandbox-only loopback skip, CLI help, frontend lint/typecheck/unit/build/browser,
deterministic assets, diff check, and clean candidate status. The hosted matrix
provides the required exact-candidate macOS and Linux qualification. These
results are accepted as accumulated evidence; acceptance did not rerun or
author them.

The candidate preserves the approved Cycle 2 orchestration and batch contracts,
does not alter firmware or the C# applications, replaces the single Cycle 1
workflow with one Cycle 2 matrix, and does not add a future-batch evidence
manifest. The B1 product delta is otherwise within the assigned foundation,
web-shell, dependency, workflow, contract-index, schema, validator, test, and
documentation paths. Later-batch product and physical stopping conditions
remain deferred to C2-B2 through C2-B6 and are not claimed by this review.

## Finding

### C2B1-A001 — Evidence validator accepts literal capability tokens and credentials

The governing evidence contract requires the validator to reject any field or
value containing an actual capability token, credential, or other secret, in
addition to serial paths, machine-local URLs, and user-home paths. The candidate
validator's `SECRET` expression recognizes only selected device paths,
loopback-local URLs, and `/Users` or `/home` paths. Its recursive free-text scan
therefore accepts a literal per-launch capability value such as a 43-character
URL-safe token, an authorization credential, or a cookie-bearing value when it
does not also contain one of the few recognized path/URL forms.

The implementation test exercises only an unknown top-level field containing a
loopback URL, so rejection occurs at the extra-field check. The independent
free-text test exercises only an IPv6 loopback URL. Neither test proves the
required capability-token or credential rejection. This leaves the B1 schema
and secret-scanner acceptance item incomplete and permits the future manifest
to validate while containing the exact class of secret the contract forbids.

Requested resolution: extend the validator's recursive secret detection with
bounded, explicit recognition of capability-cookie/token and credential-bearing
forms required by the contract, and add independent negative fixtures that put
those values in otherwise valid nested and free-text manifest fields. Preserve
the existing recursive field strictness and path/URL rejection. Record a new
immutable candidate and repeat independent verification, complete accumulated
validation, exact-candidate hosted CI, and acceptance.

Disposition: open; implementation owner correction required.

## Checkpoint and manifest disposition

The B1 manifest is correctly absent at acceptance time. The orchestrator must
not create `testdata/evidence/c2-b1.json`, append the checkpoint, or mark C2-B1
complete for this candidate because `C2B1-A001` is open. No B2-B6 manifest may
be created. After a corrected exact candidate passes all preceding gates and a
new acceptance verdict is `pass`, the orchestrator may atomically create only
the C2-B1 manifest, include the three distinct role identities and exact
candidate/tree, record the four lock/asset digests and exact hosted run/job
identities, validate it with the candidate validator, commit it, and only then
append the C2-B1 checkpoint record.

## Final state

`C2B1-A001` remains open. The exact candidate does not satisfy the complete
C2-B1 acceptance gate and cannot advance to checkpoint completion.
