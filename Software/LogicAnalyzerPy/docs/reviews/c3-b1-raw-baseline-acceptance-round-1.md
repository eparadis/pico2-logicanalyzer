# C3-B1 raw-baseline acceptance — round 1

## Identity, subject, and authority

- Acceptance identity: `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`), reused only in its independent acceptance
  role and distinct from the raw-data author and verifier.
- Immutable raw candidate commit/tree:
  `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`.
- Unchanged corrected runner commit/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`.
- Independent raw verification pass commit:
  `9ac10d77cf1e8c492e7b5dae564baa43b09ebf71`.
- Accumulated-validation pass commit:
  `b49bd4932c4c091529b6c93f45de1f3f807e83f2`.
- Acceptance assignment commit/tree:
  `af4b83c3e611e940fa46a6ce5fa14f176a178bf8` /
  `2cb54da0ff748590a37bc4ee792acfe146c06cee`.

I used only static inspection and already committed immutable evidence. I did
not execute a runner, snapshot, decoder, or hostile probe. I repaired no audit
input and created only this record.

## Findings and dispositions

1. Candidate immutability and scope: no discrepancy. The candidate adds exactly
   five canonical, non-executable JSON files under
   `testdata/decoders/cycle3-raw/`. Those files remain byte-identical to the
   candidate. Corrected runner/method and accepted fixture/cap/snapshot paths
   are quiet against their immutable owners. No expected output, cap, product,
   governing, workflow, or excluded-scope byte was added or changed.
2. Authorship and ordering: no discrepancy. Final runner implementor
   `c3-b1-pre-execution-runner-implementor-replacement-3` owns the raw data;
   verifier `c3-b1-pre-execution-runner-verifier-1` independently derived and
   reproduced it; this acceptance identity is distinct from both and from all
   fixture authors. The immutable order is raw candidate, verifier assignment,
   verifier pass, accumulated validation, and acceptance assignment. No earlier
   runner-gate verdict transfers as a raw-baseline verdict.
3. Raw packet completeness: no discrepancy. Static JSON inspection finds 63
   ordered requests and 63 matching observation entries, each with one status-
   only unrecorded warm-up, five retained repetitions, and a summary. It finds
   ten hostile entries with the same warm-up/five-repetition structure,
   classification, and summary. Environment evidence binds Python 3.12.13,
   macOS 15.7.7 build 24G720, x86_64 `Macmini8,1`, resource mechanisms, exact
   17-cap profile, runner/fixture identities, source/configuration/collector
   digests, serialized restart history, and the fixed method. Manifest closure,
   canonical JSON, coverage, decoder set, repetition count, counts, timings,
   resources, results, and min/median/max arithmetic were independently
   recomputed.
4. Independent reproduction: valid and complete. The verifier derived all 63
   requests only from transitions, mapping, sample count, samplerate, options,
   and provenance file sets before comparing raw requests. It did not load
   expected calls, waits, records, typed vectors, or golden bytes as an oracle.
   A final uninterrupted reproduction performed one warm-up plus five retained
   runs per case and the complete ten-case hostile/recovery matrix. All stable
   semantics and counts reproduced; framing/accounting/caps, termination,
   forced kill, descriptor closure, exact reap, recovery, cache cleanup, and
   process cleanup passed.
5. Timing and RSS discrepancies: transparently complete and non-normative.
   Fresh total-time ranges were lower and non-overlapping for 61/63 cases; only
   `direct-uart-parity-zero` and `direct-uart-tx_packet_delim-31` overlapped.
   Child max-RSS overlapped for 58 cases and was lower/non-overlapping for
   exactly `direct-uart-data_bits-8`, `direct-uart-format-oct`,
   `direct-uart-parity-zero`, `direct-uart-tx_packet_delim-0`, and
   `direct-uart-tx_packet_delim-127`; none was higher/non-overlapping. Other
   timing and parent-RSS fields varied as recorded. No value was discarded,
   substituted, converted to a threshold, or used to weaken a cap.
6. Accumulated validation: complete. The fresh hash-locked Python 3.12.13 gate
   passed Ruff, both strict mypy scopes, fixtures, binding, 596 unrestricted
   non-hardware tests with no skip, installed help, 18 fixture and 190 runner
   focused tests, all six Cycle 2 validators, Cycle 1 hashes, 64-GiB resource
   feasibility, package/dependency/import/scope/cache/process checks, and the
   full raw reproduction. Exact Node 22 passed clean install, lint, type, five
   unit tests, 29-module build/assets, four browser tests, and one performance
   test. The mistaken nonexistent asset-checker command was explicitly
   discarded; the governed Python checker passed.
7. Unrelated user instruction commit: correctly qualified. Commit
   `c9364035d330f44045f2c0b627c4184da24dc42b` changes only root `AGENTS.md`,
   follows verification and precedes the accumulated record, and is explicitly
   retained as a user-directed unrelated descendant. It changes no raw,
   runner, method, fixture, snapshot, cap, product, or governing candidate byte
   and supplies no Cycle 3 evidence claim.
8. Cleanup, provenance, legal, and exclusions: no discrepancy. The recorded
   run and reproductions left no worker or bytecode cache; final process and
   repository audits were clean at their evidence boundaries. Exact nine-file
   provenance and the accepted project/legal disposition remain unchanged.
   No threshold proposal or decision, expected-output oracle, product host,
   public decode API, hardware/firmware/live capture, external decoder runtime,
   packaging/publication, unsupported-platform claim, or Cycle 4 work occurred.

No finding is open.

## Static checks and immutable hashes

- Commit/tree/parent inspection for candidate, verification, unrelated
  instruction, accumulated pass, and assignment: passed.
- Raw candidate quiet diff against `397981ad...`: passed.
- Corrected runner/method quiet diff against `48d139f...`: passed.
- Accepted fixture/cap/snapshot quiet diff against `7c57a34...`: passed.
- Static JSON schema-shape/count inspection: 63 requests, 63 observations, ten
  hostile observations, and five retained repetitions per entry.
- Final targeted RTK process query returned only its transient query PID, which
  had exited when inspected; no runner, worker, decoder, pytest, Playwright, or
  Vite process remained.

SHA-256 values independently recomputed from the assignment descendant:

- environment: `14da4608cf882286a8f62f0e59f596d91753244b619046d14d7f445a89012a4f`;
- hostile observations: `c956be536fc1fd5c23ebfd33b6bb51377e0f806ace57dfc02fc8888521f801ad`;
- manifest: `0706b84a0965a36e5b5d20c35c6d4ba9ab774f3bb7532e29f322dcd5a76d0efa`;
- observations: `a282ccd92ffa27ceda4624d6138de61d48314a0b352f004e3d0770c8b3bc2f03`;
- requests: `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`;
- verifier test: `08687a9bcc7fed1cfb55dbb6ec9b3c31f2ea486cfd389857916d6039b33567ca`;
- verifier record: `c9c08720039de278c12c54501e09c71634f084408330af849011004a666441c2`;
- accumulated record: `839bc5aae57a179007acbf405c7f1ce5c6484c51a7d997650e01e1cbcba879ee`.

## Safety and authority statement

This acceptance executed no snapshot, private snapshot route, decoder,
compatibility helper, hostile probe, fixture generator, product host, hardware,
network action, external runtime, browser server, publication, or excluded
capability. No worker remains. A pass authorizes only threshold-proposal
preparation from the exact immutable evidence; it approves no numeric value.

## Verdict

`pass`
