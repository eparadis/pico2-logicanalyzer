# Cycle 1 operator input (complete before hardware work)

Do not open a board port or connect a signal until every required item is known.
Unknown electrical details block the hardware path.

| Required item | Operator value/confirmation |
|---|---|
| Explicit serial port (use placeholder in commits) | `<PORT_SUPPLIED>`; operator supplied a live port out of band |
| Board variant and firmware identity/build, if known | Pico 2; latest checked-in V2 source, `BOARD_TYPE=BOARD_PICO_2`; reported identity pending C1-B3 |
| Input-front-end / level-shifter revision | 5 V protection confirmed present; exact revision pending operator record before C1-B3 hardware I/O |
| Target logic voltage | Pending operator record before hardware I/O |
| Level-shifter VRef | Pending operator record before hardware I/O |
| Permitted analyzer input range | Pending operator record before hardware I/O |
| Confirmed common-ground point | Common ground confirmed connected; exact point pending operator record |
| D0–D7 to target header/GPIO map | Firmware source maps D0–D7 to GPIO2–GPIO9; protection-board header mapping must be confirmed before hardware I/O |
| Periodic signal source and expected frequency | 1 kHz on operator-described board “channel 1”; exact logical D0–D7 identity must be confirmed before capture |
| Sample rate, trigger D0–D7, edge, pre/post samples | Orchestrator may select conservative valid values after capabilities and mapping are confirmed |
| Physical polarity to exercise | Orchestrator may select and record rising or falling |

Safety: a bare Pico GPIO must **never** receive 5 V. A 5 V target requires a
compatible, correctly referenced level shifter/probe. Confirm ground before
signal wiring. No firmware flashing, bootloader, Wi-Fi, or persistent mutation
is part of this procedure.
