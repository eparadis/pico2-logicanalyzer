# C3-B1 pre-execution runner fixture rebinding — implementation round 2

- Implementor: `c3-b1-pre-execution-runner-implementor-replacement-4`.
- Finding: `C3B2-IF002` downstream runner rebinding.
- State: **implementation ready; candidate not accepted**.
- Verdict: **pass** for this bounded implementation handoff only. No prior
  runner verification, accumulation, acceptance, raw, threshold, final-B1, or
  manifest verdict transfers.

The governing contract remains commit
`ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. This smallest exact rebind retains
the behavior of the prior accepted runner candidate
`ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a` and binds the newly accepted
fixture candidate `3af6b9f80dd52611e14acca407707d1da7b8d9ac` / tree
`14c010153ea5542617e601e4126047c561a48483`.

The fixture candidate passed fresh verification, accumulation, and acceptance
at commits `3a29e4684af6a4c8e53aa4f83f9692ddebab5670`,
`efcc7759f4af89eb438b2b8611e250d0962fc8c6`, and
`972322116b737d2fcad37e46d23116b031841359`. The exact bound identities are:

- semantic fixture SHA-256
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`;
- fixture manifest SHA-256
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`;
- unchanged 17-cap input SHA-256
  `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.

Changed paths are limited to:

- `docs/cycle-3-characterization-method.md`;
- `tools/cycle3_characterize/runner.py`;
- `tools/cycle3_characterize/candidate-binding.json`;
- `tests/implementation/test_cycle3_preexecution_runner.py`;
- this implementation record.

The method changes only the fixture identity/digest and fresh gate lineage. The
runner changes only its four fixture constants. The canonical binding refreshes
those identities and source hashes for the corrected semantic fixture, fixture
manifest, method, and runner self-byte. The implementation test adds exact new
identity assertions and proves that each superseded candidate/tree/semantic/
manifest identity is rejected before pipe creation or process launch. All 17
experiment caps, snapshot bytes and digests, closed source set, launch protocol,
containment, fail-closed ordering, worker, probes, accounting, cleanup, and
disabled characterization entrypoint remain unchanged.

Final implementation artifact SHA-256 values before this record are:

| Path | SHA-256 |
| --- | --- |
| `docs/cycle-3-characterization-method.md` | `f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341` |
| `tools/cycle3_characterize/runner.py` | `0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80` |
| `tools/cycle3_characterize/candidate-binding.json` | `4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7` |
| `tests/implementation/test_cycle3_preexecution_runner.py` | `1511083a3254a44bd95f33f75d9cf5adb022162b20a9e0c274929f4f9325ad19` |

Checks used repository-local Python 3.12 with `PYTHONDONTWRITEBYTECODE=1`:

- complete implementation runner suite, including hostile, cleanup, and
  recovery probes: **177 passed**;
- Ruff over the runner tool and implementation test: **passed**;
- strict mypy over all seven runner modules: **passed, 7 files**;
- canonical binding `--check`: **passed**;
- deterministic fixture generator `--check`: **passed**;
- `git diff --check`: **passed**;
- owned scope/diff audit: **passed**, with four prior owned paths modified and
  only this fifth owned path added.

Only inert internal probes executed. No decoder, raw characterization, baseline,
threshold, product/B2 path, external runtime, hardware, or network operation
ran. The three preserved untracked B2-owned paths were neither inspected nor
executed. No approval capability was required. Fresh independent runner
verification, root accumulation, and fresh acceptance remain mandatory.
