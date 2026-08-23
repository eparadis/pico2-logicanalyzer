# Pico Logic Analyzer (Python)

This is the native Python 3.12 command-line client for the V2 Pico logic
analyzer firmware. It runs on macOS and Linux without the original C# desktop
application.

The Cycle 2 foundation retains the accepted Cycle 1 client, which can:

- list candidate USB serial devices;
- read and validate V2 identity and capabilities;
- capture the normal eight-channel D0-D7 sample format with a rising or falling
  edge trigger;
- export deterministic, trigger-relative CSV;
- write and safely validate a provisional NumPy replay file; and
- recover a timed-out or interrupted capture through the bounded V2
  cancellation, close/reopen, and re-identification sequence.

The current shell remains intentionally bounded: it is not a replacement GUI.
Wider capture modes, sigrok decoder hosting, TCP/Wi-Fi operation, and stable
long-term replay compatibility remain future work. The existing C# applications
and firmware remain available as comparison and rollback paths.

## Install from source

From `Software/LogicAnalyzerPy/`:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-dev.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e .
.venv/bin/pico-la --help
```

The lock includes runtime, development, and build dependencies. The editable
install deliberately disables dependency resolution and build isolation so the
environment contains only the reviewed, hash-pinned dependency set.

You can use `.venv/bin/pico-la` directly or activate the environment:

```bash
source .venv/bin/activate
pico-la --help
```

`python -m pico_logic_analyzer` is equivalent to `pico-la` in the activated
environment.

## Offline web shell

Install the reviewed web runtime before its no-dependency-resolution editable
install, then start the checked-in production assets on a literal loopback
address. This shell neither invokes Node nor accesses serial hardware.

```bash
.venv/bin/python -m pip install --require-hashes -r requirements-web.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e '.[web]'
.venv/bin/pico-la web --host 127.0.0.1 --port 4173
```

## Connect to an analyzer

List USB devices matching the analyzer VID/PID:

```bash
pico-la devices
pico-la devices --json
```

Listing never opens or automatically selects a device. Supply the desired port
explicitly to every hardware command:

```bash
pico-la info --port PORT_PATH
pico-la info --port PORT_PATH --json
```

The attached board must run compatible V2 analyzer firmware. Serial operations
use finite timeouts and close the port on success and failure paths.

## Capture and replay

This example requests 6,144 samples at 100 kSa/s, with a rising trigger on D0
and 2,048 pre-trigger samples:

```bash
pico-la capture \
  --port PORT_PATH \
  --sample-rate 100000 \
  --trigger-channel 0 \
  --edge rising \
  --pre-samples 2048 \
  --post-samples 4096 \
  --csv capture.csv \
  --replay capture.npz
```

`--trigger-channel` uses logical channel numbers `0` through `7`. Cycle 1
always requests all eight channels in D0-D7 order and stores one raw `uint8`
sample word per sample instant.

Existing output files are rejected unless `--force` is supplied. The CSV and
replay files are validated and installed transactionally so a failed capture or
write does not leave a new apparently valid output.

Validate a replay without connecting hardware:

```bash
pico-la replay-validate capture.npz
pico-la replay-validate capture.npz --json
```

The replay schema is provisional. Loading is bounded, rejects unexpected or
unsafe archive members and dtypes, and disables object pickling.

## Hardware safety and smoke tests

Do not connect a signal until the analyzer/front-end revision, target voltage,
VRef, common ground, input range, and logical-to-physical channel mapping are
known. A bare Pico GPIO is not 5 V tolerant. Complete and review
[`docs/operator-input-template.md`](docs/operator-input-template.md) before a
new hardware setup.

The `hardware-smoke` and `hardware-recovery-smoke` commands are opt-in
acceptance tools for known, safe wiring. They require all signal parameters and
an explicit evidence path; committed evidence sanitizes the serial port. The
recovery command must use an operator-confirmed fixed-level input—never a
floating input—and sends the V2 cancellation byte only for an in-flight normal
capture.

See:

- [`docs/c1-b4-capture-procedure.md`](docs/c1-b4-capture-procedure.md) for the
  physical capture check;
- [`docs/c1-b5-recovery-procedure.md`](docs/c1-b5-recovery-procedure.md) for the
  timeout/recovery and second-capture check;
- [`docs/device-protocol.md`](docs/device-protocol.md) for the evidence-labelled
  V2 protocol notes; and
- [`docs/cycle-1-completion.md`](docs/cycle-1-completion.md) for the accepted
  Cycle 1 validation and hardware results.

The CLI exit codes are `0` success, `2` usage/configuration, `3`
connection/protocol, `4` capture timeout/cancellation, `5` validation/replay,
and `6` output I/O. Machine-readable output goes to stdout; diagnostics go to
stderr.

## Development validation

Run the canonical non-hardware checks from this directory:

```bash
.venv/bin/python -m pip check
.venv/bin/python -m ruff check .
.venv/bin/python -m mypy src
.venv/bin/python -m pytest -m "not hardware"
.venv/bin/python -m pico_logic_analyzer --help
```

To update the dependency lock deliberately, edit `requirements-dev.in` and
regenerate it with Python 3.12 and a current `pip-tools` installation:

```bash
pip-compile --upgrade --rebuild --allow-unsafe --strip-extras \
  --generate-hashes --output-file=requirements-dev.lock requirements-dev.in
```

Review every dependency and hash change before committing. The canonical
bootstrap must continue to use `--require-hashes`, followed by the editable
install with `--no-build-isolation --no-deps`.
