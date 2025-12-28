from app.routes import admin
app.include_router(admin.router)
from fastapi import FastAPI
from app.database import init_db
from app.routes import users, escrow, webhook

app = FastAPI(title="Trustra Digital Protocol")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(users.router)
app.include_router(escrow.router)
app.include_router(webhook.router)

@app.get("/")
def health():
    return {"status": "Trustra-NG running"}
