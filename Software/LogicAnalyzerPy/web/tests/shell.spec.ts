import { expect, test, type Page } from "@playwright/test";

function csv(width: number, count = 256): string {
  const labels = Array.from({ length: width }, (_, index) => `D${index}`);
  const rows = ["sample_index,time_seconds,trigger," + labels.join(",")];
  const trigger = Math.floor(count / 2);
  for (let index = 0; index < count; index += 1) {
    const time = (index - trigger) / 1000;
    const word = index ^ (index >> 1);
    rows.push([index, time, Number(index === trigger), ...labels.map((_, bit) => (word >> bit) & 1)].join(","));
  }
  return rows.join("\n") + "\n";
}

async function openCsv(page: Page, width: number): Promise<void> {
  await page.getByLabel("Import capture").setInputFiles({ name: `width-${width}.csv`, mimeType: "text/csv", buffer: Buffer.from(csv(width)) });
  await page.getByLabel("Physical channel IDs").fill(Array.from({ length: width }, (_, index) => index).join(","));
  await page.getByLabel("Sample rate").fill("1000"); await page.getByLabel("Trigger channel").fill("0");
  await page.getByRole("button", { name: "Open", exact: true }).click();
  await expect(page.locator("p[role=status]")).toHaveText("ready");
  await expect(page.getByLabel("Digital waveform")).toHaveAttribute("data-rendered-window", /\d+:\d+/);
}

test("production viewer covers widths, bounded Canvas, interactions, buses, export, and failures", async ({ page, context }) => {
  const consoleMessages: string[] = []; const requestUrls: string[] = [];
  page.on("console", (message) => consoleMessages.push(message.text())); page.on("request", (request) => requestUrls.push(request.url()));
  await page.goto("/"); await expect(page.getByRole("heading", { name: "Pico Logic Analyzer" })).toBeVisible();
  await expect(page.locator("p[role=status]")).toHaveText("empty");
  const cookies = await context.cookies(); expect(cookies).toHaveLength(1);
  expect(cookies[0]).toMatchObject({ name: "pico_la_capability", httpOnly: true, sameSite: "Strict" });

  for (const width of [8, 16, 24]) {
    await openCsv(page, width);
    await expect(page.getByRole("region", { name: "Channels" }).getByText(`D${width - 1}`, { exact: false }).first()).toBeVisible();
    await expect(page.getByLabel("Cursor channel values").getByRole("listitem")).toHaveCount(width);
  }

  const canvas = page.getByLabel("Digital waveform"); const commandCount = Number(await canvas.getAttribute("data-commands"));
  const transitionCount = Number(await canvas.getAttribute("data-transition-count"));
  expect(commandCount).toBeLessThanOrEqual(24 * (960 * 2 + 2) + 1); expect(transitionCount).toBeLessThanOrEqual(24 * (960 * 2 + 2));
  expect(await page.locator("*").count()).toBeLessThan(1000);
  await expect(page.getByLabel("Cursor channel values").getByText("D7: 1", { exact: true })).toBeVisible();
  const channelRegion = page.getByRole("region", { name: "Channels" }); await channelRegion.getByLabel(/D23/).uncheck();
  await expect(page.getByLabel("Cursor channel values").getByRole("listitem")).toHaveCount(23); await channelRegion.getByLabel(/D23/).check();
  const viewport = page.getByLabel("Viewport"); const before = await viewport.textContent();
  const waveform = page.getByRole("region", { name: "waveform" });
  await waveform.press("ArrowRight"); await waveform.press("+");
  const box = await waveform.boundingBox(); expect(box).not.toBeNull();
  await page.mouse.move(box!.x + box!.width * 0.8, box!.y + 40); await page.mouse.down();
  await page.mouse.move(box!.x + box!.width * 0.3, box!.y + 40); await page.mouse.up();
  await expect(viewport).not.toHaveText(before ?? "");
  const beforeWheel = await viewport.textContent(); await canvas.hover({ position: { x: 720, y: 20 } }); await page.mouse.wheel(0, -100);
  await expect(viewport).not.toHaveText(beforeWheel ?? "");
  await canvas.hover({ position: { x: 480, y: 20 } }); await expect(page.getByText(/Cursor:\s*sample/)).toBeVisible();

  await page.getByRole("button", { name: "Analyze bus" }).click(); await expect(page.getByRole("table")).toBeVisible();
  await expect(page.getByText(/1–100 of 256/)).toBeVisible(); await page.getByRole("button", { name: "Next" }).click(); await expect(page.getByText(/101–200 of 256/)).toBeVisible();
  const download = page.waitForEvent("download"); await page.getByRole("button", { name: "Export CSV" }).click();
  expect((await download).suggestedFilename()).toBe("pico-la-bus.csv");
  await page.getByLabel("Bus mode").selectOption("sampled"); await page.getByLabel("Strobe channel").selectOption("0");
  await page.getByLabel("Bus edge").selectOption("falling"); await page.getByRole("button", { name: "Analyze bus" }).click();
  await expect(page.getByRole("table")).toBeVisible(); await expect(page.getByText(/of \d+/)).toBeVisible();

  await page.route("**/api/v1/captures/*/exports", (route) => route.fulfill({ status: 500, contentType: "application/json", body: '{"error":{"code":"failed","message":"failed"}}' }));
  await page.getByRole("button", { name: "Export CSV" }).click(); await expect(page.getByRole("alert")).toContainText("request failed");
  await page.unroute("**/api/v1/captures/*/exports");

  const oversize = Buffer.alloc(34 * 1024 * 1024 + 1);
  await page.getByLabel("Import capture").setInputFiles({ name: "oversize.npz", mimeType: "application/x-pico-la-replay", buffer: oversize });
  await page.getByRole("button", { name: "Open", exact: true }).click(); await expect(page.locator("p[role=status]")).toHaveText("error");
  await expect(page.getByRole("alert")).toContainText("too large");

  const token = cookies[0].value; const visibleText = await page.locator("body").innerText();
  const browserState = await page.evaluate(() => JSON.stringify({ referrer: document.referrer, local: { ...localStorage }, session: { ...sessionStorage } }));
  expect([page.url(), visibleText, browserState, consoleMessages.join("\n"), requestUrls.join("\n")].join("\n")).not.toContain(token);
  expect(requestUrls.every((url) => url.startsWith("http://127.0.0.1:4173/"))).toBe(true);
});

test("schema-1/schema-2 replay, cancellation, disconnect, reconnect, and shutdown are explicit", async ({ page }) => {
  await page.goto("/");
  for (const name of ["schema1-8.npz", "maximum-24.npz"]) {
    await page.getByLabel("Import capture").setInputFiles(`benchmarks/fixtures/${name}`);
    await page.getByRole("button", { name: "Open", exact: true }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready");
  }
  let cancelRequested = false;
  await page.route("**/api/v1/imports", (route) => route.fulfill({ status: 202, contentType: "application/json", body: '{"operation_id":"op-ui-cancel","state":"pending","capture_id":null}' }));
  await page.route("**/api/v1/operations/op-ui-cancel", async (route) => { if (cancelRequested) await new Promise((resolve) => setTimeout(resolve, 300)); await route.fulfill({ status: 200, contentType: "application/json", body: cancelRequested ? '{"operation_id":"op-ui-cancel","state":"cancelled","capture_id":null}' : '{"operation_id":"op-ui-cancel","state":"pending","capture_id":null}' }); });
  await page.route("**/api/v1/operations/op-ui-cancel/cancel", (route) => { cancelRequested = true; return route.fulfill({ status: 200, contentType: "application/json", body: '{"operation_id":"op-ui-cancel","state":"cancelling","capture_id":null}' }); });
  await page.getByLabel("Import capture").setInputFiles({ name: "cancel.npz", mimeType: "application/x-pico-la-replay", buffer: Buffer.from("bounded") });
  await page.getByRole("button", { name: "Open", exact: true }).click(); await page.getByRole("button", { name: "Cancel import" }).click(); await expect(page.locator("p[role=status]")).toHaveText("cancelling");
  await expect(page.locator("p[role=status]")).toHaveText("ready");
  await page.unroute("**/api/v1/imports"); await page.unroute("**/api/v1/operations/op-ui-cancel"); await page.unroute("**/api/v1/operations/op-ui-cancel/cancel"); await page.reload();
  await page.route("**/api/v1/readiness", (route) => route.abort("connectionrefused")); await page.getByRole("button", { name: "Reconnect" }).click(); await expect(page.locator("p[role=status]")).toHaveText("disconnected");
  await page.unroute("**/api/v1/readiness"); await page.getByRole("button", { name: "Reconnect" }).click(); await expect(page.locator("p[role=status]")).toHaveText("empty");
  await page.getByRole("button", { name: "Shut down server" }).click(); await expect(page.locator("p[role=status]")).toHaveText("shutdown");
});
