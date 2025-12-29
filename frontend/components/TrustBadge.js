export default function TrustBadge({ score }) {
  if (score >= 80) return "🟢 Verified Pro";
  if (score >= 60) return "🟡 Trusted";
  return "⚪ New User";
}
