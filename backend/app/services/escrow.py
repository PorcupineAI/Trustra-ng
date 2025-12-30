def release_escrow(escrow, decision=None):
    if escrow.status == "DISPUTED" and decision:
        escrow.status = decision  # RELEASE_BUYER / RELEASE_SELLER
    elif escrow.status == "HELD":
        escrow.status = "RELEASE_SELLER"
    return escrow
