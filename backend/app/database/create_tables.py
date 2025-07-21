from orm_connection import engine
from orm_models import Base

Base.metadata.create_all(bind=engine)
print("✅ All tables created successfully using SQLAlchemy!")
