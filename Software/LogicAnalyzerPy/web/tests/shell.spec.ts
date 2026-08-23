import { expect, test } from "@playwright/test";

test("browser entry point is registered", async () => {
  expect("pico-la").toBe("pico-la");
});
