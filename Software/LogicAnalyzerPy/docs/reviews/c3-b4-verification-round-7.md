# C3-B4 hosted failure-diagnostic verification, round 7

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-02T00:37:12Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Failed accumulated evidence: `79ee8e6b004e21d20fd3fc15bec7d6bd45bdbf12`
- Prior round-6 candidate/tree: `db94d6b4a63aefbd1ec185a6492344be3df98842` /
  `26f3afe065e0202d9289e7ccb4a8fb47a9329a31`
- Tested candidate/tree: `f3565c11c1d7ea4351349d141401c6f98ba3940d` /
  `e0346acdcc6ea64369ba612237eb583e66311bf8`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round7.py`; neither changes product identity.
- Environment: Darwin 24.6.0 x86_64, Python 3.12.13; stable clean environments
  `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Scratch: only repository-ignored `Software/LogicAnalyzerPy/.tmp/c3-b4-r7` was used;
  verification Python commands set `PYTHONDONTWRITEBYTECODE=1`.
- Hosted CI/network: neither was invoked. This diagnostic candidate requires a new
  root-owned exact-candidate hosted dispatch to reveal the prior hidden failure.

## Independent diagnostic proof

The workflow uses exactly one `LC_ALL=C tail -c 1300` raw-byte bound and contains no
remaining 12,000-byte tail. The fresh verifier executed the exact filtering/redaction
pipeline. A longer input ending in 1,300 percent bytes yielded exactly those final
1,300 bytes after sanitization.

The permitted raw-byte set is tab, LF, CR, and printable ASCII. Exhaustive expansion
accounting found the maximum GitHub escape width is three characters, reached only by
`%`, CR, and LF. The verifier then ran the workflow's exact Bash escaping and wrapper
against the 1,300-percent worst case:

- escaped report: exactly 3,900 bytes;
- exact `::error title=Cycle 3 non-hardware pytest failure::` prefix: 51 bytes;
- terminating LF: one byte;
- complete annotation command: exactly 3,952 bytes, below the 4,096-byte ceiling.

This is a byte bound, not a character-count assumption. The preceding sanitizer emits
only ASCII, so no encoding expansion remains after escaping.

For a content proof, the verifier created and ran a real failing pytest node under the
ignored repository scratch tree, prefixed its output with more than 1,300 discarded
bytes, and processed it through the exact sanitizer. The retained tail contained the
real `FAILED test_real_failure_suffix.py::test_real_failure_suffix`, exact
`AssertionError: round7-real-suffix`, and final `1 failed in ...s` suffix. Thus the
tail selection retains pytest's final failure report rather than early progress.

After restoring only `tail -c 12000` and deleting the three newly appended selector
lines, the workflow reproduced round 6 byte-for-byte. Therefore printable-byte
filtering, all five redactions, sanitizer self-test, focused/broad append behavior,
shared status, report printing, GitHub escaping, annotation wrapper, nonzero exit, and
no-retry behavior are unchanged.

## Exact partition and retention

The exact 15 ordered unique superseded-B1 ignores are unchanged. The exact prior eight
ordered selectors remain in place, followed only by these three newly stale round-6
identity selectors:

1. `tests/verification/test_c3_b4_public_round6.py::test_candidate_tree_and_workflow_digest_are_exact`
2. `tests/verification/test_c3_b4_public_round6.py::test_exact_ordered_partition_has_eight_unique_nodes_and_nine_cases`
3. `tests/verification/test_c3_b4_public_round6.py::test_runner_guard_and_every_other_gate_byte_are_preserved`

The resulting 11 selectors are ordered and unique and expand to exactly 12 deselected
cases because the existing focused forced-kill selector has two parameters. The three
new selectors are precisely the round-6 candidate/workflow digest, old eight-selector
shape, and old exact-workflow-byte assertions. The other seven round-6 behavior and
scope nodes remain selected and passed.

Candidate-qualified collection, excluding only this descendant round-7 verifier, was
exactly `1438/1450 tests collected (12 deselected) in 0.90s`. The candidate contains
exactly 20 current B2/B3/B4 modules; none is ignored. The complete descendant broad run
collected 1,460, selected 1,448 and returned
`1442 passed, 6 skipped, 12 deselected, 106 warnings in 230.65s`. The ten additional
passes are exactly the fresh round-7 verifier, so candidate arithmetic is 1,432 passes,
six classified skips, and 12 deselections. The six skips were two sandbox-loopback and
four optional machine-local physical-artifact checks; no mandatory Cycle 3 or B2/B3/B4
check skipped.

The diagnostic-only second signal node,
`test_real_timeout_forces_kill_reap_and_emits_separate_cleanup_observation`, is absent
from both ignore and selector sets. It independently passed in 0.12 seconds and passed
again in the broad run. It was not focused, retried, or waived.

## Commands and exact results

- Fresh round-7 verifier:
  `python -m pytest -q tests/verification/test_c3_b4_public_round7.py` —
  `10 passed in 0.64s`; no skip.
- Preserved focused inherited-SIGTERM proof: `2 passed in 0.16s`.
- Independently selected second SIGTERM node: `1 passed in 0.12s`.
- Exact broad descendant partition: `1442 passed, 6 skipped, 12 deselected` in
  230.65 seconds. All seven retained round-6 nodes and all current B2/B3/B4 modules
  passed.
- Prior C3B4-V001 through V004 passed within the broad run: exact immutable public
  classes/values and typed bytes; parent/worker tightening and containment; CSV exit 5
  versus replay exit 2 before read/mapping/launch; bounded UTF-8 diagnostics and exact
  installed CLI/API behavior.
- Focused Ruff over decode, host, CLI, workflow/B4 implementation, and all seven B4
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
`7b74489c4f540a8e1a5281ae642fd77b6f8a00b403346287c40480ee49655576`.
Exact `macos-15-intel`, the first pre-checkout `uname -m`/x86_64 guard, full-history
checkout, job-wide pre-Python bytecode suppression, focused inherited-SIGTERM command,
broad-only-on-focused-success gate, and every later locked/static/CLI/web/frontend/
asset/browser gate remain in their verified order.

The candidate-relative path audit found only the workflow, its regression, and
descendant B4 evidence. No B2/B3 product or test byte, decoder/API, fixture, limit,
threshold, dependency, lock, manifest, contract, or frontend asset changed. Preserved
SHA-256 identities include public decode `d5cd8b84...19db`, private host
`b81d3c1b...15b6`, CLI `c3acce49...3ddc`, typed vectors `b5cc317f...fbf`, thresholds
`98e48bb1...e3c`, option matrix `5d84b9d9...209`, dev lock `4efa0b1d...53`, web lock
`4b0feead...45`, and package metadata `ead05ffb...cf`.

Installed metadata remains `License-Expression: GPL-3.0-only`, exact four license-file
entries, numpy/pyserial base dependencies, and aiohttp conditional only on the web
extra. License and attribution digests remain unchanged.

## Findings and dispositions

1. **Diagnostic byte bound — verified.** Every permitted raw-byte tail produces a
   complete annotation command no longer than 3,952 bytes, within 4,096.
2. **Failure suffix — verified.** Exact tail/filter/redaction processing preserves the
   real pytest failure node, assertion, and final summary suffix.
3. **Partition — verified.** Fifteen ignores and 11 selectors produce exactly 12 cases;
   only three newly stale round-6 identity nodes are added and all other round-6 nodes
   remain green.
4. **Second signal node — retained.** It is selected and passes without isolation.
5. **Prior corrections and C3B4-V001-V004 — preserved.** Full history, no bytecode,
   Intel/x86 guard, focused status gate, public behavior, bounds, resources, and exit
   taxonomy pass.
6. **Scope and identity — preserved.** No product, fixture, threshold, limit, lock,
   manifest, or frontend drift was found.

## License, scope, and gate disposition

Exact package bytes, PEP 639 metadata, attribution, and notices remain consistent with
the accepted engineering disposition. This is not a legal conclusion: shim ownership,
the historical MIT label, and combined-work treatment still require counsel or
rights-holder confirmation before conveyance. This verifier built no wheel or sdist and
performed no upload, conveyance, publication, hardware, firmware, serial, live capture,
network access, or hosted CI dispatch.

The candidate is eligible for the orchestrator's accumulated gate and exact-candidate
hosted diagnostic dispatch. This verifier does not claim those future results, final
acceptance, manifest readiness, or checkpoint completion.

## Verdict

pass
