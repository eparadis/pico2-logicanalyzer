# Cycle 3 B1 semantic fixtures

`testdata/decoders/cycle3/` is a declarative, independently authored fixture
corpus. It is the expected-output authority for later host and CLI work; it is
not generated from a decoder or any reference runtime.

The corpus freezes five API-v3 decisions: empty waits advance from sample zero,
searches include the current sample and use defined skip advancement, all
simultaneous alternatives are marked, intervals are half-open, and end of
input suppresses a partial unit while retaining earlier emitted records. It
also fixes integer `0xFF` absent-pin vectors, option coverage dispositions,
every v1 output/value tag, canonical UTF-8 CLI bytes, and a finite
experiment-only cap schema.

The fixture names are protocol review inputs, not abbreviated smoke tests.
`uart-rx-valid-default` and `uart-tx-valid-default` record the separate
optional-pin vectors and UART's Python/binary/annotation registration order;
the UART parity/invalid-stop case is separate from the distinct BREAK and IDLE
timelines; complete direct option witnesses cover 9-bit, MSB, parity, and
sample-point branches while the legacy 9-bit case remains an incomplete edge
case. SPI names the MISO-only,
MOSI-only, no-CS, mode, CS-polarity, bit-order, word-size one/eight and
incomplete cases.  I2C names START, repeated START, address, ACK/NACK, data,
STOP, shifted/unshifted and incomplete cases.  Each contains the literal input
transition timeline, expected `wait()` calls and returned pin vector, snapshot
declarations, request-wide output order, coordinates, and rational times.

UART uses the exact integral schedule 1,152,000 Hz / 115,200 baud = 10
samples per bit, retaining source `skip`, edge, and idle alternatives plus an
explicit failed finite wait for incomplete traffic. SPI retains initial
`wait({})`, edge/CS alternatives, eight sampling edges for word-eight, and
eight source-order `spi-data` entries in `BITS`. I2C repeated START appears
only where SDA falls while SCL is high after address-bit waits. These are
static source transcriptions, never decoder execution.

The option matrix is closed. Every accepted row names one of those finite direct
fixtures, while unsupported rows name their explicit rejection rule.
It never manufactures a one-edge stimulus merely to claim option coverage.

`typed-vectors.json` is independently literal v1 object data plus canonical
UTF-8 JSON bytes, including every Python value tag and all four record kinds.
Its declaration arrays retain source order.  `experiment-caps.json` is only a
positive finite experiment envelope: deadline/grace, input/request, output
and encoded/decoded/text/binary/stdout/stderr/diagnostic sizes, nesting/items,
retention, recursion, and address space all state accept/reject boundaries and
rationale.  It asserts neither enforcement nor product thresholds.

Caps are deliberately static values with boundary/coverage entries and no
claim of executable enforcement. A later, separately owned runner must enforce
them with non-decoder probes before any snapshot can run.

Each cap names dynamically recomputed static fixture maxima and its exact
integer corpus formula (rather than fixed historical maxima), with related-cap
consistency. macOS
resource observation and cap enforcement remain runner-owned.

Every cap also carries a machine-readable derivation object (operation, named
basis category/value, multiplier, optional floor, and result). This records
the 50ms scheduling-policy wall/grace bounds, input and diagnostic corpus
floors, and stderr's reference to the diagnostic result without interpreting
prose.

Rebuild with:

```text
.venv/bin/python scripts/generate_cycle3_fixtures.py
.venv/bin/python scripts/generate_cycle3_fixtures.py --check
```
