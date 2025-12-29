from fastapi import FastAPI
from app.routes import users, escrow, webhook

app = FastAPI(title="Trustra NG API")

app.include_router(users)
app.include_router(escrow)
app.include_router(webhook)
