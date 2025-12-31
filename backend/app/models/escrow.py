from sqlalchemy import Column, Integer, Float, ForeignKey
from app.services.constraints import EscrowConstraints
from app.database import Base

class Escrow(Base, EscrowConstraints):
    __tablename__ = 'escrow'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
