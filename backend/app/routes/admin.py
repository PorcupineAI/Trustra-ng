from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.escrow import Escrow

router = APIRouter(prefix="/admin", tags=["Admin"])

def admin_only(user=Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin only")
    return user

@router.get("/users")
def list_users(db: Session = Depends(get_db), admin=Depends(admin_only)):
    return db.query(User).all()

@router.get("/escrows")
def list_escrows(db: Session = Depends(get_db), admin=Depends(admin_only)):
    return db.query(Escrow).all()

@router.post("/flag-user/{user_id}")
def flag_user(user_id: int, db: Session = Depends(get_db), admin=Depends(admin_only)):
    user = db.query(User).get(user_id)
    user.flagged = True
    db.commit()
    return {"status": "flagged"}
