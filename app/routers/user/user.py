from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.config.config import get_database
import logging

router = APIRouter()

@router.get("/user")
async def read_root(db: Session = Depends(get_database)):
    try:
        query = text("SELECT * FROM wkuser")
        result = db.execute(query)

        response = {
            'usuarios': result[0]
        }
        return response
    except Exception as e:
        logging.error(f"Erro na conexão: {e}")
        return {"error": "Erro ao buscar usuários"}