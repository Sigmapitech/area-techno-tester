import { StrictMode } from "react";

import "./style.scss"
import { Link } from "react-router";

export default function HomePage() {
  return (
    <StrictMode>
      <div className="home-page">
        <Link to="/graph">Graph page</Link>
      </div>
    </StrictMode>
  );
}
