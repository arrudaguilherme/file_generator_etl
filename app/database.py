from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

DB_URL = "" # TO BE ADDED
engine = create_engine(url= DB_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine) # creates db session

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()