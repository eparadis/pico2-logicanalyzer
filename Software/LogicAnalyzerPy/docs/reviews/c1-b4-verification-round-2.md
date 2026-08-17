# C1-B4 independent verification — round 2

- Verifier: `/root/c1_b4_verification`
- Verdict: **pass for the non-hardware C1-B4 surface**
- Physical gate: pending; this verifier did not access the serial device or
  any hardware.

## Corrections re-reviewed

The atomic-output correction now records a backup immediately, removes an
empty backup if its original-to-backup rename fails, restores an already moved
first original when a second backup cannot be acquired, and removes temporary
artifacts on failure. The verifier injects the second original-to-backup rename
failure and confirms both original files are restored with no `.bak` or `.tmp`
residue. Once both new finals are installed, backup cleanup is intentionally
best-effort: an injected unlink failure preserves both new valid finals and an
orphaned backup rather than attempting an unsafe partial rollback. This is the
settled transaction disposition.

Replay bytes are compared directly for two independent writer calls, in
addition to the existing no-pickle, exact-`uint8`, canonical-metadata, and
exact-sample checks. They are byte-identical for the fixed capture.

For hardware smoke, the independent fake-service test uses a D0 waveform with
rising transitions at samples 1, 5, 9, 13, and 17. At 100 sample/s, it proves
the evidence records exactly: five transitions, 16-sample first/last span,
25 Hz measured frequency, `2/16 = 0.125` quantization allowance, named 0.02
uncalibrated-source allowance, and total 0.145 tolerance. It also verifies the
literal `<PORT_SUPPLIED>` replacement and absence of the supplied path from
the evidence. Both rising and falling first/last edge calculations and the
fewer-than-two-edge rejection are independently tested.

The procedure now derives quantization as two endpoint samples divided by the
observed span and explicitly labels the temporary 2% source allowance. For the
specified 100,000 sample/s, 1,000 Hz, 6,144-sample physical run, a roughly
6,000-sample same-polarity span contributes about 0.0334%; any operator
provided calibrated-source specification should replace the 2% allowance
before candidate freeze.

## Commands and results

- `pytest tests/verification/test_c1_b4_capture_artifacts_blackbox.py -q`:
  21 passed.
- `ruff check .`: pass.
- `mypy src`: pass.
- `pytest -m "not hardware" -q`: 186 passed, with the pre-existing expected
  duplicate-ZIP-fixture construction warning.
- `python -m pico_logic_analyzer --help`: pass.
- `git diff --check`: pass.

### Correction: hardware-evidence output failure

An added independent case injects failure of the final atomic evidence rename
after a valid fake waveform has passed measurement. The command returns exit
code 6, writes diagnostics only to stderr, and leaves neither the requested
evidence final nor a same-directory temporary file. The focused verifier count
is therefore 22 passed; the accumulated gate was rerun after this addition.
It passed with 188 non-hardware tests (and the expected duplicate-ZIP fixture
construction warning), plus Ruff, mypy, CLI help, and `git diff --check`.

## Remaining physical acceptance work

Run the explicit 100 ksample/s, 1 kHz, rising-D0 hardware smoke using the
already recorded 3.3 V protected-board wiring. Acceptance still requires the
sanitized evidence to show the requested 6,144 samples, 8-bit words,
nonconstant D0, observed rising transitions, measured frequency within the
recorded budget, artifact validation, and port closure. This remains an
acceptance/orchestrator hardware action, not a substitute for the non-hardware
verdict above.
