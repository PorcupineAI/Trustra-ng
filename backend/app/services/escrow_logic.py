from app.services.fraud_engine import predict_fraud

def can_release_escrow(amount: float) -> bool:
    return not predict_fraud(amount)
