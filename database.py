from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


DATABASE_URL = "postgresql+psycopg://postgres:nagarajanvijay...@localhost:5432/contact_db"

engine = create_engine(DATABASE_URL)

print("DB Connected Successfully")

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()    