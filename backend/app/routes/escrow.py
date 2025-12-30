from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.models.escrow import Escrow
from app.services.escrow import release_escrow

router = APIRouter(prefix="/escrow", tags=["Escrow"])

@router.post("/{escrow_id}/dispute")
def dispute_escrow(escrow_id: int, db=Depends(get_db)):
    escrow = db.query(Escrow).get(escrow_id)
    escrow.status = "DISPUTED"
    db.commit()
    return {"status": "DISPUTED"}

@router.post("/{escrow_id}/arbitrate")
def arbitrate(escrow_id: int, decision: str, db=Depends(get_db)):
    escrow = db.query(Escrow).get(escrow_id)
    release_escrow(escrow, decision)
    db.commit()
    return {"final_status": escrow.status}
