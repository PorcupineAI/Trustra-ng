from fastapi import FastAPI
from app.routes import auth, escrow, admin

app = FastAPI()

app.include_router(auth.router)
app.include_router(escrow.router)
app.include_router(admin.router)
