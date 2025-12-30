def calculate_trust_score(user):
    score = 50  # neutral base

    if user.is_verified:
        score += 20

    if user.successful_transactions > 5:
        score += 20

    if user.disputes > 0:
        score -= 30

    return max(0, min(score, 100))
