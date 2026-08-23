import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { arch, platform, release } from "node:os";
import { expect, test } from "@playwright/test";

type Fixture = { name: string; roles: string[]; artifact: string | null; sha256: string | null; sample_count: number; payload_bytes?: number; width?: number };
const manifest = JSON.parse(readFileSync("benchmarks/fixtures.json", "utf8")) as { fixtures: Fixture[] };
const percentile = (values: number[], fraction: number): number => [...values].sort((a, b) => a - b)[Math.min(values.length - 1, Math.ceil(values.length * fraction) - 1)];

test("frozen production rendering baseline", async ({ page, browser }) => {
  test.setTimeout(120_000);
  await page.goto("/");
  const emptyMilliseconds = await page.evaluate(() => new Promise<number>((resolve) => requestAnimationFrame(() => resolve(performance.now()))));
  const files = manifest.fixtures.filter((fixture) => fixture.artifact !== null);
  const sequence = [...files, ...files.slice(0, 6)];
  const loads: Array<{ name: string; milliseconds: number; commands: number; transitions: number; dom_nodes: number }> = [
    { name: "empty", milliseconds: emptyMilliseconds, commands: 0, transitions: 0, dom_nodes: await page.locator("*").count() },
  ];
  for (const fixture of sequence) {
    const started = await page.evaluate(() => performance.now());
    await page.getByLabel("Import capture").setInputFiles(`benchmarks/${fixture.artifact!}`);
    await page.getByRole("button", { name: "Open", exact: true }).click();
    await expect(page.locator("p[role=status]")).toHaveText("ready");
    const canvas = page.getByLabel("Digital waveform"); await expect(canvas).toHaveAttribute("data-rendered-window", /\d+:\d+/);
    await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
    const ended = await page.evaluate(() => performance.now());
    loads.push({ name: fixture.name, milliseconds: ended - started, commands: Number(await canvas.getAttribute("data-commands")), transitions: Number(await canvas.getAttribute("data-transition-count")), dom_nodes: await page.locator("*").count() });
    await page.waitForTimeout(300);
  }

  const waveform = page.getByRole("region", { name: "waveform" });
  const canvas = page.getByLabel("Digital waveform");
  const interact = async (iteration: number): Promise<void> => {
    const previous = await canvas.getAttribute("data-rendered-window");
    await waveform.press(iteration % 2 ? "ArrowLeft" : "ArrowRight");
    await waveform.press(iteration % 2 ? "+" : "-");
    await page.waitForFunction((prior) => document.querySelector<HTMLCanvasElement>('canvas[aria-label="Digital waveform"]')?.dataset.renderedWindow !== prior, previous);
    await page.evaluate(() => new Promise<void>((resolve) => requestAnimationFrame(() => resolve())));
  };
  for (let warmup = 0; warmup < 3; warmup += 1) { await interact(warmup); }
  const interactions: number[] = [];
  for (let iteration = 0; iteration < 30; iteration += 1) {
    const started = await page.evaluate(() => performance.now());
    await interact(iteration);
    interactions.push((await page.evaluate(() => performance.now())) - started);
    await page.waitForTimeout(50);
  }
  const heap = await page.evaluate(async () => {
    const precise = performance as Performance & { measureUserAgentSpecificMemory?: () => Promise<{ bytes: number }> };
    if (!precise.measureUserAgentSpecificMemory) return null;
    try { const measurement = await precise.measureUserAgentSpecificMemory(); return Number.isFinite(measurement.bytes) ? measurement.bytes : null; }
    catch { return null; }
  });
  const assetManifest = readFileSync("production-assets.json");
  const report = {
    schema_version: 1, method: "c2-b5-playwright-production-v1", threshold: null,
    viewport: { width: 1280, height: 900, device_pixel_ratio: 1 }, warmup_iterations: 3,
    load_iterations: loads.length, interaction_iterations: interactions.length,
    timing: "performance.now around UI action, API completion, Canvas dataset update, and next animation frame",
    browser: browser.version(), automation: "Playwright 1.50.1", node: process.version,
    host: { platform: platform(), release: release(), architecture: arch() },
    fixture_manifest_sha256: createHash("sha256").update(readFileSync("benchmarks/fixtures.json")).digest("hex"),
    fixture_generator_sha256: createHash("sha256").update(readFileSync("benchmarks/generate_fixtures.py")).digest("hex"),
    benchmark_script_sha256: createHash("sha256").update(readFileSync("tests/performance.spec.ts")).digest("hex"),
    production_asset_manifest_sha256: createHash("sha256").update(assetManifest).digest("hex"),
    fixtures: manifest.fixtures, loads,
    load_median_ms: percentile(loads.map((item) => item.milliseconds), 0.5), load_p95_ms: percentile(loads.map((item) => item.milliseconds), 0.95),
    interaction_median_ms: percentile(interactions, 0.5), interaction_p95_ms: percentile(interactions, 0.95),
    used_js_heap_bytes: heap, memory_reliable: heap !== null,
  };
  writeFileSync("test-results/c2-b5-performance.json", JSON.stringify(report, null, 2) + "\n");
  expect(loads).toHaveLength(15); expect(interactions).toHaveLength(30);
  expect(Math.max(...loads.map((item) => item.commands))).toBeLessThanOrEqual(24 * (960 * 2 + 2) + 1);
  expect(Math.max(...loads.map((item) => item.dom_nodes))).toBeLessThan(1000);
});
