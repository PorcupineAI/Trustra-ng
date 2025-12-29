import { useEffect, useState } from "react";

export default function AdminDashboard() {
  const [users, setUsers] = useState([]);
  const [escrows, setEscrows] = useState([]);

  useEffect(() => {
    fetch("/api/admin/users").then(res => res.json()).then(setUsers);
    fetch("/api/admin/escrows").then(res => res.json()).then(setEscrows);
  }, []);

  return (
    <div>
      <h1>Trustra Admin</h1>

      <h2>Users</h2>
      {users.map(u => (
        <div key={u.id}>
          {u.email} — Trust: {u.trust_score}
        </div>
      ))}

      <h2>Escrows</h2>
      {escrows.map(e => (
        <div key={e.id}>
          ₦{e.amount} — {e.status}
        </div>
      ))}
    </div>
  );
}
