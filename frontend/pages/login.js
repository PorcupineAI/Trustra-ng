import { useState } from "react";
import { setToken } from "../lib/auth";

export default function Login() {
  const [email, setEmail] = useState("");

  const login = () => {
    // TEMP token until backend auth is live
    setToken("demo-token");
    alert("Logged in (demo mode)");
  };

  return (
    <div>
      <h1>Login</h1>
      <input
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />
      <button onClick={login}>Login</button>
    </div>
  );
}
