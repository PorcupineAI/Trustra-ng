from app.models.revenue import Revenue

VERIFICATION_FEE = 200

def charge_verification(db, user_id):
    db.add(Revenue(
        source="verification",
        amount=VERIFICATION_FEE,
        reference=f"user_{user_id}"
    ))
    db.commit()
