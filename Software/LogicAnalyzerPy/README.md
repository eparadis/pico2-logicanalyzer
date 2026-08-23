# Pico Logic Analyzer (Python)

This is the native Python 3.12 application for the V2 Pico logic analyzer
firmware. Its preferred interface is the local web frontend; the command-line
capture and validation tools remain available for automation and diagnostics.
It runs on macOS without the original C# desktop application. Other operating
systems are outside the supported scope.

The application can:

- list candidate USB serial devices;
- read and validate V2 identity and capabilities;
- capture explicit ordered channel selections in the supported 8-, 16-, and
  24-channel modes with a rising or falling edge trigger;
- display captures and imported replay/CSV data in the local web frontend;
- analyze transition and strobe-sampled parallel buses;
- export deterministic, trigger-relative CSV and secure replay data; and
- recover a timed-out or interrupted capture through the bounded V2
  cancellation, close/reopen, and re-identification sequence.

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

## Start the web frontend

The local web frontend is the preferred way to use `pico-la`. With one Pico
logic analyzer connected, run this from the repository root:

```bash
./Software/LogicAnalyzerPy/start_web.sh
```

The launcher creates `.venv` and installs the reviewed, hash-locked web runtime
when needed. It then runs `pico-la devices` and starts the server only when
exactly one matching analyzer is present. It prints the local browser address,
an SSH command for access from another computer, and keeps running until you
press `Ctrl-C`.

The default address is <http://127.0.0.1:4173>. To select another loopback
address or port:

```bash
PICO_LA_WEB_HOST=127.0.0.1 PICO_LA_WEB_PORT=8080 \
  ./Software/LogicAnalyzerPy/start_web.sh
```

The launcher never automatically chooses between multiple devices and does not
print the selected serial path. The path remains server-side and is not exposed
to browser code.

### Connect from another computer

Keep `start_web.sh` running on the Mac connected to the analyzer. Enable
**Remote Login** under **System Settings → General → Sharing** on that Mac, then
run the SSH command printed by the launcher on the other computer. It will look
like this:

```bash
ssh -N -L 4173:127.0.0.1:4173 USER@ANALYZER_MAC.local
```

Leave that SSH command running and open <http://127.0.0.1:4173> on the other
computer. The browser traffic travels through the authenticated, encrypted SSH
tunnel; the `pico-la` server itself remains bound to loopback and is not exposed
directly to the LAN.

If the printed SSH hostname or username is not suitable for your network,
override either value when starting the launcher:

```bash
PICO_LA_SSH_HOST=192.168.1.50 PICO_LA_SSH_USER=myuser \
  ./Software/LogicAnalyzerPy/start_web.sh
```

For manual startup or troubleshooting, enter the application directory and
install the web runtime:

```bash
cd Software/LogicAnalyzerPy
.venv/bin/python -m pip install --require-hashes -r requirements-web.lock
.venv/bin/python -m pip install --no-build-isolation --no-deps -e '.[web]'
.venv/bin/pico-la devices
.venv/bin/pico-la web \
  --host 127.0.0.1 \
  --port 4173 \
  --device-port PORT_FROM_DEVICES_OUTPUT
```

To view replay or self-timed CSV files without connecting an analyzer, omit the
device port:

```bash
.venv/bin/pico-la web --host 127.0.0.1 --port 4173
```

Both modes serve the checked-in production assets from a literal loopback
address. Starting the frontend does not invoke Node, contact a CDN, or expose a
public server.

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
