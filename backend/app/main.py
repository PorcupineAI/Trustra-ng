from fastapi import FastAPI
from app.routes import users, escrow, admin

app = FastAPI(title="Trustra NG")

app.include_router(users)
app.include_router(escrow)
app.include_router(admin)

@app.get("/")
def root():
    return {"status": "Trustra NG live"}
