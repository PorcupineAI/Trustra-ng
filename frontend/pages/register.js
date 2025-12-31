import { useState } from "react";
import { apiPost } from "../lib/api";

export default function Register() {
  const [phone, setPhone] = useState("");
  const [name, setName] = useState("");
  const [result, setResult] = useState(null);

  const submit = async () => {
    const data = await apiPost("/api/users/register", { phone, name });
    setResult(data);
  };

  return (
    <div>
      <h1>Register on Trustra</h1>
      <input placeholder="Phone" onChange={e => setPhone(e.target.value)} />
      <input placeholder="Name" onChange={e => setName(e.target.value)} />
      <button onClick={submit}>Register</button>

      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
