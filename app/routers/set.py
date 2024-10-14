from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data import schemas
from services import sets_service
from data import database

set_router = APIRouter(prefix='/set', tags=['Set'])

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@set_router.get("/", response_model=List[schemas.Set])
def get_set(exercise_id: int, db: Session = Depends(get_db)):
    return sets_service.get_set_by_exercise(db, exercise_id)

@set_router.post("/", response_model=schemas.Set)
def create_set(set_number: int, exercise_id: int, db: Session = Depends(get_db)):
    return sets_service.create_set(db, set_number, exercise_id)