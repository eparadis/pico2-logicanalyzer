# Cycle 3 completion-proof candidate

## Immutable subject and state

- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact final product and B5 evidence candidate/tree:
  `f8f78c89655011e3ee3e74559ff9886c93eac690` /
  `e6b5d5f0afaf3023ec398cb9c42c6d42d5a1790b`.
- Fresh verified and hosted evidence commit/tree:
  `2fb89fc8c36d93b4435032c07783532d6a8aa933` /
  `f155c06c8d61e9f454f2b7026afa0805999c4300`.
- Exact committed B5 checkpoint:
  `d7e79e03cf9d1f461cc30f87a84fc5d21c2b62aa` / tree
  `40849b62bb543be07863743c2d6a8d615585abe4`.
- Checkpoint state: `Complete; Cycle 3 closure pending`.
- Open findings: none. Deferred findings: none. Remainder: `closure pending`.

The repository was clean at the committed B5 checkpoint. This file adds only
the immutable completion-proof candidate and does not change product, tests,
fixtures, expected values, methods, limits, dependencies, workflow, manifests,
or prior evidence.

## Requirements and stopping conditions

The accepted B5 manifest at commit
`5d5712477e41ee269f2828787c9fddc840c414b6`, SHA-256
`c67031fa0f9590e9cc44134e382f2c3bec70e0744c91a4f26be6a559699e1532`,
maps every requirement R1-R26 exactly once and stopping conditions 1-17
exactly once to immutable `pass` evidence. Its distinct manifest-verification
record has SHA-256
`a866d5057c35b96a3e5f81bb1d8ac0e2a6329fe839eb90f73be353cb1320937a`
and is committed atomically with the unchanged manifest.

- R1-R5 and conditions 1-5: exact snapshot/provenance/license, independent
  semantic fixtures, five edge decisions, characterization method and
  environment, raw observations, closed import graph, and prelaunch identity
  validation pass.
- R6-R16 and conditions 6-10: one fresh worker, frozen private API and typed
  result, strict IPC rejection, all hard limits, timeout/cancel/terminate/kill/
  reap/recovery, UART/SPI/I2C conformance, and in-memory/replay/CSV identity
  pass.
- R17-R25 and conditions 11-14: installed public library and CLI behavior,
  locked installation, Ruff, strict typing, complete applicable regression,
  exact hosted macOS validation, prohibited-use absence, Cycle 1/2 evidence,
  rollback, and macOS-only scope pass.
- R26 and condition 15: final corrected no-retry observations contain exactly
  three unrecorded protocol warm-ups and 15 retained runs, 18 launches total;
  every observed maximum is below the unchanged approved ceiling.
- Condition 16: five distinct ordered implementation, verification,
  accumulated-validation, acceptance, manifest-verification, and checkpoint
  histories are committed without a premature manifest or transferred pass.
- Condition 17: excluded features, runtimes, platforms, package construction,
  publication, conveyance, and Cycle 4 are absent.
- Condition 18 ordering completed so far: the unchanged B5 manifest and its
  verification record were committed together before the separate B5
  checkpoint. The literal remainder is `closure pending`.

## Exact decoder, host, public API, and resource identities

The closed decoder resource revision is
`407b5ef039aa0474c400c0721749baa126e53270`. Its exact nine-file SHA-256
inventory is:

- UART `pd.py`:
  `67655f53162c531bc6eb77d9d29b384edec80a2dd5bd741897b4aa2afc52ffcc`;
  UART `__init__.py`:
  `351098a23f5caa205068688550af53bd44a63776e1d02921ba32487ce720b92f`.
- SPI `pd.py`:
  `ef9cac5098404dc164094712e9175ba3715233248d8bbc23cb85ed3fc51d5d3d`;
  SPI `__init__.py`:
  `91b207f82c59fe1c12ad1458ef669c4293c7e4c8dd19bec14e78b455305af56c`.
- I2C `pd.py`:
  `b6899137fb5b505433e696d319b7f3cc88519b43e2a2e7fea1a9f770ba10a305`;
  I2C `__init__.py`:
  `37931874732ea0b3ca13784b8df4cd90949a2c1b5822feae5d5df6da81ee886f`.
- helper `common/srdhelper/mod.py`:
  `602b27901820a27af5fcf317b34af1a17d1449fa1ad21279507d1d5ab8acebd6`;
  helper `common/srdhelper/__init__.py`:
  `125b0616dfdd974c2f6e0e83e61cf9cdd21340f9ab11ac7b97b648792dad05d1`;
  compatibility shim `sigrokdecode.py`:
  `385124002ec16379a2542f2905c5ce41f3402032458d89f49617623ab7aaf01a`.

The accepted private-host source identities are `_decode/__init__.py`
`168eca85174bb37975b131e0525e7dbf762e58337d690405be012a8f70208f57`,
`compat.py` `763bdf54d636a98ff95ca1581184038cb24e04788acf85351897d813b214083a`,
`host.py` `8a555fb08a88badf59bdabe2f558bcd9f7918ccebd52d3c2539013bff733c990`,
`identity.py` `06813d48c1708b264694488f06b4309f84b3c3a6b38a593a5c314dbdeca2d070`,
`ipc.py` `f3502eba02c66c957c6fc12a9d6c7e181d8c5e0c8e75ea75cb59c8027c460114`,
`lifecycle.py` `9ca920ea6e2a10222509e02aad58111c51b15439a2fec21c130b27a003eb3c79`,
`loader.py` `5f2c47ece17df5b2e6c7682077952ba9e9d957fe9c0208929fc00d82d78aed83`,
`model.py` `19854e57491ff3b1271ed9e0012c878c0ed403b07f28bb5b17a9068d10e158e7`,
and `worker.py` `9a01a2c03ecb255fb3dddc43036a8d4ba3b7b62923e4a687748a1db70ffdb160`.

The installed public API, CLI, and typed marker SHA-256 values are respectively
`d5cd8b843bf2bd847dc42a7fa550d5756615177d77e80912472d088b9e6519db`,
`c3acce4965faeff55c6177dfdfff840d7a2b9c65a6ae4b05b45f26974f1d3ddc`,
and `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
Package metadata and public decoding documentation are
`ead05ffbfab1c046b43087993d7dbd1056cdc9d6ebbb87d481092bacfb30a6cf`
and `52c068632bbae7c94d9921c56c2d526610af2bcddf6abe355746ec3e1d1e1cab`.

## Fixture, method, threshold, dependency, and legal identities

- Fixture generator:
  `a101ae13cba938aa4d574fd1df3e4cc09dc845b2a643088cfee4a79313c3266f`;
  semantic fixtures:
  `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`;
  fixture manifest:
  `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`.
- Characterization method:
  `f228f02892fc2ead00713606dc795850e14651baafc42a0974d1dbd48da86341`;
  runner:
  `0ba17a1357f8326a8116c79c16c300f4bb24bde6796c6d1c97ca692e332bcf80`;
  worker:
  `76124299334fc4fb5a7ea5d28750afff9b19f59b4fda0618dd0be215f59f890c`;
  launch configuration:
  `3df74d88a1f013a7aa9f09c81d76a653159de09e9b42270137fb0f3956efbf27`.
- Exact round-4 threshold proposal commit
  `b680aa59fba4a18da2aeaacc8cbd7ad3a68784e0`, proposal SHA-256
  `98e48bb1882104d893a1d4d85659845ff20054f9b52f0b09fdf73efad2547e3c`,
  and explicit operator-decision SHA-256
  `ff1ba9665174b0912adea9eb4682d1a9e6839c6ec9b5efce073a9b055303aba6`.
  All 18 hard limits and 11 regression ceilings are exact inclusive maxima;
  SPI accepts eight-bit words and rejects nine.
- Final measurement packet:
  `980308fc3a144d1af70959793fb9e0b4476658b9856d56eb101876fc9fedb54e`.
- Development lock:
  `4efa0b1d42e5162c7a20177d1dd5e78083d75a87d2405709e04b1bcbd4f33c53`;
  optional-web lock:
  `4b0feeadf92c0bcb9f2790cc62f6b6e2f7da8937f30ff50d0c9092fd003b8145`;
  Node lock:
  `d388a2668b3f65edeb62ee99da3ad37ffc56ab1ca3439b6d418a6bbe92e838d9`;
  production-asset manifest:
  `00d553697834509104a5751affc2abad48ec619bbd7f167ac2f8a1de0953d9d9`.
- GPL-3.0-only project license:
  `3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986`;
  retained GPL-2.0-or-later notice:
  `ab15fd526bd8dd18a9e77ebc139656bf4d33e97fc7238cd11bf60e2b9b8666c6`;
  retained historical MIT notice:
  `6115c1f056dc347dd180c44bd5fb862cf1e3d48a34fecd0b6e5a0e4193b752f6`;
  attribution record:
  `3765302c5ba6602633a44b934da41cb94aba3d25455d91582f3c29bf1c0cac1e`.

The engineering disposition is GPL-3.0-only. Rights-holder or qualified-
counsel confirmation remains required before conveyance because shim
ownership, historical MIT labeling, and combined-work treatment remain legal
questions. This is not a legal conclusion and grants no conveyance authority.

## Canonical validation results

- Clean CPython 3.12.13 core and web environments were created under ignored
  `.tmp/`, installed from both hash-locked requirements files, installed the
  source without dependency resolution, and passed both dependency checks.
- Ruff passed; production mypy passed 31 files; strict installed-consumer mypy
  passed; installed `pico-la` and `pico-la decode` help passed.
- The real hostile-child gate passed three cases. The exact governed
  non-hardware partition collected 1,528 cases, selected 1,490, and completed
  with 1,483 passes, seven explicitly classified skips, and 38 transparent
  historical deselections. No applicable mandatory product gate failed.
- Fixture regeneration `--check`, all five Cycle 3 manifest validations,
  UART/SPI/I2C conformance, cross-source identity, containment, IPC, security,
  cancellation, process cleanup, Cycle 1/2 regression, resource, license,
  rollback, scope, and second digest verification passed.
- Frontend lock install, lint, typecheck, five unit tests, 29-module production
  build, asset drift, one independent browser case, and three production
  browser cases passed.
- Exact hosted GitHub Actions run `33655002746`, job `100331249147`, exercised
  commit `2fb89fc8c36d93b4435032c07783532d6a8aa933` on
  `macos-15-intel` from `2026-09-02T16:27:29Z` through
  `2026-09-02T16:44:30Z`. Pinned CPython 3.12.13, exact Node 22.14.0, both
  locked environments, Python/static/CLI, frontend/assets, Chromium, and
  production browser validation all concluded `success` on attempt one with
  no retry.

## Five ordered batch histories

The checkpoint commits/trees and manifest commits are:

1. B1 checkpoint `d4f984d26ca45dcd0f70da51ad739da427e23be4` / tree
   `7ea1fc48a28413011dca4dc6f07c5f0312b9f584`; manifest and distinct
   verification record commit `885be61a2bbea8bf5261b3983cbc79fedde0f315`,
   manifest SHA-256
   `3710e7fde7523096b70607b3a7da217b1e71fdb46492b83b72861e3eaa48cfae`.
2. B2 checkpoint `18614cc812edda68598e19d200f7bb4c87861ebd` / tree
   `d75d33f67725a7fe04ac8c4ac0d7e57efdf25ec4`; manifest and distinct
   verification record commit `0ece04929e36d356f084dba015c9a256cffec50a`,
   manifest SHA-256
   `2af5bfc21a5d888132fb4e468f543403e8948632ad9ab2dd11b8da854dd4a602`.
3. B3 checkpoint `233b3b0667add740cee96ce3c9ee266c8a639067` / tree
   `0d3709a861bf79f002246836a582b87677e29b15`; manifest and distinct
   verification record commit `6f26cc80435adfa787e5fbef1f69807c5686c864`,
   manifest SHA-256
   `4d17a6f0a1401799f1d7c0c65870744aada26eb2a3b1b8d5c723d447ceb4fac1`.
4. B4 checkpoint `9a8fc46ba4bc73cd007d678b85b6510bba0eeb87` / tree
   `62811eca22c8fd3de5403b5b6f853b187c938038`; manifest and distinct
   verification record commit `9178755f2d491c19f4c67a2e7f68f6f6ebb22672`,
   manifest SHA-256
   `699443c5ed9cb2ddd668b4b486311e251647cadf5aeb3a435263dd2597e0f72c`.
5. B5 checkpoint `d7e79e03cf9d1f461cc30f87a84fc5d21c2b62aa` / tree
   `40849b62bb543be07863743c2d6a8d615585abe4`; manifest and distinct
   verification record commit `5d5712477e41ee269f2828787c9fddc840c414b6`,
   manifest SHA-256
   `c67031fa0f9590e9cc44134e382f2c3bec70e0744c91a4f26be6a559699e1532`.

The active role identities are preserved in those manifests. B1 additionally
preserves six distinct internal fixture and runner roles plus every correction,
raw-baseline, threshold-review, accumulated-validation, acceptance, and
explicit operator-decision record. B2 preserves rejected incomplete and
blocking-write histories before accepted implementor
`c3-b2-private-host-implementor-replacement-6`, verifier
`c3-b2-private-host-verifier-replacement-4`, and acceptor
`c3-b2-private-host-acceptance-replacement-3`. B3 preserves separate UART,
SPI, I2C, cross-source, integration, verification, accumulated, and acceptance
records. B4 preserves final implementor `c3-b4-public-implementor-1`, verifier
`c3-b4-public-verifier-1`, accumulated validation, and acceptor
`c3-b4-public-acceptor-1`. B5 preserves failed measurement verification,
C3B5-V001 correction, fresh verifier `c3-b5-final-proof-verifier-2`, complete
accumulated validation, and pre-manifest acceptor `c3-b5-final-acceptor-1`.
Every failed or superseded record remains immutable and transfers no pass.

## Support, limitations, rollback, and prohibited actions

The supported Cycle 3 claim is macOS with Python 3.12. The characterized
performance claim is limited to the accepted Macmini8,1 x86_64 environment
class; exact hosted validation is limited to the governed `macos-15-intel`
runner. Decoder execution is one validated inert request in one fresh
single-use worker with finite deadline, bounded IPC/output/resources,
deterministic terminate/kill/reap cleanup, and post-failure recovery.

Known limitations are the explicit macOS-only support boundary, the
environment-class-bound regression ceilings, classified local loopback and
machine-local physical-artifact skips covered by accepted or hosted evidence,
and the legal confirmation required before conveyance. There is no deferred
Cycle 3 product work or deferred finding.

Rollback is the accepted pre-Cycle-3 Python candidate or operational use of the
preserved existing C# application and firmware. Rollback does not delete or
rewrite accepted evidence, user changes, firmware, C# sources, or decoder
snapshots.

Cycle 3 did not install or run C#/.NET, pythonnet, libsigrokdecode,
`sigrok-cli`, or an external/reference decoder runtime. It did not add browser
decoder behavior, hardware/firmware/serial/live-capture work, dynamic decoder
discovery, stacking, `.lac`, unsupported-platform support, package
construction, publication, conveyance, or Cycle 4 work.

## Handoff

All required evidence through the committed B5 checkpoint is immutable and
cleanly ordered. The exact checkpoint state remains `Complete; Cycle 3 closure
pending`; the only remainder stated by this proof is `closure pending`.
