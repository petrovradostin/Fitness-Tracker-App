from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data import schemas
from services import workouts_service
from data import database
from data.security import get_current_user

workouts_router = APIRouter(prefix="/workouts", tags=["Workouts"])

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@workouts_router.post("/create", response_model=schemas.WorkoutResponse)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return workouts_service.create_workout(db=db, workout=workout, user_id=current_user.id)


@workouts_router.get("/", response_model=List[schemas.Workout])
def get_workouts(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return workouts_service.get_user_workouts(db=db, user_id=current_user.id)
