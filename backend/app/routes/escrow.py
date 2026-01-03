from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.escrow import Escrow
from app.services.escrow_logic import can_release_escrow

router = APIRouter(prefix="/escrow", tags=["Escrow"])

@router.post("/release/{escrow_id}")
def release_escrow(escrow_id: int, db: Session = Depends(get_db)):
    escrow = db.query(Escrow).get(escrow_id)
    if not escrow:
        raise HTTPException(404)

    if not can_release_escrow(escrow.amount):
        raise HTTPException(403, "Fraud suspected")

    escrow.status = "released"
    db.commit()
    return {"status": "released"}
