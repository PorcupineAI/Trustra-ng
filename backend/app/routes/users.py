from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def list_users():
    return {"message": "Users endpoint working"}
