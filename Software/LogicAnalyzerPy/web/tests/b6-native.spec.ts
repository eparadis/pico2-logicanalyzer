import { expect, test } from "@playwright/test";

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
  }
  await page.getByRole("button", { name: "Analyze bus" }).click(); await expect(page.getByRole("table")).toBeVisible();
  const download = page.waitForEvent("download"); await page.getByRole("button", { name: "Export CSV" }).click(); expect((await download).suggestedFilename()).toBe("pico-la-bus.csv");
  await page.getByLabel("Bus mode").selectOption("sampled"); await page.getByLabel("Strobe channel").selectOption("23"); await page.getByLabel("Bus edge").selectOption("rising"); await page.getByRole("button", { name: "Analyze bus" }).click(); await expect(page.getByRole("table")).toBeVisible();
  await page.getByRole("button", { name: "Reopen device" }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready");
  await page.getByRole("button", { name: "Capture live" }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready", { timeout: 30_000 });
  const capability = (await context.cookies()).find((cookie) => cookie.name === "pico_la_capability")!.value;
  const exposed = [page.url(), await page.locator("body").innerText(), urls.join("\n"), consoleMessages.join("\n"), JSON.stringify(await page.evaluate(() => ({ local: { ...localStorage }, session: { ...sessionStorage } })))].join("\n");
  expect(exposed).not.toContain(capability); expect(urls.every((url) => !url.includes("device-port") && !url.includes("serial"))).toBe(true);
  await page.getByRole("button", { name: "Shut down server" }).click(); await expect(page.locator("p[role=status]")).toHaveText("shutdown");
});
