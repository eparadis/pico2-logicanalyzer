# C2-B6 implementation review — round 4

## Identity and immutable candidate

- Lane: implementation.
- Stable identity: `cycle2-b5-implementor-replacement-1`.
- Candidate commit: `2d5484a73d881496cdf5a35c799dfb01eedad229`.
- Candidate tree: `8c76bce79922263468cb6ceaa4f1990703a84bfc`.
- SHA-256 of the candidate's canonical Git commit object bytes:
  `36c8df2c8654f6bdf3a783944622e7840c27e5e93eef3d1e2e111876bbea308d`.
- Candidate state before this record: clean worktree. This record is a separate
  descendant artifact and is not part of the candidate.

## C2B6-A001 diagnosis and closure work

The first exact-candidate hosted run, `32669668507` / job `97268420731`, failed
in nonhardware pytest after setup, hash locks, dependency checking, Ruff, and
mypy passed. The sanitizer-bounded public annotation contained only the warning
tail, so the failing assertion was not visible. Exact local Python 3.12 with
`CI=true` passed, including 20 consecutive full stress runs: 7,580 tests passed
with 40 documented skips and no failure.

The workflow-only diagnostic correction added authenticated manual dispatch so
an exact ref can be rerun without manufacturing a product delta. Push and
pull-request path filters remain intact, the sole job remains hosted macOS, and
top-level permissions are explicitly limited to `contents: read`. A mandatory
invariant proves there is exactly one active workflow, manual dispatch is
present, both filtered triggers remain present, only the macOS job exists,
action pins and all Python/web/browser gates remain intact, the sanitizer
self-test remains intact, and no secret or privileged permission is used.

Hosted retry `32670834441` / job `97271331706` reproduced the same pytest
failure, with the warning-saturated tail again displacing the assertion. The
diagnostic command was therefore narrowed without changing selection or exit
semantics: pytest still runs the complete `not hardware` selection, but uses a
short traceback and suppresses warning bodies. The same bounded log, sanitizer,
annotation escaping, captured exit status, and nonzero propagation remain.
A forced representative pytest failure passed through that exact path with its
assertion marker visible, its sensitive sentinels redacted, and its exit status
still nonzero. The normal full suite remained green.

Run `32671167477` / job `97272128226` then exposed the actual cause: all four
tests in `test_c2_b3_physical_artifacts_blackbox.py` expected seven
machine-local C2-B3 capture/recovery files that are intentionally absent on a
clean hosted worker. This was an availability-classification defect, not a
physical-data or product failure.

The final narrow correction preserves every original physical assertion and
applies this policy:

- when no default machine-local artifacts are supplied, the four offline
  physical tests skip with an explicit documented reason;
- a partial default set fails;
- an explicitly supplied set with any missing member fails;
- a complete but corrupt set reaches digest verification and fails; and
- a complete set runs all archive, digest, dtype, width, mapping, mask,
  frequency, high-bit, CSV, and recovery assertions unchanged.

Regression tests cover absent-default, partial-default, explicit-missing,
complete, and complete-corrupt cases. The checked-in sanitized C2-B3 evidence
and schema validator remain mandatory nonhardware coverage. No raw capture was
copied into Git and the offline tests were not relabeled as hardware.

## Validation and hosted result

With the complete expected local artifact set, all four original physical tests
passed. Final local `CI=true` nonhardware validation reported 383 passed, 2
documented sandbox-loopback skips, and 106 warnings. The availability
regressions reported 3 passed. Ruff, strict mypy over 21 source files,
`pip check`, YAML parsing, the workflow invariant, and `git diff --check`
passed. The earlier 20-run stress evidence remained unchanged and relevant to
the nondeterminism diagnosis.

The exact final candidate passed hosted macOS run `32671356406`, job
`97272584254`. Every step completed successfully: checkout and pinned runtime
setup, clean environments, hash-locked installs, dependency checks, Ruff,
mypy, complete nonhardware pytest, CLI, locked Node install, frontend lint,
typecheck and unit tests, deterministic production build and asset check,
Chromium installation, and the production browser workflow. This is the
required exact-tree hosted success for C2B6-A001.

## Security and scope

The workflow exposes no secret, token, raw device identity, machine-local
location, or capture path. Manual dispatch accepts no inputs. Repository access
is explicitly read-only. The sanitizer, its hostile self-test, bounded output,
and annotation escaping remain active. No device access occurs in hosted CI.

No runtime, driver, API, viewer, generated API, asset, threshold, governing
contract, physical evidence, firmware, wiring, persistent state, public
service, packaging, .NET surface, or Cycle 3 work changed.

Relevant SHA-256 identities:

- hosted workflow:
  `ab0809523370ecfe308fe733be011c83f926315eeca12e7a0d3ab294b357ea22`;
- workflow invariant test:
  `434d7869c8ee94207afb79fc0dd7e44c0a0390eb005d790f4f8289443facf241`;
- guarded physical-artifact verifier:
  `94d794349fff256862c82e513e0e0e7d736fed46eafaf2aad2d1b65ea36f83ac`;
- artifact-availability regression tests:
  `852bfe65f98bfe00e3a8fb2e16aacf8dcdee27aea0cbb1f50ab96c7d73d536b2`;
- unchanged checked-in sanitized C2-B3 evidence:
  `9db03e119c6cacb40e87ef61d8f7ef1e24692ea45527f5e331e2103ecc59ff1b`;
  and
- unchanged evidence validator:
  `d2bbddea9e1bb43f703e5873aa38a1f854b3a702e27b9808c63e381c57856ff0`.

## Implementation verdict and Git handoff

Implementation verdict: `pass`; the implementation/integration work required
to close C2B6-A001 is complete for immutable candidate
`2d5484a73d881496cdf5a35c799dfb01eedad229`, tree
`8c76bce79922263468cb6ceaa4f1990703a84bfc`, with exact-candidate hosted macOS
success.

The root orchestrator should stage and commit only
`Software/LogicAnalyzerPy/docs/reviews/c2-b6-implementation-round-4.md` as a
separate descendant record, calculate the record's SHA-256, and submit the
exact candidate—not the descendant record commit—to fresh independent review.
