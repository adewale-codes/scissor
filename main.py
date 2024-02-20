from fastapi import FastAPI, Depends, HTTPException
from app.routes import url_shortener
from app.db.database import SessionLocal

app = FastAPI()

app.include_router(url_shortener.router)

@app.get("/")
def root():
    return {"message": "Hello World! Welcome to my scissors app"}