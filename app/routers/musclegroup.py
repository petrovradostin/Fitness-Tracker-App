from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.data import schemas
from services import musclegroups_service
from data import database

musclegroup_router = APIRouter(prefix='/musclegroup', tags=['Muscle Group'])

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@musclegroup_router.get("/", response_model=List[schemas.MuscleGroup])
def get_all_muscle_groups(db: Session = Depends(get_db)):
    muscle_groups = musclegroups_service.get_muscle_groups(db)
    return muscle_groups

@musclegroup_router.get("/group", response_model=List[schemas.MuscleGroup])
def get_muscle_group(name: str, db: Session = Depends(get_db)):
    musclegroup = musclegroups_service.get_muscle_group_by_name(db, name=name)
    if not musclegroup:
        raise HTTPException(status_code=404, detail="Muscle group not found")
    return musclegroup

@musclegroup_router.post("/create", response_model=schemas.MuscleGroup)
def create_muscle_group(name: str, db: Session = Depends(get_db)):
    return musclegroups_service.create_muscle_group(db, name)