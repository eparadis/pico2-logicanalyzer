# C3-B2 independent verification — round 2

Identity: `c3-b2-private-host-verifier-replacement-2`.

Verdict: `changes_required`.

## Immutable binding and scope

This fresh verification is bound to replacement candidate
`7a8b2d1d513cf841ec1dc9cf01b2d209b7c518b1`, tree
`22d932214cd543bc3cbd0ef9b8d9b1ffad2bdfa0`, under governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. Verification began at later
progress-only HEAD `94da77845575eaa416d7dfdf6dbeaaaea29c6fd6`, tree
`52ddbb13bcc67235da718ffd3105b25746974acf`; candidate identity was resolved
before relying on worktree content. The B1 checkpoint, approved limits,
`C3B2-II001`, `C3B2-V001`, both implementation reviews, progress history, and
immutable failed round-1 verifier evidence were reviewed without modification.

Candidate SHA-256 values independently recomputed were:

- `host.py`: `d2fca4998d75b98bfc6d6f6cd3ad98bb4c42686158b05841d87189e23a0a83aa`;
- `model.py`: `19854e57491ff3b1271ed9e0012c878c0ed403b07f28bb5b17a9068d10e158e7`;
- `ipc.py`: `f3502eba02c66c957c6fc12a9d6c7e181d8c5e0c8e75ea75cb59c8027c460114`;
- `worker.py`: `9a01a2c03ecb255fb3dddc43036a8d4ba3b7b62923e4a687748a1db70ffdb160`;
- implementation test: `d353c3b8b30a1f5a1d1895a804d8dd2b577d4f3f286312d38c860d3036fea05b`;
- immutable round-1 verifier test/review:
  `58e68082bbcc3f1e8c3d4c572722c08110573d18e11f65453c98ae13d88d76cb`
  and `2da95bb7c9f5785249e75f46fa9246564991ccb58bf2802849e4808e46bcd743`;
- implementation reviews round 1/2:
  `0e3c76715a4cfa0f3fa9c899afdf7130fdb1daf271c002db1bc156e9f8aede35`
  and `cb9e5e5a882c06e34a1fa7b0407f584819540308a96e62d07057e14a22a107dc`.

## C3B2-V001 correction

The prior finding is closed for this candidate. New black-box hostile children
independently changed decoder ID, verified file-set hash, samplerate, sample
count, trigger index, decoder-channel name, physical channel, ordered mapping,
a locally valid but non-request-derived channel list, duplicate mapping,
missing and extra options, option value, and equal-looking option value with a
different type. Each identity-changing response now fails atomically as exact
`ipc`, closes the descriptor set, and is followed by a successful real fixed
worker with the exact retained request projection. A byte-equivalent valid
projection and benign option key reordering succeed and canonicalize exactly.

The expected projection was derived from pre-spawn request facts: verified
decoder/hash; scalar samplerate and capture length/trigger; mapping insertion
order and physical channel tuple; and the complete constructor-materialized
default option set with `(key, type, value)` identity. It does not use a child
claim or a production counter as its oracle.

## Finding C3B2-V002 — result cross-references are not validated

Owner: C3-B2 implementation. Status: open.

The parent accepts a locally typed `decode-result/v1` whose declarations and
records are internally inconsistent. Two independent hostile frames were
returned as success when `ipc` rejection was required:

1. an annotation declaration index was changed from the decoder's closed index
   to `99`, leaving annotation-row references inconsistent with the declaration;
2. a locally shaped annotation record used output ID `999`, which was never
   registered or declared by the result.

Both frames retained the exact request/identity projection, legal coordinates,
empty child streams, and valid metrics. Thus the defect is after the repaired
projection boundary and is not a recurrence of `C3B2-V001`. It violates R9 and
the settled register/put/output-validation contract: declaration indices,
record kinds/output IDs, annotation classes, and coordinates must be validated
as one closed graph before any result is returned. The verifier helper is
written to prove descriptor equality and a fresh real-worker recovery after
rejection; the current candidate's unexpected success prevents those
post-rejection assertions from being reached. No partial repair was made.

Exact reproducer:

```text
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run pytest -q \
  tests/verification/test_c3_b2_private_host_round2.py
```

Observed: `2 failed, 33 passed in 7.01s`; both failures are `DID NOT RAISE
HostFailure` in the two `declarations`/`records` rows above.

## Complete-contract audit and gates

The 33 passing new rows cover the complete C3B2-V001 projection, mapped order,
defaulted option identity/type, exact success, independently asserted numeric
boundary/value+1 behavior for child metrics, decoded/retained bytes, parent RSS
growth and cleanup timing, closed diagnostic/path/traceback behavior, descriptor
equality, recovery, and absence of package-root API, shell, `PYTHONPATH`, or
request-selected spawn code. Static inspection additionally confirmed fixed
`-I -B` worker launch, closed environment and FD-only IPC; digest/import-root
verification before spawn; no dynamic path or in-process mode; no prohibited
runtime/dependency or CPU limit; parent deadline/cancellation; bounded framed
response/stdout/stderr collection; terminate/kill/close/reap ordering; and the
narrow macOS `ru_maxrss` qualification.

The exact implementation suite supplies the exhaustive independently reviewed
matrix for IDs/hashes/paths/symlinks/import shadowing, request validation,
frames/versions/lengths/duplicates/nonfinite values, tags/coordinates/nesting,
exits/signals/exceptions/hangs, memory/recursion, stream/result floods,
cancellation races, partial/extra IPC, metrics/timing/RSS/readback, and fresh
success after failures. It passed unchanged, as did all eight immutable
round-1 verifier rows. Those passes do not override the new decisive output
graph finding.

Commands and results:

- `rtk uv --cache-dir /private/tmp/cycle3-uv-cache run pytest -q
  tests/implementation/test_c3_b2_private_host.py
  tests/verification/test_c3_b2_private_host.py` — exactly `218 passed in
  19.65s` (210 implementation and 8 immutable round-1 verifier rows);
- new round-2 verifier suite — expected finding reproduction, `2 failed, 33
  passed in 7.01s`;
- Ruff over nine private sources and all three B2 test paths — passed;
- strict mypy over nine private sources — passed;
- `git diff --check` — passed.

The rejected-candidate process-list audit is supplementary. Equivalent direct
descriptor equality, child wait/reap behavior in the inherited exact suite,
and real recovery evidence were available without `ps`; no approval was
needed. Claims remain limited to macOS/Python 3.12 process containment. No
hardware, network, browser, external decoder, C#, public API/CLI, B3+, Cycle 4,
dependency, contract, progress, B1, implementation, or immutable prior evidence
was modified. No prior verdict transfers to any repair candidate.
