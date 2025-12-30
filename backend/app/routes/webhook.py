from fastapi import APIRouter, Depends
from app.services.verification import charge_verification
from app.database import get_db

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/whatsapp/verified")
def whatsapp_verified(user_id: int, db=Depends(get_db)):
    charge_verification(db, user_id)
    return {"status": "verified"}
