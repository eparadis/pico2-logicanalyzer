# C3-B3 I2C implementation round 1

## Scope

Added the I2C-only independent conformance oracle at
`tests/implementation/test_c3_b3_i2c_conformance.py`.  It assembles expected
results only from the accepted C3-B1 semantic corpus, option matrix, and
provenance fixture; it does not import decoder source to derive expected
behavior.  No product code, fixture, governing contract, checkpoint, or
acceptance record was changed.

## Candidate evidence

- Assigned base HEAD: `db825eff3ab4ca0e30f5ed0197dcad6bc93cda88`.
- Assigned base tree: `483ac497defd9400a36e067ed01925d1cc65b949`.
- Candidate HEAD/tree remained
  `db825eff3ab4ca0e30f5ed0197dcad6bc93cda88` /
  `483ac497defd9400a36e067ed01925d1cc65b949`; the two assigned paths are
  intentionally untracked implementation additions and no unrelated tracked
  path was modified by this assignment.

## Oracle and coverage accounting

- Semantic corpus SHA-256:
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`.
- Option matrix SHA-256:
  `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`.
- B1 fixture-manifest reference:
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`.
- Accepted B2 manifest SHA-256:
  `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`.
- I2C provenance file-set SHA-256:
  `dd85b78a9d016cea24e69509eeb6a40fb8552e31af08e948fb750d9e03b216ae`.

The test covers all three accepted I2C timelines: shifted START/address/ACK,
data/NACK/STOP; unshifted repeated START; and incomplete boundary. Complete
typed, emission-ordered annotation, binary, metadata, and Python records,
declarations, coordinates, canonical JSON bytes, address/data read-write,
START/repeated-START/STOP, ACK/NACK, bit/warning semantics, and repeat-run
determinism are checked by equality to the literal fixture records.

All eight matrix rows are covered: two direct-fixture rows and six unsupported
rows. Unsupported options reject while worker spawn is monkeypatched to fail;
the one default (`address_format=shifted`) is read exclusively from the matrix.
The mapping test checks both required pins under a noncontiguous, reordered
physical channel vector and deliberately makes no unsupported optional-pin
sentinel claim.

The closed provenance check covers the exact source hashes for
`sigrokdecode.py`, I2C initializer and `pd.py`, and both `common.srdhelper`
files, plus their parsed direct import roots.

## Findings

The first focused execution exposed and corrected an oracle expectation in the
noncontiguous/reordered mapping probe: the capture vector `(7, 19)` means the
first packed value drives SDA before SCL. No product defect was found.

Focused commands and results:

```text
rtk .venv/bin/python -m pytest tests/implementation/test_c3_b3_i2c_conformance.py -q
9 passed in 1.13s

rtk .venv/bin/python -m ruff check tests/implementation/test_c3_b3_i2c_conformance.py
All checks passed!

rtk git rev-parse HEAD
db825eff3ab4ca0e30f5ed0197dcad6bc93cda88

rtk git rev-parse HEAD^{tree}
483ac497defd9400a36e067ed01925d1cc65b949
```

This is an implementation record, not a verification, acceptance, checkpoint,
or accumulated-status claim.
