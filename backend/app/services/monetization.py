def escrow_fee(amount: float):
    """Charge 2% capped at 3000"""
    return min(amount * 0.02, 3000)
