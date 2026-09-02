# C3-B4 durable collection verification, round 14

- Identity: `c3-b4-public-verifier-1`; independent bounded B4 round 14.
- Timestamp: `2026-09-02T08:23:31Z`.
- Governing B1 commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate/tree: `42327be9c3ab6a85d2d17ae21a7cdf3d84633142` /
  `bc51cc4cc333e5e4df946a75dff8ace9c6d6f8d5`.
- Exact unchanged workflow SHA-256:
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`.
- Preserved ignored round-13 draft was present throughout verification but was not
  restored to the tracked tree or committed.
- Scratch was confined to ignored repository `.tmp/c3-b4-ci`; no archive extraction
  directory leaked after success or failure paths exercised here.

## Signal-context correction retained

Both round-11 and round-12 focused verifier functions retain the exact POSIX launch
contract that installs `SIG_IGN` for SIGTERM before `exec` of nested pytest. From a
normal parent, both complete verifier functions passed. A separate real shell-to-Python
exec asserted that the Python child observed `signal.SIG_IGN`. The implementation
regression covering both source launch blocks and real signal inheritance also passed.
This matches the already-passing workflow focused gate without changing workflow bytes.

## Durable immutable collection proof

Round 12 now reads the partition from immutable candidate
`c7650876544e477c277200c4f2fcbd23c67fe245`, archives precisely its
`Software/LogicAnalyzerPy` tree under a fixed prefix, and validates every member as
relative, rooted beneath that prefix, and free of `..`. Extraction uses tarfile's
`filter="data"`. Pytest collection runs from the extracted project with `PYTHONPATH`
bound to extracted `src`, a candidate-local `TMPDIR`, bytecode disabled, and the cache
provider disabled. Cleanup is in `finally`.

That round-12 node passed while both the ignored round-13 draft and the untracked fresh
round-14 verifier were present. It returned immutable arithmetic
`1459/1497 tests collected (38 deselected)` and left no `r12-c765-*` directory. Thus
descendant evidence can no longer perturb its result.

The fresh verifier independently used the same safety properties to archive exact
candidate `42327be9c3ab6a85d2d17ae21a7cdf3d84633142`. It collected exactly
`1471/1509 tests collected (38 deselected)` and left no `r14-candidate-*` directory.
Because this proof operates on immutable commit bytes, committing this verifier cannot
change the proved arithmetic.

## Retained behavior and commands

- Fresh verifier: `7 passed in 7.45s`; Ruff passed.
- Workflow, full pre-execution runner, all current B2/B3/B4 modules, all retained B4
  rounds, and fresh verification: `1026 passed, 1 skipped, 37 deselected in 146.14s`.
  The thirty-eighth workflow deselection is fixture-surface outside the bounded direct
  suite. The skip is the classified local absence of workflow artifact environment.
- Workflow remains byte-identical with 15 ordered unique ignores, 37 ordered unique
  selectors, and 38 cases. All 26 candidate B2/B3/B4 modules remain unignored.
- Raw B1, focused three-case execution, V001-V004, the 200 ms actual-hang deadline and
  default-profile recovery, artifact present/absent handling, and all retained B2/B3
  behavior passed within the fresh and retained checks.
- Ruff over production and changed/evidence files: pass. Mypy: 31 source files clean;
  strict public consumer: one file clean. Both stable environments passed `pip check`.
- Strict B1, B2, and B3 manifest validation: pass without output.
- Frontend ESLint and TypeScript: pass; Vitest: three files/five tests; Vite: 29
  modules; production asset drift: pass.
- Installed outside-source CLI grammar and PEP 639 metadata remain exact:
  `GPL-3.0-only`, four license files, numpy/pyserial base dependencies, and aiohttp only
  for the web extra.
- Retained resource checks proved the closed nine-file decoder snapshot and B1
  digests. Scoped prohibited import/command search was empty. The process inventory
  contained no product .NET, pythonnet, `sigrok-cli`, or libsigrokdecode process; its
  sole text match was the verifier's own audit command.
- Candidate-relative changes are only the round-12 verifier durability correction,
  its workflow regression, and implementation evidence. No workflow, product,
  decoder/API, B1/B2/B3 fixture, threshold, limit, selector, lock, manifest, resource,
  or frontend byte changed. `git diff --check` passed.

## Findings and dispositions

1. **Round-13 signal correction — verified.** Both nested launchers reproduce inherited
   SIGTERM ignore and pass from a normal parent.
2. **Round-14 durability correction — verified.** Round 12 now measures immutable c765
   bytes and is unaffected by descendant verifier files.
3. **Fresh proof is hosted-safe.** It independently measures immutable 42327be bytes,
   validates extraction safety, and cleans all transient data before returning.
4. **Product and contract preservation — verified.** Partition, raw B1, V001-V004,
   B2/B3, resources, locks, manifests, static checks, frontend, and installed API pass.

## Legal and execution boundary

This is an engineering verification, not a legal conclusion. Shim ownership, the
historical MIT label, and combined-work treatment still require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, conveyance, publication,
hardware, serial, capture, Cycle 4 work, or hosted CI dispatch occurred. Exact-candidate
hosted execution remains a root-owned gate and is not claimed here.

APPROVAL_NEEDED: none.

## Verdict

pass
