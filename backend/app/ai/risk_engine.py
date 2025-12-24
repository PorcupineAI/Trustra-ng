def risk_level(user):
    if user.disputes >= 3:
        return "HIGH"
    if user.trust_score < 30:
        return "MEDIUM"
    return "LOW"
