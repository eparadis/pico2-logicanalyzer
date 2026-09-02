# C3-B4 hosted Python artifact implementation, round 11

- Identity and role: `c3-b4-public-implementor-1`; bounded hosted-runtime
  correction implementor
- Immutable failed verifier commit/tree:
  `daf7425a0dea4ca23cb449650f489bcf5a41d3ae` /
  `a51b2225489e9f400e164744c69cd0e153f4fff0`
- Governing B1 contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Timestamp: `2026-09-02T06:26:01Z`

## Failed hosted evidence disposition

The preserved exact-candidate GitHub Actions run `33582589204`, job
`100099817404`, failed at step 5, the managed CPython installation and identity
guard. Its annotation records exit code 1 at the workflow's bootstrap step.
The pinned uv 0.12.6 resolver selected the later
`cpython-3.12.13+20260807` build: full `sys.version` was
`3.12.13 (main, Aug  7 2026, 02:15:27) [Clang 22.1.3 ]` and `BUILD` was
`20260807`. Architecture and managed-key suffix remained correct.

The accepted raw B1 evidence binds the June 23 build, including exact full
`sys.version` and `BUILD=20260623`. Therefore the later build is not accepted,
and neither the B1 evidence nor its verifier may be weakened. The correction
below pins and verifies the immutable accepted artifact rather than relying on
uv's moving Python-download metadata.

## Implementation and validation

The moving uv download resolution and now-unused setup-uv action are removed.
The workflow downloads the exact immutable official artifact:

- release tag: `20260623`;
- artifact:
  `cpython-3.12.13+20260623-x86_64-apple-darwin-install_only_stripped.tar.gz`;
- size recorded by the immutable release API: `24690991` bytes; and
- SHA-256:
  `a6bbea996c5f14eb55ab275889d2df45408deec504b4a7219d7b59c045b2555e`.

The workflow uses curl with HTTPS-only protocol and TLS 1.2 minimum, then
checks the pinned SHA-256 with `shasum --check --strict` before extracting.
The known `python/` archive root is removed with `--strip-components 1` into
the governed `cpython-3.12.13-macos-x86_64-none` suffix. The executable then
checks the exact accepted full `sys.version`, x86_64 architecture, and base
suffix before Node setup or dependency installation. The artifact contains no
`BUILD` file; no synthetic uv metadata is fabricated.

Both clean virtual environments still originate from that exact interpreter
and recheck the version and architecture before their respective hash-locked
installs. Full-history checkout, Node 22.14.0, the focused three-case inherited-
SIGTERM gate, bounded diagnostic/redaction behavior, all product gates, and
their order remain present.

The implementation-owned regression first failed `1 failed, 1 passed in
0.08s` because the artifact URL, digest, and extraction guard were absent. It
then passed `2 passed in 0.06s` after the correction.

The exact downloaded artifact was independently hashed locally and passed the
workflow's strict checksum. Extraction with the workflow's exact stripping and
governed destination semantics produced the accepted full `sys.version`,
x86_64 architecture, and suffix. A redundant new curl attempt from this
sandbox failed closed at DNS resolution with exit 6; no alternate bytes were
used and no escalation was requested. Root's independently downloaded ignored
archive supplied the exact bytes for the local extraction proof.

The initial round-10 verifier sweep was `4 failed, 5 passed`. The four failures
were exactly the superseded workflow identities for the prior digest, setup-uv
action, uv cache/install paths, and moving uv-install plus `BUILD` contract.
Appending those four nodes made the exact prior 26-selector partition node
stale. Root authorized those five ordered selectors. A retained round-10 node
then exposed its own literal `deselects[-6:]` identity; root separately
authorized that one exact selector and no other disposition.

The final partition has 15 ordered ignores and 32 unique ordered selector
strings representing 33 cases. All three remaining round-10 behavior/scope
nodes passed, the accepted raw B1 replacement verifier passed, and no module is
ignored. The final broad result was `1487 collected / 33 deselected / 1454
selected`; `1448 passed, 6 skipped, 33 deselected, 106 warnings in 235.52s`.
The skips were the existing loopback and optional machine-local physical-
artifact checks.

Additional final checks:

- implementation regression plus retained round-10 nodes: `5 passed, 6
  deselected in 5.65s`;
- focused artifact checksum/extraction/runtime identity: pass;
- Ruff on the implementation regression: pass; and
- `git diff --check`: pass.

Changed paths and pre-commit hashes:

- `.github/workflows/logic-analyzer-python-cycle2.yml` —
  `153c9b3987200eef271f4f26c0253622e0f087a12c1d89216971d67062041318`;
- `Software/LogicAnalyzerPy/tests/implementation/test_cycle2_workflow.py` —
  `e19af993b3b0ab179381fb0b8d4602c1097887cb716fc238828f326684adff00`;
- `Software/LogicAnalyzerPy/docs/reviews/c3-b4-implementation-round-11.md` —
  this implementation record.

No product, decoder, B1/B2/B3 fixture, threshold, limit, dependency lock,
manifest, contract, or prior evidence byte changed. All scratch remained under
ignored repository `.tmp/c3-b4-ci/`. No hosted dispatch or external mutation
was performed by this implementation identity.

## Verdict and boundary

The exact accepted build is now selected by immutable artifact identity and
verified before execution, without uv's moving download metadata. Fresh
independent verification and root-owned hosted dispatch remain required;
therefore the verdict is `candidate-not-accepted`.

The B1 rights-holder/counsel limitation remains controlling. Shim ownership,
historical MIT labeling, and combined-work treatment require counsel or
rights-holder confirmation before conveyance. No wheel, sdist, upload,
conveyance, or publication was performed or authorized.
