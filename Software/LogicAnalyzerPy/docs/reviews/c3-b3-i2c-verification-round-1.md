# C3-B3 I2C verification round 1

## Scope and identity

Fresh independent I2C-only verification was performed against frozen candidate
commit `844d69d22d2f82ae78f423762861abf3b18def66`, tree
`513c4c4bc2a8d053bfc7e6229390207bc265b60e`. The commit adds only the I2C
implementation test and its implementation review. The candidate test SHA-256
is `20c04a6f1eeb77760fe16b522ccaf1b1def8b8ca5a3418b29b3af6471bd433c3`.

The verifier derives its oracle independently from the accepted semantic
corpus, option matrix, and provenance. It does not import or copy the candidate
test's helpers or derive expected values/defaults from production decoder code.
It is confined to I2C and makes no B3 accumulation, acceptance, checkpoint, or
R13/R14/R16 claim.

## Coverage and hostile audit

The verifier covers all 3 accepted timelines with full typed result and
canonical JSON equality, all 2 direct matrix rows resolving to fixtures, all 6
unsupported rows rejecting before worker spawn, and the sole matrix-derived
default (`address_format=shifted`). Equality covers exact declarations,
emission indices/order, sample/time coordinates, Python tagged values,
annotation, binary, and metadata records. Explicit closure checks cover the
applicable START/repeated-START/STOP, ACK/NACK, BITS/warning, address-write and
data-write records; both read/write declaration surfaces; shifted/unshifted
address formatting; and the incomplete boundary. A noncontiguous and reordered
SCL/SDA capture vector checks decoder pin order, and every timeline is decoded
twice for determinism.

Hostile mutations independently prove sensitivity to declarations,
coordinates, record order, tagged values, binary payloads, metadata values,
address format/default, physical mapping, matrix fixture rebinding, and
provenance file-set identity. Exact accepted hashes are checked for the semantic
corpus, option matrix, B1 manifest reference, B2 manifest, I2C file-set, and all
five I2C/helper sources. The candidate's AST import roots are closed to the
expected standard, pytest, and private-host packages.

## Findings and correction history

The first focused verifier run produced 25 passes and one verifier failure. The
new check incorrectly required read-side records to be emitted, but the accepted
corpus emits write-side records and declares both read and write surfaces. The
verifier was corrected to preserve that distinction. This was a verifier-only
correction; no candidate or product defect was found.

## Commands and results

All commands were run through `rtk` from `Software/LogicAnalyzerPy` unless noted.

```text
rtk .venv/bin/python -m pytest tests/verification/test_c3_b3_i2c_conformance.py -q
26 passed

rtk .venv/bin/python -m pytest tests/implementation/test_c3_b3_i2c_conformance.py -q
9 passed

rtk .venv/bin/python -m pytest tests/implementation/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host.py tests/verification/test_c3_b2_private_host_round2.py tests/verification/test_c3_b2_private_host_round3.py tests/verification/test_c3_b2_private_host_round4.py -q
313 passed in 39.60s

rtk .venv/bin/python -m ruff check tests/verification/test_c3_b3_i2c_conformance.py tests/implementation/test_c3_b3_i2c_conformance.py
All checks passed

rtk git diff --check
clean
```

## Verdict

**PASS.** The exact frozen C3-B3 I2C candidate conforms to the accepted B1
semantic/matrix/provenance oracle, passes inherited B2 private-host gates, and
has no I2C finding in this verification round.
