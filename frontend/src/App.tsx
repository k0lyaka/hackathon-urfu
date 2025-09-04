import { Route, Routes } from "react-router-dom";
import { ApiContext } from "./contexts/ApiContext";
import { useRawLaunchParams } from "@telegram-apps/sdk-react";
import { useEffect, useState } from "react";
import ApiClient, { defaultBaseUrl } from "./lib/api";
import Form from "./pages/Form";
import Specializations from "./pages/Specialization";
import { Toaster } from "./components/ui/sonner";

function App() {
  const [api, setApi] = useState<ApiClient | null>(null);
  const launchParams = useRawLaunchParams();

  useEffect(() => {
    if (api) return;

    const qs = new URLSearchParams(launchParams);
    const token = btoa(qs.get("tgWebAppData")!);
    setApi(new ApiClient(defaultBaseUrl, token));
  }, [launchParams, api]);

  return (
    <ApiContext.Provider value={{ client: api }}>
      <Routes>
        <Route path="/form" element={<Form />} />
        <Route path="/specializations" element={<Specializations />} />
      </Routes>

      <Toaster position={"top-center"} />
    </ApiContext.Provider>
  );
}

export default App;
