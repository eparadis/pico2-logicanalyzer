# C3-B1 semantic-fixture correction — implementation round 2

- Identity: `c3-b1-semantic-fixture-implementor-replacement-8`
  (`/root/c3_b1_i2c_fixture_impl_r1`), fixture-only implementation role.
- Finding: `C3B2-IF002`, inconsistent unshifted-I2C binary oracle.
- Starting commit/tree: `8c2b5dcfa7b607cb5c07ab95580c9d72f5433f96` /
  `c2ec019fc1089f4d174b9afcd4e892fbd53199fa` on `python-rewrite`.
- State: **implementation ready; candidate not accepted**. These changes are
  deliberately uncommitted and authorize only root integration followed by a
  new immutable semantic-fixture candidate and the complete fresh contract
  gate sequence. This record is not verification, acceptance, accumulated
  validation, a manifest, or a checkpoint.

## Independent disposition

The authoritative checked-in I2C source was consumed only as frozen inert
source semantics supplied in the assignment: the collected address byte is
shifted only for `address_format == "shifted"`, after which the same value is
sent to Python and binary outputs and formatted for the address annotation.
Therefore wire byte `0xA0` emits `0x50` under `shifted` and `0xA0` under
`unshifted`. Base64 for the latter byte is `oA==`.

I did not inspect, import, execute, or use the uncommitted B2 `_decode` product,
its tests, or its review as an oracle. I did not run any decoder, product host,
characterization runner, raw characterization, C#/.NET, sigrok runtime,
external/reference decoder, hardware, network, or dependency operation. The
correction was independently authored from the frozen source rule and the
declarative generator inputs.

## Correction

`i2c_byte()` now derives one `emitted` value from the raw byte, address role,
and explicit address format. Its Python integer, binary byte, and annotation
hex text all consume that same value. The shifted call keeps the default and
still encodes `0x50` (`UA==`); the repeated-start direct witness passes
`unshifted` and now encodes `0xA0` (`oA==`). The prior after-the-fact Python and
annotation mutations were removed.

The implementation test now audits both option cases and requires equality
among the Python address integer, decoded binary byte, and terminal annotation
hex text. It would fail the prior cross-output inconsistency. Its static import
allowlist includes only the newly used standard-library `base64` module. The
fixture-presence predicate was made a subset check because later, already
checked-in B1 evidence JSON files legitimately coexist with the six generator
artifacts; the previous exact-directory predicate prevented this focused file
from running against the current tree.

## Byte and digest disposition

The semantic corpus has exactly one generated semantic change:
`i2c-unshifted-repeated-start`, address-write binary record at emission index 4,
changes from `UA==` (`0x50`) to `oA==` (`0xA0`). Its Python value remains 160,
its annotation remains `A0`, and all coordinates, waits, transitions, options,
declarations, and other records remain byte-identical. Every other semantic
timeline is byte-identical.

| Path | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `scripts/generate_cycle3_fixtures.py` | `d872fe9f6c1cb3407a8d05d7b9e03e3bb34b10baee8fa47e55b57bb4b64574f6` | `a101ae13cba938aa4d574fd1df3e4cc09dc845b2a643088cfee4a79313c3266f` |
| `testdata/decoders/cycle3/semantic-fixtures.json` | `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329` | `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094` |
| `testdata/decoders/cycle3/manifest.json` | `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f` | `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9` |
| `tests/implementation/test_cycle3_fixtures.py` | `fccc9746dfd50766cb3f6fbae72f08dfd40d57c791792ead2c76cf2eb6d68f45` | `6a909dd89e99ba40e76e3a66b0139ecba27a4b4843c704d24e883d4948ae6c0e` |

The manifest changes only its generator digest and semantic-fixture artifact
digest. Generated artifacts proven unchanged after two deterministic writes:

- `provenance.json`: `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`;
- `option-matrix.json`: `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`;
- `typed-vectors.json`: `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`;
- `experiment-caps.json`: `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.

Thus all other semantic timelines, option rows, typed vectors/goldens,
provenance, and experiment caps remain byte-identical.

## Focused results

- Deterministic write followed by
  `generate_cycle3_fixtures.py --check`: exit 0, repeated after digest capture
  with the same hashes above.
- `python -m pytest tests/implementation/test_cycle3_fixtures.py -q`:
  exit 0, final run `12 passed in 0.47s` (preceding run also passed).
- `ruff check scripts/generate_cycle3_fixtures.py tests/implementation/test_cycle3_fixtures.py`:
  exit 0, `All checks passed!`.
- Scoped diff: only the four corrected generator/generated/test paths plus
  this implementation record are modified; the three preserved untracked B2
  owned paths are untouched and non-evidentiary.
- Approval needed: none.

## Finding disposition

`C3B2-IF002`: **corrected in this uncommitted implementation candidate**.
No acceptance transfers. Root must create the immutable candidate and assign
fresh independent fixture verification and acceptance, then reopen every
dependent runner/raw/threshold/final-B1/manifest/checkpoint gate in governing
order before B2 resumes.
