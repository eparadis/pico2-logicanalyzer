# C3-B1 pre-execution runner fixture rebinding — verification round 1

Verdict: `pass`.

## Identity and scope

The independent verifier identity is
`c3-b1-pre-execution-runner-rebinding-verifier-1`. I verified immutable
candidate commit `ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a`, tree
`457240c481afcdf20ef41a74208749e112efa9b6`, against governing contract commit
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0`, tree
`d9fb09345ab85580cd8c877745262d1b481e366f`.

The candidate changes exactly five committed paths relative to its parent:

- `docs/cycle-3-characterization-method.md`
- `docs/reviews/c3-b1-preexecution-runner-fixture-rebinding-implementation-round-1.md`
- `tests/implementation/test_cycle3_preexecution_runner.py`
- `tools/cycle3_characterize/candidate-binding.json`
- `tools/cycle3_characterize/runner.py`

Verification was static or used only the existing inert/hostile runner probes.
No decoder, snapshot host with decoder input, fixture generator, raw baseline,
or B2 product code was run. I did not inspect or modify the untracked B2 paths
`src/pico_logic_analyzer/_decode/` and
`tests/implementation/test_c3_b2_private_host.py`. The verifier added only
`tests/verification/test_c3_b1_runner_fixture_rebinding.py` and this record.

## Findings

The candidate and tree identities resolve exactly. The corrected fixture
candidate resolves to commit `a98d328aab92f3dad66988fb70cc567946dc89d0`, tree
`450aadcf26bd6c74860872bfbf0a0a1b32d94f3b`; the current cap, semantic-fixture,
and fixture-manifest bytes are unchanged from that candidate.

Binding v3 is closed and recomputes exactly. Its accepted-fixture object names
the corrected candidate and tree plus these exact SHA-256 identities:

- experiment caps: `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`
- semantic fixtures: `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`
- fixture manifest: `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`
- candidate binding: `144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`

The source map is an exact equality check, not a subset check, and continues to
cover the method, all runner/configuration sources, all six accepted fixture
artifacts, and nine pinned snapshot source files. The candidate changes no
snapshot digest, worker, probe, accounting, launch, allowlist, protocol, public
route, cleanup path, or process model.

The immutable profile has exactly 17 positive integer cap IDs. Every cap accepts
its exact production value and a test-only request for value plus one is
rejected. The corrected corpus-derived values include `request_bytes =
46456256`, `retained_result_bytes = 185825024`, and
`worker_address_space_bytes = 68719476736`; all values are bound through the
accepted cap-file digest.

The verifier-owned test independently mutates each of candidate commit,
candidate tree, cap digest, fixture-manifest digest, and semantic-fixture
digest. Every stale identity raises the stable accepted-fixture binding failure
while monkeypatched `os.pipe` and `subprocess.Popen` counters both remain zero.
The ordinary binding check only recomputes JSON and source digests; it has no
worker-launch call. Existing focused tests retain the inert runner's import and
inventory boundaries, fixed isolated child specification, bounded streams and
results, hostile framing/accounting cases, termination/kill, exact descriptor
close/reap evidence, recovery probes, and disabled public characterization.

## Commands and results

All commands were prefixed with `rtk`; Python commands used the repository-local
Python 3.12 environment and the test command set
`PYTHONDONTWRITEBYTECODE=1`.

- `git show -s --format='%H %T %P %s' ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` — exact candidate/tree resolved.
- `git diff-tree --no-commit-id --name-only -r ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` — exactly the five declared paths.
- `git diff ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a^ ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a -- <five paths>` — inspected; correction-only changes.
- `git show -s --format='%H %T' a98d328aab92f3dad66988fb70cc567946dc89d0` — exact accepted fixture commit/tree resolved.
- `git diff --exit-code a98d328aab92f3dad66988fb70cc567946dc89d0 -- <three accepted fixture paths>` — exit 0.
- `sha256sum <candidate, binding, fixture, and verifier artifacts>` — exact hashes recorded below.
- `.venv/bin/python -m pytest tests/implementation/test_cycle3_preexecution_runner.py tests/verification/test_c3_b1_runner_fixture_rebinding.py -q` — 180 passed (172 existing focused tests plus 8 independent rebinding tests).
- `.venv/bin/ruff check tools/cycle3_characterize tests/verification/test_c3_b1_runner_fixture_rebinding.py` — passed.
- `.venv/bin/mypy --strict tools/cycle3_characterize/__init__.py tools/cycle3_characterize/accounting.py tools/cycle3_characterize/binding.py tools/cycle3_characterize/probes.py tools/cycle3_characterize/runner.py tools/cycle3_characterize/snapshot_host.py tools/cycle3_characterize/worker.py` — success for seven files.
- `.venv/bin/python -m tools.cycle3_characterize.binding --check` — exit 0.
- `git diff --check` — exit 0.

## Artifact hashes

- method: `d2ab24c1bd0b429b2ff268e948fb6129ba926075a6fae0c30faa50d0159f94ec`
- implementation record: `2f1afc78ee9eaf8c31a5a95afd95f5d43a67505e74437fd278c99eb4dc788abb`
- implementation test: `8bb173d15be7e6e510501f6958a1641fc068ba90b6290818edd2a3688383e6e9`
- candidate binding: `144c08036cb3eca490586d8af33b223fc9abfe905182cec102248ccce2108f98`
- runner: `81a2e3dbba8b5fe17043d24f8818e4b539a28e5738d79847e11539954dd36acc`
- verifier test: `14793a958bdfa4bc92cb8a46115b413d70f8d0cd9e7fb28fb65ef0f8197f0562`

The candidate therefore passes its independent fixture-rebinding verification.
This verdict does not transfer any prior accumulated-validation, acceptance,
raw-baseline, threshold, final-B1, manifest, or checkpoint pass. Those gates
must run anew in their required order against this exact candidate.
