def verify_user(user, db):
    if not is_free_slot(user.role, db):
        charge(user.phone, verification_fee())
    user.verified = True
    user.trust_badge = True
