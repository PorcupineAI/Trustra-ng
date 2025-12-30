from sqlalchemy import Column, String, Integer
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    trust_score = Column(Integer)
    role = Column(String)
