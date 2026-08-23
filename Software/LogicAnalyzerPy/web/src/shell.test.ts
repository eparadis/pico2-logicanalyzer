import React from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { expect, test } from "vitest";
import { App } from "./main";

test("offline component exposes bounded empty, import, reconnect, and shutdown controls", () => {
  const markup = renderToStaticMarkup(React.createElement(App));
  expect(markup).toContain("Pico Logic Analyzer");
  expect(markup).toContain("state state-empty");
  expect(markup).toContain("Import capture");
  expect(markup).toContain("Reconnect");
  expect(markup).toContain("Shut down server");
  expect(markup).not.toContain("pico_la_capability");
});
