import { useEffect, useState } from "react";
import { fetchAPI } from "../lib/api";

export default function AdminDashboard() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchAPI("/admin/risk-dashboard").then(setUsers);
  }, []);

  return (
    <div>
      <h1>Admin Risk Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>User</th>
            <th>Trust</th>
            <th>Risk</th>
          </tr>
        </thead>
        <tbody>
          {users.map(u => (
            <tr key={u.user_id}>
              <td>{u.user_id}</td>
              <td>{u.trust_score}</td>
              <td>{u.risk}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
