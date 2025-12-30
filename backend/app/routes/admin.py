from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.escrow import Escrow

router = APIRouter(prefix="/admin")

@router.get("/risk")
def risk_dashboard(db: Session = Depends(get_db)):
    flagged = db.query(Escrow).filter(Escrow.requires_admin == True).all()
    return flagged

@router.post("/resolve/{escrow_id}")
def resolve_escrow(escrow_id: int, approve: bool, db: Session = Depends(get_db)):
    escrow = db.query(Escrow).get(escrow_id)
    escrow.status = "released" if approve else "rejected"
    escrow.requires_admin = False
    db.commit()
    return {"status": escrow.status}
