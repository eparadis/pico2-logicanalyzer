/* Generated from ../openapi.json; Python owns the wire authority. */
export type OperationState =
  | "pending" | "running" | "cancelling" | "succeeded" | "failed" | "cancelled";
export interface ErrorEnvelope { error: { code: string; message: string } }
export interface Operation { operation_id: string; state: OperationState }
export interface BusRow {
  sample_index: number; time_seconds: string; binary: string; hexadecimal: string;
  decimal: number; end_sample_index: number | null; end_time_seconds: string | null;
  duration_seconds: string | null;
}
