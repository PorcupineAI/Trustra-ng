def enforce_payment(user, action):
    if action == "register" and not user.paid:
        raise Exception("Payment required")
    if action == "verify" and not user.verified:
        raise Exception("Verification fee required")

