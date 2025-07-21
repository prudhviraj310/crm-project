from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from orm_connection import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))

    leads = relationship("Lead", back_populates="user")
    deals = relationship("Deal", back_populates="user")
    tasks = relationship("Task", back_populates="user")


class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    status = Column(String(50))
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="leads")
    deals = relationship("Deal", back_populates="lead")
    tasks = relationship("Task", back_populates="lead")


class Deal(Base):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    value = Column(DECIMAL(10, 2))
    stage = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

    lead_id = Column(Integer, ForeignKey("leads.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    lead = relationship("Lead", back_populates="deals")
    user = relationship("User", back_populates="deals")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    due_date = Column(DateTime)
    status = Column(String(50))

    lead_id = Column(Integer, ForeignKey("leads.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    lead = relationship("Lead", back_populates="tasks")
    user = relationship("User", back_populates="tasks")
