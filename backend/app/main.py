from fastapi import FastAPI
from .admin import router as admin
from .webhook import router as webhook

app = FastAPI()

app.include_router(admin)
app.include_router(webhook)

@app.get("/")
def health():
    return {"status": "Trustra NG Live"}
