# C3-B4 evidence-backed SIGTERM isolation verification, round 8

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-02T01:09:35Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Failed hosted evidence: `b2b7fa24d0b90c96fb8da7295b861eb8021102f0`
- Prior round-7 candidate/tree: `f3565c11c1d7ea4351349d141401c6f98ba3940d` /
  `e0346acdcc6ea64369ba612237eb583e66311bf8`
- Tested candidate/tree: `fefc3307c2de0a680bf44cdcbbabf2e804495a4a` /
  `489ae588679ea4306c49304c0c1e40733b9f7938`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round8.py`; neither changes product identity.
- Environment: Darwin 24.6.0 x86_64, Python 3.12.13; stable clean environments
  `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Scratch: only repository-ignored `Software/LogicAnalyzerPy/.tmp/c3-b4-r8` was used;
  verification Python commands set `PYTHONDONTWRITEBYTECODE=1`.
- Hosted CI/network: neither was invoked. Exact-candidate hosted execution remains an
  orchestrator-owned accumulated gate and is not claimed here.

## Independent focused-command proof

The workflow contains exactly one focused pytest process. Inside the existing sole
subshell whose first operation is `trap '' TERM`, its exact ordered selectors are:

1. `tests/implementation/test_c3_b2_private_host.py::test_cleanup_regression_observation_cannot_change_timeout_or_cancelled_product_failure`
2. `tests/verification/test_c3_b2_private_host_round3.py::test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation`

The first selector has the exact `timeout` and `cancelled` parameters; the second is the
evidence-backed singleton identified by failed hosted evidence. Therefore the one
focused process collects exactly three cases. Independent execution under inherited
ignored SIGTERM returned `3 passed in 0.25s`.

Focused status is captured exactly once. The sole broad pytest process is lexically
inside `if [ "$focused_status" -eq 0 ]`; the else branch propagates focused failure.
Each focused selector occurs exactly once again and only as a broad `--deselect`, so no
case executes twice. The workflow contains exactly two pytest process invocations, no
retry label, attempt loop, or while loop, and one final status/exit path.

After deleting the added singleton selector from the focused command and the six newly
appended broad selectors, the complete workflow reproduced round 7 byte-for-byte.
Thus the exact 1,300-byte tail, printable filter, five redactions, 3,952-byte worst-case
annotation bound, one initialized/shared append log, sanitizer, report, GitHub escaping,
status, annotation, and no-retry behavior are unchanged.

## Exact partition and retention

The 15 ordered unique superseded-B1 ignores and prior 11 ordered selectors are unchanged.
Exactly these six selectors are appended in this order:

1. evidence-backed singleton:
   `tests/verification/test_c3_b2_private_host_round3.py::test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation`
2. stale round-7 candidate/workflow binding:
   `tests/verification/test_c3_b4_public_round7.py::test_candidate_tree_and_workflow_digest_are_exact`
3. stale round-7 exact prior-workflow restoration:
   `tests/verification/test_c3_b4_public_round7.py::test_redaction_log_status_and_no_retry_are_byte_preserved`
4. stale round-7 prior 11-selector/12-case shape:
   `tests/verification/test_c3_b4_public_round7.py::test_partition_is_exact_ordered_unique_eleven_selectors_twelve_cases`
5. stale round-7 assertion that the now-focused singleton remains selected:
   `tests/verification/test_c3_b4_public_round7.py::test_second_sigterm_node_remains_selected_and_passes`
6. stale round-6 literal focused-selector adjacency:
   `tests/verification/test_c3_b4_public_round6.py::test_focused_gate_is_once_no_retry_and_broad_only_on_success`

The final 17 selector strings are ordered and unique and expand to exactly 18 cases
only because the original forced-kill selector has two parameters. The singleton is
the only newly isolated product/evidence test. The other five additions are exact
workflow/partition identity assertions invalidated by that authorized adjacency.

The round-6 verifier has exactly ten nodes: the prior three identity nodes and the one
adjacency node are disposed, while the other six behavior/scope nodes remain selected
and passed. The round-7 verifier also has exactly ten nodes: the exact four newly stale
nodes are disposed, while its six diagnostic/scope nodes remain selected and passed.

Candidate-qualified collection, excluding only this descendant round-8 verifier, was
exactly `1442/1460 tests collected (18 deselected) in 0.73s`. The candidate contains
exactly 21 current B2/B3/B4 modules; none is ignored. The complete descendant broad run
collected 1,469, selected 1,451 and returned
`1445 passed, 6 skipped, 18 deselected, 106 warnings in 232.32s`. The nine additional
passes are exactly the fresh round-8 verifier, so candidate broad arithmetic is 1,436
passes, six classified skips, and 18 deselections. The separate focused phase supplies
the three transparently deselected mandatory cases. The six skips were two sandbox
loopback and four optional machine-local physical-artifact checks; no mandatory Cycle 3
or B2/B3/B4 check skipped.

## Commands and exact results

- Fresh round-8 verifier:
  `python -m pytest -q tests/verification/test_c3_b4_public_round8.py` —
  `9 passed in 0.55s`; no skip.
- Exact focused two-selector command under inherited ignored SIGTERM:
  `3 passed in 0.25s`.
- Exact broad descendant partition: `1445 passed, 6 skipped, 18 deselected` in
  232.32 seconds. All six retained round-6 nodes, six retained round-7 nodes, and all
  current B2/B3/B4 modules passed.
- Prior C3B4-V001 through V004 passed within the broad run: exact immutable public
  classes/values and typed bytes; parent/worker tightening and containment; CSV exit 5
  versus replay exit 2 before read/mapping/launch; bounded UTF-8 diagnostics and exact
  installed CLI/API behavior.
- Focused Ruff over decode, host, CLI, workflow/B4 implementation, and all eight B4
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
  B1 SHA-256 values, without extra resource or root escape. The closed characterization
  tool inventory contained no bytecode.
- Prohibited-process audit returned no active .NET, pythonnet, `sigrok-cli`, or external
  libsigrokdecode process. Scoped source/workflow search returned no prohibited import,
  dependency, or command.
- `git diff --check`: pass.

The exact workflow SHA-256 is
`9e427b6090f01a2506570246189df20ced8a077b25877d1e57af374e6c0e7805`.
Exact `macos-15-intel`, the first pre-checkout `uname -m`/x86_64 guard, full-history
checkout, job-wide pre-Python bytecode suppression, focused-before-broad status gate,
and every later locked/static/CLI/web/frontend/asset/browser gate remain in their
verified order.

The candidate-relative path audit found only the workflow, its regression, and
descendant B4 evidence. No product, B2/B3 test, decoder/API, fixture, limit, threshold,
dependency, lock, manifest, contract, or frontend asset changed. Preserved SHA-256
identities include public decode `d5cd8b84...19db`, private host `b81d3c1b...15b6`, CLI
`c3acce49...3ddc`, typed vectors `b5cc317f...fbf`, thresholds `98e48bb1...e3c`, option
matrix `5d84b9d9...209`, dev lock `4efa0b1d...53`, web lock `4b0feead...45`, and package
metadata `ead05ffb...cf`.

Installed metadata remains `License-Expression: GPL-3.0-only`, exact four license-file
entries, numpy/pyserial base dependencies, and aiohttp conditional only on the web
extra. License and attribution digests remain unchanged.

## Findings and dispositions

1. **Focused isolation — verified.** One inherited-SIGTERM pytest command executes the
   exact ordered two selectors/three cases once; broad runs only after focused success
   and deselects both selectors.
2. **Partition — verified.** Fifteen ignores and 17 unique ordered selectors produce
   exactly 18 broad deselections. Only the singleton, four stale round-7 nodes, and one
   stale round-6 adjacency node are newly disposed.
3. **Retention — verified.** Six other round-6 and six other round-7 nodes, every current
   B2/B3/B4 module, and V001-V004 remain green.
4. **Prior hosted corrections — preserved.** The diagnostic bound/redaction/log/status,
   full-history checkout, no-bytecode scope, Intel/x86 guard, no retry, and gate order
   remain exact.
5. **Scope and identity — preserved.** No product, B2/B3, fixture, threshold, limit,
   lock, manifest, resource, or frontend drift was found.

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
