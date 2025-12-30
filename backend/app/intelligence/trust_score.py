def update_trust_score(user, fraud_score):
    if fraud_score > 70:
        user.trust_score -= 10
    elif fraud_score < 30:
        user.trust_score += 5

    user.trust_score = max(0, min(user.trust_score, 100))
