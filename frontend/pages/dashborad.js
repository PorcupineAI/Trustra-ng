import { useEffect, useState } from "react";
import { getToken } from "../lib/auth";

export default function Dashboard() {
  useEffect(() => {
    if (!getToken()) location.href = "/login";
  }, []);

  return <h1>User Escrow Dashboard</h1>;
}
