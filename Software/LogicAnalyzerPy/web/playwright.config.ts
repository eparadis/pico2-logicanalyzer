import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  testIgnore: process.env.B5_BENCHMARK === "1" || process.argv.some((value) => value.includes("performance.spec.ts")) ? [] : ["performance.spec.ts"],
  fullyParallel: false,
  webServer: {
    command: "../.venv/bin/python -m pico_logic_analyzer web --host 127.0.0.1 --port 4173",
    url: "http://127.0.0.1:4173/api/v1/readiness",
    reuseExistingServer: false,
  },
  use: { baseURL: "http://127.0.0.1:4173", ...devices["Desktop Chrome"], viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 },
});
