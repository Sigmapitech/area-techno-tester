import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";

import './index.scss'

import HomePage from './routes/home';
import GraphPage from './routes/graph';

createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/graph" element={<GraphPage />} />
    </Routes>
  </BrowserRouter>,
)
