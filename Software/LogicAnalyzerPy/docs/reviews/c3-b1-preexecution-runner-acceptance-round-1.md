# C3-B1 pre-execution runner acceptance — round 1

## Identity, subject, and authority

- Acceptance identity: `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`), fresh independent acceptance lane.
- Exact runner candidate commit/tree:
  `11a8ade5d828830347095bf2580766c149cb8aef` /
  `61fa5ba18f3620188ee61dac7e3622803591aad9`.
- Accepted semantic-fixture commit/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Runner verifier pass commit:
  `8464a049c0809c9f0338c1cf7ad7ac90d1ec19eb`; accumulated-validation pass
  commit: `68529f97108f81d352d7a081068ec425719ee7bf`.
- Acceptance assignment commit/tree:
  `6583131178f0d8ade2ec36452d292e6bba7f3e5d` /
  `887403bcbfacbe351d1c22a3b6e1dd6c8415c85c`.

This audit grants no authority from the earlier fixture passes. It accepts only
the exact unchanged runner candidate for entry into the separately ordered raw-
baseline phase. I repaired no candidate, test, fixture, progress, contract,
product, decoder, helper, generator, or evidence input.

## Findings and dispositions

1. Candidate identity, ancestry, ownership, and byte equality: no discrepancy.
   The candidate commit has exactly the 11 assigned runner/method/test paths.
   Their bytes are unchanged at the assignment descendant. The accepted fixture
   surface is byte-identical to its named commit. The ordered runner-only author
   history is implementor-1, replacements 1 and 2, and final replacement 3;
   fixture authorship and all verifier/acceptance roles remain separate.
2. C3B1-RI001 through C3B1-RI012: closed. The immutable binding covers the
   accepted fixture/caps, method, complete tool surface, six fixture artifacts,
   and exact ordered nine-file snapshot set; launch configuration fixes Python
   3.12 `-I`, CWD, minimal environment, import/stdlib/source allowlists, and
   disables characterization probe mode. The protocol and diagnostic streams
   are separated and bounded. All 17 finite cap categories have value and
   rejected-boundary proof, including exact 64-GiB `RLIMIT_AS`, recursion,
   retained result, decoded/encoded and concrete value accounting. The actual
   fixed UART/SPI/I2C post-gate path is present. Public `characterize` remains
   disabled, and probe selection is absent from the characterization request.
3. Independent verification: valid and independent. Its immutable record and
   independently authored 21-test matrix bind the exact candidate, cover cap,
   digest/import/root/file/environment/CWD, framing/accounting, graceful and
   forced termination, descriptor closure, exact-child reap, recovery, fixed-
   route, option, and API-v3 behavior, and report `pass`. I reran only that
   inert/hostile non-decoder matrix: 21 passed in 2.81 seconds.
4. Accumulated evidence: complete for this internal gate. The authoritative
   corrected reruns replace the explicitly invalidated sandbox-skipped Python
   run and host-Node run: 590/590 non-hardware tests with no skip and the full
   Node 22 gate pass. The record also binds clean Python 3.12.13 bootstrap,
   locks, install/check/lint/type/help, 187 runner tests, deterministic fixture
   rebuild, Cycle 1/2 evidence, browser/performance regressions, package/import/
   dependency/process/scope audits, candidate quiet diff, and clean state.
5. Evidence ordering, provenance, method, scope, and safety: no discrepancy.
   Verification follows candidate creation; accumulated validation follows the
   verifier pass; this acceptance follows both. The method makes only truthful
   pending-execution claims and fixes warm-up/repetition, observations, and
   failure treatment. Accepted provenance, legal/project disposition, exact
   source bytes, fixture/cap identities, and excluded-scope limitations remain
   intact. Candidate changes do not expose the runner through the installed
   product or create raw results, thresholds, manifests, or checkpoints.

No finding is open.

## Checks and immutable hashes

- Commit/tree/parent inspection and candidate commit path audit: passed.
- Quiet diff of all 11 candidate-owned paths against `11a8ade5...`: passed.
- Quiet diff of the accepted fixture surface against `7c57a347...`: passed.
- `PYTHONDONTWRITEBYTECODE=1 rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_preexecution_runner_candidate.py`: 21 passed.
- Final `rtk ps` and targeted `rtk proxy pgrep` audit: the transient query PID
  had exited; no runner, worker, decoder, snapshot, or pytest process remained.

SHA-256 identities independently recomputed from the assignment descendant:

- binding: `0b9fc2a02eef194c48392db2903c6296e764c0fe9a8368d51c2551c83ed60682`;
- launch: `c6cf91ebc42d3770ffc239b531424a128a2cf06c5aa97ed99b980bc48a86c9f8`;
- runner: `cd70e895794ace146be5830aeb5fff99a3aaf009c0049eb730e69ab53e5a9d32`;
- worker: `69e8eaccad236c6ec746aa5fd2ca11c26ae47f4b7306323c9710e2603ed65be5`;
- snapshot host: `0da598c3facd1af89d34d6a82996a09a24b0cc4d691eb5c79f0ac576e051ab67`;
- accounting: `924f563067bb23fc838b9b63b05b7e209f656fab68ee9859df4839f270bbd2d5`;
- probes: `be0da3bdc27e0a228b946a339ca278b55466c48d24170552ee8eac3150942f2e`;
- method: `eb4349d60aad922381a64579e1584271ec035dfa80d52f16881709b5260e2837`;
- implementation test: `c97cd9a66b1a5fff6ec72565ca41008bc8874f9a929d01e84b2e582a379a9f4d`;
- verifier record: `a1ca9a6c75b6bdca682ef00c07a4bb72e48c69d18cc493d05ba812a5bb241024`;
- verifier test: `6dc7f48c7312a318f370c4e98de57aed72cec270e378339ccc44f05bbc15bf7a`;
- accumulated record: `2d2fb0281dcf51ffae8c87e4989ca2eb4a9cdf3da91cad220ac836a33af2289d`.

## Safety and scope statement

No decoder or approved snapshot ran. Neither
`_orchestration_execute_approved_snapshot` nor `execute_snapshot` was called.
No helper, fixture generator, product decode runtime, C#/.NET/pythonnet/
libsigrokdecode/sigrok runtime, hardware, network install, browser server, raw
characterization, excluded scope, or Cycle 4 action occurred. Only static
inspection and the already-defined inert/hostile non-decoder verifier probes
were used. No worker remains.

## Verdict

`pass`
