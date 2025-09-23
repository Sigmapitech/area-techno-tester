import { StrictMode, useState } from "react";

import "./style.scss";
import { Link } from "react-router";
import { useAuth } from "@/auth";

const API_BASE_URL = "http://127.0.0.1:8000";

function getPopupDimension() {
  const width = 500;
  const height = 700;
  const left = window.screenX + (window.innerWidth - width) / 2;
  const top = window.screenY + (window.innerHeight - height) / 2;

  return [width, height, left, top];
}

export default function HomePage() {
  const { token, logout } = useAuth();
  const [connected, setConnected] = useState(false);

  const connectDiscord = () => {
    const [width, height, left, top] = getPopupDimension();

    const popup = window.open(
      `${API_BASE_URL}/api/discord/connect?token=${token}`,
      "DiscordConnect",
      `width=${width},height=${height},left=${left},top=${top}`,
    );

    window.addEventListener("message", (event) => {
      if (event.origin !== API_BASE_URL) return;
      if (event.data?.type === "DISCORD_CONNECTED") {
        setConnected(true);
        console.log("Discord linked!", event.data.payload);
        popup?.close();
      }
    });
  };

  return (
    <StrictMode>
      <div className="home-page">
        <Link to="/graph">Graph page</Link>
        <button onClick={logout}>Logout</button>
        {!connected && (
          <button onClick={connectDiscord}>Connect with Discord</button>
        )}
      </div>
    </StrictMode>
  );
}
