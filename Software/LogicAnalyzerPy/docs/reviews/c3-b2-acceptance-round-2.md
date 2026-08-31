# C3-B2 independent acceptance — round 2

Identity: `c3-b2-private-host-acceptance-replacement-2`.

Verdict: `changes_required`.

## Immutable subject and ordering

This fresh acceptance audit is bound only to governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`; corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`; B1 manifest commit
`885be61a2bbea8bf5261b3983cbc79fedde0f315`; approved round-4 proposal and
decision `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0` and
`afd45856ee261158521b902dabdf926e5f1f922a`; exact B2 candidate
`959edf77945176b26c7cec86bcdd806d7e5769ea`, tree
`bca2c9d482e690d5bd5fa23822f96336bf6aa0b8`; fresh verifier pass
`ed39a653612b5e879aa08391fcb264f43f09a956`, tree
`dc94ec3af39363f6b6c9a41ce5f9a11b04bfe65e`; and replacement accumulated
record commit `9ed76a06dd50194fe1b9476877d0bca13f821143`.

The accumulated record is
`Software/LogicAnalyzerPy/docs/reviews/c3-b2-accumulated-validation-round-2.md`,
SHA-256 `fcdf4a7f3288a9f76bbc13d835dfa6fe1ec98754b184d60094da47f5d59808a3`.
The ancestry chain governing contract -> corrected B1 checkpoint -> candidate
-> verifier -> accumulation was independently confirmed. Candidate-to-verifier
changes are only progress plus the round-4 verifier test and record;
verifier-to-accumulation changes are only progress plus the accumulated record.
The candidate product and implementation-test bytes therefore remain bound to
the audited tree. Audit completed `2026-08-31T15:04:46Z` from branch
`python-rewrite` at `9ed76a0`, before creation of this owned record.

Predecessor candidate `d8e14bb`, its verifier/accumulation, failed acceptance
`6825e88`, and finding `C3B2-A001` remain immutable history and transfer no
result. The replacement implementor, fresh verifier, root accumulated owner,
and this acceptance identity are role-separated. This identity did not repair
or rerun the candidate.

## Acceptance audit

Finding `C3B2-A001` is closed in the replacement candidate. Request delivery is
now nonblocking and participates in the same selector lifecycle as response,
stdout, and stderr. The parent checks the inclusive deadline and cancellation
during partial delivery, closes the request descriptor at completion, maps
early close/exit/signal stably, prevents an early response from becoming
partial success, and converges on deterministic terminate/kill/close/reap.
Fresh independent tests exercise slow and never-reading children, cancellation
during partial delivery with hostile output, early close/exit/signal, readiness
anomalies, exact-child cleanup, and real subsequent decode recovery.

The verifier and accumulated record otherwise provide complete R6-R12/R22 B2
scope: immutable request/result/value models; host-owned closed decoder and
digest/import selection; pre-spawn capture, samplerate, mapping, option, and
request validation; frozen API-v3 primitives; one fresh single-use worker;
streaming versioned framed IPC; request/result projection and complete
declaration/record graph validation; all 18 approved hard product limits;
the separate 11 evidence-only macOS regression gates; typed failures;
cancellation/deadline/failure cleanup; atomic discard; and recovery after every
failure class. Static inspection found no request-, capture-, path-,
environment-, or dynamically discovered code selection and no public decoder
API/CLI or later-batch surface.

The complete Python/static/fixture/evidence gate records matching macOS,
Python, lock, project, fixture, manifest, and approved-limit identities;
`pip check`; whole-project Ruff; production and characterization mypy;
deterministic fixture/binding checks; installed CLI help; Cycle 2 and corrected
B1 evidence validation; and 938 passed nonhardware tests with only four
classified inherited optional physical-artifact skips and one governed
historical deselection. Frontend lint, type, unit, build, production-asset, and
unchanged browser regressions passed. The active-path audit found no prohibited
runtime/dependency/process use and no C#/.NET/reference decoder, hardware,
USB/serial, live capture, publication, browser product, B3+, Cycle 4, lock,
workflow, public API, or CLI action.

These passing areas cannot settle the performance finding below.

## Finding C3B2-A002 — conflicting valid performance observations leave the regression gate unpassed

Severity: blocking acceptance finding. Disposition: open; owning proof is the
B2 inherited performance regression gate.

The first exact Node 22 benchmark invocation completed the governed Playwright
test and produced a method-valid report, SHA-256
`e2602ab8c3dd02e56b1a8492bd85e12f5d6215e8254e2f9462ae5aed32ebd131`.
The unchanged checker correctly failed representative distinct-strobe p95
`140.5 ms` against the approved `116.7250000052154 ms` regression ceiling.
This was not a wrong executable, wrong method, launch failure, skipped test,
corrupt report, or non-candidate run.

With no byte, process, method, iteration, checker, or threshold change, root
then made one transparent quiescent rerun. That complete invocation passed and
produced report SHA-256
`460b28250af8d8d5fa899dd426c1bf6b61b1791444215cbc2c87a471d940f7b0`.
Preserving both reports is correct, but the record establishes no objective
reason that invalidates the first governed observation and no predeclared retry
or aggregation rule under which the second invocation replaces it. “Possible
scheduling” is explicitly not established as a root cause.

The governing procedure requires the complete accumulated gate to pass and
states that acceptance cannot waive a failed gate. Selecting the later pass
from two conflicting valid exact-method invocations would amount to such a
waiver and would make readiness depend on an undeclared retry policy. The
accepted report therefore does not by itself prove that this candidate meets
the inherited regression ceiling reliably enough for atomic manifest assembly.

Required disposition: preserve both reports; determine and document a
contract-consistent resolution for the valid failed observation without
weakening/rebasing the method, checker, iterations, or ceiling. If objective
evidence invalidates the first invocation, bind that evidence and rerun the
complete owning accumulated gate. If the observation reflects product or
environment behavior covered by the approved gate, correct it at the earliest
owner and repeat the required immutable candidate, verification, complete
accumulation, and acceptance sequence. A further unstructured rerun-until-pass
is not sufficient. No performance run was launched by this acceptance.

## Commands, cleanup, and authority

Read-only commands used through RTK: repository status; commit/tree/parent and
SHA-256 inspection; ancestry checks; candidate/descendant name-status and
source diffs; contract and immutable review inspection; static searches; and
process inventory. The accumulated gate was audited as the authoritative run;
no focused or performance rerun substituted for it. The full process inventory
completed, while a narrower `pgrep` query was unavailable because the local
process service could not supply a list; the accumulated record's successful
root cleanup inventory remains the owning cleanup evidence. No approval was
needed.

No manifest or checkpoint may be assembled while `C3B2-A002` is open. After a
fresh complete proof and independent acceptance pass, the sole next authority
is root B2 atomic manifest assembly, followed by distinct manifest verification,
joint manifest/verification-record commit, and only then the B2 checkpoint.
B3 remains unauthorized.

`changes_required`
