# CLI contract

The installed executable is `pico-la`; `python -m pico_logic_analyzer --help`
is equivalent for source installs. C1-B3 implements only `devices` and `info`;
capture, replay, and hardware-smoke commands remain owned by later batches.

```text
pico-la devices [--json]
pico-la info --port PORT [--json] [--timeout SECONDS]
pico-la capture --port PORT --sample-rate HZ --trigger-channel CHANNEL
                --edge {rising,falling} --pre-samples N --post-samples N
                --csv PATH --replay PATH [--timeout SECONDS] [--force]
pico-la replay-validate PATH [--json]
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
