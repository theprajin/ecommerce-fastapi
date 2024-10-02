import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from src.common.config import settings

# Load .env file
load_dotenv()

# Set up database connection
DATABASE_URL = settings.DATABASE_URL
DATABASE_URL_ONLINE = os.getenv("DATABASE_URL_ONLINE")

# engine = create_engine(DATABASE_URL, echo=settings.DEBUG)
engine = create_engine(DATABASE_URL_ONLINE, echo=settings.DEBUG)

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
