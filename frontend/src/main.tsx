import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./App.tsx";

import { retrieveLaunchParams } from "@telegram-apps/sdk-react";
import { init } from "./init.ts";

const root = createRoot(document.getElementById("root")!);

const launchParams = retrieveLaunchParams();
const { tgWebAppPlatform: platform } = launchParams;
const debug =
  (launchParams.tgWebAppStartParam || "").includes("platformer_debug") ||
  import.meta.env.DEV;

// Configure all application dependencies.
await init({
  debug,
  mockForMacOS: platform === "macos",
}).then(() => {
  root.render(
    <StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </StrictMode>
  );
});
