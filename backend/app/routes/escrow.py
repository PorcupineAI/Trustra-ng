from fastapi import APIRouter

router = APIRouter(prefix="/escrow", tags=["escrow"])

@router.get("/")
def escrow_status():
    return {"status": "escrow ok"}
