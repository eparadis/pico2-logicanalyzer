# Cycle 1 operator input (complete before hardware work)

Do not open a board port or connect a signal until every required item is known.
Unknown electrical details block the hardware path.

| Required item | Operator value/confirmation |
|---|---|
| Explicit serial port (use placeholder in commits) | `<PORT_SUPPLIED>`; operator supplied a live port out of band |
| Board variant and firmware identity/build, if known | Pico 2; latest checked-in V2 source, `BOARD_TYPE=BOARD_PICO_2`; reported identity pending C1-B3 |
| Input-front-end / level-shifter revision | Operator confirms the integrated checked-in `LogicAnalyzerV2` protection-board design is installed and matches its documented input range |
| Target logic voltage | Operator-confirmed 3.3 V periodic source |
| Level-shifter VRef | Operator-confirmed 3.3 V selection |
| Permitted analyzer input range | Operator confirms the installed board matches the checked-in design and that the 3.3 V source is within its permitted input range |
| Confirmed common-ground point | Operator confirms common ground is connected at the board point labeled `GND` |
| D0–D7 to target header/GPIO map | Checked-in `LogicAnalyzerV2` and `BOARD_PICO_2` sources map labeled inputs 1–8 to logical D0–D7 and GPIO2–GPIO9; after examining the installed circuit, the operator directly confirms labeled input `1` reaches Pico 2 GPIO2, therefore logical D0 |
| Periodic signal source and expected frequency | Operator-confirmed 1 kHz, 3.3 V periodic signal on labeled input `1`, physically confirmed to reach D0/GPIO2 |
| Sample rate, trigger D0–D7, edge, pre/post samples | Orchestrator may select conservative valid values after capabilities and mapping are confirmed |
| Physical polarity to exercise | Orchestrator may select and record rising or falling |

Safety: a bare Pico GPIO must **never** receive 5 V. A 5 V target requires a
compatible, correctly referenced level shifter/probe. Confirm ground before
signal wiring. No firmware flashing, bootloader, Wi-Fi, or persistent mutation
is part of this procedure.
