from fastapi import APIRouter

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/")
def webhook():
    return {"received": True}
