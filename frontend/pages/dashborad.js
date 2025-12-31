// frontend/pages/dashboard.js
import React, { useEffect, useState } from "react";

export default function Dashboard() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("/").then(res => res.json()).then(data => setMessage(data.message));
  }, []);

  return (
    <div>
      <h1>Trustra-NG Dashboard</h1>
      <p>{message}</p>
    </div>
  );
}
