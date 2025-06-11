from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.config.config import get_database

app = FastAPI()

@app.get("/")
def read_root(db: Session = Depends(get_database)):
    return {"message": "Conexão com SQLite funcionando"}
