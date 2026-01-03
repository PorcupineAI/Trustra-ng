from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.escrow import Escrow
from app.models.user import User
from app.services.monetization import escrow_fee

router = APIRouter(prefix="/escrow", tags=["escrow"])

@router.post("/create")
def create_escrow(
    buyer_id: int,
    seller_id: int,
    amount: float,
    db: Session = Depends(get_db)
):
    # Validate users exist
    buyer = db.query(User).filter(User.id == buyer_id).first()
    seller = db.query(User).filter(User.id == seller_id).first()
    
    if not buyer or not seller:
        raise HTTPException(400, "Buyer or seller not found")
    
    if amount <= 0:
        raise HTTPException(400, "Amount must be positive")
    
    # Calculate fee
    fee = escrow_fee(amount)
    
    # Create escrow
    escrow = Escrow(
        buyer_id=buyer_id,
        seller_id=seller_id,
        amount=amount,
        fee=fee
    )
    
    db.add(escrow)
    db.commit()
    db.refresh(escrow)
    
    return {
        "status": "success",
        "message": "Escrow created",
        "escrow_id": escrow.id,
        "amount": amount,
        "fee": fee,
        "total": amount + fee
    }

@router.get("/{escrow_id}")
def get_escrow(escrow_id: int, db: Session = Depends(get_db)):
    escrow = db.query(Escrow).filter(Escrow.id == escrow_id).first()
    
    if not escrow:
        raise HTTPException(404, "Escrow not found")
    
    return escrow

@router.get("/")
def list_escrows(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    escrows = db.query(Escrow).offset(skip).limit(limit).all()
    return escrows
