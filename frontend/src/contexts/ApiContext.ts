import { createContext } from "react";
import ApiClient from "../lib/api/index";

export const ApiContext = createContext<{ client: ApiClient | null }>({
  client: null,
});
