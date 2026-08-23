import React, { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { createRoot } from "react-dom/client";
import { ApiError, api } from "./api";
import type { BusPage, BusRequest, CaptureMetadata, Channel, Operation, WaveformWindow } from "./api.generated";
import type { DeviceInfo } from "./api.b6.generated";
import { clampViewport, pan, sampleAtPixel, zoomAt, type Viewport } from "./geometry";
import { drawWaveform, planWaveform, triggerMarker, valueAt } from "./waveform";
import "./style.css";

type AppState = "loading" | "ready" | "empty" | "error" | "disconnected" | "cancelling" | "shutdown";
type BusMode = "transition" | "sampled";
const CANVAS_PIXELS = 960; const MAX_WINDOW = 100_000; const PAGE_SIZE = 100;

function parseChannelIds(text: string): number[] | null {
  if (!/^\d+(,\d+)*$/.test(text)) return null;
  const ids = text.split(",").map(Number);
  return ids.length >= 1 && ids.length <= 24 && new Set(ids).size === ids.length && ids.every((id) => id >= 0 && id <= 23) ? ids : null;
}

function messageFor(error: unknown): string {
  if (error instanceof ApiError) {
    if (error.status === 409) return "Another operation is already active.";
    if (error.status === 413) return "The selected file is too large.";
  }
  return "The request failed. Check the file or reconnect to the local server.";
}

export function App(): React.JSX.Element {
  const [state, setState] = useState<AppState>("empty"); const [error, setError] = useState("");
  const [file, setFile] = useState<File | null>(null); const [channelText, setChannelText] = useState("0,1,2,3,4,5,6,7");
  const [sampleRate, setSampleRate] = useState("100000"); const [triggerChannel, setTriggerChannel] = useState("0");
  const [triggerEdge, setTriggerEdge] = useState<"rising" | "falling">("rising");
  const [capture, setCapture] = useState<CaptureMetadata | null>(null); const [channels, setChannels] = useState<Channel[]>([]);
  const [visible, setVisible] = useState<number[]>([]); const [view, setView] = useState<Viewport>({ start: 0, end: 1, pixels: CANVAS_PIXELS });
  const [cursorWave, setCursorWave] = useState<WaveformWindow | null>(null); const [cursor, setCursor] = useState(0);
  const [operation, setOperation] = useState<Operation | null>(null); const [busMode, setBusMode] = useState<BusMode>("transition");
  const [operationKind, setOperationKind] = useState<"import" | "live">("import");
  const [busChannels, setBusChannels] = useState<number[]>([]); const [strobe, setStrobe] = useState<number | null>(null);
  const [busEdge, setBusEdge] = useState<"rising" | "falling">("rising"); const [busOffset, setBusOffset] = useState(0);
  const [busPage, setBusPage] = useState<BusPage | null>(null); const canvas = useRef<HTMLCanvasElement>(null);
  const [device, setDevice] = useState<DeviceInfo | null>(null); const [liveChannels, setLiveChannels] = useState("0,1,2,3,4,5,6,7");
  const [liveRate, setLiveRate] = useState("100000"); const [livePre, setLivePre] = useState("1024"); const [livePost, setLivePost] = useState("3072");
  const [liveTrigger, setLiveTrigger] = useState("0"); const [liveEdge, setLiveEdge] = useState<"rising" | "falling">("rising"); const [liveTimeout, setLiveTimeout] = useState("10");
  const pollAbort = useRef<AbortController | null>(null); const waveAbort = useRef<AbortController | null>(null);
  const drag = useRef<{ x: number; view: Viewport } | null>(null);
  const csv = file ? file.type === "text/csv" || file.name.toLowerCase().endsWith(".csv") : false;
  const parsedIds = parseChannelIds(channelText); const triggerId = Number(triggerChannel); const parsedRate = Number(sampleRate);
  const metadataValid = !csv || (parsedIds !== null && Number.isInteger(parsedRate) && parsedRate > 0 && Number.isInteger(triggerId) && parsedIds.includes(triggerId));

  useEffect(() => () => { pollAbort.current?.abort(); waveAbort.current?.abort(); }, []);

  const loadCapture = useCallback(async (id: string, signal?: AbortSignal) => {
    const [metadata, channelData] = await Promise.all([api.capture(id, signal), api.channels(id, signal)]);
    setCapture(metadata); setChannels(channelData.channels); const ids = channelData.channels.map((channel) => channel.channel_id);
    setVisible(ids); setBusChannels(ids); setStrobe(ids.length > 1 ? ids.at(-1)! : null); setBusPage(null); setBusOffset(0);
    const end = Math.min(metadata.sample_count, MAX_WINDOW); setView(clampViewport(0, end, metadata.sample_count, CANVAS_PIXELS));
    setCursor(Math.min(metadata.sample_count - 1, metadata.trigger_index)); setError(""); setState(metadata.sample_count ? "ready" : "empty");
  }, []);

  const open = async (): Promise<void> => {
    if (!file || !metadataValid) { setError("Select a supported file and enter valid CSV metadata."); setState("error"); return; }
    pollAbort.current?.abort(); const controller = new AbortController(); pollAbort.current = controller; setOperationKind("import");
    setState("loading"); setError(""); setBusPage(null);
    if (canvas.current) { delete canvas.current.dataset.renderedWindow; delete canvas.current.dataset.transitionCount; delete canvas.current.dataset.commands; }
    const metadata = csv ? { channel_ids: parsedIds!, sample_rate_hz: parsedRate, trigger_channel: triggerId, trigger_edge: triggerEdge } : undefined;
    try {
      let current = await api.import(file, metadata, controller.signal); setOperation(current);
      for (let attempt = 0; attempt < 300 && ["pending", "running", "cancelling"].includes(current.state); attempt += 1) {
        await new Promise((resolve) => globalThis.setTimeout(resolve, 100));
        current = await api.operation(current.operation_id, controller.signal); setOperation(current);
      }
      if (current.state === "cancelled") { setError(""); setState(capture ? "ready" : "empty"); return; }
      if (current.state !== "succeeded" || !current.capture_id) throw new Error("import did not succeed");
      await loadCapture(current.capture_id, controller.signal);
    } catch (caught) {
      if ((caught as Error).name === "AbortError") return;
      setError(messageFor(caught)); setState(caught instanceof TypeError ? "disconnected" : "error");
    } finally { if (pollAbort.current === controller) pollAbort.current = null; }
  };

  const connectDevice = async (reopen = false): Promise<void> => {
    setState("loading"); setError("");
    try { setDevice(reopen ? await api.reconnectDevice() : await api.identify()); setState(capture ? "ready" : "empty"); }
    catch (caught) { setDevice(null); setError(messageFor(caught)); setState(caught instanceof TypeError ? "disconnected" : "error"); }
  };

  const captureLive = async (): Promise<void> => {
    const ids = parseChannelIds(liveChannels); const rate = Number(liveRate); const pre = Number(livePre); const post = Number(livePost); const trigger = Number(liveTrigger); const timeout = Number(liveTimeout);
    if (!device || ids === null || !ids.includes(trigger) || ![rate, pre, post, trigger, timeout].every(Number.isFinite)) { setError("Enter a valid ordered live capture configuration."); setState("error"); return; }
    setState("loading"); setError(""); setBusPage(null); setOperationKind("live");
    try {
      let current = await api.liveCapture({ sample_rate_hz: rate, pre_trigger_samples: pre, post_trigger_samples: post, trigger_channel: trigger, trigger_edge: liveEdge, channel_ids: ids, timeout_seconds: timeout }); setOperation(current);
      for (let attempt = 0; attempt < 320 && ["pending", "running", "cancelling"].includes(current.state); attempt += 1) { await new Promise((resolve) => globalThis.setTimeout(resolve, 100)); current = await api.operation(current.operation_id); setOperation(current); }
      if (current.state === "cancelled") { setState(capture ? "ready" : "empty"); return; }
      if (current.state !== "succeeded" || !current.capture_id) throw new Error("live capture failed");
      await loadCapture(current.capture_id);
    } catch (caught) { setError(messageFor(caught)); setState(caught instanceof TypeError ? "disconnected" : "error"); }
  };

  const cancel = async (): Promise<void> => {
    if (!operation || !["pending", "running"].includes(operation.state)) return;
    setState("cancelling");
    try { setOperation(await api.cancel(operation.operation_id)); }
    catch (caught) { setError(messageFor(caught)); setState("error"); }
  };

  useEffect(() => {
    if (!capture || !visible.length || state !== "ready") return;
    waveAbort.current?.abort(); const controller = new AbortController(); waveAbort.current = controller;
    const start = Math.max(0, Math.floor(view.start)); const end = Math.min(capture.sample_count, Math.max(start + 1, Math.ceil(view.end)));
    void api.waveform(capture.capture_id, start, end, visible, view.pixels, controller.signal).then((data) => {
      const segments = planWaveform(data.channels, data.start, data.end, view.pixels);
      if (canvas.current) {
        canvas.current.dataset.commands = String(drawWaveform(canvas.current, segments, visible.length, globalThis.devicePixelRatio || 1, triggerMarker(capture.trigger_index, data.start, data.end, view.pixels)));
        canvas.current.dataset.renderedWindow = `${data.start}:${data.end}`;
        canvas.current.dataset.transitionCount = String(data.channels.reduce((total, channel) => total + channel.transitions.length, 0));
      }
    }).catch((caught: unknown) => { if ((caught as Error).name !== "AbortError") { setError(messageFor(caught)); setState("disconnected"); } });
    return () => controller.abort();
  }, [capture, state, view, visible]);

  useEffect(() => {
    if (!capture || !visible.length || state !== "ready") { setCursorWave(null); return; }
    const controller = new AbortController();
    const timer = globalThis.setTimeout(() => {
      void api.waveform(capture.capture_id, cursor, cursor + 1, visible, 1, controller.signal).then(setCursorWave).catch((caught: unknown) => {
        if ((caught as Error).name !== "AbortError") setCursorWave(null);
      });
    }, 120);
    return () => { globalThis.clearTimeout(timer); controller.abort(); };
  }, [capture, cursor, state, visible]);

  const cursorValues = useMemo(() => channels.filter((channel) => visible.includes(channel.channel_id)).map((channel) => ({
    label: channel.label,
    value: valueAt(cursorWave?.channels.find((item) => item.channel_id === channel.channel_id)?.transitions ?? [], cursor),
  })), [channels, cursor, cursorWave, visible]);

  const busRequest = useCallback((offset: number): BusRequest | null => {
    const ids = busChannels.filter((id) => busMode === "transition" || id !== strobe);
    if (!ids.length || (busMode === "sampled" && (strobe === null || ids.includes(strobe)))) return null;
    return { mode: busMode, channel_ids: ids, strobe_channel: busMode === "sampled" ? strobe : null, edge: busMode === "sampled" ? busEdge : null, offset, limit: PAGE_SIZE };
  }, [busChannels, busEdge, busMode, strobe]);

  const analyze = async (offset = 0): Promise<void> => {
    if (!capture) return; const request = busRequest(offset);
    if (!request) { setError("Choose data channels and a distinct strobe channel."); return; }
    try { const page = await api.bus(capture.capture_id, request); setBusPage(page); setBusOffset(offset); setError(""); }
    catch (caught) { setError(messageFor(caught)); }
  };

  const exportBus = async (): Promise<void> => {
    if (!capture) return; const request = busRequest(0); if (!request) { setError("Choose a valid bus configuration."); return; }
    try {
      const response = await api.export(capture.capture_id, { format: request.mode === "transition" ? "bus-transition-csv" : "bus-sampled-csv", channel_ids: request.channel_ids, strobe_channel: request.strobe_channel, edge: request.edge });
      const href = URL.createObjectURL(await response.blob()); const link = document.createElement("a"); link.href = href; link.download = "pico-la-bus.csv"; link.rel = "noopener"; link.click(); globalThis.setTimeout(() => URL.revokeObjectURL(href), 0);
    } catch (caught) { setError(messageFor(caught)); }
  };

  const reconnect = async (): Promise<void> => {
    setState("loading"); setError("");
    try { await api.health(); if (capture) await loadCapture(capture.capture_id); else setState("empty"); }
    catch (caught) { setError(messageFor(caught)); setState("disconnected"); }
  };

  const shutdown = async (): Promise<void> => {
    pollAbort.current?.abort(); waveAbort.current?.abort();
    try { await api.shutdown(); setState("shutdown"); setCapture(null); setCursorWave(null); }
    catch (caught) { setError(messageFor(caught)); setState("disconnected"); }
  };

  const setCursorFromX = (x: number): void => setCursor(sampleAtPixel(view, Math.max(0, Math.min(view.pixels, x))));
  const zoom = (factor: number, center = cursor): void => { if (capture) setView((current) => zoomAt(current, center, factor, capture.sample_count, MAX_WINDOW)); };

  return <main>
    <header><h1>Pico Logic Analyzer</h1><p className={`state state-${state}`} role="status">{state}</p></header>
    {error && <p role="alert">{error}</p>}
    <section aria-labelledby="live-heading"><h2 id="live-heading">Live device</h2>
      <p>{device ? `Connected: ${device.channel_count} channels, ${device.buffer_size} byte buffer` : "No live device connected."}</p>
      <button disabled={state === "loading" || state === "cancelling"} onClick={() => void connectDevice(false)}>Identify device</button>
      <button disabled={!device || state === "loading" || state === "cancelling"} onClick={() => void connectDevice(true)}>Reopen device</button>
      {device && <fieldset><legend>Live capture</legend>
        <label>Ordered physical channels <input aria-label="Live channel IDs" value={liveChannels} onChange={(event) => setLiveChannels(event.target.value)} /></label>
        <button type="button" onClick={() => setLiveChannels(Array.from({ length: 8 }, (_, index) => index).join(","))}>8 channels</button><button type="button" onClick={() => setLiveChannels(Array.from({ length: 16 }, (_, index) => index).join(","))}>16 channels</button><button type="button" onClick={() => setLiveChannels(Array.from({ length: 24 }, (_, index) => index).join(","))}>24 channels</button>
        <label>Sample rate (Hz) <input aria-label="Live sample rate" value={liveRate} onChange={(event) => setLiveRate(event.target.value)} /></label>
        <label>Pre-trigger samples <input aria-label="Live pre-trigger samples" value={livePre} onChange={(event) => setLivePre(event.target.value)} /></label>
        <label>Post-trigger samples <input aria-label="Live post-trigger samples" value={livePost} onChange={(event) => setLivePost(event.target.value)} /></label>
        <label>Trigger channel <input aria-label="Live trigger channel" value={liveTrigger} onChange={(event) => setLiveTrigger(event.target.value)} /></label>
        <label>Trigger edge <select aria-label="Live trigger edge" value={liveEdge} onChange={(event) => setLiveEdge(event.target.value as "rising" | "falling")}><option value="rising">rising</option><option value="falling">falling</option></select></label>
        <label>Timeout (seconds) <input aria-label="Live timeout" value={liveTimeout} onChange={(event) => setLiveTimeout(event.target.value)} /></label>
        <button disabled={state === "loading" || state === "cancelling"} onClick={() => void captureLive()}>Capture live</button>
      </fieldset>}
    </section>
    <section aria-labelledby="import-heading"><h2 id="import-heading">Open capture</h2>
      <label>Replay or CSV <input aria-label="Import capture" type="file" accept=".npz,.csv,application/x-pico-la-replay,text/csv" onChange={(event) => { setFile(event.target.files?.[0] ?? null); setError(""); }} /></label>
      {csv && <fieldset><legend>CSV import metadata</legend>
        <label>Physical channels <input aria-label="Physical channel IDs" value={channelText} onChange={(event) => setChannelText(event.target.value)} /></label>
        <label>Sample rate (Hz) <input aria-label="Sample rate" inputMode="numeric" value={sampleRate} onChange={(event) => setSampleRate(event.target.value)} /></label>
        <label>Trigger channel <input aria-label="Trigger channel" inputMode="numeric" value={triggerChannel} onChange={(event) => setTriggerChannel(event.target.value)} /></label>
        <label>Trigger edge <select aria-label="Trigger edge" value={triggerEdge} onChange={(event) => setTriggerEdge(event.target.value as "rising" | "falling")}><option value="rising">rising</option><option value="falling">falling</option></select></label>
        <output aria-label="Packed mapping">{parsedIds ? parsedIds.map((id, index) => `D${id}→bit${index}`).join(", ") : "Invalid mapping"}</output>
      </fieldset>}
      <button disabled={!file || !metadataValid || state === "loading" || state === "cancelling"} onClick={() => void open()}>Open</button>
      {operation && ["pending", "running"].includes(operation.state) && <button onClick={() => void cancel()}>{operationKind === "live" ? "Cancel live capture" : "Cancel import"}</button>}
    </section>
    {capture && state === "ready" && <>
      <section aria-labelledby="channels-heading"><h2 id="channels-heading">Channels</h2><p>{capture.sample_count} samples at {capture.sample_rate_hz} Hz; trigger sample {capture.trigger_index}</p>
        <div className="channel-controls">{channels.map((channel) => <label key={channel.channel_id}><input type="checkbox" checked={visible.includes(channel.channel_id)} onChange={() => setVisible((ids) => ids.includes(channel.channel_id) ? ids.filter((id) => id !== channel.channel_id) : channels.filter((item) => [...ids, channel.channel_id].includes(item.channel_id)).map((item) => item.channel_id))} />{channel.label} <small>D{channel.channel_id}/bit{channel.packed_position}</small></label>)}</div>
      </section>
      <section aria-label="waveform" className="waveform" tabIndex={0}
        onKeyDown={(event) => { if (!capture) return; const step = Math.max(1, Math.round((view.end - view.start) / 10)); if (event.key === "ArrowRight") setView((current) => pan(current, step, capture.sample_count)); if (event.key === "ArrowLeft") setView((current) => pan(current, -step, capture.sample_count)); if (["+", "="].includes(event.key)) zoom(1.25); if (event.key === "-") zoom(0.8); }}
        onWheel={(event) => { event.preventDefault(); const rectangle = event.currentTarget.getBoundingClientRect(); const center = sampleAtPixel(view, ((event.clientX - rectangle.left) / Math.max(1, rectangle.width)) * view.pixels); setCursor(center); zoom(event.deltaY < 0 ? 1.25 : 0.8, center); }}
        onPointerDown={(event) => { drag.current = { x: event.clientX, view }; event.currentTarget.setPointerCapture(event.pointerId); }}
        onPointerMove={(event) => { const rectangle = event.currentTarget.getBoundingClientRect(); setCursorFromX(((event.clientX - rectangle.left) / Math.max(1, rectangle.width)) * view.pixels); if (drag.current && capture) { const samplesPerPixel = (drag.current.view.end - drag.current.view.start) / view.pixels; setView(pan(drag.current.view, Math.round((drag.current.x - event.clientX) * samplesPerPixel), capture.sample_count)); } }}
        onPointerUp={(event) => { drag.current = null; event.currentTarget.releasePointerCapture(event.pointerId); }} onPointerCancel={() => { drag.current = null; }}>
        <h2>Waveform</h2><canvas ref={canvas} width={CANVAS_PIXELS} height={Math.max(1, visible.length) * 28} aria-label="Digital waveform" />
        {!visible.length && <p>No channels are visible.</p>}
        <output aria-label="Viewport">samples {view.start}–{view.end - 1}</output>
        <p><strong>Cursor:</strong> sample {cursor}; trigger-relative time {((cursor - capture.trigger_index) / capture.sample_rate_hz).toPrecision(8)} s</p>
        <ul aria-label="Cursor channel values">{cursorValues.map((item) => <li key={item.label}>{item.label}: {item.value}</li>)}</ul>
      </section>
      <section aria-labelledby="bus-heading"><h2 id="bus-heading">Parallel bus</h2>
        <label>Mode <select aria-label="Bus mode" value={busMode} onChange={(event) => { setBusMode(event.target.value as BusMode); setBusPage(null); }}><option value="transition">transition</option><option value="sampled">distinct strobe</option></select></label>
        <fieldset><legend>Ordered data channels (LSB first)</legend>{channels.map((channel) => <label key={channel.channel_id}><input type="checkbox" checked={busChannels.includes(channel.channel_id)} disabled={busMode === "sampled" && strobe === channel.channel_id} onChange={() => setBusChannels((ids) => ids.includes(channel.channel_id) ? ids.filter((id) => id !== channel.channel_id) : [...ids, channel.channel_id])} />{channel.label}</label>)}</fieldset>
        {busMode === "sampled" && <><label>Strobe <select aria-label="Strobe channel" value={strobe ?? ""} onChange={(event) => { const id = Number(event.target.value); setStrobe(id); setBusChannels((ids) => ids.filter((item) => item !== id)); }}>{channels.map((channel) => <option key={channel.channel_id} value={channel.channel_id}>{channel.label}</option>)}</select></label><label>Edge <select aria-label="Bus edge" value={busEdge} onChange={(event) => setBusEdge(event.target.value as "rising" | "falling")}><option value="rising">rising</option><option value="falling">falling</option></select></label></>}
        <button onClick={() => void analyze(0)}>Analyze bus</button><button onClick={() => void exportBus()}>Export CSV</button>
        {busPage && <><p>{busPage.total ? `${busPage.offset + 1}–${busPage.offset + busPage.rows.length} of ${busPage.total}` : "No bus rows"}</p><table><caption>Bus rows</caption><thead><tr><th>Sample</th><th>Time (s)</th><th>Binary</th><th>Hex</th><th>Decimal</th><th>End sample</th><th>Duration (s)</th></tr></thead><tbody>{busPage.rows.map((row, index) => <tr key={`${row.sample_index}-${index}`}><td>{row.sample_index}</td><td>{row.time_seconds}</td><td>{row.binary}</td><td>{row.hexadecimal}</td><td>{row.decimal}</td><td>{row.end_sample_index ?? "—"}</td><td>{row.duration_seconds ?? "—"}</td></tr>)}</tbody></table><nav aria-label="Bus pagination"><button disabled={busOffset === 0} onClick={() => void analyze(Math.max(0, busOffset - PAGE_SIZE))}>Previous</button><button disabled={busPage.next_offset === null} onClick={() => void analyze(busPage.next_offset ?? busOffset)}>Next</button></nav></>}
      </section>
    </>}
    <footer><button disabled={state === "shutdown"} onClick={() => void reconnect()}>Reconnect</button><button disabled={state === "shutdown"} onClick={() => void shutdown()}>Shut down server</button></footer>
  </main>;
}

if (typeof document !== "undefined") {
  createRoot(document.getElementById("root")!).render(<React.StrictMode><App /></React.StrictMode>);
}
