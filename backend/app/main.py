from fastapi import FastAPI
from app.database import init_db

app = FastAPI(title="Trustra-NG Backend")

# Initialize database tables with constraints
init_db()

@app.get("/")
async def root():
    return {"message": "Trustra-NG backend is live with AI & monetization ready!"}
