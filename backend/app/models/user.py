from sqlalchemy import Column, Integer, String
from app.services.constraints import UserConstraints
from app.database import Base

class User(Base, UserConstraints):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(20), nullable=False)
    name = Column(String(100), nullable=True)
