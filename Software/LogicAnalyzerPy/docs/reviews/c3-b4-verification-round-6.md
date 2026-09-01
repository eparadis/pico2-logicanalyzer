# C3-B4 deterministic hosted harness verification, round 6

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-01T23:46:38Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Prior round-5 candidate/tree: `8cd114fa316f10db4d403197f3204771ccd36638` /
  `5b4c8f46ca626861a3191282aa5e2b282f806246`
- Tested candidate/tree: `db94d6b4a63aefbd1ec185a6492344be3df98842` /
  `26f3afe065e0202d9289e7ccb4a8fb47a9329a31`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round6.py`; neither changes product identity.
- Environment: Darwin 24.6.0 x86_64, Python 3.12.13; stable clean environments
  `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Scratch: only the repository-ignored `Software/LogicAnalyzerPy/.tmp/c3-b4-r6` was
  used. `PYTHONDONTWRITEBYTECODE=1` was set for verification Python commands.
- Hosted CI/network: neither was invoked. Exact-candidate hosted execution remains an
  orchestrator-owned accumulated gate and is not claimed here.

## Independent method and hosted control flow

The fresh verifier independently bound the candidate/tree/workflow SHA-256, parsed the
workflow, enumerated candidate-tree B2/B3/B4 modules, executed the focused forced-kill
node under inherited SIGTERM ignore, restored round-5 bytes after removing only the
authorized harness changes, and executed candidate-qualified collection plus the broad
retained partition.

The job has exact `PYTHONDONTWRITEBYTECODE: "1"` at job scope between `runs-on` and
`steps`, so it applies before checkout/setup and every Python invocation. The sole
`actions/checkout@v4` step has exact `fetch-depth: 0`; the local history audit also
resolved both the governing B1 and prior candidate commits.

The focused command selects exactly
`tests/implementation/test_c3_b2_private_host.py::test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure`.
It occurs once as an executable selector inside a subshell whose first operation is
`trap '' TERM`; Python and its child therefore inherit ignored SIGTERM. The selector
collects its exact `timeout` and `cancelled` parameter cases. An independent execution
using the hosted signal disposition returned `2 passed in 0.16s`.

Focused status is captured exactly once. The one broad command is lexically inside
`if [ "$focused_status" -eq 0 ]`; otherwise the final status is the focused status.
The focused selector appears a second and only second time as a broad deselection, so it
cannot execute twice. There is no retry. Both invocations append to the same single
initialized log; the same bounded sanitizer, report, annotation, and final status/exit
path runs after either result.

## Exact partition and retention

The 15 superseded-B1 ignores are unchanged from round 5, exact, ordered and unique.
The broad command contains these eight exact ordered unique node selectors:

1. `tests/implementation/test_cycle3_fixtures.py::test_cycle3_fixture_surface_is_present_and_rebuildable`
2. `tests/verification/test_c3_b4_public_round4.py::test_candidate_binding_and_exact_workflow_digest`
3. `tests/verification/test_c3_b4_public_round4.py::test_hosted_correction_preserves_every_prior_workflow_byte_and_gate_order`
4. `tests/implementation/test_c3_b2_private_host.py::test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure`
5. `tests/verification/test_c3_b4_public_round5.py::test_candidate_binding_and_exact_workflow_digest`
6. `tests/verification/test_c3_b4_public_round5.py::test_partition_has_exact_ordered_unique_ignores_and_deselections`
7. `tests/verification/test_c3_b4_public_round5.py::test_every_candidate_b2_b3_b4_module_is_retained`
8. `tests/verification/test_c3_b4_public_round5.py::test_partition_is_the_only_workflow_change_from_round4`

They expand to exactly nine cases because selector 4 has two parameters. Selectors 5-8
are precisely the four newly stale round-5 workflow identity/partition-byte assertions.
The other three round-5 tests—retained round-4 behavior/scope, runner guard, and product
drift exclusion—remain selected and passed. No round-5 module was ignored.

Candidate-qualified collection, excluding only this descendant round-6 evidence file,
was exactly `1430/1439 tests collected (9 deselected) in 0.91s`. The candidate contains
exactly 19 current B2/B3/B4 modules; none is ignored. The complete descendant broad run
collected 1,449, deselected exactly nine, and selected 1,440. Its result was
`1434 passed, 6 skipped, 9 deselected, 106 warnings in 239.55s`. The ten additional
passes are exactly this fresh verifier, so candidate-only arithmetic is 1,424 passes,
six classified skips, and nine deselections. The six skips were two sandbox-loopback
checks and four optional machine-local physical-artifact checks; no mandatory Cycle 3
or B2/B3/B4 check skipped.

## Commands and exact results

- Fresh round-6 verifier:
  `python -m pytest -q tests/verification/test_c3_b4_public_round6.py` —
  `10 passed in 0.53s`; no skip.
- Independent focused SIGTERM-inheritance proof — `2 passed in 0.16s`.
- Exact broad descendant partition — `1434 passed, 6 skipped, 9 deselected` in
  239.55 seconds. All retained B2/B3/B4 modules and all retained round-5 nodes passed.
- Prior C3B4-V001 through V004 passed within the broad run: exact immutable public
  classes/values and typed bytes; parent/worker tightening and containment; CSV exit 5
  versus replay exit 2 before read/mapping/launch; bounded UTF-8 diagnostics and exact
  installed CLI/API behavior.
- Focused Ruff over decode, host, CLI, workflow/B4 implementation, and all six B4
  verifier rounds: pass.
- Production mypy: `Success: no issues found in 31 source files`.
- Strict installed public consumer: `Success: no issues found in 1 source file`.
- Stable clean core and web `pip check`: `No broken requirements found` in both.
- Strict accepted-manifest validation for `c3-b1.json`, `c3-b2.json`, and `c3-b3.json`:
  all exited 0 without output.
- Frontend ESLint and TypeScript: pass; Vitest: three files/five tests passed; Vite:
  29 modules built; production asset drift check: pass.
- Installed outside-source `pico-la decode --help`: exact replay/CSV grammar,
  metadata/channel/option spellings, and UART/SPI/I2C choices retained.
- Resource checks reproduced exactly the accepted nine decoder snapshot files and all
  B1 SHA-256 values, without extra resource or root escape. No bytecode appeared in the
  closed `tools/cycle3_characterize` inventory.
- Prohibited-process audit returned no active .NET, pythonnet, `sigrok-cli`, or external
  libsigrokdecode process. Scoped product/workflow search returned no prohibited import,
  dependency, or command.
- `git diff --check`: pass.

The exact workflow SHA-256 is
`2b7c35159c9f6a6b521830290c4c4a4e17a1f7753911dad97c94161084256d82`.
After removing job-level no-bytecode, restoring the prior checkout step, and replacing
only the focused/broad harness segment with round 5, the workflow reproduced round 5
byte-for-byte. Thus exact `macos-15-intel`, the first pre-checkout `uname -m`/x86_64
guard, sanitizer, permissions, triggers, language versions, locked installs, static,
CLI, web/frontend, asset, Playwright/browser gates, and their ordering remain unchanged.

The candidate-relative path audit found only the workflow, its workflow regression,
and descendant B4 evidence. No B2/B3 product or test byte, decoder/API, fixture, limit,
threshold, dependency, lock, manifest, or contract changed. Preserved SHA-256 identities
include public decode `d5cd8b84...19db`, private host `b81d3c1b...15b6`, CLI
`c3acce49...3ddc`, typed vectors `b5cc317f...fbf`, round-4 thresholds
`98e48bb1...e3c`, option matrix `5d84b9d9...209`, dev lock `4efa0b1d...53`, web lock
`4b0feead...45`, and package metadata `ead05ffb...cf`.

Installed metadata remains `License-Expression: GPL-3.0-only`, exact four license-file
entries, numpy/pyserial base dependencies, and aiohttp conditional only on the web
extra. License and attribution digests remain unchanged.

## Findings and dispositions

1. **Hosted determinism correction — verified.** Full history, job-wide pre-Python
   bytecode suppression, and focused inherited-SIGTERM execution are exact.
2. **Execution accounting — verified.** The forced-kill node executes once in the
   focused phase, broad runs only on focused success, and broad deselects both already
   executed cases. Both phases share one bounded sanitized log/status path; no retry or
   alternate result path exists.
3. **Partition and retention — verified.** Fifteen ordered ignores and eight ordered
   selectors produce exactly nine deselected cases. Only four newly stale round-5 nodes
   were added; every other round-5 behavior/scope test and every current B2/B3/B4 module
   remains green.
4. **C3B4-V001 through V004 — remain resolved.** Public behavior, validation order,
   limits, canonical bytes, exit taxonomy, resource closure, and diagnostics pass.
5. **Scope and identity — preserved.** Runner/guard/gate ordering is exact and no
   product, fixture, threshold, limit, lock, manifest, or frontend drift was found.

## License, scope, and gate disposition

Exact package bytes, PEP 639 metadata, attribution, and notices remain consistent with
the accepted engineering disposition. This is not a legal conclusion: shim ownership,
the historical MIT label, and combined-work treatment still require counsel or
rights-holder confirmation before conveyance. This verifier built no wheel or sdist and
performed no upload, conveyance, publication, hardware, firmware, serial, live capture,
network access, or hosted CI dispatch.

The candidate is eligible for the orchestrator's accumulated gate and exact-candidate
hosted macOS dispatch. This verifier does not claim those future results, final
acceptance, manifest readiness, or checkpoint completion.

## Verdict

pass
