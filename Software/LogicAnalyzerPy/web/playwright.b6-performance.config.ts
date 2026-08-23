import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  fullyParallel: false,
  workers: 1,
  webServer: {
    command: "../.venv/bin/python -m pico_logic_analyzer web --host 127.0.0.1 --port 4174",
    url: "http://127.0.0.1:4174/api/v1/readiness",
    reuseExistingServer: false,
  },
  use: { baseURL: "http://127.0.0.1:4174", ...devices["Desktop Chrome"], viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 },
});
