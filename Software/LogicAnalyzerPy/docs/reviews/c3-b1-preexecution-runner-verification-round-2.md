# C3-B1 pre-execution runner verification — round 2

## Identity and immutable subject

- Verifier: `c3-b1-pre-execution-runner-verifier-1`
  (`/root/c3_b1_runner_verify`), independent verifier lane reused only in its
  original role.
- Corrected candidate commit/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`.
- Assignment commit: `6f6dbe81e6555da4721ad81ccfeb375e35db681a`.
- Accepted semantic-fixture commit/tree: `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Round-1 pass transfer: none. I repaired no candidate byte and modified only
  my assigned verification test plus this new immutable review record.

## Fresh complete verification

The independently maintained verifier matrix was rebound to the corrected
candidate. It again checks all 17 immutable caps at accepted and rejected
profile boundaries; exact accepted fixture/cap identity; closed source binding
and digests; import/root/file/traversal/symlink/shadow/environment/CWD
boundaries; request/result framing; nonfinite, depth, item, record,
encoded/decoded, text, binary, diagnostic, stdout/stderr, retained-result,
sample/request, recursion, address-space, deadline, and kill-grace accounting;
and whole-result discard.

Actual inert/hostile children again exercised valid results, partial/extra/
malformed frames, nonfinite JSON, invalid base64, depth/item/accounting limits,
stream/diagnostic floods, recursion failure, graceful termination, forced kill,
and recovery after each failure. Every checked success/failure child was the
exact child reaped; all subprocess streams and both raw protocol descriptors
were closed; and a fresh valid child succeeded after each failure. An inert
child reported the exact Python 3.12 recursion and RLIMIT_AS soft/hard values.

Static and inert object inspection repeated the fixed nine-source provenance
and UART/SPI/I2C module graph, closed accepted/rejected options, API-v3
`HasChannel`, `Wait`, `Register`, and half-open `Put` semantics, method truth,
and absence of broad suppression. Public `characterize` remains fixed disabled.
The private post-gate route and worker `execute_snapshot` call remain
structurally present and were inspected only as AST/source.

## RI013 independent proof and history

An independent subprocess proved that Python 3.12 `-I` ignores the environment-
only `PYTHONDONTWRITEBYTECODE=1`: `sys.dont_write_bytecode` reported `False`.
The corrected frozen launch JSON and actual `_popen_spec` both require exactly
`-I -B worker.py`. Two consecutive real inert `bytecode` workers imported and
exact-path-verified only the bound sibling `probes.py`; both reported
`{"dont_write_bytecode": true, "probes": true}`. After each launch the exact
tool inventory was unchanged, no `__pycache__` existed, and binding/inventory
verification passed. A real valid probe then succeeded with the inventory
still unchanged.

The immutable progress history was audited in order. The round-1 candidate was
verified, accumulated, and accepted before characterization. Exactly three
authorized UART `uart-rx-valid-default` warm-ups then ran; each attempt's five
recorded repetitions and later requests failed before launch after bytecode
inventory drift. No SPI/I2C snapshot and no recorded baseline repetition ran.
RI013 invalidated the old runner passes, the provisional output/cache artifacts
were quarantined, and corrected candidate `48d139f...` plus assignment
`6f6dbe8...` followed. This verification performed no fourth snapshot
execution.

## Exact identities

The complete 11-path runner/method/test candidate surface is byte-identical to
`48d139f...`. Independently recomputed corrected SHA-256 values are:

- binding `1d36da4a8e06707c5fad8830c7037fd5aa601fdc8854dc4f33b9aec4b2d992eb`;
- launch `3df74d88a1f013a7aa9f09c81d76a653159de09e9b42270137fb0f3956efbf27`;
- probes `dc0d5ba2e5c1ec1f3e805f9a41a92b29e5edce8a4bb6172ef6fc82dbf8848b2a`;
- runner `2f0d32ec2d2fea047cb5f78e6b3d32753e6d69d3f9d0f398bd589691011ef942`;
- worker `76124299334fc4fb5a7ea5d28750afff9b19f59b4fda0618dd0be215f59f890c`;
- method `8ef7bdac50554fb42ec97d3c5d685d3f6b55074c82478c750e4e62ff3d318325`;
- implementation test `74e5c8d823f1f58ffc84e57bbae7264ee80c67586dec1e3e816e8ccce8f341c1`;
- verifier test `c6cec19e2e97a833315270d2ae9dbf1cd9b19433122cf545b1f5d2512204bf5b`.

## Commands and results

All commands used RTK command shapes.

- Fresh verifier suite: 23 passed in 3.14 seconds.
- Combined corrected implementation and independent verifier suites: 190
  passed in 18.02 seconds.
- Ruff over verifier, runner tools, and focused implementation test: passed.
- Strict mypy over the six substantive tool modules: passed with no issues.
- Binding check: passed without output.
- Exact candidate-path quiet diff against `48d139f...`: passed.
- `git diff --check`: passed.
- Final RTK process listing was searched for the worker command: no match; no
  worker remains.

## Safety, findings, and verdict

No private snapshot route, `execute_snapshot`, decoder, approved snapshot,
compatibility helper, expected-fixture generator, product runtime, hardware,
network, installation, or excluded action ran. No fourth snapshot execution
occurred. Only static source/AST/bytes/JSON inspection and inert/hostile
non-decoder probes were used. No finding is open.

`pass`
