# C2-B6 native macOS acceptance procedure

This procedure is opt-in and runs only after every fake, static, API, frontend,
browser, and performance gate is green. The operator supplies the one explicit
runtime port. Evidence must replace it with `<PORT_SUPPLIED>` and must not store
the USB serial, location, capability cookie, or device identity string.

## Preflight

Confirm the Pico 2 is running the checked-in V2 firmware; protection, 3.3 V
VRef, common ground, and analyzer-input direction remain correct; the safe
approximately 1 kHz source is connected to board-label pins 1, 9, 17, and 24,
corresponding to D0, D8, D16, and D23; and the fixed-low D1 recovery input is
unchanged. `pico-la devices` may be used read-only to confirm the operator's
port, but neither the harness nor server may select a candidate automatically.

Before execution, root obtains authorization for the exact stable commands.
No firmware, bootloader, Wi-Fi, persistent-state, packaging, or public-serving
command is permitted.

## Authorized sequence

1. Run `scripts/c2_b6_native_acceptance.py` with the operator-supplied explicit
   `--port` and a temporary evidence path. It performs identify, close/reopen
   and re-identify, bounded 8/16/24 normal captures, then a second 24-channel
   capture. Its durable JSON contains only `<PORT_SUPPLIED>`, opaque
   `device-1`, capabilities, bounds, and observed physical channel numbers.
2. Set `PICO_LA_DEVICE_PORT` only in the authorized process environment and run
   `npm run test:native` with `B6_NATIVE=1`. The fixed command line contains no
   port. The server reads the explicit environment value at launch and never
   exposes it through HTTP. The installed locked Chromium workflow identifies,
   captures 8/16/24, displays waveform/trigger/cursor data, analyzes and exports
   transition and distinct-strobe bus data, reopens/re-identifies, captures a
   second time, checks URL/DOM/storage/console/request nondisclosure, and shuts
   down.
3. Independently inspect the temporary JSON and browser result for bounded
   counts, the D0/D8/D16/D23 pattern, no raw port/identity/capability, serial
   close between operations, and no persistent-device change. Copy only the
   sanitized reviewed evidence into the repository.

On cancellation or timeout, the only device mutation permitted is the accepted
one-byte `ff` recovery while a normal capture is in flight, followed by bounded
drain, close, reopen, and re-identification. Any failure stops the sequence;
there is no automatic retry, port substitution, threshold rebase, or power-cycle
demand.
