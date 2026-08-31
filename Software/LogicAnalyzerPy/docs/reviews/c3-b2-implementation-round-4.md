# C3-B2 implementation — round 4

Identity: `c3-b2-private-host-implementor-replacement-6`.

Verdict: `candidate-not-accepted`.

## Binding and disposition

This implementation is a correction of acceptance finding `C3B2-A001` in
`c3-b2-acceptance-round-1.md`, from starting state
`6825e88ce52279f3e75e1186a9462415194206c3`. It is governed by immutable
contract `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`; preserves corrected B1 checkpoint
`d4f984d`; approved limits proposal/decision `b680aa5` / `afd4585`; and does
not transfer authority from rejected candidate `d8e14bbe490035894f3103a1289b27464a89d0d6`,
its verifier records, or acceptance verdict.

`C3B2-A001` is addressed in the owned implementation worktree: request-pipe
delivery now runs inside the same parent-owned nonblocking selector lifecycle
as response, stdout, and stderr draining. This is implementation evidence
only; fresh independent verification, accumulated validation, and acceptance
remain required.

## Changed design

`host.py` now launches the fixed worker without writing the request. The parent
registers its request write descriptor for nonblocking write readiness and all
three child outputs for read readiness under one wall deadline and cancellation
loop. It handles partial writes, closes the request descriptor only after full
delivery, and continues simultaneous output drain. A broken request pipe maps
to stable `process-exit`; deadline and cancellation map to `timeout` and
`cancelled`. Every exceptional path terminates/kills, closes request and
response descriptors plus standard pipes, reaps the exact child, and discards
all partial buffers before any result handling.

No hard limit, regression ceiling, frame check, model, worker, IPC, public API,
CLI, B1 evidence, verifier, or acceptance artifact changed.

## Focused evidence

The owned implementation suite includes explicit hostile-worker cases for:

- a framed request larger than pipe capacity delivered to a worker that never
  reads (`timeout`), with close/reap and a following fresh decode;
- cancellation immediately after the observed partial request write
  (`cancelled`), with close/reap and recovery;
- a worker that closes/exits during large-request delivery (`process-exit`),
  with close/reap and recovery; and
- deterministic closure of both request and response parent descriptors on
  success and delivery failure.

Results on 2026-08-31:

- `Software/LogicAnalyzerPy/.venv/bin/python -m pytest Software/LogicAnalyzerPy/tests/implementation/test_c3_b2_private_host.py -q`: `232 passed`.
- the three immutable B2 verifier suites together: `75 passed`.
- Ruff over both owned Python files: passed.
- `mypy --strict Software/LogicAnalyzerPy/src/pico_logic_analyzer/_decode`:
  `Success: no issues found in 9 source files`.
- `git diff --check`: passed.

Owned file SHA-256 values after validation:

- `host.py`: `8a555fb08a88badf59bdabe2f558bcd9f7918ccebd52d3c2539013bff733c990`.
- `test_c3_b2_private_host.py`:
  `77116dab6279a2e6bb579f14d72a2be59a02725cba2ef1f888b69492ae6954b5`.

## Scope and limitation

Only the assigned host, implementation test, and this implementation record
are changed; no files are staged or committed. The bounded process-list check
was denied by the sandbox, so final no-process confirmation requires root's
already-authorized process inspection. The focused tests themselves reap their
owned children before return. No approval was otherwise needed.

`candidate-not-accepted`
