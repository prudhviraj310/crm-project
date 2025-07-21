from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace the below credentials with your MySQL Workbench credentials
DATABASE_URL = "mysql+pymysql://root:yourpassword@localhost:3306/yourdbname"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
