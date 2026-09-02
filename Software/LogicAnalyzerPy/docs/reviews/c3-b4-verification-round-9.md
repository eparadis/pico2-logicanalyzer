# C3-B4 exact hosted Python verification, round 9

- Identity and role: `c3-b4-public-verifier-1`; fresh independent B4 verifier round
- Timestamp: `2026-09-02T01:38:45Z`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Failed hosted evidence resolved from `5cc6150`:
  `5cc615044c0bcaac6f640e5decc74503025745f3`
- Prior round-8 candidate/tree: `fefc3307c2de0a680bf44cdcbbabf2e804495a4a` /
  `489ae588679ea4306c49304c0c1e40733b9f7938`
- Tested candidate/tree: `3b8de59f8fc5276a92d5ea5fef5b48b259374a52` /
  `aee4e77238ce2dfd8d311b47873dfe3ebb21d4d6`
- Candidate branch/worktree: `python-rewrite`; candidate was clean. The qualified
  descendant worktree contains only this review and
  `tests/verification/test_c3_b4_public_round9.py`; neither changes product identity.
- Environment: Darwin 24.6.0 x86_64, exact CPython 3.12.13; stable clean environments
  `/private/tmp/cycle3-clean-core` and `/private/tmp/cycle3-clean-web`.
- Scratch: only repository-ignored `Software/LogicAnalyzerPy/.tmp/c3-b4-r9` was used;
  verification Python commands set `PYTHONDONTWRITEBYTECODE=1`.
- Hosted CI/network: neither was invoked. Exact-candidate hosted execution remains an
  orchestrator-owned accumulated gate and is not claimed here.

## Exact Python and accepted B1 proof

The workflow contains exactly one `actions/setup-python@v5` block with exact
`python-version: "3.12.13"`. No floating `python-version: "3.12"` remains. The setup
block precedes both `python -m venv .venv` and `python -m venv .venv-web`, so both clean
workflow environments derive from the accepted patch-level interpreter.

The accepted raw B1 replacement node
`tests/verification/test_c3_b1_raw_baseline_candidate_replacement.py::test_candidate_identity_digest_environment_schema_and_summary_arithmetic`
is absent from all 15 ignores and all 20 selectors. The verifier independently loaded
`testdata/decoders/cycle3-raw/environment.json` and compared its complete recorded
version string with the running interpreter:

`3.12.13 (main, Jun 23 2026, 15:54:40) [Clang 22.1.3 ]`

The tuple was exactly `(3, 12, 13)`, the complete `sys.version` strings matched, and the
accepted node passed. It was selected again in the retained relevant sweep and passed.
This validates the accepted immutable verifier; it does not weaken or disposition it.

Exact Node `22.14.0` remains present once and unchanged.

## Preserved focused harness and partition

The one focused pytest process remains inside the sole inherited-SIGTERM-ignore
subshell and retains exact selector order: original two-parameter forced-kill node,
then the evidence-backed round-3 singleton. Independent execution returned
`3 passed in 0.25s`. Broad remains conditional on focused success and deselects both
selectors, with no retry or double execution.

After replacing exact Python 3.12.13 with the prior floating 3.12 value and deleting
only the three newly appended round-8 selectors, the workflow reproduced round 8
byte-for-byte. Thus full-history checkout, job-wide no-bytecode, `macos-15-intel`, the
pre-checkout x86_64 guard, focused/broad status, 1,300-byte diagnostic tail, redaction,
shared log, annotation, no retry, Node setup, and every later gate/order are unchanged.

The 15 ordered unique ignores and prior 17 selectors remain unchanged. Exactly these
three stale round-8 identity nodes are appended:

1. `tests/verification/test_c3_b4_public_round8.py::test_candidate_tree_and_workflow_digest_are_exact`
2. `tests/verification/test_c3_b4_public_round8.py::test_diagnostic_log_status_redaction_and_1300_bound_are_unchanged`
3. `tests/verification/test_c3_b4_public_round8.py::test_partition_is_exact_ordered_unique_seventeen_selectors_eighteen_cases`

The final 20 selector strings are ordered and unique and expand to exactly 21 cases
only because the original forced-kill selector has two parameters. The round-8 verifier
has exactly nine nodes; only the three exact candidate/workflow/old-partition identity
nodes are disposed, while the other six behavior/scope nodes remain selected and pass.

Candidate-qualified collection, excluding only this descendant round-9 verifier, was
exactly `1448/1469 tests collected (21 deselected) in 0.95s`. The candidate contains
exactly 22 current B2/B3/B4 modules; none is ignored.

## Commands and exact results

- Fresh round-9 verifier:
  `python -m pytest -q tests/verification/test_c3_b4_public_round9.py` —
  `9 passed in 0.83s`; no skip.
- Exact focused three-case inherited-SIGTERM command: `3 passed in 0.25s`.
- Accepted raw-B1 identity node, workflow regression, every current B2/B3/B4 module,
  all B4 rounds, and the fresh verifier under the applicable selectors:
  `830 passed, 20 deselected in 110.83s`; no skip. The omitted twenty-first broad
  deselection is the frozen fixture-surface node whose module was outside this relevant
  direct sweep. Subtracting the nine descendant verifier cases gives candidate-relevant
  arithmetic of 821 passes and 20 deselections, plus the separate three focused passes.
- Prior C3B4-V001 through V004 passed within that sweep: exact immutable public
  classes/values and typed bytes; parent/worker tightening and containment; CSV exit 5
  versus replay exit 2 before read/mapping/launch; bounded UTF-8 diagnostics and exact
  installed CLI/API behavior.
- Focused Ruff over decode, host, CLI, workflow/B4 implementation, and all nine B4
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
`b25d28ae03bc203dccc819d90aca8f76199e2b034e5b5e7b94575e2ed4a64a84`.

The candidate-relative path audit found only the workflow, its regression, and
descendant B4 evidence. No product, B1/B2/B3 test, decoder/API, fixture, limit,
threshold, dependency, lock, manifest, contract, or frontend asset changed. Preserved
SHA-256 identities include public decode `d5cd8b84...19db`, private host
`b81d3c1b...15b6`, CLI `c3acce49...3ddc`, typed vectors `b5cc317f...fbf`, thresholds
`98e48bb1...e3c`, option matrix `5d84b9d9...209`, dev lock `4efa0b1d...53`, web lock
`4b0feead...45`, and package metadata `ead05ffb...cf`.

Installed metadata remains `License-Expression: GPL-3.0-only`, exact four license-file
entries, numpy/pyserial base dependencies, and aiohttp conditional only on the web
extra. License and attribution digests remain unchanged.

## Findings and dispositions

1. **Exact hosted Python — verified.** Setup requests 3.12.13 exactly once, precedes
   both clean environments, and contains no floating 3.12 value.
2. **Accepted raw B1 replacement — retained and green.** It is selected and its complete
   recorded `sys.version` exactly matches the verifier runtime.
3. **Partition — verified.** Fifteen ignores and 20 ordered unique selectors produce 21
   cases; only three stale round-8 identity nodes are newly disposed and six other
   round-8 nodes remain green.
4. **Prior corrections and V001-V004 — preserved.** Node 22.14, focused three cases,
   diagnostic bound, full history, no bytecode, Intel/x86 guard, public behavior, and
   gate order remain exact.
5. **Scope and identity — preserved.** Every current B2/B3/B4 module is unignored and no
   product, B1/B2/B3, fixture, threshold, limit, lock, manifest, or frontend drift was
   found.

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
