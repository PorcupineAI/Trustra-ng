def calculate_trust_score(events):
    score = 50

    for e in events:
        if e == "successful_escrow":
            score += 5
        elif e == "dispute":
            score -= 10
        elif e == "verified":
            score += 10
        elif e == "fraud_signal":
            score -= 20

    return max(0, min(100, score))
