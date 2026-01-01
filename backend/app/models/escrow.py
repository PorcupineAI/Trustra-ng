from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db.base import Base

class Escrow(Base):
    __tablename__ = "escrow"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer)
    seller_id = Column(Integer)
    amount = Column(Float)
