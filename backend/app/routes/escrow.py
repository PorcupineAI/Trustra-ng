from fastapi import APIRouter
from app.services.monetization import escrow_fee

router = APIRouter()

@router.get("/dashboard")
def dashboard_summary():
    return {
        "total_users": 124,
        "active_escrows": 17,
        "revenue_today": 35200,
        "escrow_fee_example": escrow_fee(100000)
    }
