import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App(): React.JSX.Element {
  return <main><h1>Pico Logic Analyzer</h1><p>Offline web shell ready.</p></main>;
}

createRoot(document.getElementById("root")!).render(<React.StrictMode><App /></React.StrictMode>);
