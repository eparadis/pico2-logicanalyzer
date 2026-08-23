import { expect, test } from "@playwright/test";

test("live device workflow is explicit, bounded, cancellable, and opaque", async ({ page, context }) => {
  const secret = "/machine/local/secret-port"; const requests: string[] = []; const messages: string[] = [];
  page.on("request", (request) => requests.push(`${request.url()} ${request.postData() ?? ""}`));
  page.on("console", (message) => messages.push(message.text()));
  let width = 8; let sequence = 0; let cancelling = false;
  await page.route("**/api/v1/device/identify", (route) => route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ device_id: "device-1", connected: true, max_frequency_hz: 100000000, blast_frequency_hz: 125000000, buffer_size: 393216, channel_count: 24 }) }));
  await page.route("**/api/v1/device/reconnect", (route) => route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ device_id: "device-1", connected: true, max_frequency_hz: 100000000, blast_frequency_hz: 125000000, buffer_size: 393216, channel_count: 24 }) }));
  await page.route("**/api/v1/device/captures", async (route) => {
    const body = route.request().postDataJSON() as { channel_ids: number[] }; width = body.channel_ids.length; sequence += 1;
    await route.fulfill({ status: 202, contentType: "application/json", body: JSON.stringify({ operation_id: `live-${sequence}`, state: "pending", capture_id: null }) });
  });
  await page.route("**/api/v1/operations/live-*/cancel", async (route) => {
    cancelling = true;
    await route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ operation_id: `live-${sequence}`, state: "cancelling", capture_id: null }) });
  });
  await page.route("**/api/v1/operations/live-*", async (route) => {
    const held = sequence === 4;
    await route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ operation_id: `live-${sequence}`, state: cancelling ? "cancelled" : held ? "running" : "succeeded", capture_id: cancelling || held ? null : `live-capture-${sequence}` }) });
  });
  await page.route(/\/api\/v1\/captures\/live-capture-\d+(?:\/channels|\/waveform.*)?$/, async (route) => {
    const url = route.request().url();
    if (url.includes("/channels")) { await route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ channels: Array.from({ length: width }, (_, channel_id) => ({ channel_id, label: `D${channel_id}`, packed_position: channel_id })) }) }); return; }
    if (url.includes("/waveform")) { const query = new URL(url).searchParams; const ids = (query.get("channel_ids") ?? "").split(",").map(Number); await route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ start: Number(query.get("start")), end: Number(query.get("end")), channels: ids.map((channel_id) => ({ channel_id, transitions: [{ sample_index: 0, value: 0 }, { sample_index: 8, value: 1 }] })) }) }); return; }
    await route.fulfill({ status: 200, contentType: "application/json", body: JSON.stringify({ capture_id: `live-capture-${sequence}`, sample_count: 32, sample_rate_hz: 100000, trigger_index: 8, trigger_channel: 0, trigger_edge: "rising", channel_ids: Array.from({ length: width }, (_, index) => index) }) });
  });

  await page.goto("/"); await page.getByRole("button", { name: "Identify device" }).click();
  await expect(page.getByText("Connected: 24 channels, 393216 byte buffer")).toBeVisible();
  for (const channels of [8, 16, 24]) {
    await page.getByRole("button", { name: `${channels} channels` }).click();
    await page.getByRole("button", { name: "Capture live" }).click();
    await expect(page.locator("p[role=status]")).toHaveText("ready");
    await expect(page.getByRole("region", { name: "Channels" }).getByText(`D${channels - 1}`, { exact: false }).first()).toBeVisible();
  }
  await page.getByRole("button", { name: "Reopen device" }).click(); await expect(page.locator("p[role=status]")).toHaveText("ready");

  cancelling = false;
  await page.getByRole("button", { name: "Capture live" }).click(); await page.getByRole("button", { name: "Cancel live capture" }).click();
  await expect(page.locator("p[role=status]")).toHaveText("ready");

  const cookie = (await context.cookies()).find((item) => item.name === "pico_la_capability")!;
  const exposed = [await page.locator("body").innerText(), page.url(), JSON.stringify(await page.evaluate(() => ({ local: { ...localStorage }, session: { ...sessionStorage } }))), requests.join("\n"), messages.join("\n")].join("\n");
  expect(exposed).not.toContain(secret); expect(exposed).not.toContain(cookie.value);
  expect(requests.every((entry) => !entry.includes("port"))).toBe(true);
});
