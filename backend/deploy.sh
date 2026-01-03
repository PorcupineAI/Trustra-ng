#!/bin/bash
set -e

echo "🚀 Trustra NG Deployment Script"
echo "================================"

# Check Python version
echo "Python version:"
python --version

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python -c "
import os
from alembic.config import Config
from alembic import command

try:
    cfg = Config('alembic.ini')
    cfg.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL', ''))
    command.upgrade(cfg, 'head')
    print('✅ Migrations completed')
except Exception as e:
    print(f'⚠️  Migrations error: {e}')
"

# Start server
echo "Starting Trustra NG server..."
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1
