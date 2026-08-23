import { expect, test } from "vitest";
import { clampViewport, pan, pixelAtSample, sampleAtPixel, zoomAt } from "./geometry";
test("viewport pan and cursor-centered zoom are clamped", () => {
  expect(pan({ start: 0, end: 10, pixels: 1 }, -9, 100)).toMatchObject({ start: 0, end: 10 });
  expect(zoomAt({ start: 0, end: 100, pixels: 1 }, 80, 2, 100)).toMatchObject({ start: 40, end: 90 });
  expect(zoomAt({ start: 100, end: 200, pixels: 1000 }, 175, 2, 1000)).toEqual({ start: 138, end: 188, pixels: 1000 });
  expect(sampleAtPixel({ start: 100, end: 200, pixels: 1000 }, 750)).toBe(175);
  expect(pixelAtSample({ start: 100, end: 200, pixels: 1000 }, 175)).toBe(750);
  expect(clampViewport(-50, 500, 100, 800)).toEqual({ start: 0, end: 100, pixels: 800 });
  expect(zoomAt({ start: 0, end: 100_000, pixels: 800 }, 50_000, 0.5, 393_216, 100_000)).toEqual({ start: 0, end: 100_000, pixels: 800 });
});
