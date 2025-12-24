@app.post("/webhook/paystack")
def paystack_webhook(payload):
    if payload["event"] == "charge.success":
        mark_user_as_paid(payload["data"]["metadata"])
