import { StrictMode } from "react";

import "./style.scss";
import { Link } from "react-router";
import { useAuth } from "@/auth";

export default function HomePage() {
  const { token, logout } = useAuth();

  return (
    <StrictMode>
      <div className="home-page">
        <Link to="/graph">Graph page</Link>
        <button onClick={logout}>Logout</button>
      </div>
    </StrictMode>
  );
}
