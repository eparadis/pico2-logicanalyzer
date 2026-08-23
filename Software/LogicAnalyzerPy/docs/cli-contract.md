# CLI contract

The installed executable is `pico-la`; `python -m pico_logic_analyzer --help`
is equivalent for source installs. The accepted Cycle 1 discovery, capture,
replay, and hardware-smoke behavior remains available while its Cycle 2
successors are owned by their respective batches. The `web` command currently
starts only the inert, loopback-only offline shell; it does not open serial
hardware.

The web shell accepts literal IPv4 or IPv6 loopback addresses and `--port 0`
for an OS-assigned port. On successful bind it writes exactly
`pico-la web: ready http://AUTHORITY/` to stdout, where `AUTHORITY` is the
actual canonical loopback authority (IPv6 is bracketed). `GET /api/v1/readiness`
returns `{"status":"ready","api_version":"v1"}`. A valid protected
`POST /api/v1/shutdown` returns 204, expires the capability cookie, and exits
the process with status 0. The supported frontend gate is Node `22.14.0`,
Playwright `1.50.1`, and the commands `npm ci`, `npm run lint`,
`npm run typecheck`, `npm test -- --run`, `npm run build`, and
`npm run test:browser`.

```text
pico-la devices [--json]
pico-la info --port PORT [--json] [--timeout SECONDS]
pico-la capture --port PORT --sample-rate HZ --trigger-channel CHANNEL
                --edge {rising,falling} --pre-samples N --post-samples N
                --csv PATH --replay PATH [--timeout SECONDS] [--force]
pico-la replay-validate PATH [--json]
pico-la web [--host LOOPBACK_ADDRESS] [--port PORT]
pico-la hardware-smoke --port PORT --signal-hz HZ --sample-rate HZ
                       --trigger-channel CHANNEL --edge {rising,falling}
                       --pre-samples N --post-samples N --evidence PATH
pico-la hardware-recovery-smoke --port PORT --idle-channel CHANNEL
                       --idle-level {0,1} --cancel-after SECONDS
                       --signal-channel CHANNEL --signal-hz HZ --sample-rate HZ
                       --edge {rising,falling} --pre-samples N --post-samples N
                       --evidence PATH
```

Exit codes are 0 success, 2 usage/configuration, 3 connection/protocol, 4
capture timeout/cancellation, 5 validation/replay, and 6 output I/O. Requested
machine data belongs on stdout; diagnostics/progress belong on stderr.

`devices --json` writes exactly one JSON object with a `devices` array. Every
entry has `device`, `vid`, `pid`, `serial_number`, `location`, and `description`
keys; unavailable optional metadata is `null`. Text output is either the exact
empty-list message `No supported Pico logic analyzer serial ports found.` or one
candidate per line in sorted path order. Candidate records match only VID
`0x1209` and PID `0x3020`; listing does not select or open a port.

`info` requires `--port`. Its text output is exactly the five validated V2
identity fields in firmware order. `info --json` writes one object with
`identity`, `max_frequency_hz`, `blast_frequency_hz`, `buffer_size`, and
`channel_count`. JSON is compact, sorted-key UTF-8 on stdout followed by LF.
An omitted timeout is 10 seconds; supplied values must be finite and positive.
Serial/permission/unplug/timeout/malformed-identity diagnostics return exit 3
and write no machine data to stdout.
