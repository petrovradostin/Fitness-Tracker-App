from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from data import database
from data import schemas
from services import reps_service

reps_router = APIRouter(prefix='/reps', tags=['Reps'])

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@reps_router.get("/", response_model=List[schemas.Reps])
def get_reps(set_id: int, db: Session = Depends(get_db)):
    return reps_service.get_reps_by_set(db, set_id)

@reps_router.post("/create", response_model=schemas.Reps)
def create_reps(reps: int, weight: float, set_id: int, db: Session = Depends(get_db)):
    return reps_service.create_reps(db, reps, weight, set_id)
