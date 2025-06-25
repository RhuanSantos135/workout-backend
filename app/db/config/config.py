from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

DATABASE_URL = "postgresql+psycopg2://rhuan_dev:AxR256396dd@localhost:5432/workout_db"

engine = create_engine(DATABASE_URL, pool_recycle=3600, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"An error occurred while connecting: {e}")
    finally:
        db.close()