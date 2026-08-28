# C3-B1 pre-execution runner fixture rebinding — verification round 2

- Verifier: `c3-b1-pre-execution-runner-rebinding-verifier-2`.
- Finding: `C3B2-IF002` downstream runner rebinding.
- Candidate commit: `55d22640334ef05176568f275c3e4e7ec63c3336`.
- Candidate tree: `b96790c572f2fceda4445f55d8373b9a21e2cd9d`.
- Implementor: `c3-b1-pre-execution-runner-implementor-replacement-4`.
- Verdict: `pass`.

I independently verified this exact immutable candidate against governing
contract commit `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` / tree
`d9fb09345ab85580cd8c877745262d1b481e366f`. The candidate changes exactly five
paths: the method, runner, canonical binding, implementation runner test, and
implementor record. Its accepted corrected fixture is commit/tree
`3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
`14c010153ea5542617e601e4126047c561a48483`, after verification
`3a29e4684af6a4c8e53aa4f83f9692ddebab5670`, accumulation
`efcc7759f4af89eb438b2b8611e250d0962fc8c6`, and acceptance
`972322116b737d2fcad37e46d23116b031841359`, in that order.

## Independent evidence

The canonical binding and runner constants close over:

- semantic fixture SHA-256
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`;
- fixture manifest SHA-256
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`;
- unchanged 17-cap SHA-256
  `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`;
- method SHA-256
  `f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341`;
- runner SHA-256
  `0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80`;
- canonical binding SHA-256
  `4b7230cca6a41002da52853dae41724da1e24d22ef94e2b0b644b7e0d237fde7`;
- implementation test SHA-256
  `1511083a3254a44bd95f33f75d9cf5adb022162b20a9e0c274929f4f9325ad19`;
- verifier test SHA-256
  `ee58c01b91155a86e1dd1a33b84f107c89c7bdced293a3d73064005a98d51505`.

The binding contains exactly the closed 24-file source inventory: method,
seven Python tool modules, two tool configurations, six accepted fixture
artifacts, and nine snapshot source bytes. Recomputed hashes equal every entry.
The launch document retains isolated Python 3.12 `-I -B`, its minimal
environment, closed import/source allowlists, disabled characterization probe
mode, and fixed write-only protocol descriptor.

The diff from prior accepted runner `ca0ee7514c157c145bb3970fd2b884fbc8d9ea8a`
/ tree `457240c481afcdf20ef41a74208749e112efa9b6` is confined to four fixture
identities, their method/binding source hashes, and explicit stale-identity
tests. The 17 caps, accounting, worker, probes, launch configuration, snapshot
host, framing, process lifecycle, and result validation are byte-unchanged.

The new verifier supplies 17 non-vacuous tests. Mutations replace every bound
identity with zero values and each superseded commit/tree/semantic/manifest
identity, and mutate the source map with missing, extra, traversal, and digest
substitutions. Every mutation is rejected before `os.pipe` or
`subprocess.Popen`. It also recomputes all source and fixture hashes, confirms
the accepted gate order, and proves exact accept/value-plus-one rejection for
all 17 caps.

The complete 177-test implementation runner suite independently covers
symlink, traversal, substitution and digest attacks; closed file and import
inventory; hostile framing, stdout/stderr/diagnostic/result limits; depth,
items, bytes, text, record and address-space limits; recursion; deadline;
terminate, kill, descriptor close and exact reap; failure recovery; worker and
probe behavior; and the disabled characterization entrypoint. Only inert and
hostile internal probes ran. No decoder route, snapshot characterization, raw
collection, B2/product path, external runtime, hardware, or network operation
executed.

## Commands and results

- Round-2 verifier plus complete implementation suite: `194 passed` (`17` new
  verifier tests plus `177` implementation runner tests).
- Canonical binding `python -m tools.cycle3_characterize.binding --check`:
  passed.
- Deterministic fixture generator `scripts/generate_cycle3_fixtures.py
  --check`: passed.
- Scoped Ruff over the complete runner tool, implementation runner test, and
  new verifier: passed.
- Strict mypy over all seven runner modules: passed, seven source files.
- Candidate commit/tree, fixture tree, five-path diff, prior-runner diff,
  source/digest closure, worktree scope, and `git diff --check`: passed.

Findings: none. This verdict is limited to the exact immutable runner
fixture-rebinding candidate. It makes no acceptance, accumulated-validation,
raw-baseline, threshold, final-B1, manifest, B2, product, or future-work claim.
