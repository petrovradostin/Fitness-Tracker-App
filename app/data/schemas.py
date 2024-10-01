from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class WorkoutBase(BaseModel):
    exercise: str
    duration: int
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    owner_id: int
    date_posted: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    workouts: List[Workout] = []

    class Config:
        from_attributes = True
