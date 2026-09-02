# C3-B4 hosted-failure correction verification, round 12

- Identity: `c3-b4-public-verifier-1`; independent bounded B4 round 12.
- Timestamp: `2026-09-02T07:18:38Z`.
- Governing B1 commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Failed hosted predecessor: run `33599975263`, job `100151298994`, verifier
  `773460d980349d6449cb2f522558ad2f03808f9a`.
- Tested candidate/tree: `c7650876544e477c277200c4f2fcbd23c67fe245` /
  `87e36568aae7fe0cc55cfc1f584cc8b025c52769`.
- Exact workflow SHA-256:
  `12ff6bb2cd7e437b733f3aaeb9488c6926604572419468c60604f0dea1c6a990`.
- Candidate worktree was clean; verification scratch stayed beneath ignored repository
  `.tmp/c3-b4-ci/round12` and the retained ignored round-11 artifact directory.

## Hosted-failure dispositions

The actual child still receives the deliberately strict private profile with
`wall_deadline_ms=200` and `terminate_grace_ms=20`, and the test still requires the
`hang` request to raise `RunnerFailure`. Only the independent recovery request now uses
the governed default profile. The exact corrected node passed in 0.34 seconds and the
complete pre-execution runner suite passed in the retained sweep. No product deadline,
threshold, limit, or implementation byte changed.

The round-11 artifact-byte test now obtains both paths from the hosted workflow
environment. Independent branch tests proved:

- both exact environment paths present: one pass, checking the 24,690,991-byte archive,
  SHA-256 `a6bbea996c5f14eb55ab275889d2df45408deec504b4a7219d7b59c045b2555e`,
  archive layout, executable, full accepted `sys.version`, and x86_64;
- both absent: exactly one specifically classified pytest skip; and
- either variable present alone: failure, never skip or silent weakening.

The immutable artifact URL/digest/extraction/runtime guard remains statically selected.

## Partition and retained behavior

The exact workflow partition contains 15 ordered unique ignores and 37 ordered unique
selector strings representing 38 cases. The five appended selectors are exactly the
missed superseded round-10 local-uv venv node followed by four stale round-11
candidate/partition/count identity nodes. Round 11 has ten tests; the other six
behavior/scope nodes remain selected. All 25 current B2/B3/B4 implementation and
verification modules are unignored. Independent candidate-qualified collection was
exactly `1459/1497 tests collected (38 deselected)`.

The accepted raw-B1 replacement remains selected and green. Full-history checkout,
job-wide no-bytecode, macOS Intel/x86 guard, Node 22.14.0, the three-case focused gate,
broad-only-on-focused-success ordering, 1,300-byte diagnostic bound, redaction/status,
and no retry remain intact.

## Commands and results

- Fresh verifier: `10 passed in 3.78s`; Ruff passed.
- Workflow, full pre-execution runner, every current B2/B3/B4 module, and every B4
  round under the applicable partition: `1017 passed, 1 skipped, 37 deselected in
  133.76s`. The thirty-eighth broad deselection is the fixture-surface node outside
  this bounded direct sweep; the skip is the intentional local artifact-env absence.
- V001-V004 passed within that retained sweep: immutable public API/typed bytes;
  complete parent/worker tightening; CSV exit 5 versus replay exit 2 before read,
  mapping, or launch; and bounded installed CLI/API behavior.
- Ruff over production and changed/evidence tests: pass. Mypy: 31 source files clean;
  strict consumer: one file clean. Both stable environments passed `pip check`.
- Strict B1, B2, and B3 manifest validation: pass without output.
- Frontend ESLint and TypeScript: pass; Vitest: three files/five tests; Vite: 29
  modules; production asset drift: pass.
- Installed CLI grammar and PEP 639 metadata remain exact: `GPL-3.0-only`, four
  license files, numpy/pyserial base dependencies, aiohttp only for the web extra.
- Retained resource checks proved the closed nine-file decoder snapshot and B1
  digests. Scoped prohibited import/command search was empty. The process inventory
  contained no product .NET, pythonnet, `sigrok-cli`, or libsigrokdecode process; its
  sole text match was the verifier's own audit command.
- Candidate-relative drift is limited to workflow, two implementation tests, and
  implementation/prior verifier evidence. No production, decoder/API, B1/B2/B3
  fixture, threshold, limit, lock, manifest, resource, or frontend byte changed.
- `git diff --check`: pass.

## Findings and dispositions

1. **Loaded-runner recovery — verified.** The 200 ms hang proof is preserved while
   recovery is independently tested under the governed default profile.
2. **Artifact environment handling — verified.** Hosted-present passes, local-absent
   skips specifically, and both partial states fail closed.
3. **Transparent partition — verified.** Only the missed round-10 node and four exact
   stale round-11 identities are added; every retained node/module is green.
4. **Product and contract preservation — verified.** Raw B1, V001-V004, B2/B3,
   resources, locks, manifests, static checks, frontend, and installed API remain intact.

## Legal and execution boundary

This is an engineering verification, not a legal conclusion. Shim ownership, the
historical MIT label, and combined-work treatment still require counsel or rights-holder
confirmation before conveyance. No wheel, sdist, upload, conveyance, publication,
hardware, serial, capture, Cycle 4 work, or hosted CI dispatch occurred.

APPROVAL_NEEDED: none.

## Verdict

pass
