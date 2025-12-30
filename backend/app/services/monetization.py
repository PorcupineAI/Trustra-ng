from decimal import Decimal

ESCROW_PERCENT = Decimal("0.02")
ESCROW_CAP = Decimal("3000")

def calculate_escrow_fee(amount: Decimal) -> Decimal:
    fee = amount * ESCROW_PERCENT
    return min(fee, ESCROW_CAP)
