from fastapi import FastAPI
from routes import users

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["Users"])


@app.get("/")
def root():
    return {"status": "API running"}