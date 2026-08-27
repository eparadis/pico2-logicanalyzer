# C3-B1 threshold-proposal acceptance — round 2

## Identity, subject, and authority

- Acceptance identity: `c3-b1-pre-execution-runner-acceptance-1`
  (`/root/c3_b1_runner_accept`), reused only in its independent acceptance
  role and distinct from proposal authorship and verification.
- Immutable corrected proposal commit/tree:
  `395646fa1172382928581d7266723f5b044cf8f2` /
  `6857f9a67ff70220e6d6b2a11f9ca450005c8321`.
- Fresh verification pass commit:
  `1cdedcae57e6233010410172196b23f6167ee675`.
- Fresh accumulated-validation pass commit:
  `0d00fe4b88a1192b893afbf8e32c39bd6493b2fd`.
- Acceptance assignment commit/tree:
  `1ce64c4cd86772e5763e72a8a1292daf41d8419f` /
  `7e1d81942a0d9684aa84bc46d97340edf2ff3002`.

This is a fresh proposal acceptance audit. No round-1 verdict, finding
disposition, or approval transfers. I repaired no proposal, rationale, test,
evidence, product, progress, contract, or environment input and created only
this record. This record makes no operator decision.

## Findings and dispositions

1. Candidate identity, scope, and status: no discrepancy. Candidate
   `395646f...` adds exactly the assigned round-2 machine-readable proposal and
   rationale. Both remain byte-identical to that commit. Status is exactly
   `proposal-not-approved`; neither artifact claims approval, enforcement,
   product authority, a manifest, or a checkpoint.
2. C3B1-TPV001 correction: exact and complete. The accepted raw maximum is
   `105,815,301 ns`; multiplying by eight gives `846,522,408 ns`; ceiling to a
   `100,000,000 ns` quantum gives exactly `900,000,000 ns`. Inclusive accept is
   `900,000,000`, exclusive first reject is `900,000,001`, and the rationale's
   approximately `8.51 times` statement is accurate. After normalizing the
   permitted round/provenance metadata and reversing only that value, boundary,
   and rationale correction, no other round-1 numeric meaning differs.
3. Complete 29-limit closure: no discrepancy. Static parsing confirms exactly
   29 unique closed IDs, positive integers, required units and kinds, and for
   every entry `accept == value` and `reject == value + 1`. All raw maxima,
   formulae, experiment-cap identities, hard-cap relationships, and evidence
   digests recompute. Every hard ceiling is equal to or stricter than its
   experiment cap. Cross-limit feasibility passes for samples/request framing,
   output retention/RSS/address space, successful deadline, deadline/grace/
   cleanup, termination/reap, and maximum SPI word size eight.
4. Evidence and provenance closure: no discrepancy. The proposal names the
   accepted fixture, corrected runner, immutable raw candidate, raw verifier,
   accumulated pass, raw acceptance, original proposal assignment, failed
   round-1 proposal, failed-verification assignment and commit, and correction
   assignment in order. Its five raw-file digests and experiment-cap digest
   match immutable evidence and retain the characterized macOS 15.7.7 build
   24G720, x86_64, Python 3.12.13 qualification. Raw timing/RSS discrepancies
   remain explicit and are not converted into approval or hidden by averaging.
5. Fresh independent verification: valid and complete. The verifier transferred
   no pass, independently recomputed all 29 values and exact 900-ms arithmetic,
   checked correction scope/provenance and feasibility, and applied a non-
   vacuous negative mutation matrix covering missing/extra/duplicate IDs,
   invalid types/values, changed maxima/formulae, weakened caps, inconsistent
   units/bounds, timing-policy contradictions, SPI nine, approved status, and
   evidence substitutions. Its immutable 22-test result is `pass`; my static
   rerun also produced 22 passes in 0.36 seconds.
6. Fresh accumulated evidence: complete for the proposal gate. Repository-local
   Python 3.12 passed `pip check`, whole-project Ruff, both strict mypy scopes,
   deterministic fixture/binding checks, 637 applicable non-hardware tests,
   all six Cycle 2 validators, and the fresh proposal verifier. Exact local
   Node 22 passed lint, type, five unit tests, 29-module build/assets, four
   browser tests, and offline performance plus the unchanged accepted-threshold
   checker. No applicable mandatory check failed or remained skipped.
7. Historical applicability classification: explicit and justified, not a
   waiver. The three excluded historical nodes are: (a) the pre-proposal
   fixture namespace assertion, superseded for current applicability by the
   governing proposal paths and passing deterministic fixture checks; (b) the
   raw-evidence test's immutable former `/private/tmp` executable identity,
   while raw evidence remains unchanged and current repository-local tooling
   is intentionally distinct; and (c) the failed round-1 exact-formula identity
   assertion, whose immutable failure is preserved while all 22 fresh round-2
   tests pass. No historical test or evidence byte was edited.
8. Local tooling and authorization: correctly bounded. Python and copied exact
   Node 22 tooling reside only under ignored repository `.venv`; no package was
   installed and no network dependency action occurred. One reusable loopback
   npm-script authorization class replaced per-process requests. The first
   system-Node performance artifact was rejected by its metadata checker and
   replaced with a passing exact Node 22 run; it supplies no accepted result.
9. Ordering, safety, and next authority: no discrepancy. The corrected proposal
   follows the failed round-1 evidence and correction assignment; fresh
   verification follows candidate creation; accumulated validation follows the
   verifier pass; this acceptance follows both. A pass authorizes only
   presentation of these exact committed values for explicit operator approval
   or amendment. It does not approve any value or authorize B2/product work.

No finding is open.

## Static checks and immutable hashes

- Commit/tree/parent and two-path candidate-scope inspection: passed.
- Candidate quiet diff against `395646f...`: passed.
- Static JSON audit: status `proposal-not-approved`; 29 unique positive-integer
  entries; all inclusive/exclusive boundaries exact.
- Static round-2 verifier:
  `rtk .venv/bin/python -m pytest -q
  tests/verification/test_c3_b1_threshold_proposal_round2.py` — 22 passed.
- Final targeted process query returned only its transient query PID, which had
  exited when inspected; no runner, worker, decoder, pytest, Playwright, or Vite
  process remained.

SHA-256 values independently recomputed from the assignment descendant:

- proposal: `94882b710f2d569c0ea0535366a0c1c3df3514aa20a18e4cd35f652177458ec2`;
- rationale: `18a6b58a2b05f7dd7aa302a6e1bb4d074621440648a2e735a1d16d9708b209b0`;
- verifier test: `f146f0d58a65116825f6ee6b2e04e4fcf495fca89de9565bf70e26b662509c79`;
- verifier record: `c160cc75238ab48479fb3cfe4d0c4d0c86ee052102a4fd2715050b285d4e50a0`;
- accumulated record: `b3a1455aefb3044d1048d6e2253885ba9908a09e7bc5e24c287bb63b21723b4b`.

## Safety and authority statement

Only static JSON, Markdown, Git, and static verifier-test inspection occurred.
No snapshot, decoder, hostile probe, runner, product host, hardware, network,
install, external runtime, browser server, publication, excluded action, or
Cycle 4 work ran. No operator decision was made. No worker remains.

## Verdict

`pass`
