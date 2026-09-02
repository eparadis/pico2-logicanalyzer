# C3-B4 immutable CPython artifact verification, round 11

- Identity: `c3-b4-public-verifier-1`; independent bounded B4 round 11.
- Timestamp: `2026-09-02T06:38:55Z`.
- Governing B1 commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Tested candidate/tree: `fb2f4d63df41f7d5d0c2253c59f02803dac14a55` /
  `57faa63344049874e09ebaa89807de8ea6188547`.
- Exact workflow SHA-256:
  `153c9b3987200eef271f4f26c0253622e0f087a12c1d89216971d67062041318`.
- Candidate worktree was clean. Before the evidence commit, the qualified descendant
  contained only this review and `tests/verification/test_c3_b4_public_round11.py`.
- Scratch was confined to ignored repository `.tmp/c3-b4-ci/round11`.

## Artifact and runtime proof

The official CPython standalone artifact was independently downloaded over the exact
HTTPS-only/TLS-1.2-minimum URL configured in the workflow. It was exactly 24,690,991
bytes and its SHA-256 was exactly
`a6bbea996c5f14eb55ab275889d2df45408deec504b4a7219d7b59c045b2555e`.
Every archive member was rooted beneath the expected `python/` component. Extraction
with the workflow's `--strip-components 1` semantics produced exact accepted
`sys.version` `3.12.13 (main, Jun 23 2026, 15:54:40) [Clang 22.1.3 ]` and x86_64.

The workflow pins release tag `20260623`, the exact artifact name and digest, checks
the digest strictly before extraction, and runs the complete version/x86_64/managed-
suffix guard before Node setup or dependency installation. Moving setup-uv, uv catalog
resolution, setup-python, and the inapplicable synthetic `BUILD` check are absent.
Both clean venvs still originate from `PICO_LA_PYTHON` and independently recheck full
version and architecture before their hash-locked dependency installs.

## Partition and retained behavior

The exact partition contains 15 ordered unique ignores and 32 ordered unique selector
strings representing 33 cases. The six appended selectors are precisely the four
superseded round-10 uv/candidate identities and the two now-stale round-10 partition
identities. The three other round-10 behavior/scope nodes remain selected and green.
All 24 current B2/B3/B4 implementation and verification modules are unignored.
Independent candidate-qualified collection was exactly
`1454/1487 tests collected (33 deselected)`.

Full-history checkout, job-wide no-bytecode, `macos-15-intel`, pre-checkout x86_64
guard, Node 22.14.0, the one inherited-SIGTERM focused command with its three cases,
broad-only-on-focused-success ordering, 1,300-byte diagnostic bound, sanitization,
status propagation, and no retry remain present. The accepted raw-B1 replacement node
is selected and passes without weakening.

## Commands and results

- Fresh verifier: `10 passed in 2.26s`; Ruff passed.
- Retained workflow plus every B2/B3/B4 module and B4 round, under the applicable
  partition: `835 passed, 32 deselected in 117.28s`. The remaining broad deselection is
  the fixture-surface node outside this direct module sweep.
- V001-V004 passed within the retained sweep: exact immutable public API/typed bytes;
  complete parent/worker tightening; CSV exit 5 versus replay exit 2 before reads,
  mapping, or launch; bounded installed CLI/API behavior and exact error ordering.
- Production and evidence Ruff: pass. Mypy: 31 source files clean; strict public
  consumer: one file clean. Both stable clean environments passed `pip check`.
- Strict accepted B1, B2, and B3 manifest validation: pass without output.
- Frontend ESLint and TypeScript: pass; Vitest: three files/five tests; Vite: 29
  modules; production asset drift: pass.
- Installed outside-source CLI retained exact replay/CSV grammar and UART/SPI/I2C
  choices. Installed metadata remains `GPL-3.0-only`, four exact license files,
  numpy/pyserial base dependencies, and aiohttp only in the web extra.
- Retained resource checks proved the closed exact nine-file decoder snapshot and B1
  digests. Scoped prohibited import/command search was empty. The complete process
  inventory contained no product .NET, pythonnet, `sigrok-cli`, or libsigrokdecode
  process (the only textual match was the verifier's own audit command).
- Candidate-relative scope contains only workflow, implementation regression, and
  accumulated/round-10/round-11 evidence. No product, decoder/API, B1/B2/B3 fixture,
  limit, threshold, lock, manifest, resource, or frontend bytes drifted.
- `git diff --check`: pass.

## Findings and dispositions

1. **Immutable artifact correction — verified.** URL, size, digest, extraction layout,
   accepted complete runtime identity, ordering, and both venv origins are exact.
2. **Transparent partition — verified.** Exactly six stale round-10 identity nodes are
   newly disposed; all retained behavior and every current module remain green.
3. **Product and contract preservation — verified.** Raw B1, V001-V004, B2/B3,
   resources, locks, manifests, static checks, frontend, and installed API are intact.

## Legal and execution boundary

The package bytes, PEP 639 metadata, attribution, and notices remain consistent with
the accepted engineering disposition. This is not a legal conclusion: shim ownership,
the historical MIT label, and combined-work treatment still require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload, conveyance,
publication, hardware, serial, capture, Cycle 4 work, or hosted CI dispatch occurred.

APPROVAL_NEEDED: none.

## Verdict

pass
