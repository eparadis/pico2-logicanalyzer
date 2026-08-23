import { expect, test } from "@playwright/test";

test("production shell is offline, capability-protected, and shuts down", async ({ page, context }) => {
  const consoleMessages: string[] = [];
  page.on("console", (message) => consoleMessages.push(message.text()));
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "Pico Logic Analyzer" })).toBeVisible();
  const cookies = await context.cookies();
  expect(cookies).toHaveLength(1);
  expect(cookies[0]).toMatchObject({ name: "pico_la_capability", httpOnly: true, sameSite: "Strict" });
  const readiness = await page.request.get("/api/v1/readiness");
  expect(readiness.status()).toBe(200);
  const shutdown = await page.evaluate(async () => {
    const response = await fetch("/api/v1/shutdown", { method: "POST", credentials: "same-origin" });
    return response.status;
  });
  expect(shutdown).toBe(204);
  expect(consoleMessages.join("\n")).not.toContain(cookies[0].value);
});
