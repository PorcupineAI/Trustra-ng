import requests
from .config import BASE_URL, PHONE_NUMBER_ID, WHATSAPP_TOKEN

def send_message(to, body, buttons=None):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive" if buttons else "text",
        "text": {"body": body}
    }

    if buttons:
        payload["interactive"] = {
            "type": "button",
            "body": {"text": body},
            "action": {"buttons": buttons}
        }

    requests.post(
        f"{BASE_URL}/{PHONE_NUMBER_ID}/messages",
        headers={
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        },
        json=payload
    )

def handle_message(data):
    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
        phone = msg["from"]
        text = msg["text"]["body"].lower()

        if "verify" in text:
            send_message(phone, "Seller verified. Trust Score: 65/100")

        elif "escrow" in text:
            send_message(
                phone,
                "Use Escrow?",
                buttons=[
                    {"type":"reply","reply":{"id":"ESCROW_YES","title":"Use Escrow"}},
                    {"type":"reply","reply":{"id":"ESCROW_NO","title":"No"}}
                ]
            )
    except:
        pass
