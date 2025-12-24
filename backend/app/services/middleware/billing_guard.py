def require_payment(user, action):
    if user.paid:
        return True

    if action == "register":
        raise Exception("Payment required to register")

    if action == "verification":
        raise Exception("Verification fee required")
