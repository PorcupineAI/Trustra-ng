def calculate_trust_score(user):
    score = 50

    score += min(user.successful_trades * 2, 30)
    score -= min(user.disputes * 5, 40)

    if user.verified:
        score += 10

    return max(0, min(100, score))
