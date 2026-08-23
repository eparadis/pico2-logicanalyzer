# C2-B1 independent verification, round 14

- Lane / identity: verifier / `cycle2-verifier`
- Implementor identity: `cycle2-implementor-replacement-1`
- Reviewed candidate commit: `dbd68260d030273916240ffe64d622f0d79824d0`
- Reviewed candidate tree: `c0d8ac1c16233ca168d7efe915ced3865497a0df`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `changes_required`

## Candidate and acceptance-finding audit

The checked-out commit/tree exactly match the assignment and the starting
worktree was clean. Relative to candidate `51f925ec571fff960e69d4fd0b040976789c51f5`,
the executable delta is limited to the Cycle 2 evidence validator and its
implementation tests. The other added paths are immutable verifier/acceptance
records.

### C2B1-A001 — closed for literal-secret rejection

Independent otherwise-valid manifests placed hostile values in recursively
scanned free text. The validator rejected all five fixed classes tested:

- a standalone 43-character URL-safe capability shape;
- `Authorization: Bearer` credential syntax;
- a cookie-bearing capability value;
- an `api_key=` credential; and
- a `password:` credential.

The unchanged valid baseline manifest was accepted. Existing recursive field,
path/URL, device-path, digest, role, timestamp, and schema checks remain active.
The focused implementation/verifier suite passed 11/11.

Disposition: closed as originally reported; literal secret-bearing manifests
are no longer accepted.

## New finding

### C2B1-V012 — Credential keyword rule rejects ordinary non-secret evidence prose

The new expression permits whitespace alone as the delimiter between any of
`authorization`, `cookie`, `token`, `api key`, or `password` and the next
non-space word. Consequently ordinary security evidence is classified as a
secret. An independently constructed otherwise-valid manifest with the benign
finding text:

```text
Capability token redaction verified with fixed hostile fixtures
```

was rejected as `invalid or secret-bearing findings[0]`. This text contains no
credential value and is exactly the kind of finding/decision prose a Cycle 2
manifest may need to record. Similar false positives follow for phrases such as
`authorization required` or `password handling verified`.

The implementation tests do not expose this defect because they test only
secret-positive cases. They also place the same secret in both a nested source
artifact and free-text finding in one manifest, so the first rejection does not
independently prove which recursive location caused it.

Requested resolution: retain standalone 43-character capability detection and
use explicit credential syntax rather than arbitrary whitespace for generic
keywords—for example `=` or `:` for named token/API-key/password fields,
`Bearer`/`Basic` authorization schemes with a following value, and cookie
header/capability-cookie forms. Add separate otherwise-valid negative manifests
for each recursive location and positive manifests containing benign security
prose such as `token redaction verified`, `authorization required`, and
`password handling verified`.

Disposition: open; validator/implementation owner.

## Independent accumulated evidence

- Fixed hostile-secret probe: 5/5 rejected; valid baseline accepted.
- Benign security-prose probe: rejected unexpectedly; reproduced C2B1-V012.
- Focused evidence implementation plus verifier tests: 11 passed in 0.95
  seconds, exit 0.
- Ruff over `Software/LogicAnalyzerPy`: pass, exit 0.
- mypy: pass over 19 source files, exit 0.
- Full non-hardware pytest: 227 passed in 1.53 seconds, exit 0.
- Pinned Node v22.14.0 installed-Chromium browser smoke: 1 passed in 1.5
  seconds, exit 0.
- A prior combined Ruff/mypy/pytest invocation produced no attributable result
  and was externally interrupted after 1058.3 seconds; the three commands were
  then rerun separately with the results above.

## Final finding state

C2B1-A001 is closed for actual literal-secret rejection. C2B1-V012 remains
open because the validator is not false-positive-safe for valid evidence and
therefore cannot yet be accepted as the frozen evidence gate.
