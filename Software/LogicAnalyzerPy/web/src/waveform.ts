export type Point = { sample_index: number; value: number };
export type ChannelWave = { channel_id: number; transitions: Point[] };
export type Segment = { x1: number; y1: number; x2: number; y2: number; verticalTo?: number; channel: number };
export type Marker = { x: number; kind: "trigger" };

export const ROW_HEIGHT = 28;

export function planWaveform(channels: ChannelWave[], start: number, end: number, width: number, row = ROW_HEIGHT): Segment[] {
  const span = Math.max(1, end - start); const bounded = Math.max(1, width) * 2 + 2;
  return channels.flatMap((channel, channelIndex) => {
    const points = channel.transitions.slice(0, bounded); const result: Segment[] = [];
    points.forEach((point, index) => {
      const next = points[index + 1]; const x1 = ((point.sample_index - start) / span) * width;
      const x2 = (((next?.sample_index ?? end) - start) / span) * width;
      const y = channelIndex * row + (point.value ? 5 : row - 5);
      const nextY = next ? channelIndex * row + (next.value ? 5 : row - 5) : undefined;
      result.push({ x1, y1: y, x2, y2: y, verticalTo: nextY, channel: channel.channel_id });
    });
    return result.slice(0, bounded * 2);
  });
}

export function valueAt(points: Point[], sample: number): number {
  let value = points[0]?.value ?? 0;
  for (const point of points) { if (point.sample_index > sample) break; value = point.value; }
  return value;
}

export function triggerMarker(trigger: number, start: number, end: number, width: number): Marker | null {
  return trigger >= start && trigger < end ? { x: ((trigger - start) / Math.max(1, end - start)) * width, kind: "trigger" } : null;
}

export function drawWaveform(canvas: HTMLCanvasElement, segments: Segment[], rows: number, dpr: number, marker: Marker | null = null): number {
  const context = canvas.getContext("2d"); if (!context) return 0;
  const cssWidth = Math.max(1, canvas.clientWidth || canvas.width); const cssHeight = Math.max(1, rows * ROW_HEIGHT);
  const ratio = Math.max(1, Math.min(4, dpr)); canvas.width = Math.round(cssWidth * ratio); canvas.height = Math.round(cssHeight * ratio);
  context.setTransform(ratio, 0, 0, ratio, 0, 0); context.clearRect(0, 0, cssWidth, cssHeight);
  context.strokeStyle = "#38d878"; context.lineWidth = 1; context.beginPath();
  for (const segment of segments) { context.moveTo(segment.x1, segment.y1); context.lineTo(segment.x2, segment.y2); if (segment.verticalTo !== undefined) context.lineTo(segment.x2, segment.verticalTo); }
  context.stroke();
  if (marker) { context.strokeStyle = "#ffb347"; context.beginPath(); context.moveTo(marker.x, 0); context.lineTo(marker.x, cssHeight); context.stroke(); }
  return segments.length + (marker ? 1 : 0);
}
