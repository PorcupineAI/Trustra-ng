from fastapi import APIRouter
from app.services.monetization import escrow_fee

router = APIRouter()

@router.post("/create")
def create(amount: float):
    fee = escrow_fee(amount)
    return {"amount": amount, "fee": fee}
