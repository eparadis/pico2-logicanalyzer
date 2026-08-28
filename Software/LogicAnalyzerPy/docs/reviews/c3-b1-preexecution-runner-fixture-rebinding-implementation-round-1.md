# C3-B1 pre-execution runner fixture rebinding — implementation round 1

Verdict: implementation ready.

This implementation-only correction rebinding updates the prior runner candidate
`48d139f...` to the accepted fixture correction candidate
`a98d328aab92f3dad66988fb70cc567946dc89d0` / tree
`450aadcf26bd6c74860872bfbf0a0a1b32d94f3b`. The governing contract remains
commit `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree
`d9fb09345ab85580cd8c877745262d1b481e366f`.

The corrected immutable identities are semantic fixture SHA-256
`1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`,
experiment caps SHA-256
`6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`,
and fixture manifest SHA-256
`ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`.
The fixture correction was independently verified, accumulated, and accepted by
`b708293...`, `1054cf3...`, and `d30012d...` respectively. No decoder ran in
this implementation round.

Changed paths are the runner identity/binding source, regenerated binding,
focused inert test, method, and this review:

- `tools/cycle3_characterize/runner.py`
- `tools/cycle3_characterize/candidate-binding.json`
- `tests/implementation/test_cycle3_preexecution_runner.py`
- `docs/cycle-3-characterization-method.md`
- `docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-implementation-round-1.md`

The runner now binds the corrected candidate/tree, cap, manifest, and semantic
fixture digest before any child setup. The binding payload carries each identity
and continues to bind the exact 17-cap input, source inventory, launch document,
nine snapshot bytes, ordered source-set digests, `-I -B` child launch, separate
protocol/stdout/stderr, and existing resource/cleanup controls. No snapshot
digest, process design, source allowlist, or public-characterization behavior
changed.

The regenerated `candidate-binding.json` SHA-256 is
`144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`.
Its bound method, runner, launch, and worker source SHA-256 values are,
respectively,
`d2ab24c1bd0b429b2ff268e948fb6129ba926075a6fae0c30faa50d0159f94ec`,
`81a2e3dbba8b5fe17043d24f8818e4b539a28e5738d79847e11539954dd36acc`,
`3df74d88a1f013a7aa9f09c81d76a653159de09e9b42270137fb0f3956efbf27`,
and `76124299334fc4fb5a7ea5d28750afff9b19f59b4fda0618dd0be215f59f890c`.

Focused checks, with repository-local Python 3.12 and
`PYTHONDONTWRITEBYTECODE=1`, completed successfully:

- `pytest tests/implementation/test_cycle3_preexecution_runner.py -q` — 172 passed.
- `ruff check tools/cycle3_characterize` — passed.
- `mypy --strict` over the seven runner modules — passed.
- `python -m tools.cycle3_characterize.binding --check` — passed.
- `git diff --check` — passed.

The focused test includes each of the 17 exact cap accept/reject boundaries;
old candidate, cap, manifest, and semantic binding identities fail before pipe
or process creation; and the existing two-consecutive inert-worker,
cache/inventory, hostile, cleanup, and recovery probes remain covered. The test
route imports no decoder/helper/product runtime and does not invoke the private
snapshot entrypoint.
