# Use specific Python 3.11 version
FROM python:3.11.9-slim-bullseye

WORKDIR /app

# Install ONLY essential system deps (no Rust)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements FIRST for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip

# Install packages one by one to avoid conflicts
RUN pip install --no-cache-dir fastapi==0.104.1
RUN pip install --no-cache-dir uvicorn[standard]==0.24.0
RUN pip install --no-cache-dir sqlalchemy==2.0.23
RUN pip install --no-cache-dir psycopg2-binary==2.9.9
RUN pip install --no-cache-dir python-dotenv==1.0.0
RUN pip install --no-cache-dir "pydantic<2.0"  # ⬅️ USE PYDANTIC v1!
RUN pip install --no-cache-dir alembic==1.13.0
RUN pip install --no-cache-dir python-jose[cryptography]==3.3.0
RUN pip install --no-cache-dir passlib[bcrypt]==1.7.4
RUN pip install --no-cache-dir requests==2.31.0

# Copy app
COPY . .

# Create simple startup script
RUN echo '#!/bin/bash\n\
set -e\n\
\n\
echo "🚀 Starting Trustra NG..."\n\
\n\
# Initialize database\n\
python -c "\n\
from app.database import engine, Base\n\
from app.models import user, escrow, revenue, playing_with_neon, dispute, risk_log\n\
Base.metadata.create_all(bind=engine)\n\
print(\"✅ Database tables created\")\n\
"\n\
\n\
# Start server\n\
uvicorn app.main:app --host 0.0.0.0 --port \$PORT --workers 1\n\
' > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]
