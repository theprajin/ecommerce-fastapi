from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.common.config import settings

# Set up database connection
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, echo=settings.DEBUG)

# Create session local and base model
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency injection for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Function to create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)
