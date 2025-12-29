from fastapi import APIRouter

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/")
def hook():
    return {"received": True}
