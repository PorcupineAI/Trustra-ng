from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.escrow import Escrow
from app.services.escrow_engine import process_escrow

router = APIRouter(prefix="/escrow")

@router.post("/release/{escrow_id}")
def release_escrow(escrow_id: int, db: Session = Depends(get_db)):
    escrow = db.query(Escrow).get(escrow_id)
    user = escrow.user

    fraud_score = process_escrow(escrow, user, db)

    return {
        "status": escrow.status,
        "fraud_score": fraud_score
    }
