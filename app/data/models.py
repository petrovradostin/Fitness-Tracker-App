from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    workouts = relationship("Workout", back_populates="owner")

class Workout(Base):
    id = Column(Integer, primary_key=True, index=True)
    exercise = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # minutes
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)
    date_posted = Column(DateTime, default=datetime.now)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship("User", back_populates="workouts")
