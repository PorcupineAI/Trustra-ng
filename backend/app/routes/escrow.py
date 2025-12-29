from fastapi import APIRouter
from app.services.monetization import escrow_fee

router = APIRouter(prefix="/escrow", tags=["Escrow"])

@router.post("/fee")
def fee(amount: int):
    return {"fee": escrow_fee(amount)}
