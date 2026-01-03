def predict_fraud(amount: float) -> bool:
    if amount > 1_000_000:
        return True
    return False
