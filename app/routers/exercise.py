from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from data import schemas
from services import exercises_service
from data import database

exercise_router = APIRouter(prefix='/exercises', tags=['Exercises'])

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@exercise_router.get("/", response_model=List[schemas.Exercise])
def get_exercises(muscle_group_id: int, db: Session = Depends(get_db)):
    exercises = exercises_service.get_exercises(db, muscle_group_id)
    return exercises

@exercise_router.post("/create", response_model=schemas.Exercise)
def create_exercise(name: str, muscle_group_id: int, db: Session = Depends(get_db)):
    return exercises_service.create_exercise(db, name, muscle_group_id)
