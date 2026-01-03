from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Escrow(Base):
    __tablename__ = "escrow"
    
    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    seller_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float, nullable=False)
    fee = Column(Float, default=0.0)
    status = Column(String, default="pending")
    is_disputed = Column(Boolean, default=False)
    requires_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Escrow(id={self.id}, amount={self.amount}, status={self.status})>"
