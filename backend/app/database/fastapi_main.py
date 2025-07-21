from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.orm_connection import SessionLocal
from app.database import models_orm

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create lead
@app.post("/leads")
def create_lead(name: str, email: str, phone: str, source: str, status: str, db: Session = Depends(get_db)):
    new_lead = models_orm.Lead(
        name=name,
        email=email,
        phone=phone,
        source=source,
        status=status
    )
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead

# Get all leads
@app.get("/leads")
def get_all_leads(db: Session = Depends(get_db)):
    leads = db.query(models_orm.Lead).all()
    return leads
