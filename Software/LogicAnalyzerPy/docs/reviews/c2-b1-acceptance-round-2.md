# C2-B1 independent acceptance, round 2

- Lane / identity: acceptance / `cycle2-acceptance`
- Implementor identity: `cycle2-implementor-replacement-1`
- Verifier identity: `cycle2-verifier`
- Reviewed candidate commit: `47575f54230965a3f1772aac53064323aea3f119`
- Reviewed candidate tree: `6cbec99662323b5d530def6cb8dfc5cb092ee927`
- Review date: 2026-08-22 America/Los_Angeles
- Prior verdict transfer: none
- Verdict: `pass`

## Candidate and evidence identity

The assigned commit exists and resolves to the assigned tree. Relative to the
previously rejected candidate, the executable delta is limited to the Cycle 2
evidence validator, its implementation tests, and the verifier-owned recovery
timeout test. The remaining additions are immutable acceptance and verification
records. The prior rejected acceptance record remains unchanged.

Independent verification record
`Software/LogicAnalyzerPy/docs/reviews/c2-b1-verification-round-17.md` has SHA-256
`a7604ec0058b24d0a7338a48e4e9f2b49dd229e06e32683c8748d3c55648a970`, names the
same candidate and tree, reports `pass`, closes `C2B1-CI-MAC-002`, and reports no
open verifier finding. Rounds 14 and 15 durably close `C2B1-A001` and
`C2B1-V012`; round 16 preserves the hosted macOS timeout-fixture diagnosis.

Public hosted run `32622678276` identifies the exact candidate and tree and
completed with `success`. Ubuntu job `97153164756` and macOS job `97153164870`
both identify the exact candidate and completed with `success`.

## Acceptance audit

The validator recursively rejects standalone 43-character URL-safe capability
values, explicit Bearer/Basic authorization credentials, Cookie/Set-Cookie
headers, and explicitly delimited capability, token, API-key, and password
values. It retains device-path, local-URL, user-home, recursive-field, digest,
role, timestamp, and schema checks. Its grammar does not classify ordinary
security prose about token redaction, authorization, cookies, passwords, or
security review as a credential. Independent and implementation fixtures cover
hostile values in otherwise-valid nested and free-text locations and benign
prose in valid manifests. `C2B1-A001` and `C2B1-V012` are accepted as closed.

The recovery verifier uses an injected monotonic clock and one production
deadline. Its first scripted read advances the shared clock by five
milliseconds; the second must receive a positive timeout strictly smaller than
the first. This deterministically distinguishes one overall timeout budget from
a renewed per-read budget without depending on host scheduling. The corrected
fixture, full local gate, and repeated exact-candidate hosted matrix support
closure of `C2B1-CI-MAC-002`.

The orchestrator-supplied exact-product accumulated gate reports `pip check`,
Ruff, mypy, CLI help, 231 non-hardware passes with one sandbox-only loopback
skip, frontend install/lint/typecheck/unit/build/browser, deterministic assets,
diff check, and clean candidate state passing. Independent verification reports
the exact timeout test, 65 protocol/foundation tests, Ruff, mypy over 19 source
files, 232 non-hardware passes in its environment, and the pinned Node 22
installed-Chromium production smoke passing. The differing local skip outcome
is explained by the documented sandbox-only loopback restriction and is not a
required-behavior skip in the independent or hosted environments.

The full B1 foundation remains within scope: approved governing contracts are
unchanged; the single Cycle 2 macOS/Linux workflow, locked optional web runtime,
Node 22.14.0 frontend, deterministic local assets, inert loopback-only server,
canonical Host/Origin/capability-cookie boundary, clean lifecycle, missing-extra
diagnostic, evidence schema, and preserved Cycle 1 non-hardware behavior have
passing accumulated and independent evidence. Firmware, C# applications,
hardware, public serving, `.lac`, .NET, packaging/publication, and excluded
Cycle 3 surfaces remain untouched. Later stopping-condition work remains owned
by C2-B2 through C2-B6 and is not claimed complete here.

## Findings and dispositions

- `C2B1-A001`: closed and accepted.
- `C2B1-V012`: closed and accepted.
- `C2B1-CI-MAC-002`: closed and accepted.
- New findings: none.

## Manifest and checkpoint handoff

The C2-B1 manifest is correctly absent from the reviewed candidate because the
governing order requires acceptance first. The orchestrator may now atomically
create only `Software/LogicAnalyzerPy/testdata/evidence/c2-b1.json`. It must name
this exact candidate and tree; record the distinct implementation,
verification, and acceptance identities; include the exact local and hosted
commands/results, run and job identities, sources, findings/dispositions,
limitations, deferred work, stopping-condition coverage, and separate
development-lock, web-lock, package-lock, and asset-manifest digests; and pass
the candidate's Cycle 2 validator. The manifest must then be committed before
the orchestrator appends the C2-B1 checkpoint record and marks the batch
complete. No C2-B2 through C2-B6 manifest may be created early.

## Final state

The exact candidate satisfies the complete pre-manifest C2-B1 acceptance gate.
No acceptance finding remains open. Checkpoint completion remains contingent
only on the orchestrator-owned atomic manifest validation/commit and subsequent
progress-log checkpoint append required by the governing procedure.
