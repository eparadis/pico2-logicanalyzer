# C3-B2 independent verification — round 1

Identity: `c3-b2-private-host-verifier-replacement-1`.

Verdict: `changes_required`.

## Immutable candidate binding

Verification inspected implementation candidate
`2e4e5ce215e619d19a1f1e26646ebc595ff7c903`, tree
`51424b7c9b3b3f7bca470eae3c54ba39f9bc8d84`, under governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. Current HEAD was the later
progress-only commit `40cc0e39f09efb815ecba80d84bb41bfba2ff0d9`; its only changed path was
`docs/cycle-3-orchestration-progress.md`. The candidate tree and its five owned
paths remained exact.

Candidate file SHA-256 values independently recomputed from the worktree were:

- `src/pico_logic_analyzer/_decode/host.py`:
  `b1e473983b7cf72a0e191abfb693912ecbc3cd620922685e6ba30257960b2628`;
- `src/pico_logic_analyzer/_decode/ipc.py`:
  `f3502eba02c66c957c6fc12a9d6c7e181d8c5e0c8e75ea75cb59c8027c460114`;
- `src/pico_logic_analyzer/_decode/worker.py`:
  `9a01a2c03ecb255fb3dddc43036a8d4ba3b7b62923e4a687748a1db70ffdb160`;
- `tests/implementation/test_c3_b2_private_host.py`:
  `20f80b0e14c08a85a3c0f996962bb815dcb5d23018cf81dfb1486910d6091bef`;
- `docs/reviews/c3-b2-implementation-round-1.md`:
  `0e3c76715a4cfa0f3fa9c899afdf7130fdb1daf271c002db1bc156e9f8aede35`.

The corrected B1 manifest, fixture manifest, round-4 threshold proposal and
operator approval were treated as authoritative inputs. The verifier derived
the result/request binding requirement directly from R6, R9, the closed
request/result schema, and the B2 inert-code-selection boundary. Production
counters were not used as an oracle.

## Finding C3B2-V001 — hostile child can replace validated result identity

Owner: C3-B2 implementation. Status: open.

The parent validates and pins the request before launch, but after reading a
syntactically valid `decode-result/v1` it validates only the returned object's
local shape and resource metrics. It never compares the materialized result to
the validated request or the `DecoderIdentity` returned by `verify_decoder`.
Consequently a child frame can replace each of the following independently and
still be returned as success:

- decoder ID (`uart` to `i2c`);
- pinned file-set SHA-256;
- samplerate;
- capture sample count;
- channel-to-physical mapping; and
- materialized options.

Exact reproducer:

```text
uv run pytest -q tests/verification/test_c3_b2_private_host.py
```

Observed result: `6 failed, 2 passed`. Every failure is `DID NOT RAISE
HostFailure` at the parent boundary for one independently mutated identity
class. The hostile subprocess emits a closed, length-framed version-1 result
with empty stdout/stderr and valid independent zero-valued child metrics. It
does not import an implementation-test helper. Each row then invokes a fresh
real fixed worker and confirms recovery, so the finding is not a retained-state
or poisoned-global artifact.

This violates R6's requirement that identity/files/data cannot select code,
R9's deterministic typed identity, and the B2 closed result contract. It also
allows a successful result to claim a different decoder/hash/capture than the
single preflighted execution. The result must be rejected atomically (stable
private failure, no partial success) unless all request-derived and
verified-identity fields agree exactly.

The finding is independently actionable at
`_decode_with_factory`: retain the verified identity/request-derived expected
projection and compare it with the validated response before returning. Any
correction creates a new immutable implementation candidate and requires fresh
verification; this record and its verdict do not transfer.

## Other verification observations

The independent suite additionally observed no descriptor-set growth across a
fresh valid decode and confirmed that neither `decode_private` nor
`decode_capture` is exported from the package root. Static inspection found the
worker invocation fixed to the package-owned worker path with `-I -B`, a closed
environment, FD-only request/response transport, no request-selected module or
path, no in-process mode, no new public CLI/API, no CPU rlimit, and macOS-only
`ru_maxrss` assumptions stated without extending the platform claim.

The candidate implementation suite covers the broader malformed/duplicate/
nonfinite IPC, option/mapping, output/tag/coordinate, process-exit/signal,
timeout/cancellation, stdout/stderr/response flood, cleanup, metric mutation,
retention, recursion and address-space boundary matrix. Those implementation
checks all pass, but they do not exercise the cross-object result/request
binding defect above. Because this decisive open finding rejects the candidate,
this round does not claim complete independent proof for every adversarial
class, non-macOS containment, hardware, B3 conformance, or any future public
surface.

## Commands and results

- `uv run pytest -q tests/implementation/test_c3_b2_private_host.py` — pass,
  exactly `198 passed in 13.77s`.
- `uv run pytest -q tests/verification/test_c3_b2_private_host.py` — expected
  verifier failure, `6 failed, 2 passed in 1.19s`, reproducing `C3B2-V001`.
- `uv run ruff check src/pico_logic_analyzer/_decode
  tests/implementation/test_c3_b2_private_host.py
  tests/verification/test_c3_b2_private_host.py` — pass.
- `uv run mypy --strict src/pico_logic_analyzer/_decode` — pass, 9 source
  files.
- `git diff --check` — pass.
- Central process inspection (`rtk ps -axo pid=,command=`) was denied by the
  execution sandbox. No direct approval was requested by this verifier; root
  must perform the already-governed centralized process audit if it remains
  required for this rejected candidate.

No implementation, implementation test/review, B1 artifact, contract,
dependency, manifest, progress record, public surface, B3+, or Cycle 4 path was
modified. Verifier-owned evidence consists only of this review and
`tests/verification/test_c3_b2_private_host.py`.
