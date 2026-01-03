#!/bin/bash

echo "🧪 Testing setup..."
python --version
pip --version

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🔧 Setting up database..."
# Create tables directly if Alembic fails
python -c "
from app.database import engine, Base
from app.models import user, escrow, revenue, playing_with_neon, dispute, risk_log
Base.metadata.create_all(bind=engine)
print('✅ Database tables created')
"

echo "🚀 Starting server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
