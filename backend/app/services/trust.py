def update_trust(user, event):
    rules = {
        "escrow_success": 10,
        "delivery_confirmed": 5,
        "verified": 10,
        "dispute_lost": -15,
        "late_delivery": -5,
        "fake_report": -20
    }

    delta = rules.get(event, 0)
    user.trust_score = max(0, min(100, user.trust_score + delta))

    if user.trust_score >= 80:
        user.trust_badge = "gold"
    elif user.trust_score >= 50:
        user.trust_badge = "silver"
    else:
        user.trust_badge = "basic"

    return user
