from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Trustra NG",
    version="1.0.0",
    docs_url="/docs" if os.getenv("ENVIRONMENT") != "production" else None,
    redoc_url="/redoc" if os.getenv("ENVIRONMENT") != "production" else None,
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers
from app.routes import auth, users, escrow, admin, webhook, dispute

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(escrow.router)
app.include_router(admin.router)
app.include_router(webhook.router)
app.include_router(dispute.router)

@app.get("/")
def root():
    return {"status": "Trustra NG API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "Trustra NG"}
