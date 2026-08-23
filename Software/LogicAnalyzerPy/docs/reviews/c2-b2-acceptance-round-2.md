# C2-B2 independent acceptance — round 2

- Lane / stable identity: acceptance / `cycle2-acceptance-replacement-2`
- Implementor identity: `cycle2-implementor-replacement-5`
- Verifier identity: `cycle2-verifier-replacement-3`
- Product candidate commit: `90adb3adb38a938ce470fa854e6fc7b98e1501c9`
- Product candidate tree: `5a09d57e4caa266a43f164edaffc94fc9a3236d7`
- Accepted at: `2026-08-23T17:34:13Z`
- Prior-verdict transfer: none
- Verdict: `pass`

## Audit inputs

Acceptance independently audited the current macOS-only Cycle 2 goal,
orchestration contract, complete batch procedure and settled B2 contracts; the
approved discovery record and current progress log; accepted Cycle 1 completion
and recovery evidence; the accepted C2-B1 manifest/checkpoint and immutable
reviews; the original C2-B2 manifest/checkpoint and acceptance; all four
immutable C2-B2 verification rounds; checked-in V2 firmware as read-only
protocol authority; physical finding `C2B3-I001`; the exact corrected candidate
delta; and the fresh verifier and root accumulated-validation results.

The assigned commit exists and resolves to the assigned tree. Current HEAD is a
tracked descendant adding only orchestration, verifier-test, and immutable
verification records relative to this corrected product candidate. Untracked
`Software/LogicAnalyzerPy/scripts/validate_c2_b3_capture.py` is B3-lane work and
was excluded from candidate identity, product judgment, and test execution.
Round-four verification has SHA-256
`56f5a99c0d34464ae09081145ef2b9d1378e6b6c792276152515cb3dc47e443a`,
names the exact candidate/tree, reports `pass`, and has no open finding.

## Integrated candidate and regression audit

The correction replaces the obsolete eight-entry default result labels and
mappings with complete ordered defaults derived from `config.channel_ids`.
Consequently the contract-required D0-D23 CLI/config/result path produces 24
ordered `D0` through `D23` entries, and reordered subsets follow physical IDs
rather than packed positions. Explicit metadata remains bounded and continues
to reject wrong lengths, empty/overlong/non-string values, and duplicate labels.

The complete B2 evidence continues to cover ordered one-to-24-channel model and
request-position semantics; mode-derived byte widths and native dtypes; literal
48-byte requests; bounded fragmented and contaminated responses; zero upper
24-bit padding; canonical inert schema-2 replay and schema-1 reads; hostile
archive/NPY/JSON cases; deterministic generalized and legacy-compatible CSV;
bounded explicit `csv-import`; CLI exits and cleanup; accepted Cycle 1
regressions; and the locked production frontend shell. No earlier acceptance or
partial B3 recovery/8/16-channel physical result was transferred.

## Findings and dispositions

1. `C2B2-V001`: resolved; new replay writes use schema 2 and schema-1 reads remain covered.
2. `C2B2-V002`: resolved; valid seven-channel and wider ordered subsets remain accepted.
3. `C2B2-V003`: resolved; bounded legacy integer-rate inference remains covered.
4. `C2B2-V004`: resolved; bounded explicit `csv-import` remains available.
5. `C2B2-V005`: resolved; explicit CSV metadata validation precedes timing arithmetic.
6. `C2B2-V006`: resolved; CLI CSV reads remain bounded before materialization.
7. `C2B3-I001`: resolved; full ordered D0-D23 default labels and mappings are produced while malformed explicit metadata still rejects.
8. `C2B2-A002`: no new acceptance finding; disposition closed by this pass.

No finding is open.

## Commands and concise results

- Candidate/tree, ancestry, changed-path, excluded-untracked-path, and `git diff --check` audits: pass.
- Round-four record digest: exact assigned SHA-256 matched.
- Independent round-four plus implementation focused matrix: 45 passed.
- Fresh verification: focused 45 passed; Ruff; mypy over 19 files; full non-hardware Python 276 passed, 1 covered sandbox-only loopback skip, 94 warnings; CLI; pinned Node 22.14.0 lint/type/unit/build/assets; brokered Playwright 1 passed.
- Root complete accumulated gate: pip check; Ruff; mypy over 19 files; full non-hardware Python 276 passed, 1 covered sandbox-only loopback skip, 94 warnings; CLI; assets; pinned Node 22.14.0 lint/type/unit/build; brokered Playwright 1 passed; `git diff --check` passed.

## Scope, authority, and checkpoint decision

The product correction is confined to the B2-owned Python capture model and a
focused implementation test. It adds no bus analysis, browser capture API or
viewer behavior, performance work, decoder, other firmware mode, or later-batch
evidence. No hardware or serial operation, firmware edit/build/flash,
bootloader, Wi-Fi, power-cycle, persistent device action, C#/.NET, `.lac`,
public server, packaging/publication, or Cycle 3 action is authorized by or
credited to this acceptance.

Verdict is `pass`. The exact corrected candidate satisfies the complete C2-B2
checkpoint readiness gate. This acceptance authorizes only orchestrator-owned
replacement/validation of the C2-B2 manifest and checkpoint record as required,
followed by a complete fresh C2-B3 physical sequence. It does not authorize
transfer of the earlier recovery, 8-channel, or 16-channel physical results.
