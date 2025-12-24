def create_escrow(amount):
    fee = int(amount * 0.018)
    return {
        "amount": amount,
        "fee": fee,
        "net": amount - fee,
        "status": "HELD"
    }

