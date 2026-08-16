# Cycle 1 orchestration progress

## C1-B1: Preflight, scaffold, and narrow protocol evidence

- State: In progress
- Objective: Create a runnable Python 3.12 skeleton and narrow V2 evidence without guessing a native binary layout.
- Prerequisites: Approved preparatory documents; operator assertion of intended V2 target; writable workspace.
- Implementation agent: `/root/c1_b1_implementation`
- Verification agent: `/root/c1_b1_protocol_verification`
- Acceptance agent: `/root/c1_b1_acceptance` (assigned after integration)
- In scope: scaffold, contracts, operator template, evidence schema, protocol notes, lock, CI, and focused scaffold tests.
- Out of scope: production serial/capture, GUI, Qt/pythonnet/Roslyn, firmware changes, and later-cycle work.
- Owned files: all new project files except `testdata/protocol/`, `docs/protocol-fixture-provenance.md`, and acceptance-review records; `.github/workflows/logic-analyzer-python-cycle1.yml` only in `.github`.
- Source evidence: V2 `LogicAnalyzer_Structs.h`/`LogicAnalyzer.c`; C# `AnalyzerDriverBase.cs`, `LogicAnalyzerDriver.cs`, `CaptureSession.cs`, and `VersionValidator.cs`.
- Acceptance evidence: clean source install, CLI help, Ruff, mypy, pytest, independently authored golden fixtures, and protocol provenance review.
- Authority notes: dependency/Python installation requires the normal approval
  mechanism; no hardware I/O or firmware/persistent-device mutation in this
  batch.
- Risks/unknowns: no known-good C#/board trace is checked in; fixture provenance
  and deployed-layout confirmation are verifier/C1-B3 work. Linux/macOS CI must
  both pass before this checkpoint is accepted.

## Deferred work

- C1-B2 owns production models, codec, parser, fake/replay transport, and negative protocol tests.
- C1-B3 owns pySerial, explicit-port identity, and physical identity confirmation.
- C1-B4 owns physical capture and CSV/replay writes; C1-B5 owns lifecycle hardening and final hardware proof.
