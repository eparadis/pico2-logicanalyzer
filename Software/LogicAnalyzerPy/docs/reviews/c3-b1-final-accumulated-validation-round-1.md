# C3-B1 final accumulated validation — round 1

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable corrected final candidate/tree:
  `1f8793210a3298ed190ff30f97c84b6f9feb9b29` /
  `cbe33ca272ba1b452f6d87fb5e702134a471f702`.
- Fresh final verification: `pass`, committed at
  `42b6a185f183fe701e0037cbc6b4636196c96f34`; test SHA-256
  `6f931ad8acbff9078e1f6ea125954c4861d4278aa5c0531b81b60ddd8fcb88d2`
  and record SHA-256
  `a1cadd1a09836680721418ff606af771b5a9b85f497b27c03d0f8cca64950eaf`.
- Completed: `2026-08-27T17:13:30Z`.
- Verdict: **pass**. All 21 frozen command records passed. No applicable
  mandatory check failed or remained skipped.

This pass authorizes only fresh final C3-B1 acceptance. It creates no manifest,
checkpoint, B2 product authority, package/distribution authority, non-macOS
claim, or Cycle 4 authority.

## Repository-local Python 3.12 gate

Every Python command used the ignored repository-local `.venv` with CPython
3.12.13. No environment or formatting tool ran from `/private/tmp`; no package
was installed and no dependency/network approval was needed. The pip cache was
unwritable and therefore disabled, without affecting the healthy environment.

| Frozen command class | Result |
| --- | --- |
| `pip check` | exit 0; no broken requirements |
| whole-project Ruff | exit 0 |
| strict mypy over product | exit 0; 21 files |
| strict mypy over characterization tools | exit 0; seven files |
| deterministic fixture generator `--check` | exit 0; no drift |
| corrected runner binding `--check` | exit 0; no drift |
| installed CLI help | exit 0 |
| six Cycle 2 evidence validators | exit 0 each |
| applicable unrestricted non-hardware matrix | exit 0; 657 passed, three explicitly deselected, 149 accepted warnings in 128.24 s |

The complete unfiltered 660-test inventory ran first. It reported 657 passes
and exactly the three already reviewed immutable historical failures:

1. the pre-proposal fixture namespace assertion rejects the four governing
   threshold/final-binder JSON additions while every substantive fixture and
   deterministic rebuild test passes;
2. the raw-history identity assertion requires its immutable
   `/private/tmp/cycle3-clean-python/bin/python` characterization executable,
   while this gate intentionally uses repository-local tooling; and
3. the immutable round-1 threshold identity test correctly rejects the old
   one-second `C3B1-TPV001` value while every fresh round-2 threshold and final
   candidate test passes.

The applicable run deselected only those exact node IDs and then passed all 657
selected tests. No source, historical test, candidate, raw value, proposal, or
approval byte was edited to obtain the result. Accepted warnings remain only
the inherited aiohttp key/deprecation warnings and deliberate duplicate-ZIP
warning; no new warning class appeared.

## Exact repository-local Node 22 gate

The ignored local Node runtime is exactly v22.14.0. The existing reusable
loopback npm-script authorization was reused for browser/performance work; no
per-process request occurred.

| Frozen command class | Result |
| --- | --- |
| ESLint | exit 0 |
| TypeScript | exit 0 |
| Vitest | exit 0; three files, five tests |
| Vite production build | exit 0; 29 modules |
| governed Python asset checker | exit 0; no drift |
| accepted Playwright browser regressions | exit 0; one plus three tests |
| B6 offline performance and accepted-threshold checker | exit 0; one test |

The accepted performance report records Node v22.14.0, Chromium
133.0.6943.16, Playwright 1.50.1, and method
`c2-b5-playwright-production-v2`; SHA-256 is
`315649da912bb92a012cab2c766935ce79c8af4a11245683dbb6aeed280935fa`.
Generated results were moved intact beneath ignored local `.venv/artifacts`.

## Evidence, dependencies, and exact candidate

- Final binder/rationale remain byte-identical to candidate `1f87932`, with
  SHA-256
  `55983bbe9613c0deb0fe7f05a2e88b680b9cfed352f4cccfae9cdd01ca744adf`
  and `9577c4b268af5a4a8c6b7f59f934e8ba689a23d4bda66aa0e8662533acd82396`.
- Fresh final verification repeated 32 live digests, 29 approved boundaries,
  21 commands, six roles, complete implementation histories, correction-only
  equivalence, commit/tree reachability, and 17 negative mutation families.
- All six accepted Cycle 2 manifests validate against the accepted draft
  2020-12 schema. Accepted Cycle 1 B1-B5 manifest hashes remain respectively
  `12cb4dfe2bcd898cef4a7c5d9dd4803954c91e9965d17c22efe365d5976717bc`,
  `0fe57660c6d88116633a6bcdf28a0a998ca29fdec94fc324c5a2ed3a345238af`,
  `2d02aea3417de296b44348aa2dcf5d59661430d52b726be2bd1ee3aa77b2b598`,
  `16ebfc390d658cec07d01adce2facaa2505f7eeaa42c2f2642cfb326f9eeeead`,
  and `3b5ef8eca10c4ce51692bc8356f4e6f0cfd24f0aa5b9826646d513691c23ab9d`.
- `requirements-dev.lock` and `requirements-web.lock` both remain
  `6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`;
  the package lock remains
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`
  and the production asset manifest remains
  `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
- `find_spec` returned `None` for `pythonnet`, `clr`, `sigrokdecode`, and
  `libsigrokdecode`. Active product source, metadata, and locks contain no
  `pythonnet`, .NET/CLR, libsigrokdecode, or `sigrok-cli` runtime dependency.
- Project/license disposition `538a4aa` and its rights-holder/counsel
  limitation remain exact. No snapshot was copied into the installed package,
  and no wheel or sdist was built.

## Scope, cleanup, and disposition

Exact candidate quiet diff, all bound hashes, `git diff --check`, generated
asset equality, and clean tracked worktree passed. The centralized reusable
process audit and a targeted post-command query found no pytest, Playwright,
Vite, Cycle 3 characterization, or product web process remaining.

No product decoder host, public decode API, approved-limit weakening, C#/.NET/
pythonnet/libsigrokdecode/`sigrok-cli`, external decoder runtime, hardware,
USB/serial action, firmware, publication/distribution, non-macOS claim, B2
implementation, excluded action, or Cycle 4 work occurred. Findings: none.
Next authority: fresh final C3-B1 acceptance.

`pass`
