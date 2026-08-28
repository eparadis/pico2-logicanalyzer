# C3-B1 semantic-fixture correction acceptance — round 2

## Identity and immutable subject

- Acceptance identity: `c3-b1-semantic-fixture-correction-acceptance-2`
  (`/root/c3_b1_i2c_fixture_accept_r1`), independent of the fixture
  implementor, verifier, primary orchestrator, B2 implementor, and every
  downstream evidence owner.
- Governing contract commit/tree:
  `ea83a403bb6f644d33069d3bebd41d5f1e0a60c0` /
  `d9fb09345ab85580cd8c877745262d1b481e366f`.
- Exact candidate commit/tree:
  `3af6b9f80dd52611e14acca407707d1da7b8d9ac` /
  `14c010153ea5542617e601e4126047c561a48483`.
- Candidate owner: `c3-b1-semantic-fixture-implementor-replacement-8`.
- Independent verifier: `c3-b1-semantic-fixture-correction-verifier-2`;
  `pass`; descendant commit
  `3a29e4684af6a4c8e53aa4f83f9692ddebab5670`; verifier-test SHA-256
  `9f750b51294b2078e82373adbbdd81ac287de669603f82bf59e65cc8e001a10a`;
  review SHA-256
  `e3402ea64e9dde2417c0aefbfd257e6a44db13947dae774ed33bcb6866645f23`.
- Root accumulated gate: `pass`; descendant commit
  `efcc7759f4af89eb438b2b8611e250d0962fc8c6`; record SHA-256
  `a3b8efddf3f6423e6a4cdde048a178a627ab7f9175c93a3084141f1940c6fc6e`.
- Finding: `C3B2-IF002`.

The candidate, verifier, and accumulated commits resolve and are ancestors in
that exact order. This acceptance inspected and tested only the immutable
fixture/evidence chain. The three preserved untracked B2-owned paths were not
read, run, changed, or used as an oracle. Candidate bytes were not repaired.

## Findings and dispositions

1. **Pass — exact scope and role separation.** The candidate changes exactly
   five paths: the new implementation record, generator, generated semantic
   corpus, generated fixture manifest, and focused implementation test. The
   verifier descendant adds only its test and review plus the root-owned
   progress update; the accumulated descendant adds only its review. All
   implementor, verifier, acceptance, orchestrator, and B2 identities remain
   distinct. No prior fixture, runner, raw, threshold, final-B1, manifest,
   checkpoint, or B2 verdict transfers.

2. **Pass — frozen I2C semantics close `C3B2-IF002`.** Static inspection of
   `Software/decoders/i2c/pd.py` confirms that the collected address byte `d`
   is shifted right only when `address_format == "shifted"`, after which the
   same `d` is emitted to Python and binary outputs and formatted for the
   address annotation. Consequently wire byte `0xA0` is `0x50` for shifted
   output and `0xA0` for unshifted output. The corrected unshifted Python,
   binary, and annotation values are respectively `160`, byte `0xA0`
   (`oA==`), and `A0`; the shifted case remains `0x50` (`UA==`).

3. **Pass — exact single-record semantic change.** Independent structural
   comparison against the candidate parent found 63 timelines before and
   after. Only timeline `i2c-unshifted-repeated-start` differs, and within it
   only `expected_records[4].value.data_base64` changes from `UA==` to `oA==`.
   Its emission index, coordinates, times, class, output ID, Python value, and
   annotation are unchanged. All other records and timelines, including every
   shifted case, are identical; all top-level edge decisions, optional-pin
   cases, oracle declaration, and schema are identical.

4. **Pass — internal consistency and generic generation.** The generator's
   `i2c_byte()` derives one emitted address value from the raw byte, address
   role, and explicit format and uses it for Python, binary, and annotation
   records. There is no fixture-ID exception or B2/product/runtime oracle.
   Focused assertions independently decode and compare all three output kinds
   for shifted and unshifted witnesses, and the verifier includes mutations
   for the old binary byte, changed non-target timelines, cross-kind drift,
   option inversion, and fixture-specific generation.

5. **Pass — artifact and manifest closure.** Recomputed SHA-256 values are:
   generator
   `a101ae13cba938aa4d574fd1df3e4cc09dc845b2a643088cfee4a79313c3266f`,
   semantic corpus
   `34d2a114b653dc1a5d2fc9f253457e11e6b1acd4bc10d38ffa98d84bdd93d094`,
   fixture manifest
   `71c64b2c80142cf5d535e03f93f9d3ce66ada120582115fbf403f3621f97c5b9`,
   provenance
   `e0a6082869cdf51e7abf74441065b080b8e1d6614a45ad52f034ef95f4f4c8e4`,
   option matrix
   `5d84b9d9855e9e2e75d45d5cd9560fbcfd1ac6ff88abfcf1c1326d3427ffc209`,
   typed vectors
   `b5cc317ff476fcb2446eaf6b376c346210f63fbca8d0df84984b7990a528ffbf`,
   and experiment caps
   `6347a04f44f02179e73fd9178fce4daad227d06c9a7a4ac2c12e0b0669f60d3d`.
   The manifest's generator and artifact bindings recompute, while provenance,
   option matrix, typed vectors, and caps retain their prior identities.

6. **Pass — fresh verification is strong and reproducible.** The fresh
   verifier suite passed `6 passed in 0.28s`; the focused implementation suite
   passed `12 passed in 0.49s`; deterministic generator `--check` passed; and
   scoped Ruff passed with `All checks passed!`. Candidate-range
   `git diff --check` also passed. These runs used repository-local Python and
   did not execute a decoder, B2 host/test, raw characterization, C#/.NET,
   pythonnet, libsigrokdecode, sigrok-cli, external/reference runtime,
   hardware, network, dependency installation, or publication operation.

7. **Pass — accumulated evidence is complete and honestly classified.** The
   root accumulated record ran from a clean exact-descendant clone, bound
   Python imports to that clone, and reports complete Python, Cycle 2, frozen
   web, browser, performance, digest, process, and scope gates. Its unfiltered
   result is transparently recorded as 623 passed, 124 failed, and 6 skipped;
   all 124 failures are classified as exact-candidate fail-closed reactions in
   invalidated downstream modules. The candidate-applicable partition passed
   404 tests with six documented inherited skips. A final process audit found
   no surviving clone server, browser, worker, decoder, characterization, C#,
   .NET, or sigrok process. The exclusions are dependency-order invalidations,
   not waivers or transferred passes.

8. **Pass — authority remains bounded.** `C3B2-IF002` is closed only for this
   exact semantic-fixture candidate. This pass authorizes only downstream
   runner rebinding. Runner verification/acceptance, raw characterization and
   its gates, threshold proposal and explicit operator approval, final-B1
   binding and gates, replacement manifest verification, and a replacement B1
   checkpoint must occur in governing order. This pass does not authorize B2
   resumption, product changes, B3+, or Cycle 4.

Open candidate findings: none. Approval needed: none.

## Verdict

pass
