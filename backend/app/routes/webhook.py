from fastapi import APIRouter

router = APIRouter(prefix="/webhook", tags=["webhook"])

@router.post("/")
def webhook_receiver():
    return {"status": "webhook ok"}
