export type Viewport = { start: number; end: number; pixels: number };

export function clampViewport(start: number, end: number, count: number, pixels = 1): Viewport {
  const safeCount = Math.max(1, Math.floor(count));
  const width = Math.max(1, Math.min(safeCount, Math.round(end - start)));
  const left = Math.max(0, Math.min(safeCount - width, Math.round(start)));
  return { start: left, end: left + width, pixels: Math.max(1, Math.floor(pixels)) };
}

export function sampleAtPixel(view: Viewport, pixel: number): number {
  const ratio = Math.max(0, Math.min(1, pixel / Math.max(1, view.pixels)));
  return Math.min(view.end - 1, view.start + Math.floor(ratio * (view.end - view.start)));
}

export function pixelAtSample(view: Viewport, sample: number): number {
  return ((sample - view.start) / Math.max(1, view.end - view.start)) * view.pixels;
}

export function zoomAt(view: Viewport, sample: number, factor: number, count: number, maxWidth = count): Viewport {
  const oldWidth = view.end - view.start;
  const width = Math.max(1, Math.min(count, maxWidth, Math.round(oldWidth / Math.max(0.01, factor))));
  const ratio = Math.max(0, Math.min(1, (sample - view.start) / oldWidth));
  const left = Math.round(sample - ratio * width);
  return clampViewport(left, left + width, count, view.pixels);
}

export function pan(view: Viewport, delta: number, count: number): Viewport {
  return clampViewport(view.start + delta, view.end + delta, count, view.pixels);
}
