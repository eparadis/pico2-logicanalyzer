# C3-B4 managed-Python verification, round 10

- Identity: `c3-b4-public-verifier-1`; fresh independent round-10 verification.
- Timestamp: `2026-09-02T02:14:07Z`.
- Governing B1 commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Failed round-9 evidence: `13f8ef1b1f56594abd70fa631b5d9f1ed6ce09c8`.
- Tested candidate/tree: `ab6744c3263b504e1b4006ece64be12962ce8b47` /
  `7450014af13a8d61120de078d2c1c7d730f70c39`.
- Exact workflow SHA-256:
  `f5b2a05ba66d54944e624ee0c6777f39d4cffc8a5aa3bf719086a1f1b28d5cc8`.
- Fresh verifier SHA-256:
  `3eb211fda335196cf9182c93f6dc090ca782b24563a95987727aa052a5ad77db`.
- Candidate worktree was clean. The qualified descendant contains only this review and
  `tests/verification/test_c3_b4_public_round10.py`, both unstaged evidence artifacts.
- Scratch was confined to repository-ignored `.tmp/c3-b4-ci`; no network, hosted CI,
  stage, commit, escalation, hardware, serial, capture, or publication was performed.

## Independent expectations and results

The workflow uses immutable
`astral-sh/setup-uv@c771a70e6277c0a99b617c7a806ffedaca235ff9` (v9), requests
exact uv `0.12.6`, and disables the action cache. `actions/setup-python` is absent.
Both uv cache and managed-install roots are beneath ignored repository
`.tmp/c3-b4-ci`. The exact managed key is
`cpython-3.12.13-macos-x86_64-none`; its complete expected `sys.version`, x86_64
machine, base-prefix suffix, and `BUILD` value `20260623` are checked before Node or
dependency installation. The existing accepted offline runtime reproduced every
value. The verifier independently created core and web venvs from that interpreter
and reverified the full version and architecture in each.

Node `22.14.0`, full-history checkout, job-wide no-bytecode, `macos-15-intel`, the
pre-checkout x86_64 guard, focused/broad ordering, 1,300-byte bounded diagnostic,
sanitization, status propagation, and no-retry behavior remain exact. The focused
command retained its ordered two-parameter forced node plus the evidence-backed
round-3 singleton and passed all three cases once. Broad remains conditional on
focused success and deselects both focused selectors.

The workflow has exactly 15 ordered unique ignores and 26 ordered unique selectors,
expanding to 27 cases. Relative to round 9, only the six predicted stale nodes were
appended: the round-4 Intel/prebootstrap identity, round-6 job-header identity, and
four round-9 candidate/Python/workflow/partition identity nodes. All other round-9
nodes and every current B2/B3/B4 module remain selected. Candidate-qualified
collection was exactly `1478 collected / 27 deselected / 1451 selected`.

## Commands and evidence

- Fresh verifier: `9 passed in 5.37s`; Ruff passed.
- Exact focused gate: `3 passed in 0.23s`.
- Accepted raw-B1 replacement identity node: `1 passed in 0.12s`, under the exact
  complete CPython 3.12.13 version recorded by B1.
- Retained B2/B3/B4 direct sweep, including every B4 verification round and the fresh
  verifier: `830 passed, 26 deselected in 118.84s`. The twenty-seventh broad
  deselection is the fixture-surface node outside this bounded module sweep.
- V001-V004 passed in that sweep: immutable public API/typed bytes, parent/worker
  limit tightening, CSV exit 5 versus replay exit 2 before read/mapping/launch, and
  bounded installed CLI/API behavior.
- Ruff over production and B4 evidence: pass. Mypy: 31 production files clean;
  strict installed consumer: one file clean. Both stable clean environments reported
  no broken requirements.
- Strict B1, B2, and B3 manifest validation: pass without output.
- Frontend ESLint and TypeScript: pass; Vitest: three files/five tests pass; Vite:
  29 modules built; production asset drift: pass.
- Installed outside-source `pico-la decode --help` retained exact replay/CSV grammar,
  metadata/channel/options, and UART/SPI/I2C choices.
- Installed metadata remains `GPL-3.0-only`, with exact four license files,
  numpy/pyserial base dependencies, and aiohttp only for the web extra.
- Decoder-resource and digest checks passed in the retained suite: exact closed nine
  files with B1 digests and no root escape. Scoped prohibited import/command search
  found only expected upstream attribution comments; a complete process snapshot had
  no .NET, pythonnet, `sigrok-cli`, or libsigrokdecode process.
- Candidate-relative path audit found only workflow/regression and evidence changes;
  no product, B1/B2/B3, decoder/API, fixture, limit, threshold, dependency, lock,
  manifest, resource, or frontend change. `git diff --check` passed.

## Findings and dispositions

1. **Managed runtime correction — verified.** Immutable setup-uv, exact uv/runtime,
   ignored roots, predependency guard, and both venv origins are exact and green.
2. **Partition — verified.** Counts are 15 ignores, 26 selectors, and 27 cases; only
   the six predicted stale identities are newly disposed.
3. **Accepted behavior — preserved.** Raw B1, focused three-case execution, V001-V004,
   B2/B3 regressions, static checks, resources, locks, manifests, and frontend pass.
4. **Scope — preserved.** No product or accepted contract identity drift was found.

## Legal and gate limitation

The package bytes, PEP 639 metadata, attribution, and notices remain consistent with
the accepted engineering disposition. This is not a legal conclusion: shim ownership,
the historical MIT label, and combined-work treatment still require counsel or
rights-holder confirmation before conveyance. No wheel/sdist was built or uploaded and
no publication occurred. Exact-candidate hosted macOS execution remains a root-owned
accumulated gate and is not claimed here.

APPROVAL_NEEDED: none.

## Verdict

pass
