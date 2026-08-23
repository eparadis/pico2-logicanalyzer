import type {
  BusPage, BusRequest, CaptureMetadata, Channel, ExportRequest, Operation, WaveformWindow,
} from "./api.generated";
import type { DeviceInfo, LiveCaptureRequest } from "./api.b6.generated";

export class ApiError extends Error {
  constructor(readonly status: number, message: string) { super(message); }
}

async function checked(response: Response | Promise<Response>): Promise<Response> {
  const value = await response;
  if (!value.ok) throw new ApiError(value.status, `request failed (${value.status})`);
  return value;
}

async function json<T>(response: Response | Promise<Response>): Promise<T> {
  return (await checked(response)).json() as Promise<T>;
}

const request = (input: RequestInfo | URL, init: RequestInit = {}): Promise<Response> =>
  fetch(input, { credentials: "same-origin", ...init });

export const api = {
  health: (): Promise<{ status: "ready"; api_version: "v1" }> => json(request("/api/v1/readiness")),
  identify: (): Promise<DeviceInfo> => json(request("/api/v1/device/identify", { method: "POST" })),
  reconnectDevice: (): Promise<DeviceInfo> => json(request("/api/v1/device/reconnect", { method: "POST" })),
  liveCapture: (body: LiveCaptureRequest): Promise<Operation> =>
    json(request("/api/v1/device/captures", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) })),
  import: (artifact: File, metadata?: object, signal?: AbortSignal): Promise<Operation> => {
    const csv = artifact.type === "text/csv" || artifact.name.toLowerCase().endsWith(".csv");
    const safeArtifact = new File([artifact], artifact.name.slice(0, 128), {
      type: csv ? "text/csv" : "application/x-pico-la-replay",
    });
    const form = new FormData(); form.append("artifact", safeArtifact);
    if (metadata) form.append("metadata", new Blob([JSON.stringify(metadata)], { type: "application/json" }));
    return json(request("/api/v1/imports", { method: "POST", body: form, signal }));
  },
  operation: (id: string, signal?: AbortSignal): Promise<Operation> =>
    json(request(`/api/v1/operations/${encodeURIComponent(id)}`, { signal })),
  cancel: (id: string): Promise<Operation> =>
    json(request(`/api/v1/operations/${encodeURIComponent(id)}/cancel`, { method: "POST" })),
  capture: (id: string, signal?: AbortSignal): Promise<CaptureMetadata> =>
    json(request(`/api/v1/captures/${encodeURIComponent(id)}`, { signal })),
  channels: (id: string, signal?: AbortSignal): Promise<{ channels: Channel[] }> =>
    json(request(`/api/v1/captures/${encodeURIComponent(id)}/channels`, { signal })),
  waveform: (id: string, start: number, end: number, ids: number[], pixels: number, signal?: AbortSignal): Promise<WaveformWindow> => {
    const query = new URLSearchParams({ start: String(start), end: String(end), channel_ids: ids.join(","), pixel_width: String(pixels) });
    return json(request(`/api/v1/captures/${encodeURIComponent(id)}/waveform?${query}`, { signal }));
  },
  bus: (id: string, body: BusRequest, signal?: AbortSignal): Promise<BusPage> =>
    json(request(`/api/v1/captures/${encodeURIComponent(id)}/bus`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body), signal })),
  export: (id: string, body: ExportRequest): Promise<Response> =>
    checked(request(`/api/v1/captures/${encodeURIComponent(id)}/exports`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) })),
  shutdown: (): Promise<Response> => checked(request("/api/v1/shutdown", { method: "POST" })),
};
