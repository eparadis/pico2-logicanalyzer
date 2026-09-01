# C3-B4 accumulated validation, round 1

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Independently verified B4 evidence commit/tree:
  `a076d185fd24e1531e2a76aea70824d0b7659837` /
  `a30b03c6406d33f361634827a246c9dc9a009a05`.
- Completed: `2026-09-01T22:27:11Z`.
- Verdict: **changes_required**. Local accumulated validation passed, but the
  mandatory exact-candidate hosted macOS job failed on a runner outside the
  frozen x86_64 environment class.

This failed gate authorizes no acceptance, manifest, checkpoint, publication,
or Cycle 4 work. The hosted failure is preserved rather than retried or waived.

## Clean local accumulated gate

The exact candidate was cloned with no shared hardlinks. A fresh repository-
local `.venv` used CPython 3.12.13. Development dependencies were installed
offline with `--require-hashes` from the already hash-verified wheelhouse, and
the product was installed editable with `--no-build-isolation --no-deps`.
`pip check` and installed `pico-la --help` passed.

The governed applicable non-hardware partition used the accepted 15
superseded-B1 ignores and the one frozen historical fixture-surface
deselection. It completed with **1422 passed, four classified optional physical-
artifact skips, one historical deselection, and 149 inherited warnings in
237.32 seconds**. No mandatory Cycle 3 test skipped.

Additional local results:

- whole-project Ruff: pass;
- mypy over production `src`: pass, 31 source files;
- strict mypy over `tools/cycle3_characterize`: pass;
- fixture generator and characterization binding `--check`: pass;
- all six Cycle 2 and accepted C3-B1 through C3-B3 manifest validators: pass;
- official Node 22.14.0 archive SHA-256:
  `6698587713ab565a94a360e091df9f6d91c8fadda6d00f0cf6526e9b40bed250`,
  exactly the accepted governed digest;
- exact Node 22.14.0 locked install: 215 packages;
- ESLint and TypeScript: pass;
- Vitest: three files, five tests passed;
- Vite: 29 modules built; and
- production asset drift check: pass.

The first Node bootstrap observation used the host default Node 26.7.0 only to
identify an environment mismatch and supplies no accepted frontend result. The
complete accepted frontend gate was then rerun under the exact official Node
22.14.0 runtime above.

## Exact-candidate hosted result and diagnosis

Root pushed only exact commit `a076d185fd24e1531e2a76aea70824d0b7659837`
to dedicated branch `cycle3-b4-ci-a076d18`. GitHub Actions run
`33501933713`, job `99837032689`, resolved the same head SHA. Environment,
checkout, Python 3.12, Node 22.14.0, both clean dependency installs through
Ruff, production mypy, and the strict installed public consumer all passed.
The non-hardware pytest step then failed with repeated
`pico_logic_analyzer._decode.model.HostFailure: process-exit` in the B3 UART
conformance worker calls. Later CLI, web, frontend, asset, and browser steps
were correctly skipped. Hosted conclusion: `failure`.

This is not treated as infrastructure success or replaced by the local pass.
The workflow uses the moving `macos-latest` label, while all approved Cycle 3
limit evidence explicitly freezes macOS x86_64. GitHub's official
`actions/runner-images` inventory retrieved for diagnosis maps `macos-latest`
to macOS 26 arm64 and maps `macos-15-intel` to macOS 15 x64. That architecture
drift explains a worker bootstrap exit before framed error handling under the
x86_64-derived absolute `RLIMIT_AS` contract. The official inventory was kept
only as ignored diagnostic scratch data; its retrieved SHA-256 was
`e2282f1ccf4a8c952433ada336e1eeda9eaffe97592c9b9c334fcaac6115f63d`.

## Required correction

Return the workflow to the governed environment class by replacing only the
moving `macos-latest` runner label with the explicit current x64 macOS label,
and add a fail-fast architecture identity check. The correction requires a new
immutable candidate, fresh independent B4 verification, a complete fresh
accumulated gate, and a new exact-candidate hosted run. No threshold, fixture,
decoder semantic path, limit, or accepted environment class may change.

The B1 rights-holder/counsel limitation remains controlling. No wheel, sdist,
upload, conveyance, or publication occurred.

`changes_required`
