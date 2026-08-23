import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { arch, platform, release } from "node:os";
import { performance as nodePerformance } from "node:perf_hooks";
import { expect, test, type Page } from "@playwright/test";

type Fixture = { name: string; roles: string[]; artifact: string | null; sha256: string | null; sample_count: number; payload_bytes?: number; width?: number };
type Load = { name: string; milliseconds: number; commands: number; transitions: number; dom_nodes: number };
type BusSample = { fixture: string; roles: string[]; mode: "transition" | "sampled"; milliseconds: number; rows: number; payload_bytes: number };
const manifest = JSON.parse(readFileSync("benchmarks/fixtures.json", "utf8")) as { fixtures: Fixture[] };
const nearestRank = (values: number[], fraction: number): number => [...values].sort((a, b) => a - b)[Math.max(0, Math.ceil(values.length * fraction) - 1)];
const nextPaint = (page: Page): Promise<unknown> => page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));

test("frozen production rendering baseline", async ({ page, browser }) => {
  test.setTimeout(300_000);
  const loads: Load[] = []; const busSamples: BusSample[] = [];
  for (let iteration = 0; iteration < 2; iteration += 1) {
    const started = nodePerformance.now(); await page.goto("/");
    await expect(page.locator("p[role=status]")).toHaveText("empty"); await nextPaint(page);
    loads.push({ name: "empty", milliseconds: nodePerformance.now() - started, commands: 0, transitions: 0, dom_nodes: await page.locator("*").count() });
  }

  const requiredNames = ["constant-8", "sparse-16", "dense-24", "maximum-16", "bus-representative-8", "maximum-24", "maximum-8"];
  const required = requiredNames.map((name) => manifest.fixtures.find((fixture) => fixture.name === name)!);
  const sequence = [...required, ...required];

  const measureBus = async (fixture: Fixture, mode: "transition" | "sampled"): Promise<void> => {
    await page.getByLabel("Bus mode").selectOption(mode);
    if (mode === "sampled") {
      await page.getByLabel("Strobe channel").selectOption(fixture.name === "bus-representative-8" ? "7" : "0");
      await page.getByLabel("Bus edge").selectOption("rising");
    }
    const started = await page.evaluate(() => performance.now());
    await page.getByRole("button", { name: "Analyze bus" }).click();
    await expect(page.getByRole("table")).toBeVisible(); await nextPaint(page);
    const milliseconds = (await page.evaluate(() => performance.now())) - started;
    const rows = await page.getByRole("table").locator("tbody tr").count();
    expect(rows).toBeGreaterThan(0); expect(rows).toBeLessThanOrEqual(100);
    busSamples.push({ fixture: fixture.name, roles: fixture.roles.filter((role) => role.startsWith("bus-")), mode, milliseconds, rows, payload_bytes: fixture.payload_bytes! });
  };

  for (const fixture of sequence) {
    const started = await page.evaluate(() => performance.now());
    await page.getByLabel("Import capture").setInputFiles(`benchmarks/${fixture.artifact!}`);
    await page.getByRole("button", { name: "Open", exact: true }).click();
    await expect(page.locator("p[role=status]")).toHaveText("ready");
    const canvas = page.getByLabel("Digital waveform"); await expect(canvas).toHaveAttribute("data-rendered-window", /\d+:\d+/); await nextPaint(page);
    const ended = await page.evaluate(() => performance.now());
    loads.push({ name: fixture.name, milliseconds: ended - started, commands: Number(await canvas.getAttribute("data-commands")), transitions: Number(await canvas.getAttribute("data-transition-count")), dom_nodes: await page.locator("*").count() });
    if (fixture.roles.some((role) => role === "bus-representative" || role === "bus-worst")) {
      await measureBus(fixture, "transition"); await measureBus(fixture, "sampled");
    }
    await page.waitForTimeout(300);
  }

  const waveform = page.getByRole("region", { name: "waveform" }); const canvas = page.getByLabel("Digital waveform");
  const interact = async (iteration: number): Promise<void> => {
    const previous = await canvas.getAttribute("data-rendered-window");
    await waveform.press(iteration % 2 ? "ArrowLeft" : "ArrowRight"); await waveform.press(iteration % 2 ? "+" : "-");
    await page.waitForFunction((prior) => document.querySelector<HTMLCanvasElement>('canvas[aria-label="Digital waveform"]')?.dataset.renderedWindow !== prior, previous); await nextPaint(page);
  };
  for (let warmup = 0; warmup < 3; warmup += 1) await interact(warmup);
  const interactions: number[] = [];
  for (let iteration = 0; iteration < 30; iteration += 1) {
    const started = await page.evaluate(() => performance.now()); await interact(iteration);
    interactions.push((await page.evaluate(() => performance.now())) - started); await page.waitForTimeout(50);
  }

  const heap = await page.evaluate(async () => {
    const precise = performance as Performance & { measureUserAgentSpecificMemory?: () => Promise<{ bytes: number }> };
    if (!precise.measureUserAgentSpecificMemory) return null;
    try { const measurement = await precise.measureUserAgentSpecificMemory(); return Number.isFinite(measurement.bytes) ? measurement.bytes : null; } catch { return null; }
  });
  const loadStatistics = requiredNames.concat("empty").map((name) => {
    const raw = loads.filter((item) => item.name === name).map((item) => item.milliseconds);
    return { name, iterations: raw.length, initial_ready_paint_ms: raw, median_ms: nearestRank(raw, 0.5), p95_ms: nearestRank(raw, 0.95) };
  });
  const busObservations = ["bus-representative-8", "dense-24"].flatMap((fixture) => ["transition", "sampled"].map((mode) => {
    const matching = busSamples.filter((item) => item.fixture === fixture && item.mode === mode);
    const raw = matching.map((item) => item.milliseconds);
    return { fixture, roles: matching[0].roles, mode: mode === "sampled" ? "distinct-strobe" : mode, iterations: raw.length, timings_ms: raw, median_ms: nearestRank(raw, 0.5), p95_ms: nearestRank(raw, 0.95), rows: Math.max(...matching.map((item) => item.rows)), row_counts: matching.map((item) => item.rows), payload_bytes: matching[0].payload_bytes };
  }));
  const assetManifest = readFileSync("production-assets.json");
  const report = {
    schema_version: 2, method: "c2-b5-playwright-production-v2", threshold: null,
    viewport: { width: 1280, height: 900, device_pixel_ratio: 1 }, warmup_iterations: 3,
    load_iterations_per_case: 2, load_iterations: loads.length, interaction_iterations: interactions.length, bus_iterations_per_mode_and_role: 2,
    statistics: { method: "nearest-rank", index_formula: "max(0, ceil(p * n) - 1) on ascending raw samples", median_p: 0.5, high_percentile: "p95", high_percentile_p: 0.95, rounding: "none; JSON retains the raw IEEE-754 millisecond values returned by the timing clocks" },
    timing: "performance.now around UI action through API completion, rendered Canvas/table DOM, and next animation frame; Node performance.now brackets empty navigation/load/paint",
    browser: browser.version(), automation: "Playwright 1.50.1", node: process.version,
    host: { platform: platform(), release: release(), architecture: arch() },
    fixture_manifest_sha256: createHash("sha256").update(readFileSync("benchmarks/fixtures.json")).digest("hex"),
    fixture_generator_sha256: createHash("sha256").update(readFileSync("benchmarks/generate_fixtures.py")).digest("hex"),
    benchmark_script_sha256: createHash("sha256").update(readFileSync("tests/performance.spec.ts")).digest("hex"),
    production_asset_manifest_sha256: createHash("sha256").update(assetManifest).digest("hex"),
    fixtures: manifest.fixtures, loads, load_statistics: loadStatistics,
    load_median_ms: nearestRank(loads.map((item) => item.milliseconds), 0.5), load_p95_ms: nearestRank(loads.map((item) => item.milliseconds), 0.95),
    interactions_ms: interactions, interaction_median_ms: nearestRank(interactions, 0.5), interaction_p95_ms: nearestRank(interactions, 0.95),
    bus_observations: busObservations, used_js_heap_bytes: heap, memory_reliable: heap !== null,
  };
  writeFileSync("test-results/c2-b5-performance.json", JSON.stringify(report, null, 2) + "\n");
  expect(loads).toHaveLength(16); expect(loadStatistics.every((item) => item.iterations === 2)).toBe(true);
  expect(interactions).toHaveLength(30); expect(busObservations.every((item) => item.iterations === 2)).toBe(true);
  expect(Math.max(...loads.map((item) => item.commands))).toBeLessThanOrEqual(24 * (960 * 2 + 2) + 1);
  expect(Math.max(...loads.map((item) => item.dom_nodes))).toBeLessThan(1000);
});
