def fraud_flags(user):
    flags = []

    if user.failed_verifications > 3:
        flags.append("verification_abuse")

    if user.disputes > 2:
        flags.append("high_dispute_risk")

    return flags
