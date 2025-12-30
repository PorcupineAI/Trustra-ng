from fastapi import APIRouter, Depends
from app.database import get_db
from app.intelligence.trust_score import calculate_trust_score
from app.intelligence.fraud import fraud_flags

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{user_id}/trust")
def user_trust(user_id: int, db=Depends(get_db)):
    user = db.query(User).get(user_id)

    return {
        "trust_score": calculate_trust_score(user),
        "flags": fraud_flags(user)
    }
