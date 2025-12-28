def calculate_trust_score(user):
    score = 50  # neutral baseline

    if user.is_verified:
        score += 20

    if user.completed_escrows > 5:
        score += 10

    if user.disputes > 0:
        score -= user.disputes * 15

    return max(0, min(score, 100))
