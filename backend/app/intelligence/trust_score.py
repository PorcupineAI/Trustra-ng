def calculate_trust(user):
    score = 50
    if user.verified:
        score += 20
    return min(score, 100)
