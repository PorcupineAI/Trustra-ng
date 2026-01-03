from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def dashboard():
    return {
        "users": 120,
        "escrow_volume": 4000000,
        "risk_level": "low"
    }
