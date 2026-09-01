# C3-B4 public library and installed CLI implementation, round 1

- Identity and role: `c3-b4-public-implementor-1`; bounded B4 product implementor
- Timestamp: `2026-09-01T09:44:36Z`
- Governing commit/tree: `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`
- Accepted B3 checkpoint: `233b3b0667add740cee96ce3c9ee266c8a639067`
- Starting orchestration commit/tree: `712c9d5022502d086b7530b2f6703ca19faadb42` /
  `b50df740f7f1d55a09bbc5aec2f3bab15a433eb4`
- B1 internal candidate/ownership: not applicable; this identity authored no B1
  expected output, fixture, threshold, method, runner, or probe surface.

## Delivered bounded behavior

The worktree implements R17-R20's product portion:

- frozen public result, declaration, record, rational-time, and tagged-value
  models plus the synchronous
  `pico_logic_analyzer.decode.decode_capture(capture, decoder_id, channels,
  options, limits=None)` entry point;
- one delegation to the accepted private B2 host, declaration-order channel
  canonicalization, pre-launch request validation, and a closed numeric caller-
  limit mapping that cannot exceed any approved ceiling or disable isolation,
  digest/import verification, validation, cancellation/reaping, or the decoder
  allowlist;
- parent enforcement of tightened deadline, request/result/pipe/retention,
  output, nesting, recursion, and address-space selections, while retaining the
  accepted hard ceilings;
- the exact installed offline `pico-la decode` replay/CSV surface, typed mapping
  and option assignments, explicit CSV metadata ordering, legacy-only D0-D7
  rate inference, canonical compact sorted-key version-1 JSON plus LF, stderr-
  only errors, and decoder exit 7;
- lazy preservation of existing CLI serial seams so offline decode imports no
  serial or web dependency and opens no live capture path;
- exact-byte private package-resource placement for the accepted nine-file
  snapshot, closed file-set verification, preserved logical file-set digests,
  public typing marker, documentation, attribution, license texts, PEP 639
  metadata, and the existing hosted-macOS workflow additions; and
- focused external-working-directory, exact B1 object/byte-vector, replay/CSV,
  metadata, error, limit, no-serial/no-web, package/resource, and strict-mypy
  consumer tests.

No decoder snapshot, fixture, option matrix, threshold, semantic result,
browser/frontend/API path, hardware/firmware path, live capture, serial path,
publication path, unsupported-platform claim, B5 artifact, or Cycle 4 artifact
was edited or added.

## Changed paths

- Public product: `src/pico_logic_analyzer/decode/__init__.py`, `py.typed`.
- Minimum private-host/resource integration: `_decode/{host,identity,loader,worker}.py`
  and the exact private `_decoder_snapshots/407b5ef.../` nine-file tree.
- Installed CLI: `src/pico_logic_analyzer/cli/main.py`.
- Package/dependency inputs: `pyproject.toml`, `requirements-dev.in`,
  `requirements-web.in`, and independently generated `requirements-dev.lock`
  and `requirements-web.lock` outputs.
- Licensing/docs: `LICENSE`, `LICENSES/{GPL-2.0-or-later,MIT}.txt`,
  `ATTRIBUTION.md`, `README.md`, `docs/cycle-3-decoding.md`.
- Focused checks: `tests/implementation/test_c3_b4_public.py` and
  `tests/implementation/c3_b4_consumer.py`.
- Hosted proof workflow: `.github/workflows/logic-analyzer-python-cycle2.yml`.
- This implementation handoff only; no progress/evidence/checkpoint artifact.

## Authoritative provenance and notable digests

- Public module: `dafe3d4db7289adf57c299f4e8a2ade480addf3f7a624551ddc9779845eeba8c`.
- Focused test / strict consumer:
  `f4fd07645d289b1ec522b93e8ef71a55ca83cf896eff544fcf17d2fe59a83ea4` /
  `d7fb75b80348ef447a1a2aa30848808f2856351df5f491c0f417d128a68145a0`.
- Attribution / package GPLv3 / GPLv2 / MIT:
  `3765302c5ba6602633a44b934da41cb94aba3d25455d91582f3c29bf1c0cac1e` /
  `3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986` /
  `ab15fd526bd8dd18a9e77ebc139656bf4d33e97fc7238cd11bf60e2b9b8666c6` /
  `6115c1f056dc347dd180c44bd5fb862cf1e3d48a34fecd0b6e5a0e4193b752f6`.
- Public decoding documentation: `52c068632bbae7c94d9921c56c2d526610af2bcddf6abe355746ec3e1d1e1cab`.
- Current PEP 639 package metadata / workflow:
  `ead05ffbfab1c046b43087993d7dbd1056cdc9d6ebbb87d481092bacfb30a6cf` /
  `4d6427e39e822326ab81ac1015728fd9bc2b279270c1b0fb22f458528a7a6319`.
- Generated dev/web locks:
  `4efa0b1d42e5162c7a20177d1dd5e78083d75a87d2405709e04b1bcbd4f33c53` /
  `4b0feeadf92c0bcb9f2790cc62f6b6e2f7da8937f30ff50d0c9092fd003b8145`.
- Every packaged snapshot byte matches its accepted source SHA-256; public
  file-set digests remain UART `eb9ee54a...d3f3`, SPI `96bbaf9f...c193`, and
  I2C `dd85b78a...16ae` because the digest manifest retains the accepted logical
  source paths.

## Commands and exact results

- Focused missing-behavior check before production edits:
  `.venv/bin/python -m pytest -q tests/implementation/test_c3_b4_public.py`:
  `3 failed`, proving absent public module and package resources.
- Latest combined B4/private-host/CLI/workflow focused run:
  `.venv/bin/python -m pytest -q tests/implementation/test_c3_b4_public.py
  tests/unit/test_cli.py tests/implementation/test_cycle2_workflow.py
  tests/implementation/test_c3_b2_private_host.py`: `254 passed in 54.08s` on
  the final regenerated-lock worktree.
- All eight accepted B3 implementation/verification conformance modules:
  `421 passed in 59.08s`.
- `.venv/bin/python -m ruff check .`: pass.
- `.venv/bin/python -m mypy src`: `Success: no issues found in 31 source files`.
- `.venv/bin/python -m mypy --strict
  tests/implementation/c3_b4_consumer.py`: `Success: no issues found in 1
  source file`.
- `git diff --check`: pass.
- Generated lock review: the dev lock changed only its truthful command header
  and the exact setuptools `75.8.0` to `77.0.3` artifact hashes; the
  independently generated web lock retains all exact runtime/build inputs and
  removes only dev tools and their transitive-only dependencies.
- Root completed one hash-verified wheelhouse download and offline locked
  installs in stable Python 3.12.13 environments `/private/tmp/cycle3-clean-core`
  and `/private/tmp/cycle3-clean-web`. The exact install shapes were
  `pip install --require-hashes -r requirements-{dev,web}.lock`, followed by
  `pip install --no-build-isolation --no-deps -e .` for core and
  `pip install --no-build-isolation --no-deps -e '.[web]'` for web; all four
  passed under setuptools `77.0.3`.
- Independent `/private/tmp` inspection with each environment's
  `python -m pip check`: `No broken requirements found.`
- Independent installed metadata in both environments: distribution `0.1.0`,
  setuptools `77.0.3`, `License-Expression: GPL-3.0-only`, the exact four
  `License-File` entries, runtime requirements `numpy==2.2.2` and
  `pyserial==3.5`, and optional-only
  `aiohttp==3.11.12; extra == "web"`. The four installed license/attribution
  bytes reproduced the authoritative hashes above exactly. The web environment
  imported aiohttp `3.11.12`; the package metadata keeps it out of the base
  dependency set.
- Independent resource inspection in both environments found the empty
  `py.typed` marker and exactly the accepted nine decoder files, with no extra
  file. `verify_decoder()` reproduced UART `eb9ee54a...d3f3`, SPI
  `96bbaf9f...c193`, and I2C `dd85b78a...16ae`.
- From outside the source tree, both installed `pico-la decode --help` commands
  passed with the exact grammar. The web environment performed a real UART
  public `decode_capture` and emitted schema
  `pico-logic-analyzer.decode-result/v1`; aiohttp remained independent of the
  decode path. The core clean environment ran the complete focused public
  implementation module from `/private/tmp`: `14 passed in 3.10s`, including
  exact external replay/CSV CLI bytes and external public-library execution.
- The first no-build-isolation editable reinstall correctly failed under the
  then-frozen `setuptools==75.8.0`: that backend predates PEP 639 and rejected
  B1's required SPDX string metadata. Root independently confirmed PEP 639
  support begins at setuptools 77 and selected the smallest reviewed non-yanked
  patch, `77.0.3`. Inputs and build-system now pin that exact version; the
  generated hash locks, offline locked installs, and editable reinstalls now
  pass.

Environment: macOS x86_64, Python 3.12.13. Existing focused and stable clean
core/web environments were used as identified above. No required focused test
skipped. Immutable-candidate installed-set digest and hosted CI remain
orchestrator gates after candidate integration.

## Findings, risks, and dispositions

1. `C3B4-I001` — accepted PEP 639 metadata was incompatible with setuptools
   75.8.0. Disposition: product inputs and independently generated hash locks
   now pin reviewed `77.0.3`; root-brokered locked installs and independent
   installed metadata/resource inspection pass.
2. `C3B4-I002` — repository-root snapshot lookup could not work after install.
   Disposition: exact bytes now live only in B1's mandated private commit-rooted
   package-data layout; the loader and verifier use that closed root and reject
   extras/symlinks/digest mismatch while retaining accepted logical identities.
3. `C3B4-I003` — eager CLI driver import would import pyserial for offline
   decode and broke R19. Disposition: existing patch seams are retained behind
   lazy wrappers; external guarded-import decode succeeds with both `serial`
   and `aiohttp` forbidden.

The B1 rights-holder/counsel limitation remains explicit: the shim lacks an
in-file notice and Cycle 3 authorizes neither conveyance nor publication. No
wheel, sdist, upload, or publication occurred.

## Prohibited-runtime/action audit and worktree

Static imports/dependencies and exercised paths add no C#/.NET, pythonnet,
libsigrokdecode, `sigrok-cli`, external/reference runtime, decoder discovery,
plugin, stacking, serial/live capture, web/browser decode, hardware, firmware,
publication, non-macOS claim, B5, or Cycle 4 use. The checked-in snapshots were
executed only through the already accepted B2 host and were never used as an
oracle for B1 expected values.

Ending worktree is intentionally unstaged and consists only of the enumerated
B4 paths above plus this record, including both reviewed generated lock
changes; there are no unrelated user changes observed.

## Verdict and approval routing

Verdict: `candidate-not-accepted`. The bounded product implementation and lock
closure, stable clean installs, installed metadata/resources, external public
API/CLI behavior, and proportional focused checks are green. No legal
confirmation or build/publication boundary is simulated. This is a worktree
candidate, not an immutable, independently verified, accepted, or checkpointed
candidate. `APPROVAL_NEEDED`: none for this bounded implementation handoff.
