from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db, engine
from . import models
from .config import Settings

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

    