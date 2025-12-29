from fastapi import FastAPI
from app.routes import users, escrow, webhook

app = FastAPI(title="Trustra Digital Protocol API")

app.include_router(users.router)
app.include_router(escrow.router)
app.include_router(webhook.router)
