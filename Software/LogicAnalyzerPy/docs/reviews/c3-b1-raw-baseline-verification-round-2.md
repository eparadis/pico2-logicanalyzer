# C3-B1 raw-baseline verification — round 2

Verdict: `pass`.

## Identity, authority, and scope

Verifier `c3-b1-pre-execution-runner-rebinding-verifier-1` continued only in
its independent verifier lane, distinct from the raw-data author. I verified
raw candidate commit `2ae1e4335c38a5cf717491c7936f857292f71498`, tree
`772b13476c97a976eb3a304e9b87aec8011260ec`, against governing contract commit
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`.

The raw candidate's parent is accepted runner-chain commit
`bf1fc5eaa232bf09e66df77bd1c4be3e1ae4ffbd`; accepted runner candidate
`ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` and corrected fixture candidate
`a98d328aab92f3dad66988fb70cc567946dc89d0` are both ancestors. No runner verdict
was transferred to the raw candidate.

The candidate changes only environment, observations, hostile observations,
and manifest under `testdata/decoders/cycle3-raw/`; unchanged `requests.json`
is the fifth member of the closed raw set. I changed only verifier-owned
`tests/verification/test_c3_b1_raw_baseline_candidate.py` and this record. I did
not inspect or modify either untracked B2 path. No fixture, runner, method,
threshold, final-B1, checkpoint, product, dependency, hardware, network, C#,
.NET, or external decoder path was changed or executed.

## Candidate identity and static verification

All five raw files are canonical newline-terminated JSON with exact closed
schemas. Their SHA-256 values are:

- environment: `fd8b2cd798678d0b9c6cb6b1e71e02ec71738183a1e5b84ebd71fb90ee7c7b34`
- requests: `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`
- observations: `28e1b9a2276eda2ca1c4cc1e8740b774e29125521aca5e45c31f3e4b1e8791cd`
- hostile observations: `d8ef77f4293ff1e49d5772b6bb44df61f3dc4cfa37ceda13dcb54a3cce74d080`
- manifest: `7c964750841e80d0c4bad606d2b76da8575a330d65836aaca8a9284a0668608e`

The closed environment and manifest independently reproduce the exact binding
`144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`, caps
`6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`,
semantic fixtures `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`,
fixture manifest `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`,
and runner acceptance record
`6dae8c73787dc7908e0ec311c84325251482d32073cc2fd6083147ead943e060`.
The exact nine provenance source digests, 17-cap values, Python 3.12.13
executable/version, macOS 15.7.7 build 24G720 x86_64 `Macmini8,1` environment,
one-warm-up/five-retained rule, and resource mechanisms all match.

I independently derived the complete ordered 63-request set before reading the
raw request list for comparison. Derivation used only static transitions,
logical-to-physical mapping, sample count, samplerate, options, and provenance
file sets. Expected calls, waits, records, typed vectors, golden bytes, and
historical observations were not used as request or execution oracles. All 63
derived requests matched byte-for-structure. The verifier independently
recomputed every stored observation and hostile count/field/cleanup
min/median/max summary. Mutation checks prove a changed manifest digest,
snapshot summary, and hostile cleanup summary are rejected.

## Fresh reproduction

The final uninterrupted reproduction performed 486 child launches:

- 63 snapshot warm-ups plus 315 retained snapshot executions;
- ten hostile warm-ups plus 50 retained hostile executions;
- eight recovery warm-ups plus 40 retained recovery executions after each
  expected-failure hostile kind.

All 63 snapshot cases succeeded five of five. Every fresh canonical semantic
value and every stable input-sample, request-byte, output-record, binary-byte,
nested-depth, nested-item, stdout-byte, and stderr-byte count matched the
committed raw observation. Each of the 378 snapshot launches completed, was
exactly reaped, closed both raw protocol descriptors, and left no partial
result or worker.

`limits` and `address_space_over` succeeded five of five with exact values and
counts. The other eight kinds failed five of five as classified, discarded
their results, and each was followed by a valid successful recovery. All 90
retained hostile/recovery executions matched stable values/counts and were
reaped with both descriptors closed. Retained dispositions were:

- `hang`, `stdout_flood`, and `stderr_flood`: five each
  `terminated-and-reaped`;
- `ignore_term`: five `killed-and-reaped`;
- the remaining six kinds: five each `completed` (cleanup disposition, not a
  success classification).

For `hang`, retained total time was 5,029,612,158 / 5,030,838,311 /
5,031,945,311 ns (min/median/max), with terminate-to-reap 1,203,206 /
1,521,132 / 1,610,477 ns. For `ignore_term`, total time was 5,278,777,482 /
5,280,722,423 / 5,285,865,959 ns, terminate-to-reap 250,158,895 /
250,424,919 / 257,146,466 ns, and kill-to-reap 1,028,602 / 1,036,833 /
1,395,923 ns.

No `cycle3_characterize` process remained; a direct post-run process query
returned no match. The tool directory contained exactly its nine allowed
entries and no `__pycache__` or bytecode file. Combined process queries
intermittently encountered a local `sysmond service not found` error; each
isolated query immediately reran successfully with exit 1/no matches.

## Timing and RSS observations

Timing and RSS are observations, not thresholds. The complete per-case fresh
and recorded triples and relation classifications are retained in the verifier
report. Fresh snapshot total time ranged 93,833,496–115,330,594 ns: 34 cases
were higher and non-overlapping with the committed range, while 29 overlapped.
No total-time range was lower and non-overlapping.

Across the other timing fields, higher/non-overlapping versus overlap counts
were: parent total 35/28, launch 13/50, reap 23/40, child import 6/57, and child
decode 2/61. Child load had three higher/non-overlapping, one
lower/non-overlapping, and 59 overlapping cases. These differences changed no
semantic or stable count.

Fresh child max-RSS ranged 17,797,120–21,188,608 bytes. Exactly
`direct-uart-bit_order-lsbnegfirst` and `direct-uart-stop_bits-0p0` were higher
and non-overlapping; the other 61 overlapped. Parent process-wide cumulative
`ru_maxrss` ranged 42,729,472–52,051,968 bytes and was higher/non-overlapping
for all 63 before/after case comparisons, consistent with the verifier process
having already loaded pytest and candidate data. No RSS result is treated as a
cap, threshold, failure, or substituted measurement.

## Commands and artifacts

All commands were prefixed with `rtk` and Python execution used the
repository-local 3.12 environment with `PYTHONDONTWRITEBYTECODE=1`.

- candidate/tree, parent, ancestry, and four-path diff audits — passed;
- SHA-256, canonical JSON, schema, manifest closure, environment, provenance,
  request derivation, arithmetic, and mutation preflight — 3 passed, 1
  reproduction test deselected;
- fresh complete reproduction — 1 passed in 108.96 seconds;
- focused inert runner suite — 172 passed in 14.93 seconds;
- Ruff over verifier and runner tools — passed;
- `python -m tools.cycle3_characterize.binding --check` — exit 0;
- `git diff --check` — exit 0;
- isolated `pgrep -fl cycle3_characterize` — exit 1/no matches;
- tool-directory cache/inventory listing — exact nine allowed entries, no
  cache.

Verifier test SHA-256:
`895a0cead7038eccd3993b9493169652910ac8a24ad84a843211af49a461474c`.
Fresh `/private/tmp/c3-b1-raw-baseline-verifier-report.json` SHA-256:
`373f66bd0d28af15bbdf394ebe94c07133235365912a429a98baeeede5a86916`.

The exact raw candidate therefore passes fresh independent verification. This
verdict does not transfer accumulated-validation, acceptance, threshold,
operator, final-B1, manifest, or checkpoint evidence; those gates remain to be
performed in contract order.
