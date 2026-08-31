# C3-B2 private-host implementation — round 1

Identity: `c3-b2-private-host-implementor-replacement-3`.

Implementation provenance is ordered and non-transferable. Identity
`c3-b2-private-host-implementor-replacement-1` produced rejected immutable
candidate `a24b14c` / tree `56cd862...` under finding `C3B2-II001`; no verdict
transfers from it. Identity `c3-b2-private-host-implementor-replacement-2`
produced only uncommitted partial increments through 143 focused passes and
explicitly reported not candidate-ready; no verdict transfers from those bytes.
Replacement-3 inherited those uncommitted bytes, completed and audited them,
owns this current implementation handoff, and reports 198 focused passes.

This implementation handoff is not a verification, acceptance, manifest, or
checkpoint verdict. It is bound to contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree
`d9fb09345ab85580cd8c877745262d1b481e366f`, corrected B1 checkpoint
`d4f984d26ca45dcd0f70da51ad739da427e23be4`, semantic fixture `3af6b9f`,
runner `380d5dd`, and B1 joint manifest `885be61` / SHA-256
`3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`.

The private `_decode` surface provides immutable request/result/failure models,
closed UART/SPI/I2C identity and hash checks, closed pre-spawn validation,
frozen API-v3 primitives, a fresh fixed `-I -B` FD-only worker, bounded v1
length-framed IPC, safe failure conversion, deadline and terminate/kill/reap
cleanup. It introduces no public decode API or CLI.

All 29 literals bind to round-4 proposal `b680aa5` and approval `afd4585`,
including parent retained growth `33554432`, successful parent total
`1300000000` ns, launch `50000000` ns, and SPI word size `8`; limits are
inclusive and focused tests exercise first rejection.

This replacement specifically changes the parent lifecycle. `CancellationToken`
is parent-owned and is checked before identity/pre-spawn and while waiting;
cancellation produces the stable `cancelled` failure. The parent uses a single
wall-clock deadline across response/stdout/stderr draining, caps stdout at the
approved 65,536 bytes (not the 2,097,152-byte encoded-result cap), rejects
oversize response traffic, then deterministically terminates, waits for the
250 ms grace, kills if necessary, closes descriptors, and reaps. Successful
launch and total-parent timing ceilings are checked from parent monotonic time.
The fixed v1 result frame now additionally requires exact child import/load/
decode timings and `ru_maxrss`; the parent rejects missing, extra, non-integer,
negative, or above-ceiling metrics before materializing a result. On the
supported macOS platform `ru_maxrss` is bytes. Parent retained growth exactly
mirrors the B1 proposal test: `parent_after.ru_maxrss -
parent_before.ru_maxrss`, with the approved 33,554,432-byte inclusive ceiling.
The parent now uses a selectors-based bounded drain, so it leaves no daemon
reader behind, and maps stream overflow to `output-limit`.

Focused results (replacement worktree):

- `uv run pytest -q tests/implementation/test_c3_b2_private_host.py`: 198 passed;
- `uv run ruff check src/pico_logic_analyzer/_decode tests/implementation/test_c3_b2_private_host.py`:
  passed;
- `uv run mypy --strict src/pico_logic_analyzer/_decode`: success, 9 source files;
- `git diff --check`: passed.

Coverage includes all semantic timelines through fresh workers, canonical
values, hostile malformed/oversize/truncated/extra IPC, cyclic/non-finite
values, mapping/options and SPI boundary negatives, identity/import-root
checks, lifecycle failure, worker reaping, and recovery after preflight
failure, plus pre-spawn cancellation and the independently asserted stdout
boundary. Post-check inspection found no private worker or focused pytest
process remaining.

Replacement-3 adds direct parent-boundary tests
`test_parent_boundary_hostile_child_failures_reap_and_recover`,
`test_parent_boundary_stream_exact_boundary_is_not_rejected`,
`test_parent_boundary_timeout_cancels_open_pipes_and_recovers`, and
`test_parent_boundary_cancellation_while_pipes_are_open_reaps_and_recovers`.
They run hostile nonzero and signal exits; truncated, extra, and oversized
response traffic; stdout/stderr first overruns; worker `memory`, `recursion`,
`decoder`, and `ipc` frames; open-pipe timeout; and cancellation through
`_decode_with_factory`, then run a new fixed-worker valid UART decode after
each category. The stream tests prove 65,536 settles while 65,537 is rejected
for each stream. A parent bug found by that matrix was corrected: an
unsuccessful child exiting before a complete frame is now `process-exit`, while
actual stream/response overrun remains `output-limit`.

Audit corrections add 50 ms bounded selector polling with a real cross-thread
cancellation test against quiet open pipes; cleanup for normal-wait timeout,
reap-time overrun, and request-write failure; and distinct injected total-run
and launch timer seams. The total timer begins at parent entry, while launch
times only worker spawning. Decoded JSON bytes and cycle-safe retained deep-size
accounting now reject independently of frame size before a result is returned.
The worker uses closed bootstrap constants, verifies them against the imported
limits, reads back `RLIMIT_AS` and recursion, and has exact limit-install
assertions. No unapproved CPU rlimit is installed. Successful result frames
must have empty stdout/stderr; bounded nonempty streams remain test-only
failure-path traffic.

Final direct result-frame tests construct a real settled UART result with a
closed v1 metric frame: one stdout byte and one stderr byte each reject through
the parent boundary, reap/close, and recover; empty streams succeed. Bootstrap
tests cover AS and recursion readback mismatch without changing the pytest
parent recursion setting.

The direct hostile-child rows additionally assert that every child is reaped
and both captured stdout/stderr descriptors are closed before recovery.
Response-FD closure follows the same `finally`/cleanup branch; this remains
implementation evidence, not independent B2 verification, acceptance, or a
candidate pass.

The final lifecycle additions directly retain the exact response FD and prove
`os.fstat` fails after post-drain normal-wait timeout and reap-ceiling paths,
request-write failure after a real Popen, and the successful fixed-worker path.
The write-failure row also proves the child is reaped and captured pipes close.

No prohibited runtime, external decoder, hardware, network, browser, public
surface, fixture/threshold/contract, B3+, or Cycle 4 change was made.
Independent B2 verification, accumulation, acceptance, and evidence remain.
