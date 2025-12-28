from app.services.monetization import calculate_fee

def create_escrow(amount):
    fee = calculate_fee(amount)
    net_amount = amount - fee
    return fee, net_amount
