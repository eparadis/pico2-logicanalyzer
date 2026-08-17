# C1-B3 explicit-port identity procedure

This procedure is opt-in. It does not choose or open a port until the operator
supplies `--port <PORT>`. It does not flash firmware or alter persistent device
state.

Before physical use, complete `docs/operator-input-template.md`: in particular,
confirm the board, firmware intent, safe electrical setup, and permission to
open the supplied port. Do not connect unknown-voltage signals. A bare Pico GPIO
must never receive 5 V.

List USB candidates without opening any port:

```bash
pico-la devices
pico-la devices --json
```

Only records whose pySerial metadata has VID `0x1209` and PID `0x3020` are
listed. Linux and macOS records can omit serial number, location, or description;
those fields appear as `null` in JSON and are simply omitted from text. Listing
is advisory and never selects a candidate for another command.

Read identity from the one port selected by the operator:

```bash
pico-la info --port <PORT> --timeout 10
pico-la info --port <PORT> --timeout 10 --json
```

The text output is the five V2 identity lines in firmware order. JSON is a
single canonical object on stdout. Diagnostics only go to stderr. Exit status
is `0` on success, `2` for invalid invocation/timeout configuration, and `3`
for permission, unplug, serial, timeout, or malformed-identity failures.

For each identity operation the host creates the serial object with no port,
sets 115200 baud, 8 data bits, no parity, one stop bit, no XON/XOFF, RTS/CTS, or
DSR/DTR flow control, and sets finite read/write timeouts. It asserts DTR and
RTS, assigns the explicit port, opens it, waits 100 ms, then drains at most 1024
already-queued bytes for at most 200 ms before sending the identity frame. USB
CDC devices may ignore line settings; DTR/RTS are nevertheless retained because
the compatible C# client asserts both. The source-derived timings and deployed
identity remain pending physical C1-B3 confirmation.

The transport owns one byte buffer for both identity text and later binary
phases; it does not combine a text reader with a binary reader. Identity fields
strictly accept LF or CRLF termination; a lone or embedded carriage return is
not normalized. Every success,
timeout, malformed response, permission failure, and unplug path closes the
port. The optional service API
`V2DeviceService.identify_after_reopen(<PORT>, timeout)` intentionally performs
two explicit identity operations separated by close/reopen for a fake or
operator-controlled smoke; it is not run automatically and does not open real
hardware during non-hardware tests.
