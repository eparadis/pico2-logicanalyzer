# C3-B1 raw-baseline verification — round 1

## Identity, authority, and scope

- Verifier: `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), reused only in its verifier role and distinct
  from the raw-data author.
- Raw candidate commit/tree: `397981adf0f89115647203e749db1b1e5b3384cf` /
  `e4baf918c3de4b7df94ad51340bf5b5bfc8f16d2`.
- Unchanged corrected runner commit/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`.
- Reproduction assignment commit: `f47be7b4f58918943f30694d6737e00afa8d0508`.
- No pre-execution-runner verdict transferred to this raw candidate. I changed
  no raw, runner, method, launch, fixture, snapshot, expected-output, cap,
  product, progress, or governing byte.

## Independent request derivation and candidate audit

The verifier test independently derives all 63 ordered requests from only each
accepted timeline's transitions, logical-to-physical mapping, sample count,
samplerate, options, and the provenance decoder file sets. It does not read
expected calls, expected waits, expected records, typed vectors, or golden
bytes. Only after constructing the complete independent list does it load the
raw request file and require exact structural equality. All 63 matched.

The five raw files are canonical, non-executable JSON and the candidate adds no
other path. Their SHA-256 values independently reproduce as:

- environment `14da4608cf882286a8f62f0e59f596d91753244b619046d14d7f445a89012a4f`;
- hostile observations `c956be536fc1fd5c23ebfd33b6bb51377e0f806ace57dfc02fc8888521f801ad`;
- manifest `0706b84a0965a36e5b5d20c35c6d4ba9ab774f3bb7532e29f322dcd5a76d0efa`;
- observations `a282ccd92ffa27ceda4624d6138de61d48314a0b352f004e3d0770c8b3bc2f03`;
- requests `fe5b345270eced91298250032411b6a85112c55baf46d3b71afb424ef385f94c`.

Manifest closure, all bound source/configuration hashes, accepted fixture and
runner identities, exact 17-cap profile, five-repetition summaries, and the
recorded executable/environment were recomputed. Reproduction used exactly
`/private/tmp/cycle3-clean-python/bin/python`, Python 3.12.13, on the recorded
macOS 15.7.7 / 24G720 x86_64 `Macmini8,1` host. The raw and runner path families
remain byte-identical to their named commits.

## Fresh snapshot reproduction

The final uninterrupted verifier run performed one fresh unrecorded warm-up
and five fresh executions for each independently derived request: 378 exact
private fixed-snapshot-route calls. For every case, all five fresh canonical
records, text, binary, registration/output-type counts, address-space and
recursion diagnostics reproduced the committed observation semantics exactly.
Stable input samples, request bytes, output records, binary bytes, nested depth,
nested items, stdout bytes, and stderr bytes reproduced exactly. Encoded,
decoded, text, diagnostic, and retained sizes varied only with decimal lengths
of deliberately nondeterministic timing/memory diagnostics and remained within
the unchanged production caps. Expected fixture output was never loaded or
used as a runtime oracle.

All 63 cases succeeded five of five. Complete parent launch/reap/total,
child load/import/decode, child max-RSS, parent max-RSS, result/count, and
summary fields were present in both committed and fresh observations. Stored
min/median/max arithmetic was independently recomputed exactly.

## Fresh hostile reproduction and cleanup

The verifier independently repeated one unrecorded warm-up plus five retained
runs for all ten production-profile hostile cases. `limits` and
`address_space_over` succeeded as classified. `malformed`, `items`,
`stdout_flood`, `stderr_flood`, `diagnostic_flood`, `recursion_over`, `hang`,
and `ignore_term` failed as classified, discarded their results, and each was
followed by a fresh valid recovery. Every child was exactly reaped and all
subprocess streams plus both raw protocol descriptors closed.

- `hang`: five retained runs were `terminated-and-reaped`; total time
  5,024,338,444 / 5,027,258,840 / 5,028,616,267 ns and terminate-to-reap
  1,312,986–4,181,406 ns.
- `ignore_term`: five retained runs were `killed-and-reaped`; total time
  5,275,901,504 / 5,276,836,745 / 5,277,542,436 ns,
  terminate-to-kill 250,632,128–252,120,686 ns, and kill-to-reap
  1,026,783–1,195,120 ns.
- `stdout_flood` and `stderr_flood` were terminated and reaped after the parent
  stream caps fired. Other hostile failures had already exited and were reaped
  with disposition `completed`; this describes cleanup state, not success.

No worker or bytecode cache remained after reproduction.

## Transparent timing and memory discrepancies

Timing and memory are observations, not thresholds. Semantic/count equality
does not depend on their equality.

Per case, fresh total-time ranges were lower and non-overlapping with the
committed ranges for 61 of 63 cases. The two overlapping cases were
`direct-uart-parity-zero` and `direct-uart-tx_packet_delim-31`. Across all 63
cases, fresh total-time extrema were 79,779,065–96,074,984 ns; the per-case
committed values remain preserved unchanged. Child max-RSS ranges overlapped
for 58 cases. Fresh child max-RSS was lower and non-overlapping for exactly
`direct-uart-data_bits-8`, `direct-uart-format-oct`,
`direct-uart-parity-zero`, `direct-uart-tx_packet_delim-0`, and
`direct-uart-tx_packet_delim-127`; no case was higher and non-overlapping.
Fresh child max-RSS extrema were 17,068,032–20,344,832 bytes.

Thus every case is transparently classified: the two named timing cases
overlap and every other named candidate case is faster/non-overlapping; the
five named RSS cases are lower/non-overlapping and every other case overlaps.
Launch, reap, load, import, decode, parent-total, and parent-RSS values also
varied per execution as expected; no value was discarded or substituted, no
cap was approached, and no threshold conclusion is drawn from the difference.

## Commands and results

All shell commands used RTK shapes.

- Final complete clean-environment reproduction verifier: 3 passed in 101.18s.
- Independent identity/request preflight after formatting-only cleanup: 2
  passed, 1 deselected.
- Focused corrected runner suite: 167 passed in 14.84s.
- Ruff over the independent verifier: passed.
- Binding check, raw-candidate quiet diff, corrected-runner quiet diff, manifest
  closure, `git diff --check`, scope, cache, and process audits: passed.

## Safety and verdict

Only the authorized exact private snapshot route for the 63 independently
derived requests and the ten named inert/hostile probes ran. Expected fixture
output was not used as an oracle. No threshold proposal, cap change, product
host, hardware, network, dependency/install, C#/.NET, external decoder,
publication, or other prohibited action occurred. No worker remains. No
finding is open.

`pass`
