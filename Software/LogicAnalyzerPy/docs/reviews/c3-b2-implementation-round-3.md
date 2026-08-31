# C3-B2 private-host implementation — round 3

Identity: `c3-b2-private-host-implementor-replacement-5`.

Verdict: `candidate-ready`.

## Ordered binding and finding history

This work starts from current HEAD `555caa2` under governing contract
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. Rejected candidate
`7a8b2d1d513cf841ec1dc9cf01b2d209b7c518b1` and immutable verifier evidence
`a62ecc3` remain rejected evidence; neither transfers a verdict. Round 2
verification found C3B2-V002: a typed child result could contain inconsistent
declarations or an undeclared record output id.

## Implemented correction

`_decode_with_factory()` now invokes one `_validate_result_graph()` after
typed materialization and before timing/RSS accounting and return. It rejects
with stable `ipc` on invalid declaration collection indices/identity, malformed
annotation-row references, invalid frozen register kind/output-id pairings,
class-index overruns, metadata mismatches, record coordinate inversions or
extent overruns, and non-exact absolute/trigger-relative rational times. The
register ordering is the frozen API-v3 lifecycle ordering for UART, SPI, and
I2C; it is not derived from fixture records. Child failures still occur before
any result return and the hostile tests check descriptor closure and a fresh
worker recovery.

Current SHA-256 values are `host.py`
`b913febe115299aa761e913e9f953c9acfdcda6f076fdfaffa29e2a4ca9e3e71` and
`test_c3_b2_private_host.py`
`e3da648cb4dccbf97023a886a43a616c7249ccb614fc692cadde79e7508323c4`.

The implementation test adds a 16-row hostile adjacency matrix covering
duplicate/gapped/reordered declaration indices, row-reference errors,
undeclared and cross-kind outputs, annotation/binary class bounds, metadata,
coordinates, and both rational time edges. Its isolated command passed:

```text
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run pytest -q -k closed_result_graph_edge tests/implementation/test_c3_b2_private_host.py
# 16 passed, 210 deselected in 5.31s
```

The immutable round-2 verifier command also passed:

```text
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run pytest -q tests/verification/test_c3_b2_private_host_round2.py
# 35 passed in 7.92s
```

Ruff, strict mypy, and `git diff --check` passed:

```text
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run ruff check src/pico_logic_analyzer/_decode tests/implementation/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host_round2.py
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run mypy --strict src/pico_logic_analyzer/_decode
rtk git diff --check
```

## Regression observation separation

The prior product-path conversion of regression observations into
`process-exit` was corrected. The eleven `REGRESSION_LIMITS` retain their exact
values but are now measured in a private per-call `_RegressionObservation` and
checked only by `_validate_regression_observation()`. The product path still
requires a metric frame with exactly the four expected non-negative integer
fields, but a valid metric above a regression ceiling no longer changes a
decode result. There is no public API, callback retention, or cross-call state.
Hard deadline, terminate-grace, kill, close, and reap behavior remains on the
product path.

The full product suites passed after that correction:

```text
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run pytest -q tests/implementation/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host.py
# 235 passed in 27.33s
rtk uv --cache-dir /private/tmp/cycle3-uv-cache run pytest -q tests/verification/test_c3_b2_private_host_round2.py
# 35 passed in 8.03s
```

Exact-candidate private observations passed the separate regression gate. A
successful worker measured the eight applicable success fields:

```text
worker_peak_rss_bytes=25812992; parent_retained_growth_bytes=241664;
successful_parent_total_ns=148854777; launch_ns=2076229; reap_ns=29946;
child_load_ns=6752369; child_import_ns=94301380; child_decode_ns=388717
```

A separate real fixed hostile child ignored `SIGTERM`; a test-only 50 ms hard
deadline and 10 ms grace forced the hard kill/close/reap path. Its three
applicable cleanup observations were nonzero and passed unchanged ceilings:

```text
timeout_cleanup_total_ns=67136142; terminate_to_reap_ns=11203769;
kill_to_reap_ns=738074
```

`timeout_cleanup_total_ns` is measured from the original run start, not just
the reap helper. No product decode or cleanup path invokes a regression-limit
validator; the existing pure validators remain evidence-gate helpers only.

The added implementation row verifies that an over-ceiling but structurally
valid observation returns product success while the independent gate rejects
the same observation. Earlier scheduling-load failures remain immutable
historical evidence of the corrected defect, not a current verdict.

The API-v3 frozen lifecycle also permits an interval end coordinate equal to
the capture extent (`put(..., es <= len(samples))`), and existing B1 golden
records use that terminal endpoint. The validator preserves that frozen
semantics rather than changing the accepted lifecycle or fixtures.

No C# or external decoder was executed; no public API, CLI, dependency,
fixture, B1, progress, contract, verifier artifact, B3+, or Cycle 4 path was
modified. This record is implementation evidence only and does not replace an
independent verifier or acceptance verdict.
