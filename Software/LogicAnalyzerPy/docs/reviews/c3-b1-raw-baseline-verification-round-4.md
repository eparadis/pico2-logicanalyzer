# C3-B1 raw-baseline verification — round 4

Verdict: `pass`.

## Immutable subject and verifier scope

- Verifier identity: `c3-b1-raw-baseline-verifier-replacement-1`.
- Raw candidate commit/tree: `d0d9dbe87f7841f09f261556de0909475e048b95` / `a749b4e192246afab34eb6f11438d64eaeaa4d0c`.
- Assignment descendant: `484f792b79693ab1d0b6f0773c21f4fb19ce445f`.
- Accepted runner candidate: `380d5dd77ae6c6f8648391e3c849c13c4b98fe8a` / `aa55b4884c39981026ba233b48dc8f360d404c8a`.
- Accepted runner chain: `01f059cb5f60e885c7d19e8bf5376bdb27dcca19` / `1c15252a26e5a4af571228dbf37999e385026f87`.
- Corrected fixture candidate: `3af6b9f80dd52611e14acca407707d1da7b8d9ac` / `14c010153ea5542617e601e4126047c561a48483`.

The verifier owns only
`tests/verification/test_c3_b1_raw_baseline_candidate_replacement.py` and this
review. It did not modify or commit the raw candidate, existing verifier,
fixture, runner, threshold, final, product, B2, hardware, network, or Cycle 4
state. It did not run any B2, threshold, final, product, or downstream suite.

## Static and structural verification

The static preflight passed three tests with the complete reproduction test
intentionally deselected. It independently derived exactly 63 requests from
timeline transitions, physical-channel mapping, sample count, samplerate,
options, and provenance source sets before comparing the resulting closed
request documents. It did not use raw requests or expected records to derive
an execution request.

The preflight verified canonical encoding and closed schemas for all five raw
documents; exact manifest closure; all 63 timeline identities; five retained
repetitions per timeline; the full ten-kind hostile profile; all summary
min/median/max arithmetic; exact environment provenance; all 17 production
caps; all nine frozen source digests; and the accepted binding, runner,
fixture, and fixture-manifest identities. Non-vacuous mutations of manifest,
snapshot-summary, and hostile-cleanup data were rejected.

Exact candidate SHA-256 values:

- environment: `d0c038a17b09f8b66b81d07e42ccae9d36ca5fce08dc252ccea491c69e18aa6f`
- requests: `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`
- observations: `ba2c7bd1c8a4ea832f6037d311a212c2abbecf9c9c9d67d40eb5a079110c29ee`
- hostile observations: `af86b3765cc32298003f140312b79640963d3ac7d61b9b259a871827b5522d91`
- manifest: `5d08929c7af59840ecbb01232c17b3c730161f9b8478e53bfd51fe6b3ea761b8`
- collection review: `75822b3dd81bba77701b57628126cc643b0b96595133d094208ecc152b386e01`

## Single fresh uninterrupted reproduction

Exactly one fresh complete reproduction ran and passed in 101.61 seconds. No
reproduction was restarted or repeated. Its exact accounting was:

- 63 snapshot warm-ups plus 315 retained snapshot launches;
- ten hostile warm-ups plus 50 retained hostile launches;
- eight recovery warm-ups plus 40 retained recovery launches;
- **486 child launches total**.

All 63 snapshot cases produced the recorded canonical semantic result and the
eight stable count fields on every retained repetition. The two designed
hostile successes completed, all eight expected failures failed as classified,
and all 40 retained recoveries succeeded. Every snapshot, hostile, and
recovery child was reaped and closed exactly two protocol descriptors. The
timeout/flood paths terminated and reaped; `ignore_term` reached kill and reap.
No bytecode cache or characterization process survived the gate.

Retained `hang` total time was 5,026,178,081 / 5,027,301,824 /
5,028,756,798 ns and terminate-to-reap time was 1,574,964 / 1,692,275 /
4,188,498 ns (min/median/max). Retained `ignore_term` total time was
5,277,680,031 / 5,277,958,260 / 5,282,587,393 ns, terminate-to-reap time was
250,172,233 / 250,388,914 / 254,978,441 ns, and kill-to-reap time was 954,467 /
1,267,789 / 1,566,631 ns.

## Transparent timing and RSS discrepancies

Timing and RSS values were retained only as transparent observations. They
were not thresholds and did not affect semantic or stable-count verdicts. The
report retains fresh and recorded triples plus an explicit range relation for
each of the 63 cases.

Fresh total time ranged 79,809,725–97,681,249 ns: 52 case ranges were lower
and non-overlapping and 11 overlapped. Parent total had the same 52/11 split.
For lower/higher/overlap respectively, launch relations were 2/3/58; reap
1/0/62; child load 5/0/58; child import 18/0/45; and child decode 16/0/47.

Fresh child max-RSS ranged 16,891,904–20,398,080 bytes: seven case ranges were
lower and non-overlapping and 56 overlapped. Fresh parent cumulative
`ru_maxrss` ranged 41,046,016–48,713,728 bytes and was higher and
non-overlapping for all 63 before/after comparisons, as expected for the
pytest verifier process. No value was promoted into a threshold.

## Commands and artifacts

Every shell command began with `rtk`; Python validation used the repository
CPython 3.12 environment and `PYTHONDONTWRITEBYTECODE=1`.

- static verifier preflight: 3 passed, 1 deselected;
- single complete reproduction: 1 passed in 101.61 seconds;
- Ruff over the replacement verifier: passed after import normalization;
- `git diff --check` over the verifier: passed;
- characterization inventory: exact nine permitted files and no cache;
- process audit: no characterization, snapshot-host, private-decode, browser,
  Vite, or server process matched.

Verifier-test SHA-256:
`d61e45363cb461a198e5d9c14aea8a7d27543968c9bf2ee79d6b3a38dbd56d3f`.
Fresh report SHA-256:
`be83d2258261f4b25c2c518669ab612dd9fc3bd25b835807f0beea3032ca089f`.

`pass`
