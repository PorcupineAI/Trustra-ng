from sqlalchemy import Column, Integer, Float
from app.database import Base

class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
