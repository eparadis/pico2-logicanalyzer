# CLI contract

The installed executable is `pico-la`; `python -m pico_logic_analyzer --help`
is equivalent for source installs. C1-B1 declares help only—operational command
behavior is owned by later batches.

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
