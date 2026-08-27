# C3-B1 threshold-proposal accumulated validation — round 2

## Subject and verdict

- Validation owner: primary Cycle 3 orchestrator (`/root`).
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Immutable proposal candidate/tree:
  `395646fa1172382928581d7266723f5b044cf8f2` /
  `6857f9a67ff70220e6d6b2a11f9ca450005c8321`.
- Required fresh verification: `pass`, committed at
  `1cdedcae57e6233010410172196b23f6167ee675`; verifier-test SHA-256
  `f146f0d58a65116825f6ee6b2e04e4fcf495fca89de9565bf70e26b662509c79`
  and record SHA-256
  `c160cc75238ab48479fb3cfe4d0c4d0c86ee052102a4fd2715050b285d4e50a0`.
- Completed: `2026-08-27T13:50:57Z`.
- Verdict: **pass**. No applicable mandatory check failed or remained skipped.

This gate authorizes only fresh independent proposal acceptance. It does not
approve a numeric value, create product enforcement, authorize B2, or transfer
any pass from the failed round-1 proposal.

## Repository-local Python gate

All Python tooling ran from the ignored repository-local `.venv`, using Python
3.12.13. No environment was built or executed from `/private/tmp`, no package
was installed, and no dependency/network approval was needed. `pip check`
passed. `requirements-dev.lock` and `pyproject.toml` remain respectively
`6f78ec8f0219b919c44ed9b9f1d30c2337fcce7c911b8d3dc4c13edb707a6575`
and `56f56100d48c9586ca49f14c77e84f23668e1af0670d548c22fca1db636061f2`.

| Command class | Result |
| --- | --- |
| Ruff over the complete project | exit 0 |
| strict mypy over `src` | exit 0; 21 source files |
| strict mypy over all seven characterization modules | exit 0; seven files |
| deterministic Cycle 3 fixture generator `--check` | exit 0; no drift |
| characterization binding `--check` | exit 0; no drift |
| fresh round-2 proposal verifier | exit 0; 22 passed in 0.37 s |
| all applicable unrestricted non-hardware tests | exit 0; 637 passed, 3 explicitly deselected, 149 accepted warnings in 124.51 s |
| all six accepted Cycle 2 evidence validators | exit 0 each |

The accepted warnings are the inherited aiohttp key/deprecation warnings and
the deliberate duplicate-ZIP warning. No new warning class appeared.

### Exact applicability classification

An unfiltered 640-test inventory was run first and reported 637 passes plus
three expected history-sensitive failures. No source or historical test was
edited to hide them. The passing accumulated command deselected exactly these
three node IDs:

1. `test_cycle3_fixture_surface_is_present_and_rebuildable` freezes the
   pre-proposal JSON namespace and therefore rejects the two proposal files
   that the governing assignment requires in that directory. All substantive
   fixture tests and the deterministic generator check still passed.
2. `test_candidate_identity_digest_environment_schema_and_summary_arithmetic`
   requires `sys.executable` to equal the former raw-characterization path
   `/private/tmp/cycle3-clean-python/bin/python`. The raw evidence still names
   and hashes that immutable environment; this accumulated gate intentionally
   uses the operator-requested repository-local interpreter instead.
3. The round-1 exact-proposal identity test correctly continues to reject the
   obsolete one-second boundary recorded by `C3B1-TPV001`. Its remaining 21
   historical negative tests passed, while all 22 fresh round-2 tests passed.

These are not waivers of current behavior: each excluded assertion is tied to
an immutable earlier subject, and its applicable current replacement passed.

## Repository-local exact Node 22 regression

The already accepted Node 22.14.0 runtime was copied into ignored local path
`.venv/node22`; an ignored local script shell ensures npm child commands use
that runtime while preserving project `node_modules/.bin`. This required no
download. One reusable authorization class covers loopback-only npm test
scripts, and it was reused without per-process requests.

`web/package-lock.json` remains
`d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
`web/production-assets.json` remains
`00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.

| Command class | Result |
| --- | --- |
| exact local Node version | v22.14.0 |
| ESLint and TypeScript | exit 0 each |
| Vitest | exit 0; three files, five tests |
| Vite production build plus governed Python asset checker | exit 0; 29 modules, no drift |
| accepted Playwright browser regressions | exit 0; one plus three tests |
| B6 offline performance and accepted-threshold checker | exit 0; one test |

An initial performance attempt launched Playwright under system Node v26.7.0
because npm's child shell did not inherit the local binary prefix. The browser
test passed but the frozen metadata checker correctly rejected it. That report
was replaced by a fresh Node v22.14.0 run whose browser test and unchanged
threshold checker both passed. The accepted report SHA-256 is
`3e9cd4363f6ec6399d7aac5df132986e866da229c4d89adf5dc9e020ef5f3345`;
generated results were moved intact beneath ignored local `.venv/artifacts`.

## Identity, scope, and disposition

The proposal and rationale remain byte-identical to candidate `395646f` and
retain SHA-256 values
`94882b710f2d569c0ea0535366a0c1c3df3514aa20a18e4cd35f652177458ec2`
and `18a6b58a2b05f7dd7aa302a6e1bb4d074621440648a2e735a1d16d9708b209b0`.
The proposal remains `proposal-not-approved`. Exact 900-ms formula arithmetic,
29-category closure, boundaries, caps, evidence digests, environment
qualification, provenance, and negative mutations passed again.

Final `git diff --check`, candidate quiet diff, and clean worktree checks
passed. No product decoder host, public API, approved-limit file, hardware,
USB/serial action, firmware, external runtime, publication, Cycle 4 work, or
numeric operator decision occurred. No pytest, Playwright, Vite, or product
server remained. Findings: none. Next authority: fresh proposal acceptance.

`pass`
