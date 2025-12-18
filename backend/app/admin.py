from fastapi import APIRouter

router = APIRouter(prefix="/admin")

@router.get("/health")
def admin_health():
    return {"admin": "ok"}
