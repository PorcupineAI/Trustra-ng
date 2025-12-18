from fastapi import APIRouter, Request
from app.whatsapp import handle_message
from app.config import VERIFY_TOKEN

router = APIRouter()

@router.get("/webhook")
def verify(mode: str, challenge: str, verify_token: str):
    if verify_token == VERIFY_TOKEN:
        return int(challenge)
    return "Invalid"

@router.post("/webhook")
async def receive(req: Request):
    data = await req.json()
    handle_message(data)
    return {"ok": True}
