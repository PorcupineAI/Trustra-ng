def handle_verify(text: str, sender: str):
    parts = text.split()

    if len(parts) != 2:
        return {
            "reply": "Usage:\nVERIFY 080XXXXXXXX"
        }

    phone = parts[1]

    # 🔐 MOCK TRUST SCORE (we will replace later)
    trust_score = 82
    status = "Trusted Seller"

    return {
        "reply": (
            f"TRUSTRA™ VERIFICATION RESULT\n\n"
            f"Phone: {phone}\n"
            f"Trust Score: {trust_score}/100\n"
            f"Status: {status}\n\n"
            f"Tip: Use ESCROW for safe transactions."
        )
    }
