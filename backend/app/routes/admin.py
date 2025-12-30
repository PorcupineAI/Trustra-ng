from fastapi import APIRouter, Depends
from app.database import get_db
from app.models.user import User
from app.intelligence.trust_score import calculate_trust_score
from app.intelligence.fraud import fraud_flags
from app.intelligence.risk_engine import risk_level

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/risk-dashboard")
def risk_dashboard(db=Depends(get_db)):
    users = db.query(User).all()
    report = []

    for u in users:
        trust = calculate_trust_score(u)
        flags = fraud_flags(u)
        report.append({
            "user_id": u.id,
            "trust_score": trust,
            "flags": flags,
            "risk": risk_level(trust, flags)
        })

    return report
