from sqlalchemy import Column, Integer, Float
from app.services.constraints import RevenueConstraints
from app.database import Base

class Revenue(Base, RevenueConstraints):
    __tablename__ = 'revenue'
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
