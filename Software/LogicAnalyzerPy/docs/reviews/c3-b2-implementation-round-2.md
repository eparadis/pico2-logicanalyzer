# C3-B2 private-host implementation — round 2

Identity: `c3-b2-private-host-implementor-replacement-4`.

Verdict: `implementation ready`.

## Ordered identity and finding history

This repair is governed by contract `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree `d9fb09345ab85580cd8c877745262d1b481e366f`. It begins at HEAD `6423432` after rejected candidate `2e4e5ce215e619d19a1f1e26646ebc595ff7c903` and immutable verifier evidence `052401272b93bc94491e3301218e33fac94c8aac`. Neither the rejected candidate nor its `changes_required` verdict transfers to this worktree.

Replacement-1 candidate `a24b14c` was rejected under `C3B2-II001`; replacement-2 supplied incomplete uncommitted increments; replacement-3 completed candidate `2e4e5ce`. The round-1 verifier found `C3B2-V001`: a structurally valid hostile child frame could replace a result identity after request preflight. This replacement owns only that correction.

## Change and binding

`src/pico_logic_analyzer/_decode/host.py` retains an immutable projection before spawning the worker, sourced only from the validated request and verified `DecoderIdentity`. After structural validation, limit accounting, and typed materialization, the parent rejects with stable `ipc` unless the result exactly matches it. It binds decoder ID, verified file-set SHA-256, samplerate, capture sample count and trigger index, ordered decoder-channel/physical mappings and their capture channel identity, and all materialized options/defaults. Option comparison includes value type, so a locally valid `1` cannot substitute for expected `1.0`.

The check is before success timing/RSS accounting and return; no partial result escapes. It does not change worker selection, framing, limits, timing, cancellation, containment, cleanup, imports, or public surface.

`tests/implementation/test_c3_b2_private_host.py` adds parent-boundary rows for all six verifier mutations plus trigger metadata, ordered mappings, duplicate declarations, missing defaults, option value/type changes, exact valid acceptance, reap/descriptor closure, and fresh-worker recovery.

## Checks

- `uv run pytest -q tests/implementation/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host.py` — `218 passed in 19.14s` (210 implementation rows, including the prior 198 and 12 new rows; the committed verifier's 8 rows, including all six prior failures, passed).
- `uv --cache-dir /private/tmp/cycle3-uv-cache run ruff check src/pico_logic_analyzer/_decode tests/implementation/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host.py` — passed.
- `uv --cache-dir /private/tmp/cycle3-uv-cache run mypy --strict src/pico_logic_analyzer/_decode` — `Success: no issues found in 9 source files`.
- `git diff --check` — passed.

The initial static-check command could not access the sandboxed shared uv cache; the same checks passed with an isolated `/private/tmp` cache. No dependency was installed or changed.

## Changed artifacts

- `src/pico_logic_analyzer/_decode/host.py` — SHA-256 `d2fca4998d75b98bfc6d6f6cd3ad98bb4c42686158b05841d87189e23a0a83aa`.
- `tests/implementation/test_c3_b2_private_host.py` — SHA-256 `d353c3b8b30a1f5a1d1895a804d8dd2b577d4f3f286312d38c860d3036fea05b`.

## Residual scope

This is not verification, accumulated validation, acceptance, manifest, or checkpoint evidence. Fresh independent verification is required for the next candidate. No decoder-path selection, external decoder/runtime, hardware, dependency, public API/CLI, B3+, Cycle 4, or immutable round-1/verifier/progress artifact was changed.
