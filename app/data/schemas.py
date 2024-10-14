from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class WorkoutBase(BaseModel):
    name: str
    description: str

class WorkoutCreate(WorkoutBase):
    name: str
    description: str

class Workout(WorkoutBase):
    id: int
    user_id: int
    date_posted: datetime

    class Config:
        from_attributes = True

class WorkoutResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True



class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    username: str
    email: str
    password: str

class User(UserBase):
    id: int
    workouts: List[Workout] = []

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True



class MuscleGroup(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ExerciseCreate(BaseModel):
    name: str
    muscle_group_id: int

class Exercise(BaseModel):
    name: str

    class Config:
        from_atributes = True



class SetCreate(BaseModel):
    set_number: int
    exercise_id: int

class Set(BaseModel):
    set_number: int

    class Config:
        from_atributes = True



class RepsCreate(BaseModel):
    reps: int
    weight: float
    set_id:int

class Reps(BaseModel):
    reps: int
    weight: float

    class Config:
        from_atributes = True
    