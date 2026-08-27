# C3-B1 pre-execution runner acceptance — round 2

## Identity and fresh immutable subject

- Acceptance identity: `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`), reused only in its original independent
  acceptance role.
- Corrected candidate commit/tree:
  `48d139f86aabcfa3e34567473c05ade13340107f` /
  `fc36f73089ee6d1c86e3bd6c922c44dffe15477b`.
- Accepted semantic-fixture commit/tree:
  `7c57a347bbe575e3f451383ea498f56abc362f26` /
  `02a408895dd834e6e6885218cb7323f46439e880`.
- Round-2 verifier pass commit:
  `8bcd7ba19795633a9e0e215c1d9f2cc47a893b03`.
- Round-2 accumulated-validation pass commit:
  `d307c3059a4e35c6389304f4782b3d06776fae2b`.
- Acceptance assignment commit/tree:
  `b354fe5014e9ad89a21207d5fba55a4f2f22f962` /
  `978957f4ad338f227dfb858b6766d4c1ea14665e`.

This is a complete fresh audit. The round-1 candidate, verifier, accumulated
result, acceptance, and provisional raw data transfer no pass. I repaired no
candidate, test, fixture, progress, contract, product, evidence, or runtime
input and created only this record.

## Findings and dispositions

1. RI013 discovery and historical execution: no discrepancy. The old
   `-I worker.py` launch ignored environment-only bytecode suppression. Exactly
   three ordered, previously authorized `uart-rx-valid-default` warm-ups ran;
   each created `snapshot_host.pyc`, after which all recorded repetitions and
   later requests failed before worker launch. Zero recorded baseline
   repetitions succeeded, and no SPI or I2C snapshot ran. The provisional JSON
   and caches were quarantined rather than promoted or corrected. RI013
   properly invalidated the old candidate and every dependent round-1 pass.
2. Correction ownership, scope, and identity: no discrepancy. Final runner
   owner `c3-b1-pre-execution-runner-implementor-replacement-3` made the
   seven-path runner-owned correction. The complete 11-path candidate surface
   is byte-identical to `48d139f...`; the accepted fixture/cap, expected output,
   exact snapshot, product, governing, legal/provenance, and excluded-scope
   bytes remain unchanged. Role separation is preserved.
3. RI013 correction and repeatability proof: closed. Both frozen launch JSON
   and actual `Popen` specification require exactly Python 3.12
   `-I -B worker.py`. Independent proof confirms `-I` ignores the environment-
   only setting. Two consecutive real inert sibling-import workers report
   bytecode disabled, import only exact-path-bound `probes.py`, leave no cache
   or inventory drift, and are followed by a valid recovery probe.
4. Round-2 verification: valid, fresh, and independent. The immutable record
   and 23-test verifier matrix bind the corrected candidate and freshly cover
   all 17 cap boundaries, binding/import/root/file/environment/CWD rejection,
   framing/accounting/resources, graceful termination, forced kill, stream and
   raw-descriptor closure, exact-child reap, recovery, fixed route, options,
   and API-v3 semantics. I reran only this inert/hostile non-decoder matrix:
   23 passed in 3.15 seconds.
5. Round-2 accumulated validation: complete and authoritative. The fresh
   result records 593/593 non-hardware tests with no skip, 190 corrected focused
   passes, clean Python 3.12.13 hash-locked install/check/Ruff/strict-mypy/help,
   fixture byte rebuild, 64-GiB set/readback, Cycle 1/2 evidence, installed and
   prohibited import/package/process/scope audits, cache-free repeatability,
   and exact Node 22 clean-install/lint/type/unit/build/assets/browser/
   performance passes. The two sandbox-restricted Python skips and first
   browser-server failure are explicitly invalidated by the corrected approved
   reruns. No mandatory check failed or remained skipped.
6. Route, method, provenance, scope, and safety: no discrepancy. The fixed
   private UART/SPI/I2C post-gate route and worker `execute_snapshot` call are
   structurally present; public `characterize` remains disabled and callers
   cannot select paths, modules, imports, or probes. The method truthfully binds
   `-I -B`, pending gate status, observations, warm-up/repetition rules, and
   whole-failure treatment. Accepted fixture, nine-source provenance, and
   project/legal limitations remain bound and unchanged. No raw candidate,
   threshold, manifest, checkpoint, installed runner exposure, or excluded
   scope is claimed.

No finding is open.

## Checks and SHA-256 identities

- Candidate commit/tree, parent, seven-path correction scope, and ordered
  evidence ancestry: passed.
- Quiet diff of the complete 11 candidate paths against `48d139f...`: passed.
- Quiet diff of the accepted fixture surface against `7c57a34...`: passed.
- `PYTHONDONTWRITEBYTECODE=1 rtk .venv/bin/python -m
  tools.cycle3_characterize.binding --check`: passed without output.
- `PYTHONDONTWRITEBYTECODE=1 rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_preexecution_runner_candidate.py`: 23 passed.
- Final targeted RTK process audit: the query PID had exited; no runner,
  worker, decoder, snapshot, or pytest process remained.

Independently recomputed SHA-256 values:

- binding: `1d36da4a8e06707c5fad8830c7037fd5aa601fdc8854dc4f33b9aec4b2d992eb`;
- launch: `3df74d88a1f013a7aa9f09c81d76a653159de09e9b42270137fb0f3956efbf27`;
- probes: `dc0d5ba2e5c1ec1f3e805f9a41a92b29e5edce8a4bb6172ef6fc82dbf8848b2a`;
- runner: `2f0d32ec2d2fea047cb5f78e6b3d32753e6d69d3f9d0f398bd589691011ef942`;
- worker: `76124299334fc4fb5a7ea5d28750afff9b19f59b4fda0618dd0be215f59f890c`;
- method: `8ef7bdac50554fb42ec97d3c5d685d3f6b55074c82478c750e4e62ff3d318325`;
- implementation test: `74e5c8d823f1f58ffc84e57bbae7264ee80c67586dec1e3e816e8ccce8f341c1`;
- verifier record: `0fc07aea133702352d0dee74d18e4287f707481b598773481d7c9d37501942dc`;
- verifier test: `c6cec19e2e97a833315270d2ae9dbf1cd9b19433122cf545b1f5d2512204bf5b`;
- accumulated record: `4656a53c49f7abc93d5b68faa0e2689537c69221499193830c0c13882999d645`.

## Safety and scope statement

No fourth snapshot execution or raw retry occurred. I did not call the private
snapshot route, `_orchestration_execute_approved_snapshot`, or
`execute_snapshot`. No decoder, approved snapshot, compatibility helper,
fixture generator, product runtime, C#/.NET/pythonnet/libsigrokdecode/sigrok
runtime, hardware, network install, browser server, excluded action, or Cycle 4
work ran. Only static inspection and the existing inert/hostile non-decoder
verifier probes were used. No worker remains.

## Verdict

`pass`
