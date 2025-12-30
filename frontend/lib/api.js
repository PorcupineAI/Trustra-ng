const API_BASE = process.env.NEXT_PUBLIC_API_BASE;

export async function fetchAPI(path) {
  const res = await fetch(`${API_BASE}${path}`);
  return res.json();
}
