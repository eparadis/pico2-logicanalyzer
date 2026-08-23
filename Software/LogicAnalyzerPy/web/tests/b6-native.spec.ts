import { expect, test } from "@playwright/test";

const downloadBytes = async (download: import("@playwright/test").Download): Promise<Buffer> => {
  const stream = await download.createReadStream(); const chunks: Buffer[] = [];
  for await (const chunk of stream) chunks.push(Buffer.from(chunk));
  return Buffer.concat(chunks);
};

test("authorized native macOS live workflow", async ({ page, context }) => {
  test.setTimeout(120_000);
  const urls: string[] = []; const consoleMessages: string[] = [];
  page.on("request", (request) => urls.push(request.url()));
  page.on("console", (message) => consoleMessages.push(message.text()));
  await page.goto("/"); await page.getByRole("button", { name: "Identify device" }).click();
  await expect(page.getByText(/Connected: 24 channels/)).toBeVisible();
  for (const width of [8, 16, 24]) {
    await page.getByRole("button", { name: `${width} channels` }).click();
    await page.getByLabel("Live sample rate").fill("100000"); await page.getByLabel("Live pre-trigger samples").fill("1024"); await page.getByLabel("Live post-trigger samples").fill("3072");
    await page.getByLabel("Live trigger channel").fill("0"); await page.getByLabel("Live trigger edge").selectOption("rising"); await page.getByLabel("Live timeout").fill("10");
    await page.getByRole("button", { name: "Capture live" }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready", { timeout: 30_000 });
    await expect(page.getByLabel("Digital waveform")).toHaveAttribute("data-rendered-window", /\d+:\d+/);
    await expect(page.getByRole("region", { name: "Channels" }).getByText(`D${width - 1}`, { exact: false }).first()).toBeVisible();
    await expect(page.getByRole("region", { name: "Channels" })).toContainText("trigger sample 1024");
    await expect(page.getByText("Cursor: sample 1024; trigger-relative time 0.0000000 s")).toBeVisible();
    const values = page.getByLabel("Cursor channel values");
    for (const channel of [0, 8, 16, 23].filter((channel) => channel < width)) await expect(values.getByText(`D${channel}: 1`, { exact: true })).toBeVisible();
  }
  const ordered = page.getByRole("group", { name: "Ordered data channels (LSB first)" });
  for (let channel = 0; channel < 24; channel += 1) if (![0, 8, 16, 23].includes(channel)) await ordered.getByLabel(`D${channel}`, { exact: true }).uncheck();
  for (const channel of [0, 8, 16, 23]) await expect(ordered.getByLabel(`D${channel}`, { exact: true })).toBeChecked();
  await page.getByRole("button", { name: "Analyze bus" }).click(); await expect(page.getByRole("table")).toBeVisible();
  const rows = await page.getByRole("table").locator("tbody tr").allTextContents();
  expect(rows.length).toBeGreaterThan(2); expect(rows.every((row) => row.includes("0000") || row.includes("1111"))).toBe(true);
  expect(rows.some((row) => row.includes("0x0") && row.includes("0000"))).toBe(true); expect(rows.some((row) => row.includes("0xF") && row.includes("1111"))).toBe(true);
  const samples = await page.getByRole("table").locator("tbody tr td:first-child").allTextContents();
  expect(samples.map(Number)).toEqual([...samples.map(Number)].sort((a, b) => a - b));
  const downloadPromise = page.waitForEvent("download"); await page.getByRole("button", { name: "Export CSV" }).click(); const download = await downloadPromise;
  expect(download.suggestedFilename()).toBe("pico-la-bus.csv"); const exported = (await downloadBytes(download)).toString("utf8");
  expect(exported).toMatch(/^sample_index,time_seconds,binary,hexadecimal,decimal,end_sample_index,end_time_seconds,duration_seconds\n/);
  expect(exported).toContain(",0000,0x0,0,"); expect(exported).toContain(",1111,0xF,15,");
  await page.getByLabel("Bus mode").selectOption("sampled"); await page.getByLabel("Strobe channel").selectOption("23"); await page.getByLabel("Bus edge").selectOption("rising"); await page.getByRole("button", { name: "Analyze bus" }).click(); await expect(page.getByRole("table")).toBeVisible();
  const sampled = await page.getByRole("table").locator("tbody tr").allTextContents(); expect(sampled.length).toBe(31); expect(sampled.every((row) => row.includes("111") && row.includes("0x7") && row.includes("7"))).toBe(true);
  await page.getByRole("button", { name: "Reopen device" }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready");
  await page.getByRole("button", { name: "Capture live" }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready", { timeout: 30_000 });
  const capability = (await context.cookies()).find((cookie) => cookie.name === "pico_la_capability")!.value;
  const exposed = [page.url(), await page.locator("body").innerText(), urls.join("\n"), consoleMessages.join("\n"), JSON.stringify(await page.evaluate(() => ({ local: { ...localStorage }, session: { ...sessionStorage } })))].join("\n");
  expect(exposed).not.toContain(capability); expect(urls.every((url) => !url.includes("device-port") && !url.includes("serial"))).toBe(true);
  await page.getByRole("button", { name: "Shut down server" }).click(); await expect(page.locator("p[role=status]")).toHaveText("shutdown");
});
