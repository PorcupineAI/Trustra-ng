import { useState } from "react";
import { setToken } from "../lib/auth";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function submit() {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_BASE}/auth/login`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
      }
    );
    const data = await res.json();
    setToken(data.access_token);
    window.location.href = "/dashboard";
  }

  return (
    <div>
      <h1>Login</h1>
      <input placeholder="Email" onChange={e => setEmail(e.target.value)} />
      <input type="password" placeholder="Password"
             onChange={e => setPassword(e.target.value)} />
      <button onClick={submit}>Login</button>
    </div>
  );
}
