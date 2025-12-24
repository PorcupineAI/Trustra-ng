from sqlalchemy import Column, Integer, String
from app.database import Base

class Dispute(Base):
    __tablename__ = "disputes"

    id = Column(Integer, primary_key=True)
    escrow_id = Column(Integer)
    status = Column(String)
