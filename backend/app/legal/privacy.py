from fastapi import APIRouter

router = APIRouter()

@router.get("/privacy")
def privacy():
    return {"privacy": "User data is protected under NDPR."}
