# C2-B3 implementation evidence — round 1

- Implementation identity: `cycle2-implementor-replacement-5`
- Product candidate: `90adb3adb38a938ce470fa854e6fc7b98e1501c9`
- Product tree: `5a09d57e4caa266a43f164edaffc94fc9a3236d7`
- Physical execution: 2026-08-23; explicit port recorded only as
  `<PORT_SUPPLIED>`; no serial number or location retained.
- Device identity: `LOGIC_ANALYZER_PICO_2_V6_0`.
- Electrical/operator prerequisites: protected integrated LogicAnalyzerV2, 3.3 V
  VRef, common ground, safe approximately 1 kHz 3.3 V fan-out to D0/D8/D16/D23,
  analyzer-input direction, and fixed-low D1 were reconfirmed before execution.

## Bounded sequence

1. Identity succeeded with the fixed V2 identity.
2. The accepted fixed-low D1 recovery sequence succeeded: 0.25 s bounded
   in-flight cancellation, one `ff`, bounded drain, close/reopen,
   re-identification, and a second rising-D0 capture without a power cycle.
   The second capture was 6144 samples with 41 rising transitions over 4000
   samples, measured 1000.0 Hz, and tolerance 0.0205.
3. Independent raw schema-2 and CSV audits read each replay archive directly,
   reconstructed canonical CSV, and checked the driven-bit projection rather
   than accepting CLI success alone.

| Ordered channels | dtype | Count | Driven mask | Rising transitions | Frequency Hz | Tolerance | Upper byte | CSV SHA-256 | Replay SHA-256 |
| --- | --- | ---: | --- | ---: | ---: | ---: | --- | --- | --- |
| D0-D7 | `uint8` | 6144 | `0x01` | 42 | 1005.641403 | 0.020490557 | n/a | `fc4c4759394b4fc5180440d09dfe6a0082ca6401b93f18a38782ce3012fa37a3` | `b1401639e128f78f964552f8e0c613bb3e70ff86b17c015382547d96ad031ad6` |
| D0-D15 | `uint16` | 6144 | `0x0101` | 42 | 1010.349926 | 0.020492854 | n/a | `ee1e2bf48400c520c6e3a6aa25ce5917303bf720bd3cddf713e1cececfdb2b9f` | `614765cd3f1385153e348d91a49d75bc47e214640b3532aba8418adb89ff58a1` |
| D0-D23 | `uint32` | 6144 | `0x810101` | 42 | 1005.394801 | 0.020490436 | all bits 24-31 zero | `c6255f31621b1a366dc839af3f94240a2b897760ed2433a43e6f33495866efe5` | `af3b61f1081f7e272e0d429bae004ddccdc11363cff2061dd25228ddebae41bd` |

For every width the driven projection contained both all-low and all-high
states. Unconnected/floating bits were observational only and were not used as
acceptance criteria. The sanitized recovery artifact SHA-256 is
`40745b7e3be4e53d8b9957f72efd310fcd5c1a309395213b36fbf392da482ad1`.

## Scope and safety

No firmware build/change/flash, bootloader, Wi-Fi, power cycle, unknown-pin
probe, persistent device action, browser UI, or other capture mode occurred.
Raw artifacts remain outside the repository; this record contains no machine
port, serial, location, local URL, or capability-bearing values.
