def predict_fraud_probability(user):
    score = 0.0

    if user.failed_verifications > 2:
        score += 0.4

    if user.disputes > 1:
        score += 0.3

    if not user.is_verified:
        score += 0.2

    return min(score, 1.0)
