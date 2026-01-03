from sqlalchemy import Column, Integer, Float, String
from app.database import Base

class Escrow(Base):
    __tablename__ = "escrow"

    id = Column(Integer, primary_key=True)
    payer_id = Column(Integer)
    payee_id = Column(Integer)
    amount = Column(Float)
    status = Column(String, default="locked")
