# C3-B1 raw-baseline verification — round 3

Verdict: `pass`.

## C3B1-RV001 and correction

Verifier identity
`c3-b1-pre-execution-runner-rebinding-verifier-1` corrected only its owned raw
verification test. Accumulated validation of verification commit
`b76554ce2c28d83ea6f88fbfe4275ea07d517431` in the mandated clean environment
reported 606 passed, one failed, and one deselected. The sole failure was
`test_candidate_identity_digest_environment_schema_and_summary_arithmetic`:
the test required the recorded collection executable
`/Users/ed/git/pico2-logicanalyzer/Software/LogicAnalyzerPy/.venv/bin/python` to
equal verifier runtime `sys.executable`, while the clean clone correctly used
`/private/tmp/cycle3-clean-python/bin/python`.

That assertion confused immutable collection provenance with verifier-runtime
compatibility. It invalidates the round-2 verifier-test portability claim and
its test SHA `895a0cead7038eccd3993b9493169652910ac8a24ad84a843211af49a461474c`;
it does not alter or invalidate the raw candidate bytes or observations.

The corrected test now requires the environment to record the exact immutable
collection executable path as provenance. Separately, it requires the verifier
to have the exact recorded `sys.version` and recorded implementation equal to
the independently queried `platform.python_implementation()` and `CPython`.
It no longer requires the clean verifier executable path to equal the
collection path. No other identity, environment, schema, canonical-JSON,
manifest, request-derivation, semantic, count, arithmetic, mutation, cleanup,
resource, or process assertion was weakened.

## Immutable subject and scope

The raw candidate remains exact commit
`2ae1e4335c38a5cf717491c7936f857292f71498`, tree
`772b13476c97a976eb3a304e9b87aec8011260ec`, governed by contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. Accepted runner candidate
`ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a`, accepted runner-chain descendant
`bf1fc5eaa232bf09e66df77bd1c4be3e1ae4ffbd`, and corrected fixture
`a98d328aab92f3dad66988fb70cc567946dc89d0` remain unchanged inputs.

All five raw SHA-256 values remain unchanged:

- environment `fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34`
- requests `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`
- observations `28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd`
- hostile observations `d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080`
- manifest `7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e`

Only
`tests/verification/test_c3_b1_raw_baseline_candidate.py` and this round-3
record changed. No raw candidate, runner, fixture, method, threshold, final,
checkpoint, product, or B2 path was modified. The two untracked B2 paths were
not inspected.

## Fresh clean verification

The corrected static preflight ran with exact clean verifier executable
`/private/tmp/cycle3-clean-python/bin/python`: three passed and the complete
reproduction test was intentionally deselected. It revalidated all five raw
hashes, canonical JSON and closed schemas/manifest, exact collection
provenance, compatible exact CPython version/implementation, runner and fixture
identities, nine provenance digests, 17 caps, independently derived 63-request
set, stored min/median/max arithmetic, and non-vacuous manifest/snapshot/hostile
mutations.

The final uninterrupted clean reproduction then passed in 102.30 seconds and
performed exactly 486 child launches:

- 63 snapshot warm-ups and 315 retained snapshot runs;
- ten hostile warm-ups and 50 retained hostile runs;
- eight recovery warm-ups and 40 retained recoveries.

All 63 snapshot cases succeeded five of five with exact canonical semantics and
stable counts. `limits` and `address_space_over` succeeded five of five; all
eight expected-failure hostile kinds failed five of five as classified and all
40 retained recovery runs succeeded. Every snapshot, hostile, and recovery
child was exactly reaped and closed both protocol descriptors. `hang`,
`stdout_flood`, and `stderr_flood` were terminated and reaped; `ignore_term`
was killed and reaped; other completion dispositions matched the candidate.

Retained `hang` total time was 5,027,171,697 / 5,029,443,040 /
5,030,328,140 ns and terminate-to-reap was 1,330,066 / 1,611,492 / 4,472,233
ns (min/median/max). Retained `ignore_term` total time was 5,277,453,257 /
5,279,684,091 / 5,283,453,396 ns, terminate-to-reap 251,652,898 /
252,257,744 / 255,281,578 ns, and kill-to-reap 1,206,092 / 1,221,070 /
1,283,321 ns.

## Transparent timing and RSS discrepancies

Timing and memory observations remain non-threshold evidence. Fresh snapshot
total time ranged 81,593,072–95,516,596 ns: three case ranges were higher and
non-overlapping, 44 were lower and non-overlapping, and 16 overlapped.
Parent-total relations were also 3/44/16. For higher/lower/overlap, launch was
14/2/47; reap 22/0/41; child import 0/16/47; child load 0/4/59; and child decode
1/2/60.

Fresh child max-RSS ranged 16,887,808–20,348,928 bytes: 18 case ranges were
lower and non-overlapping and 45 overlapped. Fresh parent cumulative
`ru_maxrss` ranged 42,094,592–48,640,000 bytes and was higher/non-overlapping
for all before/after comparisons because the verifier process had loaded pytest
and the candidate corpus. The fresh report preserves every per-case recorded
and reproduced triple and classification. No timing or RSS observation was
used as a threshold or changed a semantic/count verdict.

## Commands, cleanup, and artifacts

All commands were prefixed with `rtk` and Python runs set
`PYTHONDONTWRITEBYTECODE=1`.

- clean static verifier preflight — 3 passed, 1 deselected;
- clean complete 486-launch reproduction — 1 passed in 102.30 seconds;
- clean focused inert runner suite — 172 passed in 15.01 seconds;
- Ruff over the verifier and runner tools — passed;
- clean `python -m tools.cycle3_characterize.binding --check` — exit 0;
- `git diff --check` — exit 0;
- tool inventory/cache listing — exact nine allowed entries, no cache;
- isolated process audit — exit 1/no `cycle3_characterize` match.

Corrected verifier-test SHA-256:
`b29634ace872049ce275d93bc81274e0776236d688b6ef2cbbb243922b0db016`.
Fresh `/private/tmp/c3-b1-raw-baseline-verifier-report.json` SHA-256:
`4e3bf651dce57261a405a8c3bb9b4f163c45272e5dd98c0679714082da0a6f6f`.

`C3B1-RV001` is resolved. The exact immutable raw candidate passes fresh
independent verification under the clean verifier interpreter. No accumulated,
acceptance, threshold, operator, final-B1, manifest, or checkpoint pass is
transferred; dependent gates must consume this corrected verification evidence
in contract order.
