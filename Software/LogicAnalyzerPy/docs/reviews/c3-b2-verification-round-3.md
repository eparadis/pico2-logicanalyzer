# C3-B2 independent verification — round 3

Identity: `c3-b2-private-host-verifier-replacement-3`.

Verdict: `pass`.

## Immutable binding

This fresh verification is bound to exact implementation candidate
`d8e14bbe490035894f3103a1289b27464a89d0d6`, tree
`0ca3d0aec612183e3da01b24f341580743489d38`, under governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. Verification began at later
progress-only HEAD `939c1fe1bb411fb59ebd76bec8cf8ab0a0cdf1b9`; `git diff` from the candidate
showed only `docs/cycle-3-orchestration-progress.md`. No later product content
was used.

Independently recomputed candidate SHA-256 values were:

- private sources (`__init__`, `compat`, `host`, `identity`, `ipc`, `lifecycle`,
  `loader`, `model`, `worker`): respectively `168eca85174bb37975b131e0525e7dbf762e58337d690405be012a8f70208f57`,
  `763bdf54d636a98ff95ca1581184038cb24e04788acf85351897d813b214083a`,
  `b913febe115299aa761e913e9f953c9acfdcda6f076fdfaffa29e2a4ca9e3e71`,
  `06813d48c1708b264694488f06b4309f84b3c3a6b38a593a5c314dbdeca2d070`,
  `f3502eba02c66c957c6fc12a9d6c7e181d8c5e0c8e75ea75cb59c8027c460114`,
  `9ca920ea6e2a10222509e02aad58111c51b15439a2fec21c130b27a003eb3c79`,
  `5f2c47ece17df5b2e6c7682077952ba9e9d957fe9c0208929fc00d82d78aed83`,
  `19854e57491ff3b1271ed9e0012c878c0ed403b07f28bb5b17a9068d10e158e7`,
  and `9a01a2c03ecb255fb3dddc43036a8d4ba3b7b62923e4a687748a1db70ffdb160`;
- implementation test: `e3da648cb4dccbf97023a886a43a616c7249ccb614fc692cadde79e7508323c4`;
- immutable round-1 and round-2 verifier tests:
  `58e68082bbcc3f1e8c3d4c572722c08110573d18e11f65453c98ae13d88d76cb`
  and `1b5f547bf79c42bb00c3157e34be0b77f78afb5c1483e213ea1212771dd44757`.

The approved round-4 threshold proposal/approval, B1 evidence, progress,
`C3B2-II001`, `C3B2-V001`, `C3B2-V002`, all three implementation records, and
both immutable failed verifier records were reviewed. Prior verdicts did not
transfer.

## Independent derivation and attacks

The round-4 authority defines 18 product hard limits and 11 exact-candidate
macOS regression ceilings. Hard limits are inclusive product constraints and
their first overrun is rejected. Regression ceilings retain their exact
approved values but are observations, not real-time product failure policy.
Static inspection proved `_decode_with_factory` contains no regression-limit
lookup and the regression validator has exactly one occurrence: its own pure
definition. A hostile result with all four worker observations above their
ceilings still returned exact product success and delivered one per-call
observation; the separate gate rejected it. Every one of the 11 fields passed
at its exact ceiling and failed at value+1, and negative, bool, float, string,
and null mutations failed. Missing and extra construction are excluded by the
frozen dataclass; malformed/missing/extra worker metric maps failed atomic
`ipc`, preserved descriptor equality, and were followed by fresh success.

A real fixed worker independently produced a successful observation and passed
the separate gate: child import/load/decode `88,853,611 / 6,989,846 / 380,949`
ns, worker RSS `25,387,008` bytes, parent retained growth `176,128` bytes,
parent total/launch/reap `141,803,338 / 2,065,573 / 30,763` ns. A separate real
child ignored `SIGTERM`; test-only 50 ms deadline and 10 ms grace exercised
timeout, forced kill, close, and reap. All three cleanup measurements were
nonzero, passed the unchanged gate, leaked no descriptor, and did not replace
the product `timeout` failure. No observer is retained across calls and fresh
success follows hostile failures.

The new 32-row verifier suite independently attacks declaration identity and
description invariants, duplicate identifiers, emission-index ordering, exact
rational absolute and trigger-relative time, and the valid terminal capture
endpoint. Together with the immutable round-2 and exact implementation suites,
the graph matrix covers duplicate/gapped/reordered annotation, row, and binary
declarations; row references and duplicates; frozen registered output
kind/order/namespace; undeclared and cross-kind output IDs; annotation and
binary class bounds; metadata output/type/name/description; closed Python tag
values; negative/reversed/terminal/overrun coordinates; and all UART, SPI, and
I2C fixed decoders. Validation is generic frozen-lifecycle structure, not
fixture-record hardcoding. Every hostile result is rejected before return,
with atomic FD close/reap and fresh-worker recovery.

The accumulated 229 implementation rows, 8 immutable round-1 rows, and 35
immutable round-2 rows re-proved the full original matrix: repository identity,
hash/path/symlink/import-shadow protection; request mappings/options; IPC
version, framing, lengths, duplicates, nonfinite, partial and extra data; tags,
IDs, coordinates, nesting and diagnostics; exits, signals, exceptions, hangs,
address-space/recursion/stream/result floods; cancellation races; every hard
boundary and first overrun; worker bootstrap limit readback; no partial result,
poisoned state, or descriptor/child leak; and fresh success after every failure.
Static checks retain fixed `-I -B` package worker launch, closed environment,
FD-only IPC, pre-spawn digest/import verification, no request-selected path,
dynamic or in-process execution, no public API/CLI, no CPU limit, and no
prohibited dependency/runtime. The claim remains macOS/Python 3.12 only.

## Commands and results

- New verifier suite: exactly `32 passed in 4.24s`.
- Exact combined suite: exactly `304 passed in 38.00s` = 229 implementation +
  8 round 1 + 35 round 2 + 32 round 3.
- Ruff over nine private sources and all four B2 test paths: passed.
- strict mypy over nine private sources: `Success: no issues found in 9 source files`.
- `git diff --check`: passed.
- Separate live-success observation gate: passed with the exact values recorded
  above; separate real forced-cleanup gate is included in the new verifier and
  passed.

Direct lifecycle, descriptor equality, reap, and recovery evidence made a
process-list approval unnecessary. No network, hardware, browser, C#, external
decoder/runtime, dependency installation/change, public surface, B1, progress,
contract, implementation, prior evidence, B3+, or Cycle 4 path was modified.
Verifier ownership is limited to this record and
`tests/verification/test_c3_b2_private_host_round3.py`.
