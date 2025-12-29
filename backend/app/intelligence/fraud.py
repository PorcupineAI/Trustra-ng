def evaluate_user(user):
    risk = 0

    if user.failed_transactions > 2:
        risk += 30

    if user.escrow_disputes > 1:
        risk += 40

    if user.account_age_days < 7:
        risk += 20

    return risk
