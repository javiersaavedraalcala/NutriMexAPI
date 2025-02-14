from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/NutriMexAPI"

# Create sqlalchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()