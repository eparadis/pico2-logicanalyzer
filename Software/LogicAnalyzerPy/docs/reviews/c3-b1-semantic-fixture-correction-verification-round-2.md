# C3-B1 semantic-fixture correction verification — round 2

## Identity and immutable subject

- Verification identity: `c3-b1-semantic-fixture-correction-verifier-2`
  (`/root/c3_b1_i2c_fixture_verify_r1`), distinct from implementor
  `c3-b1-semantic-fixture-implementor-replacement-8`.
- Finding: `C3B2-IF002`, inconsistent unshifted-I2C binary oracle.
- Finding-record commit: `8c2b5dcfa7b607cb5c07ab95580c9d72f5433f96`.
- Candidate commit/tree: `3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
  `14c010153ea5542617e601e4126047c561a48483`.
- Governing contract commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Candidate state: `candidate-not-accepted`. This verdict is fixture-candidate
  verification only; no earlier verdict transfers and no later acceptance,
  runner, raw, threshold, final-B1, manifest, checkpoint, B2, or completion
  verdict is claimed.

The commit has exactly five changed paths: the round-2 implementation record,
generator, semantic corpus, fixture manifest, and focused implementation test.
Its implementation record names the assigned implementor identity and retains
candidate-not-accepted status. Commit authorship is Ed Paradis
`<eparadis@users.noreply.github.com>`; the durable role identity is the distinct
implementor named above.

## Independent static semantic result

Frozen `Software/decoders/i2c/pd.py` assigns the received byte to `d`, changes
`d` only when `address_format == "shifted"`, and then passes that same `d` to
the Python record, binary `bytes([d])`, and annotation formatting. Therefore
the selected unshifted address emits integer `160`, byte `0xA0` (base64
`oA==`), and annotation `A0`; the shifted witness remains integer `80`, byte
`0x50` (base64 `UA==`), and annotation `50`.

An independent comparison of all 63 timeline IDs against the finding-record
commit found exactly one unequal timeline and exactly one unequal record:
`i2c-unshifted-repeated-start.expected_records[4]`. Replacing only its candidate
`data_base64` value `oA==` with the old `UA==` makes the complete old record
identical. Thus coordinates, rational times, emission index, kind, output ID,
binary class, waits, pins, transitions, declarations, mapping, options, sample
metadata, every other record, and every other timeline remain unchanged.

The generator's `i2c_byte` helper is generic: it accepts explicit
`address_format`, computes one `emitted` value, and uses it for integer,
base64-encoded binary, and annotation representations. It contains no fixture
ID branch. Its imports remain the standard-library-only static set and it has
no decoder, B2, raw-characterization, subprocess, external-runtime, or dynamic
oracle dependency. The focused implementation assertion is non-vacuous: it
extracts Python, binary, and annotation address outputs for both shifted and
unshifted fixtures and independently requires equality to `0x50` and `0xA0`.

All complete prior semantic-fixture properties remain present: 63 declarative
timelines, their complete waits/transitions/declarations/options/records, the
closed option matrix and typed vectors, provenance, five edge-semantic
decisions, optional-pin witnesses, finite experiment caps, canonical generated
artifacts, and deterministic generator check. The correction does not modify
decoder bytes or any B2, runner, raw, threshold, final, manifest-evidence,
product, lock, workflow, contract, metadata, B3+, or Cycle 4 path.

## Digest closure

| Artifact | SHA-256 |
| --- | --- |
| generator | `a101ae13cba938aa4d574fd1df3e4cc09dc845b2a643088cfee4a79313c3266f` |
| semantic corpus | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| fixture manifest | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| provenance | `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4` |
| option matrix | `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209` |
| typed vectors | `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf` |
| experiment caps | `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d` |
| independent verifier test | `9f750b51294b2078e82373adbbdd81ac287de669603f82bf59e65cc8e001a10a` |

Every manifest artifact digest and generator self-digest recomputed exactly.
Provenance, option matrix, typed vectors, and experiment caps are byte-identical
to the finding-record commit. Deterministic regeneration reported no drift.

## Commands and exact results

All shell commands used RTK and repository-local Python. No decoder, B2 test or
code, raw characterization, C#/.NET/pythonnet/libsigrokdecode/sigrok-cli,
external/reference runtime, hardware, network, or dependency operation ran.

- `Software/LogicAnalyzerPy/.venv/bin/python -m pytest Software/LogicAnalyzerPy/tests/verification/test_c3_b1_semantic_fixture_correction_round2.py -q`
  — exit 0; `6 passed in 0.29s`.
- `Software/LogicAnalyzerPy/.venv/bin/python -m pytest Software/LogicAnalyzerPy/tests/implementation/test_cycle3_fixtures.py -q`
  — exit 0; `12 passed in 0.48s`.
- `Software/LogicAnalyzerPy/.venv/bin/ruff check Software/LogicAnalyzerPy/scripts/generate_cycle3_fixtures.py Software/LogicAnalyzerPy/tests/implementation/test_cycle3_fixtures.py Software/LogicAnalyzerPy/tests/verification/test_c3_b1_semantic_fixture_correction_round2.py`
  — exit 0; `All checks passed!`.
- `Software/LogicAnalyzerPy/.venv/bin/python Software/LogicAnalyzerPy/scripts/generate_cycle3_fixtures.py --check`
  — exit 0; deterministic generated bytes match.
- `git diff --check` and candidate-range `git diff --check` — exit 0.
- Candidate range scope audit — exactly five expected tracked paths; no other
  candidate delta.

The worktree additionally contains the three preserved untracked B2-owned
paths and this verifier's two owned paths. The B2 paths were not read, run, or
modified and are not evidence. Candidate bytes were not repaired.

## Findings and disposition

1. `C3B2-IF002`: closed for this exact fixture candidate. The unshifted I2C
   Python, binary, and annotation oracle is internally consistent at `0xA0`,
   while shifted behavior remains `0x50`.
2. Open candidate findings: none.
3. Required ordering remains active: root-owned accumulated fixture validation
   and fresh acceptance must precede every invalidated downstream gate. This
   verification does not transfer any prior verdict or authorize B2 resumption.
4. Approval needed: none.

## Verdict

pass
