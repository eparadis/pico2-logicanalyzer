import { expect, test } from "@playwright/test";

test.use({ deviceScaleFactor: 2, viewport: { width: 1280, height: 900 } });

test("independent maximum-width DPR, request, DOM, and secret bounds", async ({ page, context }) => {
  const urls: string[] = []; const messages: string[] = [];
  page.on("request", (request) => urls.push(request.url()));
  page.on("console", (message) => messages.push(message.text()));
  await page.goto("/");
  const cookie = (await context.cookies()).find((item) => item.name === "pico_la_capability");
  expect(cookie).toBeDefined(); expect(cookie).toMatchObject({ httpOnly: true, sameSite: "Strict" });
  await page.getByLabel("Import capture").setInputFiles("benchmarks/fixtures/maximum-24.npz");
  await page.getByRole("button", { name: "Open", exact: true }).click();
  await expect(page.locator("p[role=status]")).toHaveText("ready");
  const canvas = page.getByLabel("Digital waveform");
  await expect(canvas).toHaveAttribute("data-rendered-window", /\d+:\d+/);
  const dimensions = await canvas.evaluate((element) => ({
    backingWidth: element.width, backingHeight: element.height,
    cssWidth: element.clientWidth, cssHeight: element.clientHeight,
  }));
  expect(dimensions.backingWidth).toBe(dimensions.cssWidth * 2);
  expect(dimensions.backingHeight).toBe(24 * 28 * 2);
  expect(await page.getByLabel("Cursor channel values").getByRole("listitem").count()).toBe(24);
  expect(await page.locator("*").count()).toBeLessThan(1000);
  const waveformUrls = urls.filter((url) => url.includes("/waveform?"));
  expect(waveformUrls.length).toBeGreaterThan(0);
  for (const raw of waveformUrls) {
    const url = new URL(raw); const start = Number(url.searchParams.get("start"));
    const end = Number(url.searchParams.get("end"));
    expect(end - start).toBeLessThanOrEqual(100_000);
    expect(Number(url.searchParams.get("pixel_width"))).toBeLessThanOrEqual(960);
  }
  const exposed = [page.url(), await page.locator("body").innerText(), messages.join("\n"),
    JSON.stringify(await page.evaluate(() => ({ local: { ...localStorage }, session: { ...sessionStorage }, referrer: document.referrer }))),
    urls.join("\n")].join("\n");
  expect(exposed).not.toContain(cookie!.value);
});
