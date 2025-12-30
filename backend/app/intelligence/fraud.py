def predict_fraud(user, escrow):
    score = 0

    if user.trust_score < 40:
        score += 30

    if escrow.amount > 1_000_000:
        score += 25

    if escrow.is_disputed:
        score += 20

    if user.failed_transactions > 3:
        score += 25

    return min(score, 100)
