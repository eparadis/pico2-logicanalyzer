# C3-B1 semantic-fixture correction — implementation round 1

- Identity: `c3-b1-semantic-fixture-implementor-replacement-7`
- Governing contract: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Starting candidate: `ad731527612cbaa36701b50caf6019cef9a653f7`
- Finding: `C3B2-IF001`
- Scope: the authoritative B1 timeline
  `uart-msb-9bit-boundary-incomplete` and deterministic generated bindings only.

## Static derivation

The frozen UART source computes a sample point as
`ceil(frame_start + (bit_width - 1) * sample_point / 100 + bitnum * bit_width)`.
The timeline has `frame_start = 1`, `bit_width = 10`, and `sample_point = 99`.
The start sample is therefore `ceil(1 + 9 * .99) = 10`; successive data-slot
centres are 20, 30, 40, and 50 before the declared capture ends at sample 56.
The next centre would be 60 and cannot return.

The human-readable transitions make real edges at 11, 21, 31, and 41; `[51, 0]`
is a same-level declaration, not an edge. The
frozen `decode()` loop waits on both the scheduled data condition and an edge
condition, so those edges return before the next scheduled centre.  The exact
trace is consequently 1, 10, 11, 20, 21, 30, 31, 40, 41, 50, then terminal
end-of-input at 56.  The terminal wait is `[{"skip": 10}, {"0": "e"}]` with
both alternatives false.

At rising edges 11 and 31, `inspect_edge()` calls `inspect_idle()` and begins
an idle candidate. Therefore the source's next waits include the third
alternatives `{skip: 110}` at samples 20 and 40, and `{skip: 101}` at samples
21 and 41. The edge alternatives match at 21 and 41 and their low signals
clear the idle candidates. These alternatives are present even though neither
idle timeout wins.

At sample 10 `get_start_bit()` emits the Python STARTBIT record and start-bit
annotation at 5..15.  At each of samples 20, 30, 40, and 50,
`get_data_bits()` immediately emits one RX data-bit annotation: values
1, 0, 1, 0 at 15..25, 25..35, 35..45, and 45..55.  The source emits no DATA,
binary, or FRAME record until all nine bits exist.  Normal end-of-input aborts
the next wait and does not retract those six already-emitted records.

The closed option-matrix row `uart-sample_point-99` remains a separate
`direct-fixture` binding to `direct-uart-sample_point-99`. The corrected named
incomplete fixture is separate boundary coverage. I retained its explicit 99%
declaration because it is coherent with its declared timeline and requires a
smaller correction than changing declared fixture coverage; it does not claim
to own or replace the separate matrix witness.

## Changes and deterministic artifacts

- `scripts/generate_cycle3_fixtures.py`: corrected timeline meaning, 99-percent
  wait schedule, finite end coordinate, and complete pre-termination record
  transcription.
- `tests/implementation/test_cycle3_fixtures.py`: added a focused static test
  for every wait/match/pin/terminal and record coordinate/value; also asserts
  the direct `sample_point: 99` matrix binding.
- `testdata/decoders/cycle3/semantic-fixtures.json`:
  `1d97cf3ff4fb560e7dd73b621da0e40d7f1fb310b60c2d43fcb59f3ebf91a329`.
- `testdata/decoders/cycle3/experiment-caps.json`:
  `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.
  Its fixture-corpus-byte derivation changed deterministically.
- `testdata/decoders/cycle3/manifest.json`:
  `ce8eceb72480d042ef298cb6fe6944a4808fed0644e729c8c2de9fa1955ec37f`.
  Only affected digest bindings changed.

## Commands and results

- `python3 scripts/generate_cycle3_fixtures.py` — passed; static generator only.
- `.venv/bin/python -m pytest tests/implementation/test_cycle3_fixtures.py -q -k uart_msb_9bit_incomplete` — passed (1 passed).
- `.venv/bin/python -m pytest tests/implementation/test_cycle3_fixtures.py -q -k 'not cycle3_fixture_surface'` — passed (11 passed, 1 deselected); the deselected test is the unrelated inventory failure described below.
- `.venv/bin/python -m ruff check scripts/generate_cycle3_fixtures.py tests/implementation/test_cycle3_fixtures.py` — passed.
- `.venv/bin/python scripts/generate_cycle3_fixtures.py --check` — passed.
- `git diff --check` — passed.
- Strict mypy over these pre-existing untyped fixture files is not currently
  applicable as a green gate: it reports 180 baseline `object`/collection
  errors throughout both whole files, including numerous lines outside this
  correction. No suppression or type-scope weakening was added.
- The full fixture-file pytest invocation is presently blocked by four
  pre-existing additional JSON artifacts in the fixture directory
  (`b1-final-candidate*.json` and `threshold-proposal*.json`), which violate
  its exact-six-file assertion. They are outside this role's owned paths and
  were preserved.

## Oracle exclusions and readiness

No decoder, host, B2 code/test, raw observation, C#/.NET/pythonnet,
libsigrokdecode, sigrok-cli, external/reference runtime, or characterization
output was inspected or executed. Expectations were derived only from the
declarative transitions, frozen UART source as inert text, and Step-5 contract.

The correction is ready for independent fixture verification once the
pre-existing full-file pytest inventory issue is resolved or explicitly
qualified by the orchestrator. It is not an acceptance or verification verdict.
