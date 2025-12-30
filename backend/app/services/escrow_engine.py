from app.intelligence.fraud import predict_fraud
from app.intelligence.trust_score import update_trust_score

def process_escrow(escrow, user, db):
    fraud_score = predict_fraud(user, escrow)

    update_trust_score(user, fraud_score)

    if fraud_score >= 70:
        escrow.status = "blocked"
        escrow.requires_admin = True
    else:
        escrow.status = "released"

    db.commit()
    return fraud_score
