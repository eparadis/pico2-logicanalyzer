import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: "../src/pico_logic_analyzer/web/assets",
    emptyOutDir: true,
  },
  test: { exclude: ["tests/**", "node_modules/**"] },
});
