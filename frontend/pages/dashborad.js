import { getToken } from "../lib/auth";
import { useEffect } from "react";

export default function Dashboard() {
  useEffect(() => {
    if (!getToken()) window.location.href = "/login";
  }, []);

  return <h1>Welcome to Trustra Dashboard</h1>;
}
