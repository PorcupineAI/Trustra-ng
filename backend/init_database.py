"""
Alternative initialization script.
Use Alembic for production, this for development only.
"""
from app.database import engine, Base
from app.models import (
    User, 
    Escrow, 
    Revenue, 
    PlayingWithNeon, 
    Dispute, 
    RiskLog
)

def init_db():
    """Initialize database tables."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created!")

if __name__ == "__main__":
    init_db()
