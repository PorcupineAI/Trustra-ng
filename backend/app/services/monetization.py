FREE_SELLERS = 1000
FREE_BUYERS = 500

def calculate_fee(amount):
    return min(amount * 0.02, 3000)

