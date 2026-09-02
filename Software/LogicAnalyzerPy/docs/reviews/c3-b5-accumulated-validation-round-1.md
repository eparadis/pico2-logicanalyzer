# C3-B5 accumulated validation — round 1

- Orchestrator role: root accumulated-validation and hosted-dispatch owner.
- Timestamp: `2026-09-02T16:45:18Z`.
- Governing contract/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Corrected B5 implementation candidate/tree:
  `f8f78c89655011e3ee3e74559ff9886c93eac690` /
  `e6b5d5f0afaf3023ec398cb9c42c6d42d5a1790b`.
- Fresh verifier evidence commit/tree exercised by every accumulated gate:
  `2fb89fc8c36d93b4435032c07783532d6a8aa933` /
  `f155c06c8d61e9f454f2b7026afa0805999c4300`.
- Accepted B4 checkpoint: `9a8fc46ba4bc73cd007d678b85b6510bba0eeb87`.

## Clean locked local gate

The gate created fresh ignored `.tmp/c3-b5-clean-core` and
`.tmp/c3-b5-clean-web` environments from the accepted Darwin/x86_64 CPython
3.12.13 interpreter. `uv` installed `requirements-dev.lock` and
`requirements-web.lock` with required hashes and installed the core and web
source editable with dependency resolution disabled. Both clean environments
passed dependency consistency. The clean core environment passed Ruff, mypy
over 31 production source files, strict mypy over the installed public decode
consumer, and both installed CLI help surfaces.

The focused real hostile child gate passed three cases, including ignored
SIGTERM, forced kill/reap, distinct cleanup observation, and recovery. The
unchanged hosted-workflow partition then collected 1,528 non-hardware cases,
transparently deselected the governed 38 historical candidate-bound cases, and
finished with 1,483 passes and seven classified skips. The skips were two
sandbox loopback checks, four machine-local C2-B3 physical-artifact checks
whose sanitized checked-in evidence was exercised, and one hosted-only pinned
artifact availability check whose immutable URL/digest/extraction contract was
exercised statically and then actually provisioned by hosted CI. No mandatory
applicable case failed or was silently omitted.

The fixture generator `--check`, all four accepted C3 manifest schema checks,
and production asset-drift check passed. The frontend lock installed cleanly;
lint, typecheck, all five unit tests, the 29-module production build, and both
browser-smoke invocations passed (one bounded independent browser test and
three production shell/live tests). The local host had Node 26.7.0 and emitted
the expected engine warning for the exact Node 22.14.0 declaration; no local
claim transfers from that runtime. The mandatory hosted run below used and
passed exact Node 22.14.0.

## Final measurements, digests, and absence audits

The corrected packet records exactly three unrecorded warm-ups and 15 retained
runs, 18 launches total, with no retry or outlier deletion. Fresh verifier
reproduction independently observed the same counts and kept all 11 maxima
below the unchanged approved round-4 ceilings. The complete hostile process,
IPC, timeout, cancellation, terminate, kill, reap, recovery, output-bound, and
failure matrix passed locally and in the accumulated partition. The full gate
also exercised all three protocol conformance suites, cross-source identity,
public API/CLI, import/dependency/process absence, Cycle 1/2 regression,
license/resource, excluded-action, and rollback/support evidence.

A second root digest/schema pass produced:

- B1 manifest: `3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`;
- B2 manifest: `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`;
- B3 manifest: `4d17a6f0a1401799f1d7c0c65870744aada26eb2a3b1b8d5c723d447ceb4fac1`;
- B4 manifest: `699443c5ed9cb2ddd668b4b486311e251647cadf5aeb3a435263dd2597e0f72c`;
- B5 verifier test:
  `8bd21ab5ebd2f18bae0cae9ffdb702e97e5fb6e8638cfb1e66c0fa02be2f0b72`;
- B5 verifier review:
  `95157008368c868c66d89b239ff7e8f206564e70836ec6c404384c120c6e6389`;
- hosted workflow:
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`.

Together with fresh verification, the accumulated packet maps R1-R26 and
stopping conditions 1-17. No B5 manifest/checkpoint, completion proof, closure
verdict/record, seal, package build, publication, conveyance, excluded feature,
or Cycle 4 action existed or occurred during this gate.

## Exact hosted macOS PASS

Exact verifier evidence commit `2fb89fc8c36d93b4435032c07783532d6a8aa933`
was pushed to dedicated branch `cycle3-b5-ci-2fb89fc`. GitHub Actions run
`33655002746`, job `100331249147`, resolved that exact head on the required
`macos-15-intel` runner and concluded `success`. The job ran from
`2026-09-02T16:27:29Z` through `2026-09-02T16:44:30Z` with no failed or retried
step.

The runner guard, full-history checkout, pinned CPython 3.12.13 download and
SHA-256 verification, exact runtime identity, clean hash-locked core and web
installs, both hosted `pip check` gates, Ruff, production and strict consumer
mypy, hostile SIGTERM gate, complete non-hardware partition, CLI, exact Node
22.14.0 lock install, frontend lint/typecheck/unit tests/build, asset drift,
Chromium installation, and production browser smoke all passed.

Status polling reused the saved read-only `rtk curl` command class and stored
responses only under ignored `.tmp/c3-b5-ci/`. No workflow retry, new approval
class, artifact publication, or conveyance occurred.

## Disposition

Verdict: `pass`. The exact corrected B5 candidate, fresh verifier evidence,
complete accumulated local validation, and mandatory exact-candidate hosted
macOS gate are sufficient to advance to the distinct pre-manifest B5
acceptance review. They do not themselves accept B5 or authorize terminal
artifacts out of order.

The GPL-3.0-only engineering disposition and B1 rights-holder/qualified-counsel
limitation remain controlling before conveyance. No legal conclusion or
conveyance authority is added here. `APPROVAL_NEEDED`: none.
