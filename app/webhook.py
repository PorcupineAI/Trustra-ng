from fastapi import APIRouter, Request
from app.verifier import handle_verify
from app.escrow import handle_escrow

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(request: Request):
    payload = await request.json()

    try:
        message = payload["entry"][0]["changes"][0]["value"]["messages"][0]
        text = message["text"]["body"].strip().upper()
        sender = message["from"]
    except Exception:
        return {"status": "ignored"}

    if text.startswith("VERIFY"):
        return handle_verify(text, sender)

    if text.startswith("ESCROW"):
        return handle_escrow(text, sender)

    return {
        "reply": (
            "Welcome to TRUSTRA™\n\n"
            "Commands:\n"
            "VERIFY 080XXXXXXXX\n"
            "ESCROW START\n"
        )
    }
