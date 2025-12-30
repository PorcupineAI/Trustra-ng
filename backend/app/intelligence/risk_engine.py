def risk_level(trust_score: int, flags: list):
    if trust_score < 30 or "verification_abuse" in flags:
        return "HIGH"
    if trust_score < 60:
        return "MEDIUM"
    return "LOW"
