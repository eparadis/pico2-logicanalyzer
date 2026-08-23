/* Generated from ../openapi.json; Python owns the wire authority. */
export type OperationState =
  | "pending" | "running" | "cancelling" | "succeeded" | "failed" | "cancelled";
export interface ErrorEnvelope { error: { code: string; message: string } }
export interface DeviceInfo {
  device_id: string; connected: boolean; max_frequency_hz: number;
  blast_frequency_hz: number; buffer_size: number; channel_count: number
}
export interface LiveCaptureRequest {
  sample_rate_hz: number; pre_trigger_samples: number; post_trigger_samples: number;
  trigger_channel: number; trigger_edge: "rising" | "falling";
  channel_ids: number[]; timeout_seconds: number
}
export interface Operation { operation_id: string; state: OperationState; capture_id: string | null }
export interface CaptureMetadata {
  capture_id: string; sample_count: number; sample_rate_hz: number;
  trigger_index: number; trigger_channel: number;
  trigger_edge: "rising" | "falling"; channel_ids: number[]
}
export interface Channel { channel_id: number; label: string; packed_position: number }
export interface WaveformWindow {
  start: number; end: number;
  channels: { channel_id: number; transitions: { sample_index: number; value: number }[] }[]
}
export interface BusRequest { mode: "transition" | "sampled"; channel_ids: number[]; strobe_channel: number | null; edge: "rising" | "falling" | null; offset: number; limit: number }
export interface BusPage { rows: BusRow[]; offset: number; total: number; next_offset: number | null }
export interface ExportRequest { format: "bus-transition-csv" | "bus-sampled-csv"; channel_ids: number[]; strobe_channel: number | null; edge: "rising" | "falling" | null }
export interface BusRow {
  sample_index: number; time_seconds: string; binary: string; hexadecimal: string;
  decimal: number; end_sample_index: number | null; end_time_seconds: string | null;
  duration_seconds: string | null;
}
