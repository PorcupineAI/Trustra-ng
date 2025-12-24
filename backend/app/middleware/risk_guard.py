def block_high_risk(user):
    return user.trust_score < 20
