from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Example: SQLite (for testing/development)
SQLALCHEMY_DATABASE_URL = "sqlite:///./crm.db"

# For PostgreSQL or MySQL (for production):
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # Only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
