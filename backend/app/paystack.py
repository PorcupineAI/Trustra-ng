import requests
from app.config import PAYSTACK_SECRET

HEADERS = {"Authorization": f"Bearer {PAYSTACK_SECRET}"}

def init_payment(email, amount):
    return requests.post(
        "https://api.paystack.co/transaction/initialize",
        headers=HEADERS,
        json={"email": email, "amount": amount}
    ).json()
