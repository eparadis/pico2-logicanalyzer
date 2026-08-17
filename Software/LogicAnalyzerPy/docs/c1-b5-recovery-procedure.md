# C1-B5 recovery smoke procedure

`hardware-recovery-smoke` is an opt-in physical proof, not a general abort
command. Do not run it until the operator confirms the fixed-level idle input.
For the Cycle 1 proof, the operator confirmed labeled input `2`/D1/GPIO3
connected directly to the analyzer `GND`, making it fixed low. The established
1 kHz 3.3 V protected input `1`/D0/GPIO2 connection remains the periodic
signal.

```console
pico-la hardware-recovery-smoke --port <PORT> --idle-channel 1 --idle-level 0 \
  --cancel-after <SECONDS> --signal-channel 0 --signal-hz 1000 \
  --sample-rate 100000 --edge rising --pre-samples 2048 --post-samples 4096 \
  --evidence <EVIDENCE.json> --timeout 10
```

The command starts a normal capture on the confirmed idle channel, waits the
bounded delay, sends exactly one `ff` while that capture is in flight, drains at
most 4096 bytes under one recovery deadline, closes, reopens and identifies,
then captures D0. Evidence is atomically written and sanitizes the port as
`<PORT_SUPPLIED>`. Timeout or Ctrl-C performs the same internal recovery before
returning exit 4. It never flashes firmware or changes persistent device state.
