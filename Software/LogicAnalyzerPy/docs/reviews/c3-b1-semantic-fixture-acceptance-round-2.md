# C3-B1 semantic-fixture acceptance — round 2

## Identity and immutable subject

- Acceptance identity/role: `c3-b1-semantic-fixture-acceptance-1`
  (`/root/c3_b1_fixture_accept`), reused only in its original independent
  semantic-fixture acceptance role.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Round-2 assignment commit/tree:
  `942dc7a868874c25930e2cd11c1c64ef5b7db5ba` /
  `9e5c3d3da21fa48777ab88bedfe6c6b5d2c89045`.
- Exact corrected fixture candidate commit/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Fresh round-9 verification commit/record SHA-256:
  `8b08f7d72bc67f4bb8753190e2e0d70402a13675` /
  `3e2f507332fdfc82e8e49df016b66db223508144677cc5166d8a4e090d0378c6`.
- Fresh accumulated-validation round-2 commit/record SHA-256:
  `bdd5e5a1bd953ff06e0a17b6f5f3fcc227ddf4ae` /
  `196b07bf214adddb70b094c30402d706415f183f4451beb82e6bf0ee2d6162ac`.
- Accepted independent project/license review commit/record SHA-256:
  `538a4aa669a782919dafefb26a81d7346ed45f5c` /
  `b7afc4df18ba9bf5e40ee5a795e4544e54a59be27b1fea9a8617681ea82919cf`.
- Audit UTC: `2026-08-27T03:23:19Z`.
- Audit descendant before this record: HEAD
  `942dc7a868874c25930e2cd11c1c64ef5b7db5ba`, tree
  `9e5c3d3da21fa48777ab88bedfe6c6b5d2c89045`, branch `python-rewrite`, clean
  worktree.

No earlier verdict transfers. In particular, round-8 verification,
accumulated-validation round 1, and acceptance round 1 remain accurate only
for superseded candidate `c1420ad9b4309fc7417acbc228085b68237c24d0` and
provide no authority for this corrected candidate.

## Audit boundary and commands

I freshly read the repository/subagent instructions, exact governing goal and
contracts, current assignment, the complete immutable candidate/reviewer
history, RI011 discovery and invalidation sequence, exact corrected candidate
diff and artifacts, round-9 verifier record, accumulated round-2 record, and
accepted project/license review. Checked-in source was inspected only as inert
bytes/static AST evidence. I did not execute a fixture generator, decoder,
runner, helper, product, C#/.NET, pythonnet, libsigrokdecode, sigrok runtime,
hardware, network installation, raw characterization, browser, or Cycle 4
action.

All shell commands used the required `rtk` prefix. Results:

- `rtk git rev-parse HEAD HEAD^{tree}` and `rtk git show -s --format=...` for
  the contract, assignment, candidate, verifier, accumulated-validation, and
  project/license commits — exit 0; all identities above matched.
- `rtk git diff-tree --no-commit-id --name-status -r 7c57a34...` and exact
  parent/candidate diff inspection — exit 0; the correction changes only
  semantic-fixture prose, generator, cap JSON, fixture manifest, and fixture
  implementation assertions.
- `rtk git diff --name-status 7c57a34...HEAD` plus exact candidate-path quiet
  diff — exit 0; descendants contain only progress and immutable evidence, and
  every candidate/test path is byte-identical to the corrected candidate.
- `rtk shasum -a 256` over all candidate artifacts and the three evidence
  records — exit 0; every recorded digest matched.
- Static `rtk jq` audits of all fixture JSON — exit 0: 63 timelines, 1,058
  waits, 1,049 records, five edge decisions, 165 unique option rows, 12 typed
  vectors, 12 literal goldens, nine source files, three file sets, and 17
  unique complete caps.
- Static `rtk jq` cap assertions — exit 0; all 17 caps have the complete
  schema, positive finite integer values, unique IDs, derivation results equal
  to values, and exact accept-at-value/reject-at-value-plus-one boundaries.
- Independent `rtk jq -n` arithmetic — exit 0:
  `724292 * 4096 = 2966700032`, `64 * 1024^3 = 68719476736`, max-floor
  `68719476736`, reject boundary `68719476737`.
- `rtk git log --oneline --reverse` over fixture/review history — exit 0; all
  nine verification rounds, old acceptance, corrected candidate, and ordered
  invalidation history remain immutable.
- Final `rtk git diff --check` and `rtk git status --short` — exit 0 and clean
  before creation of this record.

## Candidate identities and corrected finite cap

Corrected candidate SHA-256 values are generator
`6fc5289ba1076413283942be0374bd97def08b284bf7a7cef4e7b6105636be63`,
semantic-fixture document
`86ca972e1522ad12ab459902dacffa933d6f89289088815d7584b9f627e69d39`,
experiment caps `63cde36892a15a390be0c27c50eac18431d7a4b11381b0e4b82c0fe64f808cd8`,
fixture manifest `0f5f1d9a01fc807dd0f4078ac84b20158f515a76ae4f1f83cc74651c4797413a`,
and implementation test
`838e5a81d5778437edf7ea652eea0921aee58a300f3a9f6a024ac1943e97d273`.

Unchanged candidate SHA-256 values are provenance/license document
`3155b8ea00e54fc8facd86d6a28604e9a0f3cf1097751392e6a12380ad9ddc4c`,
provenance JSON `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`,
semantic JSON `8da1d2aa2256cce5c56ac2df4a629d90a95c21cb84d633522780394439888e64`,
option matrix `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`,
typed vectors `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`,
and immutable verifier test
`e7081c043c790223d07b76724d6b5f73cca6c1d185635b0ad18f591bbd7a5cf9`.

The 17 exact values remain: wall deadline `5000 ms`; terminate grace `250
ms`; input `100000 samples`; request `46354688 bytes`; output `69632 records`;
encoded and decoded `6180864 bytes` each; stdout `193152 bytes`; stderr `96576
bytes`; diagnostic `12072 bytes`; text and binary `3090432 bytes` each; nested
depth `40`; nested items `69632`; retained result `185418752 bytes`; recursion
`320 frames`; and corrected worker address space `68719476736 bytes`.

For `worker_address_space_bytes`, the corpus basis is `724292`, multiplier is
`4096`, static compatibility floor is exactly 64 GiB, operation is
`max-floor`, result/accept is `68719476736`, and reject is `68719476737`.
The JSON and prose consistently define an absolute macOS-x86_64 managed-CPython
`RLIMIT_AS` ceiling. They explicitly distinguish it from RSS, data, and growth
and classify the clean-environment set/readback only as feasibility input for
the runner, not boundary enforcement, raw characterization, a runtime
baseline, or an approved product threshold.

## Findings and dispositions

1. **Pass — exact subject, immutability, scope, and roles.** Candidate/tree and
   all evidence identities are exact. Descendant changes do not alter any
   candidate/test byte. The fixture implementor, fixture verifier, this
   acceptance identity, primary orchestrator, project/license reviewer, and
   distinct runner implementor/verifier/acceptance identities remain properly
   separated. This identity authored only this record and repaired nothing.

2. **Pass — RI011 discovery and invalidation were correctly ordered.** The
   runner lane discovered that old absolute `RLIMIT_AS=2966700032` was below a
   fresh inert managed-CPython virtual-address baseline and could not be set.
   Runner work paused before a candidate; the old fixture's round-8,
   accumulated-1, and acceptance-1 passes were invalidated for future use; the
   fixture owner produced a new immutable candidate; fresh round-9 verification
   and accumulated-2 validation then passed. No old pass or uncommitted runner
   result transferred.

3. **Pass — corrected max-floor arithmetic and feasibility are exact.** Static
   independent arithmetic reproduces `max(724292 * 4096, 64 * 1024^3) =
   68719476736`, with exact plus-one rejection. Round 9 independently observed
   VSZ `35113566208` and RSS `10534912`, confirmed the old limit failed with
   `ValueError: current limit exceeds maximum limit`, and set/read back
   `(68719476736, 68719476736)` in the same fresh governed CPython 3.12
   environment. Accumulated round 2 repeated the exact clean-environment
   64-GiB set/readback. These results establish feasibility only.

4. **Pass — finite cap specification remains complete and truthful.** Every
   cap has a unique ID, positive finite integer, unit, domain, source basis,
   structured operation, multiplier/floor, result, rationale, later-runner
   coverage, and exact boundary. The corrected address-space rationale does
   not relabel virtual address space as RSS/data/growth or claim observation as
   a product baseline. The corpus globally states no enforcement and no
   approved product threshold; actual boundary enforcement remains entirely
   the distinct runner candidate's burden.

5. **Pass — all semantic fixture authority remains unchanged and complete.**
   The correction changes no expected output. The 63 finite UART/SPI/I2C
   timelines retain all transitions, waits, simultaneous predicates, skip and
   EOI behavior, five frozen edge decisions, half-open coordinates, emissions,
   source-exact declarations, and integer `0xFF` absent optional RX/TX/MISO/
   MOSI/no-CS semantics. The 165-row matrix closes defaults, enums, boundaries,
   types, sentinels, unknowns, duplicates, contextual UART delimiters, and SPI
   width preapproval through named direct witnesses or explicit rejection.

6. **Pass — vectors, goldens, provenance, imports, and notices remain bound.**
   Twelve v1 objects and 12 literal compact sorted UTF-8-plus-LF goldens cover
   all four record kinds and nine Python value tags with real file sets,
   declarations, defaults, mappings, output IDs, coordinates, rational times,
   and base64. Import commit `407b5ef039aa0474c400c0721749baa126e53270`,
   prior gitlink `0235970293590f673a253950e6c61017cefa97df`, nine exact
   source digests, closed imports including helper `.mod`, and three ordered
   file sets remain exact. Eight files retain GPLv2-or-later notices; the shim
   truthfully records no in-file notice observed.

7. **Pass — round-9 verification is fresh and complete.** It independently
   re-audited the corrected cap plus all unchanged fixture semantics, 1,058
   waits, 1,049 records, options, sentinels, declarations, vectors/goldens,
   provenance, imports, notices, schemas, digests, derivations, boundaries,
   no-oracle and prohibited-runtime scope. Its only non-static action was the
   assigned inert clean-Python feasibility probe; no decoder or repository
   module ran. It reports no unresolved finding.

8. **Pass — accumulated-validation round 2 is complete and correctly ordered.**
   It followed round-9 `pass`, binds the same corrected candidate, and records
   a freshly cleared hash-locked Python 3.12 environment; editable no-deps/
   no-build-isolation install; `pip check`; Ruff; strict mypy; all 403
   non-hardware tests with no skip; installed help; deterministic fixture
   rebuild; focused tests; exact set/readback; Cycle 1/2 evidence preservation;
   prohibited dependency/import/process audit; optional-web/performance
   regressions; candidate quiet diff; and clean final state. No mandatory gate
   failed, skipped, used a stale candidate, or simulated a result.

9. **Pass — accepted project/license input is correctly ordered and bounded.**
   The independent review binds the exact nine sources, notices, provenance,
   current MIT metadata, and repository GPLv3 text. It specifies future private
   commit-pinned placement, retained headers, attribution/license files,
   `GPL-3.0-only` distribution metadata, bounded package-data patterns, and
   clean artifact/install verification. None has been prematurely implemented
   or claimed: the current editable install exposes no snapshot. Shim and MIT
   rights-holder/counsel confirmation remains mandatory before conveyance, and
   no build, wheel, sdist, publication, distribution, or legal guarantee is
   authorized by this acceptance.

10. **Pass — readiness is limited to the distinct runner phase.** This exact
    corrected fixture candidate, fresh verification, accumulated validation,
    and project/license input are ready only for a new distinct pre-execution
    runner candidate. The runner must independently prove all cap enforcement,
    boundary/overrun behavior, cleanup, termination, close, and reap paths with
    inert/hostile non-decoder probes before unchanged accepted runner bytes may
    execute any snapshot. This verdict does not authorize decoder execution,
    raw characterization, threshold proposal/approval, package placement,
    manifest/checkpoint creation, or any later batch.

## Discrepancies, deferrals, worktree, and approval

- Discrepancies: none.
- Deferrals in governing order: distinct runner implementation, verification,
  accumulated validation, and acceptance; permitted decoder characterization
  and raw observations; independent reproduction; threshold proposal/reviews/
  acceptance; explicit operator numeric approval; prescribed package changes
  and counsel/rights-holder confirmation before conveyance; later B1 final
  gates, manifest verification, and checkpoint.
- Worktree scope: exactly this one new acceptance record; no candidate, test,
  progress, contract, product, runner/method/probe/raw, decoder, package/lock/
  workflow, evidence manifest, Cycle 1/2, browser, hardware, firmware, C#,
  or Cycle 4 path changed.
- Approval needed: none.

pass
