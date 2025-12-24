from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Escrow(Base):
    __tablename__ = "escrows"

    id = Column(Integer, primary_key=True)
    buyer_phone = Column(String)
    seller_phone = Column(String)
    amount = Column(Float)
    status = Column(String)  # pending | funded | released | disputed
