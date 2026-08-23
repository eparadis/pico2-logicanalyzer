import { defineConfig, devices } from "@playwright/test";

if (process.env.B6_NATIVE !== "1" || !process.env.PICO_LA_DEVICE_PORT) {
  throw new Error("native B6 execution requires explicit runtime authorization");
}

export default defineConfig({
  testDir: "./tests",
  workers: 1,
  webServer: {
    command: "../.venv/bin/python -m pico_logic_analyzer web --host 127.0.0.1 --port 4176",
    url: "http://127.0.0.1:4176/api/v1/readiness",
    reuseExistingServer: false,
  },
  use: { baseURL: "http://127.0.0.1:4176", ...devices["Desktop Chrome"], viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 },
});
