from app.intelligence.fraud import evaluate_user

def update_trust_score(user):
    risk = evaluate_user(user)
    user.trust_score = max(0, 100 - risk)
