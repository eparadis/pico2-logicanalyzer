# C2-B5 verification round 1

- Identity: `cycle2-verifier-replacement-3`, independent Verification lane.
- UTC: `2026-08-23T20:21:51Z`.
- Product candidate: `5e1a4cc87325e0c1f39df6b0f3c5757f900d1504`;
  tree `9c2b786680c4d30941f06fd9fc5eaf4d448bf484`.
- Implementation record reviewed as evidence only: `1d07caaab3e012529ba15b5db3f91747eef34c0f`.
- Verdict: `changes_required`.

## Findings and dispositions

1. `C2B5-V001` — open. The frozen performance method/evidence does not satisfy the B5
   reproducibility contract:
   - fixtures carrying `bus-representative` and `bus-worst` roles are imported only as waveform
     loads; the benchmark never requests, renders, paginates, or times a bus table;
   - the empty, maximum-24, and bus-representative cases have only one initial observation, so
     the required multiple-iteration median/high-percentile method is not applied to every
     approved case; and
   - the 30 raw pan/zoom timings are discarded. Only aggregate median/p95 values are durable,
     so an independent reviewer cannot recompute either statistic from the record.
   Independent verifier assertions for these three properties fail. No performance threshold
   is evaluated or proposed by this finding.

## Independent product and corpus evidence

- Inert ZIP/NPY inspection independently verified every non-empty fixture member set, SHA-256,
  payload size, sample count, exact unsigned dtype for 8/16/24-bit widths, ordered D0-D23 IDs,
  and default labels. Required empty/constant/sparse/dense/maximum-width/schema-1 and both bus
  roles are present. Fixture manifest SHA-256 is
  `9e2372ac1861b2b47bdaaf5cedab9a9b1faf671e459f640753ccf1124408e496`;
  checked-in baseline SHA-256 is
  `1a692cfe7a3b0cec0c4b30b9f8e496d67a8ca50ec1b418f25ffda6deba4a5888`.
- Fresh verifier baseline tests: 1 passed and 3 failed, exactly corresponding to `C2B5-V001`.
- Fresh independent DPR-2 production-browser test passed: maximum-24 showed 24 ordered channel
  values; Canvas backing dimensions matched DPR; DOM stayed below 1,000; waveform requests
  remained at most 100,000 samples and 960 pixels; the capability was absent from URL, DOM,
  storage, referrer, console messages, and recorded request URLs.
- Source and accumulated black-box audit covered schema-1/schema-2/CSV imports; all widths;
  labels/visibility; fixed pan and cursor-centered zoom; trigger/cursor sample, relative time,
  and values; transition-reduced Canvas bounds; transition/distinct-strobe ordering,
  pagination, deterministic safe export; loading/ready/empty/error/disconnected/cancelling/
  shutdown; failure, reconnect, abort, cleanup; and production runtime without Node, CDN,
  serial opening, development server, server paths, or durable residue. No separate product
  defect was found outside the baseline-method finding.

## Commands and results

- Clean accumulated non-hardware Python, excluding the intentionally failing verifier file:
  346 passed, 2 sandbox-loopback skips, 44 warnings.
- Ruff passed; mypy passed for 21 source files; dependency, OpenAPI, production-asset, CLI-help,
  and diff checks passed.
- Node 22 lint/typecheck passed; Vitest 3 files and 5 tests passed; production build transformed
  29 modules and reproduced committed assets.
- Root-brokered real-loopback API: 1 passed. Production workflow Playwright: 2 passed.
  Verifier DPR-2 Playwright: 1 passed in 619 ms test time / 1.8 s total.
- Fresh frozen benchmark reproduction: 1 passed in 23.5 s test time / 24.4 s total. The locally
  generated report had SHA-256
  `2d2bc3f2166a9dcd34db14a1e28f2899092e8218aa33c426fab293ddcbb220f7` and was removed with
  other generated residue after inspection. Reproduction confirms execution, but cannot cure
  the missing bus observations, per-case repetitions, or discarded raw interaction samples.

## Scope and authority

The candidate changes B5 frontend, tests, fixtures, baseline, and production assets only; the
accepted B2/B4 production boundary is unchanged. No hardware/serial, firmware, C#/.NET,
persistent service, public server, packaging, B6, acceptance, threshold proposal/approval, or
Cycle 3 action occurred. Product, prior evidence, governing contracts, manifests, and progress
were not modified.

Open findings: `C2B5-V001`. Deferred findings: none.
