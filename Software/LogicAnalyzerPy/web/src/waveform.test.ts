import { expect, test } from "vitest";
import { drawWaveform, planWaveform, triggerMarker, valueAt } from "./waveform";
test("wave planning remains bounded by viewport pixels and preserves labels channels", () => {
  const points = Array.from({ length: 99 }, (_, sample_index) => ({ sample_index, value: sample_index % 2 }));
  const plan = planWaveform([{ channel_id: 23, transitions: points }], 0, 100, 10, 28);
  expect(plan).toHaveLength(22); expect(plan[0]).toMatchObject({ x1: 0, channel: 23 });
});
test("transition intervals provide exact cursor values and trigger marker", () => {
  expect(valueAt([{ sample_index: 0, value: 0 }, { sample_index: 4, value: 1 }], 5)).toBe(1);
  expect(triggerMarker(4, 0, 8, 800)).toEqual({ x: 400, kind: "trigger" });
  expect(triggerMarker(8, 0, 8, 800)).toBeNull();
  expect(valueAt([{ sample_index: 4, value: 1 }], 4)).toBe(1);
});
test("Canvas commands are bounded and include a trigger marker", () => {
  const calls: string[] = [];
  const context = new Proxy({}, { get: (_target, name) => name === "setTransform" || name === "clearRect" || name === "beginPath" || name === "moveTo" || name === "lineTo" || name === "stroke" ? () => calls.push(String(name)) : undefined, set: () => true });
  const canvas = { width: 100, height: 28, clientWidth: 100, getContext: () => context } as unknown as HTMLCanvasElement;
  const count = drawWaveform(canvas, [{ x1: 0, y1: 4, x2: 100, y2: 4, verticalTo: 24, channel: 0 }], 1, 2, { x: 50, kind: "trigger" });
  expect(count).toBe(2); expect(calls.filter((call) => call === "lineTo")).toHaveLength(3);
});
