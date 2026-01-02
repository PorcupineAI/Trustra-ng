from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    password_hash = Column(String)
    is_verified = Column(Boolean, default=False)
    trust_score = Column(Float, default=50.0)
    role = Column(String, default="user")
    trust_badge = Column(String, default="basic")
    
    # Additional fields for fraud detection
    failed_transactions = Column(Integer, default=0)
    failed_verifications = Column(Integer, default=0)
    disputes = Column(Integer, default=0)
    successful_trades = Column(Integer, default=0)
