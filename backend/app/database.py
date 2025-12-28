from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    from app.models.user import User
    from app.models.escrow import Escrow
    from app.models.revenue import Revenue

    Base.metadata.create_all(bind=engine)
