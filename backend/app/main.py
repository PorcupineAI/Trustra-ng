from fastapi import FastAPI

from app.routes.users import router as users_router
from app.routes.escrow import router as escrow_router
from app.routes.webhook import router as webhook_router

app = FastAPI(title="Trustra NG API")

app.include_router(users_router)
app.include_router(escrow_router)
app.include_router(webhook_router)
