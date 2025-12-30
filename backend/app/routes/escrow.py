from fastapi import APIRouter, Depends, HTTPException
from decimal import Decimal
from app.services.monetization import calculate_escrow_fee
from app.database import get_db
from app.models.revenue import Revenue

router = APIRouter(prefix="/escrow", tags=["Escrow"])

@router.post("/create")
def create_escrow(amount: Decimal, db=Depends(get_db)):
    fee = calculate_escrow_fee(amount)
    net = amount - fee

    db.add(Revenue(
        source="escrow",
        amount=fee,
        reference="escrow_fee"
    ))
    db.commit()

    return {
        "amount": amount,
        "fee": fee,
        "net_held": net
    }
