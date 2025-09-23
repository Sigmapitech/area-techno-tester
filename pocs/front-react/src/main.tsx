import { createRoot } from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router";

import "./index.scss";

import GraphPage from "./routes/graph";
import HomePage from "./routes/home";
import LoginPage from "./routes/login";

createRoot(document.getElementById("root")!).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/graph" element={<GraphPage />} />
      <Route path="/login" element={<LoginPage />} />
    </Routes>
  </BrowserRouter>,
);
