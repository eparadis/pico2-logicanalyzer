# C2-B2 independent acceptance — round 1

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-1`
- Implementor identity: `cycle2-implementor-replacement-4`
- Verifier identity: `cycle2-verifier-replacement-2`
- Candidate commit: `c3f43a9ef0311c34ece3f95c94871fcfcd2c12a3`
- Candidate tree: `782f101981348ebdde23a338c8db5a92eb81f73b`
- Accepted at: `2026-08-23T15:37:27Z`
- Verdict: `pass`

## Audit inputs

Acceptance independently audited the current macOS-only Cycle 2 goal,
orchestration contract, complete batch procedure and settled B2 contracts; the
approved discovery record; accepted Cycle 1 completion proof and evidence; the
accepted C2-B1 manifest/checkpoint and its immutable verification/acceptance
records; the C2-B2 activation and identity records; all three immutable C2-B2
verification rounds; checked-in V2 firmware as read-only protocol authority;
the exact candidate delta; and the exact-candidate accumulated-validation
record at descendant commit `2d47de0c67037d1ba3ad2ffcc43194446adc9bfd`.

The assigned commit exists and resolves to the assigned tree. The clean
descendant adds only immutable verification/progress records relative to the
product candidate. Round-three verification has SHA-256
`765e00cfe542ce29f712bf433b05e99c7175500b9bacb4cc5868348c98caa85a`,
names the exact candidate, reports `pass`, and has no open finding. No prior
verdict was transferred as acceptance authority.

## Integrated candidate and regression audit

The candidate implements the authorized ordered one-to-24-channel normal
capture domain, mode-derived byte widths and dtypes, literal 48-byte request and
bounded response handling, packed request-position extraction, schema-2 replay
with schema-1 reads, deterministic generalized and legacy-compatible CSV, and
the bounded `csv-import` CLI surface. Independent tests cover the settled
8/16/24-bit literals, reordered subsets, escaping, fragmentation, malformed and
contaminated responses, exact bounds, upper-byte rejection, hostile replay,
CSV metadata and timing, CLI exits, and cleanup.

Accepted Cycle 1 behavior remains represented in the accumulated non-hardware
suite, schema-1 compatibility checks, exact legacy D0-D7 CSV checks, default
D0-D7 CLI behavior, recovery tests, and the accepted historical physical
evidence. B2 performed no physical operation and does not replace Cycle 1
hardware facts.

## Scope and authority audit

The product delta is confined to authorized Python model, V2 protocol, device,
replay/CSV, CLI, and directly supporting test paths. It does not add bus
analysis, browser capture API/viewer behavior, performance work, other firmware
modes, decoders, or future-batch evidence. No firmware, C#, workflow, hardware,
serial, USB, native interactive browser, .NET, `.lac`, public server,
package/publication, persistent-state, or Cycle 3 action occurred.

B2's owning gate is the complete local non-hardware Python suite plus the
locked frontend production-shell gates. Exact-candidate hosted macOS CI is not
an owning B2 item and remains mandatory for the final candidate at C2-B6. No
`testdata/evidence/c2-b2.json` existed at acceptance time; creation and
checkpoint append remain orchestrator-owned after this verdict.

## Commands and concise results

- Candidate/tree and descendant path audit: exact match; descendant differences
  are only the progress record and round-three verifier record.
- `sha256sum` for round-three verification: expected digest matched.
- C2-B1 evidence validator: pass; manifest digest
  `7c45f8b7f90965fbf9c67845f3b8a0113fe84261e8085665068e6f1980bf4de0`
  matched the accepted checkpoint.
- Independent focused wider-capture test: 34 passed.
- CLI help: pass; `csv-import` present.
- Candidate delta `git diff --check`: pass.
- Exact-candidate accumulated core gate: Python 3.12.13 hash-locked install,
  `pip check`, Ruff, mypy over 19 files, and CLI help passed; pytest reported
  265 passed, 1 sandbox-loopback skip, and 94 warnings.
- Exact-candidate locked frontend gate: official Node 22.14.0 archive digest
  matched; clean install of 215 packages, lint, typecheck, one Vitest test,
  Vite production build, deterministic assets, and Playwright production-shell
  smoke (1 passed) all passed. The authorized browser smoke covers the
  sandbox-only loopback skip.

## Findings and disposition

1. `C2B2-V001`: resolved; new replay writes use schema 2 while schema-1 reads
   remain covered.
2. `C2B2-V002`: resolved; valid seven-channel and wider ordered subsets are
   accepted.
3. `C2B2-V003`: resolved; legacy integer-rate inference accepts only a unique
   rate reproducing all canonical time cells.
4. `C2B2-V004`: resolved; bounded explicit `csv-import` CLI exposure is present.
5. `C2B2-V005`: resolved; complete explicit CSV metadata validation precedes
   rate-dependent arithmetic and invalid rates produce bounded errors.
6. `C2B2-V006`: resolved; CLI input is rejected or bounded before full
   materialization, with deterministic exit and artifact behavior.
7. `C2B2-A001`: no new acceptance finding; disposition closed by this pass.

No finding is open. The exact candidate satisfies the C2-B2 acceptance gate.
The orchestrator may create and validate only the C2-B2 evidence manifest and
then append the B2 checkpoint without expanding scope.
