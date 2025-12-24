@app.post("/webhook/paystack")
def paystack_webhook(payload):
    if payload["event"] == "charge.success":
        unlock_user(payload["data"]["metadata"])
