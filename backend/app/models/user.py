from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True)
    role = Column(String)  # buyer / seller
    trust_score = Column(Integer, default=50)
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
