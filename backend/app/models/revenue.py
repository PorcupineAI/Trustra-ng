from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Revenue(Base):
    __tablename__ = "revenues"

    id = Column(Integer, primary_key=True)
    escrow_id = Column(Integer)
    fee = Column(Float)
    source = Column(String)  # escrow | verification
    created_at = Column(DateTime(timezone=True), server_default=func.now())

